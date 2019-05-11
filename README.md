## FFMA Chat App

In this project, we have created a web-based for a social media network called Fast Friends Media App which allows any one user to create a group which the user can add friends via email to the  existing group. Once the group has members, these friends can upload pictures, videos, like current social media networks. Any user can give a "like" or "dislike" to the message, also can reply with yet another picture or video as well. 

## Creators 

Under the guidance of Dr. Manuel Rodriguez, our development group consisted of Crystal Torres, Kahlil Fonseca and Alejandro Reyes. This proyect was made for the class ICOM 5016, May 10th 2019 in accordance to the requirements of the course. 

## Finally 

Thank you for your attention!! Hope you like the app!!


## ER Explanation:
As part of the phase one we were to implement the backend without connection to the database as well as the ER Diagram which can be found on pdf file. Inside the SRC folder, one can find the main app.py where one can run the current flask project. 

The ER Diagram entities and the corresponding relationships are as followed:
1. Human - Users is a hierarchical relationship. This relationship was created since most traits between users must be inherited but these can't be accesed by other users due to the type of relationships.
2. Human - Creates - GroupChat is a one to many relationship since one human can create many groups but many groups can only belong to one human. This causes that Group to be an entity that has total participation because without someone to create it, the group can't exist. 
3. Users - Belongs - Group is a many to many relationship due to one user can be part of many groups and one group can have many users.
4. Users - Friends - Users is a many to many relationship since any one user can have many users as friends.
5. Users - Sends - Message is a one to many relationship, where the user can send many messages but any message can only be sent 
by one user. 
6. Messages - Reacts - Reactions is a many to many relationship, in this case we have that a weak entity which is reactions since 
these can't exist without a message. Thus this implies total partition must be neeeded from reactions in this relationship.
7. Replies - Reply Reacts - Reactions  is a many to many relationship, in this case we have that a weak entity which is reactions since 
these can't exist without a reply. Thus this implies total partition must be neeeded from reactions in this relationship.
8. Messages - Contains - Hashtags is a many to many relationship, in which we can see that one message can have many hashtags and 
one hashtag can be in many messages. 
9. Messages - Replies - Replies is a one to many relationships since one message can have multiple replies but every reply can 
only belong to one message. 
