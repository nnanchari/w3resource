#1.Write a Pandas program to get the powers of an array values element-wise. 
Note: First array elements raised to powers from second array
Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}

import pandas as pd
data={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
print(pd.DataFrame(data))


#2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data)


#3. Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data.info())


#4. Write a Pandas program to get the first 3 rows of a given DataFrame. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data.iloc[:3])


#5. Write a Pandas program to select the 'name' and 'score' columns from the following DataFrame. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data.iloc[:,:2])


#6. Write a Pandas program to select the specified columns and rows from a given data frame. 
Sample Python dictionary data and list labels:
Select 'name' and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data.iloc[[1,3,5,6],:2])


#7. Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data[data.attempts>2])


#8. Write a Pandas program to count the number of rows and columns of a DataFrame. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(len(data.axes[0]))
print(len(data.axes[1]))


#9. Write a Pandas program to select the rows where the score is missing, i.e. is NaN. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data[data.score.isnull()])


#10. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive). 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
 labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data[data.score.between(15,20)])


#11. Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 15. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data[(data.attempts <2) & (data.score>15)]


#12. Write a Pandas program to change the score in row 'd' to 11.5. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
data.iloc[3,2]=11.5
print(data)


#13. Write a Pandas program to calculate the sum of the examination attempts by the students. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data.attempts.sum())

#14. Write a Pandas program to calculate the mean score for each different student in DataFrame. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(data.score.mean())


#15. Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame. Go to the editor
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Values for each column will be:
name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
data.loc['k']=['Suresh', 15.5,1,'yes']
print(data)
data=data.drop('k')
print(data)


#16. Write a Pandas program to sort the DataFrame first by 'name' in descending order, then by 'score' in ascending order. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Values for each column will be:
name : "Suresh", score: 15.5, attempts: 1, qualify: "yes", label: "k"

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
data_new=data.sort_values(by=['name','score'],ascending=[1,0])
print(data_new)


#17. Write a Pandas program to replace the 'qualify' column contains the values 'yes' and 'no' with True and False. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
data.qualify=data.qualify.map({'yes':True, 'no':False})
print(data)


#18. Write a Pandas program to change the name 'James' to 'Suresh' in name column of the DataFrame. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
data.iloc[3,0]='Suresh'
print(data)


#19. Write a Pandas program to delete the 'attempts' column from the DataFrame. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
new_data=data.drop(columns=['attempts'])
print(new_data)


#20. Write a Pandas program to insert a new column in existing DataFrame.
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
color = ['Red','Blue','Orange','Red','White','White','Blue','Green','Green','Red']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
data['color']=color
print(data)


#21. Write a Pandas program to iterate over rows in a DataFrame.
Sample Python dictionary data and list labels:
exam_data = [{'name':'Anastasia', 'score':12.5}, {'name':'Dima','score':9}, {'name':'Katherine','score':16.5}]

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)

for index,row in data.iterrows():
	print(row['name'],row['score'])
	
	
#22. Write a Pandas program to get list from DataFrame column headers. 
Sample Python dictionary data and list labels:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

import pandas as pd
data=pd.DataFrame(exam_data,index=labels)
print(list(data.columns))



#23. Write a Pandas program to rename columns of a given DataFrame Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9

import pandas as pd
data={'col1':[0,1,2],'col2':[2,3,4],'col3':[4,5,6]}
data=pd.DataFrame(data)
print(data)
new_data=data.rename(columns={'col1':'column1','col2':'column2','col3':'column3'})
print(new_data)


#24. Write a Pandas program to select rows from a given DataFrame based on values in some columns. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
Rows for colum1 value == 4

import pandas as pd
data={'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
data=pd.DataFrame(data)
print(data)
print(data[data['col1']==4])


#25. Write a Pandas program to change the order of a DataFrame columns. Go to the editor
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1
After altering col1 and col3
col3 col2 col1
0 7 4 1
1 8 5 4
2 9 6 3
3 0 7 4
4 1 8 5


data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
data=pd.DataFrame(data)
print(data)
print(data.iloc[:,[2,1,0]])


#26. Write a Pandas program to add one row in an existing DataFrame. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1


data=pd.DataFrame(data)
data.loc[5]=[10,11,12]
print(data)

#27. Write a Pandas program to write a DataFrame to CSV file using tab separator. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1

data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
data=pd.DataFrame(data)
print(data)
data.to_csv('C:/Users/ggvnanc/Desktop/AAA/Python/DataFrame/data_file.csv',sep='\t',index=False)
new_data=pd.read_csv('C:/Users/ggvnanc/Desktop/AAA/Python/DataFrame/data_file.csv')
print(new_data)


#28. Write a Pandas program to count city wise number of people from a given of data set (city, name of the person). 
Sample data:
city Number of people
0 California 4
1 Georgia 2
2 Los Angeles 4

data = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})

