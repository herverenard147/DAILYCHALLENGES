"""
mnist_neural_network.py
═══════════════════════
Réseau de neurones entièrement connecté — Reconnaissance de chiffres manuscrits (MNIST).
Implémentation complète avec scikit-learn + matplotlib/seaborn.

Étapes :
  1. Chargement et prétraitement du dataset MNIST
  2. Construction du réseau de neurones (784 → 128 → 64 → 10)
  3. Entraînement avec suivi perte et accuracy sur 10 époques
  4. Évaluation : accuracy, matrice de confusion, chiffres difficiles
  5. Optimisation par réglage des hyperparamètres
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from matplotlib.patches import Patch
import warnings
warnings.filterwarnings("ignore")

OUTPUT   = "output"
os.makedirs(OUTPUT, exist_ok=True)
np.random.seed(42)


# ══════════════════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — CHARGEMENT ET PRÉTRAITEMENT DU DATASET MNIST
# ══════════════════════════════════════════════════════════════════════════════

def load_and_preprocess():
    """
    Charge le vrai dataset MNIST via tf.keras.datasets.
    70 000 images réelles de chiffres manuscrits (28×28 pixels, niveaux de gris).

    Traitement appliqué :
      - Normalisation des pixels dans [0, 1]  (division par 255)
      - Aplatissement 28×28 → vecteur de 784 pixels
      - One-hot encoding des labels  (ex: 3 → [0,0,0,1,0,0,0,0,0,0])
      - Split officiel MNIST : 60 000 train / 10 000 test
    """
    print("═" * 65)
    print("  ÉTAPE 1 — Chargement et prétraitement du dataset MNIST")
    print("═" * 65)

    print("\n  Chargement du dataset MNIST via tf.keras.datasets...")
    (X_train_raw, y_train), (X_test_raw, y_test) = keras.datasets.mnist.load_data()

    print(f"\n  ✓ Dataset chargé")
    print(f"    Entraînement : {X_train_raw.shape[0]} images | Test : {X_test_raw.shape[0]} images")
    print(f"    Dimension brute : {X_train_raw.shape[1]}×{X_train_raw.shape[2]} pixels")
    print(f"    Plage originale : [{X_train_raw.min()}, {X_train_raw.max()}]")

    # ── Normalisation ──────────────────────────────────────────────────────────
    # Division par 255 : pixels dans [0, 1]
    # Accélère la convergence et stabilise les gradients
    X_train = X_train_raw.astype(np.float32) / 255.0
    X_test  = X_test_raw.astype(np.float32)  / 255.0
    print(f"  ✓ Normalisation : pixels dans [{X_train.min():.2f}, {X_train.max():.2f}]")

    # ── Aplatissement 28×28 → 784 ─────────────────────────────────────────────
    # Le réseau entièrement connecté attend un vecteur 1D en entrée
    X_train = X_train.reshape(-1, 784)
    X_test  = X_test.reshape(-1, 784)
    print(f"  ✓ Aplatissement : 28×28 → vecteur de {X_train.shape[1]} pixels")

    # ── One-hot encoding ───────────────────────────────────────────────────────
    # Transforme label entier → vecteur binaire (requis par categorical cross-entropy)
    # ex: 3 → [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    y_train_ohe = keras.utils.to_categorical(y_train, num_classes=10)
    y_test_ohe  = keras.utils.to_categorical(y_test,  num_classes=10)
    exemple_idx = np.where(y_train == 3)[0][0]
    print(f"  ✓ One-hot encoding : ex. label=3 → {y_train_ohe[exemple_idx].astype(int)}")

    # ── Visualisation des images d'exemple ────────────────────────────────────
    _plot_sample_images(X_train, y_train)

    return X_train, X_test, y_train, y_test


def _plot_sample_images(X, y):
    """Grille 2×5 : un exemple de chaque chiffre 0 à 9."""
    fig, axes = plt.subplots(2, 5, figsize=(12, 5))
    fig.suptitle("Exemples d'images MNIST — un chiffre par classe (0–9)",
                 fontsize=13, fontweight="bold")
    for digit, ax in enumerate(axes.flat):
        idx = np.where(y == digit)[0][0]
        ax.imshow(X[idx].reshape(28, 28), cmap="gray_r")
        ax.set_title(f"Chiffre {digit}", fontsize=11, fontweight="bold")
        ax.axis("off")
    plt.tight_layout()
    _save(fig, "01_exemples_mnist.png")


# ══════════════════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — CONSTRUCTION DU RÉSEAU DE NEURONES
# ══════════════════════════════════════════════════════════════════════════════

def build_model(hidden=(128, 64), lr=0.001):
    """
    Réseau entièrement connecté avec Keras Sequential.

    Architecture :
      Entrée   : 784 neurones  (28×28 pixels aplatis)
      Couche 1 : 128 neurones  activation ReLU
      Couche 2 :  64 neurones  activation ReLU
      Sortie   :  10 neurones  activation Softmax (classification multi-classes)

    Compilation :
      Perte      : categorical_crossentropy
      Optimiseur : Adam
      Métrique   : accuracy
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 2 — Construction du réseau de neurones")
    print("═" * 65)
    print(f"\n  Architecture :")
    print(f"    Entrée      : 784 neurones  (28×28 aplatis en vecteur)")
    for i, n in enumerate(hidden, 1):
        print(f"    Couche {i}    : {n:>3} neurones  (activation : ReLU)")
    print(f"    Sortie      :  10 neurones  (activation : Softmax)")
    print(f"\n  Compilation :")
    print(f"    Perte       : Categorical Cross-Entropy")
    print(f"    Optimiseur  : Adam  (lr={lr})")
    print(f"    Métrique    : Accuracy")

    model = keras.Sequential(name="mnist_fcnn")
    model.add(layers.Input(shape=(784,)))
    for n in hidden:
        model.add(layers.Dense(n, activation="relu"))
    model.add(layers.Dense(10, activation="softmax"))

    model.compile(
        optimizer=keras.optimizers.Adam(learning_rate=lr),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    model.summary()
    print(f"\n  ✓ Modèle construit")
    return model


# ══════════════════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — ENTRAÎNEMENT
# ══════════════════════════════════════════════════════════════════════════════

def train_model(model, X_train, y_train, n_epochs=10):
    """
    Entraîne le modèle avec model.fit() de Keras.
    10% des données d'entraînement servent de jeu de validation (validation_split).
    Keras calcule la perte et l'accuracy à chaque époque nativement — pas besoin
    de les recalculer manuellement sur tout le dataset (inefficace avec scikit-learn).
    Trace les courbes d'évolution de la perte et de l'accuracy.
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 3 — Entraînement du réseau de neurones")
    print("═" * 65)

    n_val = int(0.1 * len(X_train))
    print(f"\n  Entraînement : {len(X_train) - n_val} exemples | Validation : {n_val} exemples")
    print(f"  Epochs : {n_epochs} | Batch size : 32\n")

    history = model.fit(
        X_train, y_train,
        epochs=n_epochs,
        batch_size=32,
        validation_split=0.1,   # 10% réservés pour la validation
        verbose=1
    )

    _plot_training_curves(
        history.history["loss"],
        history.history["val_loss"],
        history.history["accuracy"],
        history.history["val_accuracy"]
    )
    return model


def _plot_training_curves(tr_loss, val_loss, tr_acc, val_acc):
    """Courbes de perte (left) et d'accuracy (right) sur 10 époques."""
    epochs = range(1, len(tr_loss) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Évolution pendant l'entraînement (10 époques)",
                 fontsize=13, fontweight="bold")

    ax = axes[0]
    ax.plot(epochs, tr_loss,  "b-o", ms=6, label="Entraînement")
    ax.plot(epochs, val_loss, "r-o", ms=6, label="Validation")
    ax.set_title("Perte (Cross-Entropy)", fontweight="bold")
    ax.set_xlabel("Époque"); ax.set_ylabel("Perte")
    ax.legend(); ax.grid(True, ls="--", alpha=0.4)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    ax2 = axes[1]
    ax2.plot(epochs, [a*100 for a in tr_acc],  "b-o", ms=6, label="Entraînement")
    ax2.plot(epochs, [a*100 for a in val_acc], "r-o", ms=6, label="Validation")
    ax2.set_title("Accuracy (%)", fontweight="bold")
    ax2.set_xlabel("Époque"); ax2.set_ylabel("Accuracy (%)")
    ax2.legend(); ax2.grid(True, ls="--", alpha=0.4)
    ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    _save(fig, "02_courbes_entrainement.png")


# ══════════════════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — ÉVALUATION DES PERFORMANCES
# ══════════════════════════════════════════════════════════════════════════════

def evaluate_model(model, X_test, y_test):
    """
    Évalue sur le jeu de test :
      - Accuracy globale et rapport par classe
      - Matrice de confusion (quels chiffres sont confondus ?)
      - Taux d'erreur par chiffre (quels chiffres sont difficiles ?)
      - Exemples de prédictions correctes et incorrectes
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 4 — Évaluation des performances")
    print("═" * 65)

    # model.predict() retourne des probabilités (softmax) → argmax pour le label
    y_prob = model.predict(X_test, verbose=0)
    y_pred = np.argmax(y_prob, axis=1)

    acc = accuracy_score(y_test, y_pred)
    print(f"\n  ✓ Accuracy sur le jeu de test : {acc*100:.2f}%")

    print("\n  Rapport de classification par chiffre :")
    print("  " + "─" * 55)
    report = classification_report(y_test, y_pred,
                                   target_names=[f"Chiffre {i}" for i in range(10)])
    for line in report.split("\n"):
        print(f"  {line}")

    _plot_confusion_matrix(y_test, y_pred)
    _plot_difficult_digits(y_test, y_pred)
    _plot_predictions(X_test, y_test, y_pred)

    return acc


def _plot_confusion_matrix(y_test, y_pred):
    """Heatmap de la matrice de confusion — cases rouges = erreurs fréquentes."""
    cm = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=range(10), yticklabels=range(10),
                linewidths=0.5, ax=ax)
    ax.set_title("Matrice de confusion\n(lignes = vrais labels  ·  colonnes = prédictions)",
                 fontsize=13, fontweight="bold")
    ax.set_xlabel("Chiffre prédit", fontsize=11)
    ax.set_ylabel("Vrai chiffre",   fontsize=11)
    # Encadre la diagonale (prédictions correctes)
    for i in range(10):
        ax.add_patch(plt.Rectangle((i, i), 1, 1, fill=False, edgecolor="green", lw=2.5))

    plt.tight_layout()
    _save(fig, "03_matrice_confusion.png")


def _plot_difficult_digits(y_test, y_pred):
    """Bar chart du taux d'erreur par classe — identifie les chiffres difficiles."""
    err = {}
    for d in range(10):
        mask    = y_test == d
        err[d]  = (y_pred[mask] != d).sum() / mask.sum() * 100

    digits    = list(err.keys())
    error_pct = list(err.values())
    mean_err  = np.mean(error_pct)
    colors    = ["#E63946" if e == max(error_pct)
                 else "#F4A261" if e > mean_err
                 else "#2A9D8F" for e in error_pct]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(digits, error_pct, color=colors, edgecolor="white", linewidth=0.8)
    for bar, pct in zip(bars, error_pct):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
                f"{pct:.1f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.axhline(mean_err, color="#333", linestyle="--", linewidth=1.2,
               label=f"Moyenne : {mean_err:.1f}%")
    ax.set_xticks(digits)
    ax.set_xticklabels([f"Chiffre {d}" for d in digits], rotation=20)
    ax.set_ylabel("Taux d'erreur (%)"); ax.set_ylim(0, max(error_pct) * 1.25)
    ax.set_title("Taux d'erreur par chiffre\n(rouge = le plus difficile  ·  vert = le plus facile)",
                 fontsize=13, fontweight="bold")
    ax.legend()
    ax.grid(True, ls="--", alpha=0.3, axis="y")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    legend = [Patch(color="#E63946", label="Plus difficile"),
              Patch(color="#F4A261", label="Au-dessus de la moyenne"),
              Patch(color="#2A9D8F", label="En dessous de la moyenne")]
    ax.legend(handles=legend, fontsize=9)
    plt.tight_layout()
    _save(fig, "04_chiffres_difficiles.png")

    print(f"\n  Classement par difficulté (taux d'erreur) :")
    for rank, (d, e) in enumerate(sorted(err.items(), key=lambda x: -x[1]), 1):
        bar = "█" * int(e / 2)
        print(f"    #{rank:<2} Chiffre {d} : {e:5.1f}%  {bar}")


