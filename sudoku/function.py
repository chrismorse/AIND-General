from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    answer_dict = dict(zip(boxes,grid))

    # walk through all keys
    for key,value in answer_dict.items():


        if value == '.' :
            newValList = '';
            newVals = ['1','2','3','4','5','6','7','8','9']

            row_units_to_check = row_units[rowIndex(key)]
            column_units_to_check = column_units[colIndex(key)]
            square_units_to_check = square_units[squareIndex(key)]

            units_to_check = row_units_to_check + column_units_to_check + square_units_to_check

            #print()
            #print("looking at -> " + key) 
            #print("units to check")
            #print(units_to_check)

            #printBreak()
            '''for val in row_units[rowIndex(key)]:
                print(answer_dict[val])
                if answer_dict[val] in newVals:
                    newVals.remove(answer_dict[val])
            '''
            for val in units_to_check:
                if answer_dict[val] in newVals:
                    newVals.remove(answer_dict[val])         
            #print(newVals)

            newValList = ''.join(newVals)
            answer_dict[key] = newValList
            #print(newValList)
            '''
            printBreak()
            print("Cols")
            print(column_units[colIndex(key)]) 

            printBreak()
            print("Square")
            print(square_units[squareIndex(key)]) 
            '''
            #printBreak()

    return(answer_dict)    

def printBreak():
    print("-"*100)

def rowIndex(box):
    return list(rows).index(box[0])

def colIndex(box):
    return list(cols).index(box[1])

def squareIndex(box):
    for key in square_units:
        if box in key:
            return(list(square_units).index(key))
    
def main():
    puzzle = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..' 
    display(grid_values(puzzle))


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()




'''
5. Strategy 1: Elimination


from utils import *

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for boxkey,boxvalue in values.items():
        #printBreak()

        
        if len(boxvalue) == 1 :
            #print("boxkey -> " + boxkey)
            #print("boxvalue -> " + boxvalue) 
            row_units_to_check = row_units[rowIndex(boxkey)]
            column_units_to_check = column_units[colIndex(boxkey)]
            square_units_to_check = square_units[squareIndex(boxkey)]

            units_to_check = row_units_to_check + column_units_to_check + square_units_to_check
            #print(units_to_check)

            for peerunit in units_to_check:
                if boxkey != peerunit:
                    #print("peerunit -> " + peerunit) 
                    #print("values[peerunit] -> " + values[peerunit])
                    values[peerunit] = values[peerunit].replace(boxvalue,"")
                    #print("values[peerunit] -> " + values[peerunit])
                    
                    
                #if answer_dict[val] in key and :
                    
                    #newVals.remove(answer_dict[val])         

            #newValList = ''.join(newVals)
            #answer_dict[key] = newValList


        
    return(values)    

def printBreak():
    print("-"*50)

def rowIndex(box):
    return list(rows).index(box[0])

def colIndex(box):
    return list(cols).index(box[1])

def squareIndex(box):
    for key in square_units:
        if box in key:
            return(list(square_units).index(key))
'''