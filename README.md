# MPU6050-I2C-Python-Class
Using a MPU6050 and its Digital Motion Processor (DMP) over I2C with Python on a Raspberry PI

A bunch of issues have been fixed from thisisG's Python Class with this repo (incorrect yaw calc, python3 syntax, replaced time.clock(), etc).

Make sure I2C has been activated on your Pi using raspi-config
Make sure to have "pip3 install simple-pid" installed when testing "MPU6050_cal.py". This not required to run this however this:

Try "python3 MPU6050_example.py" for reading sequence of roll, pitch and yaw. Note: offset will periodically be recalcuated during runtime
