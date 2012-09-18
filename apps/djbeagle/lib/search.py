from djbeagle.lib.engines import util


def run(engines, criteria, num_results=10):
    availible_engines = util.get_availible_engines()
    results = []
    for engine in engines:
        instance = availible_engines[engine]()
        results.extend(instance.search(criteria.split(" "), num_results))
    return results
