from __future__ import with_statement
import os.path

MODULE_TEMPLATE=""".. Autogenerated by genmods.py

******************************************************************************
%(name)s
******************************************************************************

:mod:`%(package)s.%(module)s`
==============================================================================

.. automodule:: %(package)s.%(module)s
   :members:
   :undoc-members:
   :inherited-members:
   :show-inheritance:

"""

INDEX_TEMPLATE=""".. Autogenerated by genmods.py

.. _api-index:

##############################################################################
   %(package_name)s
##############################################################################

.. only:: html

   :Release: |version|
   :Date: |today|

.. toctree::

   %(rsts)s
"""



def genfiles(package, package_name, modules, dir='api'):

    if not os.path.exists(dir):
        os.makedirs(dir)

    for module,name in modules:
        with open(os.path.join(dir,module+'.rst'), 'w') as f:
            f.write(MODULE_TEMPLATE%locals())

    rsts = "\n   ".join(module+'.rst' for module,name in modules)
    with open(os.path.join(dir,'index.rst'),'w') as f:
        f.write(INDEX_TEMPLATE%locals())


modules=[
    ('basepage', 'basepage'),
     ('console', 'console'),
     ('fit_thread', 'fit_thread'), 
     ('fitpage', 'fitpage'),
     ('fitpanel', 'fitpanel'),
     ('fitproblem', 'fitproblem'),
     ('fitting', 'fitting'), 
     ('help_panel', 'help_panel'),
     ('hint_fitpage', 'hint_fitpage'), 
     ('model_thread', 'model_thread'),
     ('models', 'models'),
     ('pagestate', 'pagestate'),
     ('simfitpage', 'simfitpage'),
]
package ='sans.perspectives.fitting'
package_name ='Reference'

if __name__ == "__main__":
    genfiles(package, package_name, modules, dir='api/perspectives/fitting')

    print "Sphinx: generate .rst files complete..."
    