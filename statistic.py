from collections import Counter
import math

class vector_storage:
    def __init__(self):
        self.__vectors = []

    @property
    def vectors(self):
        return self.__vectors
    
    def create_vec(self):
        print()
        if len(self.vectors) == 0:
            print("Hello there!")
            print("This program gives to you the ability to insert numbers that will be stored in a vector.")
            print("You can do numerous things with it later, but first;")
        
        name = str(input("How will be its name? "))
        cap = int(input("How many numbers your vector will have? "))

        if cap > 1:
            vec = vector(name, cap)

            while vec.last_pos != vec.capacity - 1:
                num = float(input("Insert number: "))
                vec.insert(num)
            
            self.vectors.append({"Name": name, "Vector": vec})
            
            return vec
        else:
            print("Your vector must have at least 2 values.")
    
    def display_vectors(self):
        return self.vectors

    def get_vec(self, name):
        for i in self.vectors:
            if i["Name"] == name:
                return i
                 
        return None

<<<<<<< Updated upstream
    def rename_vec(self, name, new_name):
        vec_entry = self.get_vec(name)

        if vec_entry:
            vec_entry["Name"] = new_name
            return True
        
        return False

=======
>>>>>>> Stashed changes
    def delete_vec(self, name):
        vec_entry = self.get_vec(name)

        if vec_entry:
            self.vectors.remove(vec_entry)
            return True
        
        return False

#########################################################################################################

class vector:
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity
        self.__count = 0
        self.__last_pos = -1
        self.__values = [None] * capacity
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity
    
    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, count):
        self.__count = count
    
    @property
    def last_pos(self):
        return self.__last_pos
    
    @last_pos.setter
    def last_pos(self, last_pos):
        self.__last_pos = last_pos
    
    @property
    def values(self):
        return self.__values
    
    @values.setter
    def values(self, values):
        self.__values = values

    def display_vector(self):
        if self.last_pos == -1:
            return -1
        else:
            for i in range(self.last_pos + 1):
                print(i, '-', self.values[i])
    
    def binary_search(self, value):
        arr = self.merge_sort(self.values)
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
    
    def insert(self, value):
        if self.last_pos == self.capacity - 1:
            return False
        else:
            self.count += 1
            self.last_pos += 1
            self.values[self.last_pos] = value

    def delete(self, value):
        position = self.binary_search(value)

        if position == -1:
            return False
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
            arr.append((self.values[i] - mean) ** 2)

        variance = sum(arr) / self.count
        return variance

    def use_vec(self):
        while True:
            print()
            print("What do you want to know about this vector? Choose the numbers below:")
            print("+-----------------------------------------+")
            print("1- Display vector")
<<<<<<< Updated upstream
            print("2- Rename vector")
            print("3- Search element")
            print("4- Insert element")
            print("5- Delete element")
            print("6- Sum of the elements")
            print("7- Quantity of elements")
            print("8- Sort vector")
            print("9- Arithmetic mean")
            print("10- Median")
            print("11- Mode")
            print("12- Amplitude")
            print("13- Variance")
            print("14- Mean deviation")
            print("15- Standard deviation")
            print("16- Delete vector")
            print("17- Add another vector")
=======
            print("2- Search element")
            print("3- Insert element")
            print("4- Delete element")
            print("5- Sum of the elements")
            print("6- Quantity of elements")
            print("7- Sort vector")
            print("8- Arithmetic mean")
            print("9- Median")
            print("10- Mode")
            print("11- Amplitude")
            print("12- Variance")
            print("13- Mean deviation")
            print("14- Standard deviation")
            print("15- Delete vector")
            print("16- Add another vector")
>>>>>>> Stashed changes
            print("+-----------------------------------------+")
            print()

            choice = int(input("Which do you choose? "))

            if choice == 1: # Display vector
                display_vector = self.display_vector()

                if display_vector == -1:
                    print("Empty vector.")
                else:
                    print(display_vector)
<<<<<<< Updated upstream

            elif choice == 2: # Rename vector
                new_name = str(input("New name for the vector: "))
                storage.rename_vec(self.name, new_name)
            
            elif choice == 3: # Search element
=======
            
            elif choice == 2: # Search element
