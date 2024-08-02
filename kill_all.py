class Chessboard:
    def __init__(self, size=8):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.castle = None
        self.soldiers = []

    def add_soldier(self, x, y):
        self.board[x][y] = 'S'
        self.soldiers.append((x, y))

    def place_castle(self, x, y):
        self.castle = (x, y)
        self.board[x][y] = 'C'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def find_home(self):
        if not self.castle:
            return "Castle not placed on the board."

        path = []
        current_x, current_y = self.castle
        path.append((current_x, current_y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        direction = 0

        while True:
            move_made = False
            next_x, next_y = current_x + directions[direction][0], current_y + directions[direction][1]

            while 0 <= next_x < self.size and 0 <= next_y < self.size:
                if self.board[next_x][next_y] == 'S':
                    path.append((next_x, next_y))
                    self.board[next_x][next_y] = '.'
                    current_x, current_y = next_x, next_y
                    direction = (direction + 1) % 4
                    move_made = True
                    break
                next_x += directions[direction][0]
                next_y += directions[direction][1]

            if not move_made:
                break

        return path

def main():
    board = Chessboard()

    num_soldiers = int(input("Enter number of soldiers: "))
    for i in range(num_soldiers):
        x, y = map(int, input(f"Enter coordinates for soldier {i + 1} (row,col): ").split(','))
        board.add_soldier(x - 1, y - 1)  # Convert to 0-based index

    castle_x, castle_y = map(int, input("Enter coordinates for the castle (row,col): ").split(','))
    board.place_castle(castle_x - 1, castle_y - 1)  # Convert to 0-based index

    print("\nInitial Board:")
    board.print_board()

    path = board.find_home()

    print("Path taken by the castle:")
    for step in path:
        print(f"({step[0] + 1},{step[1] + 1})")  # Convert to 1-based index for output

if __name__ == "__main__":
    main()
