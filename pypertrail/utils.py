class Utils:

    from colors import cyan, yellow, green, magenta, red  # noqa: F401
    COLORS = ['cyan', 'yellow', 'green', 'magenta', 'red']

    @staticmethod
    def colorize_event(event, color):

        attribs = ()
        if color == 'system' or color == 'all':
            attribs += (event['hostname'],)

        if color == 'program' or color == 'all':
            attribs += (event['program'],)

        pre = '{0} {1} {2}'.format(event['received_at'],
                                   event['hostname'],
                                   event['program'])

        post = ' {0}'.format(event['message'])

        idx = hash(attribs) % 5
        color = Utils.COLORS[idx]
        pre = getattr(Utils, color)(pre)

        return pre + post

    @staticmethod
    def format_event(event, color):
        if color and color != 'off':
            return Utils.colorize_event(event, color)
        else:
            return '{0} {1} {2} {3}'.format(event['received_at'],
                                            event['hostname'],
                                            event['program'],
                                            event['message'])
