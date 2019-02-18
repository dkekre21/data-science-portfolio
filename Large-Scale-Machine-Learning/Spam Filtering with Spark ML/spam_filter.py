############ SPAM FILTERING PROGRAM CODE (.py file) #############

## Import required packages
from __future__ import print_function
import sys
from pyspark.sql import SparkSession
from pyspark.mllib.feature import HashingTF
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD

if __name__=="__main__":
	print("This is the name of the script: ", sys.argv[0])
	print("Number of arguments: ", len(sys.argv))
	print("The arguments are: ", str(sys.argv))

## Exception handling
	if len(sys.argv)!=4:
		print("Usage: logit model: ", file=sys.stderr)
		exit(-1)


## Define input path to files - spam, non-spam, and query
	inputPath1=sys.argv[1]
	inputPath2 = sys.argv[2]
	inputPath3 = sys.argv[3]

## Create an instance of a SparkSession object
	spark=SparkSession\
		.builder\
		.appName("SpamFiltering")\
		.getOrCreate()

	sc= spark.sparkContext

## Read input files
	nospam_emails = sc.textFile(inputPath1)
	spam_emails = sc.textFile(inputPath2)
	query_emails=sc.textFile(inputPath3)

## Convert all words into tokens and calculate their frequency 
	tf=HashingTF(numFeatures=10000)
	spam_Features=spam_emails.map(lambda x: tf.transform(x.split()))
	nospam_Features=nospam_emails.map(lambda x: tf.transform(x.split()))

## Create LabeledPoint for spam as '1' and non-spam emails as '0'
	spam=spam_Features.map(lambda x: LabeledPoint(1,x))
	nospam=nospam_Features.map(lambda x: LabeledPoint(0,x))

## Create the training set by combining spam and non-spam emails together
	combined_emails=spam.union(nospam)

## Use the combined data to train the Logistic regression model
	model=LogisticRegressionWithSGD.train(combined_emails)

## Classify query emails into spam and non-spam based on trained model

	## First apply the same HashingTF and create tokens/features
	query_Features=query_emails.map(lambda x: tf.transform(x.split()))
	query_classify=model.predict(query_Features)
	
	## Concatenate the classification prediction with email text
	query_output=query_classify.zip(query_emails)
	
	## Calculate the accuracy of full model : spam + non-spam
	pred=combined_emails.map(lambda x: (x.label,model.predict(x.features)))
	accuracy_model=pred.filter(lambda (act,pred):act==pred).count()/float(combined_emails.count())*100.0

	## Spam accuracy of the model
	predSpam=spam.map(lambda x: (x.label,model.predict(x.features)))
	accuracy_spam=predSpam.filter(lambda (act,pred):act==pred).count()/float(spam.count())*100.0

	## Non-Spam accuracy of the model
	predNoSpam=nospam.map(lambda x: (x.label,model.predict(x.features)))
	accuracy_nospam=predNoSpam.filter(lambda (act,pred):act==pred).count()/float(nospam.count())*100.0
	
	print("\n")
	print("************* CLASSIFYING QUERY EMAILS ******************")
	df=spark.createDataFrame(query_output)
	df.show()
	#print(query_output)
	print("\n")
	
	spark.stop()

	print("************* SPAM FILTERING MODEL ACCURACY ******************")
	print("Accuracy of the model: "+ str(accuracy_model)+ " %")
	print("************* SPAM FILTERING SPAM ACCURACY *******************")
	print("Accuracy of the model: "+ str(accuracy_spam)+ " %")
	print("************* SPAM FILTERING NON-SPAM ACCURACY ***************")
	print("Accuracy of the model: "+ str(accuracy_nospam)+ " %")


############ SPARK- SUBMIT COMMAND SET ##############

## First created four variables to add fexibility for argument path selection, then ran spark submit command

dhanshrivm@dhanshrivm-VirtualBox:~$ PROG="/media/sf_Ubuntu_Shared/spamfilter.py"
dhanshrivm@dhanshrivm-VirtualBox:~$ 
dhanshrivm@dhanshrivm-VirtualBox:~$ INPUT_PATH1="/media/sf_Ubuntu_Shared/emails_nospam.txt"
dhanshrivm@dhanshrivm-VirtualBox:~$ 
dhanshrivm@dhanshrivm-VirtualBox:~$ INPUT_PATH2="/media/sf_Ubuntu_Shared/emails_spam.txt"
dhanshrivm@dhanshrivm-VirtualBox:~$ 
dhanshrivm@dhanshrivm-VirtualBox:~$ INPUT_PATH3="/media/sf_Ubuntu_Shared/query.txt"
dhanshrivm@dhanshrivm-VirtualBox:~$ 
dhanshrivm@dhanshrivm-VirtualBox:~$ ./Downloads/spark-2.3.0-bin-hadoop2.7/bin/spark-submit $PROG $INPUT_PATH1 $INPUT_PATH2 $INPUT_PATH3


##################### OUTPUT ######################

************* CLASSIFYING QUERY EMAILS ******************
+---+--------------------+
| _1|                  _2|
+---+--------------------+
|  1|this is a year of...|
|  1|you are the lucky...|
|  1|Do not miss your ...|
|  1|Get real money fa...|
|  0|Dear Spark Learne...|
|  0|Hi Mom, Apologies...|
|  0|Wow, hey Fred, ju...|
|  0|Hi Spark user lis...|
|  1|Please do not rep...|
|  0|Hi Mahmoud, Are y...|
+---+--------------------+

************* SPAM FILTERING MODEL ACCURACY ******************
Accuracy of the model: 100.0 %
************* SPAM FILTERING SPAM ACCURACY *******************
Accuracy of the model: 100.0 %
************* SPAM FILTERING NON-SPAM ACCURACY ***************
Accuracy of the model: 100.0 %