data=pd.DataFrame(data)
new_data=data.groupby(['city']).size().reset_index(name='number of people')
print(new_data)


#29. Write a Pandas program to delete DataFrame row(s) based on given column value. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1

data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
data=pd.DataFrame(data)
print(data.drop([1]))


#31. Write a Pandas program to select a row of series/dataframe by given integer index. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1

data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
data=pd.DataFrame(data)
print(data.iloc[2,:])


#32. Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe. 
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0


data=pd.DataFrame(data)
print(data.fillna(0))


#33. Write a Pandas program to convert index in a column of the given dataframe.
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
data=pd.DataFrame(data)
data.reset_index(level=0,inplace=True)
#Hiding index
print(data.to_string(index=False))      

        
#34. Write a Pandas program to set a given value for particular cell in  DataFrame using index value. 
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Set a given value for particular cell in the DataFrame

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}


data=pd.DataFrame(data)
data.set_value(0,'score',15)


#35. Write a Pandas program to count the NaN values in one or more columns in DataFrame. 
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0
Number of NaN values in one or more columns:
2

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
data=pd.DataFrame(data)
print(data.isna().values.sum())


#36. Write a Pandas program to drop a list of rows from a specified DataFrame. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 4 5 8
2 3 6 9
3 4 7 0
4 5 8 1

data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
data=pd.DataFrame(data)
data=data.drop([2,4])
print(data)


#37. Write a Pandas program to reset index in a given DataFrame.
Sample data:
Original DataFrame
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
data=pd.DataFrame(data)
data=data.drop([0,1])
print(data)
print(data.reset_index())


#39. Write a Pandas program to combining two series into a DataFrame. Go to the editor
Sample data:
Data Series:
0 100
1 200
2 python
3 300.12
4 400
dtype: object
0 10
1 20
2 php
3 30.12
4 40

import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])

data=pd.concat([s1,s2],axis=1)
print(data)


#40. Write a Pandas program to shuffle a given DataFrame rows. 
Sample data:
Original DataFrame:
attempts name qualify score
0 1 Anastasia yes 12.5
1 3 Dima no 9.0
2 2 Katherine yes 16.5
3 3 James no NaN
4 2 Emily no 9.0
5 3 Michael yes 20.0
6 1 Matthew yes 14.5
7 1 Laura no NaN
8 2 Kevin no 8.0
9 1 Jonas yes 19.0


data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
df = pd.DataFrame(data)
print(data)


#41. Write a Pandas program to convert DataFrame column type from string to datetime.
Go to the editor
Sample data:
String Date:
0 3/11/2000
1 3/12/2000
2 3/13/2000


data = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'])
print(data)
new_data=pd.to_datetime(data)
print(new_data)


#42. Write a Pandas program to rename a specific column name in a given DataFrame. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9


data = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}

data=pd.DataFrame(data)
print(data)
new_data=data.rename(columns={'col2':'column2'})
print(new_data)


#43. Write a Pandas program to get a list of a specified column of a DataFrame. 
Sample data:
Powered by
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 9

