"""
Jairus Martinez
Date: 1-25-25

This is an mlflow experiment that tracks the results of 3 different models:
1. NN - 1 Hidden Layer, 4 Neurons
2. NN - 2 Hidden Layers, 64 Neurons Each
3. CNN

I have an experimental Jupyter Notebook with more detail for the CNN implementation, the theory behind its approach,
and the inuition behind the different architectual choices. That code has extensive comments and markdown on these details.

For this module, the goal was to spin up an mlflow experment for tracking all 3 models, abstract the data pre-processing
for the two model types (NN/CNN), and then train, evaluate, and log the results in a reproducible way. Therefore the code here
is straight to the point and streamlines the original EDA/dev training.
"""

import logging

import numpy as np

import mlflow
from mlflow.models.signature import infer_signature
from keras.src.callbacks.history import History

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

def plot_results(history: History, model_name: str):
    """
    Plots model accuracy vs epoch AND model loss vs epoch (for train and validation data).
    Args:
        history (Keras History Object): This is the Keras's History object returned when running model.fit()
        model_name (str): Name of the model that will correspond with plot PNG name
    Returns:
        None 
    """
    # training & validation accuracy values
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Train Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Model Accuracy vs Epochs')
    plt.ylabel('Accuracy')
    plt.xlabel('Epochs')
    plt.legend(loc='upper left')

    # training & validation loss values
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss vs Epochs')
    plt.ylabel('Loss')
    plt.xlabel('Epochs')
    plt.legend(loc='upper left')

    plt.tight_layout()

    plt.savefig(f"{model_name}.png")
    mlflow.log_artifact(f"{model_name}.png")

def preprocess_nn_data(path: str) -> tuple:
    """
    Preprocess the protein data for the neural networks.
    Args:
        path (str): Path to Numpy Npz protein data
    Returns:
        (tuple): X_train, X_val, X_test, y_train, y_val, y_test
    """
    # download and prep the data
    protein_data = np.load(path)

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        protein_data["positions"], protein_data["labels"], test_size=0.1
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=0.2
    )

    # format train set
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1] * X_train.shape[2]))
    y_train = to_categorical(y_train - 1)

    # format val set
    X_val = X_val.reshape((X_val.shape[0], X_val.shape[1] * X_val.shape[2]))
    y_val = to_categorical(y_val - 1)

    # format test set
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1] * X_test.shape[2]))
    y_test = to_categorical(y_test - 1)

    logging.info("NN Data Shapes:")
    logging.info(f"X_train: {X_train.shape}")
    logging.info(f"y_train: {y_train.shape}")
    logging.info(f"X_val: {X_val.shape}")
    logging.info(f"y_val: {y_val.shape}")
    logging.info(f"X_test: {X_test.shape}")
    logging.info(f"y_test: {y_test.shape}")

    return X_train, X_val, X_test, y_train, y_val, y_test


def preprocess_cnn_data(path: str) -> tuple:
    """
    Preprocess the protein data for the convolutional neural network.
    The experimental notebook has more details/comments on the intuition
    and reasoning for the model architecture.
    Args:
        path (str): Path to Numpy Npz protein data
    Returns:
        (tuple): X_train, X_val, X_test, y_train, y_val, y_test
    """
    # download data
    protein_data = np.load(path)

    # add spatial/channel dims
    tensor_positions = tf.convert_to_tensor(protein_data["positions"], dtype=tf.float32)
    tensor_positions = tf.expand_dims(tensor_positions, axis=-1)
    tensor_positions = tf.expand_dims(tensor_positions, axis=2)

    tensor_labels = tf.convert_to_tensor(protein_data["labels"], dtype=tf.int32)
    tensor_labels = tf.keras.utils.to_categorical(tensor_labels - 1, num_classes=3)

    # convert tensors temporarily to ndarrays to work with train_test_split
    np_positions = tensor_positions.numpy()
    np_labels = tensor_labels.numpy()

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        np_positions, np_labels, test_size=0.1
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=0.2
    )

    # convert ndarrays back to tensors for CNN
    X_train = tf.convert_to_tensor(X_train)
    y_train = tf.convert_to_tensor(y_train)

    X_val = tf.convert_to_tensor(X_val)
    y_val = tf.convert_to_tensor(y_val)

    X_test = tf.convert_to_tensor(X_test)
    y_test = tf.convert_to_tensor(y_test)

    logging.info("CNN Data Shapes:")
    logging.info(f"X_train: {X_train.shape}")
    logging.info(f"y_train: {y_train.shape}")
    logging.info(f"X_val: {X_val.shape}")
    logging.info(f"y_val: {y_val.shape}")
    logging.info(f"X_test: {X_test.shape}")
    logging.info(f"y_test: {y_test.shape}")

    return X_train, X_val, X_test, y_train, y_val, y_test


