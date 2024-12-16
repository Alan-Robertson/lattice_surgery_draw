import abc

from lattice_surgery_draw.style import TikzStyle 

def style_compose(fn):
    '''
        Style composition decorator
    '''
    def _wrap(self, *args, **kwargs):
        style = self.style(*args, **kwargs)
        return fn(style)
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
        style = self.style(*style_args, **style_kwargs)
        return f"""\
\\draw[{self.style(*style_args, **style_kwargs)}]\
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
        key : str = None
    ):
        self.x_0 = x_0
        self.y_0 = y_0
        self.radius = radius
        super().__init__(tikz_style, key)

    @style_compose
    def draw(self, style):
        style = self.style(*style_args, **style_kwargs)
        return f"""\
\\draw[{self.style(*style_args, **style_kwargs)}]\
({self.x_0}, {self.y_0}) \
rectangle \
({self.x_1}, {self.y_1});
""" 