data = {'col1': [1,2,3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
print(data)
print(data.col1.to_list())


#45. Write a Pandas program to find the row for where the value of a given column is maximum. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11

data{'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

data=pd.DataFrame(data)
print(data['col1'].idxmax())
print(data['col2'].idxmax())
print(data['col3'].idxmax())


#46. Write a Pandas program to check whether a given column is present in a DataFrame or not. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Col4 is not present in DataFrame.
Col1 is present in DataFrame.

data{'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

data=pd.DataFrame(data)

if 'col1' in data.columns:
     print('yes')
else:
     print('no')
if 'col4' in data.columns:
     print('yes')
else:
     print('no')
	

#47. Write a Pandas program to get the specified row value of a given DataFrame. 
Sample data:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11

data{'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}

data=pd.DataFrame(data)
print(data[0])
print(data[3])


#48. Write a Pandas program to get the datatypes of columns of a DataFrame. 

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
data= pd.DataFrame(data)
print(data.dtypes)


#49. Write a Pandas program to append data to an empty DataFrame

data=pd.DataFrame({'col1':range(3),'col2':range(3)})
print(data)
new_data = data.append(pd.DataFrame({'col1':range(3),'col2':range(3)}))


#50. Write a Pandas program to sort a given DataFrame by two or more columns

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

import pandas as pd
import numpy as np

data= pd.DataFrame(data)
new_data=data.sort_values(by=['attempts','name'],ascending=[1,1])
print(new_data)


#51. Write a Pandas program to convert the datatype of a given column (floats to ints)

data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9.1, 16.5, 12.77, 9.21, 20.22, 14.5, 11.34, 8.8, 19.13],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
print(data.dtypes)
data.score=data.score.astype(int)
print(data.dtypes)


#53. Write a Pandas program to insert a given column at a specific column index in a DataFrame. 
Sample data:
Original DataFrame
col2 col3
0 4 7
1 5 8
2 6 12
3 9 1
4 5 11

data = pd.DataFrame({'col2': [4,5,6,9,5], 'col3': [7, 8,12,1,11]})
newcol= [1, 2, 3, 4, 7]
data.insert(loc=0,column='col1',value=newcol)


#54. Write a Pandas program to convert a given list of lists into a Dataframe. 
Sample data:
Original list of lists:
[[2, 4], [1, 3]]


list=[['col1','col2'], [2, 4], [1, 3]]
data=pd.DataFrame(list,columns=header)
print(data)


#55. Write a Pandas program to group by the first column and get second column as lists in rows. 
Sample data:
Original DataFrame
col1 col2
0 C1 1
1 C1 2
2 C2 3
3 C2 3
4 C2 4
5 C3 6
6 C2 5


data = pd.DataFrame({'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]})
print(data)
data=data.groupby('col1')['col2'].apply(list)
print(data)


#56. Write a Pandas program to get column index from column name of a given DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Index of 'col2'
1

data= {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
data = pd.DataFrame(data)
print(data.get_loc('col2'))


#57. Write a Pandas program to count number of columns of a DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
Number of columns:
3

data= {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
data = pd.DataFrame(data)
print(length(data.columns))


#58. Write a Pandas program to select all columns, except one given column in a DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 8
2 3 6 12
3 4 9 1
4 7 5 11
All columns except 'col3':

data= {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
data = pd.DataFrame(data)
print(data[['col2','col3']])


#59. Write a Pandas program to get first n records of a DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
First 3 rows of the said DataFrame':
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8

data= {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
data = pd.DataFrame(data)
print(data.head(3))


60. Write a Pandas program to get last n records of a DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
Last 3 rows of the said DataFrame':
col1 col2 col3
3 4 9 12
4 7 5 1
5 11 0 11

data= {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
data = pd.DataFrame(data)
print(data.tail(3))


#61. Write a Pandas program to get topmost n records within each group of a DataFrame. Go to the editor
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11

data= {{'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
data = pd.DataFrame(data)
data1=data.nlargest(3,'col1')
print(data1)
data2=data.nlargest(3,'col2')
print(data2)
data3=data.nlargest(3,'col3')
print(data3)


#62. Write a Pandas program to remove first n rows of a given DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
After removing first 3 rows of the said DataFrame:
col1 col2 col3
3 4 9 12
4 7 5 1
5 11 0 11

data= {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
data = pd.DataFrame(data)
print(data.iloc[3:])


#63. Write a Pandas program to remove last n rows of a given DataFrame. 
Sample Output:
Original DataFrame
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8
3 4 9 12
4 7 5 1
5 11 0 11
After removing last 3 rows of the said DataFrame:
col1 col2 col3
0 1 4 7
1 2 5 5
2 3 6 8

data={'col1': [1, 2, 3, 4, 7, 11], 'col2': [4, 5, 6, 9, 5, 0], 'col3': [7, 5, 8, 12, 1,11]}
data = pd.DataFrame(data)
print(data.iloc[:3])
  
        
        
        
        

































































