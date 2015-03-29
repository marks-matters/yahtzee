def singles(dice_list, dice_value):
	return sum(filter(lambda x: x == dice_value, dice_list))

def three_of_a_kind(dice_list):
	for dice in dice_list:
		trip_check = 0
		cumulative_score = 0
		for dice_two in dice_list:
			if dice == dice_two:
				trip_check += 1
		if trip_check >= 3:
			return sum(dice_list)
	return 0

def four_of_a_kind(dice_list):
	for dice in dice_list:
		quad_check = 0
		cumulative_score = 0
		for dice_two in dice_list:
			if dice == dice_two:
				quad_check += 1
		if quad_check >= 4:
			return sum(dice_list)
	return 0

def yahtzee(dice_list):
	first_die = dice_list[0]
	yahtzee_check = 0
	cumulative_score = 0

	for dice in dice_list:
		if dice == first_die:
			yahtzee_check += 1
	if yahtzee_check == 5:
		return 50
	return 0

def fullhouse(dice_list):
	fullhouse_check = 0
	if three_of_a_kind(dice_list) > 0:
		for dice_one in dice_list:
			for dice_two in dice_list:
				if dice_one == dice_two:
					fullhouse_check += 1
		if fullhouse_check == 13:
			return 25
	return 0

def long_straight(dice_list):
	straight_list = []
	dice_list.sort()
	start_die = dice_list[0] - 1
	for dice in dice_list:
		straight_list.append(dice - start_die)
	if straight_list == [1,2,3,4,5]:
		return 40
	return 0

def short_straight(dice_list):
	straight_counter = 0
	straight_list = []
	dice_list.sort()
	for i in range(3):
		if dice_list[i] == dice_list[i+1]:
			straight_counter += 1
	if straight_counter >= 3:
		return 30
	return 0


















