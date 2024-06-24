from .entities.entities import SoldierEntity, CityEntity, TankEntity
from .components.components import PositionComponent, VelocityComponent, HealthComponent, RenderComponent
from ..assets_loader import load_images


#Только эту функцию надо будет оставить, остальные убрать.
def create_entity(x: int, y: int, entity_color: int, entity: SoldierEntity | TankEntity | CityEntity, dx: int = 0, dy: int = 0) -> SoldierEntity | TankEntity | CityEntity:
    entity = entity()
    entity.add_component('position', PositionComponent(x, y))
    entity.add_component('velocity', VelocityComponent(dx, dy))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[entity_color]))
    return entity

