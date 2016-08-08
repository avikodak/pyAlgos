'''
File Name                   : reversewordsinastring.py
Created on                  : Aug 7, 2016
Author                      : avikodak
Testing Status              : Tested
URL                         : http://www.practice.geeksforgeeks.org/problem-page.php?pid=282
'''

'''
Tested
'''
if __name__ == '__main__':
    testCases = int(input())
    for counter in range(1, testCases + 1):
        userInput = input().strip()
        print(".".join(userInput.split('.')[::-1]).strip())