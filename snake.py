from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Creates the initial snake and appoints the head.
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Creates a snake body consisting for three segments each with a pre-defined position.
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Adds a segment to the snake body.
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        # Resets the game by creating a new snake while disposing of the old one.
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # Adds a new segment to the end of the snake body.
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Each segment will move in the position of its predecessor, thus creating the moving illusion.
        # However, the head of the snake will move by a constant amount in the direction it's currently facing.
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Changes the direction of the snake while ensuring it does not collide within itself.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
