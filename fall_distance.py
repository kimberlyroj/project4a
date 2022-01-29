#Author: Kimberly Rojas
#GitHub username: kimberlyroj
#Date: 1/28/2021
#Description: Code that will determine the distance an object falls due to gravity in a specific time period:
def fall_distance(time):#function
  gravity=9.8
  distance=(1/2)*gravity*time**2 #determine the distance
  return round(distance,3) #return distance
time=float(input())
dist=fall_distance(time)
print(dist)
