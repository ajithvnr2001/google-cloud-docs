---
url: https://docs.cloud.google.com/vision/docs/request/
title: Make a Vision API request \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:31.396127+00:00
---

# Make a Vision API request  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/request/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)



Send feedback 

#  Make a Vision API request Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Vision API is a REST API that uses HTTP POST operations to perform data analysis on images you send in the request. The API uses JSON for both requests and responses.

## Summary

  * Requests are POST requests to `https://vision.googleapis.com/v1/images:annotate`.
  * You must [authenticate](https://docs.cloud.google.com/vision/docs/auth) your requests.
  * The request body looks like this. Responses look sort of like this, but the fields will vary depending on what type of annotation you're doing.
  * Here's how to [send a request with cURL](https://docs.cloud.google.com/vision/docs/using-curl).
  * There are also [client libraries](https://docs.cloud.google.com/vision/docs/reference/libraries).
  * Looking for a quick demo? Just [drag and drop](https://docs.cloud.google.com/vision/docs/drag-and-drop)!



## Endpoint

The Vision API consists of a single endpoint (`https://vision.googleapis.com/v1/images`) that supports one HTTP request method (`annotate`):
    
    
    POST https://vision.googleapis.com/v1/images:annotate
    

## Authentication

The POST request must authenticate by passing either an API key or an OAuth token. For details, refer to the [Authenticate](https://docs.cloud.google.com/vision/docs/auth) page.

## JSON request format

The body of your POST request contains a JSON object, containing a single `requests` list, which itself contains one or more objects of type [`AnnotateImageRequest`](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate#AnnotateImageRequest):
    
    
    {
      "requests":[
        {
          "image":{
            "content":"/9j/7QBEUGhvdG9...image contents...eYxxxzj/Coa6Bax//Z"
          },
          "features":[
            {
              "type":"LABEL_DETECTION",
              "maxResults":1
            }
          ]
        }
      ]
    }
    

Every request:

  * Must contain a `requests` list.



Within the `requests` list:

  * `image` specifies the image file. It can be sent as a base64-encoded string, a Cloud Storage file location, or as a publicly-accessible URL. See Providing the image for details.

  * `features` lists the types of annotation to perform on the image. You can specify one or many types, as well as the `maxResults` to return for each.

  * `imageContext` (not shown in the example above) specifies hints to the service to help with annotation: bounding boxes, languages, and crop hints aspect ratios.




## Providing the image

You can provide the image in your request in one of three ways:

  * As a base64-encoded image string. If the image is stored locally, you can convert it to a string and pass it as the value of `image.content`:
        
        {
          "requests":[
            {
              "image":{
                "content":"/9j/7QBEUGhvdG9zaG9...image contents...fXNWzvDEeYxxxzj/Coa6Bax//Z"
              },
              "features":[
                {
                  "type":"FACE_DETECTION",
                  "maxResults":10
                }
              ]
            }
          ]
        }
        

See [Base64-encoding](https://docs.cloud.google.com/vision/docs/base64) for instructions on encoding on various platforms.

  * As a [Cloud Storage](https://docs.cloud.google.com/storage) URI. Pass the full URI as the value of `image.source.imageUri`:
        
        {
          "requests":[
            {
              "image":{
                "source":{
                  "imageUri":
                    "gs://bucket_name/path_to_image_object"
                }
              },
              "features":[
                {
                  "type":"LABEL_DETECTION",
                  "maxResults":1
                }
              ]
            }
          ]
        }
        

The file in Cloud Storage must be accessible to the authentication method you're using. If you're using an API key, the file must be publicly accessible. If you're using a service account, the file must be accessible to the user who created the service account.

  * As a publicly-accessible HTTP or HTTPS URL. Pass the URL as the value of `image.source.imageUri`:
        
        {
          "requests":[
            {
              "image":{
                "source":{
                  "imageUri":
                    "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"
                }
              },
              "features":[
                {
                  "type":"LOGO_DETECTION",
                  "maxResults":1
                }
              ]
            }
          ]
        }
        

When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request may fail if the specified host denies the request (e.g. due to request throttling or DoS prevention), or if Google throttles requests to the site for abuse prevention. As a best practice, don't depend on externally-hosted images for production applications.




## JSON response format

The `annotate` request receives a JSON response of type `AnnotateImageResponse`. Although the requests are similar for each feature type, the responses for each feature type can be quite different. Consult the [Vision API Reference](https://docs.cloud.google.com/vision/docs/reference/rest/v1/images/annotate#AnnotateImageResponse) for complete information.

The code below demonstrates a sample label detection response for the photo shown below:

![](https://docs.cloud.google.com/static/vision/docs/images/faulkner.jpg)
    
    
    {
      "responses": [
        {
          "labelAnnotations": [
            {
              "mid": "/m/0bt9lr",
              "description": "dog",
              "score": 0.97346616
            },
            {
              "mid": "/m/09686",
              "description": "vertebrate",
              "score": 0.85700572
            },
            {
              "mid": "/m/01pm38",
              "description": "clumber spaniel",
              "score": 0.84881884
            },
            {
              "mid": "/m/04rky",
              "description": "mammal",
              "score": 0.847575
            },
            {
              "mid": "/m/02wbgd",
              "description": "english cocker spaniel",
              "score": 0.75829375
            }
          ]
        }
      ]
    }
    

## Client libraries

Google provides client libraries in a number of programming languages to simplify the process of building and sending requests, and receiving and parsing responses.

Refer to the [Client libraries](https://docs.cloud.google.com/vision/docs/reference/libraries) for installation and usage instructions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
