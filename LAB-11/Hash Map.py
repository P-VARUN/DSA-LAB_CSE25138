class HashingDemonstrator:
    def __init__(self, size):
        self.size = size
        
    def _hash_function(self, key):
        return key % self.size

    # 1. Separate Chaining
    def separate_chaining(self, keys):
        hash_table = [[] for _ in range(self.size)]
        
        for key in keys:
            index = self._hash_function(key)
            hash_table[index].append(key)
            
        return hash_table

    # 2. Linear Probing
    def linear_probing(self, keys):
        hash_table = [None] * self.size
        
        for key in keys:
            index = self._hash_function(key)
            
            i = 0
            while i < self.size:
                new_index = (index + i) % self.size
                if hash_table[new_index] is None:
                    hash_table[new_index] = key
                    break
                i += 1
            
            if i == self.size:
                print(f"Hash table is full! Could not insert {key} using Linear Probing.")
                
        return hash_table

    # 3. Quadratic Probing
    def quadratic_probing(self, keys):
        hash_table = [None] * self.size
        
        for key in keys:
            index = self._hash_function(key)
            
            i = 0
            inserted = False
            while i < self.size:
                new_index = (index + (i * i)) % self.size
                if hash_table[new_index] is None:
                    hash_table[new_index] = key
                    inserted = True
                    break
                i += 1
                
            if not inserted:
                print(f"Could not insert {key} using Quadratic Probing (Table might not be half empty or size isn't prime).")
                
        return hash_table


if __name__ == "__main__":
    # Table size of 10
    hasher = HashingDemonstrator(10)
    
    # Keys intentionally chosen to cause collisions at index 2 (12, 22, 42) and index 5 (15, 25)
    keys_to_insert = [12, 15, 22, 25, 42, 8, 9]

    print("Keys to insert:", keys_to_insert)
    print("\n--- Separate Chaining ---")
    print(hasher.separate_chaining(keys_to_insert))

    print("\n--- Linear Probing ---")
    print(hasher.linear_probing(keys_to_insert))

    print("\n--- Quadratic Probing ---")
    print(hasher.quadratic_probing(keys_to_insert))