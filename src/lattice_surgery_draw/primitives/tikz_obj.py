import abc

from lattice_surgery_draw.primitives.style import TikzStyle 
from lattice_surgery_draw.primitives.utils import tikz_sanitise 

def style_compose(fn):
    '''
        Style composition decorator
    '''
    def _wrap(self, *args, **kwargs):
        style = self.style(*args, **kwargs)
        return fn(self, style)
    return _wrap 


class TikzObj(abc.ABC):
    def __init__(
        self,
        tikz_style : TikzStyle,
        key : str = None
    ):
        if key is None:
            key = str(hex(id(self)))
        if tikz_style is None:
            tikz_style = TikzStyle()
        self._key = key
        self._style = tikz_style 

    def __call__(self, *args, **kwargs):
        return self.draw(*args, **kwargs) 

    def __repr__(self, *args, **kwargs):
        return self.draw(*args, **kwargs)

    def style(self, *args, **kwargs): 
        return self._style(*args, **kwargs)


class TikzRectangle(TikzObj):
    '''
        Rectangle object
    '''

    def __init__(
        self,
        x_0 : float,
        y_0 : float,
        x_1 : float,
        y_1 : float,
        tikz_style : TikzStyle = None,
        key : str = None
    ):
        self.x_0 = x_0
        self.y_0 = y_0
        self.x_1 = x_1
        self.y_1 = y_1
        super().__init__(tikz_style, key)

    @style_compose
    def draw(self, style):
        return f"""\
\\draw[{str(style)}]\
({self.x_0}, {self.y_0}) \
rectangle \
({self.x_1}, {self.y_1});
""" 

class TikzCircle(TikzObj):
    '''
       Circle Object 
    '''
    def __init__(
        self,
        x_0 : float,
        y_0 : float,
        radius : float,
        tikz_style : TikzStyle = None,
        key : str = None,
        label : str = ""
    ):
        self.x_0 = x_0
        self.y_0 = y_0
        self.radius = radius
        self.label = tikz_sanitise(label)
        super().__init__(tikz_style, key)

    # TODO RADIUS
    @style_compose
    def draw(self, style):
        return f"""\\node[shape=circle, {str(style)}] \
({self._key}) at ({self.x_0}, {self.y_0}) {{{self.label}}};\n
""" 


class TikzNode(TikzObj):
    def __init__(
        self,
        x_0 : float,
        y_0 : float,
        tikz_style : TikzStyle = None,
        key : str = None,
        label : str = ""
    ):
        self.x_0 = x_0
        self.y_0 = y_0
        self.label = tikz_sanitise(label)
        super().__init__(tikz_style, key)

    @style_compose
    def draw(self, style):
        return f"\\node[{style}] at ({self.x_0}, {self.y_0}) {{{self.label}}};\n"


class TikzBoundingBox(TikzRectangle):
    '''
        Bounding box object
    '''
    @style_compose
    def draw(self, style):
        return f"""\
\\useasboundingbox\
({self.x_0}, {self.y_0}) \
rectangle \
({self.x_1}, {self.y_1});
""" 


class TikzImg(TikzObj): 
    def __init__(
    self,
    x_0 : float,
    y_0 : float,
    path : str,      
    height : float = 3,
    width : float = 3,
    scale : float = 1,
    angle : float = 0, 
    flip : int = 1,
    label : str = ''
    ):
        self.x_0 = x_0
        self.y_0 = y_0
        self.path = path
        self.scale = scale
        self.angle = angle
        self.flip = flip
        self.label = label

        self.height = height
        self.width = width

    def draw(self, *args, **kwargs):
        return f"""\
            \\node[minimum height={self.height}em,
                  minimum width={self.width}em,
                       path picture={{
                           \\node[yscale={self.flip},inner sep=0,outer sep=0] at (path picture bounding box.center){{
                               \\includegraphics[scale={self.scale}, angle={self.angle}, origin=c]{{{self.path}}}
                           }};
                       }}] at ({self.x_0}, {self.y_0}) {{{self.label}}};
        """

def rescale_factory(rescale):
    class ScaledTikzImg(TikzImg):
        def __init__(self, *args, scale=1, scale_eps=3, **kwargs):
            scale = scale * rescale 
            super().__init(*args, scale=scale, **kwargs)
    return ScaledTikzImg
