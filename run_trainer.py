import sys

sys.dont_write_bytecode = True

import torch
import os
from core.config import Config
from core import Trainer

def main(rank, config):
    trainer = Trainer(rank, config)
    trainer.train_loop()

if __name__ == "__main__":
    # config = Config("./config/finetune.yaml").get_config_dict()
    config = Config("./config/lucir.yaml").get_config_dict()

    if config["n_gpu"] > 1:
        pass
        os.environ["CUDA_VISIBLE_DEVICES"] = config["device_ids"]
        # torch.multiprocessing.spawn(main, nprocs=config["n_gpu"], args=(config,))
    else:
        main(0, config)