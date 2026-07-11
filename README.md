# 🐍 Snake Game (Python)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Turtle_Graphics-Built--In-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Object_Oriented_Programming-OOP-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/license/yourusername/snake-game-python?style=flat-square" />
  <img src="https://img.shields.io/github/stars/yourusername/snake-game-python?style=flat-square" />
  <img src="https://img.shields.io/github/forks/yourusername/snake-game-python?style=flat-square" />
  <img src="https://img.shields.io/github/repo-size/yourusername/snake-game-python?style=flat-square" />
  <img src="https://img.shields.io/github/last-commit/yourusername/snake-game-python?style=flat-square" />
  <img src="https://img.shields.io/github/issues/yourusername/snake-game-python?style=flat-square" />
</p>

---

## 📖 Overview

A classic **Snake Game** developed using **Python** and the built-in **Turtle Graphics** module.

This project demonstrates the fundamentals of **Object-Oriented Programming (OOP)** by separating the game's logic into multiple classes. It includes smooth snake movement, random food spawning, collision detection, score tracking, and a persistent high-score system that stores the highest score even after the game is closed.

The project is lightweight, beginner-friendly, and a great example of organizing Python applications into reusable modules.

---

# 📸 Gameplay

<p align="center">
  <img src="images/game_screenshot.png" alt="Snake Game Screenshot" width="850">
</p>

---

# ✨ Features

- 🐍 Smooth snake movement
- 🍎 Random food generation
- 📈 Live score tracking
- 🏆 Persistent high-score system
- 💥 Wall collision detection
- 🔄 Self-collision detection
- 🎮 Responsive keyboard controls
- 📂 Modular Object-Oriented architecture
- ⚡ Automatic game reset after collision
- 💾 High score saved locally
- 🚀 Lightweight with no external dependencies

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| Turtle Graphics | Game Rendering |
| OOP | Code Structure |
| Random Module | Food Generation |
| Text File (`data.txt`) | High Score Storage |

---

# 📂 Project Structure

```
snake-game-python/
│
├── images/
│   └── game_screenshot.png
│
├── main.py
├── snake.py
├── food.py
├── scoreboard.py
├── data.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📄 File Description

| File | Description |
|------|-------------|
| `main.py` | Creates the game window, initializes all game objects, handles keyboard events, manages the game loop, and detects collisions. |
| `snake.py` | Defines the Snake class, controls movement, growth, and prevents reversing direction. |
| `food.py` | Generates food at random positions whenever the snake eats. |
| `scoreboard.py` | Displays the score, updates the high score, and saves it permanently to `data.txt`. |
| `data.txt` | Stores the highest score achieved by the player. |
| `images/` | Contains screenshots used in the README. |

---

# 🧩 Object-Oriented Design

The game follows a modular OOP architecture where each class is responsible for a single task.

```text
                +------------------+
                |     main.py      |
                +------------------+
                 /       |       \
                /        |        \
               /         |         \
      +---------+   +---------+   +---------------+
      | snake.py|   | food.py |   | scoreboard.py |
      +---------+   +---------+   +---------------+
            |             |               |
            |             |               |
      Snake Movement   Food Spawn     Score & High Score
```

---

# ⚙️ How the Game Works

### 1️⃣ Game Initialization

- Creates the Turtle screen
- Sets screen size
- Enables keyboard listeners
- Creates:
  - Snake
  - Food
  - Scoreboard

---

### 2️⃣ Main Game Loop

The game continuously:

- Updates the screen
- Moves the snake
- Checks food collision
- Checks wall collision
- Checks self collision
- Updates the score

---

### 3️⃣ Eating Food

Whenever the snake touches the food:

- Food moves to a new random location
- Snake grows by one segment
- Score increases
- High score updates if necessary

---

### 4️⃣ Collision Detection

The game detects:

✅ Wall collision

- Snake touches screen boundary

✅ Self collision

- Snake touches its own body

Instead of closing the game, it automatically resets while preserving the high score.

---

# 🎮 Controls

| Key | Action |
|------|--------|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/snake-game-python.git
```

---

## 2. Navigate to the Project

```bash
cd snake-game-python
```

---

## 3. Run the Game

```bash
python main.py
```

---

# 💾 High Score System

The game stores the highest score inside:

```
data.txt
```

Unlike many beginner Snake games, the high score is **persistent**, meaning it remains saved even after closing the game.

---

# 📸 Game Mechanics

| Event | Result |
|--------|--------|
| Snake eats food | Snake grows |
| Snake hits wall | Game resets |
| Snake hits itself | Game resets |
| New high score | Saved automatically |
| Restart | High score remains |

---

# 🌟 Learning Outcomes

This project demonstrates:

- Object-Oriented Programming (OOP)
- Class Design
- Python Modules
- Turtle Graphics
- Event Handling
- Collision Detection
- File Handling
- Game Loops
- Keyboard Input
- Random Position Generation
- Code Organization
- Modular Programming

---

# 📈 Possible Improvements

Future enhancements could include:

- 🔊 Sound effects
- 🎵 Background music
- 🎯 Multiple difficulty levels
- ⏸ Pause / Resume functionality
- 💣 Obstacles
- ⚡ Power-ups
- 🌙 Dark / Light themes
- 🏅 Achievement system
- 🥇 Online leaderboard
- 🎨 Improved graphics
- 🕹 Start menu
- 💖 Multiple lives
- 📱 Pygame version

---

# 🤝 Contributing

Contributions are always welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/YourFeature
```

3. Commit your changes

```bash
git commit -m "Add Your Feature"
```

4. Push the branch

```bash
git push origin feature/YourFeature
```

5. Open a Pull Request

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It helps the project reach more developers and motivates future improvements.

---

# 📜 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more details.

---

# 👨‍💻 Author

**Prem Kumar**

GitHub: https://github.com/yourusername

---

<p align="center">
  <b>Made with ❤️ using Python and Turtle Graphics</b>
</p>
