# Lab 7

Previous tasks implemented:

- Create a Turret class with turret image
  - Turret is stationary at a location of your choice
  - Turret fires bullets towards the player
    - Use same bullet image but make turret bullets shorter (round)
    - Give turret a cannon cooldown
    - you can user Geometry class to get turret angle. First point is the turret location, 
    second point is the player location
    - Keep turret bullets in a separate list called `turret_bullets`
- Move image loading to Level class
- Clean up `__init__` methods for entities (pull images from level class)
- Create levels states and level progression

Tutorial: 

- Iterate through the turret bullets and check collision with player
- Implement player health and draw it on screen
  - If player is hit, remove 1 health. If player health is <= 0, player.alive = False
  - If player collides with asteroid, player dies immediately
- Implement Turret health and draw it on screen
  - If turret is hit, remove health. If turret health is <= 0, turret.alive = False
- Add explosion animations
- Add small explosions for laser hit on player and turret

Tasks:

- Implement collisions between player and turret. If player and turret collide,
  player dies
- Implement teleporting on right mouse button click. If right button is pressed, player 
  teleports to the location where the mouse is positioned on screen. 
  - Cooldown for the teleport ability is 10 seconds (600 frames)
  - Render teleport cooldown text to screen
- Turret random location can be on any edge of the screen (top, bottom, left,
  right), instead of only left edge of the screen as in the tutorial. But
  turrent cannot be spawned in the middle of the screen, it has to be on an edge.
- Add health packs
  - Every 10 seconds a health pack is spawned somewhere on the screen, randomly
  - When player picks up the health pack the player's health is increased
  - Find a graphic for the health pack and add it to level
  - HealthPack class can either inherit from entity, or you can create a new
    class from scratch, like for the explosion.
  - HealhtPack should not move across the screen. Only one health pack can be
    on screen at the time. If 10 seconds passes and health pack is not picked
    up by the player, the pack moves to a different location. 
  - If health pack is picked up by the player, another healht pack will not be
    spawned for 10 seconds from the moment the player picked up the pack.

