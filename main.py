import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Define the training set
training_data = np.array([
    [1, 1, 1, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 0, 1, 1, 1]
], dtype=np.float32)

# Define the target outputs for training
target_outputs = np.array([
    [1],
    [1],
    [0],
    [0],
    [1],
    [1],
    [1],
    [1],
    [0],
    [0],
    [0],
    [0],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1],
    [1]
], dtype=np.float32)

# Create the neural network model
model = Sequential()
model.add(Dense(16, input_dim=5, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(training_data, target_outputs, epochs=1000, verbose=0)

# Testing set
testing_data = np.array([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1]
], dtype=np.float32)

# Predict the outputs for the testing set
predictions = model.predict(testing_data)

# Round the predicted outputs to 0 or 1
rounded_predictions = np.round(predictions)

# Print the predictions
for i, prediction in enumerate(rounded_predictions):
    print(f"Input: {testing_data[i]} - Predicted Output: {prediction[0]}")
