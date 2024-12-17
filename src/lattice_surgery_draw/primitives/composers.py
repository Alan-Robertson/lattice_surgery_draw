from lattice_surgery_draw.primitives.header_tex import Header 
from lattice_surgery_draw.primitives.header_tex import DefaultTexHeader

class Composer(Header):
    '''
        Basic composition object
        Takes lists of objects and maps str over them 
    '''
    def __init__(
        self,
        *components
        )
    self.tikz_frames = list(self.tikz_frames)

    def append(self, tikz_frame, index=None):
        if index is None: 
            self.tikz_frames.append(tikz_frame) 

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        tex_str = self.header.get_header()
        for frame in tikz_frames: 
            tex_str += str(frame)
        tex_str += self.header.get_footer() 

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

    def get_header():
        return self.header.get_header()

    def get_footer():
        return self.footer.get_footer()

class TikzFrame(Composer):
    '''
        TikzFrame composer
    '''
    def __init__(self,  style_decl=None):
        self.style_decl = DefaultStyleDecl()
