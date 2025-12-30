def displayData(rates):
  print(f"\n{'Term (in Years)':>10} {'Interest Rate (as Percentage)':>30}") 
  for term, rate in rates.items():
    print(f"{term:>8} {rate:>24}")
  
def get_gic(rates):
  try:
    gic_term = int(input("\nEnter GIC Term: "))
    if gic_term not in rates:
      raise ValueError
    return gic_term

  except ValueError:
    print("Invalid input. Enter only the options shown above.\n")
    exit()

def get_amount(): 
  try:
    amount = float(input("Enter amount to invest: "))
    if amount <= 0:
      raise ValueError
    return amount
  except ValueError:
    print("Invalid input. Enter a number greater than zero.\n")
    exit()

def main():
  rates = {
    1 : 4.9,
    2 : 4.1,
    3 : 4.0,
    4 : 3.8,
    5 : 3.75
  }

  displayData(rates)
  gic_term = get_gic(rates)
  amount = get_amount()

  interest_rate = rates[gic_term]
  total_interest = amount*gic_term*(interest_rate/100)

  total_amount = total_interest + amount

  print(f"Interest at end of term = ${total_interest:,.2f}")
  print(f"Total at end of term = ${total_amount:,.2f}\n")

# run this only when file is executed directly
if __name__ == "__main__":
    main()