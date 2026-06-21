import math   # pour math.pi et math.pow


class Circle:

    # ── Constructeur ───────────────────────────────────────────────────────
    def __init__(self, radius):
        self.radius = radius          # on stocke toujours le radius

    # ── Propriété : diameter ───────────────────────────────────────────────
    # @property permet d'accéder à .diameter comme un attribut normal
    # mais c'est calculé automatiquement depuis le radius
    @property
    def diameter(self):
        return self.radius * 2

    # Setter : permet de créer un cercle avec le diameter
    # ex : c = Circle(0) puis c.diameter = 10  →  radius = 5
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    # ── Méthode : area ─────────────────────────────────────────────────────
    def area(self):
        return math.pi * math.pow(self.radius, 2)

    # ── Dunder __str__ : affichage lisible ─────────────────────────────────
    # Appelé quand on fait print(circle)
    def __str__(self):
        return "Circle(radius=" + str(self.radius) + ", diameter=" + str(self.diameter) + ")"

    # ── Dunder __repr__ : affichage technique ──────────────────────────────
    # Appelé dans la console / dans une liste
    def __repr__(self):
        return "Circle(" + str(self.radius) + ")"

    # ── Dunder __add__ : addition de deux cercles ──────────────────────────
    # Appelé quand on fait c1 + c2
    def __add__(self, other):
        new_radius = self.radius + other.radius
        return Circle(new_radius)

    # ── Dunder __gt__ : plus grand que ────────────────────────────────────
    # Appelé quand on fait c1 > c2
    def __gt__(self, other):
        return self.radius > other.radius

    # ── Dunder __lt__ : plus petit que ────────────────────────────────────
    # Appelé quand on fait c1 < c2  ET utilisé par sorted()
    def __lt__(self, other):
        return self.radius < other.radius

    # ── Dunder __eq__ : égalité ───────────────────────────────────────────
    # Appelé quand on fait c1 == c2
    def __eq__(self, other):
        return self.radius == other.radius