import numpy as np 
from datetime import datetime, timedelta 

epoch = datetime(1970, 1, 1) 

def epoch_seconds(date): 
    ## convert datetime to seconds 
    td = date - epoch 
    return td.days*86400 + td.seconds + (float(td.microseconds)/100000) 
    
def score(ups, downs): 
    return ups - downs 
    
def reddit_score(ups, downs, date): 
    """The hot formula. Should match the equivalent function in postgres.""" 
    s = score(ups, downs) 
    order = np.log10(max(abs(s), 1)) 
    
    if s > 0: sign = 1 
    elif s < 0: sign = -1 
    else: sign = 0 
    
    seconds = epoch_seconds(date) - 1134028003 
    
    return round(order + sign * seconds / 45000, 7) 
    
print(reddit_score(1000, 200, datetime(2021, 8, 10))) 
print(reddit_score(1000, 200, datetime(2020, 8, 10)))