# ICOM5016 - Social Media Based Webpage
  In this project, we will be creating a webpage social media network called Fast Friends Media where any user can post pictures as well 
videos; and any other user that was in the group to which the post was uploaded will be able to react or reply to said post. 

As part of the phase one we were to implement the backend without connection to the database as well as the ER Diagram which can be found 
on pdf file. Inside the SRC folder, one can find the main app.py where one can run the current flask project. 

The ER Diagram entities and the corresponding relationships are as followed:
1. Human - Users is a hierarchical relationship. This relationship was created since most traits between users must be inherited but these
can't be accesed by other users due to their relationships.
2. Human - Creates - Group is a one to many relationship since one human can create many groups but many groups can only belong to one
human. This causes that Group to be an entity that has total participation because without someone to create it, the group can't exist. 
3. Users - Belongs - Group is a many to many relationship due to one user can be part of many groups and one group can have many users.
4. Users - Friends - Users is a many to many relationship since any one user can have many users as friends.
5. Users - Sends - Message(Posts) is a one to many relationship, where the user can send many messages but any message can only be sent 
by one user. 
6. Messages(Posts) - Has - Reactions is a many to many relationship, in this case we have that a weak entity which is reactions since 
these can't exist without a message. Thus this implies total partition must be neeeded from reactions in this relationship.
7. Messages(Posts) - Videos AND Pictures is a hierarchical relationship since a post can possibly contain videos and pictures but this 
doesnt imply that it has to contain such things. Most of the attributes are then inherited from the Message such as date, size, user id,
etc.
8. Messages(Posts) - Contains - Hashtags is a many to many relationship, in which we can see that one message can have many hashtags and 
one hashtag can be in many messages. 
9. Messages(Posts) - Has/Belongs - Replies is a one to many relationships since one message can have multiple replies but every reply can 
only belong to one message. 
