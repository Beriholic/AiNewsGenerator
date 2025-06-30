import os
from dotenv import load_dotenv

load_dotenv()

ZHIPU_API_KEK: str = ""
ZHIPU_MODEL: str = ""
SERPER_API_KEY: str =""
MAX_REVIEW_CYCLES: int = 0
OUTPUT_BASE: str = ""

def load():
    global ZHIPU_API_KEY, ZHIPU_MODEL, SERPER_API_KEY, MAX_REVIEW_CYCLES, OUTPUT_BASE
    if os.getenv("ZHIPU_API_KEY") is None:
        raise Exception("ZHIPU_API_KEY is not set")
    if os.getenv("ZHIPU_MODEL") is None:
        raise Exception("ZHIPU_MODEL is not set")
    if os.getenv("SERPER_API_KEY") is None:
        raise Exception("SERPER_API_KEY is not set")
    if os.getenv("MAX_REVIEW_CYCLES") is None:
        raise Exception("MAX_REVIEW_CYCLES is not set")
    if os.getenv("OUTPUT_BASE") is None:
        raise Exception("OUTPUT_BASE is not set")

    ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY")
    ZHIPU_MODEL = os.getenv("ZHIPU_MODEL")
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    MAX_REVIEW_CYCLES = int(os.getenv("MAX_REVIEW_CYCLES"))
    OUTPUT_BASE = os.getenv("OUTPUT_BASE")

    if MAX_REVIEW_CYCLES < 0:
        raise Exception("MAX_REVIEW_CYCLES must be greater than 0")

    if not os.path.exists(OUTPUT_BASE):
        os.mkdir(OUTPUT_BASE)
