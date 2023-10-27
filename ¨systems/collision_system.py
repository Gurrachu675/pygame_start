from ..components.position import PositionComponents 

class CollisionSystem:
    def check_collision(self, snake, food):
        snake_pos = snake.components[PositionComponents]
        food_pos = food.components[PositionComponents]
        return snake_pos.x == food_pos.x and snake_pos.y == food_pos.y