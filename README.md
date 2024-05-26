# Rugby Scrummage Simulator

This project is a Rugby Scrummage Simulator that calculates and visualizes the forces exerted by two players during a scrummage. The simulator uses a graphical user interface (GUI) built with Tkinter and plots the results using Matplotlib.

## Fun fact : I coded this program in french with mostly french text and variable names.
## Features

- **Input Coordinates:** Users can input coordinates for various body parts of two players.
- **Force Calculation:** Calculates the resultant forces exerted by each player.
- **Simulation Results:** Determines the winner based on the forces exerted.
- **Visualization:** Plots the positions and forces on a graph.
- **Example Values:** Provides default example values for quick simulations.
- **Clear Values:** Allows users to clear all input fields.

## Requirements

- Python 3.x
- Numpy
- Matplotlib
- Tkinter

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rugby-scrummage-simulator.git
   cd rugby-scrummage-simulator
   ```

2. Install the required packages:
   ```bash
   pip install numpy matplotlib
   ```

## Usage

Run the script to launch the GUI:
```bash
python scrummage_simulator.py
```

### GUI Layout

- **X and Y Labels:** Columns for X and Y coordinates for each body part.
- **Coordinate Inputs:** Rows for entering coordinates of toe, ankle, knee, hip, shoulder, weight, height, and initial impulse for both players.
- **Simulate Button:** Starts the simulation and displays the results.
- **Clear All Values Button:** Clears all input fields.
- **Use Example Values Button:** Fills the input fields with predefined example values.

### Example Simulation

1. Launch the GUI.
2. Enter coordinates for the players or click "Use Example Values" to auto-fill.
3. Click "Simulate" to run the simulation.
4. The results will be printed in the console, and a plot will display the forces and positions.

## Code Overview

### Classes and Functions

- **Joueur Class:**
  - Initializes player attributes and calculates angles between body parts.

- **Simulation Functions:**
  - `simuler_ruck`: Simulates the ruck, calculating forces and determining the winner.
  - `definir_longueur_fleche`: Normalizes and sets the length of force arrows.
  - `angle_between`: Calculates the angle between two vectors.

- **GUI Functions:**
  - `utiliser_valeur_exemple1`: Fills the input fields with example values for player 1.
  - `utiliser_valeur_exemple2`: Fills the input fields with example values for player 2.
  - `simuler_mele`: Retrieves input values, creates player objects, runs the simulation, and plots the results.
  - `clear_all_entries`: Clears all input fields.

### Visualization

- **Matplotlib Plots:**
  - Plots the positions of the body parts and the forces exerted by each player.
  - Annotates each body part for better visualization.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by the dynamics of rugby scrummaging.
- Utilizes mathematical principles for force and angle calculations.

## Contributors
- @Thomas Peyrissaguet

