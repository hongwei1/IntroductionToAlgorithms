class chapter2InsertionSort:
    #
    a = [5,7,1,9,4]
    # b = a.copy()
    # print(len(a))
    # # sort the array.
    # for i in range(len(a)):
    #     print(i)
    #     min = a[i]
    #     j = i
    #     while (j < len(a) and a[j] < min):
    #         min = a[j]
    #         j=j+1
    #     b[i]=min;
    #
    # print(b)

    #1st: prepare min value from the array:
    def get_min_value_and_index(thelist):
        min = thelist[0]
        min_idex= 0
        for j in range(1, len(thelist)):
            if(thelist[j] < min):
                min = thelist[j]
                min_idex = j
        # print("the min value is {}".format(min))
        # print("the index of min value is {}".format(min_idex))
        return (min,min_idex)

    #2rd: prepare the swap algrithom:
    def swap_two_items(thelist, i, j):
        first_value = thelist[i]
        thelist[i]= thelist[j]
        thelist[j]= first_value
        return thelist

    #3rd: sort
    def my_sort_algorithm (theList):
        for i in range(0, len(theList)):
            min_idex = i
            # this step should find the min index from i to len(theList)
            for j in range(i+1, len(theList)):
                if(theList[j]< theList[min_idex]):
                    min_idex= j
            chapter2InsertionSort.swap_two_items(theList,i,min_idex)
        return theList


    #4th: the book one, insertion-sort
    def insertion_sort(theList):
        for i in range(1, len(theList)):
            key = theList[i]
            j = i-1
            while( j>=0 and theList[j]>key):
                theList[j+1] = theList[j]
                j = j - 1
            theList[j+1] = key
        return theList;