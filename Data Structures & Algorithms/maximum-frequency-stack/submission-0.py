class FreqStack:

    def __init__(self):
        self.key_counter = {}
        self.freq_map = defaultdict(list)
        self.mx_f = 0
        

    def push(self, val: int) -> None:
        f = self.key_counter.get(val, 0) + 1
        self.key_counter[val] = f

        self.mx_f = max(self.mx_f, f)       
        
        self.freq_map[f].append(val)
        

    def pop(self) -> int:
        pop = self.freq_map[self.mx_f].pop()
        self.key_counter[pop] -= 1
        new_f = self.key_counter[pop]
        if new_f == 0:
            del self.key_counter[pop]    
        if not self.freq_map[self.mx_f]:
            self.mx_f = max(0, self.mx_f-1)
        return pop    
        

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()