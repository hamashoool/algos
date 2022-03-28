class SymbolTable:
    def __init__(self):
        self.MAX = 15
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, symbol):
        hash = 0
        for char in symbol:
            hash += ord(char) + 23
        return hash % self.MAX

    def add(self, symbol, type_):
        hash = self.get_hash(symbol)
        found = False
        for idx, element in enumerate(self.arr[hash]):
            if len(element)==2 and element[0]==symbol:
                self.arr[hash][idx] =  (symbol,type_)
                found = True
                break
        if not found:
            self.arr[hash].append((symbol, type_))
    
    def get(self, symbol):
        hash = self.get_hash(symbol)
        for element in self.arr[hash]:
            if element[0] == symbol:
                return print(f'\n({symbol}) symbol already exists in the symbol-table.')
        return print(f'\n({symbol}) symbol does not exists in the symbol-table.')
    
    def delete(self, symbol):
        hash = self.get_hash(symbol)
        for index, element in enumerate(self.arr[hash]):
            if element[0] == symbol:
                print(f'\n({symbol}) is deleted from the symbol-table.')
                del self.arr[hash][index]
    
    def show(self):
        print('\n')
        for index, ls in enumerate(self.arr):
            if ls == []:
                ls = ""
            else:
                st = f""
                for element in ls:
                    comma = ','
                    if element == ls[-1]:
                        comma = ''
                    st = st + f' {element[0]} ( {element[1]} ){comma}'
                ls = st
            print(f'{index}: {ls}')
        

if __name__ == "__main__":
    symbol_table = SymbolTable()
    display_text = '\nPress 1 to insert a new symbol along with its type into the symbol-table\n\n' \
        'Press 2 to lookup whether a given symbol already exists in the symbol-table or not\n\n' \
        'Press 3 to dump the contents of the symbol table to the console\n\n' \
        'Press 4 to delete a given symbol if it already exists in the symbol-table\n\n' \
        'Press 0 to exit\n\n'

    while True:    
        print(display_text)
        option = int(input("Option goes here: "))

        if option == 0:
            break

        elif option == 1:
            symbol = str(input("symbol to add goes here: "))
            type_ = str(input("type goes here: "))
            symbol_table.add(symbol, type_)

        elif option == 2:
            key = str(input("symbol to lookup goes here: "))
            symbol_table.get(key)

        elif option == 3:
            symbol_table.show()

        elif option == 4:
            symbol = str(input("symbol to delete goes here: "))
            symbol_table.delete(symbol)

        else:
            print("Invalid option. press (q) for quit or any key to continue")
            question = str(input("here: "))
            if question == 'q' or question == 'Q':
                break
            else:
                continue