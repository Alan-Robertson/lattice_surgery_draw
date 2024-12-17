from lattice_surgery_draw.primitives.composers import Composer 

class Region(Composer):
    def __init__(self, 
        x_0, 
        y_0,    
        x_1, 
        y_1, 
        region_style=None,
        *components):
            
        region_obj = TikzRectangle(x_0, y_0, x_1, y_1, tikz_style=region_style)  
        super().__init__(region_obj, *components)
        
         
