#Netflix.py

#----------------------
#netflix_read
#----------------------

"""
Reading customer id's and movie id's
"""

def netflix_read(r):
    s = r.readline()
    s = s.rstrip('\n')
    return s

#----------------------
#predict ratings
#----------------------

"""
Predicting the ratings of the movies for each customer
"""

def netflix_predict(movie, customer):
    import json
    customer_dict = json.load(open('mjh3664customer.txt', 'r')
    movie_dict = json.load(open('mjh3664movie.txt', 'r')
    cust_avg = json.load(open('savant-cacheUsers.txt', 'r'))

    if movie in movie_dict:
        return (movie_dict[movie][0]+ eval(cust_avg[customer]) / 2)
    else:
        return eval(cust_avg[customer])
        
                      
#----------------------
#netflix_return
#----------------------

"""
Adding everything back in: customer id and predicted rating
"""

def netflix_return(w, rate):
    w.write(str(rate ) + '\n')
    

#----------------------
#rmse function
#----------------------

"""
Root Mean Square Error function, testing accuracy of our predictions
"""

def rmse(a,p):
    import math
    import json
    cust_real = json.load(open('savant-cacheActual.txt', 'r'))
    r = []
    for item in a:
        r.append(cust_real[a])
    z = zip(r,p)
    sum = 0
    for x,y in z:
        sum += (x - y) ** 2
    return '%0.2f' % (math.sqrt(sum / len(a)))
    
#----------------------
#netflix_solve
#----------------------

def netflix_solve(r, w):
    real_data = []
    predicted_data = []
    while True:
        a = netflix_read(r)
        if not a:
            break
        if ':' in a:
            netflix_return(w,a)
            a.rstrip(':')
            movie = a
            continue
        else:
            customer = a
        real_data.append(movie + ' ' + customer)
        b = netflix_predict(movie, customer)
        netflix_return(w, b)
        predicted_data.append(b)
    netflix_return(w,rmse(real_data,predicted_data))
