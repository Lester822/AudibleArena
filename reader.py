import time

LOG_PATH = 'C:\\Users\sasta\AppData\LocalLow\Wizards Of The Coast\MTGA\player.log'

def main():
    lines_read = 0
    while True:
        log_file = open('C:\\Users\sasta\AppData\LocalLow\Wizards Of The Coast\MTGA\player.log', 'r')
        contents = log_file.readlines()[lines_read:]
        lines_read += len(contents)
        if len(contents) > 0:
            return contents
main()