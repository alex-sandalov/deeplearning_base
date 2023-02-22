
# task 1
def almost_double_factorial(n):
    cnt = 1
    for i in range(2, n + 1):
        if i % 2:
            cnt *= i
    return cnt

# task 2
sorted_items = sorted(items, key=lambda x: x[1][-1])

# task 3
def cumsum_and_erase(A, erase=1):
    pref = [0]
    for i in range(1, len(A) + 1):
        pref.append(pref[i - 1] + A[i - 1])
    B = [pref[i] for i in range(1, len(A) + 1) if pref[i] != erase]
    return B

# task 4
def process(sentences):
    result = []
    for i in range(len(sentences)):
        r = []
        s = sentences[i].split()
        for j in range(len(s)):
            if s[j].isalpha():
            r.append(s[j])
        result.append(' '.join(r))
    return result

# task 5
class Neuron:
  
    def __init__(self, w, f = lambda x: x):
        self.w = w
        self.f = f
        self.x = None

    def forward(self, x):
        self.x = x
        s = 0
        for i in range(len(x)):
            s += self.x[i] * self.w[i]
        return self.f(s)
    
    def backlog(self):
        return self.x