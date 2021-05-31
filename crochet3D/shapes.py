import numpy as np

# radial, azimuth, longitudinal
# outwards, around, along
# girth, angle, length 
# rho, phi, z

def sc_6_into_magic_ring():
    #for a circle: round, stitch, 0-1
    ring = (0,0,0.5)
    polar_bottom = [(1,0,0),(1,1,0),(1,2,0),(1,3,0),(1,4,0),(1,5,0)]
    polar_top = [(1,0,1),(1,1,1),(1,2,1),(1,3,1),(1,4,1),(1,5,1)]
    vertices = []
    vertices.append(to_cartesian(ring))
    for point in polar_bottom:
        print(point)
        print(to_cartesian(point))
        vertices.append(to_cartesian(point))
    for point in polar_top:
        vertices.append(to_cartesian(point))
    # 0=ring, 1-6=[bottom points] 7-12[top points]
    faces = [[0,1,2],[0,7,8],[1,2,7],[2,7,8],
            [0,2,3],[0,8,9],[2,3,8],[3,8,9],
            [0,3,4],[0,9,10],[3,4,9],[4,9,10],
            [0,4,5],[0,10,11],[4,5,10],[5,10,11],
            [0,5,6],[0,11,12],[5,6,11],[6,11,12],
            [0,6,1],[0,12,7],[6,1,12],[1,12,7]]
    print(vertices)
    return np.array(vertices), np.array(faces)

def to_cartesian(point):
    r = point[0]
    theta = point[1]
    x = r*np.cos(theta)
    y= r*np.sin(theta)
    return (x,y,point[2])