# Note:
# to start tracking in mlflow, you need to start the mlflow server by running the following in the CLI
# mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow-artifacts --host 0.0.0.0 --port 5001
# open localhost and then run this module

mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("PROTEIN_NN_CNN")

if __name__ == "__main__":
    # nn-specific data pre-processed data
    X_train, X_val, X_test, y_train, y_val, y_test = preprocess_nn_data(
        "cath_3class_ca.npz"
    )
    signature = infer_signature(X_train, y_train)

    # Experiment 1: Basic Neural Network with one Layer
    with mlflow.start_run(run_name="Basic NN - One Layer"):
        model = keras.Sequential(
            [layers.Dense(4, activation="relu"), layers.Dense(3, activation="softmax")]
        )
        model.compile(
            optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
        )

        mlflow.log_param("hidden_layers", 1)
        mlflow.log_param("neurons", 4)
        mlflow.log_param("hidden_layer_activations", "relu")
        mlflow.log_param("output_layer_activation", "softmax")
        mlflow.log_param("optimizer", "rmsprop")
        mlflow.log_param("loss_function", "categorical_crossentropy")

        history = model.fit(
            X_train, y_train, epochs=20, batch_size=128, validation_data=(X_val, y_val)
        )

        plot_results(history, "nn_single__1")

        mlflow.log_param("epochs", 20)
        mlflow.log_param("batch_size", 128)

        test_loss, test_accuracy = model.evaluate(X_test, y_test)
        mlflow.log_metric("test_accuracy", test_accuracy)
        mlflow.log_metric("test_loss", test_loss)

        mlflow.keras.log_model(model, "nn_single__1", signature=signature)

        mlflow.end_run()

    # Experiment 2: Basic Neural Network, 2 Hidden layers
    with mlflow.start_run(run_name="Basic NN - Two Layers"):
        model = keras.Sequential(
            [
                layers.Dense(64, activation="relu"),
                layers.Dense(64, activation="relu"),
                layers.Dense(3, activation="softmax"),
            ]
        )
        model.compile(
            optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
        )

        mlflow.log_param("hidden_layers", 2)
        mlflow.log_param("neurons_per_layer", 64)
        mlflow.log_param("hidden_layer_activations", "relu")
        mlflow.log_param("output_layer_activation", "softmax")
        mlflow.log_param("optimizer", "rmsprop")
        mlflow.log_param("loss_function", "categorical_crossentropy")

        history = model.fit(
            X_train, y_train, epochs=20, batch_size=128, validation_data=(X_val, y_val)
        )

        plot_results(history, "nn_double__2")

        mlflow.log_param("epochs", 20)
        mlflow.log_param("batch_size", 128)

        test_loss, test_accuracy = model.evaluate(X_test, y_test)
        mlflow.log_metric("test_accuracy", test_accuracy)
        mlflow.log_metric("test_loss", test_loss)

        mlflow.keras.log_model(model, "nn_double__2", signature=signature)

        mlflow.end_run()

    # cnn-specific data pre-processed data (overwrite nn vars)
    X_train, X_val, X_test, y_train, y_val, y_test = preprocess_cnn_data(
        "cath_3class_ca.npz"
    )
    signature = infer_signature(X_train, y_train)

    # Experiment 3: CNN
    with mlflow.start_run(run_name="CNN"):
        model = keras.Sequential(
            [
                layers.Input(shape=(1202, 1, 3, 1)),
                layers.Conv3D(
                    filters=32, kernel_size=(3, 1, 3), activation="relu", padding="same"
                ),
                layers.MaxPooling3D(pool_size=(2, 1, 1), padding="same"),
                layers.Conv3D(
                    filters=64, kernel_size=(3, 1, 3), activation="relu", padding="same"
                ),
                layers.MaxPooling3D(pool_size=(2, 1, 1), padding="same"),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dense(64, activation="relu"),
                layers.Dense(3, activation="softmax"),
            ]
        )
        model.compile(
            optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
        )

        mlflow.log_param("model_type", "CNN")
        mlflow.log_param("input_shape", (1202, 1, 3, 1))
        mlflow.log_param("conv_layers", 2)
        mlflow.log_param("dense_layers", 3)
        mlflow.log_param("optimizer", "adam")
        mlflow.log_param("loss_function", "categorical_crossentropy")

        history = model.fit(
            X_train, y_train, validation_data=(X_val, y_val), epochs=20, batch_size=128
        )

        plot_results(history, "cnn__3")

        mlflow.log_param("epochs", 20)
        mlflow.log_param("batch_size", 128)

        test_loss, test_accuracy = model.evaluate(X_test, y_test)
        mlflow.log_metric("test_accuracy", test_accuracy)
        mlflow.log_metric("test_loss", test_loss)

        mlflow.keras.log_model(model, "cnn__3", signature=signature)

        mlflow.end_run()
