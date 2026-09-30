import calculations as calc

def check(data, expect, real):
    result = "Match" if real == expect else "Does not match"  

    print("Input data: ", data)
    print("Expected result: ", expect)
    print("Actual result: ", real)
    print(f"\n Result: {result}\n")

check("(5)", 5, calc.mean(5))
check("(2, 4, 6)", 4, calc.mean(2, 4, 6))
check("()", None, calc.mean())

check("(0)", 0, calc.clamp(0))
check("(100)", 100, calc.clamp(100))
check("(-10)", 0, calc.clamp(-10))
check("(150)", 100, calc.clamp(150))
check("(50, 100, 0)", None, calc.clamp(50, 100, 0))

check("([1, 2, 3], [2, 3, 4])", 20,
    calc.weighted_sum([1, 2, 3], [2, 3, 4]))

check("([], [])", None,
    calc.weighted_sum([], []))

check("([1, 2], [3])", None,
    calc.weighted_sum([1, 2], [3]))

check("([1], [])", None,
      calc.weighted_sum([1], []))

check('("Andrew")',
      "Andrew | {}",
      calc.format_record("Andrew"))

check('("Andrew", age=18)',
      "Andrew | {'age': 18}",
      calc.format_record("Andrew", age=18))

check('("Andrew", age=18, group="CS-55")',
      "Andrew | {'age': 18, 'group': 'CS-55'}",
      calc.format_record("Andrew", age=18, group="CS-55"))


check("factorial(0)", 1, calc.factorial(0))
check("factorial(1)", 1, calc.factorial(1))
check("factorial(4)", 24, calc.factorial(4))
check("factorial(-1)", None, calc.factorial(-1))


check("factorial_loop(0)", 1, calc.factorial_loop(0))
check("factorial_loop(1)", 1, calc.factorial_loop(1))
check("factorial_loop(4)", 24, calc.factorial_loop(4))
check("factorial_loop(-1)", None, calc.factorial_loop(-1))