precision, recall, prc_threshold=[.1,.2,.3,.4,.5,.6],[.1,.2,.3,.4,.5,.6],[.1,.2,.3,.4,.5,.6]
n_th=2
print(list(zip(precision, recall, prc_threshold))[::n_th])