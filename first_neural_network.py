inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]

w = 0.1
b = 0.3
learning_rate = 0.1
epochs = 100

def predict(i):
    return w * i + b

#Train the network
for _ in range(epochs):
    pred = [predict(i) for i in inputs]
    errors = [(t - p) ** 2  for p,t in zip(pred, targets)]
    cost = sum(errors) / len(targets)
    print(f"Weight: {w:.2f}, Bais:{b:.2f}, Cost: {cost:.2f}")

    errors_d = [2 * (p - t) for p, t in zip(pred, targets)]
    weight_d = [e * i for e, i in zip(errors_d, inputs)]
    bias_d = [e  for e in errors_d]

    b -= learning_rate * (sum(bias_d) / len(bias_d)) 
    w -= learning_rate * (sum(weight_d) / len(weight_d))

test_inputs = [5, 6]
test_targets = [20, 22]
pred = [predict(i) for i in test_inputs]
for i, t, p in zip(test_inputs, test_targets, pred):
    print(f"input:{i}, target: {t}, pred: {p:.4f}")