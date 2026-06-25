"""
classification_nn.py
════════════════════
Classification avec Réseaux de Neurones — Pipeline Complet

Note : implémenté avec scikit-learn (MLPClassifier) qui reproduit
exactement l'API de TensorFlow/Keras Sequential.

Étapes couvertes :
  1. Types de classification (Binary, Multi-class, Multi-label)
  2. Environnement et dataset (make_circles)
  3. Modèle de base (1 couche dense)
  4. Modèle amélioré (couches + neurones + Adam)
  5. Frontière de décision (plot_decision_boundary)
  6. Fonctions d'activation (ReLU vs Sigmoid)
  7. Split Train / Test (80/20)
  8. Évaluation finale et visualisations
  9. Résumé des points clés
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from sklearn.datasets import make_circles, make_blobs, make_multilabel_classification
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

OUTPUT = "output"
np.random.seed(42)


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 1 — TYPES DE CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════

def etape1_types_de_classification():
    """
    Explication et visualisation des 3 types de classification :
    Binary, Multi-class, Multi-label.
    """
    print("═" * 65)
    print("  ÉTAPE 1 — Types de classification")
    print("═" * 65)

    explications = {
        "Classification Binaire": {
            "definition": "Prédit l'appartenance à l'une de 2 classes uniquement.",
            "exemple": "Un email est-il SPAM ou NON-SPAM ?",
            "sortie": "0 ou 1  (une seule étiquette par exemple)",
            "perte": "Binary Cross-Entropy",
            "activation_sortie": "Sigmoid → probabilité entre 0 et 1",
        },
        "Classification Multi-classes": {
            "definition": "Prédit l'appartenance à l'une de N classes (N > 2).",
            "exemple": "Ce chiffre manuscrit est-il 0, 1, 2, ... ou 9 ? (MNIST)",
            "sortie": "Une seule étiquette parmi N classes",
            "perte": "Categorical Cross-Entropy",
            "activation_sortie": "Softmax → probabilités qui somment à 1",
        },
        "Classification Multi-label": {
            "definition": "Prédit plusieurs étiquettes simultanément pour un même exemple.",
            "exemple": "Un film peut être Action ET Comédie ET Romance à la fois.",
            "sortie": "Vecteur binaire  (ex: [1, 0, 1, 1] pour 4 étiquettes)",
            "perte": "Binary Cross-Entropy sur chaque étiquette indépendamment",
            "activation_sortie": "Sigmoid sur chaque sortie",
        },
    }

    for nom, info in explications.items():
        print(f"\n  ┌─ {nom}")
        for cle, val in info.items():
            print(f"  │  {cle:<22} : {val}")
        print("  └─────────────────────────────────────────────")

    # Visualisation des 3 types
    _plot_classification_types()


def _plot_classification_types():
    """3 scatter plots côte à côte — un par type de classification."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle("Les 3 types de classification", fontsize=14, fontweight="bold")
    COLORS = ["#E63946", "#2A9D8F", "#F4A261", "#457B9D"]

    # ── Binaire : make_circles ─────────────────────────────────────
    X_b, y_b = make_circles(300, noise=0.05, random_state=42)
    ax = axes[0]
    for cls, color, label in [(0, "#E63946", "Classe 0"), (1, "#2A9D8F", "Classe 1")]:
        mask = y_b == cls
        ax.scatter(X_b[mask,0], X_b[mask,1], c=color, s=25, alpha=0.7, label=label)
    ax.set_title("Binaire\n(2 classes : 0 ou 1)", fontweight="bold")
    ax.set_xlabel("X₁"); ax.set_ylabel("X₂")
    ax.legend(fontsize=9); ax.grid(True, ls="--", alpha=0.3)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    # ── Multi-classes : 4 blobs ────────────────────────────────────
    X_m, y_m = make_blobs(300, centers=4, random_state=42, cluster_std=1.2)
    ax2 = axes[1]
    for cls in range(4):
        mask = y_m == cls
        ax2.scatter(X_m[mask,0], X_m[mask,1], c=COLORS[cls], s=25,
                    alpha=0.7, label=f"Classe {cls}")
    ax2.set_title("Multi-classes\n(4 classes distinctes)", fontweight="bold")
    ax2.set_xlabel("X₁"); ax2.set_ylabel("X₂")
    ax2.legend(fontsize=9); ax2.grid(True, ls="--", alpha=0.3)
    ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)

    # ── Multi-label : barres d'étiquettes ─────────────────────────
    X_ml, y_ml = make_multilabel_classification(
        n_samples=200, n_features=2, n_classes=3,
        n_labels=2, random_state=42
    )
    ax3 = axes[2]
    # Encoder les combinaisons d'étiquettes en couleurs
    combos     = [tuple(row) for row in y_ml]
    unique_c   = list(set(combos))
    combo_color = {c: COLORS[i % len(COLORS)] for i, c in enumerate(unique_c)}
    colors_ml  = [combo_color[c] for c in combos]
    ax3.scatter(X_ml[:,0], X_ml[:,1], c=colors_ml, s=25, alpha=0.7)
    ax3.set_title("Multi-label\n(plusieurs étiquettes par exemple)", fontweight="bold")
    ax3.set_xlabel("X₁"); ax3.set_ylabel("X₂")
    ax3.grid(True, ls="--", alpha=0.3)
    ax3.spines["top"].set_visible(False); ax3.spines["right"].set_visible(False)
    ax3.text(0.05, 0.95, "Couleur = combinaison\nd'étiquettes actives",
             transform=ax3.transAxes, fontsize=8, va="top",
             bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))

    plt.tight_layout()
    _save(fig, "01_types_classification.png")


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 2 — DATASET make_circles
# ═══════════════════════════════════════════════════════════════════

