"""Dernier recours : publication manuelle assistée. Le texte prêt à copier et le visuel
apparaissent dans le tableau de bord, et une alerte (issue GitHub) prévient l'équipe."""
class Manuel:
    nom = "Manuel assisté"
    def dispo(self): return True
    def publier(self, post, reseau, texte, medias):
        return "MANUEL"
