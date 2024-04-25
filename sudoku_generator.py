import pygame
import math, random

"""
This was adapted from a GeeksforGeeks article "Program for Sudoku Generator" by Aarti_Rathi and Ankur Trisal
https://www.geeksforgeeks.org/program-sudoku-generator/
"""

class SudokuGenerator:
    """
    create a sudoku board - initialize class variables and set up the 2D board
    This should initialize:
    self.row_length		- the length of each row
    self.removed_cells	- the total number of cells to be removed
    self.board			- a 2D list of ints to represent the board
    self.box_length		- the square root of row_length
    
    Parameters:
    row_length is the number of rows/columns of the board (always 9 for this project)
    removed_cells is an integer value - the number of cells to be removed
    
    Return:
    None
    """
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = int(self.row_length ** 0.5)
        self.board = [[0 for j in range(9)] for i in range(9)]
        self.diagonal = False

    """
    Returns a 2D python list of numbers which represents the board

    Parameters: None
    Return: list[list]
    """
    def get_board(self):
        return self.board

    """
    Displays the board to the console
    This is not strictly required, but it may be useful for debugging purposes
    Parameters: None
    Return: None
    """
    def print_board(self):
        for row in self.board:
            print(row)

    """
    Determines if num is contained in the specified row (horizontal) of the board
    If num is already in the specified row, return False. Otherwise, return True

    Parameters:
    row is the index of the row we are checking
    num is the value we are looking for in the row
    
    Return: boolean
    """
    def valid_in_row(self, row, num):
        for col in range(len(self.board[row])):
            if num == self.board[row][col]:
                return False
        return True

    """
    Determines if num is contained in the specified column (vertical) of the board
    If num is already in the specified col, return False. Otherwise, return True

    Parameters:
    col is the index of the column we are checking
    num is the value we are looking for in the column
    
    Return: boolean
    """
    def valid_in_col(self, col, num):
        for row in range(len(self.board)):
            if num == self.board[row][col]:
                return False
        return True

    """
    Determines if num is contained in the 3x3 box specified on the board
    If num is in the specified box starting at (row_start, col_start), return False.
    Otherwise, return True

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    num is the value we are looking for in the box

    Return: boolean
    """
    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if num == self.board[row][col]:
                    return False
        return True

    """
    Determines if it is valid to enter num at (row, col) in the board
    This is done by checking that num is unused in the appropriate, row, column, and box

    Parameters:
    row and col are the row index and col index of the cell to check in the board
    num is the value to test if it is safe to enter in this cell

    Return: boolean
    """
    def is_valid(self, row, col, num):
        row_start, col_start = 0, 0
        row = int(row)
        col = int(col)
        num = int(num)
        
        # find col_start of box
        if 0 <= col <= 2:
            col_start = 0
        if 3 <= col <= 5:
            col_start = 3
        if 6 <= col <= 8:
            col_start = 6
        # find row_start of box
        if 0 <= row <= 2:
            row_start = 0
        if 3 <= row <= 5:
            row_start = 3
        if 6 <= row <= 8:
            row_start = 6

        if self.valid_in_box(row_start, col_start, num):
            if self.valid_in_col(col, num):
                if self.valid_in_row(row, num):
                    return True

        """print(f"valid_in_box = {self.valid_in_box(row_start, col_start, num)}")
        print(f"valid_in_col = {self.valid_in_col(col, num)}")
        print(f"valid_in_box = {self.valid_in_box(row_start, col_start, num)}")"""

        return False

    """
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

    Parameters:
    row_start and col_start are the starting indices of the box to check
    i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    Return: None
    """
    def fill_box(self, row_start, col_start):
        valid_nums = [i for i in range(1, 10, 1)]
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                num = valid_nums[random.randrange(0, len(valid_nums), 1)]
                self.board[row][col] = num
                valid_nums.remove(num)

    """
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

    Parameters: None
    Return: None
    """
    def fill_diagonal(self):
        if not self.diagonal:
            self.fill_box(0, 0)
            self.fill_box(3, 3)
            self.fill_box(6, 6)
            self.diagonal = True

    """
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
    
    Parameters:
    row, col specify the coordinates of the first empty (0) cell

    Return:
    boolean (whether or not we could solve the board)
    """
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    """
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

    Parameters: None
    Return: None
    """
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    """
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
    
    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

    Parameters: None
    Return: None
    """
    def remove_cells(self):
        removed = 0
        while removed < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.board[row][col] == 0:
                continue
            else:
                self.board[row][col] = 0
                removed += 1

class Cell:
    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.value = value

    def draw(self):
        # Draws this cell, along with the value inside it.
        # If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell.
        # The cell is outlined red if it is currently selected.
        pass

class Board:
    def __init__(self, width, height, screen, difficulty):
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the user chose easy, medium, or hard.
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.generator = SudokuGenerator(9, self.difficulty)
        self.generator.fill_values()
        self.generator.remove_cells()
        original_board = self.generator.get_board()
        self.original_board = [[j for j in original_board[i]] for i in range(len(original_board))]
        self.cells = [[Cell(self.generator.board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]
        self.selected_cell = None
        self.selected = False

    def draw(self):
        # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.
        pass

    def select(self, row, col):
        # Marks the cell at (row, col) in the board as the current selected cell.
        # Once a cell has been selected, the user can edit its value or sketched value.
        self.selected_cell = self.cells[row][col]
        self.selected = True

    def click(self, x, y):
        # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
        # of the cell which was clicked. Otherwise, this function returns None.
        pass

    def clear(self):
        # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
        # filled by themselves.
        self.selected_cell.set_sketched_value(0)
        self.selected_cell.set_cell_value(0)

    def sketch(self, value):
        # Sets the sketched value of the current selected cell equal to user entered value.
        # It will be displayed at the top left corner of the cell using the draw() function.
        self.selected_cell.set_sketched_value(value)


    def place_number(self, value):
        # Sets the value of the current selected cell equal to user entered value.
        # Called when the user presses the Enter key.
        self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit).
        self.cells =  [[Cell(self.original_board[row][col], row, col, self.screen) for col in range(9)] for row in range(9)]


    def is_full(self):
        # Returns a Boolean value indicating whether the board is full or not.
        for row in range(len(self.cells)):
            for cell in self.cells[row]:
                if cell.value == 0:
                    return False
        return True

    def update_board(self):
        # Updates the underlying 2D board with the values in all cells.
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.generator.board[row][col] = self.cells[row][col].value

    def find_empty(self):
        # Finds an empty cell and returns its row and col as a tuple (x, y).
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                cell = self.cells[row][col]
                if cell.value == 0:
                    return row, col
        return None

    def check_board(self):
        # Check whether the Sudoku board is solved correctly.
        valid = 0
        self.update_board()
        for row in range(len(self.generator.board)):
            for col in range(len(self.generator.board)):
                if self.generator.is_valid(row, col, self.generator.board[row][col]):
                    valid += 1
        if valid == 9*9 :
            return True
        else:
            return False


'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board