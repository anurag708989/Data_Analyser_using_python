#for hacktoberfest2k20:)

import mysql.connector as sql
import numpy as np
import matplotlib.pyplot as plt  
import sys



database = 'STASTISTICAL_DATA_ANALYSIS'
user = 'customer'
password = ''
branchName = "Chemical_2019" # Table Name


try:
	
	conn = sql.connect(host='localhost',database=database,user=user,password=password)

	cursor = conn.cursor()


except Exception as e:
	sys.exit("Sorry, Couldn't Connect to Server. Please try again later.")


 ##########################################################################################################################################################################################################"""                         The Functions Start Here                                        """


def studentDataCollector(RollNo_Enter):

	RollNo_Enter_x = str(int(RollNo_Enter)%100)

	cursor.execute(f"select Cgpa, Name from {branchName} where Rollno = {RollNo_Enter};")
	name_cgpa_enter = cursor.fetchall()


	Cgpa_Enter, Name_Enter = name_cgpa_enter[0]

	Cgpa_Enter = np.array(Cgpa_Enter)
	Name_Enter = np.array(Name_Enter)

	return (RollNo_Enter_x, Cgpa_Enter, Name_Enter)
	


def rollnoCgpaPassCollector():

	cursor.execute(f"Select RollNo, Cgpa from {branchName} where Cgpa >= 3;")
	rollno_cgpa_pass = cursor.fetchall()

	RollNo_Pass = []
	Cgpa_Pass = []

	for item in rollno_cgpa_pass:

		rollno_pass, cgpa_pass =  item

		RollNo_Pass.append(rollno_pass)
		Cgpa_Pass.append(cgpa_pass)


	RollNo_Pass_x = []

	for i in RollNo_Pass:
		RollNo_Pass_x.append(str(int(i)%100))

	RollNo_Pass_x = np.array(RollNo_Pass_x) 
	Cgpa_Pass = np.array(Cgpa_Pass)
	Cgpa_Pass=Cgpa_Pass[::-1]
	RollNo_Pass_x=RollNo_Pass_x[::-1]



	return (RollNo_Pass, Cgpa_Pass, RollNo_Pass_x)


def rollnoCgpaFailCollector():

	cursor.execute(f"Select RollNo, Cgpa from {branchName} where Cgpa < 3;")
	rollno_cgpa_fail = cursor.fetchall()

	RollNo_Fail = []
	Cgpa_Fail = []

	for item in rollno_cgpa_fail:

		rollno_fail, cgpa_fail =  item

		RollNo_Fail.append(rollno_fail)
		Cgpa_Fail.append(cgpa_fail)


	RollNo_Fail_x = []

	for i in RollNo_Fail:
		RollNo_Fail_x = RollNo_Fail_x + [str(int(i)%100)]

	RollNo_Fail_x = np.array(RollNo_Fail_x)

	return (RollNo_Fail, Cgpa_Fail, RollNo_Fail_x)


def cgpaDistributor():


	
	
	cgpa_eq_10=0   	# 10
	cgpa_less_10=0 	# 9-10
	cgpa_less_9=0 	# 8-9
	cgpa_less_8=0 	# 7-8
	cgpa_less_7=0 	# 6-7
	cgpa_less_6=0 	# 5-6
	cgpa_less_5=0 	# 4-5
	cgpa_less_4=0	#3-4
	cgpa_less_3=0 	#2-3
	cgpa_less_2=0 	#1-2
	cgpa_less_1=0	#0-1

	for i in Cgpa_All:

		if i==10:
			cgpa_eq_10 += 1

		if i>=9 and i<10:
			cgpa_less_10 += 1

		if i>=8 and i<9:
			cgpa_less_9 += 1

		if i>=7 and i<8:
			cgpa_less_8 += 1

		if i>=6 and i<7:
			cgpa_less_7 += 1

		if i>=5 and i<6:
			cgpa_less_6 += 1

		if i>=4 and i<5:
			cgpa_less_5 += 1

		if i>=3 and i<4:
			cgpa_less_4 += 1

		if i>=2 and i<3:
			cgpa_less_3 += 1

		if i>=1 and i<2:
			cgpa_less_2 += 1

		if i>=0 and i<1:
			cgpa_less_1 += 1


	height = (cgpa_eq_10,cgpa_less_10,cgpa_less_9,cgpa_less_8,cgpa_less_7,cgpa_less_6,cgpa_less_5,cgpa_less_4,cgpa_less_3,cgpa_less_2,cgpa_less_1)

	return height

