import os

def does_file_exist(filename):
    return filename in os.listdir()

def get_file_contents(filename):
    if does_file_exist(filename):
        f = open(filename)
        text_file = f.readlines()
        return text_file

filename = ('AirQuality.csv')
tes_dir = 'testDir'
header = get_file_contents(filename)[0]

if does_file_exist(tes_dir):
    pass
else:
    os.mkdir('testDir')
for i in range(3, 13):
    j = '%02d' % i
    path = 'testDir/' + j + '-2004.csv'
    month = j + '/2004'
    data = list(filter(lambda line : month in line.split(";")[0], get_file_contents(filename)))
    f = open(path, 'w')
    f.write(header)
    f.write(str(data))

for i in range(1, 5):
    j = '%02d' % i
    path = 'testDir/' + j + '-2005.csv'
    month = j + '/2005'
    ndata = list(filter(lambda line : month in line.split(";")[0], get_file_contents(filename)))
    f = open(path, 'w')
    f.write(header)
    f.write(str(ndata))

print(data)
print()

# def create_monthly_responses(filename):
#     if does_file_exist(filename):
#         os.mkdir('monthly_responses')
#         header = get_file_contents(filename)[0]
#         for i in range(3, 13):
#             j = '%02d' % i
#             path = 'monthly_responses/' + j + '-2004.csv'
#             month = j + '/2004'
#             data = [line for line in get_file_contents(filename) if month in line[0]]
#             f = open(path, 'w')
#             f.write(header)
#             f.write(str(data))

#         for i in range(1, 5):
#             j = '%02d' % i
#             path = 'monthly_responses/' + j + '-2005.csv'
#             month = j + '/2005'
#             ndata = list(filter(lambda line : month in line.split(";")[0], get_file_contents(filename)))
#             f = open(path, 'w')
#             f.write(header)
#             f.write(str(ndata))