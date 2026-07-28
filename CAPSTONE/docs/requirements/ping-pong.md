# Characteristics of a Ping-Pong Game

## Display
- Show the playing field.
- Display two paddles.
- Display a moving ball.
- Show player scores.

## Paddle Controls
- Player 1 can move paddle up and down.
- Player 2 can move paddle up and down (or be AI-controlled).
- Prevent paddles from moving off-screen.

## Movement
- Ball starts in the center.
- Ball moves continuously.
- Ball bounces off the top and bottom edges.
- Ball changes direction after hitting a paddle.

## Collision Detection
- Detect collisions between:
- Ball and paddles
- Ball and screen boundaries
- Update the ball's direction accordingly.

## Scoring
- Award one point when the opponent misses the ball.
- Reset the ball to the center after each point.
- Display updated scores.

## Game End
- End the game when a player reaches a target score (e.g., 5 or 10).
- Display the winnner