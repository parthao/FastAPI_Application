from dataclasses import dataclass

@dataclass
class AIParam:
        max_length:int=64
        num_return_sequences:int=10
        do_sample:bool=True
        top_k:int=50
        top_p:float=0.95
        temperature:float=0.8