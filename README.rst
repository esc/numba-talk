==========
Numba Talk
==========

My Numba talk.

Abstract
========

In this talk I will take you on a whirlwind tour of Numba and you will be
quipped with a mental model of how Numba works and what it is good at. At the
end, you will be able to decide if Numba could be useful for you.

In this talk I will take you on a whirlwind tour of Numba, the just-in-time,
type-specializing, function compiler for accelerating numerically-focused
Python. Numba can compile the computationally intensive functions of your
numerical programs and libraries from Python/NumPy to highly optimized binary
code. It does this by inferring the data types used inside these functions and
uses that information to generate code that is specific to those data types and
specialised for your target hardware. On top of that, it does all of this
on-the-fly---or just-in-time---as your program runs. This significantly reduces
the potential complexity that traditionally comes with pre-compiling and
shipping numerical code for a variety of operating systems, Python versions and
hardware architectures. All you need in principle, is to
``conda install numba`` and decorate your compute intensive functions with
``@njit``!

This talk will equip you with a mental model of how Numba is implemented and
how it works at the algorithmic level. You will gain a deeper understanding of
the types of use-cases where Numba excels and why. Also, you will understand
the limitations and caveats that exist within Numba, including any potential
ideas and strategies that might alleviate these. At the end of the talk you
will be in a good position to decide if Numba is for you and you will have
learnt about the concrete steps you need to take to include it as a dependency
in your program or library.

Speaker-Bio
===========


Valentin `esc` Haenel is a long-time "Python for Data" user and developer who
still remembers hearing Travis Oliphant's NumPy keynote at the EuroScipy 2008.
This was during a time where he first became aware of the nascent scientific
Python stack. He started using Python for simple modeling of spiking neurons
and evaluation of data from perception experiments during his Masters degree in
computational neuroscience.  Since then he has been active as a contributor
across more than 100 open source projects. For example, within the Blosc
ecosystem where he has contributed to Bcolz, Python-Blosc and Bloscpack.
Furthermore, he has acquired significant experience as a Git trainer and
consultant and had published the first German language book about the topic in
2011.  In 2014 and 2015 he helped kickstart the PyData Berlin community
alongside a few other volunteers and co-organized the first two editions of the
PyData Berlin Conference. Since 2019 he works for Anaconda as a senior software
engineer on the Numba project. His areas of contribution for the project so far
have been social architecture, release management, mutable datastructures and
recently, the compiler frontend.

Past Events
===========

* Turchin Seminar 2022-03-04 :: Presented Numba to Andrei Klimov and others as
  part of the Turchin Seminar (Online) :: `slides <https://github.com/esc/numba-talk/blob/main/pdf/2022-03-04-turchin-seminar-haenel-numba.pdf>`_
* EuroScipy 2019 :: `website <https://pretalx.com/euroscipy-2019/talk/EDNVGJ/>`_, and
  `slides <https://github.com/esc/numba-talk/blob/main/pdf/2019-09-05-euroscipy-haenel-numba.pdf>`_.

Dependencies
============

The talk is made with:

* `wiki2beamer <http://wiki2beamer.sourceforge.net/>`_ (included in repository)
* `LaTeX Beamer <https://bitbucket.org/rivanvx/beamer/wiki/Home>`_
* `Pygments <http://pygments.org/>`_
* `Minted <http://code.google.com/p/minted/>`_ (included in repository)
* `ccBeamer <http://blog.hartwork.org/?p=52>`_ (included in repository)

Licensing
=========

Content
-------

All Content is...

* Copyright 2019 Valentin Haenel <valentin@haenel.co>
* Licensed under the terms of `Attribution-ShareAlike 3.0 Unported  (CC BY-SA 3.0)  <http://creativecommons.org/licenses/by-sa/3.0/>`_

Included Dependencies
---------------------

The following dependencies are shipped with the sources:

* Wiki2beamer (file: ``wiki2beamer-0.10.0``) is licensed under Gnu Public Licence v2
* Minted (file: ``minted.sty``) is licensed under LaTeX Project Public License  version 1.3
* ccBeamer (directory: ``creative_commons/``) is licensed under Creative Commons Attribution-ShareAlike 3.0
