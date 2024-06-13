import pyautogui as pg
text=input("Enter Your Text:")
times=int(input("Enter number of Repetitions:"))
pg.sleep(2)
for i in range(0,times):
    pg.write(text)
    pg.press("enter")