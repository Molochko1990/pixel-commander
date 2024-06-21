from .entities.entities import SoldierEntity
from .components.components import PositionComponent, VelocityComponent, HealthComponent, RenderComponent
from ..assets_loader import load_images


def create_soldier():
    entity = SoldierEntity()
    entity.add_component('position', PositionComponent(1, 1))
    entity.add_component('velocity', VelocityComponent(0, 0))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[6]))
    return entity
