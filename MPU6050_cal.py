from MPU6050 import MPU6050
#from SimplePID import SimplePID
from simple_pid import PID 


def avg_from_array(a_array):
    sum = 0.0
    for index in range(0, len(a_array)):
        sum += a_array[index]

    return sum/len(a_array)


i2c_bus = 1
device_address = 0x68
# The offsets are different for each device and should be changed
# accordingly using a calibration procedure
x_accel_offset = 0
y_accel_offset = 0
z_accel_offset =0
x_gyro_offset = 0
y_gyro_offset = 0
z_gyro_offset = 0
enable_debug_output = True

mpu = MPU6050(i2c_bus, device_address, x_accel_offset, y_accel_offset,
              z_accel_offset, x_gyro_offset, y_gyro_offset, z_gyro_offset,
              enable_debug_output)

kp = 0.03125
ki = 0.25
kd = 0

pidax = PID(kp, ki, kd, 0,1, (-15000, 15000),True )
piday = PID(kp, ki, kd, 0,0, (-15000, 15000),True )
pidaz = PID(kp, ki, kd, 0,0, (-15000, 15000),True )

pidgx = PID(kp, ki, kd, 0,0, (-15000, 15000),True )
pidgy = PID(kp, ki, kd, 0,0, (-15000, 15000),True )
pidgz = PID(kp, ki, kd, 0,0, (-15000, 15000),True )


accel_reading = mpu.get_acceleration()

x_accel_reading = accel_reading[0]
y_accel_reading = accel_reading[1]
z_accel_reading = accel_reading[2]

x_accel_avg = [0]*100
y_accel_avg = [0]*100
z_accel_avg = [0]*100

x_accel_offset_avg = [0]*100
y_accel_offset_avg = [0]*100
z_accel_offset_avg = [0]*100

axindex = 0
ayindex = 0
azindex = 0

gyro_reading = mpu.get_rotation()

x_gyro_reading = gyro_reading[0]
y_gyro_reading = gyro_reading[1]
z_gyro_reading = gyro_reading[2]

x_gyro_avg = [0]*100
y_gyro_avg = [0]*100
z_gyro_avg = [0]*100

x_gyro_offset_avg = [0]*100
y_gyro_offset_avg = [0]*100
z_gyro_offset_avg = [0]*100

gxindex = 0
gyindex = 0
gzindex = 0

try:
    while True:
        accel_reading = mpu.get_acceleration()
        x_accel_reading = accel_reading[0]
        y_accel_reading = accel_reading[1]
        z_accel_reading = accel_reading[2]

        gyro_reading = mpu.get_rotation()
        x_gyro_reading = gyro_reading[0]
        y_gyro_reading = gyro_reading[1]
        z_gyro_reading = gyro_reading[2]

        if 1 > 0:
            x_accel_offset = pidax(x_accel_reading)

            mpu.set_x_accel_offset(int(x_accel_offset))

            x_accel_avg[axindex] = x_accel_reading
            x_accel_offset_avg[axindex] = x_accel_offset

            axindex += 1
            if axindex == len(x_accel_avg):
                axindex = 0
                print('x_avg_read: ' +
                      str(avg_from_array(x_accel_avg)) +
                      ' x_avg_offset: ' +
                      str(avg_from_array(x_accel_offset_avg)))
                print('y_avg_read: ' +
                      str(avg_from_array(y_accel_avg)) +
                      ' y_avg_offset: ' +
                      str(avg_from_array(y_accel_offset_avg)))
                print('z_avg_read: ' +
                      str(avg_from_array(z_accel_avg)) +
                      ' z_avg_offset: ' +
                      str(avg_from_array(z_accel_offset_avg)))

        if 1 > 0:
            y_accel_offset = piday(y_accel_reading)

            mpu.set_y_accel_offset(int(y_accel_offset))

            y_accel_avg[ayindex] = y_accel_reading
            y_accel_offset_avg[ayindex] = y_accel_offset

            ayindex += 1
            if ayindex == len(y_accel_avg):
                ayindex = 0

        if 1 > 0:
            z_accel_offset = pidaz(z_accel_reading)

            mpu.set_z_accel_offset(int(z_accel_offset))

            z_accel_avg[azindex] = z_accel_reading
            z_accel_offset_avg[azindex] = z_accel_offset

            azindex += 1
            if azindex == len(z_accel_avg):
                azindex = 0

        # Gyro calibration
        if 1 > 0:
            x_gyro_offset = pidgx(x_gyro_reading)

            mpu.set_x_gyro_offset(int(x_gyro_offset))

            x_gyro_avg[gxindex] = x_gyro_reading
            x_gyro_offset_avg[gxindex] = x_gyro_offset

            gxindex += 1
            if gxindex == len(x_gyro_avg):
                gxindex = 0
                print('x_gyro_avg_read: ' +
                      str(avg_from_array(x_gyro_avg)) +
                      ' x_avg_offset: ' +
                      str(avg_from_array(x_gyro_offset_avg)))
                print('y_gyro_avg_read: ' +
                      str(avg_from_array(y_gyro_avg)) +
                      ' y_avg_offset: ' +
                      str(avg_from_array(y_gyro_offset_avg)))
                print('z_gyro_avg_read: ' +
                      str(avg_from_array(z_gyro_avg)) +
                      ' z_avg_offset: ' +
                      str(avg_from_array(z_gyro_offset_avg)))

        if 1 >0:
            y_gyro_offset = pidgy(y_gyro_reading)

            mpu.set_y_gyro_offset(int(y_gyro_offset))

            y_gyro_avg[gyindex] = y_gyro_reading
            y_gyro_offset_avg[gyindex] = y_gyro_offset

            gyindex += 1
            if gyindex == len(y_gyro_avg):
                gyindex = 0

        if 1 > 0:
            z_gyro_offset = pidgz(z_gyro_reading)

            mpu.set_z_gyro_offset(int(z_gyro_offset))

            z_gyro_avg[gzindex] = z_gyro_reading
            z_gyro_offset_avg[gzindex] = z_gyro_offset

            gzindex += 1
            if gzindex == len(z_gyro_avg):
                gzindex = 0

except KeyboardInterrupt:
    pass

