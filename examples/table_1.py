import ptable as pt


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
    # pt.save('table_1.png')
