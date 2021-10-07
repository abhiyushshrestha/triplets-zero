from itertools import combinations
import numpy as np

class TripletsZero:
    def __init__(self):
        self.user_list = ''
        self.values = ''
        self.flag = 1

    def getValues(self):
        '''
            Funtion to get the values from the user
        :return: list of the values entered by the user
        '''
        input_string = input('Enter numbers separated by space: ')
        print("\n")
        user_list = input_string.split()
        try:
            values = list(map(int, user_list))
            self.flag = 0
        except:
            self.flag = 1
            values = ''
            print("The value entered must be all numbers.")
        return values

    def getCombinations(self, values, n):
        '''
            Function to get the combination of the values
        :param values: input values entered by the user
        :param n: total number of combination to make
        :return: list of combination values
        '''
        comb_values = combinations(values, n)
        combination_values = []
        for i in comb_values:
            combination_values.append(list(i))
        return combination_values

    def removeDuplicates(self, tripletsZero):
        '''
            Function to remove the duplicates
        :param tripletsZero: a list of all the triplets including duplicates
        :return: a unique lists of triplets
        '''
        triplets = []
        for triplet in tripletsZero:
            if triplet not in triplets:
                triplets.append(triplet)
        return triplets

    def checkTripletsZero(self, comb_value):
        '''
            Function to check if the triplets is zero or not
        :param comb_value:
        :return: sum of a triplet
        '''
        comb_value_np = np.array(comb_value)
        tripletsSum = np.sum(comb_value_np)
        return tripletsSum

    def tripletsZero(self, combination_values):
        '''
            Function to get all the triplets
        :param combination_values: lists of all the possible combination of values entered by the user
        :return: lists of triplets that sums up to zero
        '''
        tripletsZeroList = []
        for comb_value in combination_values:
            tripletsSum = self.checkTripletsZero(comb_value)
            if tripletsSum == 0:
                comb_value_list = comb_value
                tripletsZeroList.append(comb_value_list)

        # Performing sorting of elements in the list to get the find out the duplicate list
        for triplet in tripletsZeroList:
            triplet.sort()

        triplets = self.removeDuplicates(tripletsZeroList)
        return triplets


if __name__ == "__main__":

    triplet = TripletsZero()
    while triplet.flag == 1:
        values = triplet.getValues()
        if triplet.flag == 0:
            break

    combination_values = triplet.getCombinations(values, 3)
    tripletsZero = triplet.tripletsZero(combination_values)
    print(tripletsZero)

