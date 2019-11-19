# Alec Ramdass
# Tuesday, November 12th, 2019
'''
Description:
This program will open whichever Lab you need
for CSCI-127 according to the number you input
'''

import webbrowser

print('Use this program to Open any Lab you need to review for CSCI-127\n')

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

site = ('ERROR',Lab1,Lab2,Lab3,Lab4,Lab5,Lab6,Lab7,Lab8,Lab9,Lab10,Lab11)

while True:
    LabNum = int(input('Enter Desired Lab Number: '))
    webbrowser.open(site[LabNum])

