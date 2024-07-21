import math

import pygame.math

Vector2 = pygame.math.Vector2


def project_flat(focal_length: float, x: float, y: float) -> float:
    return (focal_length * x) / (focal_length + y)


class Vector3(pygame.math.Vector3):
    def project_vertex(self, focal_length: float) -> Vector2:
        out_vector = Vector2()
        z = self.z
        if self.z <= -19.99:
            z = -19.99
        out_vector.x = project_flat(focal_length, self.x, z)
        out_vector.y = project_flat(focal_length, self.y, z)
        return out_vector


class Cuboid:
    def __init__(self, x, y, z, width, height, depth, color):
        self.x = x
        self.y = y
        self.z = z
        self.vectors = [
            Vector3(x-(width/2), y-(height/2), z-(depth/2)),
            Vector3(x+(width/2), y-(height/2), z-(depth/2)),
            Vector3(x-(width/2), y-(height/2), z+(depth/2)),
            Vector3(x+(width/2), y-(height/2), z+(depth/2)),
            Vector3(x-(width/2), y+(height/2), z-(depth/2)),
            Vector3(x+(width/2), y+(height/2), z-(depth/2)),
            Vector3(x-(width/2), y+(height/2), z+(depth/2)),
            Vector3(x+(width/2), y+(height/2), z+(depth/2))
        ]
        self.color = color

    def project(self, focal_length) -> list:
        out_vectors = []
        for vector in self.vectors:
            out_vector = vector.project_vertex(focal_length)
            out_vector.x *= 50
            out_vector.x += 960
            out_vector.y *= 50
            out_vector.y += 540
            out_vectors.append((out_vector, math.sqrt(vector.x**2 + (vector.z+focal_length)**2)))

        return out_vectors

    def project_lines(self, focal_length) -> list:
        out_lines = []
        vectors = self.project(focal_length)
        out_lines.append([vectors[0], vectors[1]])
        out_lines.append([vectors[0], vectors[2]])
        out_lines.append([vectors[0], vectors[4]])
        out_lines.append([vectors[1], vectors[3]])
        out_lines.append([vectors[1], vectors[5]])
        out_lines.append([vectors[2], vectors[3]])
        out_lines.append([vectors[2], vectors[6]])
        out_lines.append([vectors[3], vectors[7]])
        out_lines.append([vectors[4], vectors[5]])
        out_lines.append([vectors[4], vectors[6]])
        out_lines.append([vectors[5], vectors[7]])
        out_lines.append([vectors[6], vectors[7]])
        return out_lines

    def project_polygons(self, focal_length) -> list:
        out_polygons = []
        vectors = self.project(focal_length)
        out_polygons.append([[vectors[0][0], vectors[1][0], vectors[3][0], vectors[2][0]], (vectors[0][1] + vectors[1][1] + vectors[3][1] + vectors[2][1])/4])  # top
        out_polygons.append([[vectors[4][0], vectors[5][0], vectors[7][0], vectors[6][0]], (vectors[4][1] + vectors[5][1] + vectors[7][1] + vectors[6][1])/4])  # bottom
        out_polygons.append([[vectors[0][0], vectors[1][0], vectors[5][0], vectors[4][0]], (vectors[0][1] + vectors[1][1] + vectors[5][1] + vectors[4][1])/4])  # front
        out_polygons.append([[vectors[2][0], vectors[3][0], vectors[7][0], vectors[6][0]], (vectors[2][1] + vectors[3][1] + vectors[7][1] + vectors[6][1])/4])  # back
        out_polygons.append([[vectors[0][0], vectors[2][0], vectors[6][0], vectors[4][0]], (vectors[0][1] + vectors[2][1] + vectors[6][1] + vectors[4][1])/4])  # left
        out_polygons.append([[vectors[1][0], vectors[3][0], vectors[7][0], vectors[5][0]], (vectors[1][1] + vectors[3][1] + vectors[7][1] + vectors[5][1])/4])  # right
        return out_polygons

    def add_x(self, amount):
        for vector in self.vectors:
            vector.x += amount
        self.x += amount

    def add_y(self, amount):
        for vector in self.vectors:
            vector.y += amount
        self.y += amount

    def add_z(self, amount):
        for vector in self.vectors:
            vector.z += amount
        self.z += amount
