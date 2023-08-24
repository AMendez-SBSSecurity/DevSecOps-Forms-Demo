import shutil
from tempfile import NamedTemporaryFile
import csv
import platform
newline_param = ''
if platform.system == "Windows":
    newline_param = '\n'
def fnctAddNewLine (tmpCSVFilePath,*args):
    with open(tmpCSVFilePath, 'a', newline=newline_param) as f_object: 
        writer_object = csv.writer(f_object, delimiter=',') 
        writer_object.writerow(args) 
        f_object.close()


def fnctUpdatel_ine(tmpCSVFilePath,*args):
    tmpFile=NamedTemporaryFile(mode='w', delete=False,newline=newline_param)
    tmpIDExist=False
    tmpFields=[]
    columnsToConcatenate=args[0].split(",")
    integertMapCol=map(int,columnsToConcatenate)
    columnsToConcatenate=list(integertMapCol)
    columnsToReplace=args[1].split(",")
    integertMapCol=map(int,columnsToReplace)
    columnsToReplace=list(integertMapCol)
    values=args[2:]
    with open(tmpCSVFilePath, 'r') as csvfile:
        tmpReader = csv.DictReader(csvfile)
        tmpDictCsv= dict(list(tmpReader)[0])
        tmpFields=list(tmpDictCsv.keys())
        csvfile.close()
    with open(tmpCSVFilePath, 'r', newline=newline_param) as csvfile, tmpFile:
        tmpReader = csv.DictReader(csvfile, fieldnames=tmpFields)
        tmpWriter = csv.DictWriter(tmpFile, fieldnames=tmpFields)
        for row in tmpReader:
            if row[tmpFields[0]] == str(values[0]): 
                i=0
                tmpIDExist=True
                for field in tmpFields:
                    if i in columnsToConcatenate: 
                        if row[field] == "":
                            row[field]=values[i] 
                        elif values[i] != "":
                            row[field]= row[field] +";"+ values[i]
                        else :
                            row[field]=row[field]
                    elif i in columnsToReplace:
                        row[field]=values[i]
                    else:
                        row[field]=row[field]
                    i+=1
            tmpWriter.writerow(row)
        csvfile.close()
    shutil.move(tmpFile.name,tmpCSVFilePath) 
    if not tmpIDExist:
        fnctAddNewLine(tmpCSVFilePath,*values)