def etape2_dataset():
    """
    Création du dataset make_circles (1000 échantillons).
    Visualisation de la distribution des données.
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 2 — Dataset make_circles")
    print("═" * 65)

    # ── Création du dataset ────────────────────────────────────────
    samples = 1000
    X, y = make_circles(samples, noise=0.03, random_state=42)

    print(f"\n  X (features) : {X.shape}  →  {samples} exemples × 2 coordonnées (x₁, x₂)")
    print(f"  y (labels)   : {y.shape}  →  {samples} étiquettes binaires (0 ou 1)")
    print(f"\n  5 premiers exemples :")
    print(f"  {'X[:,0]':<12} {'X[:,1]':<12} {'y'}")
    print("  " + "─" * 30)
    for i in range(5):
        print(f"  {X[i,0]:< 10.4f}   {X[i,1]:< 10.4f}   {y[i]}")
    print(f"\n  Classe 0 : {(y==0).sum()} exemples | Classe 1 : {(y==1).sum()} exemples")

    # Conversion DataFrame pour inspection
    df = pd.DataFrame({"x1": X[:,0], "x2": X[:,1], "label": y})
    print(f"\n  Statistiques descriptives :")
    print(df.groupby("label")[["x1","x2"]].mean().to_string())

    _plot_dataset(X, y)
    return X, y


def _plot_dataset(X, y):
    """Scatter plot du dataset make_circles avec distribution marginale."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Dataset make_circles — Distribution des données",
                 fontsize=13, fontweight="bold")

    # ── Scatter principal ──────────────────────────────────────────
    ax = axes[0]
    for cls, color, label in [(0,"#E63946","Cercle extérieur (0)"),
                               (1,"#2A9D8F","Cercle intérieur (1)")]:
        mask = y == cls
        ax.scatter(X[mask,0], X[mask,1], c=color, s=18, alpha=0.6, label=label)
    ax.set_title("Scatter plot — make_circles(1000, noise=0.03)", fontweight="bold")
    ax.set_xlabel("x₁"); ax.set_ylabel("x₂")
    ax.legend(fontsize=10); ax.grid(True, ls="--", alpha=0.3)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    # ── Distribution marginale ─────────────────────────────────────
    ax2 = axes[1]
    for cls, color, label in [(0,"#E63946","Classe 0"), (1,"#2A9D8F","Classe 1")]:
        mask = y == cls
        ax2.hist(X[mask,0], bins=30, alpha=0.6, color=color, label=f"{label} (x₁)")
        ax2.hist(X[mask,1], bins=30, alpha=0.35, color=color, linestyle="--",
                 edgecolor=color, facecolor="none", label=f"{label} (x₂)")
    ax2.set_title("Distribution marginale de x₁ et x₂ par classe", fontweight="bold")
    ax2.set_xlabel("Valeur"); ax2.set_ylabel("Fréquence")
    ax2.legend(fontsize=8); ax2.grid(True, ls="--", alpha=0.3)
    ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    _save(fig, "02_dataset_distribution.png")


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 3 — MODÈLE DE BASE (1 couche dense)
# ═══════════════════════════════════════════════════════════════════

