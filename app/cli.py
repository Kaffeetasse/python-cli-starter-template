import logging
import time
from argparse import ArgumentParser

# noinspection PyUnresolvedReferences
from requests.packages import urllib3

from app.custom_formatter import CustomFormatter


def main():
    start_time = time.process_time()

    # define CLI Arguments
    parser = ArgumentParser(prog="cli")
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Set log level eg. DEBUG, INFO, WARNING",
    )
    args = parser.parse_args()

    # handle arguments
    loglevel = args.log_level

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    ch.setFormatter(CustomFormatter())
    logging.basicConfig(handlers=[ch], level=logging.DEBUG, force=True)
    logging.captureWarnings(True)
    logger = logging.getLogger("main")
    urllib3_logger = logging.getLogger("urllib3")
    urllib3_logger.setLevel(logging.CRITICAL)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    logger.info(f"START")

    # ADD CODE HERE

    end_time = time.process_time() - start_time
    logger.info(f"DONE, elapsed: {end_time:0.3f}s")


if __name__ == "__main__":
    main()
