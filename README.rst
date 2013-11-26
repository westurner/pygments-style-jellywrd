pygments-style-jellywrd
========================
A pygments version of a jellywrd vim color scheme.

Derived from https://github.com/nanotech/jellybeans.vim 
with https://github.com/honza/vim2pygments 

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

