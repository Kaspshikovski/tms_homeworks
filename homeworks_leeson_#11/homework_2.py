class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed

        self.passengers = []

        self.seats = {number: None for number in range(1, max_seats + 1)}

    @property
    def has_free_seats(self):
        return len(self.passengers) < self.max_seats

    def add_passenger(self, passenger):
        if passenger in self:
            return False

        if not self.has_free_seats:
            return False

        for seat, person in self.seats.items():
            if person is None:
                self.seats[seat] = passenger
                self.passengers.append(passenger)
                return True

    def add_passengers(self, passengers):
        for passenger in passengers:
            self.add_passenger(passenger)

    def remove_passenger(self, passenger):
        if passenger not in self:
            return False

        for seat, person in self.seats.items():
            if person == passenger:
                self.seats[seat] = None
                break

        self.passengers.remove(passenger)
        return True

    def remove_passengers(self, passengers):
        for passenger in passengers:
            self.remove_passenger(passenger)

    def increase_speed(self, value):
        if value < 0:
            raise ValueError('Значение должно быть положительным')

        self.speed = min(self.speed + value, self.max_speed)

    def decrease_speed(self, value):
        if value < 0:
            raise ValueError('Значение должно быть положительным')

        self.speed = max(self.speed - value, 0)

    def __contains__(self, passenger):
        return passenger in self.passengers

    def __iadd__(self, passenger):
        self.add_passenger(passenger)
        return self

    def __isub__(self, passenger):
        self.remove_passenger(passenger)
        return self

    def __str__(self):
        return (
            f'Скорость: {self.speed}/{self.max_speed}\n'
            f'Пассажиры: {self.passengers}\n'
            f'Свободные места: {self.has_free_seats}'
        )