import logging.config
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
import os

from harvester import Harvester


def main():
    parsed_keywords = os.environ['KEYWORDS'].split(",")
    harvester = Harvester()
    harvester.harvest(keywords=parsed_keywords)


if __name__ == '__main__':
    main()
