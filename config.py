import os
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
from web_and_mobile_pikabu_tests.utils import paths


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv('REMOTE_URL')
    device_name: str = os.getenv('DEVICE_NAME')
    appName: str = os.getenv('APP_NAME')
    appWaitActivity: str = os.getenv('APP_WAIT_ACTIVITY')
    app_local: str = paths.abs_path_from_project(os.getenv('APP'))
    app_bstack: str = os.getenv('APP')
    platformName: str = os.getenv('PLATFORM_NAME')
    platformVersion: str = os.getenv('PLATFORM_VERSION')
    userName: str = os.getenv('USER_NAME')
    accessKey: str = os.getenv('ACCESS_KEY')
    udid: str = os.getenv('UDID')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'local_emulator':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)
            options.set_capability('udid', self.udid)

        if context == 'real_local':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_local)
            options.set_capability('udid', self.udid)

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformName', self.platformName)
            options.set_capability('platformVersion', self.platformVersion)
            options.set_capability('appWaitActivity', self.appWaitActivity)
            options.set_capability('app', self.app_bstack)
            options.set_capability(
                'bstack:options', {
                    'projectName': 'Pikabu',
                    'buildName': 'Pikabu',
                    'sessionName': 'Pikabu',
                    'userName': self.userName,
                    'accessKey': self.accessKey,
                },
            )

        return options


config = Config(context="local_emulator")
