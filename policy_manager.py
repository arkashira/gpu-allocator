class PolicyManager:
    def __init__(self):
        self.policies = {}

    def add_policy(self, policy_name, policy_config):
        self.policies[policy_name] = policy_config

    def get_policy(self, policy_name):
        return self.policies.get(policy_name)

    def update_policy(self, policy_name, policy_config):
        if policy_name in self.policies:
            self.policies[policy_name] = policy_config
        else:
            raise ValueError("Policy does not exist")

    def delete_policy(self, policy_name):
        if policy_name in self.policies:
            del self.policies[policy_name]
        else:
            raise ValueError("Policy does not exist")