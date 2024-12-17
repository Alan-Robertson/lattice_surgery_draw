from lattice_surgery_draw.primitives.headers import Header, DefaultTexHeader, DefaultTikzHeader
from lattice_surgery_draw.primitives.style import DeclarativeStyle, DefaultDeclarativeStyle 


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
        header = None,
        style_decl=None
    ):

        if header is None:
            header = DefaultTikzHeader()
        self.header = header

        self.style_decl = DefaultDeclarativeStyle()
        super().__init__(*components)

    def get_header(self): 
        return self.header.get_header()  + str(self.style_decl) 

    def get_footer(self):
        return self.header.get_footer() 
