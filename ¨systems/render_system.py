from ..components.position import PositionComponents
from ..components.render import RenderComponents 

class RenderSystem:
    def update(self, entity, screen):
        pos = entity.components[PositionComponents]
        render = entity.components[RenderComponents]

