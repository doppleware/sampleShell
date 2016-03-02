from cloudshell.shell.core.driver_context import *
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
import tweepy


class SampleShellDriver (ResourceDriverInterface):
    
    def __init__(self):
        pass

    # Initialize the driver session, this function is called everytime a new instance of the driver is created
    # This is a good place to load and cache the driver configuration, initiate sessions etc.
    def initialize(self, context):              
        """
        :type context: cloudshell.shell.core.driver_context.InitCommandContext
        """
        return 'Finished initializing'

    # Destroy the driver session, this function is called everytime a driver instance is destroyed
    # This is a good place to close any open sessions, finish writing to log files

    def tweet(self, message):
        auth = tweepy.OAuthHandler('VqaHHwb0lYW7kq0EK8clEByFh','CsES4nNmXV6SS5vFIClck9dgzwK9y8SLAATqJExpkcA3FR9tLF')
        auth.set_access_token('15255909-XsJS1gJaee9wbHr1OnkcFMx4D0wGhC9c0Y7gZY7Ae','PgnhuBIXrDXQlZv8jj3fShDqsBENX9wyzPYVtOgeC9Uqe')
        api = tweepy.API(auth)
        api.update_status('Somepne is using my automated tweeting widget.')

        return 'Yeah, I\'m not going to let you tweet that'


    def cleanup(self):
        pass

    # An example command
    def example_command(self, context, user_param1, user_param2):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        """   
        result = self._helper_method(user_param1)
        return result
    
    # An example command that that supports cancellation
    def example_command_with_cancellation(self, context, cancellation_token, user_param1):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        :type cancellation_token: cloudshell.shell.core.driver_context.CancellationContext
        """
        result = self._helper_method(user_param1)

        return result 
    
    # private functions are always hidden
    def _helper_method(self,title):
        return "---====%s====---" % title
