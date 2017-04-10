from deuces import Deck, Evaluator
import pandas as pd


def build_dataframe(nb_hands=1000):
    decks = [ Deck() for _ in range(nb_hands) ]
    boards = [ deck.draw(5) for deck in decks ]
    player1 = [ deck.draw(2) for deck in decks ]
    player2 = [ deck.draw(2) for deck in decks ]

    e = Evaluator()
    score1 = [ e.evaluate(b, h) for (b, h) in zip(boards, player1) ]
    score2 = [ e.evaluate(b, h) for (b, h) in zip(boards, player2) ]

    return pd.DataFrame({'score1': score1, 'score2': score2})
