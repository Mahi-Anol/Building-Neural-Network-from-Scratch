inputs=[1,2,3,4]
weights=[[0.1,0.2,0.3,0.4],[0.5,0.6,0.7,0.8],[0.3,0.6,0.4,0.5]]## Assuming we have 3 neurons. So each neuron have 4 weights assosiate with it for 4 input.

bias=[i+1 for i in range(len(weights)+1)]

output=[] 

for i,w_s in enumerate(weights,0):
    o=0 #sum holder of multiplication
    for j,w in enumerate(w_s,0):
        o+=(w*inputs[j])
    o+=bias[i] #Adding the bias after weight multiplication.
    output.append(o)
print(output)
