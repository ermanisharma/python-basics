# iterable, immutable ( can modify after creation)
# unique
# unordered
# unchangeable*
# unindexed
# no duplicate memebers allowed

# for learning purpose
employeeIdSet = {1414100,1414101, 1414102, 1414103, 1414104}

print('Length of Set : ',len(employeeIdSet))

for id in employeeIdSet :
    print('EmployeeId : ', id )

# in realtime application - set is created as below
employeeId_Set2 = set()

#employeeIdSet.remove(141000) #gives error, if item does not exists
employeeIdSet.discard(1414100)
del employeeIdSet

print('Length of Set : ',len(employeeIdSet))