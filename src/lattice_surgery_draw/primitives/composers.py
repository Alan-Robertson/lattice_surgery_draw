from lattice_surgery_draw.primitives.headers import Header, DefaultTexHeader, DefaultTikzHeader
from lattice_surgery_draw.primitives.style import DeclarativeStyle, DefaultDeclarativeStyle 
from lattice_surgery_draw.primitives.tikz_obj import TikzBoundingBox 



class Composer(Header):
    '''
        Basic composition object
        Takes lists of objects and maps str over them 
    '''
    def __init__(
        self,
        *components
        ):
        self._tikz_frames = list(components)

    def append(self, tikz_frame, index=None):
        if index is None: 
            self.tikz_frames.append(tikz_frame) 

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        tex_str = self.get_header()
        for frame in self._tikz_frames: 
            tex_str += str(frame)
        tex_str += self.get_footer() 
        return tex_str

    def get_header(self):
        return ""

    def get_footer(self):
        return ""


class TexFile(Composer):
    '''
        Tex file composer
        Takes a tex header object
    '''
    def __init__(self, *tikz_frames, header=None):
        if header is None:
            header = DefaultTexHeader()
        self.header = header 
        super().__init__(*tikz_frames)

    def get_header(self):
        return self.header.get_header()

    def get_footer(self):
        return self.header.get_footer()


class TikzFrame(Composer):
    '''
        TikzFrame composer
    '''
    def __init__(
        self,
        *components,
        x_0 = None,
        y_0 = None,
        x_1 = None,
        y_1 = None,
        header = None,
        style_decl=None
    ):

        if header is None:
            header = DefaultTikzHeader()
        self.header = header

        if x_0 is not None:
            bounding_box = tuple(
                TikzBoundingBox(
                    x_0, y_0, x_1, y_1
                )
            )
        else:
            bounding_box = tuple() 

        self.style_decl = DefaultDeclarativeStyle()
        super().__init__(*bounding_box, *components)

    def get_header(self): 
        return self.header.get_header()  + str(self.style_decl) 

    def get_footer(self):
        return self.header.get_footer() 
