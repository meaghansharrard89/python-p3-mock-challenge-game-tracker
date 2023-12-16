class Game:
    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    # Game - title getter
    @property
    def title(self):
        return self._title

    # Game - title setter.Titles must be of type str. Titles must be longer than 0 characters. Should not be able to change after the game is instantiated:
    @title.setter
    def title(self, title):
        if not hasattr(self, "title") and isinstance(title, str) and len(title) > 0:
            self._title = title

    # Returns a list of all results for that game. Results must be of type Result:
    def results(self):
        return [result for result in Result.all if result.game == self]

    # Returns a unique list of all players that played a particular game. Players must be of type Player:
    def players(self):
        return list(set(result.player for result in self.results()))

    # Returns the average of all the player's scores for a particular game instance:
    def average_score(self, player):
        total = [result.score for result in self.results() if result.player == player]
        average = sum(total) / len(total)
        return average


class Player:
    def __init__(self, username):
        self.username = username

    # Player - username getter:
    @property
    def username(self):
        return self._username

    # Player - username setter. Usernames must be of type str. Usernames must be between 2 and 16 characters, inclusive. Should be able to change after the player is instantiated:
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    # Returns a list of all results for that player. Results must be of type Result:
    def results(self):
        return [result for result in Result.all if result.player == self]

    # Returns a unique list of all games played by a particular player. Games must be of type Game:
    def games_played(self):
        return list(set(result.game for result in self.results()))

    # Returns True if the player has played the game object provided. Returns False otherwise:
    def played_game(self, game):
        return any(result.game == game for result in self.results())

    # Returns the number of times the player has played the game instance provided. Returns 0 if the player never played the game provided:
    def num_times_played(self, game):
        return sum(result.game == game for result in self.results())

    # classmethod. Returns the Player instance with the highest average score for the game provided. Returns None if there are no players that played the game provided:
    @classmethod
    def highest_scored(cls, game):
        players = [result.player for result in game.results()]
        if not players:
            return None

        highest_player = max(players, key=lambda player: game.average_score(player))
        return highest_player


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)

    # Result - score getter:
    @property
    def score(self):
        return self._score

    # Result - score setter. Scores must be of type int. Scores must be between 1 and 5000, inclusive. Should not be able to change after the result is instantiated:
    @score.setter
    def score(self, score):
        if not hasattr(self, "score") and isinstance(score, int) and 1 <= score <= 5000:
            self._score = score

    # Result - player getter/setter. Must be of type Player:
    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    # Result - game getter/setter. Must be of type Game:
    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
