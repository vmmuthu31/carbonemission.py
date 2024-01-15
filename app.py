from flask import Flask, render_template
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('path_to_your_csv/Agrofood_co2_emission.csv')

@app.route('/')
def index():
    # The main page of the application
    return render_template('index.html')

@app.route('/heatmap')
def heatmap():
    # Route for heatmap visualization
    heatmap_img = generate_heatmap()
    return render_template('heatmap.html', heatmap_image=heatmap_img)

def generate_heatmap():
    # Function to create a heatmap
    plt.figure(figsize=(12,12))
    sns.heatmap(df.corr(), annot=True, fmt="1.1f")
    heatmap_path = 'static/heatmap.png'
    plt.savefig(heatmap_path)
    plt.close()  # Close the plot to free up memory
    return heatmap_path

if __name__ == '__main__':
    # Ensure the 'static' folder exists
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)
