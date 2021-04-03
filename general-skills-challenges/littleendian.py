import sys, os; 
os.fdopen(1,"wb").write("abc".encode("utf-16be"))