def allCgpa():
	Cgpa_All=[]
	Cgpa_All=list(Cgpa_Pass)+Cgpa_Fail
	Sum_Of_All_Cgpa = sum(Cgpa_All)
	average_of_all_cgpa = round(Sum_Of_All_Cgpa / len(Cgpa_All),2)

	return Cgpa_All, average_of_all_cgpa


def averageGrouper():
	
	sum_top_10=0
	sum_above_average=0
	sum_below_average=0
	sum_fail=0

	Cgpa_All_Sorted = np.sort(Cgpa_All)
	Cgpa_All_Sorted=Cgpa_All_Sorted[::-1]

	for i in range(10):
		sum_top_10 += Cgpa_All_Sorted[i]

	for i in Cgpa_All_Sorted:

		if i < sum_top_10/10 and i > average_of_all_cgpa:
			sum_above_average += i

		if i < average_of_all_cgpa and i >3 :
			sum_below_average += i

		if i<3:
			sum_fail += i


	fraction_top_10 = (sum_top_10 / (sum_top_10 + sum_above_average + sum_below_average+sum_fail) ) * 100 

	fraction_above_average = (sum_above_average / (sum_top_10 + sum_above_average + sum_below_average + sum_fail) ) * 100

	fraction_below_average = (sum_below_average / (sum_top_10 + sum_above_average + sum_below_average + sum_fail) ) * 100

	fraction_fail=(sum_fail / (sum_top_10 + sum_above_average + sum_below_average + sum_fail) ) * 100

	return (fraction_top_10, fraction_above_average, fraction_below_average, fraction_fail)


###################################################################################################################################################################################

""" The graph functions   """

def comparrsionGraph():

	plt.xlabel(" Roll Number of Student ")
	plt.ylabel(" CGPA of each student  ")
	plt.title(" Data Analysis ")
	plt.ylim(0, 11)

	plt.plot(RollNo_Pass_x, Cgpa_Pass, color="orange", label='Student pass', linestyle='dashed', marker='o', markerfacecolor='red', markersize=12 )

	plt.plot(RollNo_Fail_x, Cgpa_Fail, color='black', label='student fail', linestyle='dashed', marker='o', markerfacecolor='grey', markersize=10 )

	plt.plot(RollNo_Entered_x, Cgpa_Entered, color='purple', label = ( f'Name: {Name_Entered}, Roll number: {RollNo_Entered}, CGPA: {Cgpa_Entered}'), marker='o', markerfacecolor='green', markersize=14)

	plt.legend()
	plt.show()



def bargraph():
	
	height= [average_of_all_cgpa,Cgpa_Entered]
	left=[2,6]
	tick_label=[f' Average of all students: {average_of_all_cgpa}',f'Name:{Name_Entered} \n Roll Number: {RollNo_Entered_x} \n CGPA: {Cgpa_Entered}']
	plt.xlabel("    STUDENTS DETAILS    ")
	plt.ylabel(" CGPA ")
	plt.title(" Data Analysis ")
	plt.ylim(0, 11)
	plt.xlim(0, 9)
	plt.bar(left, height, tick_label=tick_label, width=0.4, color=['orange','green'] )
	plt.show()



def frequencyDistributionGraph():

	left=[1,2,3,4,5,6,7,8,9,10,11]
	tick_label=['10','9-10','8-9','7-8','6-7','5-6','4-5','3-4','2-3','1-2','1-0']

	plt.xlabel('CGPA Range')
	plt.ylabel('Number of Students in Given CGPA Range')
	plt.title('Frequency of CGPA')
	plt.bar(left,height,tick_label=tick_label,width=0.6,color=['red','purple'])
	plt.show()



def pieChart():

	activities=['Top-10', 'Below -average', 'Above-average', 'Fail' ]
	slices=[fraction_top_10, fraction_above_average, fraction_below_average, fraction_fail]
	colors=('r','y','g', 'b')
	explode=(0.3,0,0,0)

	plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=False, explode=explode, radius=1.3, autopct='%1.1f%%', pctdistance=0.6)
	plt.legend()
	plt.show()

###################################################################################################################################################################################

if __name__ == "__main__": 


	RollNo_Entered = input("Enter your Rollno : ")

	RollNo_Entered_x, Cgpa_Entered, Name_Entered = studentDataCollector(RollNo_Entered)

	RollNo_Pass, Cgpa_Pass, RollNo_Pass_x = rollnoCgpaPassCollector()

	RollNo_Fail, Cgpa_Fail, RollNo_Fail_x = rollnoCgpaFailCollector()

	Cgpa_All, average_of_all_cgpa = allCgpa()

	height = cgpaDistributor()

	fraction_top_10, fraction_above_average, fraction_below_average, fraction_fail = averageGrouper()



	comparrsionGraph()
	bargraph()
	frequencyDistributionGraph()
	pieChart()