>>>>>>> Stashed changes
                while True:
                    num = float(input("Which number to search? "))
                    position = self.binary_search(num)

                    if position == -1:
                        print("Number was not found.")
                    else:
                        print(f"The number {num} was found in position {position}.")

                    answer = str(input("Search another one? [y/n] "))

                    if answer == 'n':
                        break
            
<<<<<<< Updated upstream
            elif choice == 4: # Insert element
=======
            elif choice == 3: # Insert element
>>>>>>> Stashed changes
                while True:
                    num = float(input("Which number to insert? "))
                    insert = self.insert(num)

                    if insert is False:
                        print("Full vector, can't insert number.")
                        break
                    else:
                        print(f"Number {num} was inserted.")
                        
                    answer = str(input("Insert another one? [y/n] "))
                        
                    if answer == 'n':
                        break
            
<<<<<<< Updated upstream
            elif choice == 5: # Delete element
=======
            elif choice == 4: # Delete element
>>>>>>> Stashed changes
                while True:
                    num = float(input("Which number to delete? "))
                    delete = self.delete(num)

                    if delete == False:
                        print("Number was not found.")
                    else:
                        print(f"Number {num} was deleted.")

                    answer = str(input("Delete another one? [y/n] "))

                    if answer == 'n':
                        break
            
<<<<<<< Updated upstream
            elif choice == 6: # Sum of the elements
                print(sum(self.values))
            
            elif choice == 7: # Quantity of elements
                print(self.count)
            
            elif choice == 8: # Sort vector
                print(self.merge_sort(self.values))
            
            elif choice == 9: # Arithmetic mean
                print(self.arit_mean())
            
            elif choice == 10: # Median
=======
            elif choice == 5: # Sum of the elements
                print(sum(self.values))
            
            elif choice == 6: # Quantity of elements
                print(self.count)
            
            elif choice == 7: # Sort vector
                print(self.merge_sort(self.values))
            
            elif choice == 8: # Arithmetic mean
                print(self.arit_mean())
            
            elif choice == 9: # Median
>>>>>>> Stashed changes
                self.merge_sort(self.values)
                median = len(self.values) // 2
                print(self.values[median])

<<<<<<< Updated upstream
            elif choice == 11: # Mode
                print(self.find_mode(self.values))

            elif choice == 12: # Amplitude
                print(max(self.values) - min(self.values))

            elif choice == 13: # Variance
                print(self.variance())

            elif choice == 14: # Mean deviation
=======
            elif choice == 10: # Mode
                print(self.find_mode(self.values))

            elif choice == 11: # Amplitude
                print(max(self.values) - min(self.values))

            elif choice == 12: # Variance
                print(self.variance())

            elif choice == 13: # Mean deviation
>>>>>>> Stashed changes
                mean_deviation = self.variance()
                
                if mean_deviation < 0:
                    print(mean_deviation * -1)
                else:
                    print(mean_deviation)

<<<<<<< Updated upstream
            elif choice == 15: # Standard deviation
                print(math.sqrt(self.variance()))

            elif choice == 16: # Delete vector
                storage.delete_vec(self.name)
                break

            elif choice == 17: # Add another vector
=======
            elif choice == 14: # Standard deviation
                print(math.sqrt(self.variance()))

            elif choice == 15: # Delete vector
                storage.delete_vec(self.name)
                break

            elif choice == 16: # Add another vector
>>>>>>> Stashed changes
                break

            else:
                print("You didn't select any of the menu numbers. Please repeat.")
                continue

#########################################################################################################

storage = vector_storage()

while True:
    vec = storage.create_vec()
    vector_length = len(storage.vectors)
    
    if vector_length == 1:
        vec.use_vec()

    elif vector_length > 1:
        print(f"At the moment, you have {vector_length} vectors stored.")
        print("Your vectors: ", storage.vectors)
        choice = str(input("Do you want to add one more or see one of them? [a/s] "))

        if choice == 'a':
            continue
        elif choice == 's':
            while True:
                vec_choice = str(input("Which one? "))
                check = storage.get_vec(vec_choice)

                if check:
                    check["Vector"].use_vec()
                else:
                    print("Vector was not found.")
                    continue
        else:
            print("You didn't select any options given.")
            pass