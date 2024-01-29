import math

class KinematicModel:
    def __init__(self, a, b, c, init_pose):
        self.a = a
        self.b = b
        self.c = c

        self.joint_limits = {
            'Q1': [-180, 180],
            'Q2': [-180, 90],
            'Q3': [-180, 180],
            'D4': [0, 30],
            'G1': [0, 6],
            'G2': [0, 6]
        }

        self.current_joint_state = {
            'Q1': init_pose[0],
            'Q2': init_pose[1],
            'Q3': init_pose[2],
            'D4': init_pose[3],
            'G1': init_pose[4],
            'G2': init_pose[5]
        }

        self.current_cartesian_state = {
            'X': 0.0,
            'Y': 0.0,
            'Z': 0.0
        }

        # Used to fill cartesian state with appropriate values
        self.movej_rel('Q1', 0)

    def check_limits(self, q1, q2, d4):
        if (self.joint_limits['Q1'][0] <= q1 <= self.joint_limits['Q1'][1] and
            self.joint_limits['Q2'][0] <= q2 <= self.joint_limits['Q2'][1] and
            self.joint_limits['D4'][0] <= d4 <= self.joint_limits['D4'][1]):
            return True
        else:
            return False

    def movej_rel(self, axis, delta):
        next = self.current_joint_state[axis] + delta
        if (self.joint_limits[axis][0] <= next <= self.joint_limits[axis][1]):
            self.current_joint_state[axis] += delta
            pose = self.FKM(self.current_joint_state['Q1'], self.current_joint_state['Q2'], self.current_joint_state['D4'])
            self.current_cartesian_state['X'] = pose[0]
            self.current_cartesian_state['Y'] = pose[1]
            self.current_cartesian_state['Z'] = pose[2]
            return "In bounds"
        else:
            return "Joint limit exceeded!"
        
    def movel_rel(self, axis, delta):
        self.current_cartesian_state[axis] += delta
        j = self.IKM(self.current_cartesian_state['X'], self.current_cartesian_state['Y'], self.current_cartesian_state['Z'])
        if (self.joint_limits['Q1'][0] <= j[0] <= self.joint_limits['Q1'][1] and
            self.joint_limits['Q2'][0] <= j[1] <= self.joint_limits['Q2'][1] and
            self.joint_limits['D4'][0] <= j[2] <= self.joint_limits['D4'][1]):
            self.current_joint_state['Q1'] = j[0]
            self.current_joint_state['Q2'] = j[1]
            self.current_joint_state['D4'] = j[2]
            return "In bounds"
        else:
            self.current_cartesian_state[axis] -= delta
            return "Joint limit exceeded!"
        
    def movej_abs(self, q1, q2, d4):
        if (self.joint_limits['Q1'][0] <= q1 <= self.joint_limits['Q1'][1] and
            self.joint_limits['Q2'][0] <= q2 <= self.joint_limits['Q2'][1] and
            self.joint_limits['D4'][0] <= d4 <= self.joint_limits['D4'][1]):
            self.current_joint_state['Q1'] = q1
            self.current_joint_state['Q2'] = q2
            self.current_joint_state['D4'] = d4
            pose = self.FKM(self.current_joint_state['Q1'], self.current_joint_state['Q2'], self.current_joint_state['D4'])
            self.current_cartesian_state['X'] = pose[0]
            self.current_cartesian_state['Y'] = pose[1]
            self.current_cartesian_state['Z'] = pose[2]
            return "In bounds"
        else:
            return "Joint limit exceeded!"
        
    def movel_abs(self, x, y, z):
        j = self.IKM(x, y, z)
        if (self.joint_limits['Q1'][0] <= j[0] <= self.joint_limits['Q1'][1] and
            self.joint_limits['Q2'][0] <= j[1] <= self.joint_limits['Q2'][1] and
            self.joint_limits['D4'][0] <= j[2] <= self.joint_limits['D4'][1]):
            self.current_joint_state['Q1'] = j[0]
            self.current_joint_state['Q2'] = j[1]
            self.current_joint_state['D4'] = j[2]
            self.current_cartesian_state['X'] = x
            self.current_cartesian_state['Y'] = y
            self.current_cartesian_state['Z'] = z
            return "In bounds"
        else:
            return "Joint limit exceeded!"

    def FKM(self, q1, q2, d4):
        x = -(self.a - (d4 + self.b) * math.sin(math.radians(q2))) * math.sin(math.radians(q1))
        y = (self.a - (d4 + self.b) * math.sin(math.radians(q2))) * math.cos(math.radians(q1))
        z = (d4 + self.b) * math.cos(math.radians(q2)) + self.c
        return [x, y, z]
    
    def IKM(self, x, y, z):
        z = z - self.c
        q1 = -math.atan2(x, y)
        q2 = math.atan2(x+self.a*math.sin(q1), z*math.sin(q1))
        d4 = z/math.cos(q2) - self.b
        return [math.degrees(q1), math.degrees(q2), d4]