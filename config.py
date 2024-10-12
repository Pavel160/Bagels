from dotenv import load_dotenv
import os

load_dotenv()

NUM_DIGITS = int(os.getenv('NUM_DIGITS', 3))
MAX_GUESSES = int(os.getenv('MAX_GUESSES', 10))
