// board.js
class Board {
    constructor(ctx) {
      this.ctx = ctx;
      this.grid = this.getEmptyBoard();
    }
  
    getEmptyBoard() {
      return Array.from(
        {length: ROWS}, () => Array(COLS).fill(0)
      );
    }
  
    drawBoard() {
      // code to draw the board
    }
  
    checkCollision(piece) {
      // code to check for collisions
    }
  }