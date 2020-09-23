def groupingDishes(dishes):
    '''
    Group dishes by ingredients
    - has to be in at least two dishes
    - first element in the list is the name of the ingredient
    - all other elements are th enames of the dishes that contain this ingredient
    - sorted in lexographical order
    '''
    ingredients_dict= {}

    for dish in dishes: # iterate through dishes
        for ingredient in dish[1:]:
            if ingredient in ingredients_dict: # adding items to ht
                ingredients_dict[ingredient].append(dish[0])
            else:
                ingredients_dict[ingredient] = [dish[0]]
        
    result = []

    for ingredient in sorted(ingredients_dict): # sort lexographically
        if len(ingredients_dict[ingredient]) > 1: # ingredient shows up in more than one dish
            result.append([ingredient] + sorted(ingredients_dict[ingredient]))
    return result

