---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/speech_emotion_tensorflow/
title: Speech Emotion Recognition using Apache Beam \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:26:56.870986+00:00
---

# Speech Emotion Recognition using Apache Beam  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/speech_emotion_tensorflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Speech Emotion Recognition using Apache Beam Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/speech_emotion_tensorflow.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/speech_emotion_tensorflow.ipynb) Speech Emotion Classification is a machine learning technique that deciphers emotions from audio data. It involves data augmentation, feature extraction, preprocessing and training an appropriate model. For structured workflow design, Apache Beam is a suitable tool. This notebook showcases Apache Beam's use in speech emotion classification and achieves the following:

  * Imports and processes the CREMA-D dataset for speech emotion analysis.
  * Perform various data augmentation and feature extraction techniques using the [Librosa](https://librosa.org/doc/latest/index.html) library.
  * Develops a TensorFlow model to classify emotions.
  * Stores the trained model.
  * Constructs a Beam pipeline that: 
    * Creates a PCollection of audio samples.
    * Applies preprocessing transforms.
    * Utilizes the trained model to predict emotions.
    * Stores the emotion predictions.

For more insights into leveraging Apache Beam for machine learning pipelines, explore [AI/ML Pipelines using Beam](https://beam.apache.org/documentation/ml/overview/).

## Installing Apache Beam
    
    
    pip install apache_beam[interactive] --quiet

## Importing necessary libraries

Here is a brief overview of the libraries imported:

  * **[os](https://docs.python.org/3/library/os.html)** : Used for file and directory operations.
  * **[NumPy](https://numpy.org/doc/stable/)** : Allows efficient numerical manipulation of arrays.
  * **[Pandas](https://pandas.pydata.org/docs/)** : Facilitates data manipulation and analysis.
  * **[Librosa](https://librosa.org/doc/latest/index.html)** : Provides tools for analyzing and working with audio data.
  * **[IPython](https://ipython.readthedocs.io/en/stable/index.html)** : Creates visualizations for multimedia content. Here we have used it for playing audio files.
  * **[Sklearn](https://scikit-learn.org/stable/index.html)** : Offers comprehensive tools for Machine Learning. Here we have used it for preprocessing and splitting the data.
  * **[TensorFlow](https://www.tensorflow.org/api_docs)** and **[Keras](https://keras.io/api/)** : Enables building and training complex Machine Learning and Deep Learning model.
  * **[TFModelHandlerNumpy](https://beam.apache.org/documentation/ml/about-ml/#tensorflow)** : Defines the configuration used to load/use the model that we train. We use TFModelHandlerNumpy because the model was trained with TensorFlow and takes numpy arrays as input.
  * **[RunInference](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.html#apache_beam.ml.inference.RunInference)** : Loads the model and obtains predictions as part of the Apache Beam pipeline. For more information, see docs on prediction and inference.
  * **[Apache Beam](https://beam.apache.org/documentation/)** : Builds a pipeline for Image Processing.


    
    
    import os
    
    import numpy as np
    import pandas as pd
    
    import librosa
    from IPython.display import Audio
    
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow.python.keras.callbacks import EarlyStopping, ReduceLROnPlateau
    
    from keras import layers
    from keras import models
    from keras.utils import np_utils
    from keras.models import Sequential
    from keras.utils import np_utils, to_categorical
    from keras.callbacks import ModelCheckpoint
    
    from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerNumpy
    from apache_beam.ml.inference.base import RunInference
    import apache_beam as beam
    

## Importing dataset from Google Drive

[CREMA-D](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4313618/) is a dataset that contains a collection of 7442 audio recordings of actors portraying different emotions. The dataset can be downloaded from [Kaggle](https://www.kaggle.com/datasets/ejlok1/cremad). As it is large in size, it will be inconvenient to upload it on Colab every time we want to run the notebook. Instead, we have uploaded the dataset on Google Drive after downloading it from Kaggle. Then we can access it directly using Colab. Please ensure if you are following this method, then your Colab notebook must be created with the same Google account in which the folder is stored.
    
    
    from google.colab import drive
    drive.mount('/content/gdrive', force_remount=True)
    
    
    
    Mounted at /content/gdrive
    

Here we create a path for the folder in Google Drive containing the audios to access them.
    
    
    root_dir = "/content/gdrive/My Drive/"
    Crema = root_dir + 'CREMA/'
    

Using the os library, we can list all the audio files in the Google Drive folder
    
    
    os.chdir(Crema)
    os.listdir()[:10] # Listing the first 10 audio files
    
    
    
    ['1079_TIE_NEU_XX.wav',
     '1079_TIE_SAD_XX.wav',
     '1079_TSI_ANG_XX.wav',
     '1079_TSI_DIS_XX.wav',
     '1079_TSI_HAP_XX.wav',
     '1079_TSI_FEA_XX.wav',
     '1079_TSI_NEU_XX.wav',
     '1079_TSI_SAD_XX.wav',
     '1079_WSI_ANG_XX.wav',
     '1079_WSI_DIS_XX.wav']
    

## Creating a DataFrame

We will create a DataFrame with two columns, path and emotion:

  * Path: This will contain the path to a specific audio file in the directory.
  * Emotion: This is the label which will state the emotion of an audio file.

The emotion can be extracted from the audio file name.
    
    
    emotion_df = []
    
    for wav in os.listdir(Crema):
        info = wav.partition(".wav")[0].split("_")
        if (len(info)<3):
            continue;
        if info[2] == 'SAD':
            emotion_df.append(("sad", Crema + "/" + wav))
        elif info[2] == 'ANG':
            emotion_df.append(("angry", Crema + "/" + wav))
        elif info[2] == 'DIS':
            emotion_df.append(("disgust", Crema + "/" + wav))
        elif info[2] == 'FEA':
            emotion_df.append(("fear", Crema + "/" + wav))
        elif info[2] == 'HAP':
            emotion_df.append(("happy", Crema + "/" + wav))
        elif info[2] == 'NEU':
            emotion_df.append(("neutral", Crema + "/" + wav))
    
    
    Crema_df = pd.DataFrame.from_dict(emotion_df)
    Crema_df.rename(columns={1 : "Path", 0 : "Emotion"}, inplace=True)
    
    Crema_df.head()
    

## Preprocessing

The audio files we want to use are in .wav format. However, an ML model works on numerical data. So we need to perform some preprocessing operations to extract numerical features from the audios and transform these features to a more suitable form. This will improve the performance of our model.

### Data Augmentation

This is the process of transforming existing data in various ways to generate more samples and increase model robustness. We make multiple versions of the same data item but with some differences. This allows the model to recognize a wider variety of data and reduce overfitting. We have performed the following data augmentation techniques:

  * **Noise injection** : Adds a random factor to all data items to provide some noise.
  * **Stretching** : Alters the speed of an audio, simulating variations in speech rate or tempo.
  * **Pitch Shifting** : Changes the pitch of an audio, depicting variations of speaker characteristics or musical notes.


    
    
    def noise(data):
        noise_amp = 0.035 * np.random.uniform() * np.amax(data)
        data = data + noise_amp * np.random.normal(size = data.shape[0])
        return data
    
    def stretch(data, rate = 0.8):
        return librosa.effects.time_stretch(data, rate = rate)
    
    def pitch(data, sampling_rate, pitch_factor = 0.7):
        return librosa.effects.pitch_shift(data, sr = sampling_rate, n_steps = pitch_factor)
    

### Feature Extraction

We need to extract some numerical features from the audios to feed our ML model. The [Librosa](https://librosa.org/doc/latest/index.html) library allows us to do this easily. First, we need to understand what a **mel scale** is. It is a scale of pitches that is based on the way humans perceive and discriminate between different frequencies of sound. Now, let us discuss the features we will extract from the audio:

  * **Zero Crossing Rate (ZCR)** : Measures how often the sound changes it's sign (positive or negative) over time.
  * **Chroma Short-Time Fourier Transform (STFT)** : Breaks down the audio signal into small segments (frames) and calculates the Fourier Transform for each frame, resulting in a time-frequency representation of the signal.
  * **Mel-Frequency Cepstral Coefficients (MFCC)** : A set of coefficients derived from the mel spectrogram
  * **Melspectogram** : A visual representation of the frequency content of an audio signal mapped on the mel scale.
  * **Root Mean Square** : Provides the Root Mean Square value for each frame, which is a measure of the amplitude or energy of a sound signal.

You can read more about all the features we can extract using the Librosa library [here](https://librosa.org/doc/latest/feature.html).
    
    
    def extract_features(data, sample_rate):
        # ZCR
        result = np.array([])
        zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
        result=np.hstack((result, zcr)) # stacking horizontally
    
        # Chroma STFT
        stft = np.abs(librosa.stft(data))
        chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        result = np.hstack((result, chroma_stft)) # stacking horizontally
    
        # MFCC
        mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mfcc)) # stacking horizontally
    
        # Root Mean Square
        rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
        result = np.hstack((result, rms)) # stacking horizontally
    
        # Melspectogram
        mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel)) # stacking horizontally
    
        return result
    

The function below is used to extract the features from the audio stored at a path. Then it applies the data augmentation techniques we defined previously, and extracts features for each augmented data too. This gives us three versions of a data item:

  * Normal features
  * Features from data with noise
  * Features from time stretched and pitch shifted data

These are added into our final dataset as individual samples.
    
    
    def get_features(path):
        data, sample_rate = librosa.load(path, duration=2.5, offset=0.6)
    
        # without augmentation
        normal_features = extract_features(data, sample_rate)
        result = np.array(normal_features)
    
        # data with noise
        noise_data = noise(data)
        noise_features = extract_features(noise_data, sample_rate)
        result = np.vstack((result, noise_features)) # stacking vertically
    
        # data with stretching and pitching
        stretch_data = stretch(data)
        stretch_pitch_data = pitch(stretch_data, sample_rate)
        stretch_pitch_features = extract_features(stretch_pitch_data, sample_rate)
        result = np.vstack((result, stretch_pitch_features)) # stacking vertically
    
        return result
    

Now we will iterate through the Crema_df DataFrame containing the path and emotion of each audio sample. We will extract features for each audio's three versions, add it to X, and add the corresponding emotion to Y.
    
    
    X, Y = [], []
    for path, emotion in zip(Crema_df.Path, Crema_df.Emotion):
        feature = get_features(path)
        for ele in feature:
            X.append(ele)
            Y.append(emotion)
    
    
    
    /usr/local/lib/python3.10/dist-packages/librosa/core/pitch.py:101: UserWarning: Trying to estimate tuning from empty frequency set.
      return pitch_tuning(
    

Here we have made a DataFrame using the lists X and Y.
    
    
    Features = pd.DataFrame(X)
    Features['labels'] = Y
    Features.to_csv('features.csv', index=False)
    Features.head()
    

The X and Y datasets are separated here. X stores the features of audio samples while Y stores the corresponding labels.
    
    
    X = Features.iloc[: ,:-1].values
    Y = Features['labels'].values
    

The [pad sequences](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences) function is used to pad the input data to the same length, to ensure that all samples have the same shape.
    
    
    X = tf.keras.utils.pad_sequences(X)
    

Scikit Learn's [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) is used to convert categorical labels into numerical data. It creates a column in the labels dataset for each category, which contains only binary data. For example, if we have the following categories: `[Anger, Disgust, Fear, Happy, Neutral, Sad]` And a specific audio belongs to 'Anger' category, then the OneHotEncoder will transform it to: `[1, 0, 0, 0, 0, 0]` Please note that the order of which column represents which category may differ.
    
    
    encoder = OneHotEncoder()
    Y = encoder.fit_transform(np.array(Y).reshape(-1,1)).toarray()
    

Splitting into train/test splits
    
    
    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0, shuffle=True)
    x_train.shape, y_train.shape, x_test.shape, y_test.shape
    
    
    
    ((16744, 162), (16744, 6), (5582, 162), (5582, 6))
    

Now we will scale the data and split it into training and testing sets.

  * [Scaling](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.scale.html) is done to make all numerical data have similar magnitudes. This makes computations easier.
  * The training sets are used to train the model.
  * The testing sets are used to test the model's accuracy.


    
    
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)
    x_train.shape, y_train.shape, x_test.shape, y_test.shape
    
    
    
    ((16744, 162), (16744, 6), (5582, 162), (5582, 6))
    
    
    
    X.shape, x_train.shape, x_test.shape
    
    
    
    ((22326, 162), (16744, 162), (5582, 162))
    

We will use a 1D Convolutional layer in our model, and for that, our input data needs to be a a 3D tensor with dimensions `(batch_size, time_steps, input_dim)`. So we will expand the dimensions of our X_train and X_test datasets. The extra 1 in the shape depicts that our data is 1 dimensional.
    
    
    x_train = np.expand_dims(x_train, axis=2)
    x_test = np.expand_dims(x_test, axis=2)
    x_train.shape, y_train.shape, x_test.shape, y_test.shape
    
    
    
    ((16744, 162, 1), (16744, 6), (5582, 162, 1), (5582, 6))
    

### Training the model

We will build a sequential model to classify speech emotions using TensorFlow and Keras. Here is an overview of the layers used:

  * **Conv1D** : Applies a set of filters to capture patterns in sequential data like time series or audio, enabling feature extraction through sliding convolutions.
  * **Activation** : Introduces non-linearity by applying an element-wise activation function to the input, enhancing the network's learning capacity.
  * **BatchNormalization** : Normalizes input activations within a mini-batch, accelerating training by stabilizing and improving gradient flow.
  * **Dropout** : Randomly deactivates a fraction of neurons during training, reducing overfitting by promoting generalization.
  * **MaxPooling1D** : Downsamples the input by retaining the maximum value in each local region, reducing computation.
  * **Flatten** : Reshapes input data from a multidimensional format into a 1D vector, suitable for fully connected layers.
  * **Dense** : Connects each neuron to every neuron in the previous layer, allowing complex relationships to be learned during training.

In the end, we need probabilities for each of the 6 classes of emotions, so we need 6 outputs. This is why the last Dense layer returns an array of size 6.
    
    
    model = Sequential()
    model.add(layers.Conv1D(256, 6, padding='same',input_shape=(x_train.shape[1],1)))
    model.add(layers.Activation('relu'))
    model.add(layers.Conv1D(256, 6, padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.MaxPooling1D(pool_size=(8)))
    model.add(layers.Conv1D(128, 6, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Conv1D(128, 6, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Conv1D(128, 6, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Conv1D(128, 6, padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.MaxPooling1D(pool_size=(8)))
    model.add(layers.Conv1D(64, 6, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Conv1D(64, 6, padding='same'))
    model.add(layers.Activation('relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Flatten())
    model.add(layers.Dense(6))
    model.add(layers.Activation('softmax'))
    opt = keras.optimizers.Adam(learning_rate=0.0001)
    model.summary()
    
    
    
    Model: "sequential"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     conv1d (Conv1D)             (None, 162, 256)          1792      
                                                                     
     activation (Activation)     (None, 162, 256)          0         
                                                                     
     conv1d_1 (Conv1D)           (None, 162, 256)          393472    
                                                                     
     batch_normalization (BatchN  (None, 162, 256)         1024      
     ormalization)                                                   
                                                                     
     activation_1 (Activation)   (None, 162, 256)          0         
                                                                     
     dropout (Dropout)           (None, 162, 256)          0         
                                                                     
     max_pooling1d (MaxPooling1D  (None, 20, 256)          0         
     )                                                               
                                                                     
     conv1d_2 (Conv1D)           (None, 20, 128)           196736    
                                                                     
     activation_2 (Activation)   (None, 20, 128)           0         
                                                                     
     conv1d_3 (Conv1D)           (None, 20, 128)           98432     
                                                                     
     activation_3 (Activation)   (None, 20, 128)           0         
                                                                     
     dropout_1 (Dropout)         (None, 20, 128)           0         
                                                                     
     conv1d_4 (Conv1D)           (None, 20, 128)           98432     
                                                                     
     activation_4 (Activation)   (None, 20, 128)           0         
                                                                     
     conv1d_5 (Conv1D)           (None, 20, 128)           98432     
                                                                     
     batch_normalization_1 (Batc  (None, 20, 128)          512       
     hNormalization)                                                 
                                                                     
     activation_5 (Activation)   (None, 20, 128)           0         
                                                                     
     dropout_2 (Dropout)         (None, 20, 128)           0         
                                                                     
     max_pooling1d_1 (MaxPooling  (None, 2, 128)           0         
     1D)                                                             
                                                                     
     conv1d_6 (Conv1D)           (None, 2, 64)             49216     
                                                                     
     activation_6 (Activation)   (None, 2, 64)             0         
                                                                     
     conv1d_7 (Conv1D)           (None, 2, 64)             24640     
                                                                     
     activation_7 (Activation)   (None, 2, 64)             0         
                                                                     
     dropout_3 (Dropout)         (None, 2, 64)             0         
                                                                     
     flatten (Flatten)           (None, 128)               0         
                                                                     
     dense (Dense)               (None, 6)                 774       
                                                                     
     activation_8 (Activation)   (None, 6)                 0         
                                                                     
    =================================================================
    Total params: 963,462
    Trainable params: 962,694
    Non-trainable params: 768
    _________________________________________________________________
    

Now we will compile the model.
    
    
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
    

Next, we will train our model. [ReduceLROnPlateau](https://keras.io/api/callbacks/reduce_lr_on_plateau/) is used to reduce the learning rate when the loss has stopped improving. [EarlyStopping](https://keras.io/api/callbacks/early_stopping/) monitors the val_loss and stops the training process when it doesn't improve.
    
    
    rlrp = ReduceLROnPlateau(monitor='loss', factor=0.4, verbose=0, patience=2, min_lr=0.0000001)
    es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=20)
    
    model.fit(x_train, y_train, batch_size=16, epochs=100, validation_data=(x_test, y_test), callbacks=[es, rlrp])
    
    
    
    Epoch 1/100
    1047/1047 [==============================] - 29s 13ms/step - loss: 1.5803 - accuracy: 0.3272 - val_loss: 1.5216 - val_accuracy: 0.3739 - lr: 1.0000e-04
    Epoch 2/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.4870 - accuracy: 0.3807 - val_loss: 1.5065 - val_accuracy: 0.3884 - lr: 1.0000e-04
    Epoch 3/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 1.4541 - accuracy: 0.3952 - val_loss: 1.4635 - val_accuracy: 0.3954 - lr: 1.0000e-04
    Epoch 4/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.4253 - accuracy: 0.4105 - val_loss: 1.4341 - val_accuracy: 0.4282 - lr: 1.0000e-04
    Epoch 5/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.4092 - accuracy: 0.4199 - val_loss: 1.4595 - val_accuracy: 0.4077 - lr: 1.0000e-04
    Epoch 6/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.3890 - accuracy: 0.4299 - val_loss: 1.4032 - val_accuracy: 0.4317 - lr: 1.0000e-04
    Epoch 7/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.3709 - accuracy: 0.4471 - val_loss: 1.3958 - val_accuracy: 0.4294 - lr: 1.0000e-04
    Epoch 8/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 1.3613 - accuracy: 0.4482 - val_loss: 1.4311 - val_accuracy: 0.4102 - lr: 1.0000e-04
    Epoch 9/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.3420 - accuracy: 0.4563 - val_loss: 1.3901 - val_accuracy: 0.4409 - lr: 1.0000e-04
    Epoch 10/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.3292 - accuracy: 0.4643 - val_loss: 1.3893 - val_accuracy: 0.4434 - lr: 1.0000e-04
    Epoch 11/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.3162 - accuracy: 0.4689 - val_loss: 1.3742 - val_accuracy: 0.4482 - lr: 1.0000e-04
    Epoch 12/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.3033 - accuracy: 0.4738 - val_loss: 1.3821 - val_accuracy: 0.4507 - lr: 1.0000e-04
    Epoch 13/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 1.2889 - accuracy: 0.4833 - val_loss: 1.3452 - val_accuracy: 0.4609 - lr: 1.0000e-04
    Epoch 14/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 1.2715 - accuracy: 0.4933 - val_loss: 1.3690 - val_accuracy: 0.4559 - lr: 1.0000e-04
    Epoch 15/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.2642 - accuracy: 0.4916 - val_loss: 1.3460 - val_accuracy: 0.4618 - lr: 1.0000e-04
    Epoch 16/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.2439 - accuracy: 0.5028 - val_loss: 1.3293 - val_accuracy: 0.4719 - lr: 1.0000e-04
    Epoch 17/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.2287 - accuracy: 0.5073 - val_loss: 1.3309 - val_accuracy: 0.4663 - lr: 1.0000e-04
    Epoch 18/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.2193 - accuracy: 0.5122 - val_loss: 1.3353 - val_accuracy: 0.4686 - lr: 1.0000e-04
    Epoch 19/100
    1047/1047 [==============================] - 13s 13ms/step - loss: 1.2044 - accuracy: 0.5237 - val_loss: 1.3370 - val_accuracy: 0.4636 - lr: 1.0000e-04
    Epoch 20/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.1869 - accuracy: 0.5258 - val_loss: 1.3021 - val_accuracy: 0.4805 - lr: 1.0000e-04
    Epoch 21/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.1744 - accuracy: 0.5288 - val_loss: 1.3028 - val_accuracy: 0.4807 - lr: 1.0000e-04
    Epoch 22/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.1574 - accuracy: 0.5376 - val_loss: 1.3189 - val_accuracy: 0.4717 - lr: 1.0000e-04
    Epoch 23/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.1437 - accuracy: 0.5492 - val_loss: 1.3197 - val_accuracy: 0.4694 - lr: 1.0000e-04
    Epoch 24/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.1234 - accuracy: 0.5563 - val_loss: 1.3482 - val_accuracy: 0.4678 - lr: 1.0000e-04
    Epoch 25/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.1152 - accuracy: 0.5568 - val_loss: 1.3050 - val_accuracy: 0.4821 - lr: 1.0000e-04
    Epoch 26/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 1.1022 - accuracy: 0.5677 - val_loss: 1.2853 - val_accuracy: 0.4867 - lr: 1.0000e-04
    Epoch 27/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.0844 - accuracy: 0.5678 - val_loss: 1.2719 - val_accuracy: 0.4925 - lr: 1.0000e-04
    Epoch 28/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.0644 - accuracy: 0.5828 - val_loss: 1.2978 - val_accuracy: 0.4798 - lr: 1.0000e-04
    Epoch 29/100
    1047/1047 [==============================] - 14s 14ms/step - loss: 1.0524 - accuracy: 0.5882 - val_loss: 1.2986 - val_accuracy: 0.4844 - lr: 1.0000e-04
    Epoch 30/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 1.0364 - accuracy: 0.5920 - val_loss: 1.2919 - val_accuracy: 0.4894 - lr: 1.0000e-04
    Epoch 31/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 1.0160 - accuracy: 0.6043 - val_loss: 1.2651 - val_accuracy: 0.4937 - lr: 1.0000e-04
    Epoch 32/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 1.0056 - accuracy: 0.6058 - val_loss: 1.2905 - val_accuracy: 0.4841 - lr: 1.0000e-04
    Epoch 33/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.9838 - accuracy: 0.6154 - val_loss: 1.2708 - val_accuracy: 0.4955 - lr: 1.0000e-04
    Epoch 34/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.9778 - accuracy: 0.6135 - val_loss: 1.2651 - val_accuracy: 0.5032 - lr: 1.0000e-04
    Epoch 35/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.9610 - accuracy: 0.6234 - val_loss: 1.3275 - val_accuracy: 0.4751 - lr: 1.0000e-04
    Epoch 36/100
    1047/1047 [==============================] - 13s 13ms/step - loss: 0.9461 - accuracy: 0.6349 - val_loss: 1.2683 - val_accuracy: 0.4971 - lr: 1.0000e-04
    Epoch 37/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 0.9443 - accuracy: 0.6332 - val_loss: 1.2852 - val_accuracy: 0.4923 - lr: 1.0000e-04
    Epoch 38/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.9169 - accuracy: 0.6452 - val_loss: 1.2813 - val_accuracy: 0.4961 - lr: 1.0000e-04
    Epoch 39/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.9133 - accuracy: 0.6436 - val_loss: 1.2613 - val_accuracy: 0.5050 - lr: 1.0000e-04
    Epoch 40/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.8981 - accuracy: 0.6509 - val_loss: 1.2701 - val_accuracy: 0.5084 - lr: 1.0000e-04
    Epoch 41/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.8874 - accuracy: 0.6515 - val_loss: 1.2848 - val_accuracy: 0.4928 - lr: 1.0000e-04
    Epoch 42/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.8712 - accuracy: 0.6620 - val_loss: 1.2626 - val_accuracy: 0.5052 - lr: 1.0000e-04
    Epoch 43/100
    1047/1047 [==============================] - 15s 14ms/step - loss: 0.8702 - accuracy: 0.6597 - val_loss: 1.2687 - val_accuracy: 0.5109 - lr: 1.0000e-04
    Epoch 44/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.8500 - accuracy: 0.6694 - val_loss: 1.2604 - val_accuracy: 0.5133 - lr: 1.0000e-04
    Epoch 45/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.8305 - accuracy: 0.6759 - val_loss: 1.2698 - val_accuracy: 0.5122 - lr: 1.0000e-04
    Epoch 46/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.8266 - accuracy: 0.6805 - val_loss: 1.2949 - val_accuracy: 0.5043 - lr: 1.0000e-04
    Epoch 47/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.8132 - accuracy: 0.6860 - val_loss: 1.2778 - val_accuracy: 0.5021 - lr: 1.0000e-04
    Epoch 48/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.7994 - accuracy: 0.6940 - val_loss: 1.2740 - val_accuracy: 0.5091 - lr: 1.0000e-04
    Epoch 49/100
    1047/1047 [==============================] - 13s 13ms/step - loss: 0.7836 - accuracy: 0.6936 - val_loss: 1.2925 - val_accuracy: 0.5070 - lr: 1.0000e-04
    Epoch 50/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.7757 - accuracy: 0.7038 - val_loss: 1.3190 - val_accuracy: 0.5011 - lr: 1.0000e-04
    Epoch 51/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 0.7679 - accuracy: 0.7001 - val_loss: 1.2861 - val_accuracy: 0.5027 - lr: 1.0000e-04
    Epoch 52/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.7542 - accuracy: 0.7114 - val_loss: 1.3435 - val_accuracy: 0.4927 - lr: 1.0000e-04
    Epoch 53/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.7459 - accuracy: 0.7093 - val_loss: 1.3164 - val_accuracy: 0.5072 - lr: 1.0000e-04
    Epoch 54/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.7287 - accuracy: 0.7193 - val_loss: 1.2878 - val_accuracy: 0.5188 - lr: 1.0000e-04
    Epoch 55/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.7178 - accuracy: 0.7262 - val_loss: 1.3178 - val_accuracy: 0.5054 - lr: 1.0000e-04
    Epoch 56/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.7076 - accuracy: 0.7258 - val_loss: 1.3746 - val_accuracy: 0.4912 - lr: 1.0000e-04
    Epoch 57/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 0.6955 - accuracy: 0.7306 - val_loss: 1.3457 - val_accuracy: 0.5097 - lr: 1.0000e-04
    Epoch 58/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.6843 - accuracy: 0.7364 - val_loss: 1.3558 - val_accuracy: 0.5000 - lr: 1.0000e-04
    Epoch 59/100
    1047/1047 [==============================] - 12s 12ms/step - loss: 0.6790 - accuracy: 0.7370 - val_loss: 1.3310 - val_accuracy: 0.5150 - lr: 1.0000e-04
    Epoch 60/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.6683 - accuracy: 0.7431 - val_loss: 1.3515 - val_accuracy: 0.5127 - lr: 1.0000e-04
    Epoch 61/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.6628 - accuracy: 0.7419 - val_loss: 1.3877 - val_accuracy: 0.4955 - lr: 1.0000e-04
    Epoch 62/100
    1047/1047 [==============================] - 12s 11ms/step - loss: 0.6462 - accuracy: 0.7501 - val_loss: 1.3549 - val_accuracy: 0.5202 - lr: 1.0000e-04
    Epoch 63/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.6305 - accuracy: 0.7597 - val_loss: 1.3709 - val_accuracy: 0.5109 - lr: 1.0000e-04
    Epoch 64/100
    1047/1047 [==============================] - 13s 12ms/step - loss: 0.6245 - accuracy: 0.7610 - val_loss: 1.3442 - val_accuracy: 0.5269 - lr: 1.0000e-04
    Epoch 00064: early stopping
    <keras.callbacks.History at 0x7a8558211bd0>
    

We can see that the accuracy of our model is not very high. This is because speech data is more complex than other forms of data and much more training data and/or preprocessing techniques are required to build a good speech emotion classifier. If you want to increase the accuracy, you can use multiple datasets instead of just one, and use more features from the Librosa library. You can also try experimenting with LSTM layers in the model. Here are some of the popular speech emotion datasets:

  * [RAVDESS](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)
  * [LSSED](https://github.com/tobefans/LSSED)
  * [TESS](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)
  * [IEMOCAP](https://www.kaggle.com/datasets/columbine/iemocap)



### Saving model in Google Cloud Bucket

In our final Beam pipeline, we will use RunInference. For that, we need to have a pretrained model stored in a location that is accessible to a model handler. Storing the model in a Google Cloud Bucket is the easiest way to do this.
    
    
    save_model_dir = '' # Add the link to you GCS bucket here
    model.save(save_model_dir)
    
    
    
    WARNING:absl:Found untraced functions such as _jit_compiled_convolution_op, _jit_compiled_convolution_op, _jit_compiled_convolution_op, _jit_compiled_convolution_op, _jit_compiled_convolution_op while saving (showing 5 of 8). These functions will not be directly callable after loading.
    

### Creating a model handler

A model handler is used to save, load and manage trained models. We have used TFModelHandlerNumpy since our model was built using TensorFlow and takes NumPy arrays as input.
    
    
    model_handler = TFModelHandlerNumpy(save_model_dir)
    

## Preprocessing functions for Beam pipeline

We need to define some functions to perform the same preprocessing tasks we did on our training data. We can't reuse the previously defined function directly since they processed multidimensional data, and in a pipeline we deal with a single data item, which requires different methods. This function loads the audio data using Librosa and extracts features using the previously defined function.
    
    
    def feature_extraction(element):
      data, sample_rate = librosa.load(path, duration=2.5, offset=0.6)
      return extract_features(data, sample_rate)
    

Here we have scaled the data using standardization. The data is transformed such that it's mean is 0 and standard deviation is 1.
    
    
    def scaling(element):
      element = (element-np.mean(element))/np.std(element)
      return element
    

In the end we will save our predictions in a list. RunInference returns an array of probabilities for each class. We select the maximum probability, replace it by 1, and replace all other values with 0. Now our new list is in a standard one hot encoded format, and we can use the inverse transform function of the OneHotEncoder to return which class the resultant array represents.
    
    
    predictions = []
    
    
    
    from tensorflow.python.ops.numpy_ops import np_config
    np_config.enable_numpy_behavior()
    def save_predictions(element):
        list_of_predictions = element.inference.tolist()
        highest_prediction = max(list_of_predictions)
        l = []
        for i in range(len(list_of_predictions)):
          if list_of_predictions[i] == highest_prediction:
            l.append(1)
          else:
            l.append(0);
        ans = encoder.inverse_transform(np.array(l).reshape(1,-1))[0][0]
        predictions.append(ans)
        print(ans)
    

## Building the Beam Pipeline

This pipeline performs the following tasks

  * Creates a PCollection of input paths
  * Extracts features using the previously defined functions
  * Performs scaling
  * Runs inference on new data using the previously trained model
  * Saves predictions in a list


    
    
    pipeline_input = Crema_df[:2].Path
    
    
    
    with beam.Pipeline() as p:
        _ = (p | beam.Create(pipeline_input)
               | beam.Map(feature_extraction)
               | beam.Map(scaling)
               | RunInference(model_handler)
               | beam.Map(save_predictions)
            )
    
    
    
    sad
    sad
    
    
    
    Crema_df[:2]
    
    
    
    from IPython.display import Audio
    Audio(Crema_df.iloc[0].Path)
    
    
    
    Audio(Crema_df.iloc[1].Path)
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
