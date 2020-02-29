'''
Author: Alec Ramdass
Date: Tuesday, November 12th, 2019

Description: This program was written to conveniently 
access the labs for my CSCI-127 class.
'''
import sys as s
import webbrowser as w

print('To open a labs from CSCI-127 (Introduction to Computer Science)')

Lab1 = "https://stjohn.github.io/teaching/csci127/f19/lab1.html"
Lab2 = "https://stjohn.github.io/teaching/csci127/f19/lab2.html"
Lab3 = "https://stjohn.github.io/teaching/csci127/f19/lab3.html"
Lab4 = "https://stjohn.github.io/teaching/csci127/f19/lab4.html"
Lab5 = "https://stjohn.github.io/teaching/csci127/f19/lab5.html"
Lab6 = "https://stjohn.github.io/teaching/csci127/f19/lab6.html"
Lab7 = "https://stjohn.github.io/teaching/csci127/f19/lab7.html"
Lab8 = "https://stjohn.github.io/teaching/csci127/f19/lab8.html"
Lab9 = "https://stjohn.github.io/teaching/csci127/f19/lab9.html"
Lab10 = "https://stjohn.github.io/teaching/csci127/f19/lab10.html"
Lab11 = "https://stjohn.github.io/teaching/csci127/f19/lab11.html"

site = (0,Lab1,Lab2,Lab3,Lab4,Lab5,Lab6,Lab7,Lab8,Lab9,Lab10,Lab11)

while True:
    labNum = int(input("[Type '0' to exit program]\nEnter Lab Number(1-11): "))
    if type(labNum) != type(0):
        print("Enter a number between 1 and 11")
    elif labNum == 0:
       s.exit()
    else:
        w.open(site[labNum])

