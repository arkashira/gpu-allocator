import tkinter as tk
from policy_manager import PolicyManager

class UI:
    def __init__(self, master):
        self.master = master
        self.policy_manager = PolicyManager()
        self.policy_name_label = tk.Label(master, text="Policy Name:")
        self.policy_name_label.pack()
        self.policy_name_entry = tk.Entry(master)
        self.policy_name_entry.pack()
        self.policy_config_label = tk.Label(master, text="Policy Config:")
        self.policy_config_label.pack()
        self.policy_config_entry = tk.Entry(master)
        self.policy_config_entry.pack()
        self.add_policy_button = tk.Button(master, text="Add Policy", command=self.add_policy)
        self.add_policy_button.pack()
        self.get_policy_button = tk.Button(master, text="Get Policy", command=self.get_policy)
        self.get_policy_button.pack()
        self.update_policy_button = tk.Button(master, text="Update Policy", command=self.update_policy)
        self.update_policy_button.pack()
        self.delete_policy_button = tk.Button(master, text="Delete Policy", command=self.delete_policy)
        self.delete_policy_button.pack()

    def add_policy(self):
        policy_name = self.policy_name_entry.get()
        policy_config = self.policy_config_entry.get()
        self.policy_manager.add_policy(policy_name, policy_config)

    def get_policy(self):
        policy_name = self.policy_name_entry.get()
        policy = self.policy_manager.get_policy(policy_name)
        print(policy)

    def update_policy(self):
        policy_name = self.policy_name_entry.get()
        policy_config = self.policy_config_entry.get()
        self.policy_manager.update_policy(policy_name, policy_config)

    def delete_policy(self):
        policy_name = self.policy_name_entry.get()
        self.policy_manager.delete_policy(policy_name)

root = tk.Tk()
my_ui = UI(root)
root.mainloop()