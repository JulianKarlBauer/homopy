# HomoPy
*Your solution for stiffness problems*

HomoPy is a Python package to perform calculations of effective stiffness properties in homogenized materials, with an emphasize on fiber reinforced polymers. Furthermore, the package offers visualisation tools for elastic stiffness tensors, so called Young's modulus' bodies. These allow a comparison of angle dependent stiffnesses of different materials.
Currently, HomoPy offers two types of homogenization procedures:
- Halpin-Tsai with a Shear-Lag modification
- Mori-Tanaka

## Halpin-Tsai
The Halpin-Tsai method is an empirical approach to homogenize two isotropic materials (cf. [1]. Our approach is modified with the Shear-Lag model after Cox (cf. [2]), which is also used in [3] and [4]. Being a scalar homeginzation scheme, it allows to calculate the effective stiffness in the plane which is orthogonal to the isotropic plane within transverse isotropic materials, as it is the case for unidirectional reinforced polymers. The effective stiffness, or Young's modulus, is then a function of the angle to the reinforcing direction. A fiber distrubtion within the plane is recognized by volume averaging of imaginary plies of individual orientations in analogy to the laminate theory.

## Mori-Tanaka
The Mori-Tanaka scheme goes back to Mori and Tanaka (cf. [5]) and is a mean-field homogenization scheme based on Eshelby's solution (cf. [6]). The implementation so far only allows spheroidal inclusions, which in fact is an ellispoid with identical minor axes or ellipsoid of revolution, respectively. Our algorithm allows to homogenize materials with different types of fibers, each possibily having an individual fiber distrubtion. Being a tensorial homogenization scheme, the fiber orientation tensor is directly included in the calculation and the result is an effective stiffness tensor. The authors would like to emphasize that for multi-inclusion problems or non-isotropic inclusions, the effective stiffness tensor may violate thermodynamic requirements, such as a symmetric stiffness tensor. Further readings of this attribute are given in [7] and [8]. It is in the remit of the user to keep this in mind and act accordingly.

***
Further topic related methods of the package:
- Closures to calculate orientation tensors of forth order from an orientation tensor of second order are implemented by a dependence on the package [fiberoripy](https://github.com/nilsmeyerkit/fiberoripy)
- Determining fiber orientation tensors from micrographs is possible by the implemented method of ellipses (yet to come)

***
[1] John C. Halpin, *Effects of environmental factors on composite materials*, 1969. \
[2] H. L. Cox, *The elasticity and strength of paper and other fibrous materials*, British Journal of Applied Physics 3 (3) (1952) 72–79. doi:10.1088/05083443/3/3/302. \
[3] S.-Y. Fu, G. Xu, Y.-W. Mai, *On the elastic modulus of hybrid particle/short-fiber/polymer composites*, Composites Part B: Engineering 33 (4) (2002) 291–299. doi:10.1016/S1359-8368(02)00013-6. \
[4] S.-Y. Fu, B. Lauke, Y.-W. Mai, *Science and engineering of short fibre-reinforced polymer composites*, Woodhead Publishing (2019). \
[5] T. Mori, K. Tanaka, *Average stress in matrix and average elastic energy of materials with misfitting inclusions*, Acta Metallurgica 21 (5) (1973), 571-574. \
[6] J.-D. Eshelby, *The determination of the elastic field of an ellipsoidal inclusion, and related problems*, Proceedings of the Royal Society of London A 241 (1957), 376–396. \
[7] Y. P. Qiu, G. J. Weng, *On the application of mori-tanaka’s theory involving transversely isotropic spheroidal inclusions*, International Journal of Engineering Science 28 (11) (1990) 1121-1137. doi:10.1016/00207225(90)90112-V. \
[8] G. J. Weng, *The theoretical connection between mori-tanaka’s theory and the hashin-shtrikman-walpole bounds*, International Journal of Engineering Science 28 (11) (1990) 1111–1120. doi:10.1016/00207225(90)90111-U
