from dataclasses import dataclass


@dataclass
class AIResult:
        Chunks: list
        TotalChunks: int
        EstimatedTotalTimeSeconds: float
        EstimatedMinutes: float

@dataclass
class AIResponseModel:
        OriginalFileName:str
        StoredFileName:str
        SavedTo:str
        AIResult: AIResult
        ContentSize:int=0
        
        
