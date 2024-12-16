import abc

class ColourMap(abc.ABC): 
    def __getitem__(self, key):
        raise Exception("Abstract Base Class")


class DefaultColourMap(ColourMap): 
    COLOUR_REG = 'reg'
    COLOUR_REG = 'regnode'

    COLOUR_EXTERN = 'extern'
    COLOUR_EXTERN = 'externnode'

    COLOUR_LOCAL_ROUTE = 'route'
    COLOUR_LOCAL_ROUTE = 'routenode'

    COLOUR_IO = 'io'
    COLOUR_IO = 'ionode'

    COLOUR_ROUTE = 'routeend'
    COLOUR_NONE = 'arbitrary'
    COLOUR_DEBUG = 'yellow!30'
    COLOUR_JOIN = 'scmerge'
    COLOUR_GRID = 'black!50!white'
    COLOUR_TELEPORT = 'teleport'

    TELEPORT_COLOUR = 'cyan!40'
    JOIN_COLOUR = 'red!40!yellow!30'

    __colour_map = {
        SCPatch.IO : COLOUR_IO,
        SCPatch.ROUTE : COLOUR_ROUTE,
        SCPatch.LOCAL_ROUTE : COLOUR_LOCAL_ROUTE,
        SCPatch.EXTERN : COLOUR_EXTERN,
        SCPatch.REG : COLOUR_REG,
        SCPatch.INTERMEDIARY : COLOUR_NONE, 
        SCPatch.NONE : COLOUR_NONE,
        'debug' : COLOUR_DEBUG
    }

    def __getitem__(self, key): 
        return self.colour_map.get(key, 'debug')
