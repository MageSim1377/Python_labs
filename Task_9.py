ip = input("Enter IP and I in magic way will check its correctness (or no). If I wont be able to do it you can... do nothing to me! (and to programmer please:) ): ")

nums = ip.split('.')

flag = True

for i in range(len(nums)):
    if nums[i].isdigit() and not (int(nums[i]) < 0 or int(nums[i]) > 256):
        flag = False
        break

if len(nums) == 4 and flag:
    print("It is correct IP! You are good, man")
else:
    print("It is not correct IP. You have to think about it")
