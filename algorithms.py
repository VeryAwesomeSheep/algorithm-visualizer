import random, time
import ui

class Algorithms:
	# shell sort
	def ShellSort(delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		values = [bar.value() for bar in bars]

		n = len(values) 
		gap = n//2
		while gap > 0: 
			for i in range(gap,n): 
				temp = values[i] 
				j = i 
				while  j >= gap and values[j-gap] > temp:
					time.sleep(delay)
					bars[j].setValue(values[j-gap])
					values[j] = values[j-gap] 
					j -= gap 
				time.sleep(delay)
				bars[j].setValue(temp)
				values[j] = temp 
			gap //= 2

		return values

	# insertion sort
	def InsertionSort(delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		values = [bar.value() for bar in bars]

		for i in range(1, len(values)):
			key = values[i]
			j = i - 1

			while j >= 0 and values[j] > key:
				time.sleep(delay)
				values[j + 1] = values[j]
				bars[j + 1].setValue(values[j])
				j -= 1

			values[j + 1] = key
			bars[j + 1].setValue(key)

		return values

	# function for radix sort
	def radixSortHelper(delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		values = [bar.value() for bar in bars]

		__class__.radixSort(values, delay)

		return values

	# main radix sort function
	def countingSort(values, exp1, delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		n = len(values)
		output = [0] * (n) 
		count = [0] * (10) 
		for i in range(0, n): 
			index = (values[i]/exp1) 
			count[int(index % 10)] += 1
		for i in range(1,10): 
			count[i] += count[i-1] 
		i = n-1
		while i>=0: 
			index = (values[i]/exp1) 
			output[count[int((index) % 10)] - 1] = values[i] 
			count[int((index)%10)] -= 1
			i -= 1
		i = 0
		for i in range(len(values)):
			time.sleep(delay)
			bars[i].setValue(output[i])
			values[i] = output[i]
		
		return values

	# function for radix sort
	def radixSort(values, delay):    
		exp = 1
		for i in range(3):
			values = __class__.countingSort(values,exp, delay) 
			exp *= 10

		return values

	# selection sort
	def SelectionSort(delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		values = [bar.value() for bar in bars]

		n = len(values)

		for j in range(n):
			minIndex = j
			for i in range(j + 1, n):
				time.sleep(delay)
				if values[i] < values[minIndex]:
					minIndex = i
			bars[j].setValue(values[minIndex])
			bars[minIndex].setValue(values[j])
			time.sleep(delay)

			values[j], values[minIndex] = values[minIndex], values[j]

		return values

	# bubble sort
	def BubbleSort(delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		values = [bar.value() for bar in bars]

		n = len(values)

		for i in range(n-1):
			for j in range(0,n-i-1):
				if values[j] > values[j+1]:
					time.sleep(delay)
					bars[j].setValue(values[j+1])
					bars[j+1].setValue(values[j])
					values[j], values[j+1] = values[j+1], values[j]
		return values

	# comb sort
	def CombSort(delay):
		bars = [ui.Ui_MainWindow.bar1, ui.Ui_MainWindow.bar2, ui.Ui_MainWindow.bar3, ui.Ui_MainWindow.bar4, ui.Ui_MainWindow.bar5, ui.Ui_MainWindow.bar6, ui.Ui_MainWindow.bar7, ui.Ui_MainWindow.bar8, ui.Ui_MainWindow.bar9, ui.Ui_MainWindow.bar10, ui.Ui_MainWindow.bar11, ui.Ui_MainWindow.bar12, ui.Ui_MainWindow.bar13, ui.Ui_MainWindow.bar14, ui.Ui_MainWindow.bar15, ui.Ui_MainWindow.bar16, ui.Ui_MainWindow.bar17, ui.Ui_MainWindow.bar18, ui.Ui_MainWindow.bar19, ui.Ui_MainWindow.bar20, ui.Ui_MainWindow.bar21, ui.Ui_MainWindow.bar22, ui.Ui_MainWindow.bar23, ui.Ui_MainWindow.bar24, ui.Ui_MainWindow.bar25, ui.Ui_MainWindow.bar26, ui.Ui_MainWindow.bar27, ui.Ui_MainWindow.bar28, ui.Ui_MainWindow.bar29, ui.Ui_MainWindow.bar30, ui.Ui_MainWindow.bar31, ui.Ui_MainWindow.bar32, ui.Ui_MainWindow.bar33, ui.Ui_MainWindow.bar34, ui.Ui_MainWindow.bar35, ui.Ui_MainWindow.bar36, ui.Ui_MainWindow.bar37, ui.Ui_MainWindow.bar38, ui.Ui_MainWindow.bar39, ui.Ui_MainWindow.bar40, ui.Ui_MainWindow.bar41, ui.Ui_MainWindow.bar42, ui.Ui_MainWindow.bar43, ui.Ui_MainWindow.bar44, ui.Ui_MainWindow.bar45, ui.Ui_MainWindow.bar46, ui.Ui_MainWindow.bar47, ui.Ui_MainWindow.bar48, ui.Ui_MainWindow.bar49, ui.Ui_MainWindow.bar50, ui.Ui_MainWindow.bar51, ui.Ui_MainWindow.bar52, ui.Ui_MainWindow.bar53, ui.Ui_MainWindow.bar54, ui.Ui_MainWindow.bar55, ui.Ui_MainWindow.bar56, ui.Ui_MainWindow.bar57, ui.Ui_MainWindow.bar58, ui.Ui_MainWindow.bar59, ui.Ui_MainWindow.bar60, ui.Ui_MainWindow.bar61, ui.Ui_MainWindow.bar62, ui.Ui_MainWindow.bar63, ui.Ui_MainWindow.bar64, ui.Ui_MainWindow.bar65, ui.Ui_MainWindow.bar66, ui.Ui_MainWindow.bar67, ui.Ui_MainWindow.bar68, ui.Ui_MainWindow.bar69, ui.Ui_MainWindow.bar70, ui.Ui_MainWindow.bar71, ui.Ui_MainWindow.bar72, ui.Ui_MainWindow.bar73, ui.Ui_MainWindow.bar74, ui.Ui_MainWindow.bar75, ui.Ui_MainWindow.bar76, ui.Ui_MainWindow.bar77, ui.Ui_MainWindow.bar78, ui.Ui_MainWindow.bar79, ui.Ui_MainWindow.bar80, ui.Ui_MainWindow.bar81, ui.Ui_MainWindow.bar82, ui.Ui_MainWindow.bar83, ui.Ui_MainWindow.bar84, ui.Ui_MainWindow.bar85, ui.Ui_MainWindow.bar86, ui.Ui_MainWindow.bar87, ui.Ui_MainWindow.bar88, ui.Ui_MainWindow.bar89, ui.Ui_MainWindow.bar90, ui.Ui_MainWindow.bar91, ui.Ui_MainWindow.bar92, ui.Ui_MainWindow.bar93, ui.Ui_MainWindow.bar94, ui.Ui_MainWindow.bar95, ui.Ui_MainWindow.bar96, ui.Ui_MainWindow.bar97, ui.Ui_MainWindow.bar98, ui.Ui_MainWindow.bar99, ui.Ui_MainWindow.bar100]
		values = [bar.value() for bar in bars]

		n = len(values)
		gap = n
		swaps = True

		while n > 1 or swaps:
			n = max(1, int(n / 1.25))
			swaps = False
			for i in range(n - gap):
				time.sleep(delay)
				j = i + gap
				if values[i] > values[j]:
					bars[i].setValue(values[j])
					bars[j].setValue(values[i])
					values[i], values[j] = values[j], values[i]
					swaps = True

		return values
