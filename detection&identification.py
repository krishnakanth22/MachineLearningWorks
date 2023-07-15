def clean_plate(self, plate):

	gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
	thresh = cv2.adaptiveThreshold(gray, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)
	_, contours, _ = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

	if contours:
		
		areas = [cv2.contourArea(c) for c in contours]
		
		# index of the largest contour in the
		# areas array
		max_index = np.argmax(areas)

		max_cnt = contours[max_index]
		max_cntArea = areas[max_index]
		x, y, w, h = cv2.boundingRect(max_cnt)

		if not self.ratioCheck(max_cntArea,plate.shape[1],plate.shape[0]):
                    return plate, False, None
                
		
		return plate, True, [x, y, w, h]
	
	else:
            
	    return plate, False, None

def ratioCheck(self, area, width, height):
	
	min = self.min_area
	max = self.max_area

	ratioMin = 3
	ratioMax = 6

	ratio = float(width) / float(height)
	
	if ratio < 1:
            
	    ratio = 1 / ratio

	if (area < min or area > max) or (ratio < ratioMin or ratio > ratioMax):
	    return False
	
	return True
