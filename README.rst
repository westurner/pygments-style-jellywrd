pygments-style-jellywrd
========================
A pygments version of a jellywrd vim color scheme.

Derivation:

* https://github.com/nanotech/jellybeans.vim
* https://github.com/westurner/dotvim/blob/f3295fb/vimrc#L395 (`PatchColors`)
* https://github.com/westurner/vim2vim
* https://bitbucket.org/birkenfeld/pygments-main/src/default/scripts/vim2pygments.py


Install
=======

Pip
------------------
::

   $ pip install -e https://github.com/westurner/pygments-style-jellywrd#pygments-style-jellywrd

Manual
------
::

   $ git clone https://github.com/westurner/pygments-style-jellywrd
   $ cd pygments-style-jellywrd
   $ python setup.py install

Usage Sample
------------
::

   >>> from pygments.formatter import HtmlFormatter
   >>> HtmlFormatter(style='jellywrd').style
   <class 'pygments_style_jellywrd.jellywrd.JellywrdStyle'>


Export the style as CSS
-----------------------
::

   pygmentize -S jellywrd -f html -a .highlight > jellywrd.css

