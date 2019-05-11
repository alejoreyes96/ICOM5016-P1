CREATE TABLE Human(huid serial primary key,first_name varchar(20),
last_name varchar(20),birthdate varchar(10),huemail varchar(50),
hupassword varchar(50),phone_number char(10));

CREATE TABLE Users(uid serial primary key,human_id integer references Human(huid),
user_name varchar(20),ucreation_date varchar(10),umost_recent_login varchar(10),
profile_picture varchar(50));

CREATE TABLE GroupChats(gid serial primary key,gname varchar(20),
gcreation_date varchar(10),gpicture_id_path varchar(20),
huid integer references Human(huid) on delete cascade);

CREATE TABLE IsMember(uid integer references Users(uid),
gid integer references GroupChats(gid),primary key(uid,gid));

CREATE TABLE Messages(mid serial primary key,uid integer references Users(uid),
mupload_date varchar(10),msize integer,mmessage varchar(100), mmedia_path varchar(50),mtype varchar(50),mlength integer);

CREATE TABLE Hashtags(hid serial primary key,hhashtag varchar(50));

CREATE TABLE PostedTo(mid integer references Messages(mid), gid integer references
GroupChats(gid), primary key(mid,gid));

CREATE TABLE Replies(rpid serial primary key,rpupload_date varchar(10),
rpreply varchar(100),mid integer references Messages(mid),uid integer references Users(uid),rppicture varchar(50),rptype varchar(10),
rpsize integer,rplength integer);

CREATE TABLE Reactions(rid serial primary key,rupload_date varchar(10),
rtype boolean,mid integer references Messages(mid),
rpid integer references Replies(rpid),uid integer references Users(uid));

CREATE TABLE Contains(cid serial primary key,mid integer references Messages(mid),rpid integer references Replies(rpid),
hid integer references Hashtags(hid));

CREATE TABLE Friends(fuid integer references Users(uid),
uid integer references Users(uid), primary key(uid,fuid));