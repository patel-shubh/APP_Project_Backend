class Observer:

    def __init__(self, Object):
        Object.subscribe(self)

    def notify(
        self,
        Object,
        *args,
        **kwargs
        ):
        print ('Observer : ', args, kwargs, 'From', Object)