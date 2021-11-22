#   Find a pair with the given sum in an array
#   Given an unsorted integer array, find a pair with the given sum in it

from random import sample   #   bonus points, let's shuffle the lists each time
                            #   but only for the standard process call

##########################
### processing methods ###

#   standard process method, something of a brute-force approach
#   return the first pair we find, in accordance with the directive
def process(nums, target):
    for x in nums:
        cnt = nums.count(target-x)
        hlf = True if target/x==2 else False
        if ( not(cnt==1 and hlf) and cnt>0 ):
            return [x, target-x]

####################
### main program ###

nums1 = [8,7,2,5,3,1]
nums2 = [5,2,6,8,1,9]
target1 = 10
target2 = 12

print("Find {0} in {1}:\n".format(target1, nums1))
print("Pairs: {0}".format(process(sample(nums1, k=len(nums1)), target1)))

print("Find {0} in {1}:\n".format(target2, nums2))
print("Pairs: {0}".format(process(sample(nums2, k=len(nums1)), target2)))