def etape3_modele_base(X_train, X_test, y_train, y_test):
    """
    Modèle de base : Sequential avec une seule couche Dense.
    Équivalent TensorFlow :
      model = tf.keras.Sequential([tf.keras.layers.Dense(1, activation='sigmoid')])
      model.compile(loss='binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 3 — Modèle de base (1 couche dense)")
    print("═" * 65)
    print(f"\n  Architecture : Input(2) → Dense(1, Sigmoid)")
    print(f"  Perte        : Binary Cross-Entropy")
    print(f"  Optimiseur   : SGD  (Stochastic Gradient Descent)")

    model = MLPClassifier(
        hidden_layer_sizes=(),    # 0 couche cachée → équivalent à Dense(1)
        activation="logistic",    # Sigmoid
        solver="sgd",             # SGD
        learning_rate_init=0.01,
        max_iter=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    acc_train = accuracy_score(y_train, model.predict(X_train))
    acc_test  = accuracy_score(y_test,  model.predict(X_test))
    print(f"\n  ✓ Accuracy train : {acc_train*100:.2f}%")
    print(f"  ✓ Accuracy test  : {acc_test*100:.2f}%")
    print(f"\n  Observation : un modèle à 1 couche ne peut tracer qu'une")
    print(f"  frontière linéaire → insuffisant pour des cercles non-linéaires.")

    return model, acc_train, acc_test


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 4 — MODÈLE AMÉLIORÉ (couches + neurones + Adam)
# ═══════════════════════════════════════════════════════════════════

def etape4_modele_ameliore(X_train, X_test, y_train, y_test):
    """
    Modèle amélioré : 2 couches cachées, plus de neurones, optimiseur Adam.
    Équivalent TensorFlow :
      model = tf.keras.Sequential([
          tf.keras.layers.Dense(10, activation='relu'),
          tf.keras.layers.Dense(10, activation='relu'),
          tf.keras.layers.Dense(1,  activation='sigmoid')
      ])
      model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
      model.fit(X_train, y_train, epochs=100)
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 4 — Modèle amélioré (+ couches, + neurones, Adam)")
    print("═" * 65)
    print(f"\n  Architecture : Input(2) → Dense(10,ReLU) → Dense(10,ReLU) → Dense(1,Sigmoid)")
    print(f"  Perte        : Binary Cross-Entropy")
    print(f"  Optimiseur   : Adam  (adaptatif, converge plus vite que SGD)")
    print(f"  Époques      : 100")

    model = MLPClassifier(
        hidden_layer_sizes=(10, 10),  # 2 couches cachées de 10 neurones chacune
        activation="relu",            # ReLU sur les couches cachées
        solver="adam",                # Adam : meilleure convergence
        learning_rate_init=0.001,
        max_iter=100,
        random_state=42
    )
    model.fit(X_train, y_train)

    acc_train = accuracy_score(y_train, model.predict(X_train))
    acc_test  = accuracy_score(y_test,  model.predict(X_test))
    print(f"\n  ✓ Accuracy train : {acc_train*100:.2f}%  (vs modèle de base)")
    print(f"  ✓ Accuracy test  : {acc_test*100:.2f}%  (amélioration significative)")

    return model, acc_train, acc_test


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 5 — FRONTIÈRE DE DÉCISION
# ═══════════════════════════════════════════════════════════════════

