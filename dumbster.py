import scrap
import BattingODI
import Battingtest
import BowlingOdi
import BowlingTest
import Bowlingt20
import battingt20
import os

print('lastest data collected till : {} '.format(scrap.dae))
fnames=['testdata.csv','odidata.csv','t20data.csv','odibowldata.csv','testbowling.csv','t20bowling.csv']
try:
    for i in fnames:
        os.remove(i)
        print("""{} file is being deleted to update with new data""".format(i))

except:
    print("""error during deletion or files didn't exist""")
finally:
    Battingtest.testbatting(fnames[0])
    print('TEST DATA IS COLLECTED')

    BattingODI.Odibatting(fnames[1])
    print('ODI DATA IS COLLECTED')

    BowlingOdi.odiBowling(fnames[3])
    print('ODI BOWLING DATA IS COLLECTED')

    BowlingTest.testBowling(fnames[4])
    print("test bowling data is collected")

    Bowlingt20.t20Bowling(fnames[5])
    print("t20 bowling data is collected")

    battingt20.t20batting(fnames[2])
    print('t20 batiing data is collected')