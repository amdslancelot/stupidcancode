import pprint
pp = pprint.PrettyPrinter(indent=4)

class ChessBoard:

    def __init__(self, board):
        # chess: player(w/b) + chess kind(1-7) + chess seq(a-h)
        if board:
            self.board = board
        else:
            self.board = [
                ["w3a","w6a",None,None,None,None,"b7a","b3a"],
                ["w5a","w6b",None,None,None,None,"b7b","b5a"],
                ["w4a","w6c",None,None,None,None,"b7c","b4a"],
                ["w2" ,"w6d",None,None,None,None,"b7d","b2" ],
                ["w1" ,"w6e",None,None,None,None,"b7e","b1" ],
                ["w4b","w6f",None,None,None,None,"b7f","b4b"],
                ["w5b","w6g",None,None,None,None,"b7g","b5b"],
                ["w3b","w6h",None,None,None,None,"b7h","b3b"]
            ]
        print "board:"
        pp.pprint(self.board)
        print

        self.len_x = len(self.board)
        self.len_y = len(self.board[0])
       
        # Locate players' chesses 
        self.player_white, self.player_black = {}, {}
        for i in xrange(self.len_x):
            for j in xrange(self.len_y):
                chess = self.board[i][j]
                if not chess:
                    continue #skip
                if chess[0] == "w":
                     self.player_white[chess] = [i,j,False] # [x, y, moved]
                if chess[0] == "b":
                     self.player_black[chess] = [i,j,False] # [x, y, moved]
        
        # Chess kind
        self.king    = "1"
        self.queen   = "2"
        self.rook    = "3"
        self.bishop  = "4"
        self.knight  = "5"
        self.wpawn   = "6"
        self.bpawn   = "7"

        self.move_dirs = {
            self.king   : [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]],
            self.queen  : [[-1,1],[0,1],[1,1],[-1,0],[1,0],[-1,-1],[0,-1],[1,-1]],
            self.rook   : [[0,1],[-1,0],[1,0],[0,-1]],
            self.bishop : [[-1,1],[1,1],[-1,-1],[1,-1]],
            self.knight : [[-1,2],[1,2],[-2,1],[2,1],[-2,-1],[2,-1],[-1,-2],[1,-2]],
            self.wpawn  : [[0,1]],
            self.bpawn  : [[0,-1]],
        }

        self.move_steps = {
            self.king   : 1,
            self.queen  : -1,
            self.rook   : -1,
            self.bishop : -1,
            self.knight : 1,
            self.wpawn  : 1,
            self.bpawn  : 1,
        }

        self.cap_dirs = {
            self.king   : self.move_dirs[self.king],
            self.queen  : self.move_dirs[self.queen],
            self.rook   : self.move_dirs[self.rook],
            self.bishop : self.move_dirs[self.bishop],
            self.knight : self.move_dirs[self.knight],
            self.wpawn  : [[-1,1],[0,1],[1,1]],
            self.bpawn  : [[-1,-1],[0,-1],[1,-1]],
        }


    def play(self, player):
        r = []
        if player == "white":
            for chess,info in self.player_white.items():
                r += self.move(info[0], info[1], chess)
        elif player == "black":
            for chess,info in self.player_black.items():
                r += self.move(info[0], info[1], chess)
        else:
            print "[error] play"

        return self.print_result(player, r)
    
    def move(self, x, y, chess):
        r = [] #move options
        if not chess:
            return None
        
        chesskind  = chess[1]
        move_dirs  = self.move_dirs[chesskind]
        move_steps = self.move_steps[chesskind]
        cap_dirs   = self.cap_dirs[chesskind]
        
        #move
        for direc in move_dirs:
            new_x, new_y = (x + direc[0]), (y + direc[1])
            count = move_steps
            
            #If is unmoved Pawn
            if chess[0] == "w" and chess[1] == self.wpawn and not self.player_white[chess][2]:
                count += 1
            if chess[0] == "b" and chess[1] == self.bpawn and not self.player_black[chess][2]:
                count += 1
            
            while count != 0 and self.isInBoard(new_x, new_y) and not self.board[new_x][new_y]:
                r.append([x, y, chess, new_x, new_y]) #added!
                new_x, new_y = (new_x + direc[0]), (new_y + direc[1])
                if move_steps != -1: #move limited steps
                    count -= 1

        #capture
        for direc in cap_dirs:
            new_x, new_y = (x + direc[0]), (y + direc[1])
            count = move_steps
            while count != 0 and self.isInBoard(new_x, new_y) and ( not self.board[new_x][new_y] or (self.board[new_x][new_y] and self.board[new_x][new_y][0] != chess[0]) ):
                if not self.board[new_x][new_y]: #Empty, keep going
                    new_x, new_y = (new_x + direc[0]), (new_y + direc[1])
                    if move_steps != -1: #move limited steps
                        count -= 1
                    continue
                if self.board[new_x][new_y] and self.board[new_x][new_y][0] != chess[0]: #found enemy
                    r.append([x, y, chess, new_x, new_y])
                    count = 0 #stop early

        return r
            
    def isInBoard(self, x, y):
        if x >= 0 and x < self.len_x and y >= 0 and y < self.len_y:
            return True
        return False
    
    def parseMove(self, x, y, chess, new_x, new_y):
        kind = ""
        if chess[1] == self.king:
            kind = "King"
        if chess[1] == self.queen:
            kind = "Queen"
        if chess[1] == self.rook:
            kind = "Rook"
        if chess[1] == self.bishop:
            kind = "Bishop"
        if chess[1] == self.knight:
            kind = "Knight"
        if chess[1] in [self.wpawn, self.bpawn]:
            kind = "Pawn"
        return "%s at <%s:%s> can move to <%s:%s>" % (kind, chr(x+65), y+1, chr(new_x+65), new_y+1)

    def print_result(self, player, r):
        m = {}
        new_r = []
        for e in r:
            if e[2] not in m:
                m[e[2]] = 1

            new_r.append(self.parseMove(e[0], e[1], e[2], e[3], e[4]))

        new_r.append("%s legal moves (%s unique pieces) for %s player" % (len(r), len(m.keys()), player) )
        for s in new_r:
            print s
       
        return new_r 

if __name__ == "__main__":
    game = ChessBoard(None)
    game.play("white")
