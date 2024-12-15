def tikz_argparse(*args, **kwargs):
    '''
        Maps args and kwargs to tikz args
    '''
    arg_str = ','.join(map(tikz_sanitise, map(str, args)))
    kwarg_str = ','.join(map(lambda item: f"{tikz_sanitise(item[0])}={tikz_sanitise(item[1])}", kwargs.items()))
    if len(kwarg_str) == 0:
        return arg_str
    args_str = f"{arg_str},{kwarg_str}"
    if args_str[0] == ',':
        args_str = args_str[1:]
    return args_str


def tikz_sanitise(string):
    '''
    Escapes aspects of tikz strings 
    '''
    return string.replace('_', '\\_')

