import os
os.environ['KIVY_NO_ARGS'] = '1'
os.environ["KCFG_KIVY_LOG_LEVEL"] = "warning"

# for backward compatibility
from katrain.__main__ import run_app

run_app()

