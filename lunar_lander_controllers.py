




## Attitude Control First: The controller checks angle_control before main thrust. Firing the main thruster while heavily tilted will drive the lander sideways into the terrain rather than slowing its fall.
## Dynamic Target Angle: Instead of trying to maintain $\theta = 0$ constantly, the target angle leans into the origin ($0.5x + 1.0\dot{x}$) to drift horizontally back toward the landing pad.
## Descent Rate Control: The vertical controller switches to a softer target descent rate ($\approx -0.1$) as altitude drops below $0.4$, preventing heavy impact penalties.
def pd_heuristic_controller(obs):
    """
    Computes a discrete action (0, 1, 2, 3) using a heuristic PD loop.
    Target: Land smoothly between the flags at x = 0 with zero tilt and velocity.
    """
    x, y, vx, vy, angle, angular_vel, left_leg, right_leg = obs

    # Target angle: Steer towards the center (x = 0) while damping horizontal speed
    target_angle = 0.5 * x + 1.0 * vx
    # Clamp target angle to keep the craft from over-tilting
    target_angle = max(-0.4, min(0.4, target_angle))

    # Angle PD error term
    angle_error = target_angle - angle
    angle_control = angle_error * 15.0 - angular_vel * 20.0

    # Target vertical speed: Descend faster when high, slow down near the ground
    target_vy = -0.3 if y > 0.4 else -0.1
    vy_error = target_vy - vy
    vertical_thrust = vy_error * 10.0 - 0.5

    # Prioritize rotational stability, then altitude control
    if angle_control > 1.0:
        return 1  # Fire left engine -> rotate right
    elif angle_control < -1.0:
        return 3  # Fire right engine -> rotate left
    elif vertical_thrust > 0.0:
        return 2  # Fire main engine -> upward thrust
    else:
        return 0  # Coast
