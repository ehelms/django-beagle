from django.conf import settings


def get_availible_engines():
    engines = {}
    for engine in settings.SEARCH_ENGINES:
        klass = get_engine_class(engine)
        engines[klass.title] = klass
    return engines


def get_engine_titles():
    titles = []
    for engine in settings.SEARCH_ENGINES:
        klass = get_engine_class(engine)
        titles.append(klass.title)
    return titles


def get_engine_class(engine):
    engine_split = engine.split('.')
    engine_class = engine_split.pop(len(engine_split) - 1)
    engine_str = ".".join(engine_split)
    mod = __import__(engine_str, globals(), locals(), [engine_class])
    klass = getattr(mod, engine_class)
    return klass
