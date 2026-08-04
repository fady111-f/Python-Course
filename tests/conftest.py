"""
Pytest configuration and shared fixtures for Python Course Mastery
"""
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.resolve()
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
