

with open("input.txt", "r") as file_input:
    first_line = list((file_input.readline().split()))
    player_start = int(first_line[0])
    first_line = list((file_input.readline().split()))
    max_rounds = int(first_line[0])

print("Task:1")
import random

class GameTree:
    def __init__(self, depth_level, current_player, max_depth, node_value=None):
        self.depth_level = depth_level
        self.current_player = current_player
        self.max_depth = max_depth
        self.node_value = node_value
        self.children = []

    def generate_tree(self):
        if self.depth_level < self.max_depth:
            for _ in range(2):
                next_player = 1 - self.current_player
                child_node = GameTree(self.depth_level + 1, next_player, self.max_depth)
                self.children.append(child_node)
                child_node.generate_tree()

    def assign_leaf_value(self, value):
        self.node_value = value

def collect_leaf_nodes(root_node):
    if not root_node.children:
        return [root_node]
    all_leaves = []
    for child in root_node.children:
        all_leaves.extend(collect_leaf_nodes(child))
    return all_leaves

def alpha_beta(node, alpha, beta, maximizing_player):
    if node.depth_level == node.max_depth or not node.children:
        return node.node_value

    if maximizing_player:
        max_score = float('-inf')
        for child in node.children:
            score = alpha_beta(child, alpha, beta, False)
            if score is not None:
                max_score = max(max_score, score)
                alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    else:
        min_score = float('inf')
        for child in node.children:
            score = alpha_beta(child, alpha, beta, True)
            if score is not None:
                min_score = min(min_score, score)
                beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score

def mortal_kombat_game(initial_player):
    depth_limit = 5
    total_matches = 3
    round_outcomes = []

    for _ in range(total_matches):
        game_tree = GameTree(0, initial_player, depth_limit)
        game_tree.generate_tree()
        leaf_nodes = collect_leaf_nodes(game_tree)
        num_leaves = len(leaf_nodes)
        leaf_values = [random.choice([-1, 1]) for _ in range(num_leaves)]
        for i in range(num_leaves):
            leaf_nodes[i].assign_leaf_value(leaf_values[i])

        match_result = alpha_beta(game_tree, float('-inf'), float('inf'), initial_player == 0)
        if match_result == -1:
            winner = "Scorpion"
        else:
            winner = "Sub-Zero"
        round_outcomes.append(winner)
        initial_player = 1 - initial_player

    scorpion_victories = round_outcomes.count("Scorpion")
    sub_zero_victories = round_outcomes.count("Sub-Zero")
    if scorpion_victories > sub_zero_victories:
        overall_winner = "Scorpion"
    else:
        overall_winner = "Sub-Zero"

    print(f"Game Winner: {overall_winner}")
    print(f"Total Matches Played: {total_matches}")
    for index, round_winner in enumerate(round_outcomes):
        print(f"Winner of Match {index + 1}: {round_winner}")

mortal_kombat_game(player_start)

print("\n")
print("Task:2")

def pacman_game(dark_magic_cost):
    node_values = [3, 6, 2, 3, 7, 1, 2, 0]

    optimal_value = minimax_algorithm(0, 0, True, node_values, float('-inf'), float('inf'))

    left_path_with_magic = node_values[1] - dark_magic_cost
    right_path_with_magic = node_values[4] - dark_magic_cost
    best_magic_option = max(left_path_with_magic, right_path_with_magic)

    if best_magic_option > optimal_value:
        if left_path_with_magic > right_path_with_magic:
            print(f"The new minimax value is {best_magic_option}. Pacman goes left and uses dark magic")
        else:
            print(f"The new minimax value is {best_magic_option}. Pacman goes right and uses dark magic")
    else:
        print(f"The minimax value is {optimal_value}. Pacman does not use dark magic")

def minimax_algorithm(current_depth, current_index, is_maximizing_player, node_values, alpha, beta):
    if current_depth == 3:
        return node_values[current_index]

    if is_maximizing_player:
        maximum_score = float('-inf')
        for i in range(2):
            score = minimax_algorithm(current_depth + 1, current_index * 2 + i, False, node_values, alpha, beta)
            if score is not None:
                maximum_score = max(maximum_score, score)
                alpha = max(alpha, score)
            if beta <= alpha:
                break
        return maximum_score
    else:
        minimum_score = float('inf')
        for i in range(2):
            score = minimax_algorithm(current_depth + 1, current_index * 2 + i, True, node_values, alpha, beta)
            if score is not None:
                minimum_score = min(minimum_score, score)
                beta = min(beta, score)
            if beta <= alpha:
                break
        return minimum_score

pacman_game(max_rounds)