def _plot_predictions(X_test, y_test, y_pred):
    """Grille : 10 prédictions correctes (vert) + 10 incorrectes (rouge)."""
    correct   = np.where(y_pred == y_test)[0]
    incorrect = np.where(y_pred != y_test)[0]

    fig = plt.figure(figsize=(14, 6))
    fig.suptitle("Exemples de prédictions du modèle", fontsize=13, fontweight="bold")
    gs = gridspec.GridSpec(2, 10, hspace=0.6, wspace=0.3)

    for i, idx in enumerate(correct[:10]):
        ax = fig.add_subplot(gs[0, i])
        ax.imshow(X_test[idx].reshape(28, 28), cmap="gray_r")
        ax.set_title(f"✓ {y_pred[idx]}", fontsize=9, color="green", fontweight="bold")
        ax.axis("off")

    for i, idx in enumerate(incorrect[:10]):
        ax = fig.add_subplot(gs[1, i])
        ax.imshow(X_test[idx].reshape(28, 28), cmap="gray_r")
        ax.set_title(f"✗ {y_pred[idx]}\n({y_test[idx]})",
                     fontsize=7.5, color="red", fontweight="bold")
        ax.axis("off")

    fig.text(0.01, 0.75, "Correctes",  va="center", rotation=90,
             fontsize=11, color="green", fontweight="bold")
    fig.text(0.01, 0.25, "Incorrectes", va="center", rotation=90,
             fontsize=11, color="red",   fontweight="bold")
    _save(fig, "05_exemples_predictions.png")


