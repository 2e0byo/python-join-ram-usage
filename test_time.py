from perfbench import *

bm = Benchmark(
    datasets=[Dataset(factories=[lambda n: "a" * n])],
    dataset_sizes=list(2**n for n in range(25)),
    kernels=[
        Kernel(stmt='" ".join(DATASET)', label="No List"),
        Kernel(stmt='" ".join(list(DATASET))', label="List"),
        Kernel(stmt='" ".join([*DATASET])', label="Unpacking"),
        Kernel(stmt='DATASET.replace("", " ")', label="Replace"),
    ],
    xlabel="String Length",
    title="str.join(str) vs str.join(list(str))",
)

bm.run()
bm.save_as_html(filepath="perf.html")
