import csv
import os
from urllib import urlopen
from datetime import date, datetime

class HAProxy_test:
  def __init__( self, agentConfig, logger, rawConfig ):
    logger.info("HAProxy - initializing")
    self.agent_config = agentConfig
    self.logger = logger
    self.raw_config = rawConfig
    self.csv_filepath = '/etc/sd-agent/response.csv'

    logger.info("HAProxy - initialized")

  def debug( self ):
    self.logger.info("HAProxy - agentConfig keys")
    self.logger.info( self.agent_config.keys() )
    self.logger.info("HAProxy - rawConfig keys")
    self.logger.info( self.raw_config.keys() )
    self.logger.info({
      'date': datetime.today(),
      'agentConfig': self.agent_config,
      'rawConfig': self.raw_config
    })

  def main( self ):
    self.logger.info("HAProxy - inside main()")

    if 'haproxy_url' not in self.raw_config['Main']:
      self.logger.error("HAProxy - haproxy_url required in /etc/sd-agent/config.cfg but missing")
      return False

    self.status_page_url = self.raw_config['Main']['haproxy_url'] + "/;csv;norefresh"
    self.getStatusPage()
    self.logger.info("HAProxy - status page")
    self.logger.info(self.raw_status)
    self.parseStatusPage()
    self.logger.info("HAProxy - parsed status page")
    self.logger.info(self.parsed_status)

  def getStatusPage( self ):
    response = urlopen(self.status_page_url).read()
    self.raw_status = response[2:]
    f = open( self.csv_filepath, 'w')
    f.write(self.raw_status)

  def parseStatusPage( self ):
    self.parsed_status = []
    with open( self.csv_filepath, 'rb') as f:
      reader = csv.DictReader(f)

      for row in reader:
        self.parsed_status.append(row)

  def clean_url( self ):
    return

  def run(self):
    self.logger.info("HAProxy - run()")
    self.logger.info("Running in directory: "+ os.getcwd() + " in path "+ os.path.realpath( __file__ ) )
    self.debug()

    try:
      self.logger.info("HAProxy - running main()")
      return self.main()
    except Exception, e:
      import traceback
      self.logger.error('HAProxy - failure \n'+ traceback.format_exc())