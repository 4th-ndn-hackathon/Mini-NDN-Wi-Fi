import random


def start_mobility(net, cars, access_points):
    net.plotGraph(max_x=100, max_y=100)
    net.propagationModel('friisPropagationLossModel', sL=2)
    net.seed(random.randint(0, 100))
    #net.startMobility(startTime=0, model='RandomDirection', max_x=100, max_y=100, min_v=0.5, max_v=0.8)
    net.startMobility(startTime=0)
    net.mobility(cars[0], 'start', time=1, position='50.0,50.0,0.0')
    net.mobility(cars[0], 'stop', time=59, position='0.0,100.0,0.0')
    net.mobility(cars[1], 'start', time=1, position='50.0,50.0,0.0')
    net.mobility(cars[1], 'stop', time=59, position='100.0,0.0,0.0')
    net.stopMobility(stopTime=59)
