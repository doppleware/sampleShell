from cloudshell.shell.core.driver_context import *
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface


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

    def special_command (self, context):
        """
        :type context: cloudshell.shell.core.driver_context.ResourceCommandContext
        """

        return ""

    # private functions are always hidden
    def _helper_method(self,title):
        return "---====%s====---" % title

    def get_inventory(self, context):
        """
        :type context: cloudshell.shell.core.driver_context.AutoLoadCommandContext
        """
        # example autoload return results
        resources = [AutoLoadResource('Generic Chassis', 'Chassis 1', '1'),
                  AutoLoadResource('Generic Module', 'Module 1', '1/1'),
                  AutoLoadResource('Generic Port', 'Port 1', '1/1/1')]

        attributes = [
           AutoLoadAttribute('', 'Location', 'Santa Clara Lab'),
           AutoLoadAttribute('', 'Model', 'Catalyst 3850'),
           AutoLoadAttribute('', 'Vendor', 'Cisco'),
           AutoLoadAttribute('1', 'Serial Number', 'JAE053002JD'),
           AutoLoadAttribute('1', 'Model', 'WS-X4232-GB-RJ'),
           AutoLoadAttribute('1/1', 'Model', 'WS-X4233-GB-EJ'),
           AutoLoadAttribute('1/1', 'Serial Number', 'RVE056702UD'),
           AutoLoadAttribute('1/1/1', 'IPv4 Address', '192.168.10.7')
        ]

        result = AutoLoadDetails(resources, attributes)
        return result
