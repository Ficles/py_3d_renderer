import pygame.math

Vector2 = pygame.math.Vector2


def project_flat(focal_length: float, x: float, y: float) -> float:
    return ((focal_length + y) / focal_length) * x


class Vector3(pygame.math.Vector3):
    def project_vertex(self, focal_length: float) -> Vector2:
        out_vector = Vector2()
        out_vector.x = project_flat(focal_length, self.x, self.z)
        out_vector.y = project_flat(focal_length, self.y, self.z)
        return out_vector


class Cuboid:
    def __init__(self, vectors: list[Vector3]):
        self.v1 = vectors[0]
        self.v2 = vectors[1]
        self.v3 = vectors[2]
        self.v4 = vectors[3]
        self.v5 = vectors[4]
        self.v6 = vectors[5]
        self.v7 = vectors[6]
        self.v8 = vectors[7]
        self.vectors = vectors

    def project(self, focal_length) -> list:
        out_vectors = []
        for vector in self.vectors:
            out_vectors.append(vector.project_vertex(focal_length))

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
