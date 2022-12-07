conc5  = [ 7,  8, 15, 11,  9, 10]
conc10 = [12, 17, 13, 18, 19, 15]
conc15 = [14, 18, 19, 17, 16, 18]
conc20 = [19, 25, 22, 23, 18, 20]

factors = [conc5, conc10, conc15, conc20]

def sse(treatments: list[list[int]]) -> float:
	sse = 0 # comment
	for sample in treatments:
		mean = 0
		for x in sample:	
			mean += x
		mean /= len(sample)
		for x in sample:
			sse += (x - mean) ** 2

	return sse

def sst(treatments: list[list[int]]) -> float:
	sst: float = 0.0
	mean = 0
	elems = 0
	for t in treatments:
		for x in t:
			mean += x
			elems += 1
	
	mean /= elems;

	for sample in treatments:
		for obs in sample:
			sst += (obs - mean) ** 2
	
	return sst

def ssa(treatments: list[list[int]]) -> float:
	ssa = 0
	mean = 0
	elems = 0
	for t in treatments:
		for x in t:
			mean += x
			elems += 1
	
	mean /= elems;

	for t in treatments:
		sample_mean = 0
		for x in t:
			sample_mean += x
		sample_mean /= len(t)
		ssa += (sample_mean - mean) ** 2
	return ssa * len(treatments[0])


total = round(sst(factors), 2)
a = round(ssa(factors), 2)
err = round(sse(factors), 2)

e_dof = len(factors) * (len(factors[0]) - 1)
a_dof = len(factors) - 1
t_dof = len(factors) * len(factors[0]) - 1

msa = a / a_dof;
mse = err / e_dof

f_calc = round(msa / mse, 2)

print("SST", total)
print("SSA", a)
print("SSE", err)

print("f_calc", f_calc)
