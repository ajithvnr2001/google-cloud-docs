---
url: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow/
title: Use TensorFlow for explanations \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:49:28.312723+00:00
---

# Use TensorFlow for explanations  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/tensorflow/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Use TensorFlow for explanations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Vertex Explainable AI is deprecated as of March 16, 2026. Access to Vertex Explainable AI will no longer be available on or after March 16, 2027. For more information, see the [deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations) page. 

When you are working with custom-trained TensorFlow models, there is specific information you need for saving your model and configuring explanations.

If you want to use Vertex Explainable AI with an AutoML tabular model, then you don't need to perform any configuration; Vertex AI automatically configures the model for Vertex Explainable AI. Skip this document and read [Getting explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/getting-explanations).

This guide provides the information you need when training a TensorFlow model to make sure that you can use it with Vertex Explainable AI. Specifically, the guide covers the following topics:

  * Finding the input and output tensor names during training that you need to specify when you [configure a `Model` resource for Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations). This includes creating and finding the appropriate tensors for Vertex Explainable AI in special cases when the typical ones don't work.

  * Exporting your TensorFlow model as a TensorFlow SavedModel that is compatible with Vertex Explainable AI.

  * Finding the input and output tensor names from a TensorFlow SavedModel that has already been exported. This might be helpful if you don't have access to the training code for the model.




## Find input and output tensor names during training

