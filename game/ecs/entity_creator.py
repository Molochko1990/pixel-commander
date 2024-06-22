from .entities.entities import SoldierEntity, CityEntity
from .components.components import PositionComponent, VelocityComponent, HealthComponent, RenderComponent
from ..assets_loader import load_images


def create_soldier() -> SoldierEntity:
    entity = SoldierEntity()
    entity.add_component('position', PositionComponent(100, 100))
    entity.add_component('velocity', VelocityComponent(0, 0))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[6]))  # убрать 6 и заменить на норм чето
    return entity


def create_city(x: int, y: int, player_color: int) -> CityEntity:
    entity = CityEntity()
    entity.add_component('position', PositionComponent(x, y))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[player_color]))
    return entity
