# erss-hwk1-sz161-qf31

Ride Sharing System Web Application

Shuchen Zhao	    NetID: sz161
Qizhang Feng			NetID: qf31

1.Overview

In this web application, we developed a simplified version of an online ride-sharing system similar to an existing business application like Uber or Lyft. In our ride-sharing system, we established the interaction between the user and the system database, allowing users to register and connect to different system functions. This web application allows both owners, owners of vehicles and drivers, which means users can apply to join the new owners, owners as co-owners of other existing owners and owners to accept other co-owners as drivers.

2.Danger log
2.1User login failure[2019/1/20]

In the login session, we make use of the error attribute in the form, which can be implemented as {{ form.error }}. If this field is true and we detect it, we then print an error message to inform the user that her account login information was not correct, and meanwhile we redirect the page to the login page again. 

2.2Invalid registration input, email[2019/1/25]

When the user is doing registration, no matter she is registering as a user or driver, system will check the username and if this username has already been registered, it will return a error message to let the user know her input username has already existed. 

2.3	Ride owner making a new request
2.3.1 	Skip required attributes [2019/1/29]

When the user is making a new riding request as a ride owner, she has to provide the correct information about the ride destination, arrival time, passenger number, and some other optional information like special request, special vehicle information. For the above required attributes, we set those input attribute as “required”. Therefore, when the user skip one of these table, the system will automatically remind the user to fill in the required table. 

2.3.2	Invalid input for certain attribute[2019/1/31]

User may likely type in some invalid information when she is making the ride request. For example, we have set the passenger number to between 1 and 6 by confining the limit of input number between 1 and 6. If the user type in some outranged number or some invalid character in this field, the system will report the feedback to this user and ask her to fill in the correct information again. Also, as for the arrival time, this is a big issue. First the user has to type in the correct format datetime, we have already given user the hint in the placeholder of the input section. Then the arrival time user typed in cannot before the current local time. 


2.4 	Permission issue[2019/2/2]

There will be a corner case where a driver already search and get a list of the open list, and another not-driver user directly copy this page URL and want to get the same open order list. We handle this by adding a exception pattern, and before entering this page, the system will check the user’s authentication to this page. If it found this access is not authenticated by the current user or there is no login information about user, it will raise an exception.

2.5	Driver search[2019/2/4]

As a driver, she is supposed to view the whole open list. However, in this assignment, there are two special attributes for the user, which are special_requests and required_vehicle_type, and two special attributes for the driver, which are special_vehicle_info and my_vehicle_type. In the assignment requirements, these user’s attributes must exactly match those of the driver’s info. That is to say, special_requests(user) == special_vehicle_info(driver) and required_vehicle_type(user) == my_vehicle_type(driver). Only under the situations that these matches, will the driver view all the required order requests. And also, if the user did not provide and special requests or required vehicle type, the driver is also able to see this order request.


2.6	Overnumbered sharer
If the user keep joining one ride, resulting in the number of passengers getting larger and larger, we have apply a mechanism to avoid and set the max limit of passengers as the driver’s vehicle capacity.
