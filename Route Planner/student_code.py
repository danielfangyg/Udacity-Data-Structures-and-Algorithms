import heapq


def shortest_path(M, start, goal):
    path_q = [(0, [start])]
    heapq.heapify(path_q)
    while path_q:
        dest_tuple = heapq.heappop(path_q)
        dest_path = dest_tuple[1]
        dest_intersection = dest_path[-1]
        current_dist_list = [cal_dist(M.intersections[i1], M.intersections[i2])
                             for i1, i2 in zip(dest_path[:-1], dest_path[1:])]
        current_dist = sum(current_dist_list)
        if dest_intersection == goal:
            return dest_path
        neighbors = M.roads[dest_intersection]
        for neigh in neighbors:
            if neigh not in dest_path:
                neigh_dist = cal_dist(M.intersections[dest_intersection],
                                      M.intersections[neigh])
                remaining_dist = cal_dist(M.intersections[goal],
                                          M.intersections[neigh])
                total_dist = current_dist + neigh_dist + remaining_dist
                frontier_path = dest_path + [neigh]
                heapq.heappush(path_q, (total_dist, frontier_path))


def cal_dist(intersection1, intersection2):
    intersection1_x = intersection1[0]
    intersection1_y = intersection1[1]
    intersection2_x = intersection2[0]
    intersection2_y = intersection2[1]
    dist = (
            (intersection1_x - intersection2_x)**2
            + (intersection1_y - intersection2_y)**2
            )**0.5
    return dist
