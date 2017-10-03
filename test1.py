def bs(arr,s,e, tar):
	if s > e: return False
	m = (s+e) // 2
	if arr[m] == tar: return True
	if arr[m] > tar: return bs(arr,s,m-1,tar)
	else: return bs(arr,m+1,e,tar)

arr = [2,4,6,8,12,16,19,23,44,56]
print(bs(arr,0,len(arr)-1, 56))