When you use a [TensorFlow prebuilt container to serve predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers#tensorflw), you must know the names of the input tensors and the output tensor of your model. You specify these names as part of an `ExplanationMetadata` message when you [configure a `Model` for Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations)

If your TensorFlow model meets the following criteria, then you can use the "basic method" described in the next section to determine these tensor names during training:

  * Your inputs are not in serialized form
  * Each input to the model's `SignatureDef` contains the value of the feature directly (can be either numeric values or strings)
  * The outputs are numeric values, treated as numeric data. This excludes class IDs, which are considered categorical data.



If your model does not meet these criteria, then read the Adjusting training code and finding tensor names in special cases section.

### The basic method

During training, print the `name` attribute of your model's input tensors and its output tensors. In the following example, the Keras layer's `name` field produces the underlying tensor name you need for your `ExplanationMetadata`:
    
    
    bow_inputs = tf.keras.layers.Input(shape=(2000,))
    merged_layer = tf.keras.layers.Dense(256, activation="relu")(bow_inputs)
    predictions = tf.keras.layers.Dense(10, activation="sigmoid")(merged_layer)
    model = tf.keras.Model(inputs=bow_inputs, outputs=predictions)
    print('input_tensor_name:', bow_inputs.name)
    print('output_tensor_name:', predictions.name)
    

Running this Python code prints the following output:
    
    
    input_tensor_name: input_1:0
    output_tensor_name: dense_1/Sigmoid:0
    

You can then use `input_1:0` as the input tensor name and `dense_1/Sigmod:0` as the output tensor name when you [configure your `Model` for explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations).

### Adjust training code and finding tensor names in special cases

There are a few common cases where the input and output tensors for your `ExplanationMetadata` should _not_ be the same as those in your serving `SignatureDef`:

  * You have serialized inputs
  * Your graph includes preprocessing operations
  * Your serving outputs are not probabilities, logits or other types of floating point tensors



In these cases, you should use different approaches to find the right input and output tensors. The overall goal is to find the tensors pertaining to feature values you want to explain for inputs and tensors pertaining to logits (pre-activation), probabilities (post-activation), or any other representation for outputs.

#### Special cases for input tensors

The inputs in your explanation metadata differ from those in your serving `SignatureDef` if you use a serialized input to feed the model, or if your graph includes preprocessing operations.

##### Serialized inputs

TensorFlow SavedModels can accept a variety of complex inputs, including:

  * Serialized tf.Example messages
  * JSON strings
  * Encoded Base64 strings (to represent image data)



If your model accepts serialized inputs like these, using these tensors directly as input for your explanations will not work, or could produce nonsensical results. Instead, you want to locate subsequent input tensors that are feeding into feature columns within your model.

When you export your model, you can add a parsing operation to your TensorFlow graph by calling a parsing function in your serving input function. You can find parsing functions listed in the [tf.io module](https://www.tensorflow.org/api_docs/python/tf/io). These parsing functions usually return tensors as a response, and these tensors are better selections for your explanation metadata.

For example, you could use [tf.parse_example()](https://www.tensorflow.org/api_docs/python/tf/io/parse_example) when exporting your model. It takes a serialized tf.Example message and outputs a dictionary of tensors feeding to feature columns. You can use its output to fill in your explanation metadata. If some of these outputs are tf.SparseTensor, which is a named tuple consisting of 3 tensors, then you should get the names of indexes, values and dense_shape tensors and fill the corresponding fields in the metadata.

The following example shows how to get name of the input tensor after a decoding operation:
    
    
    float_pixels = tf.map_fn(
        lambda img_string: tf.io.decode_image(
            img_string,
            channels=color_depth,
            dtype=tf.float32
        ),
        features,
        dtype=tf.float32,
        name='input_convert'
      )
    
    print(float_pixels.name)
    

##### Preprocessing inputs

If your model graph contains some preprocessing operations, you might want to get explanations on the tensors _after_ the preprocessing step. In this case, you can get the names of those tensors by using `name` property of tf.Tensor and put them in the explanation metadata:
    
    
    item_one_hot = tf.one_hot(item_indices, depth,
        on_value=1.0, off_value=0.0,
        axis=-1, name="one_hot_items:0")
    print(item_one_hot.name)
    

The decoded tensor name becomes `input_pixels:0`.

#### Special cases for output tensors

In most cases, the outputs in your serving `SignatureDef` are either probabilities or logits.

If your model is attributing probabilities but you want to explain the logit values instead, you have to find the appropriate output tensor names that correspond to the logits.

If your serving `SignatureDef` has outputs that are not probabilities or logits, you should refer to the probabilities operation in the training graph. This scenario is unlikely for Keras models. If this happens, you can use [TensorBoard](https://www.tensorflow.org/tensorboard) (or other graph visualization tools) to help locate the right output tensor names.

#### Special considerations for integrated gradients

If you want to use Vertex Explainable AI's [integrated gradients feature attribution method](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#ig), then you must make sure that your inputs are differentiable with respect to the output.

The explanation metadata logically separates a model's features from its inputs. When using integrated gradients with an input tensor that is not differentiable with respect to the output tensor, you need to provide the encoded (and differentiable) version of that feature as well.

Use the following approach if you have non-differentiable input tensors, or if you have non-differentiable operations in your graph:

  1. Encode the non-differentiable inputs as differentiable inputs.
  2. Set `input_tensor_name` to the name of the original, non-differentiable input tensor, _and_ set `encoded_tensor_name` to the name of its encoded, differentiable version.



#### Explanation metadata file with encoding

For example, consider a model that has a categorical feature with an input tensor named `zip_codes:0`. Because the input data includes zip codes as strings, the input tensor `zip_codes:0` is non-differentiable. If the model also preprocesses this data to get a one-hot encoding representation of the zip codes, then the input tensor after preprocessing is differentiable. To distinguish it from the original input tensor, you could name it `zip_codes_embedding:0`.

To use the data from both input tensors in your explanations request, set the `ExplanationMetadata` as follows when you [configure your `Model` for explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations):

  * Set the input feature key to a meaningful name, such as `zip_codes`.
  * Set `input_tensor_name` to the name of the original tensor, `zip_codes:0`.
  * Set `encoded_tensor_name` to the name of the tensor after one-hot encoding, `zip_codes_embedding:0`.
  * Set `encoding` to `COMBINED_EMBEDDING`.


    
    
    {
        "inputs": {
          "zip_codes": {
            "input_tensor_name": "zip_codes:0",
            "encoded_tensor_name": "zip_codes_embedding:0",
            "encoding": "COMBINED_EMBEDDING"
          }
        },
        "outputs": {
          "probabilities": {
            "output_tensor_name": "dense/Softmax:0"
          }
        }
    }
    

**Note:** Tensor names like `zip_codes:0` and `zip_codes_embedding:0` would arise from settings in your training code. If you do not have access to the training code, the tensor naming may not be as straightforward as the preceding example. In that case, you can use TensorBoard to find the correct tensor names.

Alternatively, you could set `input_tensor_name` to the name of the encoded, differentiable input tensor and omit the original, non-differentiable tensor. The benefit of providing both tensors is that attributions can be made to individual zip code values rather than on its one-hot encoding representation. In this example, you would exclude the original tensor (`zip_codes:0`) and set `input_tensor_name` to `zip_codes_embedding:0`. This approach is _not_ recommended, because the resulting feature attributions would be difficult to reason about.

#### Encoding

To enable encoding for your `Model`, specify encoding settings as shown in the preceding example.

The encoding feature helps reverse the process from encoded data to input data for attributions, which eliminates the need to post-process the returned attributions manually. See the [list of encodings that Vertex Explainable AI supports](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/ExplanationSpec#encoding).

For the `COMBINED_EMBEDDING` encoding, The input tensor is encoded into a 1D array.

For example:

  * Input: `["This", "is", "a", "test"]`
  * Encoded input: `[0.1, 0.2, 0.3, 0.4]`



## Export TensorFlow SavedModels for Vertex Explainable AI

After training a TensorFlow model, export it as a SavedModel. The TensorFlow SavedModel contains your trained TensorFlow model, along with serialized signatures, variables, and other assets needed to run the graph. Each `SignatureDef` in the SavedModel identifies a function in your graph that accepts tensor inputs and produces tensor outputs.

To ensure that your SavedModel is compatible with Vertex Explainable AI, follow the instructions in one of the following sections, depending on whether you are using TensorFlow 2 or TensorFlow 1.

### TensorFlow 2

If you're working with TensorFlow 2.x, use [`tf.saved_model.save`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save) to save your model. You can specify input signatures when saving your model. If you have one input signature, Vertex Explainable AI uses the default serving function for your explanations requests. If you have more than one input signature, you should specify the signature of your serving default function when you save your model:
    
    
    tf.saved_model.save(m, model_dir, signatures={
        'serving_default': serving_fn,
        'xai_model': model_fn # Required for XAI
        })
    

In this case, Vertex Explainable AI uses the model function signature you saved with the `xai_model` key for your explanations request. Use the exact string `xai_model` for the key.

If you use a preprocessing function, you also need to specify the signatures for your preprocessing function and your model function. You must use the exact strings `xai_preprocess` and `xai_model` as the keys:
    
    
    tf.saved_model.save(m, model_dir, signatures={
        'serving_default': serving_fn,
        'xai_preprocess': preprocess_fn, # Required for XAI
        'xai_model': model_fn # Required for XAI
        })
    

In this case, Vertex Explainable AI uses your preprocessing function and your model function for your explanation requests. Make sure that the output of your preprocessing function matches the input that your model function expects.

Learn more about [specifying serving signatures in TensorFlow](https://www.tensorflow.org/guide/saved_model#specifying_signatures_during_export).

### TensorFlow 1.15

If you're working with TensorFlow 1.15, do **not** use [`tf.saved_model.save`](https://www.tensorflow.org/versions/r1.15/api_docs/python/tf/saved_model/save). Vertex Explainable AI does not support TensorFlow 1 models saved with this method

If you build and train your model in Keras, you must convert your model to a TensorFlow Estimator, and then export it to a SavedModel. This section focuses on saving a model.

After you build, compile, train, and evaluate your Keras model, you have to:

  * Convert the Keras model to a TensorFlow Estimator, using `tf.keras.estimator.model_to_estimator`
  * Provide a serving input function, using `tf.estimator.export.build_raw_serving_input_receiver_fn`
  * Export the model as a SavedModel, using [`tf.estimator.export_saved_model`](https://www.tensorflow.org/api_docs/python/tf/saved_model/save).


    
    
    # Build, compile, train, and evaluate your Keras model
    model = tf.keras.Sequential(...)
    model.compile(...)
    model.fit(...)
    model.predict(...)
    
    ## Convert your Keras model to an Estimator
    keras_estimator = tf.keras.estimator.model_to_estimator(keras_model=model, model_dir='export')
    
    ## Define a serving input function appropriate for your model
    def serving_input_receiver_fn():
      ...
      return tf.estimator.export.ServingInputReceiver(...)
    
    ## Export the SavedModel to Cloud Storage, using your serving input function
    export_path = keras_estimator.export_saved_model(
      'gs://' + 'YOUR_BUCKET_NAME',
      serving_input_receiver_fn
    ).decode('utf-8')
    
    print("Model exported to: ", export_path)
    

## Get tensor names from a SavedModel's `SignatureDef`

You can use a TensorFlow SavedModel's `SignatureDef` to prepare your explanation metadata, provided it meets the criteria for the "basic method" described in a previous section. This might be helpful if you don't have access to the training code that produced the model.

To inspect the `SignatureDef` of your SavedModel, you can use the SavedModel CLI. Learn more about [how to use the SavedModel CLI](https://www.tensorflow.org/guide/saved_model#details_of_the_savedmodel_command_line_interface).

Consider the following example `SignatureDef`:
    
    
    The given SavedModel SignatureDef contains the following input(s):
      inputs['my_numpy_input'] tensor_info:
          dtype: DT_FLOAT
          shape: (-1, 1)
          name: x:0
    The given SavedModel SignatureDef contains the following output(s):
      outputs['probabilities'] tensor_info:
          dtype: DT_FLOAT
          shape: (-1, 1)
          name: dense/Softmax:0
    Method name is: tensorflow/serving/predict
    

The graph has an input tensor named `x:0` and an output tensor named `dense/Softmax:0`. When you [configure your `Model` for explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations), use `x:0` as the input tensor name and `dense/Softmax:0` as the output tensor name in the `ExplanationMetadata` message.

## What's next

  * Use your input and output tensor names to [configure a `Model` for Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations)
  * [Try a sample notebook demonstrating Vertex Explainable AI on tabular data or image data](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/official/explainable_ai).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
