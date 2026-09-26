import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, test_name):

        directory = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "screenshots"
        )

        os.makedirs(directory, exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = f"{test_name}_{timestamp}.png"

        path = os.path.join(directory, filename)

        driver.save_screenshot(path)

        return path