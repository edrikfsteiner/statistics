from collections import Counter
import math

class vector_storage:
    def __init__(self):
        self.vectors = []
    
    def create_vec(self):
        print()
        if len(self.vectors) == 0:
            print("Hello there!")
            print("This program gives to you the ability to insert numbers that will be stored in a vector.")
            print("You can do numerous things with it later, but first;")
        
        name = str(input("How will be its name? "))
        cap = int(input("How many numbers your vector will have? "))

        if cap > 1:
            vec = unord_vector(name, cap)

            while vec.last_pos != vec.capacity - 1:
                num = float(input("Insert number: "))
                vec.insert(num)
            
            self.vectors.append({"Name": name, "Vector": vec.values})
            
            return vec
        else:
            print("Your vector must have at least 2 values.")
    
    def show_vectors(self):
        return self.vectors

    def get_vec(self, name):
        for i in self.vectors:
            if i["Name"] == name:
                return i 
                 
        return None

    def update_vec(self, name, new_vec):
        vec_entry = self.get_vec(name)

        if vec_entry:
            vec_entry["Vector"] = new_vec
            return True
        
        return False

    def delete_vec(self, name):
        vec_entry = self.get_vec(name)

        if vec_entry:
            self.vectors.remove(vec_entry)
            return True
        
        return False

#########################################################################################################

class unord_vector:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.count = 0
        self.last_pos = -1
        self.values = [None] * capacity
    
    def insert(self, value):
        if self.last_pos == self.capacity - 1:
            print("Full vector")
        else:
            self.count += 1
            self.last_pos += 1
            self.values[self.last_pos] = value
    
    def show_vector(self):
        if self.last_pos == -1:
            print("Empty vector")
        else:
            for i in range(self.last_pos + 1):
                print(i, '-', self.values[i])
    
    def binary_search(self, value):
        arr = self.merge_sort(vector.values)
        inf_lim = 0
        sup_lim = self.last_pos

        while True:
            current_pos = (inf_lim + sup_lim) // 2

            if arr[current_pos] == value:
                return current_pos
            elif inf_lim > sup_lim:
                return -1
            else:
                if arr[current_pos] < value:
                    inf_lim = current_pos + 1
                else:
                    sup_lim = current_pos - 1

    def delete(self, value):
        position = self.binary_search(value)

        if position == -1:
            return -1
        else:
            for i in range(position, self.last_pos):
                self.values[i] = self.values[i + 1]
            self.count -= 1
            self.last_pos -= 1

    def merge_sort(self, arr):
        if len(arr) > 1:
            half = len(arr)//2
            left = arr[:half]
            right = arr[half:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0
    
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
    
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
    
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
    
        return arr
    
    def arit_mean(self):
        mean = sum(self.values) / self.count
        return mean
    
    def find_mode(self, arr):
        counts = Counter(arr)
        max_freq = max(counts.values())
        mode = [k for k, v in counts.items() if v == max_freq]
        return mode
    
    def variance(self):
        arr = []
        mean = self.arit_mean()

        for i in range(self.last_pos + 1):
            ele = (self.values[i] - mean) ** 2
            arr.append(ele)

        sum_ele = sum(arr)
        variance = sum_ele / self.count
        return variance

    def use_vec(self):
        while True:
            print()
            print("What do you want to know about this vector? Choose the numbers below:")
            print("+-----------------------------------------+")
            print("1- Show vector")
            print("2- Search element")
            print("3- Insert element")
            print("4- Delete element")
            print("5- Sum of the elements")
            print("6- Quantity of elements")
            print("7- Sort vector")
            print("8- Arithmetic Mean")
            print("9- Median")
            print("10- Mode")
            print("11- Amplitude")
            print("12- Variance")
            print("13- Mean deviation")
            print("14- Standard deviation")
            print("15- Delete vector")
            print("16- Add another vector")
            print("+-----------------------------------------+")
            print()

            choice = int(input("Which do you choose? "))

            if choice == 1:
                self.show_vector()
            
            elif choice == 2:
                while True:
                    num = float(input("Which number to search? "))
                    position = self.binary_search(num)

                    if position == -1:
                        print("Number was not found")
                    else:
                        print(f"The number {num} was found in position {position}.")

                    answer = str(input("Search another one? [y/n] "))

                    if answer == 'n':
                        break
            
            elif choice == 3:
                while True:
                    num = float(input("Which number to insert? "))
                    self.insert(num)

                    answer = str(input("Insert another one? [y/n] "))

                    if answer == 'n':
                        break
            
            elif choice == 4:
                while True:
                    num = float(input("Which number to delete? "))
                    position = self.delete(num)

                    if position == -1:
                        print("Number was not found")
                    else:
                        print(f"The number {num} was deleted.")

                    answer = str(input("Delete another one? [y/n] "))

                    if answer == 'n':
                        break
            
            elif choice == 5:
                print(sum(self.values))
            
            elif choice == 6:
                print(self.count)
            
            elif choice == 7:
                print(self.merge_sort(self.values))
            
            elif choice == 8:
                print(self.arit_mean())
            
            elif choice == 9:
                self.merge_sort(self.values)
                median = len(self.values) // 2
                print(self.values[median])

            elif choice == 10:
                print(self.find_mode(self.values))

            elif choice == 11:
                print(max(self.values) - min(self.values))

            elif choice == 12:
                print(self.variance())

            elif choice == 13:
                mean_deviation = self.variance()
                
                if mean_deviation < 0:
                    mean_deviation * -1
                    print(mean_deviation)
                else:
                    print(mean_deviation)

            elif choice == 14:
                print(math.sqrt(self.variance()))

            elif choice == 15:
                storage.delete_vec(self.name)
                break

            elif choice == 16:
                break

            else:
                print("You didn't select any of the menu numbers. Please repeat.")
                continue

#########################################################################################################

storage = vector_storage()

while True:
    vector = storage.create_vec()
    
    if len(storage.vectors) == 1:
        vector.use_vec()

    elif len(storage.vectors) > 1:
        print(f"At the moment, you have {len(storage.vectors)} vectors stored.")
        print("Your vectors: ", storage.vectors)
        choice = str(input("Do you want to compare them or see one of them? [c/s] "))

        if choice == 'c':
            pass
        elif choice == 's':
            while True:
                vec_choice = str(input("Which one? "))
                check = storage.get_vec(vec_choice)

                if check:
                    vector.use_vec()
                    break
                else:
                    print("Vector was not found.")
                    continue
        else:
            print("You didn't select any options given.")
            pass