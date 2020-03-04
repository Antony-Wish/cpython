import tracemalloc
from collections import namedtuple
from lib.engine import Engine
from lib.engine_factory import EngineFactory

def print_frame(traceback):
    print '--------print traceback, length:', len(traceback)
    for frame in traceback:
        print str(frame)

def print_trace(trace):
    print '--------print trace, size:', trace.size
    print_frame(trace.traceback)

def engine_test():
    engine = EngineFactory.create_engine("Gas")
    tb = tracemalloc.get_object_traceback(engine)
    print_frame(tb)

def main():
    tracemalloc.start(25)

    # ... run your application ...
    print 'traceback limit', tracemalloc.get_traceback_limit()

    engine_test()

    #print tracemalloc.get_traced_memory()
    #print tracemalloc.get_tracemalloc_memory()

    #shapshot = tracemalloc.take_snapshot()
    #for trace in shapshot.traces:
    #    print_trace(trace)

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)

    tracemalloc.stop()

# 
# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)

if __name__ == "__main__":
    main()
