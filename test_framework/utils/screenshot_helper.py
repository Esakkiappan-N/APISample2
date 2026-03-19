import allure
import os
from datetime import datetime


# ─────────────────────────────────────────
# Screenshots folder path
# ─────────────────────────────────────────
BASE_DIR        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR  = os.path.join(BASE_DIR, "screenshots")

# Create screenshots folder if not exists
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)


def take_screenshot(driver, name):
    """
    Takes screenshot and:
    1. Saves as PNG file in screenshots/ folder
    2. Attaches to Allure report
    """
    # Build filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename  = f"{name}_{timestamp}.png"
    filepath  = os.path.join(SCREENSHOT_DIR, filename)

    # Save screenshot as file
    driver.save_screenshot(filepath)
    print(f"📸 Screenshot saved: {filepath}")

    # Attach to allure report
    with open(filepath, "rb") as f:
        allure.attach(
            f.read(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )