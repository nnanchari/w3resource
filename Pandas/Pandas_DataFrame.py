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



        
        
        
        
        
        
        

































































