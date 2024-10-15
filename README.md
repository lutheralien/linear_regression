# Student Score Prediction

This project implements a simple linear regression model to predict student exam scores based on the number of hours studied.

## Project Description

The script `classexample.py` uses a linear regression model to:
1. Load and preprocess student data
2. Train a model on the relationship between study hours and exam scores
3. Evaluate the model's performance
4. Predict scores for new input (hours studied)

## Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.7+
* Git (for cloning the repository)

## Installation

To set up the Student Score Prediction project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/linear_regression.git
   cd linear_regression
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install pandas scikit-learn
   ```

## Usage

To use the Student Score Prediction script:

1. Ensure you have a CSV file named `student-mat.csv` in the same directory as the script. This file should contain two columns: 'hours' (hours studied) and 'score' (exam score).

2. Run the script:
   ```
   python classexample.py
   ```

3. The script will output:
   - The Mean Squared Error of the model
   - The intercept (beta0) and slope (beta1) of the linear regression
   - A prediction for a student who studied for 12 hours

4. The prediction will also be saved to a file named `predicted_scores.txt`.

## Customizing Predictions

To predict scores for different study hours, modify the following line in `classexample.py`:

```python
hours_studied = pd.DataFrame([[12]], columns=["hours"])
```

Replace `12` with the desired number of study hours.

## Contributing

To contribute to Student Score Prediction, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact the maintainer, you can reach them at eyandilutherking2003@gmail.com.


