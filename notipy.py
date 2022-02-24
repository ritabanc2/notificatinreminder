import time
from plyer import notification
if __name__ == '__main__':
    notification.notify(
        title="Stand up",
        message="sitting too much is not good for health",
        timeout=5
    )