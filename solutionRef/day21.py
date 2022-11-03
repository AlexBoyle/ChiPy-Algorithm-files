import sys

class Solution:
    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    def parse(self, input):
        output = []
        for line in input:
            temp = line.replace("\n", "").split(" (contains ")
            temp[0] = temp[0].split(" ")
            temp[1] = temp[1].replace(" ", "").replace(")", "").split(",")
            output.append(temp)
        return output
    def groupByContains(self, input):
        output = {}
        for line in input: 
            for contains in line[1]:
                if contains in output.keys():
                    output[contains].append(line)
                else:
                    output[contains] = [line]
        return output
    def findLikeThings(self, input):
        output = {}
        for key in input.keys():
            intersection = input[key][0][0]
            for item in input[key]:
                intersection = self.intersection(intersection, item[0]);
            output[key] = intersection
        return output
    def allWords(self, input):
        output = {""}
        for line in input:
            for word in line[0]:
                output.add(word)
        return output
    def countOcc(self, thingsToFind, input):
        output = 0
        allA = []
        for key in thingsToFind:
            allA = allA + thingsToFind[key]
        for line in input:
            for word in line[0]:
                if word not in allA:
                    output = output + 1
        return output
    def run(self, input):
        input = self.parse(input)
        groupedDic = self.groupByContains(input)
        allWords = self.allWords(input)
        a = self.findLikeThings(groupedDic)
        count = self.countOcc(a, input)
        
        print (count)
    

input = []
for line in sys.stdin:
   input.append(line)
solution = Solution();
solution.run(input)



