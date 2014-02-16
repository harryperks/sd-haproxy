import csv
from datetime import date

class HAProxy_test:
  def __init__( self, agentConfig, logger, rawConfig ):
    logger.info("HAProxy - initializing")
    self.agentConfig = agentConfig
    self.logger = logger
    self.rawConfig = rawConfig
    logger.info("HAProxy - initialized")
    logger.debug({
      date: datetime.today(),
      agentConfig: self.agentConfig,
      rawConfig: self.rawConfig
    })

  def main( self ):
    self.logger.info("HAProxy - inside main()")
    return { success: true, agentConfig: self.agentConfig, rawConfig: self.rawConfig }

  def run(self):
    try:
      self.logger.info("HAProxy - running main()")
      return self.main()
    except Exception, e:
      import traceback
      self.logger.error('HAProxy - failure \n'+ traceback.format_exc())
    finally:
      self.logger.info("HAProxy - routine complete")
      return "Will this text be outputted to the command line?"
