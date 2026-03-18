def get_daily_steps():
    steps = input("Enter your daily steps for 7 days separated by spaces: ")
    step_list = steps.split()
    step_list = [int(s) for s in step_list]
    return step_list

def total_steps(nums):
    return sum(nums)

def average_steps(total, days=7):
    return total // days

def max_steps(nums):
    return max(nums)

def min_steps(nums):
    return min(nums)

def goal_check(nums, goal=10000):
    result = []
    for s in nums:
        if s >= goal:
            result.append(True)
        else:
            result.append(False)
    return result

step_list = get_daily_steps()

total = total_steps(step_list)
average = average_steps(total)
highest = max_steps(step_list)
lowest = min_steps(step_list)
goal_met = goal_check(step_list)

print("Total steps:", total)
print("Average daily steps:", average)
print("Highest steps in a day:", highest)
print("Lowest steps in a day:", lowest)
print("Goal met each day:", goal_met)