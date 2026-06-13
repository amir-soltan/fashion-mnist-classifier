# FashionMNIST Image Classifier

A Convolutional Neural Network (CNN) built with PyTorch to classify clothing items from the FashionMNIST dataset.

## Project Overview

This project demonstrates how deep learning can be used for image classification. The model is trained on the FashionMNIST dataset and predicts one of ten clothing categories from grayscale images.

## Dataset

FashionMNIST contains:

- 60,000 training images
- 10,000 testing images
- 10 classes
- 28×28 grayscale images

### Classes

- T-shirt/top
- Trouser
- Pullover
- Dress
- Coat
- Sandal
- Shirt
- Sneaker
- Bag
- Ankle boot

## Technologies Used

- Python
- PyTorch
- Torchvision
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Structure

```text
fashion-mnist-classifier/
│
├── notebooks/
│   └── FashionMNIST_Classification.ipynb
│
├── src/
│   ├── vision_data.py
│   └── helper_functions.py
│
├── images/
├── results/
├── requirements.txt
└── README.md
```

## Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fashion-mnist-classifier.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/FashionMNIST_Classification.ipynb
```

## Results

Model performance metrics and visualizations will be added here.

## Future Improvements

- Data augmentation
- Hyperparameter tuning
- Model comparison experiments
- Model deployment using Streamlit

## Author

Your Name