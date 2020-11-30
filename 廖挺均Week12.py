season = "1995-1996"
team = "Chicago Bulls"
coach = "Phil Jackson"
records = [72, 10]
starting_lineup = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
won_championship = True
best_chicago_bulls = list((season, team, coach, records,
starting_lineup, won_championship))
print(best_chicago_bulls)
print(type(best_chicago_bulls))
# indexing 索引
print(best_chicago_bulls[0])
print(best_chicago_bulls[-1])
# slicing 切片
print(best_chicago_bulls[1:4])
print(best_chicago_bulls[::-1])