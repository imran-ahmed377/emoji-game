# Emoji Game 🎮

A fun and interactive memory-matching game built with Python and Pygame. Match pairs of animal emoji tiles to win!

## Features

- 🎮 **Interactive Gameplay**: Click tiles to reveal animal emojis
- 🐾 **8 Different Animals**: Dog, Cat, Bird, Fish, Lion, Panda, Tiger, and Bear
- 🎨 **Colorful Design**: Each animal has a unique colored background
- 🏆 **Win Condition**: Match all 8 pairs to complete the game
- ⌨️ **Easy Controls**: Mouse clicks to play, ESC to exit

## Requirements

- Python 3.7+
- pygame
- pillow (for asset generation)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd emoji-game
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install pygame pillow
```

### 4. Generate Assets

If the `assets/` and `other_assets/` folders don't exist, run:

```bash
python create_assets.py
python create_matched.py
```

## How to Play

1. **Start the Game**:
   ```bash
   python app.py
   ```

2. **Game Rules**:
   - A 4x4 grid of tiles appears with a gray box covering each one
   - Click on a tile to reveal the hidden animal emoji
   - You can keep up to 2 tiles revealed at a time
   - If the two revealed tiles match, they stay revealed (a green success image displays)
   - If they don't match, they flip back after a brief moment
   - Match all 8 pairs to win!

3. **Controls**:
   - **Left Mouse Button**: Click to reveal a tile
   - **ESC Key**: Exit the game
   - **Window Close Button**: Exit the game

## Project Structure

```
emoji-game/
├── app.py                 # Main game loop
├── animal.py              # Animal class for game tiles
├── game_config.py         # Game configuration and constants
├── create_assets.py       # Script to generate animal images
├── create_matched.py      # Script to generate success image
├── assets/                # Folder containing animal emoji images
│   ├── dog.png
│   ├── cat.png
│   ├── bird.png
│   ├── fish.png
│   ├── lion.png
│   ├── panda.png
│   ├── tiger.png
│   └── bear.png
├── other_assets/          # Folder containing UI assets
│   └── matched.png        # Success/match display image
├── .venv/                 # Virtual environment (if using)
└── README.md              # This file
```

## Configuration

Game settings can be modified in `game_config.py`:

- `IMAGE_SIZE`: Size of each tile (default: 128px)
- `SCREEN_SIZE`: Size of the game window (default: 512px)
- `NUM_TILES_SIDE`: Number of tiles per side (default: 4)
- `NUM_TILES_TOTAL`: Total number of tiles (default: 16)
- `MARGIN`: Padding around tiles (default: 8px)
- `ASSET_DIR`: Directory containing animal images (default: 'assets')

## Game Logic

### Animal Class (`animal.py`)
- Randomly assigns one of 8 animals to each tile
- Ensures exactly 2 tiles per animal (for matching pairs)
- Generates the display image and gray box placeholder

### Main Game Loop (`app.py`)
- Handles mouse clicks and keyboard input
- Tracks which tiles are currently revealed
- Checks for matching pairs
- Displays success image when a match is found
- Ends game when all pairs are matched

## Gameplay Tips

- 🧠 **Memory Strategy**: Try to remember where each animal is located
- ⏱️ **Quick Matches**: Match tiles quickly before forgetting their positions
- 👀 **Pattern Recognition**: Look for patterns in tile positions

## Troubleshooting

### Missing Assets Error
If you get `FileNotFoundError` for assets:
```bash
python create_assets.py
python create_matched.py
```

### Pygame Not Found
Install pygame:
```bash
pip install pygame
```

### Pillow Not Found
Install pillow:
```bash
pip install pillow
```

## Future Enhancements

- ⏱️ Add a timer to track completion time
- 📊 Display score and statistics
- 🎵 Add sound effects and background music
- 🎨 Add different themes and difficulty levels
- 💾 Save high scores
- 🎭 More animal options
- 👥 Multiplayer mode

## License

This project is open source and available under the MIT License.

## Author

Created as an educational Pygame project.

---

**Enjoy the Game!** 🎮✨
