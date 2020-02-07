# erss-hwk1-sz161-qf31

Ride Sharing System Web Application

Shuchen Zhao	    NetID: sz161
Qizhang Feng			NetID: qf31

1.Overview

In this web application, we developed a simplified version of an online ride-sharing system similar to an existing business application like Uber or Lyft. In our ride-sharing system, we established the interaction between the user and the system database, allowing users to register and connect to different system functions. This web application allows both owners, owners of vehicles and drivers, which means users can apply to join the new owners, owners as co-owners of other existing owners and owners to accept other co-owners as drivers.

2. Danger log
2.1 User login failure [2020/1/26]

In the login session, we will check the username as well as the password. If username or password is not correct, the login page will be freshed, and user can login to the main home page untill username and password can match the record in database.

2.2 Invalid registration input, email [2020/1/28]

In every registration session, the input value in the form will be checked. If an invalid input is found, a helper message will come out and the form will be freshed. Untill all the values in form is valid, the form can be posted to the server, and the request or registraion can be done successfully.

2.3 Ride owner making a new request [2020/1/31]

When a user request a new ride, some information is required like destination, arrival time etc. For required the information, the user can not skip or leave if blank or they can not make a new request. Some of informations like vehicle type will be set as default value. For those optional value like vehicle info, the user can skip it.

2.4 Driver search [2020/1/31]

User may search for the rides that match his vehicle info like capacity and vehicle type. Only the ride requests in open status can be found. And as driver, a user will never see the ride request whose owner or sharer is himself.

2.5 Sharer search [2020/2/2]

User may search for the rides to join it as a sharer. They need to fill in the destination and arrival time windows to match the open status ride request. And only the ride request that is marked as shareable can be listed in the search result. Moreover, one request can joined by one sharer but sharer's party size is not limited. A user can not find the requests whose owner is himself.