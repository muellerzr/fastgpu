from fastcore.all import *
from fastscript.core import call_parse,Param
from .core import *

@call_parse
def fastgpu_poll(
    # Path containing `to_run` directory
    path:str='.',
    # Exit when `to_run` is empty
    exit:int=1,
):
    "Poll `path` for scripts using `ResourcePoolGPU.poll_scripts`"
    rp = ResourcePoolGPU(path=path)
    rp.poll_scripts(exit_when_empty=exit)

