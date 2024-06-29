from psutil import cpu_percent

from logger import Logger


class VishMonitor:
    def __init__(self, logger: Logger):
        self.interval = 0.1  # setting 0.1 for high accuracy
        self.logger = logger    
        self._running = True

    def start(self):
        self._running = True
        self.logger.log("Monitoring CPU...")
        while self._running:
            current_cpu_percent = cpu_percent(interval=self.interval)
            if current_cpu_percent > 80:
                self.logger.log(self.__get_alert_string(current_cpu_percent))
                
    def stop(self):
        self._running = False
        self.logger.log("Stopped monitoring CPU.")

    def set_interval(self, interval):
        self.interval = interval

    def __get_alert_string(self, current_cpu_percent):
        return f"Alert! CPU usage exceeds threshold: {current_cpu_percent}%"

    def __str__(self):
        return (
            "VishMonitor(vish="
            + str(self.vish)
            + ", monitor="
            + str(self.monitor)
            + ")"
        )
