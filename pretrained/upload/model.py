''' Dou Dizhu DMC model
'''
import os

import rlcard
from rlcard.models.model import Model as BaseModel

class Model(BaseModel):
    ''' A pretrained model on Dou Dizhu with DMC
    '''

    def __init__(self, resource_dir):
        ''' Load pretrained model
        '''
        import torch

        device = torch.device('cpu')

        model_dir = os.path.join(resource_dir, 'models')
        self.dmc_agents = []
        for i in range(3):
            model_path = os.path.join(model_dir, str(i)+'.pth')
            agent = torch.load(model_path, map_location=device)
            agent.set_device(device)
            self.dmc_agents.append(agent)

    @property
    def agents(self):
        ''' Get a list of agents for each position in a the game
        Returns:
            agents (list): A list of agents
        Note: Each agent should be just like RL agent with step and eval_step
              functioning well.
        '''
        return self.dmc_agents
