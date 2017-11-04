#!/usr/bin/python
import sys
import re
import os

########################################################
def select(columns,params,tablename):
	# print "herllo"
	table=[]
	count=0
	for i in params:
		table.append([i])

#fileopen
	data=[]
	with open(tablename+".csv", "r+") as fp1:
		dummylines = fp1.readlines()

	for x in dummylines:
		data.append(x.rstrip("\r\n"))

	stored=[]
	for x in data:
		stored=x.split(",")
		for y in range(0,len(params)):
			inofstart=columns.index(params[y])
			table[y].append(stored[inofstart])

##print output
	s=""
	for i in range(0,len(table)):
		s+=tablename+"."+table[i][0]+","

	s=s[:len(s)-1]
	if(len(table[0])>1):
		print s
	tuples=""
	for i in range(1,len(table[0])):
		for j in range(0,len(table)):
			tuples+=table[j][i]+","
		tuples=tuples[:len(tuples)-1]
		print tuples
		tuples=""

##################################################################
def selectall(columns,params,tables):

	table=[]
	count=0
	for i in params:
		table.append([i])

	f3 = open("result.csv", "wt")
#fileopen
	data=[]
	with open(tables[0]+".csv", "r+") as fp1:
		dummylines = fp1.readlines()
	with open(tables[0]+".csv", "r+") as fp1:
		dummylines2 = fp1.readlines()
	s=""
	for i in dummylines:
		for j in dummylines2:
			s+=(i.rstrip("\r\n"))+","+(j.rstrip("\r\n"))
			f3.write(s)
			f3.write('\n')
			s=""
	f3.close()

	with open("result.csv", "r+") as fp1:
		dummylines = fp1.readlines()


	for x in dummylines:
		data.append(x.rstrip("\r\n"))


	stored=[]


	for x in data:
		stored=x.split(",")
		for y in range(0,len(params)):
			inofstart=columns.index(params[y])
			table[y].append(stored[inofstart])

##print output
	s=""
	for i in range(0,len(table)):
		s+=table[i][0]+","

	s=s[:len(s)-1]
	if(len(table[0])>1):
		print s
	tuples=""
	for i in range(1,len(table[0])):
		for j in range(0,len(table)):
			tuples+=table[j][i]+","
		tuples=tuples[:len(tuples)-1]
		print tuples
		tuples=""

##############################################################	

def selectwhere(columns,params,where,tablename):

	table=[]
	count=0
	for i in params:
		table.append([i])

#fileopen
	data=[]
	with open(tablename+".csv", "r+") as fp1:
		dummylines = fp1.readlines()

	for x in dummylines:
		data.append(x.rstrip("\r\n"))

	andflag=0
	orflag=0

	andflags=0
	orflags=0
## check for and,or
	if('OR' in where or 'or' in where):
		orflag=1
	if('AND' in where or 'and' in where):
		andflag=1



#################### only OR is present
	var1=[]
	var2=[]
	if(orflag==1 and andflag==0):
	#parse and store in dictionary

		if('OR' in where):
			cond=where.split('OR')
		elif('or' in where):
			cond=where.split('or')


		for x in cond:
			op=x.split('=')
			ind=columns.index(op[0].strip())
		# index in ind and value in op[1]
			var1.append(ind)
			var2.append(int(op[1]))
		flag=0
		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				for i in range (0,len(var1)):
					if(int(stored[var1[i]])==int(var2[i])):
						flag=1
				if (flag==1):
					table[y].append(stored[inofstart])
				flag=0


	if(orflag==0 and andflag==1):
		
		if('AND' in where):
			cond=where.split('AND')
		elif('and' in where):
			cond=where.split('and')

		for x in cond:
			op=x.split('=')
			ind=columns.index(op[0].strip())
		# index in ind and value in op[1]
			var1.append(ind)
			var2.append(int(op[1]))
		flag=1
		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				for i in range (0,len(var1)):
					if(int(stored[var1[i]])!=int(var2[i])):
						flag=0
				if (flag==1):
					table[y].append(stored[inofstart])
				flag=1

	if(orflag==0 and andflag==0):
		x=where
	
		op=x.split('=')
		ind=columns.index(op[0].strip())
		# index in ind and value in op[1]
		var1.append(ind)
		var2.append(int(op[1]))
		flag=0
		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				for i in range (0,len(var1)):
					if(int(stored[var1[i]])==int(var2[i])):
						flag=1
				if (flag==1):
					table[y].append(stored[inofstart])
				flag=0



