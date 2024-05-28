with open('301_26.txt', encoding='UTF-8') as file:
    f = file.readlines()[1:]

times = []

for item in f:
    time = [int(i) for i in item.split()][::-1]
    times.append(time)

times = sorted(times)
times = [i[::-1] for i in times]
selecedTimes = [times[1]]
times = times[1:]

for time in times:
    if selecedTimes[-1][1] <= time[0]:
        selecedTimes.append(time)

lastTwoBreak = selecedTimes[-1][0] - selecedTimes[-2][1]
print(len(selecedTimes), lastTwoBreak)
