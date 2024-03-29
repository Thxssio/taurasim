#!/usr/bin/env python3
# coding=utf-8

"""
    File:
        spawn_robots.py

    Description:
        Parametrized spawner for multiple robots
"""

import math
import time
import pygame

import rospy
import rospkg
import roslaunch

PACKAGE_NAME = 'taurasim'
SPAWN_LAUNCHFILE = 'spawn_robot.launch'

COLORS = ["blue", "yellow"]

FORMATION_3X3 = {
    COLORS[0]: [(-0.2, 0), (-0.5, 0.3), (-0.5, -0.3)],
    COLORS[1]: [(0.2, 0), (0.5, 0.3), (0.5, -0.3)]
}

FORMATION_5X5 = {
    COLORS[0]: [(-0.3, 0), (-0.45, 0.4), (-0.45, -0.4), (-0.7, 0), (-1.1, 0)],
    COLORS[1]: [(0.3, 0), (0.45, 0.4), (0.45, -0.4), (0.7, 0), (1.1, 0)]
}


def get_yaw(color):
    if color == COLORS[0]:
        return 0
    else:
        return math.pi


def get_is_yellow(color):
    if color == "yellow":
        return "true"
    else:
        return "false"


def get_launchfiles(node_name, robots_per_team, team_color):
    roslaunch_files = []

    if robots_per_team == 3:
        formations = FORMATION_3X3
    elif robots_per_team == 5:
        formations = FORMATION_5X5
    else:
        raise ValueError('Invalid number of robots per team')

    for i in range(robots_per_team):
        cli_args = [
            PACKAGE_NAME,
            SPAWN_LAUNCHFILE,
            f'robot_number:={i}',
            f'is_yellow:={get_is_yellow(team_color)}',
            f'robot_name:={team_color}_team/robot_{i}',
            f'x:={formations[team_color][i][0]}',
            f'y:={formations[team_color][i][1]}',
            f'yaw:={get_yaw(team_color)}',
            f'model:={rospy.get_param(f"{node_name}/model")}',
            f'twist_interface:={rospy.get_param(f"{node_name}/twist_interface")}',
            f'controller_config_file:={rospy.get_param(f"{node_name}/controller_config_file")}',
            f'ros_control_config_file:={rospy.get_param(f"{node_name}/ros_control_config_file")}',
            f'namespace:={team_color}_team/robot_{i}'
        ]

        roslaunch_args = cli_args[2:]
        roslaunch_file = (roslaunch.rlutil.resolve_launch_arguments(cli_args)[0], roslaunch_args)

        roslaunch_files.append(roslaunch_file)

    return roslaunch_files


if __name__ == '__main__':
    try:
        rospy.init_node('robots_spawner', anonymous=True)

        # Config roslaunch
        uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
        roslaunch.configure_logging(uuid)

        # Get launchfiles
        node_name = rospy.get_name()

        robots_per_team = rospy.get_param(f"{node_name}/robots_per_team")
        team_color = rospy.get_param(f"{node_name}/team_color")

        roslaunch_files = get_launchfiles(node_name, robots_per_team, team_color)

        # Config sound
        should_play_sound = rospy.get_param(f"{node_name}/sound")

        if should_play_sound:
            rospack = rospkg.RosPack()
            path = rospack.get_path('taurasim')

            pygame.mixer.init()

            # License: The sound effect is permitted for non-commercial use under
            # license Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
            # http://www.orangefreesounds.com/
            pop_effect = pygame.mixer.Sound(path + '/sounds/pop.wav')

            pop_effect.set_volume(1.0)

        for file in roslaunch_files:
            launch = roslaunch.parent.ROSLaunchParent(uuid, [file])
            launch.start()

            if should_play_sound:
                time.sleep(0.3 * robots_per_team)
                pop_effect.play()
                time.sleep(pop_effect.get_length())

        rospy.spin()
    except rospy.ROSInterruptException:
        pass