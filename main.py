import ctypes,os,logging

class RunAsAdmin:
    _run_file_path = None

    def __init__(self, FilePath, log_file_path):
        self._run_file_path = os.path.abspath(FilePath)
        self.log_file = os.path.abspath(log_file_path)

    def execute(self):
        try:
            hinstance = ctypes.windll.shell32.ShellExecuteW(None, "runas", self._run_file_path, None, None, 1)
            if hinstance <= 32:
                logging.basicConfig(filename=self.log_file, level=logging.DEBUG)
                logging.error(f"Failed to execute with admin privileges. Return code: {hinstance}")
            else:
                logging.basicConfig(filename=self.log_file, level=logging.DEBUG)
                logging.info("Successfully executed with admin privileges.")
        except Exception as e:
            logging.basicConfig(filename=self.log_file, level=logging.DEBUG)
            return False
        return True

# Example usage
if __name__ == "__main__":
    file_path = "C:\Windows\System32\cmd.exe"  # Replace this with the actual file path
    log_file_path = os.path.join(os.getcwd(), "execution_log.log")
    runner = RunAsAdmin(file_path, log_file_path)
    runner.execute()