pyTable
=======

|Python| |matplotlib|

| pyTable is the library to plot table easily!
| (on matplotlib)

installation
------------

``$ pip install pytab``

How to use?
-----------

Example / `table_0.py <examples/table_0.py>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can plot a table easily by giving data as a dict object as below.

.. code:: python

   import pytab as pt


   if __name__ == '__main__':
       data = {
           'a': [1.0, 2.1, 3.5, '-', 2.0, 1.0, 2.1, 3.5, 4.0, 2.0, ],
           'b': [5.7, 6.1, 7.2, 8.3, 1.2, 5.7, 6.1, 7.2, 8.3, '-', ],
           }

       # The simplest table
       pt.table(data=data)

       pt.show()

.. figure:: https://github.com/HiroshiARAKI/pytable/blob/master/examples/table_0.png?raw=true
   :alt: table0

   table0

Example / `table_1.py <examples/table_1.py>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

And, you can design a table easily.

.. code:: python

   import pytab as pt


   if __name__ == '__main__':
       data = {
           'a': [1.0, 2.1, 3.5, 4.0, 2.0, 1.0, 2.1, 3.5, 4.0, 2.0, ],
           'b': [5.7, 6.1, 7.2, 8.3, 1.2, 5.7, 6.1, 7.2, 8.3, 1.2, ],
           }

       rows = [str(i) for i in range(len(data['a']))]

       pt.table(data=data,
                rows=rows,  # set numbers as row
                th_c='#aaaaee',  # set table header background-color
                td_c='gray',     # set table data (rows) background-color
                table_type='striped',  # set table type as 'striped'
                )

       pt.show()

.. figure:: https://github.com/HiroshiARAKI/pytable/blob/master/examples/table_1.png?raw=true
   :alt: table1

   table1

LICENSE
-------

| MIT
| Copyright (c) 2020 HiroshiARAKI All Rights Reserved.

.. |Python| image:: https://img.shields.io/badge/Python-%3E=3.5-a0f.svg?style=flat
.. |matplotlib| image:: https://img.shields.io/badge/matplotlib-%3E=3.1.2-2af.svg?style=flat
