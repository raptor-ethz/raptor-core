#!/bin/bash
echo 'Starting pick and place' 
gnome-terminal -- ./build/modules/mocap_publisher/app/mocap_publisher 
gnome-terminal -- ./build/modules/position_ctrl_interface/apps/position_control/pos_ctrl_interface serial:///dev/ttyACM0
gnome-terminal -- ./build/modules/reference_generator/apps/pick_and_place/pick_and_place 