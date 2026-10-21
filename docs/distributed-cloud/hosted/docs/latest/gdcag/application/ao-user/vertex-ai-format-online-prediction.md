---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction/
title: Format your prediction requests \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:26:07.503368+00:00
---

# Format your prediction requests  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-format-online-prediction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Format your prediction requests Stay organized with collections  Save and categorize content based on your preferences. 

**Preview:** Online Prediction is a Preview feature that is available as-is and is not recommended for production environments. Google provides no service-level agreements (SLA) or technical support commitments for Preview features. For more information, see GDC's [feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages).

Use online predictions when you are making requests in response to application input or in situations that require timely inference (real-time responses).

This page shows you how to format online prediction requests using the Online Prediction API for your custom-trained models and provides examples of requests and responses. After formatting your request, you can [get an online prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/quickstart-op).

## Before you begin

To verify model deployment status and send online prediction requests, request the necessary permissions from your administrator.

### Request IAM roles

Contact your Project IAM Admin to request the following roles in your project namespace:

  * **Vertex AI Prediction Viewer** (`vertex-ai-prediction-viewer`): view `DeployedModel` and `Endpoint` custom resources and check deployment status.
  * **Vertex AI Prediction User** (`vertex-ai-prediction-user`): access the Online Prediction service to send prediction requests to your model endpoint.



For more information about these roles, see [Prepare IAM permissions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions).

### Verify model and endpoint readiness

Before formatting a request to make online predictions, perform the following steps:

  1. [Export your model artifact for prediction](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-export-model-artifacts).
  2. [Deploy the model resource to an endpoint](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-deploy-model).

This action associates compute resources with the model so that it can serve online predictions with low latency.

  3. Check the status of the `DeployedModel` custom resource of your model and ensure it is ready to accept prediction requests:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get -f DEPLOYED_MODEL_NAME.yaml -o jsonpath='{.status.primaryCondition}'
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `DEPLOYED_MODEL_NAME`: the name of the `DeployedModel` definition file.

The primary condition must show that the `DeployedModel` is ready.

The following output shows a sample response:
    
    {"firstObservedTime":"2024-01-19T01:18:30Z","lastUpdateTime":"2024-01-19T01:35:47Z","message":"DeployedModel is ready", "observedGeneration":1, "reason":"Ready", "resourceName":"my-tf-model","type":"DeployedModel"}
    

  4. Check the status of the `Endpoint` custom resource and ensure it is ready to accept prediction requests:
         
         kubectl --kubeconfig PREDICTION_CLUSTER_KUBECONFIG get -f ENDPOINT_NAME.yaml -o jsonpath='{$.status.conditions[?(@.type == "EndpointReady")]}'
         

Replace the following:

     * `PREDICTION_CLUSTER_KUBECONFIG`: the path to the kubeconfig file in the prediction cluster.
     * `ENDPOINT_NAME`: the name of the `Endpoint` definition file.

The `status` field of the `EndpointReady` condition must show a `True` value.

The following output shows a sample response:
    
    {"lastTransitionTime":"2024-01-19T05:12:26Z","message":"Endpoint Ready", "observedGeneration":1,"reason":"ResourceReady","status":"True","type":"EndpointReady"}%
    




## Format your input for online predictions

