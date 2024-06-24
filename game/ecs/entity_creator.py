from .entities.entities import SoldierEntity, CityEntity, TankEntity
from .components.components import PositionComponent, VelocityComponent, HealthComponent, RenderComponent
from ..assets_loader import load_images


#Только эту функцию надо будет оставить, остальные убрать.
def create_entity(x: int, y: int, entity_color: int, entity: SoldierEntity | TankEntity | CityEntity) -> SoldierEntity | TankEntity | CityEntity:
    entity = entity()
    entity.add_component('position', PositionComponent(x, y))
    entity.add_component('velocity', VelocityComponent(0, 0))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[entity_color]))
    return entity


def create_soldier(x: int=50, y: int=50, player_color: int=6) -> SoldierEntity:
    entity = SoldierEntity()
    entity.add_component('position', PositionComponent(x, y))
    entity.add_component('velocity', VelocityComponent(0, 0))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[player_color]))
    return entity


def create_city(x: int, y: int, player_color: int) -> CityEntity:
    entity = CityEntity()
    entity.add_component('position', PositionComponent(x, y))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[player_color]))
    return entity
