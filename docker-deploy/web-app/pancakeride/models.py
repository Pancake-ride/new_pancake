from django.db import models

# Create your models here.
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

VEHICLE_TYPE = (
    ('ux', 'uberx'),
    ('cf', 'comfort'),
    ('ul', 'uberxl'),
)

RIDE_STATUS = (
    ('op', 'open'),
    ('cf', 'Confirmed'),
    ('cp', 'Complete'),
)

class Driver(models.Model):
    first_name = models.CharField(max_length = 50, null = True)
    last_name = models.CharField(max_length = 50, null = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, 
                                primary_key = True)
    license_plate_number = models.CharField(max_length = 20, null = False)
    capacity = models.IntegerField(null = False, default = 1,
                                   validators=[MinValueValidator(1)])
    special_vehicle_info = models.TextField('special_vehicle_info', null = True, blank = True, max_length = 200)
    vehicle_type = models.CharField(max_length = 2,
                                     choices = VEHICLE_TYPE,
                                     blank = True,
                                     default = 'cf',
                                     help_text = 'Vehicle type',
                                     null = False)

    

    class Meta:
        ordering = ['last_name']

    def get_absolute_url(self):
        return reverse('', args = [str(self.id)])

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)

class Ride(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          help_text = 'Unique Ride ID')
    owner = models.ForeignKey(User, on_delete = models.SET_NULL,
                              null = True, blank = True,
                              related_name = 'owner_ride')
    driver = models.ForeignKey(Driver, on_delete = models.SET_NULL,
                               null = True, blank = True,
                               related_name = 'driver_ride')
    passenger_num = models.IntegerField(default = 1,
                                        validators = [MinValueValidator(1)])
    destination = models.CharField(max_length = 50, null = False, blank = False)
    arrival_time = models.DateTimeField(null = True, blank = True)
    vehicle_type = models.CharField(max_length = 2,
                                    choices = VEHICLE_TYPE,
                                    blank = True,
                                    null = True,
                                    help_text = 'optinal vehicle type request')
    special_vehicle_info = models.TextField('special_vehicle_info', null = True,
                                            blank = True, max_length = 200)
    
    status = models.CharField(max_length = 2,
                              choices = RIDE_STATUS,
                              blank = True,
                              default = 'op',
                              help_text = 'ride status')

    shareable = models.BooleanField(default=False)
    sharer = models.ForeignKey(User, on_delete = models.SET_NULL,
                               null = True, blank = True,
                               related_name = 'sharer_ride')
    sharer_num = models.IntegerField(default=0)

    def get_sharer_confirm_url(self):
        return reverse('pancakeride:sharer_confirm', args = [str(self.id)])

    def get_driver_confirm_url(self):
        return reverse('pancakeride:driver_confirm', args = [str(self.id)])

    def get_ride_edit_url(self):
        return reverse('pancakeride:ride_request_edit', args=[str(self.id)])

    def get_ride_detail_url(self):
        return reverse('pancakeride:ride_detail', args=[str(self.id)])

    def get_driver_complete_url(self):
        return reverse('pancakeride:driver_complete', args=[str(self.id)])