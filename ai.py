import copy


class AI:

    # -----------------------
    #   playground code
    @staticmethod
    def alpha_beta(state, depth, alpha, beta, maximizer):
        if depth == 0 or state.game_over():
            if state.game_state() == 'o':
                return -1
            elif state.game_state() == 'x':
                return 1
            else:
                return 0
        elif maximizer:
            value = -2
            for move in state.possible_moves():
                temp_game = copy.deepcopy(state)
                temp_game.update(move)
                value = max(value, AI.alpha_beta(temp_game, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value
        else:
            value = 2
            for move in state.possible_moves():
                temp_game = copy.deepcopy(state)
                temp_game.update(move)
                value = min(value, AI.alpha_beta(temp_game, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value

    @staticmethod
    def best_move_for_x(state):
        value = -2
        best_move = state.possible_moves()[0]
        for move in state.possible_moves():
            temp_game = copy.deepcopy(state)
            temp_game.update(move)
            current_value = AI.alpha_beta(temp_game, 9, -2, 2, False)
            if current_value > value:
                value = current_value
                best_move = move
        state.update(best_move)

    @staticmethod
    def best_move_for_o(state):
        value = 2
        best_move = None
        for move in state.possible_moves():
            temp_game = copy.deepcopy(state)
            temp_game.update(move)
            current_value = AI.alpha_beta(temp_game, 7, -2, 2, True)
            if current_value < value:
                value = current_value
                best_move = move
        state.update(best_move)
