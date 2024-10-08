from chess import Board

def perform_tests():
    board = Board()
    board.display()
    print()
    # Move a pawn
    board.move_piece((6, 0), (4, 0))
    board.display()


def main():
    perform_tests()


if __name__ == "__main__":
    main()

