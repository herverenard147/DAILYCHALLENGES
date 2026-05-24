from game import Game


def get_user_menu_choice():
    """Affiche le menu et retourne le choix de l'utilisateur (avec validation)."""
    print("=" * 35)
    print("  ROCK  PAPER  SCISSORS")
    print("=" * 35)
    print("  [p] Play a new game")
    print("  [s] Show scores")
    print("  [q] Quit")
    print("=" * 35)

    valid = ["p", "s", "q"]
    choice = input("Your choice: ").strip().lower()

    if choice not in valid:
        print(f"Invalid option '{choice}'. Please choose p, s or q.")
        return None        # la boucle principale redemandera

    return choice


def print_results(results):
    """Affiche le récapitulatif des parties jouées.

    Args:
        results (dict): {"win": int, "loss": int, "draw": int}
    """
    total = sum(results.values())
    print("\n" + "=" * 35)
    print("  GAME SUMMARY")
    print("=" * 35)
    print(f"  Games played : {total}")
    print(f"  Wins         : {results['win']}")
    print(f"  Losses       : {results['loss']}")
    print(f"  Draws        : {results['draw']}")
    print("=" * 35)
    print("  Thanks for playing! See you next time.")
    print("=" * 35 + "\n")


def main():
    """Boucle principale du programme."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice is None:
            # Choix invalide → on réaffiche le menu
            continue

        elif choice == "p":
            # Lancer une partie
            game   = Game()
            result = game.play()          # retourne 'win', 'loss' ou 'draw'
            results[result] += 1          # mise à jour du compteur

        elif choice == "s":
            # Afficher les scores en cours
            print_results(results)

        elif choice == "q":
            # Quitter → afficher le résumé final
            print("\nThanks for playing!")
            print_results(results)
            break


if __name__ == "__main__":
    main()