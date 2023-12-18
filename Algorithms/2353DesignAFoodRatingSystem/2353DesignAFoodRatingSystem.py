from typing import List
import heapq


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_cuisines = {}
        self.foods_rating = {}
        self.cuisines_foods = {}
        for i in range(len(foods)):
            if cuisines[i] not in self.foods_cuisines:
                self.foods_cuisines[cuisines[i]] = []
            heapq.heappush(self.foods_cuisines[cuisines[i]], [-ratings[i], foods[i]])
            self.foods_rating[foods[i]] = ratings[i]
            self.cuisines_foods[foods[i]] = cuisines[i]

    def changeRating(self, food: str, newRating: int) -> None:
        heapq.heappush(
            self.foods_cuisines[self.cuisines_foods[food]], [-newRating, food]
        )
        self.foods_rating[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        if len(self.foods_cuisines[cuisine]) == 0:
            return None
        current_heap_rating, current_heap_max_food_name = self.foods_cuisines[cuisine][
            0
        ]
        while -current_heap_rating != self.foods_rating[current_heap_max_food_name]:
            current_heap_rating, current_heap_max_food_name = self.foods_cuisines[
                cuisine
            ][0]
            if -current_heap_rating == self.foods_rating[current_heap_max_food_name]:
                return current_heap_max_food_name
            else:
                heapq.heappop(self.foods_cuisines[cuisine])
        return current_heap_max_food_name


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
