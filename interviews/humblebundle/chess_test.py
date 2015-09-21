from chess import ChessBoard

if __name__ == "__main__":
    #test
    board = [
        [None ,None,"w3a",None,None,None,"b7a","b3a"],
        ["w5a","w6b",None,None,None,None,"b7b","b5a"],
        ["w4a","w6c",None,None,None,None,"b7c","b4a"],
        [None,None,"w2",None,None,None,"b7d","b2" ],
        ["w1" ,"w6e",None,None,None,None,"b7e","b1" ],
        ["w4b","w6f",None,None,None,None,"b7f","b4b"],
        ["w5b","w6g",None,None,None,None,"b7g","b5b"],
        ["w3b","w6h",None,None,None,None,"b7h","b3b"]
    ]
    game = ChessBoard(board)
    print "White Player plays:"
    game.play("white")
    print
    print "Black Player plays:"
    game.play("black")
    print
