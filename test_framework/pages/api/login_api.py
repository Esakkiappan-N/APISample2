name: Full Test Automation (API + Web + Mobile)

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    # =========================
    # ✅ 1. CHECKOUT CODE
    # =========================
    - name: Checkout code
      uses: actions/checkout@v3

    # =========================
    # ✅ 2. PYTHON SETUP
    # =========================
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    # =========================
    # ✅ 3. INSTALL DEPENDENCIES
    # =========================
    - name: Install dependencies
      run: |
        pip install -r test_framework/requirements.txt
        pip install playwright pytest allure-pytest

    # =========================
    # ✅ 4. INSTALL PLAYWRIGHT
    # =========================
    - name: Install Playwright Browsers
      run: |
        python -m playwright install --with-deps

    # =========================
    # ✅ 5. RUN API + WEB TESTS
    # =========================
    - name: Run API & Web Tests
      run: |
        pytest test_framework/tests/api test_framework/tests/web --alluredir=allure-results

    # ✅ DEBUG: Upload screenshots if failed
    - name: Upload Debug Screenshots
      uses: actions/upload-artifact@v3
      if: failure()
      with:
        name: screenshots
        path: "*.png"

    # =========================
    # 📱 MOBILE SETUP STARTS
    # =========================

    # =========================
    # ✅ 6. JAVA
    # =========================
    - name: Setup Java
      uses: actions/setup-java@v3
      with:
        distribution: 'temurin'
        java-version: '17'

    # =========================
    # ✅ 7. ANDROID SDK
    # =========================
    - name: Setup Android SDK
      uses: android-actions/setup-android@v3

    # =========================
    # ✅ 8. INSTALL SDK TOOLS
    # =========================
    - name: Install Android SDK Components
      run: |
        yes | sdkmanager --licenses
        sdkmanager --install "platform-tools" "emulator" "system-images;android-30;google_apis;x86_64"

    # =========================
    # ✅ 9. CREATE EMULATOR
    # =========================
    - name: Create Emulator
      run: |
        echo "no" | avdmanager create avd -n test -k "system-images;android-30;google_apis;x86_64" --force

    # =========================
    # ✅ 10. START EMULATOR (FIXED PATH)
    # =========================
    - name: Start Emulator
      run: |
        export ANDROID_SDK_ROOT=$ANDROID_HOME
        nohup $ANDROID_HOME/emulator/emulator -avd test -no-window -no-audio -no-boot-anim -gpu swiftshader_indirect &
        adb wait-for-device

        echo "Waiting for emulator to boot..."
        until adb shell getprop sys.boot_completed | grep "1"; do
          sleep 5
        done

        adb shell input keyevent 82
        adb devices

    # =========================
    # ✅ 11. NODE SETUP
    # =========================
    - name: Setup Node
      uses: actions/setup-node@v3
      with:
        node-version: '20'

    # =========================
    # ✅ 12. INSTALL APPIUM
    # =========================
    - name: Install Appium
      run: |
        npm install -g appium
        appium driver install uiautomator2

    # =========================
    # ✅ 13. START APPIUM
    # =========================
    - name: Start Appium Server
      run: |
        nohup appium &
        sleep 20

    # =========================
    # ✅ 14. INSTALL APK
    # =========================
    - name: Install APK
      run: |
        adb install -r tapps/app-release-4-3-26.apk

    # =========================
    # ✅ 15. RUN MOBILE TESTS
    # =========================
    - name: Run Mobile Tests
      run: |
        pytest test_framework/tests/mobile --alluredir=allure-results

    # =========================
    # ✅ 16. UPLOAD ALLURE RESULTS
    # =========================
    - name: Upload Allure Results
      uses: actions/upload-artifact@v3
      with:
        name: allure-results
        path: allure-results
