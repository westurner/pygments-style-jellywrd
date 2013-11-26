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

   pygmentize -S jellywrd -f html > jellywrd.css

