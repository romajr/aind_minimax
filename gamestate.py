from copy import deepcopy

xlim, ylim = 3, 2  # board dimensions

class GameState:

    def __init__(self):
        self._board = [[0 for j in range(ylim)] for i in range(xlim)]
        self._board[xlim-1][0] = 1  # block lower-right corner
        self._player_code = 0
        self._player_location = [None, None]

    def _get_nobody_inside(self):
        return [(x, y) for y in range(ylim) for x in range(xlim)
            if self._board[x][y] == 0]

    def _get_legal_moves(self):
        actual_player = self._player_location[self._player_code]
        if not actual_player:
            return self._get_nobody_inside()
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
        for dx, dy in directions:
            _x, _y = actual_player
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]:
                    break
                moves.append((_x, _y))
        return moves

    def forecast_move(self, move):
        if move not in self._get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        newBoard = deepcopy(self)
        newBoard._board[move[0]][move[1]] = 1
        newBoard._player_location[self._player_code] = move
        newBoard._player_code ^= 1
        return newBoard
