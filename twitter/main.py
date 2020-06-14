import logging.config
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

from harvester import Harvester


def main():
    keywords_list = ["bitcoin", "gold"]
    harvester = Harvester()
    harvester.harvest(keywords=keywords_list)


if __name__ == '__main__':
    main()