def plot_decision_boundary(model, X, y, title="Frontière de décision", ax=None):
    """
    Visualise la frontière de décision apprise par le modèle.
    Trace une grille de points et colorie chaque zone selon la classe prédite.

    Paramètres :
      model : modèle entraîné avec méthode predict()
      X     : features (n_samples × 2)
      y     : labels vrais
      title : titre du graphique
      ax    : axes matplotlib (si None, crée une nouvelle figure)
    """
    standalone = ax is None
    if standalone:
        fig, ax = plt.subplots(figsize=(7, 6))

    # Grille de points couvrant l'espace des features
    h = 0.02  # résolution de la grille
    x_min, x_max = X[:,0].min() - 0.2, X[:,0].max() + 0.2
    y_min, y_max = X[:,1].min() - 0.2, X[:,1].max() + 0.2
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # Prédiction sur chaque point de la grille
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    Z = model.predict(grid_points).reshape(xx.shape)

    # Zones colorées par classe prédite
    ax.contourf(xx, yy, Z, alpha=0.25,
                colors=["#E63946","#2A9D8F"], levels=[-0.5, 0.5, 1.5])
    ax.contour(xx, yy, Z, colors=["white"], linewidths=1.5, levels=[0.5])

    # Points du dataset
    for cls, color, label in [(0,"#E63946","Classe 0"), (1,"#2A9D8F","Classe 1")]:
        mask = y == cls
        ax.scatter(X[mask,0], X[mask,1], c=color, s=18, alpha=0.8,
                   edgecolors="white", linewidths=0.4, label=label)

    acc = accuracy_score(y, model.predict(X))
    ax.set_title(f"{title}\nAccuracy : {acc*100:.1f}%", fontweight="bold")
    ax.set_xlabel("x₁"); ax.set_ylabel("x₂")
    ax.legend(fontsize=9)
    ax.grid(True, ls="--", alpha=0.2)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    if standalone:
        plt.tight_layout()
        _save(fig, f"boundary_{title[:20].replace(' ','_').lower()}.png")
        return fig


def etape5_frontieres(model_base, model_ameliore, X_train, y_train):
    """Compare les frontières de décision des deux modèles."""
    print("\n" + "═" * 65)
    print("  ÉTAPE 5 — Visualisation des frontières de décision")
    print("═" * 65)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Comparaison des frontières de décision",
                 fontsize=13, fontweight="bold")

    plot_decision_boundary(model_base,     X_train, y_train,
                           "Modèle de base (SGD, 1 couche)", ax=axes[0])
    plot_decision_boundary(model_ameliore, X_train, y_train,
                           "Modèle amélioré (Adam, 2 couches)", ax=axes[1])

    plt.tight_layout()
    _save(fig, "03_frontieres_decision.png")
    print(f"\n  Observation : la frontière linéaire du modèle de base")
    print(f"  ne peut pas capturer la forme circulaire des données.")
    print(f"  Les couches supplémentaires + ReLU créent une frontière non-linéaire.")


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 6 — FONCTIONS D'ACTIVATION
# ═══════════════════════════════════════════════════════════════════

