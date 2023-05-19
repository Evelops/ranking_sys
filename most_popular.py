#  QuuickSort Alogrithm 

# def quick_sort(data:int):
#     n = len(data)
#     rank = [0] * n
    
#     print(f'rank? => {rank}')
    
#     for i in range(n):
#         rank[i] = 1 
#         for j in range(n):
#             if data[j] > data[i]:
#                 rank[i] += 1
                
#     return rank

# print(quick_sort([2,3,4,1,5]))

"""
HackerNews with Ranking Algorithm 
hacker뉴스의 랭킹 알고리듬 조회수를 기반으로 하며, 날짜별 가중치를 주어 계산
page_views(int): 조회수  
item_hour_age(date): 현재시간 - 문서 업로드 날짜 
gravity(int): 중력상수(가중치)
"""
def rank_to_docs(page_views, item_hour_age, gravity=1.8):
    return (page_views - 1 ) / pow((item_hour_age+2),gravity)



