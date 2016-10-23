#encoding=utf-8
#this is for the python manage.py shell test
from orderTicket.models import Train, Station, Price, Seat
from datetime import datetime

class CreateNewTrain(object):
    def __init__(self, train_id, station_list, distance_list, arrive_time_list):
        self.id = train_id
        self.station = station_list
        self.distance = distance_list
        self.arrive_time = arrive_time_list
        self.num = len(arrive_time_list)
    
    def addToDB(self):
        train = Train(train_id = self.id,
                      train_type= self.id[0],
                      num_station =self.num,
                      distance = self.distance[-1])
        train.save()
        for i in range(self.num):
            station = Station(station_name = self.station[i],
                              train_come_by = Train.objects.get(train_id=self.id),
                              order_of_station = i+1,
                              arrive_time = self.arrive_time[i],
                              distance_count = self.distance[i])
            station.save()
            

class AddSeat(object):
    def __init__(self, train_id, seat_type_list, seat_count_list, dateList): #index is the NO of the carriage
        self.train_id = train_id
        self.seat_type = seat_type_list
        self.seat_count = seat_count_list
        self.dateList = dateList

    def addToDB(self):
        train = Train.objects.get(train_id = self.train_id)
        status_length = train.num_station
        for date in self.dateList:
            for index, seat_type in enumerate(self.seat_type):
                for seat in range(self.seat_count[index]):
                    seat = Seat(train_id=train,
                                carriage_id = index+1,
                                seat_type = seat_type,
                                seat_id = seat + 1,
                                date = date,
                                status = bin(2**status_length -1)[2:] #1 means sold, 0 means avilable.
                                )
                    seat.save()

class Search(object):
    def __init__(self, start, end, date):
        self.start = start
        self.end = end
        self.date = date

    def get_train():
        trainList_start = Station.objects.filter(station_name=self.start)
        trainList_end = Station.objects.filter(station_name=self.end)
        for train in (trainList_start & trainList_end):
            start_station = Station.objects.fil
        return


def deleteTrain(train_id):
    train = Train.objects.get(train_id = train_id)
    train.delete()
train_id = 'G312'
station_list = ['广州南', '韶关', '衡阳东','衡山西', '长沙南', '岳阳东', '赤壁北', '武汉'] 
#应该有到站时间和出发时间之分，这里只考虑出发时间,除终点站以外
arrive_time_list = ['07:00', '07:53', '08:54', '09:09', '09:45', '10:21', '10:44', '11:18']
distance_list = [0,300, 500, 600, 700, 800, 1000, 1200]
seat_type_list = ['一等座','一等座', '二等座', '二等座', '二等座','商务座', '商务座']
seat_count_list = [10, 10, 20, 20, 20, 15,15]
dateList = [datetime(2016,10,1), datetime(2016,10,2), datetime(2016,10,3)]

m = Train.objects.all()
m.delete()

newTrain = CreateNewTrain(train_id, station_list, distance_list, arrive_time_list)
newTrain.addToDB()
newSeat = AddSeat(train_id, seat_type_list, seat_count_list, dateList)
newSeat.addToDB()
