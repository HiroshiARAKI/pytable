"""
pyTable
-- A wrapped useful and tiny library to plot Table worked on MatplotLib.

Copyright (c) 2020 HiroshiARAKI All Rights Reserved.

:website     https://hirlab.net/nblog
:author      Hiroshi ARAKI
:mail        araki@hirlab.net
:License     MIT
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from matplotlib.table import Table
import pandas as pd
import numpy as np
from typing import Dict, List, TypeVar, Tuple
import re

T = TypeVar('T', int, float, str)

RED = '\033[31m'
N = '\033[0m'

WARNING_COLOR_CODE = 'Warning: The color code you gave is wrong.'
WARNING_NONE_ROW = 'Warning: You did not give Row data.'
WARNING_NONE_TABLE_TYPE = 'Warning: The Table Type you gave is wrong.'

edges = ['open', 'closed', 'horizontal', 'vertical']
table_types = ['striped', 'dark', 'light', 'sky']

th_face_colors = {
    'dark': '#363636',
    'gray': '#919191',
    'light': '#d6d4d4',
    'sky': '#215aff',
    'blue': '#3944db',
    'red': '#d64045',
    'green': '#239436',
    'orange': '#f57e33',
}

th_text_colors = {
    'dark': '#ffffff',
    'gray': '#ffffff',
    'light': '#222222',
    'sky': '#ffffff',
    'blue': '#ffffff',
    'red': '#ffffff',
    'green': '#ffffff',
    'orange': '#ffffff',
}

colors = {}
colors.update(mc.BASE_COLORS)
colors.update(mc.TABLEAU_COLORS)
colors.update(mc.CSS4_COLORS)
colors.update(mc.XKCD_COLORS)


def table(data: Dict,
          data_loc: str = 'right',
          rows: List[T] = None,
          figsize: Tuple[float, float] = (3, 3),
          th_c: str = None,
          th_loc: str = 'center',
          td_c: str = None,
          td_loc: str = 'center',
          edge: str = None,
          table_type: str = None,
          th_type: str = None,
          th_face: str = None,
          th_text: str = None,
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
    :param table_type:  Table cell types e.g. 'striped'
    :param th_type:     Table header type
    :param th_face:
    :param th_text:
    :param kwargs:

    :return: matplotlib.table.Table object
    """
    df = pd.DataFrame(data)

    edge = 'closed' if edge not in edges else edge

    if th_c is not None:
        if th_c not in colors and not _match_color_code(th_c):
            _warn('th_c => ' + WARNING_COLOR_CODE)
            th_c = None

    if th_c is not None:
        th_c = [th_c for _ in range(len(df.columns))]

    if td_c is not None:
        if td_c not in colors and not _match_color_code(td_c):
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

    tb: Table = ax.table(cellText=df.values,
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

    change_th_design(tb, th_type, len(data))
    change_th_colors(tb, th_face, th_text, len(data))

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
            ['#dddddd' if i % 2 else '#ffffff' for _ in row]
            for i, row in enumerate(cells)
        ]

        return c_colors

    if t_type is 'dark':
        cells = [
            c_data[key] for key in c_data
        ]
        cells = np.array(cells).T
        c_colors = [
            ['#333333' if i % 2 else '#888888' for _ in row]
            for i, row in enumerate(cells)
        ]

        return c_colors

    if t_type is 'light':
        cells = [
            c_data[key] for key in c_data
        ]
        cells = np.array(cells).T
        c_colors = [
            ['#bbbbbb' if i % 2 else '#eeeeee' for _ in row]
            for i, row in enumerate(cells)
        ]

        return c_colors

    if t_type == 'sky':
        cells = [
            c_data[key] for key in c_data
        ]
        cells = np.array(cells).T
        c_colors = [
            ['#a7bcfa' if i % 2 else '#d0daf7' for _ in row]
            for i, row in enumerate(cells)
        ]

        return c_colors


def change_th_design(tb: Table, t_type: str, t_size: int):
    if t_type is None:
        return None
    if t_type not in th_text_colors:
        _warn(WARNING_NONE_TABLE_TYPE)
        return None

    if t_type in th_text_colors:
        for i in range(t_size):
            tb[0, i].set_text_props(color=th_text_colors[t_type])
            tb[0, i].set_facecolor(th_face_colors[t_type])


def change_th_colors(tb: Table, th_face: str, th_text: str, t_size: int):
    if th_face is not None and (_match_color_code(th_face) or th_face in colors):
        for i in range(t_size):
            tb[0, i].set_facecolor(th_face)

    if th_text is not None and (_match_color_code(th_text) or th_text in colors):
        for i in range(t_size):
            tb[0, i].set_text_props(color=th_text)


def _warn(message: str):
    print(RED + message + N)


def _match_color_code(code: str):
    return re.match(r'^#([\da-fA-F]{6}|[\da-fA-F]{3})$', code)
