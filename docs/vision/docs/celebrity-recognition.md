---
url: https://docs.cloud.google.com/vision/docs/celebrity-recognition/
title: Celebrity recognition \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:49:25.360104+00:00
---

# Celebrity recognition  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/celebrity-recognition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Celebrity recognition Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature is [deprecated](https://docs.cloud.google.com/vision/docs/deprecations) and will no longer be available on Google Cloud after September 16, 2025.

This page describes how to recognize celebrities in images using the Vision API.

The Vision API allows you to detect faces in an image. When it recognizes a face, the Vision API can compare the face against an indexed gallery of celebrities collated by Google.

The Vision API can recognize thousands of celebrities, and is intended for use on only professionally photographed media content where commonly recognizable celebrities are known to appear in the image.

If a match is found, the Vision API provides the [Knowledge Graph Machine ID (MID)](https://developers.google.com/knowledge-graph/) of the celebrity, their name, and a bounding box indicating where the face appears in the image.

## Request API access

This feature is intended for use by media & entertainment companies or approved partners on professionally-produced media content. To request API access, please submit [this form](https://docs.google.com/forms/d/e/1FAIpQLSenUFSRovp05e4ags9g2cWCAU-mUuSNPoBmRQm9Lg4B8k5KNw/viewform) with information about your company and use case.

### Request Celebrity Recognition for a local image

You can use the Vision API to perform feature detection on a local image file.

For REST requests, send the contents of the image file as a [base64 encoded](https://docs.cloud.google.com/vision/docs/base64) string in the body of your request.

For `gcloud` and client library requests, specify the path to a local image in your request. 

To send a Celebrity Recognition request you first get access to the feature for your project and then use the existing [face detection](https://docs.cloud.google.com/vision/docs/detecting-faces) feature (`FACE_DETECTION` enum). Results contain celebrity information if a celebrity is detected. 

### REST

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_IMAGE: The base64 representation (ASCII string) of your binary image data. This string should look similar to the following string: 
    * `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`
Visit the [base64 encode](https://docs.cloud.google.com/vision/docs/base64) topic for more information.
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1p4beta1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "content": "BASE64_ENCODED_IMAGE"
          },
          "features": [
            {
              "type": "FACE_DETECTION"
            }
          ],
          "imageContext": {
            "faceRecognitionParams": {
                "celebritySet": ["builtin/default"]
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1p4beta1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1p4beta1/images:annotate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "responses": [
        {
          "faceAnnotations": [
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 203
                  },
                  {
                    "x": 570
                  },
                  {
                    "x": 570,
                    "y": 368
                  },
                  {
                    "x": 203,
                    "y": 368
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 254,
                    "y": 48
                  },
                  {
                    "x": 524,
                    "y": 48
                  },
                  {
                    "x": 524,
                    "y": 318
                  },
                  {
                    "x": 254,
                    "y": 318
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 328.92297,
                    "y": 135.14728,
                    "z": -0.00084506406
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 440.65927,
                    "y": 131.96986,
                    "z": -0.18113805
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 290.14877,
                    "y": 114.45657,
                    "z": 11.400304
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 357.85278,
                    "y": 109.40719,
                    "z": -21.749352
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 411.14322,
                    "y": 108.33092,
                    "z": -21.866737
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 480.46622,
                    "y": 110.60321,
                    "z": 11.405331
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 384.6528,
                    "y": 129.57939,
                    "z": -23.62145
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 383.5203,
                    "y": 196.91586,
                    "z": -55.91733
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 387.36368,
                    "y": 236.28792,
                    "z": -29.9772
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 385.20834,
                    "y": 277.3345,
                    "z": -21.621998
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 341.77988,
                    "y": 248.98514,
                    "z": 0.5651365
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 439.91428,
                    "y": 244.32759,
                    "z": 2.6951885
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 385.44574,
                    "y": 254.93304,
                    "z": -21.696716
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 415.55923,
                    "y": 201.68005,
                    "z": -13.386427
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 354.17462,
                    "y": 205.03098,
                    "z": -12.758772
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 385.9818,
                    "y": 213.22089,
                    "z": -30.45643
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 329.98587,
                    "y": 128.55806,
                    "z": -7.625594
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 350.25543,
                    "y": 136.96538,
                    "z": 0.3162137
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 327.47772,
                    "y": 142.9333,
                    "z": -1.0234838
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 307.4751,
                    "y": 137.34349,
                    "z": 10.214714
                  }
                },
                {
                  "type": "LEFT_EYE_PUPIL",
                  "position": {
                    "x": 328.45987,
                    "y": 136.19621,
                    "z": -3.1551569
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 440.0691,
                    "y": 126.8801,
                    "z": -7.779711
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 464.28534,
                    "y": 135.34042,
                    "z": 10.301969
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 441.76584,
                    "y": 140.32564,
                    "z": -1.2271972
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 422.21207,
                    "y": 135.32939,
                    "z": 0.33341154
                  }
                },
                {
                  "type": "RIGHT_EYE_PUPIL",
                  "position": {
                    "x": 441.37714,
                    "y": 134.46259,
                    "z": -3.4412556
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 324.93048,
                    "y": 96.94437,
                    "z": -13.394134
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 444.3336,
                    "y": 95.093765,
                    "z": -13.487409
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 261.2239,
                    "y": 191.10706,
                    "z": 136.27896
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 513.192,
                    "y": 187.88185,
                    "z": 136.99525
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 384.6936,
                    "y": 107.73683,
                    "z": -26.120888
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 388.01538,
                    "y": 322.47537,
                    "z": -6.83534
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 274.37195,
                    "y": 261.15628,
                    "z": 91.56324
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 500.2335,
                    "y": 257.99966,
                    "z": 91.12145
                  }
                }
              ],
              "rollAngle": -0.8706148,
              "panAngle": -0.0915068,
              "tiltAngle": 0.05244069,
              "detectionConfidence": 0.99914575,
              "landmarkingConfidence": 0.7713903,
              "joyLikelihood": "VERY_LIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "VERY_UNLIKELY",
              "blurredLikelihood": "VERY_UNLIKELY",
              "headwearLikelihood": "VERY_UNLIKELY",**"recognitionResult": [
                {
                  "celebrity": {
                    "name": "builtin/ celebrity-mid",
                    "displayName": "celebrity-name"
                  },
                  "confidence": 0.82625544
                }
              ]**
            }
          ]
        }
      ]
    }
    

### Request Celebrity Recognition for a remote image

You can use the Vision API to perform feature detection on a remote image file that is located in Cloud Storage or on the Web. To send a remote file request, specify the file's Web URL or Cloud Storage URI in the request body. 

To send a Celebrity Recognition request you first get access to the feature for your project and then use the existing [face detection](https://docs.cloud.google.com/vision/docs/detecting-faces) feature (`FACE_DETECTION` enum). Results contain celebrity information if a celebrity is detected. 

**Caution:** When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request might fail if the specified host denies the request (for example, due to request throttling or [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) prevention), or if Google throttles requests to the site for abuse prevention. **As a best practice, don't depend on externally-hosted images for production applications**. 

### REST

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://my-cloud-bucket/img/celebrity_image.jpg

  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1p4beta1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "imageUri": "CLOUD_STORAGE_FILE_URI"
            }
          },
          "features": [
            {
              "type": "FACE_DETECTION"
            }
          ],
          "imageContext": {
            "faceRecognitionParams": {
                "celebritySet": ["builtin/default"]
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1p4beta1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1p4beta1/images:annotate" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "responses": [
        {
          "faceAnnotations": [
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 203
                  },
                  {
                    "x": 570
                  },
                  {
                    "x": 570,
                    "y": 368
                  },
                  {
                    "x": 203,
                    "y": 368
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 254,
                    "y": 48
                  },
                  {
                    "x": 524,
                    "y": 48
                  },
                  {
                    "x": 524,
                    "y": 318
                  },
                  {
                    "x": 254,
                    "y": 318
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 328.92297,
                    "y": 135.14728,
                    "z": -0.00084506406
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 440.65927,
                    "y": 131.96986,
                    "z": -0.18113805
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 290.14877,
                    "y": 114.45657,
                    "z": 11.400304
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 357.85278,
                    "y": 109.40719,
                    "z": -21.749352
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 411.14322,
                    "y": 108.33092,
                    "z": -21.866737
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 480.46622,
                    "y": 110.60321,
                    "z": 11.405331
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 384.6528,
                    "y": 129.57939,
                    "z": -23.62145
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 383.5203,
                    "y": 196.91586,
                    "z": -55.91733
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 387.36368,
                    "y": 236.28792,
                    "z": -29.9772
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 385.20834,
                    "y": 277.3345,
                    "z": -21.621998
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 341.77988,
                    "y": 248.98514,
                    "z": 0.5651365
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 439.91428,
                    "y": 244.32759,
                    "z": 2.6951885
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 385.44574,
                    "y": 254.93304,
                    "z": -21.696716
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 415.55923,
                    "y": 201.68005,
                    "z": -13.386427
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 354.17462,
                    "y": 205.03098,
                    "z": -12.758772
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 385.9818,
                    "y": 213.22089,
                    "z": -30.45643
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 329.98587,
                    "y": 128.55806,
                    "z": -7.625594
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 350.25543,
                    "y": 136.96538,
                    "z": 0.3162137
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 327.47772,
                    "y": 142.9333,
                    "z": -1.0234838
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 307.4751,
                    "y": 137.34349,
                    "z": 10.214714
                  }
                },
                {
                  "type": "LEFT_EYE_PUPIL",
                  "position": {
                    "x": 328.45987,
                    "y": 136.19621,
                    "z": -3.1551569
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 440.0691,
                    "y": 126.8801,
                    "z": -7.779711
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 464.28534,
                    "y": 135.34042,
                    "z": 10.301969
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 441.76584,
                    "y": 140.32564,
                    "z": -1.2271972
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 422.21207,
                    "y": 135.32939,
                    "z": 0.33341154
                  }
                },
                {
                  "type": "RIGHT_EYE_PUPIL",
                  "position": {
                    "x": 441.37714,
                    "y": 134.46259,
                    "z": -3.4412556
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 324.93048,
                    "y": 96.94437,
                    "z": -13.394134
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 444.3336,
                    "y": 95.093765,
                    "z": -13.487409
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 261.2239,
                    "y": 191.10706,
                    "z": 136.27896
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 513.192,
                    "y": 187.88185,
                    "z": 136.99525
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 384.6936,
                    "y": 107.73683,
                    "z": -26.120888
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 388.01538,
                    "y": 322.47537,
                    "z": -6.83534
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 274.37195,
                    "y": 261.15628,
                    "z": 91.56324
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 500.2335,
                    "y": 257.99966,
                    "z": 91.12145
                  }
                }
              ],
              "rollAngle": -0.8706148,
              "panAngle": -0.0915068,
              "tiltAngle": 0.05244069,
              "detectionConfidence": 0.99914575,
              "landmarkingConfidence": 0.7713903,
              "joyLikelihood": "VERY_LIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "VERY_UNLIKELY",
              "blurredLikelihood": "VERY_UNLIKELY",
              "headwearLikelihood": "VERY_UNLIKELY",**"recognitionResult": [
                {
                  "celebrity": {
                    "name": "builtin/ celebrity-mid",
                    "displayName": "celebrity-name"
                  },
                  "confidence": 0.82625544
                }
              ]**
            }
          ]
        }
      ]
    }
    

## Request celebrity opt-out

If you are a celebrity and would like not to be included in this feature for either Cloud Vision or Video Intelligence API, please fill out and submit [this form](https://docs.google.com/forms/d/e/1FAIpQLSeNI_qkhnUy2yGt1COZkfPwCMJnf-w-5lv5G5i7_Xl0PZyY2w/viewform?usp=sf_link).

## Report misuse

If you suspect the Vision API Celebrity Recognition feature is being misused in any way, please let us know using [this form](https://docs.google.com/forms/d/e/1FAIpQLSdQtYOpeQsGu52S9VycFc1Bl0yiJPlHKE7SFz4CVuIg5ascgg/viewform?usp=sf_link).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
