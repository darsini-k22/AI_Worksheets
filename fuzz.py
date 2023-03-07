import matplotlib.pyplot as plt
fuzzyset={
    'NL':[0,31,61],
    'NM':[31,61,95],
    'NS':[61,95,127],
    'ZE':[95,127,159],
    'PS':[127,159,191],
    'PM':[159,191,223],
    'PL':[191,223,255]
    }

def triangle(x,key):
    a=fuzzyset[key][0]
    b=fuzzyset[key][1]
    c=fuzzyset[key][2]
   
    return max(min((x-a)/(b-a),(c-x)/(c-b)),0)

def trapezoid(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif x > a and x <= b:
        return (x - a) / (b - a)
    elif x > b and x <= c:
        return 1
    else:
        return (d - x) / (d - c)

# Plot the membership functions
count=0
for key in fuzzyset:
    x = range(fuzzyset[key][0], fuzzyset[key][2]+1)
    y = []
    for i in x:
      if count==0:
        y.append(1)
        count+=1
      else:
        y.append(triangle(i, key))
        count+=1
      if count==len(fuzzyset):
        y.append(0)
      print(y)
    plt.plot(x, y, label=key)

# x=range(fuzzyset['PS'],fuzzyset['PM']+1)
# y=[]
# plt.plot(x,y)
    

# Add labels and legends
plt.xlabel('Speed (km/h)')
plt.ylabel('Membership Degree')
plt.legend()
plt.show()


def membership_degree(value):
    keys=[]
    for key in fuzzyset:
        temp=[]
        for j in range(fuzzyset[key][0],fuzzyset[key][2]):
            temp.append(j)
        if value in temp:
            keys.append(key)
    return keys


def rules(speed,acc):
    throttle_val={}
    for i in speed.keys():
        for j in acc.keys():
            if i=='NL' and j=='ZE':
                throttle_val['PL']=min(speed[i],acc[j])
            if i=='ZE' and j=='NL':
                throttle_val['PL']=min(speed[i],acc[j])
            if i=='NM' and j=='ZE':
                throttle_val['PM']=min(speed[i],acc[j])
            if i=='NS' and j=='PS':
                throttle_val['PS']=min(speed[i],acc[j])
            if i=='PS' and j=='NS':
                throttle_val['NS']=min(speed[i],acc[j])
            if i=='PL' and j=='ZE':
                throttle_val['NL']=min(speed[i],acc[j])
            if i=='ZE' and j=='NS':
                throttle_val['PS']=min(speed[i],acc[j])
            if i=='ZE' and j=='NM':
                throttle_val['PM']=min(speed[i],acc[j])
    return throttle_val


def defuzzification(throttle_val):
    num = 0
    den = 0
    for key in throttle_val:
        num += throttle_val[key] * ((fuzzyset[key][0] + fuzzyset[key][2]) / 2)
        den += throttle_val[key]
    return num / den if den != 0 else 0

def fuzzy_cruise_controller(speed_diff,acc):
    calc_speed={}
    calc_acc={}
    speed_keys=membership_degree(speed_diff)
    acc_keys=membership_degree(acc)
    calc_speed[speed_keys[0]]=triangle(speed_diff, speed_keys[0])
    calc_speed[speed_keys[1]]=triangle(speed_diff, speed_keys[1])
    calc_acc[acc_keys[0]]=triangle(acc, acc_keys[0])
    calc_acc[acc_keys[1]]=triangle(acc, acc_keys[1])
    throttle_val = rules(calc_speed, calc_acc)
    print(calc_speed)
    print(calc_acc)
    print('Trottle control is =', throttle_val)
    print('Defuzzified output =', defuzzification(throttle_val))

fuzzy_cruise_controller(100, 70)

