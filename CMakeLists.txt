cmake_minimum_required(VERSION 3.16)
project(raptor_core)

set(IS_PART_OF_RAPTOR_CORE TRUE)

add_subdirectory(modules/mocap_publisher)
add_subdirectory(modules/position_ctrl_interface)
add_subdirectory(modules/reference_generator)