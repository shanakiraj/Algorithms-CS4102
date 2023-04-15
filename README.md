# UVA Algorithms-CS4102 Assignments

This repository contains all of my programming assignments from the algorithms course at the University of Virginia (UVA). The assignments focus on four well-known algorithms: Closest Pair of Points, Kruskal's Algorithm, Seam Carving, and the Tiling Problem. Each algorithm comes with a detailed explanation, examples of applications, and any additional resources or references.

## Table of Contents

1. [Closest Pair of Points](#closest-pair-of-points)
2. [Kruskal's Algorithm](#kruskals-algorithm)
3. [Seam Carving](#seam-carving)
4. [Tiling Problem](#tiling-problem)

## Closest Pair of Points

The Closest Pair of Points problem involves finding the closest pair of points in a given set of points in a 2D plane. The algorithm utilized in this assignment is a divide-and-conquer approach, which has a time complexity of O(n log n).

Applications:

Geographic information systems: find the nearest pair of locations (e.g., restaurants, gas stations) for route planning.
Computational geometry: compute the minimum distance between two sets of points.
Clustering algorithms: identify the closest pair of data points in high-dimensional spaces.

## Kruskal's Algorithm

Kruskal's Algorithm is a greedy approach to find the minimum spanning tree for a connected, undirected graph with weighted edges. The algorithm's time complexity is O(E log E), where E is the number of edges.

**Applications:**

* Network design: build a network with minimum total cost, connecting all nodes with the least amount of cable.
* Traffic planning: find the most efficient routes between multiple locations.
* Image segmentation: cluster pixels based on their similarity in an image.

## Seam Carving

Seam Carving is an image resizing technique that maintains the most visually important features of an image while removing less important content. The algorithm identifies and removes seams (paths of minimum energy) from the image to achieve the desired dimensions.

**Applications:**

* Content-aware image resizing: adapt images to fit various screen sizes without losing important content or aspect ratios.
* Image editing: remove undesired objects or regions from an image.
* Aspect ratio conversion: change the aspect ratio of an image while preserving its visual content.

## Tiling Problem

The Tiling Problem involves finding the number of ways to fill a 2D grid of a given size with non-overlapping tiles of a fixed shape. This implementation focuses on using 2x1 domino tiles to fill a 2xN grid.

**Applications:**

* Combinatorics: calculate the number of possible tile arrangements in puzzles or games.
* Computer graphics: optimize texture mapping on 3D surfaces.
* Dynamic programming: solve larger tiling problems by building solutions from smaller subproblems.

The programming and other assignments for this course can also be found at https://uva-cs.github.io/cs4102-s22/homework/
