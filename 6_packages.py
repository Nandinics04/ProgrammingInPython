#pakages
import cowsay
import sys

if len(sys.argv) == 2:
  cowsay.cow("Hii My name is"+ sys.argv[1])