import subprocess

class FabricEnvInit:
    def __init__(self, vals):
        """init variables"""
        self.vals = vals

    def get_env_hosts(self):
        return self.vals['server_external_ip']

    def get_env_user(self):
        return self.vals['server_admin']

    def get_env_password(self):
        return self.vals['server_password']

    def get_env_port(self):
        return self.vals['server_port']
