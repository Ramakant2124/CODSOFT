
try :
    print("Try Block Start ")
    fn=int(input("Enter the Frist Number :"))
    sn=int(input("Enter the Second Number :"))
    ans=fn/sn
    print(ans)
    print("Try Block Ends")
except ZeroDivisionError as zde:
    print(zde)
    print("please choose the  denometri value is non zero ")
except ValueError as ve :
    print(ve)
    print("please Enter the numeric whole number only " )
except Exception as e:
    print(e)
    print("Except block Ther is some error exception in try bolck")
else:
    print("else block there is no exception in try block")
print("Reming code......")
print("--------END LINE -------")

