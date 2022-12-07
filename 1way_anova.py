from typing import List

conc5 = [7,  8, 15, 11,  9, 10]
conc10 = [12, 17, 13, 18, 19, 15]
conc15 = [14, 18, 19, 17, 16, 18]
conc20 = [19, 25, 22, 23, 18, 20]

treatments = [conc5, conc10, conc15, conc20]


def calculateSSE(treatments: List[List[int]]) -> float:
    sse = 0  # comment
    for sample in treatments:
        mean = 0
        for x in sample:
            mean += x
        mean /= len(sample)
        for x in sample:
            sse += (x - mean) ** 2

    return round(sse, 2)


def calculateSST(treatments: List[List[int]]) -> float:
    sst: float = 0.0
    mean = 0
    elems = 0
    for t in treatments:
        for x in t:
            mean += x
            elems += 1

    mean /= elems

    for sample in treatments:
        for obs in sample:
            sst += (obs - mean) ** 2

    return round(sst, 2)


def calculateSSA(treatments: List[List[int]]) -> float:
    ssa = 0
    mean = 0
    elems = 0
    for t in treatments:
        for x in t:
            mean += x
            elems += 1

    mean /= elems

    for t in treatments:
        sample_mean = 0
        for x in t:
            sample_mean += x
        sample_mean /= len(t)
        ssa += (sample_mean - mean) ** 2
    return round(ssa * len(treatments[0]), 2)


def calculateMSA(treatments: List[List[int]], ssa: float = None) -> float:
    if ssa is None:
        ssa = calculateSSA(treatments)

    k = len(treatments)
    return round(ssa / (k - 1), 2)


def calculateMSE(treatments: List[List[int]], sse: float = None) -> float:
    if sse is None:
        sse = calculateSSE(treatments)

    k = len(treatments)
    n = len(treatments[0])

    return round(sse / (k * (n - 1)), 2)


sse = calculateSSE(treatments)
ssa = calculateSSA(treatments)
sst = calculateSST(treatments)

mse = calculateMSE(treatments, sse)
msa = calculateMSA(treatments, ssa)

print(f"SSE: {sse}\nSSA: {ssa}\nMSE: {mse}\nMSA: {msa}")
print(f"Calculated F: {round(msa / mse, 2)}")