# ══════════════════════════════════════════════════════════════════════════════
#  ÉTAPE 5 — RÉGLAGE DES HYPERPARAMÈTRES
# ══════════════════════════════════════════════════════════════════════════════

def hyperparameter_tuning(X_train, y_train, X_test, y_test):
    """
    Compare 5 configurations (taille des couches × taux d'apprentissage).
    Identifie la meilleure configuration et la visualise.
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 5 — Optimisation par réglage des hyperparamètres")
    print("═" * 65)

    experiments = [
        {"hidden": (64, 32),   "lr": 0.001,  "label": "Petit\n64-32, lr=0.001"},
        {"hidden": (128, 64),  "lr": 0.001,  "label": "Moyen\n128-64, lr=0.001"},
        {"hidden": (256, 128), "lr": 0.001,  "label": "Grand\n256-128, lr=0.001"},
        {"hidden": (128, 64),  "lr": 0.01,   "label": "lr élevé\n128-64, lr=0.01"},
        {"hidden": (128, 64),  "lr": 0.0001, "label": "lr faible\n128-64, lr=0.0001"},
    ]

    print(f"\n  {'Configuration':<35} {'Accuracy test'}")
    print("  " + "─" * 50)

    results = []
    for cfg in experiments:
        # Construire le modèle Keras pour chaque configuration
        m = keras.Sequential(name="hp_search")
        m.add(layers.Input(shape=(784,)))
        for n in cfg["hidden"]:
            m.add(layers.Dense(n, activation="relu"))
        m.add(layers.Dense(10, activation="softmax"))
        m.compile(
            optimizer=keras.optimizers.Adam(learning_rate=cfg["lr"]),
            loss="sparse_categorical_crossentropy",
            metrics=["accuracy"]
        )
        m.fit(X_train, y_train, epochs=10, batch_size=32,
              validation_split=0.1, verbose=0)

        y_pred = np.argmax(m.predict(X_test, verbose=0), axis=1)
        acc = accuracy_score(y_test, y_pred) * 100
        results.append({**cfg, "accuracy": acc})
        print(f"  {cfg['label'].replace(chr(10),' '):<35} {acc:.2f}%")

    _plot_hyperparameter_results(results)

    best = max(results, key=lambda x: x["accuracy"])
    print(f"\n  ✓ Meilleure config : {best['label'].replace(chr(10),' ')} → {best['accuracy']:.2f}%")


def _plot_hyperparameter_results(results):
    """Bar chart des accuracy par configuration d'hyperparamètres."""
    labels   = [r["label"] for r in results]
    acc_vals = [r["accuracy"] for r in results]
    best_idx = acc_vals.index(max(acc_vals))
    colors   = ["#E63946" if i == best_idx else "#457B9D" for i in range(len(results))]

    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(range(len(results)), acc_vals, color=colors, edgecolor="white",
                  linewidth=0.8, width=0.6)
    for bar, acc in zip(bars, acc_vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f"{acc:.2f}%", ha="center", va="bottom", fontsize=10, fontweight="bold")
    ax.set_xticks(range(len(results)))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Accuracy sur le jeu de test (%)")
    ax.set_title("Comparaison des hyperparamètres\n(rouge = meilleure configuration)",
                 fontsize=13, fontweight="bold")
    ax.set_ylim(min(acc_vals) - 3, min(100, max(acc_vals) + 5))
    ax.grid(True, ls="--", alpha=0.3, axis="y")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    plt.tight_layout()
    _save(fig, "06_hyperparametres.png")


