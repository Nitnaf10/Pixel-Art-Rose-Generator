Pixel Art Rose Generator

![](https://img.shields.io/github/stars/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square)
https://img.shields.io/github/forks/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square
https://img.shields.io/github/watchers/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square
https://img.shields.io/github/contributors/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square
https://img.shields.io/github/commit-activity/m/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square
https://img.shields.io/github/last-commit/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square
https://img.shields.io/github/languages/count/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square
https://img.shields.io/github/languages/top/Nitnaf10/Pixel-Art-Rose-Generator?style=flat-square

Générateur algorithmique de motifs symétriques inspirés de rosaces, développé en Python.

---

Fonctionnalités

· Génération de motifs à symétrie d'ordre 8
· Algorithme de marche aléatoire pour des variations organiques
· Interface en ligne de commande
· Métadonnées (seed, steps) intégrées aux fichiers PNG
· Paramètres personnalisables : seed, taille, nombre d'étapes

---

Installation

```bash
git clone https://github.com/Nitnaf10/Pixel-Art-Rose-Generator.git
cd Pixel-Art-Rose-Generator
pip install Pillow
mkdir generated
```

---

Utilisation

```bash
# Génération automatique
python main.py save mon_image

# Paramètres personnalisés
python main.py save mon_image --seed 251515 --size 7 --step 1024

# Lecture des métadonnées
python main.py read mon_image

# Aide
python main.py help
```

Options

Option Description
name Nom du fichier (obligatoire)
--seed Graine aléatoire (auto par défaut)
--size Taille du motif (auto par défaut)
--step Nombre d'étapes (auto par défaut)

---

Licence

Projet open source – consulter le dépôt pour les conditions d'utilisation.