def etape6_activation_functions(X_train, X_test, y_train, y_test):
    """
    Compare ReLU vs Sigmoid comme activation des couches cachées.
    ReLU : f(x) = max(0, x)  → résout le problème du gradient évanescent
    Sigmoid : f(x) = 1/(1+e^{-x})  → sortie dans [0,1], peut saturer
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 6 — Fonctions d'activation (ReLU vs Sigmoid)")
    print("═" * 65)

    # Visualisation des fonctions
    x = np.linspace(-5, 5, 200)
    relu    = np.maximum(0, x)
    sigmoid = 1 / (1 + np.exp(-x))
    tanh    = np.tanh(x)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Fonctions d'activation", fontsize=13, fontweight="bold")

    ax = axes[0]
    ax.plot(x, relu,    color="#E63946", lw=2.5, label="ReLU  f(x)=max(0,x)")
    ax.plot(x, sigmoid, color="#2A9D8F", lw=2.5, label="Sigmoid  f(x)=1/(1+e⁻ˣ)")
    ax.plot(x, tanh,    color="#F4A261", lw=2.5, label="Tanh  f(x)=tanh(x)")
    ax.axhline(0, color="gray", lw=0.8, ls="--")
    ax.axvline(0, color="gray", lw=0.8, ls="--")
    ax.set_title("Courbes des fonctions d'activation", fontweight="bold")
    ax.set_xlabel("x"); ax.set_ylabel("f(x)")
    ax.legend(fontsize=10); ax.grid(True, ls="--", alpha=0.3)
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.annotate("Gradient = 0\npour x < 0\n(ReLU)", xy=(-2, 0),
                fontsize=8, color="#E63946",
                arrowprops=dict(arrowstyle="->", color="#E63946"),
                xytext=(-4, 0.6))

    # Comparaison des performances
    configs = {
        "ReLU":    {"activation":"relu",     "color":"#E63946"},
        "Sigmoid": {"activation":"logistic", "color":"#2A9D8F"},
        "Tanh":    {"activation":"tanh",     "color":"#F4A261"},
    }
    results = {}
    for name, cfg in configs.items():
        m = MLPClassifier(hidden_layer_sizes=(10,10), activation=cfg["activation"],
                          solver="adam", max_iter=100, random_state=42)
        m.fit(X_train, y_train)
        results[name] = {
            "model": m,
            "train": accuracy_score(y_train, m.predict(X_train)) * 100,
            "test":  accuracy_score(y_test,  m.predict(X_test))  * 100,
            "color": cfg["color"]
        }
        print(f"  {name:<10} → train={results[name]['train']:.2f}%  test={results[name]['test']:.2f}%")

    ax2 = axes[1]
    x_pos = np.arange(len(results))
    w = 0.35
    names  = list(results.keys())
    trains = [results[n]["train"] for n in names]
    tests  = [results[n]["test"]  for n in names]
    colors = [results[n]["color"] for n in names]

    bars1 = ax2.bar(x_pos - w/2, trains, w, color=colors, alpha=0.85,
                    edgecolor="white", label="Train")
    bars2 = ax2.bar(x_pos + w/2, tests,  w, color=colors, alpha=0.45,
                    edgecolor="white", hatch="//", label="Test")
    for bar, v in list(zip(bars1, trains)) + list(zip(bars2, tests)):
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3,
                 f"{v:.1f}%", ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax2.set_xticks(x_pos); ax2.set_xticklabels(names, fontsize=11)
    ax2.set_ylabel("Accuracy (%)"); ax2.set_ylim(50, 105)
    ax2.set_title("Accuracy par fonction d'activation\n(plein=train, hachuré=test)",
                  fontweight="bold")
    ax2.legend(); ax2.grid(True, ls="--", alpha=0.3, axis="y")
    ax2.spines["top"].set_visible(False); ax2.spines["right"].set_visible(False)

    plt.tight_layout()
    _save(fig, "04_fonctions_activation.png")

    return results["ReLU"]["model"]


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 7 — SPLIT TRAIN / TEST (80 / 20)
# ═══════════════════════════════════════════════════════════════════

def etape7_split(X, y):
    """
    Découpe les données en 80% entraînement / 20% test.
    Normalise les features (StandardScaler).
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 7 — Split Train / Test (80% / 20%)")
    print("═" * 65)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Normalisation : moyenne=0, écart-type=1
    scaler  = StandardScaler()
    X_train = scaler.fit_transform(X_train)  # fit + transform sur train
    X_test  = scaler.transform(X_test)       # transform seulement sur test (évite la fuite)

    print(f"\n  Données totales : {len(X)} exemples")
    print(f"  Entraînement   : {len(X_train)} exemples  (80%)")
    print(f"  Test           : {len(X_test)} exemples  (20%)")
    print(f"\n  Normalisation appliquée :")
    print(f"    Moyenne train avant : {X[:,0].mean():.4f} / après : {X_train[:,0].mean():.4f}")
    print(f"    Écart-type train    : {X[:,0].std():.4f} / après : {X_train[:,0].std():.4f}")
    print(f"\n  Règle importante : le scaler est fitté sur TRAIN uniquement")
    print(f"  (pas sur TEST) pour éviter la 'data leakage'.")

    _plot_split(X_train, X_test, y_train, y_test)
    return X_train, X_test, y_train, y_test