Online Prediction has the following two methods to send requests:

  * **Prediction request** : send a request to the [`predict`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService.Predict) method to get an online prediction.
  * **Raw prediction request** : send a request to the [`rawPredict`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/prediction/grpc/prediction.aiplatform.gdc.goog.v1#prediction.aiplatform.gdc.goog.v1.PredictionService.RawPredict) method, which lets you use an arbitrary HTTP payload rather than following a JSON format.



If you require low latency, get raw predictions because `rawPredict` skips the serialization steps and directly forwards the request to the prediction container.

This section shows how to format and encode your prediction input instances using JSON, which is required if you are using the `predict` method. This information is not required if you are using the `rawPredict` method.

If you're using the Vertex AI SDK for Python to send prediction requests, specify the list of instances without the `instances` field. For example, specify `[ ["the","quick","brown"], ... ]` instead of `{ "instances": [ ["the","quick","brown"], ... ] }`.

### Format instances as JSON strings

The basic format for Online Prediction is a list of data instances. These can be either plain lists of values or members of a JSON object, depending on how you configured your inputs in your training application. TensorFlow models can accept more complex inputs.

The following example shows an input tensor and an instance key to a TensorFlow model:
    
    
     {"values": [1, 2, 3, 4], "key": 1}
    

The makeup of the JSON string can be complex as long as it follows these rules:

  * The top level of instance data must be a JSON object, which is a dictionary of key-value pairs.

  * Individual values in an instance object can be strings, numbers, or lists. You can't embed JSON objects.

  * Lists must contain only items of the same type (including other lists). Don't mix strings and numerical values.




You pass input instances for Online Prediction as the message body for the `predict` call. Learn more about the request body's formatting requirements.

Make each instance an item in a JSON array, and provide the array as the `instances` field of a JSON object like in the following example:
    
    
    {"instances": [
      {"values": [1, 2, 3, 4], "key": 1},
      {"values": [5, 6, 7, 8], "key": 2}
    ]}
    

### Encode binary data for prediction input

**Note:** This section only applies to predictions with TensorFlow.

You can't format binary data as the UTF-8 encoded strings that JSON supports. If you have binary data in your inputs, use base64 encoding to represent it. You require the following special formatting:

  * Format your encoded string as a JSON object with a single key named `b64`. In Python 3, base64 encoding outputs a byte sequence. Convert this sequence to a string to make it JSON-serializable:
        
        {'image_bytes': {'b64': base64.b64encode(jpeg_data).decode()}}
        

  * In your TensorFlow model code, name the aliases for your binary input and output tensors so that they end with `_bytes`.




## Request and response examples

This section describes the format of the Online Prediction request and response bodies with examples for TensorFlow and PyTorch.

### Request body details

### TensorFlow

The request body contains data with the following structure (JSON representation):
    
    
    {
      "instances": [
        <value>|<simple/nested list>|<object>,
        ...
      ]
    }
    

The `instances[]` object is required and it must contain the list of instances to get predictions for.

The structure of each element of the instances list is determined by your model's input definition. Instances can include named inputs (as objects) or can contain only unlabeled values.

Not all data includes named inputs. Some instances are JSON values (boolean, number, or string). However, instances are often lists of values or complex nested lists.

The following are some examples of request bodies:

  * **CSV data with each row encoded as a string value** :


    
    
    {"instances": ["1.0,true,\\"x\\"", "-2.0,false,\\"y\\""]}
    

  * **Plain text** :


    
    
    {"instances": ["the quick brown fox", "the lazy dog"]}
    

  * **Sentences encoded as lists of words (vectors of strings)** :


    
    
    {
      "instances": [
        ["the","quick","brown"],
        ["the","lazy","dog"],
        ...
      ]
    }
    

  * **Floating point scalar values** :


    
    
    {"instances": [0.0, 1.1, 2.2]}
    

  * **Vectors of integers** :


    
    
    {
      "instances": [
        [0, 1, 2],
        [3, 4, 5],
        ...
      ]
    }
    

  * **Tensors (in this case, two-dimensional tensors)** :


    
    
    {
      "instances": [
        [
          [0, 1, 2],
          [3, 4, 5]
        ],
        ...
      ]
    }
    

  * **Images, which can be represented different ways** :



In this encoding scheme the first two dimensions represent the rows and columns of the image, and the third dimension contains lists (vectors) of the R, G, and B values for each pixel:
    
    
    {
      "instances": [
        [
          [
            [138, 30, 66],
            [130, 20, 56],
            ...
          ],
          [
            [126, 38, 61],
            [122, 24, 57],
            ...
          ],
          ...
        ],
        ...
      ]
    }
    

### Data encoding

JSON strings must be encoded as UTF-8. To send binary data, you must base64-encode the data and mark it as binary. To mark a JSON string as binary, replace it with a JSON object with a single attribute named `b64`:
    
    
    {"b64": "..."}
    

The following example shows two serialized `tf.Examples` instances, requiring base64 encoding (fake data, for illustrative purposes only):
    
    
    {"instances": [{"b64": "X5ad6u"}, {"b64": "IA9j4nx"}]}
    

The following example shows two JPEG image byte strings, requiring base64 encoding (fake data, for illustrative purposes only):
    
    
    {"instances": [{"b64": "ASa8asdf"}, {"b64": "JLK7ljk3"}]}
    

### Multiple input tensors

Some models have an underlying TensorFlow graph that accepts multiple input tensors. In this case, use the names of JSON key-value pairs to identify the input tensors.

For a graph with input tensor aliases `tag` (string) and `image` (base64-encoded string):
    
    
    {
      "instances": [
        {
          "tag": "beach",
          "image": {"b64": "ASa8asdf"}
        },
        {
          "tag": "car",
          "image": {"b64": "JLK7ljk3"}
        }
      ]
    }
    

For a graph with input tensor aliases `tag` (string) and `image` (3-dimensional array of 8-bit ints):
    
    
    {
      "instances": [
        {
          "tag": "beach",
          "image": [
            [
              [138, 30, 66],
              [130, 20, 56],
              ...
            ],
            [
              [126, 38, 61],
              [122, 24, 57],
              ...
            ],
            ...
          ]
        },
        {
          "tag": "car",
          "image": [
            [
              [255, 0, 102],
              [255, 0, 97],
              ...
            ],
            [
              [254, 1, 101],
              [254, 2, 93],
              ...
            ],
            ...
          ]
        },
        ...
      ]
    }
    

### PyTorch

If your model uses a [PyTorch prebuilt container](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-online-predictions#pt), the default handlers of TorchServe expect each instance to be wrapped in a `data` field. For example:
    
    
    {
      "instances": [
        { "data": , <value> },
        { "data": , <value> }
      ]
    }
    

### Response body details

If the call is successful, the response body contains one prediction entry per instance in the request body, given in the same order:
    
    
    {
      "predictions": [
        {
          object
        }
      ],
      "deployedModelId": string
    }
    

If prediction fails for any instance, the response body contains no predictions. Instead, it contains a single error entry:
    
    
    {
      "error": string
    }
    

The `predictions[]` object contains the list of predictions, one for each instance in the request.

On error, the `error` string contains a message describing the problem. The error is returned instead of a prediction list if an error occurred while processing any instance.

Even though there is one prediction per instance, the format of a prediction is not directly related to the format of an instance. Predictions take whatever format is specified in the outputs collection defined in the model. The collection of predictions is returned in a JSON list. Each member of the list can be a value, a list, or a JSON object of any complexity. If your model has more than one output tensor, each prediction is a JSON object containing a key-value pair for each output. The keys identify the output aliases in the graph.

### Response body examples

The following examples show some possible responses for TensorFlow:

  * A set of predictions for three input instances, where each prediction is an integer value:
        
        {"predictions":
          [5, 4, 3],
          "deployedModelId": 123456789012345678
        }
        

  * A more complex set of predictions, each containing two named values that correspond to output tensors, named `label` and `scores`, respectively. The value of `label` is the predicted category (_car_ or _beach_) and `scores` contains a list of probabilities for that instance across the possible categories:
        
        {
          "predictions": [
            {
              "label": "beach",
              "scores": [0.1, 0.9]
            },
            {
              "label": "car",
              "scores": [0.75, 0.25]
            }
          ],
          "deployedModelId": 123456789012345678
        }
        

  * A response when there is an error processing an input instance:
        
        {"error": "Divide by zero"}
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
