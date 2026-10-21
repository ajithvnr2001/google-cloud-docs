---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/nlp_tensorflow_streaming/
title: Natural Language Processing using Streaming Beam Pipeline \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:15:12.100871+00:00
---

# Natural Language Processing using Streaming Beam Pipeline  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/nlp_tensorflow_streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Natural Language Processing using Streaming Beam Pipeline Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/nlp_tensorflow_streaming.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/nlp_tensorflow_streaming.ipynb) Natural Language Processing or NLP is a field of Artifical Intelligence that enables computers to interpret and understand human language. It involves multiple steps such as applying various preprocessing functions, getting predictions from a model, storing the predictions in a useful format, etc. Sentiment Analysis is a popular use case of NLP, which allows computers to analyze the sentiment of a text. This notebook demonstrates the use of streaming pipelines in NLP.

  * Extracts comments using [Youtube API](https://developers.google.com/youtube/v3) and publishing them to Pub/Sub
  * Trains a TensorFlow model to predict the sentiment of text
  * Stores the model in Google Cloud and creates a model handler
  * Builds a Beam pipeline to: 
    1. Read data from Pub/Sub
    2. Create a [PCollection](https://beam.apache.org/documentation/programming-guide/#pcollections) of input text
    3. Perform preprocessing [transforms](https://beam.apache.org/documentation/programming-guide/#transforms)
    4. RunInference to get predictions from the previously trained model
    5. Store the results

For more information on using Apache Beam for machine learning, have a look at [AI/ML Pipelines using Beam](https://beam.apache.org/documentation/ml/overview/).

## Installing necessary libraries
    
    
    pip install apache-beam[interactive,gcp] --quiet

## Importing libraries

Here's a brief overview of the libraries we have imported and what they do:

  * **NumPy** : It provides support for multi-dimensional arrays, along with many mathematical functions to operate on these arrays efficiently.
  * **Pandas** : It allows us to work efficiently with structured or tabular data. Here we have used pandas to import a dataset from a csv file and manipulate it.
  * **TextBlob** : It is a library for processing textual data and common NLP tasks. Here we have used it to analyze comments and find their sentiment polarity.
  * **Apache Beam** : It is used to build and execute data processing pipelines.
  * **RunInference** : It uses a pretrained model to predict results for new unseen data.
  * **TFModelHandlerNumpy** : It is used to manage trained TensorFlow models that take NumPy arrays as input.


    
    
    import numpy as np
    import pandas as pd
    import tensorflow as tf
    
    from textblob import TextBlob
    
    import apache_beam as beam
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerNumpy
    from apache_beam.options import pipeline_options
    

## Sentiment Analysis

Sentiment analysis is an NLP technique used to determine the sentiment or emotion expressed in a piece of text. The goal of sentiment analysis is to identify whether the text expresses a positive, negative, or neutral sentiment towards a particular subject or topic. Our goal is to build a streaming pipeline that ultimately tells us the sentiment of YouTube comments. For that, we need to have a pretrained model that can predict the sentiment of text.

## Training a model with labeled youtube comments dataset

The dataset can be found on [Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube?select=UScomments.csv). It contains various statistics for comments on trending videos on YouTube. Since our goal is to perform a sentiment analysis on comments, we only have to consider the text.

#### Reading the data from a csv file

Pandas allows us to load data from a CSV file and convert it into a DataFrame, which makes it easy to perform data analysis and manipulation.
    
    
    comm = pd.read_csv('UScomments.csv',encoding='utf8',nrows = 1000, error_bad_lines=False)
    

The dataset has no labels, so we have used [TextBlob](https://textblob.readthedocs.io/en/dev/) to assign the appropriate labels by finding sentiment polarity. Polarity is a number between -1 to 1, which depicts the sentiment of a text. -1 represents most negative and 1 represents most positive sentiment.
    
    
    pol=[]
    for i in comm.comment_text.values:
        try:
            analysis =TextBlob(i)
            pol.append(analysis.sentiment.polarity)
    
        except:
            pol.append(0)
    

We need to convert the continuous numerical values of sentiment polarity into categorical values. We will add a new column 'pol' to the DataFrame which contains the categorical labels.

  * pol = 0 means positive comment (Sentiment polarity should be 0 or more)
  * pol = 1 means negative comment (Sentiment polarity should be less than 0)


    
    
    comm['pol']=pol
    comm['pol'][comm.pol >= 0]= 0 #positive
    comm['pol'][comm.pol < 0]= 1 #negative
    

Next, we can drop unnecessary columns from the dataset
    
    
    comm = comm.drop(['video_id','likes','replies'],axis=1)
    

### Preprocessing

Preprocessing refers to the series of steps taken to clean, transform, and prepare raw text data. This preprocessed data can easily be fed into our ML framework and provide better results.
    
    
    #Dropping null values
    comm = comm.dropna()
    
    
    
    #Removing unnecessary characters
    def remove_symbols(text):
        return text.replace("[^a-zA-Z#]", " ")
    comm['comment_text'] = comm['comment_text'].map(remove_symbols)
    
    
    
    #Removing words of length 3 or less
    def remove_short_words(text):
        return ' '.join([str(w) for w in text.split() if len(str(w))>3])
    comm['comment_text'] = comm['comment_text'].map(remove_short_words)
    
    
    
    #Converting to lowercase
    def lower_case(text):
        return text.lower()
    comm['comment_text'] = comm['comment_text'].map(lower_case)
    

Next, we will divide our dataset into 2 parts:

  * X = Array of string comments
  * Y = Polarity Category (0 or 1)

Here X is the unlabeled data which we will use for training and testing our model, and Y contains the corresponding labels.
    
    
    X = np.array(comm['comment_text'])
    Y = np.array(comm['pol'])
    

Now we need to split the data into training and testing splits. The train split will be used for training the model, and the test split will be used to check it's performance.
    
    
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    

TensorFlow's [Tokenizer](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer) is used to convert text into an array of numbers that represent it based on the frequency of each word. This is done because an ML model can't process text directly, it can only process vectors of numbers. The [fit_on_texts](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#fit_on_texts) method updates the vocabulary of the tokenizer based on the words present in the data passed to it.
    
    
    tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=10000, oov_token='<UNK>')
    tokenizer.fit_on_texts(comm['comment_text'])
    

Here we have defined a function that takes a tokenizer and array of strings as input, and returns an array of tokenized strings.

  * [texts_to_sequences](https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_sequences): Converts text to a sequence of numbers, or tokens.
  * [pad_sequences](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences): Transforms tokens of different sizes to the same size.


    
    
    maxlen=100
    def get_sequences(comments):
        sequences = tokenizer.texts_to_sequences(comments)
        padded = tf.keras.utils.pad_sequences(sequences, truncating = 'post', padding='post', maxlen=maxlen)
        return padded
    

Using the function defined aboved, now we will tokenize the X_train and X_test datasets.
    
    
    padded_seq_train = get_sequences(X_train)
    padded_seq_test = get_sequences(X_test)
    

### Building a simple TensorFlow model to predict polarity of comments

Now that we have our preprocessed training and testing data, we need to build a model. This model will take input as strings and predict which category (positive or negative) the string belongs to. Here is a brief description of the layers we have used to build this model:

  * **Embedding Layer** : It converts tokens into dense vector representations. This allows a neural network to capture semantic relationships between words and generalize better on unseen data.
  * **Bidirectional Layer** : It enhances the information flow by processing input sequences in both forward and backward directions. It is used for sequential data like natural language.
  * **Dense Layer** : It connects every neuron in the previous layer to the neurons in the next layer. The comments can either be positive or negative, so there are two categories. Thus, the Dense layer provides two outputs at the end, both of which correspond to the probabibility of the text belonging to that category.


    
    
    model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(10000,16,input_length=maxlen),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(10)),
    tf.keras.layers.Dense(2, activation='softmax')
    ])
    model.compile(
         loss='sparse_categorical_crossentropy',
         optimizer='adam',
         metrics=['accuracy']
    )
    

Next, we will create a checkpoint to save the model with the best validation accuracy.
    
    
    checkpoint_acc = tf.keras.callbacks.ModelCheckpoint("weights_acc", monitor="val_accuracy",
    save_best_only=True)
    

Now we will train our model by fitting it with the training data and using testing data for validation.
    
    
    model.fit(
         padded_seq_train, y_train,
         validation_data=(padded_seq_test, y_test),
         epochs=10,
         callbacks=checkpoint_acc
    )
    
    
    
    Epoch 1/10
    25/25 [==============================] - ETA: 0s - loss: 0.5931 - accuracy: 0.7650
    WARNING:absl:Found untraced functions such as _update_step_xla, lstm_cell_7_layer_call_fn, lstm_cell_7_layer_call_and_return_conditional_losses, lstm_cell_8_layer_call_fn, lstm_cell_8_layer_call_and_return_conditional_losses while saving (showing 5 of 9). These functions will not be directly callable after loading.
    25/25 [==============================] - 60s 2s/step - loss: 0.5931 - accuracy: 0.7650 - val_loss: 0.3625 - val_accuracy: 0.8900
    Epoch 2/10
    25/25 [==============================] - 4s 169ms/step - loss: 0.4663 - accuracy: 0.8163 - val_loss: 0.3644 - val_accuracy: 0.8900
    Epoch 3/10
    25/25 [==============================] - 3s 120ms/step - loss: 0.4550 - accuracy: 0.8163 - val_loss: 0.3663 - val_accuracy: 0.8900
    Epoch 4/10
    25/25 [==============================] - 3s 112ms/step - loss: 0.4268 - accuracy: 0.8163 - val_loss: 0.3683 - val_accuracy: 0.8900
    Epoch 5/10
    25/25 [==============================] - 3s 111ms/step - loss: 0.3700 - accuracy: 0.8238 - val_loss: 0.3266 - val_accuracy: 0.8900
    Epoch 6/10
    25/25 [==============================] - 4s 179ms/step - loss: 0.2280 - accuracy: 0.9237 - val_loss: 0.3199 - val_accuracy: 0.8450
    Epoch 7/10
    25/25 [==============================] - 4s 152ms/step - loss: 0.1034 - accuracy: 0.9825 - val_loss: 0.4166 - val_accuracy: 0.8000
    Epoch 8/10
    25/25 [==============================] - 3s 108ms/step - loss: 0.0597 - accuracy: 0.9900 - val_loss: 0.4530 - val_accuracy: 0.8500
    Epoch 9/10
    25/25 [==============================] - 3s 114ms/step - loss: 0.0311 - accuracy: 0.9962 - val_loss: 0.5967 - val_accuracy: 0.8000
    Epoch 10/10
    25/25 [==============================] - 3s 106ms/step - loss: 0.0142 - accuracy: 0.9987 - val_loss: 0.8104 - val_accuracy: 0.7800
    <keras.callbacks.History at 0x7eda55b3a4d0>
    

## Authenticating for Google cloud

We need to authenticate our google account for the following:

  * Saving the model in Google cloud
  * Publishing messages in Pub/Sub
  * Accessing previously published messages using a subscription


    
    
    from google.colab import auth
    auth.authenticate_user()
    

## Saving the model in Google cloud

We will save the model in Google Cloud so that we can easily load it using RunInference. Then it can be used to predict results for the input data in our Beam pipeline.
    
    
    model.load_weights('weights_acc')
    
    
    
    <tensorflow.python.checkpoint.checkpoint.CheckpointLoadStatus at 0x7eda3c5c42b0>
    
    
    
    save_model_dir = '' # Add the link to your GCS bucket here
    
    
    
    model.save(save_model_dir)
    
    
    
    WARNING:absl:Found untraced functions such as _update_step_xla, lstm_cell_7_layer_call_fn, lstm_cell_7_layer_call_and_return_conditional_losses, lstm_cell_8_layer_call_fn, lstm_cell_8_layer_call_and_return_conditional_losses while saving (showing 5 of 9). These functions will not be directly callable after loading.
    

## Creating a model handler

A model handler is used to save, load and manage trained ML models. Here we used TFModelHandlerNumpy as our input text is in the form of numpy arrays.
    
    
    model_handler = TFModelHandlerNumpy(save_model_dir)
    

## Understanding Pub/Sub

Google Cloud [Pub/Sub](https://cloud.google.com/pubsub/docs/overview) is a messaging service provided by Google Cloud Platform (GCP). It is designed to enable scalable, reliable, and real-time messaging between independent applications. Pub/Sub follows the publish-subscribe model, where messages are published by senders (publishers) to a topic, and then delivered to multiple receivers (subscribers) who have expressed interest in that topic.   
  
Pub/Sub acts as an unbounded source, as it's constantly receiving and sending messages in real time. In such cases, we need to build a [Streaming Pipeline](https://beam.apache.org/documentation/sdks/python-streaming/).

## Creating a publisher for a pubsub topic in Google Cloud Console

A publisher is a component that allows us to create and send messages to Google Cloud Pub/Sub. Learn more about publishing and received messages from Pub/Sub [here](https://cloud.google.com/pubsub/docs/publish-receive-messages-client-library).
    
    
    import os
    from google.cloud import pubsub_v1
    # Add your project ID here
    PROJECT_ID = '<PROJECT_ID>' # @param {type:'string'}
    # Add your topic name here
    TOPIC = '<TOPIC>' # @param {type:'string'}
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_name = 'projects/{project_id}/topics/{topic}'.format(
        project_id = PROJECT_ID,
        topic = TOPIC,
    )
    

## Extracting and sending comments to Pub/Sub

YouTube API provides an interface for accessing YouTube data. First, we need to enable YouTube API on the Google Cloud Console project. After that, we need to create a credential, which will further provide an API key. This API key, along with a video ID can be used to access data of that YouTube video. The Publisher created earlier is used to publish each comment to Pub/Sub. See examples of using the YouTube API [here](https://developers.google.com/youtube/v3/code_samples/code_snippets).
    
    
    from googleapiclient.discovery import build
    
    api_key = '' #Add your API key here
    
    def video_comments(video_id):
        # Creating youtube resource object
        youtube = build('youtube', 'v3',
                        developerKey=api_key)
    
        # Retrieve youtube video results
        video_response=youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id
        ).execute()
    
        # Iterate video response
        while video_response:
    
            # extracting required info from each object
            for item in video_response['items']:
    
                # Extracting comments
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    
                # Print comment
                print(comment, end = '\n')
                data = comment.encode("utf-8")
    
                # Publishing the comment to Pub/Sub
                publisher.publish(topic_name, data)
    
            # Repeat until there are no next pages
            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                        part = 'snippet,replies',
                        videoId = video_id
                    ).execute()
            else:
              return
    
    # The video ID can be extracted from the video URL, which can be represented like this
    # https://www.youtube.com/watch?v=VIDEO_ID
    # Enter here the desired video ID
    video_id = "fCXYrAH2gQI"
    
    # Call function
    video_comments(video_id)
    
    
    
    Can’t wait to watch you guys grow . Harmonies are on point and the oversized early 90’s blazers are a great touch.
    Amazing performance! Such an inspiring group ❤
    Love the vibe
    Your telling me this has less than 100 views????  Unreal
    I&#39;m happy that I lived long enough to see and hear music that tells the truth that millions of men and boys live every day! WELL DONE!
    Love the unity of sound
    

## Defining utility functions

Below we have defined some functions for our Beam pipeline to perform the following tasks:

  * Print the messages received from Pub/Sub
  * Tokenize the strings
  * Save the predictions in a list

These functions can be used in our pipeline by using [Map](https://beam.apache.org/documentation/transforms/python/elementwise/map/), which essentially calls the function on each element in the PCollection.
    
    
    # Index 0 corresponds to positive comment while index 1 corresponds to negative comment
    labels = ['positive','negative']
    
    
    
    # Printing values
    def print_values(element):
      print(element)
      return element
    
    # Here along with printing, we have also returned the element.
    # This is done so that the element is passed into the next functions or transforms after printing.
    
    
    
    # Tokenizing the strings
    def tokenize(element):
        padded_seq = get_sequences([element])
        return padded_seq[0]
    
    
    
    # Saving predictions in a list
    predictions = []
    from tensorflow.python.ops.numpy_ops import np_config
    np_config.enable_numpy_behavior()
    def save_predictions(element):
        list_of_predictions = element.inference.tolist()
        highest_prediction = max(list_of_predictions)
        ans = labels[list_of_predictions.index(highest_prediction)]
        predictions.append([list_of_predictions,ans])
        print(ans)
    

## Building an Apache Beam Pipeline

We need to build a streaming pipeline that takes data from Pub/Sub. A [Runner](https://beam.apache.org/documentation/#runners) is used to execute Beam pipelines in a distributed manner. We need to use a streaming runner to run a streaming pipeline. [InteractiveRunner](https://beam.apache.org/releases/pydoc/2.10.0/apache_beam.runners.interactive.interactive_runner.html) is suitable for this and allows developing and running Beam pipelines interactively in notebooks. See more details on how to use InteractiveRunner [here](https://cloud.google.com/dataflow/docs/guides/interactive-pipeline-development).
    
    
    # Add the path to your topic here
    TOPIC_PATH = '<TOPIC_PATH>' # @param {type:'string'}
    
    
    
    # Add the path to your subscription here
    SUBS_PATH = '<SUB_PATH>' # @param {type:'string'}
    

Importing InteractiveRunner
    
    
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    import apache_beam.runners.interactive.interactive_beam as ib
    
    
    
    ib.options.recording_duration = '2m' # This is how long Interactive Runner will listen to data from Pub/Sub
    ib.options.recording_size_limit = 1e9 # This is the recording size limit set to 1 GB
    options = pipeline_options.PipelineOptions()
    options.view_as(pipeline_options.StandardOptions).streaming = True # Streaming mode is set True
    

The pipeline performs the following tasks:

  * Reads messages from Cloud Pub Sub
  * Prints the messages
  * Performs preprocessing. We can reuse all of our previously defined preprocessing functions for training using [beam.Map](https://beam.apache.org/documentation/transforms/python/elementwise/map/).
  * RunInference on the preprocessed data
  * Prints the result and store in a list


    
    
    with beam.Pipeline(options=options) as p:
        _ = (p | "Read From Pub/Sub" >> beam.io.ReadFromPubSub(subscription=SUBS_PATH)
               | "Convert to String" >> beam.Map(lambda element: element.decode('utf-8'))
               | "Print" >> beam.Map(print_values)
               | "Remove Symbols" >> beam.Map(remove_symbols)
               | "Remove Short Words" >> beam.Map(remove_short_words)
               | "Lower Case" >> beam.Map(lower_case)
               | "Tokenize" >> beam.Map(tokenize)
               | "RunInference" >> RunInference(model_handler)
               | "Store Predictions" >> beam.Map(save_predictions)
            )
    
    
    
    Can’t wait to watch you guys grow . Harmonies are on point and the oversized early 90’s blazers are a great touch.
    Amazing performance! Such an inspiring group ❤
    Love the vibe
    Your telling me this has less than 100 views????  Unreal
    I&#39;m happy that I lived long enough to see and hear music that tells the truth that millions of men and boys live every day! WELL DONE!
    Love the unity of sound
    positive
    positive
    positive
    positive
    positive
    positive
    

The above pipeline is a streaming pipeline, which means it will run continuously, unless we stop it manually. This is why a keyboard interrupt can be seen here. Let us print the predictions made by the model and the corresponding sentiment.
    
    
    predictions
    
    
    
    [[[0.852806806564331, 0.14719319343566895], 'positive'],
     [[0.8602035045623779, 0.13979655504226685], 'positive'],
     [[0.8670042753219604, 0.13299570977687836], 'positive'],
     [[0.8574993014335632, 0.14250065386295319], 'positive'],
     [[0.8401712775230408, 0.15982864797115326], 'positive'],
     [[0.8648154735565186, 0.13518451154232025], 'positive']]
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
