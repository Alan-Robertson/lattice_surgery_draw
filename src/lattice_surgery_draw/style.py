from itertools import chain

class TikzStyle():
    '''
        Tikz styling object
        Converts dictionaries and lists to tikz style commands
    '''
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        return self._tikz_argparse(*args, **kwargs) 

    def __str__(self, *args, **kwargs):
        return self._tikz_argparse(*args, **kwargs) 

    def __repr__(self, *args, **kwargs):
        return self._tikz_argparse(*args, **kwargs) 

    def _tikz_argparse(self, *args, **kwargs):
        arg_str = ','.join(map(tikz_sanitise, map(str, chain(self.args, args))))
        kwarg_str = ','.join(map(lambda item: f"{tikz_sanitise(item[0])}={tikz_sanitise(item[1])}", chain(self.kwargs.items(), kwargs.items())))
        if len(kwarg_str) == 0:
            return arg_str
        args_str = f"{arg_str},{kwarg_str}"
        if args_str[0] == ',':
            args_str = args_str[1:]
        return args_str
