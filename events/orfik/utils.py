import io
import base64
import random

def jitter(iterable):
    return [i + ((1 if random.random() > 0.5 else -1) *
        random.random() * 0.05) for i in iterable]
