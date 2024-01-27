import math

class KinematicModel:
    def __init__(self, a, b, init_pose):
        self.a = a
        self.b = b

        self.joint_limits = {
            'Q1': [-90, 90],
            'Q2': [-90, 90],
            'Q3': [-90, 90],
            'D4': [0, 30]
        }

        self.current_joint_state = {
            'Q1': init_pose[0],
            'Q2': init_pose[1],
            'Q3': init_pose[2],
            'D4': init_pose[3]
        }

        self.current_cartesian_state = {
            'X': 0.0,
            'Y': 0.0,
            'Z': 0.0
        }

        # Used to fill cartesian state with appropriate values
        self.movej('Q1', 0)

    def movej(self, axis, delta):
        next = self.current_joint_state[axis] + delta
        if (next >= self.joint_limits[axis][0] and next <= self.joint_limits[axis][1]):
            self.current_joint_state[axis] += delta
            pose = self.FKM(self.current_joint_state['Q1'], self.current_joint_state['Q2'], self.current_joint_state['D4'])
            self.current_cartesian_state['X'] = pose[0]
            self.current_cartesian_state['Y'] = pose[1]
            self.current_cartesian_state['Z'] = pose[2]
            return True
        else:
            return False

    def FKM(self, q1, q2, d4):
        x = -(self.a - (d4 + self.b) * math.sin(math.radians(q2))) * math.sin(math.radians(q1))
        y = (self.a - (d4 + self.b) * math.sin(math.radians(q2))) * math.cos(math.radians(q1))
        z = (d4 + self.b) * math.cos(math.radians(q2))
        return [x, y, z]
    
    def IKM(self, x, y, z):
        q1 = -math.atan2(x, y)
        q2 = math.atan2(x+self.a*math.sin(q1), z*math.sin(q1))
        d4 = z/math.cos(q2) - self.b
        return [math.degrees(q1), math.degrees(q2), d4]