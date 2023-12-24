import threading

class PrinterService:
    _thread_lock = threading.Lock()
    _unique_instance = None

    def __new__(cls):
        with cls._thread_lock:
            # Check if there is an instance already created
            if cls._unique_instance is None:
                cls._unique_instance = super(PrinterService, cls).__new__(cls)
        return cls._unique_instance
