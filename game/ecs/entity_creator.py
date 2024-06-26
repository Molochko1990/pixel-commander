from .entities.entities import SoldierEntity, CityEntity, TankEntity
from .components.components import PositionComponent, VelocityComponent, HealthComponent, RenderComponent, PlayerComponent
from ..assets_loader import load_images


def create_entity(x: int, y: int, entity_color: int, entity: SoldierEntity | TankEntity | CityEntity, player_id: int, max_movement_range=3) -> SoldierEntity | TankEntity | CityEntity:
    entity = entity()
    entity.add_component('player_id', PlayerComponent(player_id))
    entity.add_component('position', PositionComponent(x, y))
    entity.add_component('velocity', VelocityComponent(max_movement_range))
    entity.add_component('health', HealthComponent(100))
    entity.add_component('render', RenderComponent(load_images()[entity_color]))
    return entity

