from worker import endpoint
@endpoint.task()
def add(x, y):
    f = open('eject.log', 'a')
    f.write(str(x))
    f.write("\n")
    f.close()
