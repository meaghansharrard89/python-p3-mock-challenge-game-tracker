class Game:
    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    # Game-Title getter and setter
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title"):
            self._title = title
        else:
            Exception

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set(result.player for result in self.results()))

    def average_score(self, player):
        total = [result.score for result in self.results() if result.player == player]
        if not total:
            return 0
        else:
            return sum(total) / len(total)


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    # Player-Username getter and setter
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            Exception

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list(set(result.game for result in self.results()))

    def played_game(self, game):
        return any(result.game == game for result in self.results())

    def num_times_played(self, game):
        return sum(result.game == game for result in self.results())


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    # Result-Score getter and setter
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
        else:
            Exception

    # Result-Player getter and setter
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            Exception

    # Result-Game getter and setter
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
