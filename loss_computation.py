import torch
from typing import Tuple, Union, Dict,Any
import torch.nn as nn
from transformers import PreTrainedModel as PretrainedModel
def compute_loss(
        self,
        model : Union[PretrainedModel, nn.Module],
        inputs: Dict[str, Union[torch.Tensor, Any]],
        return_outputs = False,
    ) -> Union[torch.Tensor, Tuple[torch.Tensor, Dict[str, torch.Tensor]]] :
    rewards_chosen = model(
        input_ids = inputs["input_ids_chosen"],
        attention_mask = inputs["attention_mask_chosen"],
        return_dict = True,
    )['logits']
    rewards_rejected = model(
        input_ids = inputs["input_ids_rejected"],
        attention_mask = inputs["attention_mask_rejected"],
        return_dict = True,
    )["logits"]
    loss = -nn.functional.logsigmoid(rewards_chosen - rewards_rejected).mean()
    if return_outputs:
        return loss, {
            "rewards_chosen": rewards_chosen,
            "rewards_rejected": rewards_rejected,
        }
    else:
        return loss
        