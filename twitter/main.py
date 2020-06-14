import logging

from harvester import Harvester

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')
keywords_list = ["bitcoin", "gold"]

if __name__ == '__main__':
    logging.info('Started')
    harvester = Harvester(logging=logging)
    harvester.harvest(keywords=keywords_list)
    logging.info('Finished')
