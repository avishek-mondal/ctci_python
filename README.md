# Description

These are my solutions to the CTCI book. Heavily inspired by the original CTICI repositories [here](https://github.com/careercup/CtCI-6th-Edition-Python) and [here](https://github.com/careercup/CtCI-6th-Edition). I am not contributing to them because I also experiment with other features of python in this repository

# Special files
## tlog.py

tlog, or temporary log, is just a structlog global logger. I use it instead of print statements.

# run_main.py

This is so that I don't have to copy paste these lines of code -

```
except Exception as e:
        print(e)
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)

```
everytime I start a question. Example usage is `python run_main.py --main_filename c04/p4_8_first_common_ancestor.py`. If there is an error in the code, there will be a breakpoint at the point of the error.