'''sortowanie przez scalanie (mergesort):
-dzielimy tablice na 2 części (devide and conquer)
-sortujemy rekurencyjnie połówki
-mając połówki posortowane lecimy po kolei i łączymy połówki
'''


def mergeSort(Array, Left, Right):
    def merge(Array, Left, Mid, Right):
        Len1 = Mid - Left + 1
        Len2 = Right - Mid
        Left_Array = Array[Left:Mid + 1]
        Right_Array = Array[Mid + 1:Right + 1]
        Left_index = Right_index = 0
        Main_index = Left

        while Left_index < Len1 and Right_index < Len2:
            if Left_Array[Left_index] <= Right_Array[Right_index]:  # antystabilny merge jeżeli zawsze pierwsze weźmie to po prawej
                Array[Main_index] = Left_Array[Left_index]
                Left_index += 1
            else:
                Array[Main_index] = Right_Array[Right_index]
                Right_index += 1
            Main_index += 1

        while Left_index < Len1:
            Array[Main_index] = Left_Array[Left_index]
            Left_index += 1
            Main_index += 1

        while Right_index < Len2:
            Array[Main_index] = Right_Array[Right_index]
            Right_index += 1
            Main_index += 1

    if Left < Right:
        Mid = (Left + Right) // 2
        mergeSort(Array, Left, Mid)
        mergeSort(Array, Mid + 1, Right)
        merge(Array, Left, Mid, Right)


