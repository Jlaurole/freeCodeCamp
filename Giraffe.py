#guessing game to test python skills

secret_word = "giraffe"
guess = ""
guess_count = 0


while guess != secret_word and not(out of guesses):
  if guess_count < guess_limit:
    guess = input("Enter your guess: ")
    guess_count += 1
  else:
      out_of_guesses = True
 if out_of_guesses:
    print("You lose :(")
    
 else:
    print("You Win!n")

