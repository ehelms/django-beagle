from djbeagle.lib.engines import util


def run(engine, criteria, num_results=10):
    availible_engines = util.get_availible_engines()
    results = []
    instance = availible_engines[engine]()
    results.extend(instance.search(criteria.split(" "), num_results))
    return results
