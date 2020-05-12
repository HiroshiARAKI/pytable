import matplotlib.pyplot as plt
import matplotlib.colors as mc
from matplotlib.table import Table
import pandas as pd
import numpy as np
from typing import Dict, List, TypeVar, Tuple, Optional
import re

T = TypeVar('T', int, float, str)

RED = '\033[31m'
N = '\033[0m'

WARNING_COLOR_CODE = 'Warning: The color code you gave is wrong.'
WARNING_NONE_ROW = 'Warning: You did not give Row data.'
WARNING_NONE_TABLE_TYPE = 'Warning: The Table Type you gave is wrong.'

edges = ['open', 'closed', 'horizontal', 'vertical']
table_types = ['striped']

colors = {}
colors.update(mc.BASE_COLORS)
colors.update(mc.TABLEAU_COLORS)
colors.update(mc.CSS4_COLORS)
colors.update(mc.XKCD_COLORS)


def table(data: Dict,
          data_loc: str = 'right',
          rows: List = None,
          figsize: Tuple[int, int] = (3, 3),
          th_c: str = None,
          th_loc: str = 'center',
          td_c: str = None,
          td_loc: str = 'center',
          edge: str = None,
          table_type: str = None,
          **kwargs
          ) -> Table:
    """
    Create Table
    -------------

    :param data:        table column data as dict
    :param data_loc:    data align {'left', 'center', 'right'}
    :param rows:        row data as list
    :param figsize:     table figsize as Tuple
    :param th_c:        Table header's background-color - you can use colorcodes and matplotlib's color names
    :param th_loc:      Table header align {'left', 'center', 'right'}
    :param td_c:        Table data's (rows') background-color - you can use colorcodes and matplotlib's color names
    :param td_loc:      Table data's (rows') align {'left', 'center', 'right'}
    :param edge:        Table edges {'open', 'closed', 'horizontal', 'vertical'}
    :param table_type:  Table types e.g. 'striped'
    :param kwargs:

    :return: matplotlib.table.Table object
    """
    df = pd.DataFrame(data)

    edge = 'closed' if edge not in edges else edge

    if th_c is not None:
        if th_c not in colors and not re.match(r'^#([\da-fA-F]{6}|[\da-fA-F]{3})$', th_c):
            _warn('th_c => ' + WARNING_COLOR_CODE)
            th_c = None

    if th_c is not None:
        th_c = [th_c for _ in range(len(df.columns))]

    if td_c is not None:
        if td_c not in colors and not re.match(r'^#([\da-fA-F]{6}|[\da-fA-F]{3})$', td_c):
            _warn('td_c => ' + WARNING_COLOR_CODE)
            td_c = None

    if td_c is not None:
        if rows is not None:
            td_c = [td_c for _ in range(len(rows))]
            rows = [str(' ' + r + ' ') for r in rows]
        else:
            _warn(WARNING_NONE_ROW)
            td_c = None

    fig, ax = plt.subplots(figsize=figsize)

    ax.axis('off')
    ax.axis('tight')

    tb = ax.table(cellText=df.values,
                  cellLoc=data_loc,
                  cellColours=_get_cell_c(table_type, data),
                  colLabels=df.columns,
                  colLoc=th_loc,
                  colColours=th_c,
                  rowLabels=rows,
                  rowLoc=td_loc,
                  rowColours=td_c,
                  bbox=[0, 0, 1, 1],
                  edges=edge,
                  **kwargs
                  )

    return tb


def show():
    """
    show table
    :return:
    """
    plt.show()
    plt.close()


def save(filename, dpi=150):
    """
    save table
    :param filename:
    :param dpi:
    :return:
    """
    plt.savefig(filename, dpi=dpi)
    plt.close()


def show_colors():
    """
    show color name codes
    :return:
    """
    nums = len(colors)
    print('# of colors variation: {}'.format(nums))
    for c in mc.BASE_COLORS:
        print(c, end=', ')
    print()

    for c in mc.TABLEAU_COLORS:
        print(c, end=', ')
    print()

    for c in mc.CSS4_COLORS:
        print(c, end=', ')
    print()

    for c in mc.XKCD_COLORS:
        print(c, end=', ')
    print()


def _get_cell_c(t_type: str, c_data: Dict):
    if t_type is None:
        return None
    if t_type not in table_types:
        _warn(WARNING_NONE_TABLE_TYPE)
        return None

    if t_type is 'striped':
        cells = [
            c_data[key] for key in c_data
        ]
        cells = np.array(cells).T
        c_colors = [
            ['#cccccc' if i % 2 else '#ffffff' for _ in row]
            for i, row in enumerate(cells)
        ]

        return c_colors


def _warn(message: str):
    print(RED + message + N)

