def calculateScores():
    score1 = 0
    with open("02\input.txt") as file:
        rounds = file.readlines()

    print(rounds)


    # A - rock, B - paper, C - scissors
    # 1 - rock, 2 - paper, 3 - scissors
    # 0 - loss, 3 - draw, 6 - win

    # First half of task
    for round in rounds:
        # score1 from the selected shape
        if "X" in round:
            score1+=1
        if "Y" in round: 
            score1+=2
        if "Z" in round:
            score1+=3

        # score1 from the round outcome
        # 1) tie; 2) rock crushes scissors; 3) paper covers rock; 4) scissors cut paper.
        if ("A" in round and "X" in round) or ("B" in round and "Y" in round) or ("C" in round and "Z" in round): # Draw
            score1+=3
        elif ("X" in round): 
            if ("C" in round):
                score1+=6
            else:
                score1+=0
        elif ("Y" in round): 
            if ("A" in round):
                score1+=6
            else:
                score1+=0
        elif ("Z" in round): 
            if ("B" in round):
                score1+=6
            else:
                score1+=0
    
    print(score1)

    score2 = 0
    # X - lose, Y - draw, Z - win
    # A - rock, B - paper, C - scissors
    # 1 - rock, 2 - paper, 3 - scissors
    # 0 - loss, 3 - draw, 6 - win
    # Second half of task
    for round in rounds:
        # score1 from the selected shape
        if "X" in round:
            score2+=0
            # lose
            if "A" in round:
                score2+=3
            elif "B" in round:
                score2+=1
            elif "C" in round:
                score2+=2
        if "Y" in round: 
            score2+=3
            # draw
            if "A" in round:
                score2+=1
            elif "B" in round:
                score2+=2
            elif "C" in round:
                score2+=3
        if "Z" in round:
            score2+=6
            # win
            if "A" in round:
                score2+=2
            elif "B" in round:
                score2+=3
            elif "C" in round:
                score2+=1

    print(score2)
    
if __name__ == '__main__':
    calculateScores()