#######################################################print output
	s=""
	for i in range(0,len(table)):
		s+=tablename+"."+table[i][0]+","

	s=s[:len(s)-1]
	print s
	tuples=""
	for i in range(1,len(table[0])):
		for j in range(0,len(table)):
			tuples+=table[j][i]+","
		tuples=tuples[:len(tuples)-1]
		print tuples
		tuples=""

###########################################################################################



###########################################################################################
def selectallwhere(columns,params,tables,where):

	table=[]
	count=0
	for i in params:
		table.append([i])

	f3 = open("result.csv", "wt")
#fileopen
	data=[]
	with open(tables[0]+".csv", "r+") as fp1:
		dummylines = fp1.readlines()
	with open(tables[0]+".csv", "r+") as fp1:
		dummylines2 = fp1.readlines()
	s=""
	for i in dummylines:
		for j in dummylines2:
			s+=(i.rstrip("\r\n"))+","+(j.rstrip("\r\n"))
			f3.write(s)
			f3.write('\n')
			s=""
	f3.close()

#fileopen
	data=[]
	with open("result.csv", "r+") as fp1:
		dummylines = fp1.readlines()

	for x in dummylines:
		data.append(x.rstrip("\r\n"))

	andflag=0
	orflag=0
## check for and,or
	if('OR' in where or 'or' in where):
		orflag=1
	if('AND' in where or 'and' in where):
		andflag=1



#################### only OR is present
	var1=[]
	var2=[]
	if(orflag==1 and andflag==0):
	#parse and store in dictionary
	
		if('OR' in where):
			cond=where.split('OR')
		elif('or' in where):
			cond=where.split('or')
		for x in cond:
			op=x.split('=')
			ind=columns.index(op[0].strip())
		# index in ind and value in op[1]
			var1.append(ind)
			var2.append(int(op[1]))
		flag=0
		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				for i in range (0,len(var1)):
					if(int(stored[var1[i]])==int(var2[i])):
						flag=1
				if (flag==1):
					table[y].append(stored[inofstart])
				flag=0


	if(orflag==0 and andflag==1):
		if('AND' in where):
			cond=where.split('AND')
		elif('and' in where):
			cond=where.split('and')
		for x in cond:
			op=x.split('=')
			ind=columns.index(op[0].strip())
		# index in ind and value in op[1]
			var1.append(ind)
			var2.append(int(op[1]))
		flag=1
		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				for i in range (0,len(var1)):
					if(int(stored[var1[i]])!=int(var2[i])):
						flag=0
				if (flag==1):
					table[y].append(stored[inofstart])
				flag=1

	if(orflag==0 and andflag==0):
		x=where
	
		op=x.split('=')
		ind=columns.index(op[0].strip())
		# index in ind and value in op[1]
		var1.append(ind)
		var2.append(int(op[1]))
		flag=0
		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				for i in range (0,len(var1)):
					if(int(stored[var1[i]])==int(var2[i])):
						flag=1
				if (flag==1):
					table[y].append(stored[inofstart])
				flag=0



#######################################################print output
	s=""
	for i in range(0,len(table)):
		s+=table[i][0]+","

	s=s[:len(s)-1]
	print s
	tuples=""
	for i in range(1,len(table[0])):
		for j in range(0,len(table)):
			tuples+=table[j][i]+","
		tuples=tuples[:len(tuples)-1]
		print tuples
		tuples=""
############################################################################################		
def salpha(columns,params,tables,where):
	table=[]
	count=0
	for i in params:
		table.append([i])

	f3 = open("result.csv", "wt")
#fileopen
	data=[]
	with open(tables[0]+".csv", "r+") as fp1:
		dummylines = fp1.readlines()
	with open(tables[1]+".csv", "r+") as fp1:
		dummylines2 = fp1.readlines()
	s=""
	for i in dummylines:
		for j in dummylines2:
			s+=(i.rstrip("\r\n"))+","+(j.rstrip("\r\n"))
			f3.write(s)
			f3.write('\n')
			s=""
	f3.close()

#fileopen
	data=[]
	with open("result.csv", "r+") as fp1:
		dummylines = fp1.readlines()

	for x in dummylines:
		data.append(x.rstrip("\r\n"))

	x=where
	var1=[]
	var2=[]
	op=x.split('=')
	ind=columns.index(op[0].strip())
	# index in ind and value in op[1]
	var1.append(ind)
	var2.append(columns.index(op[1].strip()))
	flag=0
	stored=[]
	for x in data:
		stored=x.split(",")		
		if((stored[var1[0]])==stored[var2[0]]):			
			for y in range(0,len(params)):
				inofstart=columns.index(params[y])
				table[y].append(stored[inofstart])

