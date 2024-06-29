from psutil import boot_time, cpu_percent
from datetime import datetime as Date
from logger import Logger as logger
from vish_monitor import VishMonitor


if "__main__" == __name__:
    logger = logger('vish_monitor.log')
    try:
        logger.log("Starting VishMonitor...")
        monitor = VishMonitor(logger=logger)
        monitor.start()
    except KeyboardInterrupt:
        logger.to_console("\n")
        logger.warn("KeyboardInterrupt detected. Exiting...")
        monitor.stop()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        logger.log("Shutdown complete.")