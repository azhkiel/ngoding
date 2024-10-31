// main.js
const canvas = document.getElementById('board');
const ctx = canvas.getContext('2d');

// Calculate size of canvas from constants.
ctx.canvas.width = COLS * BLOCK_SIZE;
ctx.canvas.height = ROWS * BLOCK_SIZE;

// Scale blocks
ctx.scale(BLOCK_SIZE, BLOCK_SIZE);

// Create board and piece
const board = new Board(ctx);
const piece = new Piece(0, ctx);

// Game loop
function gameLoop() {
  // code to update the game state and draw the pieces
}

// Start the game loop
gameLoop();