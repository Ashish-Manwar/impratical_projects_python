import random
import collections
import math
import itertools

# --- Card and Deck Definitions ---

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, 2)}
VALUE_RANKS = {v: k for k, v in RANK_VALUES.items()}


class Card:
    """Represents a single playing card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """String representation of a card."""
        return f"{self.rank}{self.suit}"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __hash__(self):
        return hash((self.suit, self.rank))

class Deck:
    """Represents a deck of 52 playing cards."""
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.shuffle()

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def deal(self, num_cards):
        """Deals a specified number of cards from the top of the deck."""
        if num_cards > len(self.cards):
            return []
        dealt = [self.cards.pop() for _ in range(num_cards)]
        return dealt

# --- Hand Evaluation Logic ---

def evaluate_hand(hand):
    """
    Evaluates a 5-card hand and returns its rank, descriptive name, and high card values for tie-breaking.
    """
    if not hand or len(hand) != 5:
        return 0, "Invalid Hand", []

    ranks = sorted([RANK_VALUES[card.rank] for card in hand], reverse=True)
    suits = [card.suit for card in hand]
    rank_counts = collections.Counter(ranks)
    
    is_flush = len(set(suits)) == 1
    
    is_straight = False
    unique_ranks = sorted(list(set(ranks)), reverse=True)
    if len(unique_ranks) == 5:
        if unique_ranks[0] - unique_ranks[4] == 4:
            is_straight = True
        elif set(unique_ranks) == {14, 5, 4, 3, 2}:
            is_straight = True
            ranks = [5, 4, 3, 2, 14] 

    if is_straight and is_flush:
        return (9, "Straight Flush", ranks)
    if 4 in rank_counts.values():
        major_rank = [r for r, c in rank_counts.items() if c == 4][0]
        minor_rank = [r for r, c in rank_counts.items() if c == 1][0]
        return (8, "Four of a Kind", [major_rank] * 4 + [minor_rank])
    if 3 in rank_counts.values() and 2 in rank_counts.values():
        major_rank = [r for r, c in rank_counts.items() if c == 3][0]
        minor_rank = [r for r, c in rank_counts.items() if c == 2][0]
        return (7, "Full House", [major_rank] * 3 + [minor_rank] * 2)
    if is_flush:
        return (6, "Flush", ranks)
    if is_straight:
        return (5, "Straight", ranks)
    if 3 in rank_counts.values():
        major_rank = [r for r, c in rank_counts.items() if c == 3][0]
        kickers = sorted([r for r, c in rank_counts.items() if c == 1], reverse=True)
        return (4, "Three of a Kind", [major_rank] * 3 + kickers)
    if list(rank_counts.values()).count(2) == 2:
        pairs = sorted([r for r, c in rank_counts.items() if c == 2], reverse=True)
        kicker = [r for r, c in rank_counts.items() if c == 1][0]
        return (3, "Two Pair", [pairs[0]]*2 + [pairs[1]]*2 + [kicker])
    if 2 in rank_counts.values():
        pair_rank = [r for r, c in rank_counts.items() if c == 2][0]
        kickers = sorted([r for r, c in rank_counts.items() if c == 1], reverse=True)
        return (2, "One Pair", [pair_rank]*2 + kickers)
    
    return (1, "High Card", ranks)

def find_best_hand(cards):
    """Finds the best 5-card hand from a list of 5 to 7 cards."""
    if len(cards) < 5:
        return 0, "Not enough cards", []
    
    best_hand_so_far = (0, "No Hand", [])
    
    for combo in itertools.combinations(cards, 5):
        current_eval = evaluate_hand(list(combo))
        if current_eval[0] > best_hand_so_far[0]:
            best_hand_so_far = current_eval
        elif current_eval[0] == best_hand_so_far[0] and current_eval[2] > best_hand_so_far[2]:
                 best_hand_so_far = current_eval

    return best_hand_so_far

# --- New Comprehensive Probability Analysis ---

HAND_RANKINGS_CHART = {
    9: "Straight Flush", 8: "Four of a Kind", 7: "Full House",
    6: "Flush", 5: "Straight", 4: "Three of a Kind",
    3: "Two Pair", 2: "One Pair", 1: "High Card"
}

def calculate_all_hand_probabilities(player_cards, community_cards, deck):
    """
    Simulates all possible future cards to calculate the probability of making each hand rank.
    """
    print("\n======================================================")
    print("      COMPREHENSIVE PROBABILITY ANALYSIS")
    print("======================================================")
    
    # Determine the remaining deck
    seen_cards = set(player_cards + community_cards)
    remaining_deck = [card for card in deck.cards if card not in seen_cards]
    
    num_remaining_cards = len(remaining_deck)
    stage = ""
    
    # Determine which stage we're in and set up the simulation
    if len(community_cards) == 3: # Flop
        stage = "Flop"
        possible_outcomes = list(itertools.combinations(remaining_deck, 2))
        print(f"Simulating all {len(possible_outcomes)} possible Turn/River combinations...")
    elif len(community_cards) == 4: # Turn
        stage = "Turn"
        possible_outcomes = list(itertools.combinations(remaining_deck, 1))
        print(f"Simulating all {len(possible_outcomes)} possible River cards...")
    else:
        return

    # Run the simulation
    hand_counts = collections.defaultdict(int)
    for outcome in possible_outcomes:
        final_cards = player_cards + community_cards + list(outcome)
        best_hand_rank = find_best_hand(final_cards)[0]
        hand_counts[best_hand_rank] += 1
        
    total_outcomes = len(possible_outcomes)
    
    # Display the results
    print("\n--- Your Probability of Making Each Hand by the River ---")
    print(f"{'Poker Hand':<20} | {'Probability':<15} | {'How It Is Calculated'}")
    print("-" * 60)
    
    # Get your current best hand rank to compare against
    current_best_rank = find_best_hand(player_cards + community_cards)[0]

    for rank in sorted(HAND_RANKINGS_CHART.keys(), reverse=True):
        hand_name = HAND_RANKINGS_CHART[rank]
        count = hand_counts[rank]
        
        # We only care about improving our hand
        if rank > current_best_rank:
            probability = (count / total_outcomes) * 100 if total_outcomes > 0 else 0
            if probability > 0.001: # Don't show negligible probabilities
                print(f"{hand_name:<20} | {probability:>6.2f}%          | ({count} outcomes / {total_outcomes} total)")

    print("-" * 60)
    print("\nStrategic Advice:")
    print("Look at the percentages. A high chance (15%+) to make a strong hand (Straight, Flush, etc.)")
    print("means you have a strong draw. A low chance (<5%) means you are likely relying on luck.")
    print("This table shows you EXACTLY what you are paying to see the next cards for.")
    print("======================================================")


# --- Main Application Logic ---

def print_hand_rankings():
    """Prints a clear chart of poker hand rankings."""
    print("="*40)
    print("         POKER HAND RANKINGS")
    print("(From Best to Worst)")
    print("----------------------------------------")
    for rank in sorted(HAND_RANKINGS_CHART.keys(), reverse=True):
        print(f"  {rank}. {HAND_RANKINGS_CHART[rank]}")
    print("="*40)

def main():
    """Main function to run the poker probability application."""
    print("♠ ♥ ♦ ♣ Welcome to the Comprehensive Poker Trainer! ♣ ♦ ♥ ♠")
    print_hand_rankings()
    
    while True:
        # A fresh, ordered deck is created for each hand for simulation purposes
        full_deck = Deck() 
        
        # A shuffled deck is used for dealing the actual game
        shuffled_deck = Deck()
        
        # --- Pre-Flop ---
        print("\n--- PRE-FLOP ---")
        player_hand = shuffled_deck.deal(2)
        dealer_hand = shuffled_deck.deal(2)
        
        print(f"Your Hole Cards: {' '.join(map(str, player_hand))}")
        
        is_pair = player_hand[0].rank == player_hand[1].rank
        is_suited = player_hand[0].suit == player_hand[1].suit
        
        if is_pair: print(f"Analysis: You have a pocket pair! A strong starting hand.")
        if is_suited: print(f"Analysis: Your cards are 'suited', improving flush chances.")

        input("\nPress Enter to see the flop...")
        
        # --- Flop ---
        print("\n--- FLOP ---")
        community_cards = shuffled_deck.deal(3)
        print(f"Community Cards: {' '.join(map(str, community_cards))}")
        
        current_hand_eval = find_best_hand(player_hand + community_cards)
        print(f"\nYour best hand right now is: {current_hand_eval[1]}")
        
        calculate_all_hand_probabilities(player_hand, community_cards, full_deck)

        input("\nPress Enter to see the turn...")
        
        # --- Turn ---
        print("\n--- TURN ---")
        turn_card = shuffled_deck.deal(1)
        community_cards.extend(turn_card)
        print(f"Turn Card: {turn_card[0]}")
        print(f"Full Board: {' '.join(map(str, community_cards))}")

        current_hand_eval = find_best_hand(player_hand + community_cards)
        print(f"\nYour best hand is now: {current_hand_eval[1]}")
        
        calculate_all_hand_probabilities(player_hand, community_cards, full_deck)

        input("\nPress Enter to see the river...")
        
        # --- River & Showdown ---
        print("\n--- RIVER & SHOWDOWN ---")
        river_card = shuffled_deck.deal(1)
        community_cards.extend(river_card)
        print(f"Final Board: {' '.join(map(str, community_cards))}")
        
        player_final = find_best_hand(player_hand + community_cards)
        dealer_final = find_best_hand(dealer_hand + community_cards)
        
        print(f"\nYour final hand ({' '.join(map(str, player_hand))}): {player_final[1]}")
        print(f"Dealer's final hand ({' '.join(map(str, dealer_hand))}): {dealer_final[1]}")
        
        # Determine winner
        winner = ""
        if player_final[0] > dealer_final[0]: winner = "You win!"
        elif dealer_final[0] > player_final[0]: winner = "The Dealer wins!"
        else:
            if player_final[2] > dealer_final[2]: winner = f"You win with a better kicker!"
            elif dealer_final[2] > player_final[2]: winner = f"The Dealer wins with a better kicker!"
            else: winner = "It's a tie! The pot is split."

        print(f"\n--- RESULT: {winner} ---")
        
        # --- Ask to play again ---
        print("-" * 28)
        again = input("Deal another hand? (yes/no): ").lower()
        if again not in ['yes', 'y']:
            print("\nThanks for playing! Happy learning!")
            break

if __name__ == "__main__":
    main()

