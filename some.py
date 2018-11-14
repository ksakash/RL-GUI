
import sqlite3

def insertDB(grid_sz, grid_str, action_str, scene):
	grid_nw = []
	for x in grid_str.split("\n"):
		tmp = []
		for y in x.strip().split(" "):
			# print(y)
			tmp += [float(y)]
		grid_nw += [tmp]
	actions = [int(x) for x in action_str.strip().split(" ")]
	print(actions)
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO GRIDS (GRIDSZ ,PATH ,MATRIX, scenerio) VALUES (?,?,?,?)",(grid_sz, str(actions), str(grid_nw), scene) )
	conn.commit()
	return


def getGridDB(grid_sz, scene):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM GRIDS WHERE GRIDSZ=" + str(grid_sz) + " AND scenerio = " +  str(scene)
	cur.execute(cmd)
	row = cur.fetchone()
	return row

def insertSurvey(gridsz, actions, reward, time, scene):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO survey_resp (gridsz ,action ,reward, time, scenerio) VALUES (?,?,?,?, ?)",(gridsz, actions, reward, time, scene) )
	conn.commit()
	return

def showSurvey(grid_sz):
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	cmd = "SELECT * FROM survey_resp WHERE scenerio > 0 and gridsz=" + str(grid_sz)
	cur.execute(cmd)
	row = cur.fetchall()
	return row
#
# me = """9.93902 12.8421 8.71663 13.8168 1.23127 20.6623 2.51048 14.2361 8.65642 8.53208
# 2.61363 27.9924 16.4527 1.90766 11.6631 9.18846 17.6012 0.932384 11.7058 16.7574
# 7.24286 3.76452 4.03663 11.2972 7.19652 7.50594 1.55235 8.51413 7.77937 8.60909
# 5.28398 19.4578 7.55837 5.78214 3.9705 4.79105 18.9326 18.3731 18.9479 8.70942
# 27.9211 6.55108 16.0663 16.7635 10.4953 3.46503 5.92905 7.70239 8.38791 7.47266
# 8.75266 18.3099 8.45757 10.3794 18.276 1.53727 15.1478 10.8083 26.8213 18.7753
# 10.5989 19.5487 3.67239 16.0351 18.1285 6.07885 16.0667 20.3353 24.0237 18.9332
# 3.92238 11.587 6.01947 16.4635 10.2552 15.9228 22.0852 18.5281 20.0235 13.0041
# 11.265 16.2228 24.5859 0.77565 12.752 16.1233 11.2271 2.99652 8.6946 14.1279
# 20.9075 12.5259 10.7525 14.1224 6.9909 1.11627 11.568 12.2467 14.6226 20.3782"""

# act = ["2 1 2 0 2 1 1 3 3 1 3 1 1 2 1 1 1 2 1 2 2 0 2 0 2 2 0 2 0 2 1 1 3 1 1 2 ",
# "2 2 0 3 3 0 0 0 0 0 2 0 0 0 2 1 1 2 1 1 3 1 3 1 1 2 2 0 2 0 0 2 2 1 2 2 2 0 3 0 3 3 3 0 3 0 3 0 2 2 2 2 2 1 2 0 ",
# "1 3 1 1 3 3 1 1 2 2 2 1 3 3 1 2 2 1 1 3 0 3 3 0 0 3 1 1 3 0 3 0 2 0 2 0 3 3 3 1 3 1 1 1 2 1 3 3 ",
# "0 0 0 0 3 1 3 1 2 1 1 3 3 0 0 0 0 2 0 3 0 2 2 2 0 0 0 3 3 3 3 3 3 3 3 1 2 1 3 1 3 0 0 0 ",
# "2 1 2 0 2 1 1 3 3 1 3 1 2 2 2 2 1 1 1 2 2 2 0 2 0 2 1 1 3 1 1 3 3 0 3 3 1 3 3 0 3 1 3 "
# ]
# ctr = 1
# for x in act:
# 	insertDB(10, me, x, ctr)
# 	getGridDB(10, ctr)
# 	ctr += 1
# insertDB(10, me, "2 2 0 3 3 0 0 0 0 0 2 0 0 0 2 1 1 2 1 1 3 1 3 1 1 2 2 0 2 0 0 2 2 1 2 2 2 0 3 0 3 3 3 0 3 0 3 0 2 2 2 2 2 1 2 0 ", 2)
