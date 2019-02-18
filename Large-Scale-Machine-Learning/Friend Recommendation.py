
################# INPUT FILE ###########################

format of input : <user id>, <friend ids..>
100,200 300
200,100 300
300,100 200
400,100 200
500,100 300
600, 100

400 500 600
400
400 500
300

################## SPARK- SHELL PROGRAM ##########################

dhanshrivm@dhanshrivm-VirtualBox:~/Downloads/spark-2.3.0-bin-hadoop2.7$ pyspark
Python 2.7.12 (default, Dec 4 2017, 14:50:18)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
2018-06-10 00:04:00 WARN Utils:66 - Your hostname, dhanshrivm-VirtualBox resolves to a
loopback address: 127.0.1.1; using 10.0.2.15 instead (on interface enp0s3)
2018-06-10 00:04:00 WARN Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another
address
2018-06-10 00:04:01 WARN NativeCodeLoader:62 - Unable to load native-hadoop library
for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use
setLogLevel(newLevel).
Welcome to
____
__
/ __/__ ___ _____/ /__
_\ \/ _ \/ _ `/ __/ '_/
/__ / .__/\_,_/_/ /_/\_\
version 2.3.0
/_/
Using Python version 2.7.12 (default, Dec 4 2017 14:50:18)
SparkSession available as 'spark'.
>>> from collections import Counter
>>>
>>> import itertools
>>>
>>>
>>>
>>> fileName = '/media/sf_Ubuntu_Shared/friend data.txt'
## read the filename
>>>
>>> N = 10 #only ouput 10 most possible friends ( not necessary )
>>>
>>>
>>>## Define Function: Convert each line <user, <friends>> into connections and common
friends. For example, for user1 <100> (100,200) (100,300) can be represented as
connections
### whereas we can say (200,300) have 100 as common friend. In order to minimize
dependency, the connections and commons are derived from same line and not across the
lines.
### If <person1,person2> are friends then map them to -ve number, so as it can be
filtered out to avoid suggesting friends as recommendations. Common friends are counted
on the go.
>>> def connecteds_and_commons(line):
...
minimum = -9999999999
...
user, friends = line.split(",")
...
friends = friends.split()
...
connecteds = [((user, friend), minimum) for friend in friends]
...
commons = [(pair, 1) for pair in itertools.permutations(friends, 2)]
...
return connecteds + commons
...
>>>
>>>
>>> data =sc.textFile( fileName, 4 )
# Read file. Into 4 partitions
>>>
>>> connections=data.flatMap( connecteds_and_commons ).reduceByKey( lambda total,
current: total + current )
## manitain count of connections and commons per user
>>>
>>> commons=connections.filter(lambda (pair, counts): counts > 0)
# filter out
connections
>>>
>>>
... friendRecommendation=(commons.map(lambda ((user, friend), counts): (user, (counts,
friend)))
## Recommend friend. Output in format <user id>, [<friend id,count of
mutual friends>...]
...
.groupByKey()
...
.map(lambda (user, suggestions):(user, Counter( dict( (friend,
count) for count, friend in suggestions ) ).most_common( N ) ) )
...
)
>>>
>>>
>>> ###################### OUTPUT #############################
>>> friendRecommendation.collect()
mutual friends>...]

## Output in format <user id>, [<friend id,count of

[(u'300', [(u'600', 1)]), (u'200', [(u'500', 2), (u'600', 1)]), (u'600', [(u'300', 1),
(u'200', 1), (u'500', 1), (u'400', 1)]), (u'500', [(u'200', 2), (u'400', 2), (u'600',
1)]), (u'400', [(u'500', 2), (u'600', 1)])]
>>>

################### References ##################
1.Data Algorithms - Recipes for Scaling Up with Hadoop and Spark, by Mahmoud Parsian
2.http://xjlin0.github.io/tech/2015/08/30/suggesting-friends-by-mapreduce

