"""Logger class."""
from inspect import getframeinfo, stack


class Logger:
    """Logger class."""

    @staticmethod
    def get_caller_info() -> tuple[str, int]:
        """Get the caller function information.

        Returns:
            tuple[str, int]: _description_
        """
        caller = getframeinfo(stack()[2][0])
        filename: list[str] = caller.filename.split('\\')
        file: str = ''
        src_found: bool = False
        for name in filename:
            if name == 'src':
                src_found = True
                file = file + '\\' + name
            elif src_found:
                file = file + '\\' + name
            else:
                continue
        return (file, caller.lineno)

    @staticmethod
    def debug(message: str) -> None:
        """Debug level of logging."""
        file, lineno = Logger.get_caller_info()
        print('DEBUG - %s: line: %d - %s' % (file, lineno, message))

    @staticmethod
    def info(message: str) -> None:
        """Debug level of logging."""
        file, lineno = Logger.get_caller_info()
        print('INFO - %s: line: %d - %s' % (file, lineno, message))

    @staticmethod
    def critical(message: str) -> None:
        """Debug level of logging."""
        file, lineno = Logger.get_caller_info()
        print('CRITICAL - %s: line: %d - %s' % (file, lineno, message))

    @staticmethod
    def error(message: str) -> None:
        """Debug level of logging."""
        file, lineno = Logger.get_caller_info()
        print('ERROR - %s: line: %d - %s' % (file, lineno, message))
