import subprocess
from IoTuring.MyApp.SystemConsts.OperatingSystemDetection import OperatingSystemDetection as OsD


class DesktopEnvironmentDetection():
    @staticmethod
    def GetDesktopEnvironment() -> str:

        de = OsD.GetEnv('DESKTOP_SESSION')
        if not de:
            de = "base"
        return de

    @staticmethod
    def IsWayland() -> bool:
        return bool(
            OsD.GetEnv('WAYLAND_DISPLAY') or
            OsD.GetEnv('XDG_SESSION_TYPE') == 'wayland' or
            p = subprocess.run(['loginctl', "show-session $(awk '/tty/ {print $1}' <(loginctl)) -p Type | awk -F= '{print $2}'"])
            )
    @staticmethod
    def IsX11() -> bool:
        return bool(
            OsD.GetEnv('DISPLAY') and
            not DesktopEnvironmentDetection.IsWayland()
            )

    @staticmethod
    def CheckXsetSupport() -> None:
        """ Check if system supports xset. Raises exception if not supported """
        if not OsD.CommandExists("xset"):
            raise Exception("xset command not found!")
        else:
            # Check if xset is working:e
            p = subprocess.run(['xset', 'dpms'], capture_output=True, shell=False)
            if p.stderr:
                raise Exception(f"Xset dpms error: {p.stderr.decode()}")
            elif not OsD.GetEnv('DISPLAY'):
                raise Exception('No $DISPLAY environment variable!')

    @staticmethod
    def IsXsetSupported() -> bool:
        if DesktopEnvironmentDetection.IsWayland():
            return False
        try:
            DesktopEnvironmentDetection.CheckXsetSupport()
            return True
        except:
            return False

