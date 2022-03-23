"""Automatically runs the main function inside boiler plate code that
    sets a breakpoint on error.

Example usage:

python run_main.py --main_filename p1_3_urlify

or

python run_main.py --main_filename p1_3_urlify.py
"""

import argparse
import importlib
import importlib.util
import os
import pdb
import sys
import traceback


def parse_main_filename():
    pargs = argparse.ArgumentParser()
    pargs.add_argument('--main_filename',
                       help="the filename where the main function is",
                       required=True)
    args = pargs.parse_args()
    return args.main_filename


def get_module(main_filename: str):
    if '.py' not in main_filename:
        main_filename = f"{main_filename}.py"
    dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(dir, main_filename)
    module_name = main_filename.replace('.py', '')
    spec = importlib.util.spec_from_file_location(
        module_name, full_path, submodule_search_locations=[])
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


if __name__ == '__main__':
    main_filename = parse_main_filename()
    try:
        module = get_module(main_filename)
        module.main()
    except Exception as e:
        print(e)
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
