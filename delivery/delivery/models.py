from django.db import models
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User)

# class Item(models.Model):
#     weight = models.FloatField()
#     name = models.CharField(max_length=20)
#     cost = models.FloatField()

#     def __str__(self):
#         return '{}'.format(self.name)

# class Location(models.Model):
#     def __str__(self):
#         return '{}'.format(self.id)

# class Leg(models.Model):
#     SEA = 0
#     ROAD = 1
#     AIR = 2
#     maxWeight = models.FloatField()
#     time = models.FloatField()
#     cost = models.FloatField()
#     fromLocation = models.ForeignKey(Location, related_name='fromLocation')
#     toLocation = models.ForeignKey(Location, related_name='toLocation')
#     type = models.IntegerField(choices= [(SEA, 'sea'), (ROAD, 'road'), (AIR, 'air')])

#     def __str__(self):
#         return '{}-{}'.format(self.fromLocation, self.toLocation)

# class Route(models.Model):
#     legs = models.ManyToManyField(Leg)
#     currentLocation = models.ForeignKey(Location)

#     def __str__(self):
#         return '{}'.format(self.id)

# class Order(models.Model):
#     STATUS_LAUNCHED = 0
#     STATUS_DELIVERED = 1
#     CRITERIA_TIME = 0
#     CRITERIA_COST = 1

#     creationTime = models.DateTimeField(auto_now_add=True)
#     itemList = models.ManyToManyField(Item)
#     route = models.ForeignKey(Route, null=True, blank=True)
#     status = models.IntegerField(choices=[(STATUS_LAUNCHED, 'launched'), (STATUS_DELIVERED, 'delivered')])
#     criteria = models.IntegerField(choices=[(CRITERIA_COST, 'cost'), (CRITERIA_TIME, 'time')])
#     startLocation = models.ForeignKey(Location, related_name='startLocation')
#     finishLocation = models.ForeignKey(Location, related_name='finishLocation')

#     def getWeight(self):
#         w = 0
#         for item in self.itemList.all():
#             w += item.weight
#         return w