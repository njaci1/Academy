import csv

filename = 'top_4.csv'

header = ('Rank', 'Rating', 'Title')

data = [
    (1,9.5,'Heartbreak Kid'),
    (2,9.6,'Knocked Up'),
    (3,9.7,'Meet The Parents'),
    (4,9.8,'Change Up')
]


def writer(header, data, filename):

    with open(filename, 'w', newLine ='') as csvfile:
        movies = csv.writer(csvfile)
        movies.writerow(header)
        for x in data:
            movies.writerow(x)


