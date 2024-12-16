class SCLayer():

    def __init__(self,
         height,
         width,
         *backgrounds
    ):
        pass

    def tikz_route_layer(self,router, layer):
        pass
        #tikz_str = '\\pgfdeclarelayer{background}\n\\pgfsetlayers{background,main}\n'

        #tikz_str = tikz_patch_graph_no_header(router.graph)
        #tikz_str += '\\begin{pgfonlayer}{background}\n'
        #tikz_str += tikz_grid(*router.qcb.shape)
        #for gate in layer:
        #    route = router.routes[gate]
        #    tikz_str += tikz_route(route, router)
        #tikz_str += '\\end{pgfonlayer}\n'
        #return tikz_str

    #def tikz_route(route, router):
        #STOP_ITERATION = object()
        #tikz_str = ""
        #element_iter = iter(route)
        ## Resources
        #while (element := next(element_iter, STOP_ITERATION)) is not STOP_ITERATION:
        #    if isinstance(element, tuple):
        #        tikz_str += tikz_circle(*element, hex(id(element)), " ") 
        #    else:
        #        curr_node = element
        #        break
        ## Routes
        #element_iter = iter(route)
        #curr_node = None
        #while (element := next(element_iter, STOP_ITERATION)) is not STOP_ITERATION:
        #    if curr_node is not None:
        #        style = COLOUR_JOIN
        #        colour = JOIN_COLOUR
        #        if (abs(curr_node.x - element.x) + abs(curr_node.y - element.y)) > 1:
        #            style = COLOUR_TELEPORT
        #            colour = TELEPORT_COLOUR
        #        tikz_str += tikz_path(hex(id(curr_node)), hex(id(element)),  style=style, **{'double distance': '0.5cm', 'double':colour})
        #    curr_node = element

        #return tikz_str

