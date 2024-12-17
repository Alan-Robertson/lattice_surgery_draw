import abc

class TikzDeclarativeStyle(abc.ABC):
    '''
        Tikz declarative style class
        Creates styles at the start of the frame by name
    ''' 
    def __init__(self, **kwargs):
        styles = kwargs

    def __repr__(self):
        style_str = r'\tikzset{'
        for key, style in styles.items():
           style_str += f"{key}/.style={{{str(style)}}},\n" 
        style_str += r'}'
        return style_str
            
    def __str__(self):
        return self.__repr__()

class DefaultTikzStyle(TikzDeclarativeStyle):
    BASE_STYLE = r"""
\tikzset{
->-/.style={-Stealth,line width = .5mm, draw=black!70,rounded corners=3pt},
background/.style={rounded corners=5pt, thick, draw=gray!60, fill=gray!20,fill opacity=0.5},
arbitrary/.style={rounded corners=5pt,thick, draw=black!70, fill=gray!40},
reg/.style= {rounded corners=5pt, thick,  draw=black!80, fill=red!40},
regsmall/.style= {line width=0,  draw=red!40, fill=red!10},
regnode/.style= {shape=circle, line width = 0.4mm, draw=red!60,fill=red!20},
route/.style= {rounded corners=5pt, thick,  draw=black!80,fill=green!20},
routenode/.style= {line width = 0.4mm, draw=black!70,fill=green!50!black!5, rounded corners = 3pt},
routeend/.style= {rounded corners=5pt, line width=0.35mm, draw=black!80,fill=green!60},
routeendnode/.style= {shape=circle, line width = 0.4mm, draw=black!70,fill=black!50!green!80},
extern/.style= {rounded corners=5pt, thick,  draw=black!80,fill=blue!40},
externnode/.style= {shape=circle, line width=0.4mm, draw=black!80,fill=blue!20},
io/.style= {rounded corners=5pt, thick,  draw=black!80,fill=purple!60},
ionode/.style= {shape=circle, line width=0.4mm, draw=black!80,fill=purple!20},
scmerge/.style= {line width=0.4mm, draw=black!80,fill=red!40!yellow!30},
teleport/.style= {line width=0.4mm, draw=black!80,fill=cyan!40},
}
"""
    def __init__(self, **kwargs):
        pass

    def __repr__(self):
        return self.BASE_STYLE
