from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)

arguments = [
  Args(False, False),
  Args(False, True),
  Args(True, False),
  Args(True, True),
]

exo_sleep_in = ExerciseFunction(
  sleep_in,
  arguments
)

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back

arguments = [
  Args('kitten', 1),
  Args('kitten', 0),
  Args('kitten', 4),
  Args('Hi', 0),
  Args('Hi', 1),
  Args('code', 0),
  Args('code', 1),
  Args('code', 2),
  Args('code', 3),
  Args('chocolate', 8),
]

exo_missing_char = ExerciseFunction(
  missing_char,
  arguments
)

def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False
  ## The above can be shortened to:
  ##   return ((a_smile and b_smile) or (not a_smile and not b_smile))
  ## Or this very short version (think about how this is the same as the above)
  ##   return (a_smile == b_smile)

arguments = [
  Args(True, True),
  Args(False, False),
  Args(True, False),
  Args(False, True),
]

exo_monkey_trouble = ExerciseFunction(
  monkey_trouble,
  arguments
)

def front_back(str):
  if len(str) <= 1:
    return str
  
  mid = str[1:len(str)-1]  # can be written as str[1:-1]
  
  # last + mid + first
  return str[len(str)-1] + mid + str[0]

arguments = [
  Args('code'),
  Args('a'),
  Args('ab'),
  Args('abc'),
  Args(''),
  Args('Chocolate'),
  Args('aavJ'),
  Args('hello'),
]

exo_front_back = ExerciseFunction(
  front_back,
  arguments
)

def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum

arguments = [
  Args(1, 2),
  Args(3, 2),
  Args(2, 2),
  Args(-1, 0),
  Args(3, 3),
  Args(0, 0),
  Args(0, 1),
  Args(3, 4),
]

exo_sum_double = ExerciseFunction(
  sum_double,
  arguments
)

def makes10(a, b):
  return (a == 10 or b == 10 or a+b == 10)

arguments = [
  Args(9, 10),
  Args(9, 9),
  Args(1, 9),
  Args(10, 1),
  Args(10, 10),
  Args(8, 2),
  Args(8, 3),
  Args(10, 42),
  Args(12, -2),
]

exo_makes10 = ExerciseFunction(
  makes10,
  arguments
)

def not_string(str):
  if len(str) >= 3 and str[:3] == "not":
    return str
  return "not " + str
  # str[:3] goes from the start of the string up to but not
  # including index 3

arguments = [
  Args('candy'),
  Args('x'),
  Args('not bad'),
  Args('bad'),
  Args('not'),
  Args('is not'),
  Args('no'),
]

exo_not_string = ExerciseFunction(
  not_string,
  arguments
)

def first_last6(nums):
  return (nums[0]==6 or nums[-1]== 6)

arguments = [
  Args([1, 2, 6]),
  Args([6, 1, 2, 3]),
  Args([13, 6, 1, 2, 3]),
  Args([13, 6, 1, 2, 6]),
  Args([3, 2, 1]),
  Args([3, 6, 1]),
  Args([3, 6]),
  Args([6]),
  Args([3]),
  Args([5, 6]),
  Args([5, 5]),
  Args([1, 2, 3, 4, 6]),
  Args([1, 2, 3, 4]),
]

exo_first_last6 = ExerciseFunction(
  first_last6,
  arguments
)

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]  

arguments = [
  Args([1, 2, 3], [7, 3]),
  Args([1, 2, 3], [7, 3, 2]),
  Args([1, 2, 3], [1, 3]),
  Args([1, 2, 3], [1]),
  Args([1, 2, 3], [2])
]

exo_common_end = ExerciseFunction(
  common_end,
  arguments
)

def same_first_last(nums):
  return len(nums) > 0 and (nums[0] == nums[-1])

arguments = [
  Args([1, 2, 3]),
  Args([1, 2, 3, 1]),
  Args([1, 2, 1]),
  Args([7]),
  Args(([])),
  Args(([1, 2, 3, 4, 5, 1])),
  Args([1, 2, 3, 4, 5, 13]),
  Args([13, 2, 3, 4, 5, 13]),
  Args([7, 7])
]

exo_same_first_last = ExerciseFunction(
  same_first_last,
  arguments
)

def sum3(nums):
  return sum(nums)

arguments = [
  Args([1, 2, 3]),
  Args([5, 11, 2]),
  Args([7, 0, 0]),
  Args([1, 2, 1]),
  Args([1, 1, 1]),
  Args([2, 7, 2])
]

exo_sum3 = ExerciseFunction(
  sum3,
  arguments
)

def count_hi(str):
  return str.count("hi")

arguments = [
  Args('abc hi ho'),
  Args('ABChi hi'),
  Args('hihi'),
  Args('hiHIhi'),
  Args(('')),
  Args('h'),
  Args('hi'),
  Args('Hi is no HI on ahI'),
  Args('hiho not HOHIhi')
  ]

exo_count_hi = ExerciseFunction(
  count_hi,
  arguments
)

def big_diff(nums):
  max_value = max(nums)
  min_value = min(nums)
  return max_value - min_value

arguments = [
  Args([10, 3, 5, 6]),
  Args([7, 2, 10, 9]),
  Args([2, 10, 7, 2]),
  Args([2, 10]),
  Args([10, 2]),
  Args([10, 0]),
  Args([2, 3]),
  Args([2, 2]),
  Args([2]),
  Args([5, 1, 6, 1, 9, 9],)
  Args([7, 6, 8, 5]),
  Args([7, 7, 6, 8, 5, 5, 6]),
]

exo_big_diff = ExerciseFunction(
  big_diff,
  arguments
)