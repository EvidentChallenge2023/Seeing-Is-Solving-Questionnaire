# Description de l'algorithme utilisé

Une équation en fonction de la distance $x$ entre le point $P$ et le point d'entrée $O$ peut se trouver en appliquant le [principe de Fermat](https://en.wikipedia.org/wiki/Snell's_law#Derivation_from_Fermat's_principle) afin de trouver la loi de Snell-Descartes.

$$
f(x)=\frac{x}{v_1\sqrt{x^2 + a^2}} + \frac{ - (l - x)}{v_2\sqrt{(l-x)^2 + b^2}}
$$

Voir [cette image](https://upload.wikimedia.org/wikipedia/commons/5/51/Snells_law_Diagram_B_vector.svg) pour référence. Considérant que $\frac{x}{\sqrt{x^2 + a^2}} =\sin\theta_1$ et $\frac{  l - x}{\sqrt{(l-x)^2 + b^2}}=\sin\theta_2$, on voit que cette première équation correspond à la loi de Snell-Descartes si $f(x) = 0$.

La dérivée par rapport à $x$ de cette fonction donne:

$$
f'(x)=\frac{a^2}{v_1(x^2 + a^2)^{3/2}} + \frac{b^2}{v_2((l-x)^2 + b^2)^{3/2}}
$$

Connaissant une fonction et sa dérivée, la solution pour $x$ peut se trouver en utilisant la [méthode de Newton](https://en.wikipedia.org/wiki/Newton%27s_method) pour trouver le zéro de la première équation $f(x)$ avec une estimation initiale de $x_0 = l/2$
