"""Logger class."""
from inspect import getframeinfo, stack


class Logger:
    """Logger class."""

    @staticmethod
    def debug(message: str) -> None:
        """Debug level of logging."""
        caller = getframeinfo(stack()[1][0])
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

        print('DEBUG - %s: line: %d - %s' % (file, caller.lineno, message))

    @staticmethod
    def info(message: str) -> None:
        """Debug level of logging."""
        caller = getframeinfo(stack()[1][0])
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
        print('INFO - %s: line: %d - %s' % (file, caller.lineno, message))

    @staticmethod
    def critical(message: str) -> None:
        """Debug level of logging."""
        caller = getframeinfo(stack()[1][0])
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
        print('CRITICAL - %s: line: %d - %s' % (file, caller.lineno, message))

    @staticmethod
    def error(message: str) -> None:
        """Debug level of logging."""
        caller = getframeinfo(stack()[1][0])
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
        print('ERROR - %s: line: %d - %s' % (file, caller.lineno, message))
