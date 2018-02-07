# I have a^2 + b^2 = c^2 and a + b + c = 1000
# this means a^2 + b^2 = (1000 - a - b)^2 = 1000^2 + a^2 + 2ab + b^2 - 2000a - 2000b
# so a solution will have 500 + ab/1000 - a - b = 0.
# Furthermore, to be a valid triangle we need a + b > c. Squaring we have
# (a+b)^2 > c^2 = (1000 - (a+b))^2 = 1000^2 - 2000(a+b) + (a+b)^2
# --> 2000(a+b) > 1000^2 --> a + b > 500. So we only need to search over (a,b) : a+b > 500.
# This means that given a value of a we can start b at 500-a. 
# Also, what's the biggest that a can be? b > a so if a=500 then b > 500 which violates our perimeter requirement.
# so I can search over 1 <= a <= 499 and max(a, 500 - a) <= b <= 999


for(a in 1:499) {
  for(b in max(c(500-a, a)):999) {
    if(500 + a * b / 1000 - a - b == 0) {
      print(a * b * (1000 - a - b))
      break
    }
  }
}