#######################################################print output
	s=""
	for i in range(0,len(table)):
		s+=table[i][0]+","

	s=s[:len(s)-1]
	print s
	tuples=""
	for i in range(1,len(table[0])):
		for j in range(0,len(table)):
			tuples+=table[j][i]+","
		tuples=tuples[:len(tuples)-1]
		print tuples
		tuples=""

############################## for multiple tables
def multicol(columns,tablename,count):
	strip_lines=[]
	with open("metadata.txt", "r+") as fp1:
		dummy = fp1.readlines()

	for x in dummy:
		strip_lines.append(x.rstrip("\r\n"))


	indexofstart=strip_lines.index(tablename)+1

	for i in range(indexofstart,len(strip_lines)):
		if strip_lines[i]=='<end_table>':
			break
		else:
			colname=tablename+"."+strip_lines[i]
			columns.append(colname)

	if (len(columns)==0):
		print "No such table(s) found"
		sys.exit()






# get and parse the query - use sqlparse

sql=sys.argv[1]

selectflag=0
whereflag=0
joinflag=0
star=0

if('select' in sql):
	selectflag=1
if('where' in sql):
	whereflag=1
if('.' in sql):
	joinflag=1
if('*' in sql):
	star=1


### change v

querynum = (sys.argv[1]).split(" ")



i = querynum.count('')
while i!=0:
	querynum.remove('')
	i = i - 1

countd=0
for word in querynum:
	if word.lower() == 'select' or word.lower() == 'from' or word.lower() == 'where':
		z = word.lower()
		querynum[querynum.index(word)] = z
	if word.lower() == 'distinct':
		countd+=1

if(countd>1):
	print "Error in sql query"
	sys.exit()

select_index = querynum.index('select') + 1
from_index = querynum.index('from')

###############################################################
col_list = []
#cols is the list of attributes between 'select and from'
while select_index != from_index:
	col_list.extend(querynum[select_index].split(","))			
	select_index += 1

i = col_list.count('')
while i!=0:
	col_list.remove('')
	i = i - 1

attr = col_list[:]


##############################################################

#tables list

t = []
tables = []

if whereflag == 0:
	t = querynum[querynum.index('from')+1 : ]
	for i in t:
		tables.extend(i.split(","))

elif whereflag == 1:
	t = querynum[querynum.index('from')+1 : querynum.index('where')]
	for i in t:
		tables.extend(i.split(","))

i = tables.count('')
while i!=0:
	tables.remove('')
	i = i - 1

#############get the column names required of a table from the metadata.txt#####################
columns=[]
tablename=tables[0]
strip_lines=[]
with open("metadata.txt", "r+") as fp1:
		dummy = fp1.readlines()

for x in dummy:
	strip_lines.append(x.rstrip("\r\n"))

try:
	indexofstart=strip_lines.index(tablename)+1
except:
	print "Error in sql query"
	sys.exit()


for i in range(indexofstart,len(strip_lines)):
	if strip_lines[i]=='<end_table>':
		break
	else:
		columns.append(strip_lines[i])

if (len(columns)==0):
		print len(columns)
		print "No such table(s) found"
		sys.exit()

#################################################################################################
# -->>> start calling the functions

# print col_list
 # print attr
subs=col_list[0]

if(subs[3:4]=='('):
	col_list.remove(col_list[0])
	col_list.append(subs[:3])
	col_list.append(subs[4:5])

# print col_list

# print col_list

funcflag=0

if('max' in col_list or 'min' in col_list or 'distinct' in col_list or 'sum' in col_list or 'avg' in col_list):
	funcflag=1

if('MAX' in col_list or 'MIN' in col_list or 'DISTINCT' in col_list or 'SUM' in col_list or 'AVG' in col_list):
	funcflag=1



crossp=0
if(len(tables)>1):
	crossp=1


if(len(col_list)==1 and col_list[0]=='*' and crossp==0): 
	col_list=columns


if(selectflag==1 and whereflag==0 and funcflag==1):

	if(col_list[0].upper()=='MAX'):
		
		try:
			index=columns.index(col_list[1])
		except:
			print "Error in sql query"
			sys.exit()

		tablename=tables[0]
		table=[]

		data=[]
		with open(tables[0]+".csv", "r+") as fp1:
			dummylines = fp1.readlines()

		for x in dummylines:
			data.append(x.rstrip("\r\n"))

		stored=[]
		for x in data:
			stored=x.split(",")
			table.append(int(stored[index]))
