#!/bin/bash
echo '*** PICK AND PLACE MISSION ***' 
gnome-terminal -- ./build/modules/mocap_publisher/app/mocap_publisher srl_quad srl_stand srl_pick_crate srl_place_crate
echo 'Started mocap publisher' 
gnome-terminal -- ./build/modules/position_ctrl_interface/apps/position_control/pos_ctrl_interface serial:///dev/ttyACM0
echo 'Started Position Control Interface' 
gnome-terminal -- ./build/modules/reference_generator/apps/pick_and_place/pick_and_place 
echo 'Started Reference Generator' 