
class TicTacToeBoard:
    def __init__(self):
        self.moves = []
        self.board = [[-1, -1, -1],
                      [-1, -1, -1],
                      [-1, -1, -1]]
    

    def valid_moves(self):
        valid_moves = []
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == -1:
                    valid_moves.append((y, x))
        return valid_moves

    def is_win(self, player):
        for y in range(3):
            if len(set(self.board[y])) == 1 and self.board[y][0] == player: 
                return True
        
        for x in range(3):
            vals = set(row[x] for row in self.board)

            if len(vals) == 1 and self.board[0][x] == player: 
                return True

        

    def make_move(self, player, x, y):
        self.board[y][x] = player
        self.moves.append((player, x, y))


    def eval_position(self, player, opponent):
        max_score = None
        best_move = None
        score = 0
        games = []

        def backtrack(active, curr_moves):
            curr_board = TicTacToeBoard()
            for x, y, p in curr_moves:
                curr_board.make_move(p, x, y)

            #while not curr_board.is_win(player) and not curr_board.is_win(opponent) and curr_board.valid_moves():
            #    valid_moves = curr_board.valid_moves()
                

            
            
            if curr_board.is_win(player):
                games.append(curr_moves[::], 1)
                return
            
            elif curr_board.is_win(opponent):
                games.append(curr_moves[::], 2)
            
            elif not curr_board.valid_moves():
                games.append(curr_moves[::], 3)

            valid_moves = curr_board.valid_moves()
            
            for x, y in valid_moves:
                curr_moves.append((active, x, y))

                if active == player:
                    backtrack(opponent, curr_moves)
                else:
                    backtrack(player, curr_moves)
                curr_moves.pop()
        
        backtrack(player, self.moves)
       
        max_score = 0
        best_move = None
        for valid_move in self.board.valid_moves():
            score = 0
            for g in games:
                if g[0][0] == valid_move:
                    if g[1] == 1: #win
                        score += 5
                    if g[1] == 2: #loss
                        score -= 5
                    if g[1] == 3: #tie
                        pass
            if score > max_score:
                max_score = score
                best_move = valid_move
        
        return best_move
            

            


board = TicTacToeBoard()
print(board.valid_moves())
print(board.make_move(1, 1, 1))
print(board.make_move(1, 0, 1))
print(board.make_move(1, 0, 0))
print(board.board)
print(board.valid_moves())
print(board.eval_position(1, 2))


