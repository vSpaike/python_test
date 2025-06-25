**Available in French or in English**

# French 

## Tests
### Lancer les tests
Il faut s'assurer d'être dans la racine, et il faut enter la commande dans le terminal: 
 - python -m unittest tests/test_generate.py
 - python -m unittest tests/test_split_conseq.py
 - python -m unittest tests/test_bst.py


## Arbre binaire de recherche

### Méthode to_bst
Afin que la méthode fonctionne correctement il est essentiel que l'arbre binaire soit complet à chaque étage. Le but lors de sa conception était d'utiliser les propriétés indiquer dans la consigne. Cependant l'implémentation de *None* lorsque une feuille était absente à posé un problème et donc la méthode fonctionne mais ne fait pas un arbre binaire de recherche si la liste fournie en paramètre n'est pas complète.


### Méthode valid et exists
Pour *exists*, l'objectif était de se servir de l'arbre afin d'éffectuer une recherche dichotomique. Sa complexité est donc O(log(n)) avec n le nombre d'éléments de l'arbre. 
Quant à *valid*, le but était seulement de s'assurer de que l'arbre était bien un arbre binaire de recherche, la complexité est O(1/2*n)~O(n)  puisque l'on parcourt la moitié des valeurs l'arbre. 

### Méthode biggest
La complexité de cette fonction est du type O(1) étant donné que l'on fait une comparaison et quelques opérations mathématiques de base. Son optimisation est sûrement possible mais au vu du temps, celle-ci n'était pas prioritaire.

### Méthode smallest
Pour cette méthode, je suppose qu'il existe une possibilité d'amélioration afin d'avoir une complexité du type O(1) comme pour la fonction biggest, cependant je n'ai pas réussi à démontrer ma pensée. 
Ainsi la complexité est de O(n) avec n la hauteur de l'arbre car on va parcourir la partie la plus à gauche de l'arbre.



# English


### Method smallest

For the method smallest i know there is a possibility to a have a coplexity of O(1) like the method biggest but i don't know how to write it. I spent to many time at trying things so i decided to write it in another way with more complexity.  