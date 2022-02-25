# Pattern Recognition and Machine Learning

## Conventions
* Vectors are denoted by lower case bold case $$ \mathbf{x} $$, and all vectors are assumed to be column vectors.
* A superscript T denotes teh transpose of a matrix or vector.
* Uppercase bold roman letters are matrices $$ \mathbf{M} $$
* The notation notation $$ (w_1, w..., w_M) $$ denotes a row vector with M elements.
* A functional is denoted $$ f[y] $$ where $$ f(y) $$ is a function.(Functional receives a function and returns a value more info on Appendix D)
* The notation $$ g(x) = O(f(x)) $$  denotes that $$ |f(x)/g(x)| $$ is bounded as $$ x -> inf $$. For instance, if $$ g(x) = 3*x^2 + 2 $$ then $$ g(x) = O(x^2) $$.
* If we have $$ N $$ values $$ \mathbf{x}_1, ...,mathbf{x}_N $$ of a D-dimensional vector, we can conbine into a data matrix $$ \mathbf{X} $$ in which the $$ n^{th} $$ row of $$ \mathbf{X} $$ corresponds to the $$ i^{th} $$ element of the $$ n^{th} $$ observation of $$ \mathbf{x}_n $$.
* For the case of one-dimensional variables we shall denote such a matrix by $$ \mathsf{x} $$ (with size N) which differes from $$ \mathbf{x} $$ (with size D).

