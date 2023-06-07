from pymavlink import mavutil

the_connection = mavutil.mavlink_connection('localhost:14550')

def arm_plane():
    the_connection.wait_heartbeat()
    the_connection.mav.command_long_send(the_connection.target_system,
                                          the_connection.target_component,
                                          mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                                          0, 1, 0, 0, 0, 0, 0, 0)

def disarm_plane():
    the_connection.wait_heartbeat()
    the_connection.mav.command_long_send(the_connection.target_system,
                                          the_connection.target_component,
                                          mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                                          0, 0, 0, 0, 0, 0, 0, 0)

def set_throttle(throttle_percentage):
    # throttle_percentage is a value between 0 and 100
    if throttle_percentage < 0 or throttle_percentage > 100:
        raise ValueError("Throttle percentage must be between 0 and 100.")
    the_connection.mav.manual_control_send(
        the_connection.target_system, 
        0, # X axis (roll) not used in manual mode
        0, # Y axis (pitch) not used in manual mode
        int(throttle_percentage * 65535 / 100), # Z axis (throttle) ranges from -100 to 100, so scale to 0 to 65535
        0, # r axis (yaw) not used in manual mode
        0) # Buttons not used in manual mode

def set_elevator_pitch(elevator_pitch_percentage):
    # elevator_pitch_percentage is a value between -100 and 100
    if elevator_pitch_percentage < -100 or elevator_pitch_percentage > 100:
        raise ValueError("Elevator/pitch percentage must be between -100 and 100.")
    the_connection.mav.manual_control_send(
        the_connection.target_system, 
        0, # X axis (roll) not used in manual mode
        int(elevator_pitch_percentage * 65535 / 200), # Y axis (pitch) ranges from -100 to 100, so scale to -32768 to 32767
        0, # Z axis (throttle) not used in manual mode
        0, # r axis (yaw) not used in manual mode
        0) # Buttons not used in manual mode
