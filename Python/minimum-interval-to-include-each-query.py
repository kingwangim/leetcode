class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]: 
        # 数组大小
        m,n=len(intervals),len(queries)
        # 返回值
        res=[-1]*n
        # 堆
        heap=[]
        # 将queries中数字按照从小到大的顺序排列，并记录每个值对应的下标
        qr=sorted([(i,q) for i,q in enumerate(queries)],key=lambda x:x[1])
        # 将区间intervals排序
        intervals.sort()
        index=0
        for i,q in qr:
            # 如果intervals中区间的左端点小于等于查询值q，则将区间的长度和右端点加入堆中
            while index<m and intervals[index][0]<=q:
                l,r=intervals[index]
                heapq.heappush(heap,[r-l+1,r])
                index+=1
            # 如果堆顶元素存储的右端点小于查询值，则对顶元素出堆
            while heap and heap[0][1]<q:
                heapq.heappop(heap)
            # 如果堆不为空，堆顶元素即为所求
            if heap:
                res[i]=heap[0][0]
        return res