def _plot_split(X_train, X_test, y_train, y_test):
    """Visualise le split train/test sur le scatter plot."""
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    fig.suptitle("Séparation Train / Test (80% / 20%)", fontsize=13, fontweight="bold")

    for ax, X, y, title, alpha in [
        (axes[0], X_train, y_train, f"Train ({len(X_train)} exemples)", 0.7),
        (axes[1], X_test,  y_test,  f"Test  ({len(X_test)} exemples)",  0.9),
    ]:
        for cls, color, label in [(0,"#E63946","Classe 0"), (1,"#2A9D8F","Classe 1")]:
            mask = y == cls
            ax.scatter(X[mask,0], X[mask,1], c=color, s=20, alpha=alpha, label=label)
        ax.set_title(title, fontweight="bold")
        ax.set_xlabel("x₁ (normalisé)"); ax.set_ylabel("x₂ (normalisé)")
        ax.legend(fontsize=9); ax.grid(True, ls="--", alpha=0.3)
        ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)

    plt.tight_layout()
    _save(fig, "05_train_test_split.png")


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 8 — ÉVALUATION FINALE
# ═══════════════════════════════════════════════════════════════════

def etape8_evaluation_finale(X_train, X_test, y_train, y_test):
    """
    Entraîne le modèle final optimisé, évalue sur train et test,
    visualise les frontières sur les deux jeux de données.
    """
    print("\n" + "═" * 65)
    print("  ÉTAPE 8 — Évaluation et visualisation finale")
    print("═" * 65)

    # Modèle final : plus de neurones, plus d'époques
    model_final = MLPClassifier(
        hidden_layer_sizes=(64, 32, 16),  # 3 couches cachées
        activation="relu",
        solver="adam",
        learning_rate_init=0.001,
        max_iter=200,
        random_state=42
    )
    print(f"\n  Modèle final : Input(2)→Dense(64,ReLU)→Dense(32,ReLU)→Dense(16,ReLU)→Dense(1,Sigmoid)")
    model_final.fit(X_train, y_train)

    acc_train = accuracy_score(y_train, model_final.predict(X_train))
    acc_test  = accuracy_score(y_test,  model_final.predict(X_test))
    print(f"\n  ✓ Accuracy train : {acc_train*100:.2f}%")
    print(f"  ✓ Accuracy test  : {acc_test*100:.2f}%")

    print(f"\n  Rapport de classification (test) :")
    print("  " + "─" * 50)
    report = classification_report(y_test, model_final.predict(X_test),
                                   target_names=["Classe 0","Classe 1"])
    for line in report.split("\n"):
        print(f"  {line}")

    # Frontières train et test côte à côte
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Modèle final — Frontières de décision (Train vs Test)",
                 fontsize=13, fontweight="bold")
    plot_decision_boundary(model_final, X_train, y_train,
                           "Données d'entraînement", ax=axes[0])
    plot_decision_boundary(model_final, X_test,  y_test,
                           "Données de test",        ax=axes[1])
    plt.tight_layout()
    _save(fig, "06_evaluation_finale.png")

    return model_final, acc_train, acc_test


# ═══════════════════════════════════════════════════════════════════
#  ÉTAPE 9 — RÉSUMÉ
# ═══════════════════════════════════════════════════════════════════

def etape9_resume(resultats: dict):
    """Affiche le tableau récapitulatif et les points clés."""
    print("\n" + "═" * 65)
    print("  ÉTAPE 9 — Résumé et points clés")
    print("═" * 65)

    print(f"\n  Comparaison des modèles :")
    print(f"  {'Modèle':<35} {'Acc. train':<14} {'Acc. test'}")
    print("  " + "─" * 60)
    for nom, r in resultats.items():
        print(f"  {nom:<35} {r['train']*100:<14.2f} {r['test']*100:.2f}%")

    _plot_comparaison_modeles(resultats)

    print(f"""
  Points clés appris :
  ─────────────────────────────────────────────────────────────
  1. Types de classification
     • Binaire    : 2 classes, perte Binary Cross-Entropy, sortie Sigmoid
     • Multi-class: N classes, perte Categorical Cross-Entropy, sortie Softmax
     • Multi-label: plusieurs étiquettes simultanées, Sigmoid indépendant

  2. Visualiser les données AVANT de modéliser
     • make_circles crée des données non-linéaires → frontière circulaire requise
     • Un modèle linéaire (1 couche) ne peut pas les séparer correctement

  3. Ajouter des couches améliore la représentation non-linéaire
     • Chaque couche cachée apprend une représentation plus abstraite
     • ReLU évite le problème du gradient évanescent (mieux que Sigmoid dans les couches cachées)

  4. Adam > SGD pour la plupart des problèmes
     • Adam ajuste le taux d'apprentissage automatiquement par paramètre
     • Converge plus vite et plus stablement que SGD

  5. Toujours normaliser les features
     • Accélère la convergence
     • Fitter le scaler sur TRAIN uniquement (évite la data leakage)

  6. Évaluer sur un jeu de test SÉPARÉ
     • Un modèle parfait sur train mais mauvais sur test = surapprentissage
     • split 80/20 : standard pour des datasets de taille moyenne
  ─────────────────────────────────────────────────────────────
""")


