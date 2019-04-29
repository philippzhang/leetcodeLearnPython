#!/usr/bin/python3
from leetcode.base.Utilitys import Utilitys
from leetcode.base.CallBack import CallBack
import os


class Main(CallBack):
    def __init__(self):
        pass


if __name__ == "__main__":
    Utilitys.test(Main, os.getcwd())
