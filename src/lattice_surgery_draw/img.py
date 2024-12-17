import os 
from functools import partial

from lattice_surgery_draw.primitives import tikz_obj 

lib_path = os.path.dirname(__file__).replace('\\', '/') + '/tikz/'

patch_path = lib_path + 'derived/surface_code'
SurfaceCodePatch = partial(tikz_obj.TikzImg, path=patch_path, height=3, width=3) 

patch_path = lib_path + 'derived/surface_code_double'
SurfaceCodePatchWide = partial(tikz_obj.TikzImg, path=patch_path, height=3, width=6) 
