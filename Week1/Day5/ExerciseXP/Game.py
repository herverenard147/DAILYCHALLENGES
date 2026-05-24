import random


class Game:

    def get_user_item(self):
        """Demande à l'utilisateur de choisir rock / paper / scissors.
        Recommence tant que le choix n'est pas valide."""
        choices = ["rock", "paper", "scissors"]
        while True:
            user_input = input("Choose rock, paper or scissors: ").strip().lower()
            if user_input in choices:
                return user_input
            print(f"Invalid choice '{user_input}'. Please type rock, paper or scissors.")

    def get_computer_item(self):
        """Retourne un choix aléatoire parmi rock / paper / scissors."""
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        """Compare les deux choix et retourne 'win', 'loss' ou 'draw'."""
        if user_item == computer_item:
            return "draw"

        winning_combos = {
            "rock":     "scissors",   # rock bat scissors
            "scissors": "paper",      # scissors bat paper
            "paper":    "rock",       # paper bat rock
        }

        if winning_combos[user_item] == computer_item:
            return "win"
        return "loss"

    def play(self):
        """Point d'entrée principal du jeu.
        Retourne le résultat : 'win', 'loss' ou 'draw'."""
        user_item     = self.get_user_item()
        computer_item = self.get_computer_item()
        result        = self.get_game_result(user_item, computer_item)

        # Affichage du résultat
        result_msg = {
            "win":  "You win! 🎉",
            "loss": "You lose! 😢",
            "draw": "It's a draw! 🤝",
        }
        print(
            f"\nYou selected {user_item}. "
            f"The computer selected {computer_item}. "
            f"{result_msg[result]}\n"
        )

        return result   # 'win' | 'loss' | 'draw'