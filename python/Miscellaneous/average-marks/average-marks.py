import math
class Solution:
    @staticmethod
    def calculate_average(name, M, S, E, H, C):
      #Write your code here
      total_sum = M + S + E + H + C
      avg = round(total_sum/5)
      
      print(name)
      print(avg)


Solution.calculate_average("A", 81, 81, 81, 33, 63)
