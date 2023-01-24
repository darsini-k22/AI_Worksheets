def read_data(filename):
  """
    Reads the txt file and returns a list which containts the data of file 
    Parameters
    ----------
    filename : str
        The name of the file that user wants to read
    
    Raises
    ------
    FileNotFoundError
      If the filename does not exist
    Returns
    -------
    list
        a list of lists which contains the data of the file
  """
  try:
    data = []
    abs_path = os.path.abspath(f"puzzles/{filename}")
    with open(abs_path, "r", encoding="utf-8") as f:
      contents = f.readlines()
    for row in contents:
      new_row = [int(number.strip()) for number in row if number != '\n' and number != ' ']
      data.append(new_row)
    return data
  except FileNotFoundError:
     return None

from abc import ABC, abstractmethod
class Node(ABC):
  """
    This class used to represent a Node in the graph 
    It's important to implement this interface in order to use
    the class DFS
    ...
    Methods
    -------
    __eq__(self, other)
        Determines if two nodes are equal or not
    
    is_the_solution(self)
        Determines if the current node is the solution of the problem
    def is_the_solution(self)
        Extends the current node according to the rules of the problem
    
    __str__(self)
        Prints the node data
  """

  @abstractmethod
  def __eq__(self, other):
    pass

  @abstractmethod
  def is_the_solution(self):
    pass

  @abstractmethod
  def extend_node(self):
    pass

  @abstractmethod
  def __str__(self):
    pass

def search(self):
    while True:

      self.number_of_steps += 1
      
      
      if self.frontier_is_empty():
        print(f"No Solution Found after {self.number_of_steps} steps!!!")
        break
        
      selected_node = self.remove_from_frontier()
      
      # check if the selected_node is the solution
      if selected_node.is_the_solution():
        print(f"Solution Found in {self.number_of_steps} steps")
        print(selected_node)
        break

      # extend the node
      new_nodes = selected_node.extend_node()

      # add the extended nodes in the frontier
      if len(new_nodes) > 0:
        for new_node in new_nodes:
          if new_node not in self.frontier and new_node not in self.checked_nodes:
            self.insert_to_frontier(new_node)

from copy import deepcopy
from dfs_algorithm import Node

class Sudoku(Node):
  """
    This class used to represent the sudoku board
    ...
    Attributes
    ----------
    puzzle : List
        represent the puzzle  
    rows : Integer, optional
        represents number of rows
    cols : Integer, optional
        represents the number of columns
  
    Methods
    -------
    __eq__(self, other)
        Determines if the current sudoku is the same with the other 
    
    check_row(self, row, value)
        Checks if the value is unique in the specific row
    check_col(self, col, value):
        Checks if the value is unique in the specific column
    
    check_sqaure(self, row, col, value)
        Checks if the value is unique in the specific square
    
    find_first_epty_slot(self)
        Finds the first slot in the puzzle with value 0, which means that the slot in empty
    extend_node(self)
        Extends the current node, creating a new instance of Sudoku for each valid number
    is_the_solution(self)
        Checks if the current node is the solution
    __str__(self)
        Returns the sudoku board in order to be printed properly
    """
  def __init__(self, puzzle, rows=9, cols=9):
    self.puzzle = puzzle
    self.rows = rows
    self.cols = cols

  
  def __eq__(self, other):   
    """
      Check if the current puzzle is equal with the other puzzle.
      Parameters
      ----------
      Other : Sudoku
          The other sudoku puzzle
      Returns
      -------
      Boolean
        True: if both puzzles are the same
        False: If puzzles are different
    """ 
    if isinstance(other, Sudoku):
      return self.puzzle == other.puzzle
    return self.puzzle == other

  
  def check_row(self, row, value):
    """
      Checks if the value is unique in the specific row
      Parameters
      ----------
      row : Integer
          The number of row 
      value: Integer
          The possible number for this row
      Returns
      -------
      Boolean
        True: if the value is valid in the row
        False: If the value is not valid
    """
    for col in range(self.cols):
      if value == self.puzzle[row][col]:
        return False
    return True
  

  def check_col(self, col, value):
    """
      Checks if the value is unique in the specific column
      Parameters
      ----------
      col : Integer
          The number of column 
      value: Integer
          The possible number for this row
      
      Returns
      -------
      Boolean
        True: if the value is valid in the column
        False: If the value is not valid
    """
    for row in range(self.rows):
      if value == self.puzzle[row][col]:
        return False
    return True
  

  def check_sqaure(self, row, col, value):
    """
      Checks if the value is unique in the specific square
      First caluclate the square and the checks if exists number
      with the same value in this square
      Parameters
      ----------
      row : Integer
          The number of row 
      col : Integer
          The number of column 
      value: Integer
          The possible number for this row
      
      Returns
      -------
      Boolean
        True: if the value is valid 
        False: If the value is not valid
    """
    square_row_start = (row // 3) * 3
    square_col_start = (col // 3) * 3

    for row in range(square_row_start, square_row_start + 3):
      for col in range(square_col_start, square_col_start + 3):
        if self.puzzle[row][col] == value:
          return False
    return True
  

  def find_first_epty_slot(self):
    """
     Find the first slot in the puzzle with value 0, which means that the slot in empty
      Returns
      -------
      Integer, Integer
        row: the number of row of the first empty slot
        col: the number of col of the first empty slot
    """
    for row in range(self.cols):
      for col in range(self.rows):
        if self.puzzle[row][col] == 0:
          return row, col


  def extend_node(self):
    """
     Extends the current node, creating a new instance of Sudoku for each valid number
      Returns
      -------
      List
        List with all valid new nodes
    """
    row, col = self.find_first_epty_slot()
    new_puzzles = []
    for number in range(1, 9+1):
      if self.check_row(row, number) and self.check_col(col, number) and self.check_sqaure(row, col, number):
        new_puzzle = deepcopy(self.puzzle)
        new_puzzle[row][col] = number
        new_puzzles.append(Sudoku(new_puzzle))
    return new_puzzles

  

  def is_the_solution(self):
    """
     Checks if the current node is the solution
      Returns
      -------
      Boolean
        True: if the puzzle has not empty slots
        False: if puzzle has empty slots
    """
    for row in range(self.rows):
      for col in range(self.cols):
        if self.puzzle[row][col] == 0:
          return False
    return True

  
  def __str__(self):
    """
     Returns the sudoku board in order to be printed properly
      Returns
      -------
      str
        the board of the sudoku
    """
    sudoku = ""
    for row in range(self.rows):
      for col in range(self.cols):
        sudoku += f"{self.puzzle[row][col]} "
      sudoku += "\n"
    return sudoku

def main():
  """
    Call the read_data function and then creates a new sudoku object.
    Finally creates an instance of DFS class, execute the algorithm
    and prints the resutls of the algorithm 
  """

  filename = input("Please enter the number of the text file: ")
  filename += ".txt"
  data = read_data(filename)

  if data is not None:
    sudoku = Sudoku(data)
    print("Depth First Search")
    dfs = DFS(sudoku)
    dfs.search()
  else:
    print("This file does not exit. Please enter another file name")


if __name__ == '__main__':
  main()