# ── Utilitaire ────────────────────────────────────────────────────────────────

def _save(fig, name):
    path = f"{OUTPUT}/{name}"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Graphique sauvegardé : {path}")


# ══════════════════════════════════════════════════════════════════════════════
#  PIPELINE PRINCIPAL
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print("\n╔" + "═"*63 + "╗")
    print("║   RÉSEAU DE NEURONES — RECONNAISSANCE DE CHIFFRES MNIST   ║")
    print("╚" + "═"*63 + "╝\n")

    X_train, X_test, y_train, y_test = load_and_preprocess()
    model  = build_model(hidden=(128, 64), lr=0.001)
    model  = train_model(model, X_train, y_train, n_epochs=10)
    acc    = evaluate_model(model, X_test, y_test)
    hyperparameter_tuning(X_train, y_train, X_test, y_test)

    print("\n" + "═"*65)
    print("  RÉSUMÉ FINAL")
    print("═"*65)
    print(f"  Dataset         : MNIST réel  ({len(X_train)} train / {len(X_test)} test)")
    print(f"  Architecture    : 784 → 128 → 64 → 10")
    print(f"  Activation      : ReLU (couches cachées) + Softmax (sortie)")
    print(f"  Perte           : Categorical Cross-Entropy")
    print(f"  Optimiseur      : Adam")
    print(f"  Accuracy finale : {acc*100:.2f}%")
    print(f"  Graphiques      : {OUTPUT}/  (6 fichiers PNG)")
    print("═"*65 + "\n")


if __name__ == "__main__":
    main()
