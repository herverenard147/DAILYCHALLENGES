Voici les réponses, formulées de façon directe et factuelle.

---

## 1. Qu'est-ce que le Machine Learning et pourquoi est-il important pour un data analyst ?

Le Machine Learning est une branche de l'intelligence artificielle qui permet à un système d'apprendre des motifs à partir de données, sans règles explicitement programmées. L'algorithme déduit une fonction de prédiction à partir d'exemples, plutôt que de suivre une logique conditionnelle écrite manuellement.

Pour un data analyst, le Machine Learning permet de passer de l'analyse descriptive (comprendre ce qui s'est passé) à l'analyse prédictive (anticiper ce qui va se passer), d'automatiser des décisions répétitives à grande échelle, et de détecter des relations non linéaires entre variables que les statistiques descriptives classiques ne révèlent pas.

---

## 2. Applications du Machine Learning par secteur

- **Finance** : détection de fraude bancaire en temps réel, scoring de crédit pour évaluer le risque de défaut de paiement.
- **Santé** : diagnostic assisté par imagerie médicale, prédiction du risque de réadmission hospitalière.
- **E-commerce** : systèmes de recommandation de produits, prévision de la demande pour la gestion des stocks.

---

## 3. Les trois types de Machine Learning

### Apprentissage supervisé
Le modèle apprend à partir de données étiquetées : chaque exemple est associé à une réponse connue. L'objectif est d'apprendre la relation entre les variables d'entrée et la sortie attendue, afin de prédire cette sortie sur de nouvelles données.

**Exemple** : prédire si un client fera défaut sur un prêt, à partir de l'historique de remboursement de clients précédents dont l'issue est connue.

### Apprentissage non supervisé
Le modèle travaille sur des données non étiquetées. L'objectif est de découvrir une structure cachée — regroupements ou associations — sans réponse prédéfinie.

**Exemple** : segmenter une base de clients en groupes homogènes selon leur comportement d'achat, sans catégories connues à l'avance.

### Apprentissage par renforcement
Un agent apprend à prendre des décisions en interagissant avec un environnement, en recevant des récompenses ou des pénalités selon ses actions. L'objectif est d'apprendre une stratégie maximisant la récompense cumulée.

**Exemple** : entraîner un robot à trouver le chemin le plus court dans un labyrinthe, avec une récompense à l'atteinte de la sortie et une pénalité par mouvement ou collision.

---

## 4. Le processus de développement d'un modèle de Machine Learning

### Feature selection
Sélection des variables les plus pertinentes pour prédire la cible. Une sélection inadéquate augmente le risque de surapprentissage, réduit la précision et nuit à l'interprétabilité du modèle.

### Model selection
Choix de l'algorithme adapté au problème, en fonction de la nature de la tâche (classification, régression, clustering), de la taille des données, et du compromis entre performance et interprétabilité. Plusieurs modèles candidats sont généralement entraînés et comparés.

### Model evaluation
Mesure de la performance du modèle sur des données non vues, via un découpage train/validation/test ou une validation croisée. Les métriques utilisées dépendent du type de problème (accuracy, precision, recall, F1-score, AUC-ROC pour la classification ; MAE, RMSE pour la régression). Cette étape garantit que le modèle généralise correctement et ne se contente pas de mémoriser les données d'entraînement.
