class Solution:
    def trap(self, height: List[int]) -> int:
        final_column = len(height) - 1
        water_sum = 0
        p1 = 0 
        current_dist = 0
        p2 = 0
        found = False
        while final_column - 1 >= 0:
            if height[final_column] > 0 and height[final_column - 1] < height[final_column]:
                found = True
                break
            final_column -= 1
        if not found:
            return 0
        while p2 != final_column: 
            # ^ 1 last iteration before we end the loop to get the area
            p1 = p2
            p2 = p1 + 1
            tmp_damage = 0
            current_dist = 0
            if height[p1] > height[p2]:
                """ this is if the next column is actually smaller somehow and this is after the first check of course """
                strongest = p2 + 1 #starting for strongest, will change
                strongest_dist = 1
                while True:
                    #reached = True

                    if p2 == final_column:
                        if height[strongest] >= height[final_column] and strongest != final_column:
                            strongest_dist = strongest - p1 - 1
                            water_sum += strongest_dist * min(height[p1], height[strongest])
                            p2 = strongest
                            water_sum += tmp_damage
                        elif strongest == final_column:
                            water_sum += current_dist * min(height[p1], height[strongest])

                        else:
                            strongest = final_column
                            water_sum += current_dist * min(height[p1], height[strongest])
                        if height[strongest] < height[p1 + 1]:
                            water_sum += height[p1 + 1] - height[strongest]
                        break
                    #Ok so we have a strongest and at the end we check if the strongest is bigger than the final column and if it is then we replace
                    if height[p2] >= height[p1]:
                        water_sum += current_dist * min(height[p1], height[p2])
                        break
                    elif height[p1] > height[p2]: 
                        water_sum -= height[p2]
                        tmp_damage += height[p2]
                    if (height[p2] >= height[strongest] and current_dist > 0): #change the strongest variable
                        strongest = p2
                        tmp_damage = 0
                        tmp_damage += height[strongest] # calculates the change past each wall to later add it back up
                        
                    """if p2 == p1 + 1 and not height[p1] <= height[final_column]:
                        tmp_p2 = p2
                        while True:
                            if tmp_p2 >= final_column:
                                reached = False
                                tmp_p2 = p2
                                break
                            if height[p1] <= height[p2]:
                                reached = True
                                tmp_p2 = p2
                                break
                            
                            if height[tmp_p2] > height[strongest]:
                                strongest = tmp_p2
                            tmp_p2 += 1"""
                    p2 += 1
                    current_dist += 1
        return water_sum