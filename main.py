import easyocr
import os
import csv

csv_file = 'output.csv'

def text_recognize(file_path):
    reader = easyocr.Reader(["ru"], gpu=False, verbose=False)
    result = reader.readtext(file_path, detail=0, allowlist='1,2,3,4,5,6,7,8,9,0,А,Б,В,Г,Е,З,И,К,Л,М,Н,О,П,С,Т,Х,Ч,Ь,Э,Я,а,б,в,г,е,з,и,к,л,м,н,о,п,с,т,х,ч,ь,э,я')
    result.insert(0, file_path)
    return result

'''
    # Проверяем, что есть как минимум два элемента в результате
    if len(result) >= 3:
        # Второй элемент (индекс 1) и третий элемент (индекс 2)
        print(result[2])  # Второй элемент
        print(result[3])  # Третий элемент
    # Проверяем равен ли вывод 2 номера и 3 если нето то это не купюра
    elif result[2] == result[3]:
        print("It's not a bill")
    else:
        print("Not enough text elements found in the image.")

'''
    #return result


def append_to_csv(data, filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main():
    folder_path = './input/'
    img_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    
    for file in os.listdir(folder_path):
        ext = os.path.splitext(file)[1].lower()
        if ext in img_extensions:
            #path = os.path.join(folder_path, file)
            img_path = os.path.join(folder_path, file)
            try:
                append_to_csv(text_recognize(file_path=img_path), csv_file)
            except:
                print('bad img'+img_path+'\n')


if __name__ == "__main__":
    main()
