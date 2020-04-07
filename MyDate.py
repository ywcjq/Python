class MyDate:
  __d_of_m = ((0,31,28,31,30,31,30,31,31,30,31,30,31),(0,31,29,31,30,31,30,31,31,30,31,30,31))
  
  @classmethod
  def __check(cls,year,month,day):
    if year > 0 and 1 <= month <= 12 \
    and 1<= day <= cls.__d_of_m[cls.__isleap(year)][month]:
      return True
    else:
      return False
      
  @classmethod
  def __isleap(cls,year):
    if year % 400 == 0 \
    or year % 4 == 0 \
    and year % 100 != 0:
      return True
    else:
      return False
  
  @classmethod
  def fromID(cls, dateid):
    value = dateid - 1
    year = 1900
    month = 1
    day = 1
    while value > 0:
      if value > cls.__d_of_m[cls.__isleap(year)][month] - day:
        value = value - (cls.__d_of_m[cls.__isleap(year)][month] - day) - 1
        day = 1
        if month == 12:
          month = 1
          year += 1
        else:
          month += 1
      else:
        day += value
        value = 0
    return cls(year, month, day)
  
  @classmethod
  def fromstr(cls, string):
    for i in '.-/':
      if i in string:
        year, month, day = string.split(i)
    return cls(int(year), int(month), int(day))
  
  def __init__(self, year, month, day):
    if self.__check(year, month, day):
      self.__year = year
      self.__month = month
      self.__day = day
    self.leap = self.__isleap(self.year)
    self.__dateID = self.__calcID()
    
  def __calcID(self):
    leapyears = 0
    ID = 0
    for y in range(1900, self.year):
      if self.__isleap(y):
        leapyears += 1
    ID = 365 * (self.year - 1900) + leapyears
    
    for m in range(1,self.month):
      ID += self.__d_of_m[self.__isleap(self.year)][m]
      
    ID += self.day
    return ID
  
  def __str__(self):
    return f'{self.year}-{self.month}-{self.day}\t{self.__dateID}'
    
  def __repr__(self):
    return f'{self.year}-{self.month}-{self.day}:{self.leap}\t{self.__dateID}'
    
  def __add__(self, num):
    return self.fromID(self.__dateID + num)
    
  def  __radd__(self, num):
    return self + num

  
  def  __sub__(self, num):
    if isinstance(num, MyDate):
      return self.__dateID - num.__dateID
    else:
      return self.fromID(self.__dateID - num)
  
  
  def tomorrow(self):
    return self + 1

  def __int__(self):
    return self.__dateID
    
  def yesterday(self):
    return self - 1
  
  @property
  def year(self):
    return self.__year
  
  @property  
  def month(self):
    return self.__month
 
  @property 
  def day(self):
    return self.__day
  
d = MyDate(2001,12,1)
d1 = MyDate.fromID(12345)
d2 = d + 500
d3 = 600 + d
d4 = MyDate.fromstr('2011.01.01')
d5 = d4.fromstr('2000-02-09')
d6 = MyDate.fromstr('1998/07/08')
n = d3 - d2
m = d3 - 100
x = m.tomorrow()
z = x.yesterday()

print(d)
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(n)
print(m)
print(x)
print(m)
print(int(m))
print(z)
print(z.year,z.month,z.day)
print(z.fromstr('2001.1.1'))
print(z)