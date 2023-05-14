import numpy as np


class PrintLogStatsCollect:
    tag: str
    log: np.ndarray
    cursor: int

    def __init__(self, tag: str):
        self.tag = tag
        self.log = np.zeros(200, dtype=np.int32)
        self.cursor = 0

    def print_remain_stats(self):
        if len(self.log) > 0:
            print(f"{self.tag}: {self.log}")
    
    def add(self, value: int):
        if self.cursor >= len(self.log):
            print(f"{self.tag}: {self.log}")
            self.log = np.zeros(200, dtype=np.int32)
            self.cursor = 0
        self.log[self.cursor] = np.int32(value)
