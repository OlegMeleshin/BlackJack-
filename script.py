from game import *
g = Game()

while True:
    start = input(" Press Enter for New round, q to quit: ")
    if start == "q":
        break

    cards_left = g.deck.cards_left()
    if cards_left < 20:
        g.deck.new_deck()

    """New game"""
    print("new game")
    deal = g.first_turn()
    if deal == "End round":
        g.player.new_hand()
        g.dealer.new_hand()
        continue

    player_turn = g.player_lead()
    if player_turn == "Robot`s turn":
        robot_turn = g.robot_turn()
        if robot_turn == "Robot stand":
            g.finalle()
            g.player.hand.clear()
            g.dealer.hand.clear()
    """Игроки сбрасывают карты"""
    g.player.new_hand()
    g.dealer.new_hand()


                    
            
        
    

 



        

        
    
        