def _plot_comparaison_modeles(resultats):
    """Bar chart comparatif de tous les modèles testés."""
    noms   = list(resultats.keys())
    trains = [resultats[n]["train"]*100 for n in noms]
    tests  = [resultats[n]["test"]*100  for n in noms]

    x = np.arange(len(noms)); w = 0.35
    fig, ax = plt.subplots(figsize=(12, 6))
    b1 = ax.bar(x - w/2, trains, w, color="#457B9D", edgecolor="white", label="Train")
    b2 = ax.bar(x + w/2, tests,  w, color="#E63946", edgecolor="white", label="Test")
    for bar, v in list(zip(b1, trains)) + list(zip(b2, tests)):
        ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.3,
                f"{v:.1f}%", ha="center", va="bottom", fontsize=8.5, fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(noms, rotation=15, ha="right", fontsize=9)
    ax.set_ylabel("Accuracy (%)"); ax.set_ylim(50, 110)
    ax.set_title("Comparaison de tous les modèles testés", fontsize=13, fontweight="bold")
    ax.legend(); ax.grid(True, ls="--", alpha=0.3, axis="y")
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    plt.tight_layout()
    _save(fig, "07_comparaison_modeles.png")


# ═══════════════════════════════════════════════════════════════════
#  UTILITAIRE
# ═══════════════════════════════════════════════════════════════════

def _save(fig, name):
    """Sauvegarde un graphique et affiche le chemin."""
    path = f"{OUTPUT}/{name}"
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  ✓ Graphique sauvegardé : {path}")


# ═══════════════════════════════════════════════════════════════════
#  PIPELINE PRINCIPAL
# ═══════════════════════════════════════════════════════════════════

def main():
    import os; os.makedirs(OUTPUT, exist_ok=True)

    print("\n╔" + "═"*63 + "╗")
    print("║   CLASSIFICATION AVEC RÉSEAUX DE NEURONES                 ║")
    print("╚" + "═"*63 + "╝")

    # Étape 1 — Types de classification
    etape1_types_de_classification()

    # Étape 2 — Dataset
    X, y = etape2_dataset()

    # Étape 7 — Split AVANT d'entraîner (bonne pratique)
    X_train, X_test, y_train, y_test = etape7_split(X, y)

    # Étape 3 — Modèle de base
    model_base, acc_b_tr, acc_b_te = etape3_modele_base(X_train, X_test, y_train, y_test)

    # Étape 4 — Modèle amélioré
    model_adam, acc_a_tr, acc_a_te = etape4_modele_ameliore(X_train, X_test, y_train, y_test)

    # Étape 5 — Frontières de décision
    etape5_frontieres(model_base, model_adam, X_train, y_train)

    # Étape 6 — Fonctions d'activation
    model_relu = etape6_activation_functions(X_train, X_test, y_train, y_test)

    # Étape 8 — Modèle final et évaluation
    model_final, acc_f_tr, acc_f_te = etape8_evaluation_finale(X_train, X_test, y_train, y_test)

    # Étape 9 — Résumé
    resultats = {
        "Base (SGD, 1 couche)":        {"train": acc_b_tr, "test": acc_b_te},
        "Amélioré (Adam, 2×10)":        {"train": acc_a_tr, "test": acc_a_te},
        "ReLU (Adam, 2×10)":            {"train": accuracy_score(y_train, model_relu.predict(X_train)),
                                          "test":  accuracy_score(y_test,  model_relu.predict(X_test))},
        "Final (Adam, 64-32-16)":       {"train": acc_f_tr, "test": acc_f_te},
    }
    etape9_resume(resultats)

    print("═"*65)
    print(f"  Graphiques générés dans ./{OUTPUT}/  (7 fichiers PNG)")
    print("═"*65 + "\n")


if __name__ == "__main__":
    main()
