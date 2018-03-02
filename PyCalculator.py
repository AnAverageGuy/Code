#Written by Joshua Martinez

operations = ["add", "addition", "+", "subtract", "subtraction", "-", "multiply", "multiplication", "divide", "division"]

def Start():
  print("Python Calculator")
  while True:
    print("What would you like to do?")
    inputO = input().lower()
    if inputO == "exit" or inputO == "quit":
      break
    if (inputO in operations):
      inputA = float(input(">"))
      inputB = float(input(">"))
      if((inputO == "+") or (inputO == "add") or (inputO == "addition")):
        value = inputA + inputB
      elif((inputO == "-") or (inputO == "subtract") or (inputO == "subtraction")):
        value = inputA - inputB
      elif((inputO == "*") or (inputO == "multiply") or (inputO == "multiplication")):
        value = inputA * inputB
      elif((inputO == "/") or (inputO == "divide") or (inputO == "division")):
        value = inputA / inputB
      print("=", value)

Start()