import ptable as pt


if __name__ == '__main__':
    data = {
        'a': [1.0, 2.1, 3.5, '-', 2.0, 1.0, 2.1, 3.5, 4.0, 2.0, ],
        'b': [5.7, 6.1, 7.2, 8.3, 1.2, 5.7, 6.1, 7.2, 8.3, '-', ],
        }

    # The simplest table
    pt.table(data=data)

    pt.show()
    # pt.save('table_0.png')
