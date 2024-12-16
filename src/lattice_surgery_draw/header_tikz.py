import abc

class TikzHeader(abc.ABC):
    def get_header(self, *args, **kwargs) -> str:
        '''
            Gets the tikz header
        '''
        raise Exception("Abstract Base Class")

    def get_footer(self, *args, **kwargs) -> str:
        '''
            Gets the tikz footer
        '''
        raise Exception("Abstract Base Class")

    def __call__(self, *args, **kwargs) -> str:
        '''
            Dispatch for _format_file
        '''
        return self._format_tikz(*arg, **kwargs)

    def _format_tikz(self, tikz_str: str) -> str:
        '''
            Attaches the header and footer
        '''
        tikz_str = self.get_header() + tikz_str
        tikz_str = tikz_str + self.get_footer()
        return self.tikz_str


class DefaultTikzHeader(TikzHeader): 
    HEADER = f"\\begin{{tikzpicture}}[]\n"
    FOOTER = "\n \\end{tikzpicture}\n"

    def get_header(self):
        return self.HEADER

    def get_footer(self):
        return self.FOOTER
