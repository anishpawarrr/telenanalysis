import gspread as gs

jsonfile = "datatele-366319-0d5fecc26b48.json"
gc = gs.service_account(jsonfile)
l = ["a", "b", "c", "d", "e", "f"]
tp = gc.open("Tele2")
wk = tp.get_worksheet(2)
l = [['1','2','3'],['4','5','6'],['7','8','9']]
for i in range(1,4):
    for j in range(1,4):
        wk.update_cell(i,j,l[i-1][j-1])
#    time.sleep(1)
#wk.update_cell(1,1,"Eureka!!!")
# wk.close()
print("hehe")