##print output
		print max(table)

	if(col_list[0].upper()=='MIN'):
		
		try:
			index=columns.index(col_list[1])
		except:
			print "Error in sql query"
			sys.exit()
		tablename=tables[0]
		table=[]

		data=[]
		with open(tables[0]+".csv", "r+") as fp1:
			dummylines = fp1.readlines()

		for x in dummylines:
			data.append(x.rstrip("\r\n"))

		stored=[]
		for x in data:
			stored=x.split(",")
			table.append(int(stored[index]))
##print output
		print min(table)

	if(col_list[0].upper()=='SUM'):
		add=0
		try:
			index=columns.index(col_list[1])
		except:
			print "Error in sql query"
			sys.exit()
		tablename=tables[0]
		table=[]

		data=[]
		with open(tables[0]+".csv", "r+") as fp1:
			dummylines = fp1.readlines()

		for x in dummylines:
			data.append(x.rstrip("\r\n"))

		stored=[]
		for x in data:
			stored=x.split(",")
			add+=(int(stored[index]))
##print output
		print add

	if(col_list[0].upper()=='AVG'):
		add=0
		try:
			index=columns.index(col_list[1])
		except:
			print "Error in sql query"
			sys.exit()
		tablename=tables[0]
		table=[]

		data=[]
		with open(tables[0]+".csv", "r+") as fp1:
			dummylines = fp1.readlines()

		for x in dummylines:
			data.append(x.rstrip("\r\n"))

		stored=[]
		count=0
		for x in data:
			stored=x.split(",")
			add+=(int(stored[index]))
			count+=1
##print output
		print float(add/float(count))

	if(col_list[0].upper()=='DISTINCT'):
		try:
			index=columns.index(col_list[1])
		except:
			print "Error in sql query"
			sys.exit()
		params=col_list[1]
		tablename=tables[0]
		collist=columns
		num=len(collist)
		table=[]
		
		for i in params:
			table.append([i])

#fileopen
		data=[]
		with open(tables[0]+".csv", "r+") as fp1:
			dummylines = fp1.readlines()

		for x in dummylines:
			data.append(x.rstrip("\r\n"))

		stored=[]
		for x in data:
			stored=x.split(",")
			for y in range(0,len(table)):
				if(stored[y] not in table[y]):
					table[y].append(stored[index])

##print output
		s=""
		for i in range(0,len(table)):
			s+=tablename+"."+table[i][0]+","

		s=s[:len(s)-1]
		print s
		tuples=""
		for i in range(1,len(table[0])):
			for j in range(0,len(table)):
				tuples+=table[j][i]+","
			tuples=tuples[:len(tuples)-1]
			print tuples
			tuples=""


# print selectflag
# print whereflag
# print crossp 
# print funcflag

if(selectflag==1 and whereflag==0 and crossp==0 and funcflag==0):
	try:
		select(columns,col_list,tables[0])
	except:
		print "Error in sql query"
		sys.exit()

if(selectflag==1 and whereflag==1 and crossp==0 and funcflag==0):
	wc=sql.split('where')
	wherecond=wc[1]
	try:
		selectwhere(columns,col_list,wherecond,tables[0])
	except:
		print "Error in sql query"
		sys.exit()


if(selectflag==1 and whereflag==0 and crossp==1 and funcflag==0):
	#create the master column
	
	columns=[]
	i=1
	for c in tables:
		multicol(columns,c,i)
		i+=1
	if(len(col_list)==1 and col_list[0]=='*'):
		col_list=columns
	try:
		selectall(columns,col_list,tables)
	except:
		print "Error in sql query"
		sys.exit()

if(selectflag==1 and whereflag==1 and crossp==1 and funcflag==0):
	wc=sql.split('where')
	wherecond=wc[1]
	columns=[]
	i=1
	for c in tables:
		multicol(columns,c,i)
		i+=1
	if(len(col_list)==1 and col_list[0]=='*'):
		col_list=columns

	d=wherecond.split('=')
	st_d=""
	st_d=d[1]

	
	if('AND' in st_d or 'and' in st_d or 'OR' in st_d or 'or' in st_d or st_d.isdigit()):
		try:
			selectallwhere(columns,col_list,tables,wherecond)		
		except:
			print "Error in sql query"
			sys.exit()
	else:	
		try:
			salpha(columns,col_list,tables,wherecond)
		except:
			print "Error in sql query"
			sys.exit()
			










