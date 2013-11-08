===================
sphinx.ecrealltheme
===================

About
=====

This is a Sphinx theme for Ecréall documentations. This theme is freely inspired by sphinx.plonetheme.

Installation
============

Make environment with easy_install::

   $ easy_install sphinxjp.themes.impressjs

Or using buildout::

    [buildout]
    parts=
        sphinx

    [sphinx]
    recipe=zc.recipe.egg
    eggs=
        Sphinx
        sphinx.ecrealltheme

setup conf.py with::

   extensions = ['sphinxjp.themecore']
   html_theme = 'ecrealltheme'
   # Opensearch support with Plone icon
   html_use_opensearch = 'http://my.site.tld/mydoc'
   ...
   # Have a disqus setting for this site to have visitors feedback?
   # (register at http://disqus.com/)
   html_theme_options = {
      'disqus_name': 'the_disqus_site_shortname'
   }


and run::

   $ make html


Requirement
===========

Libraries:

* Python 2.6 or later (not support 3.x)
* Sphinx 1.0.x or later.

Tested with...
==============

* Firefox 3
* Chrome 5


Contributing
============

Fork or being part of the plone collective organization::

    https://github.com/collective/sphinx.ecrealltheme


The ``demo/`` folder is the Sphinx I use to test this theme. You may add
more Sphinx constructs to test the Plone Sphinx theme here.

More doc about Sphinx theming can be found from `here
<http://sphinx.pocoo.org/theming.html>`_.

Credits
=======

* `Cédric Messiant <cedric.messiant@gmail.com>`_
