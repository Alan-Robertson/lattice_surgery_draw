import abc

class TexHeader(abc.ABC):
    def get_header(self, *args, **kwargs) -> str:
        '''
            Gets the latex header
        '''
        raise Exception("Abstract Base Class")

    def get_footer(self, *args, **kwargs) -> str:
        '''
            Gets the latex footer
        '''
        raise Exception("Abstract Base Class")

    def __call__(self, *args, **kwargs) -> str:
        '''
            Dispatch for _format_file
        '''
        return self._format_file(*arg, **kwargs)

    def _format_file(self, tikz_str: str) -> str:
        '''
            Attaches the header and footer
        '''
        tikz_str = self.get_header() + tikz_str
        tikz_str = tikz_str + self.get_footer()
        return self.tikz_str
        

class DefaultTexHeader(TexHeader): 
    HEADER = r"""
%!TEX options=--shell-escape
\documentclass[tikz]{standalone}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{xcolor}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage{accsupp}    
\usepackage{graphicx}
\usepackage{mathtools}
\usepackage{pagecolor}
\usepackage{amsmath} % for \dfrac
\usepackage{tikz}
\tikzset{>=latex} % for LaTeX arrow head
\usepackage{pgfplots} 
\usepackage[edges]{forest}
\usetikzlibrary{patterns, backgrounds, arrows.meta}
\setlength{\parindent}{0cm}
\setlength{\parskip}{1em}
\def\offset{0.1}
\begin{document}
"""
    FOOTER = "\n \\end{document}\n"

    def get_header(self):
        return self.HEADER

    def get_footer(self):
        return self.FOOTER
