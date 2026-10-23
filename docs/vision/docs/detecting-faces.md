---
url: https://docs.cloud.google.com/vision/docs/detecting-faces/
title: Detect faces \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:37.337506+00:00
---

# Detect faces  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/detecting-faces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback 

#  Detect faces Stay organized with collections  Save and categorize content based on your preferences. 

**Face Detection** detects multiple faces within an image along with the associated key facial attributes such as `wearing headwear`.

**Specific individual[Facial Recognition](https://en.wikipedia.org/wiki/Facial_recognition_system) is not supported.**

**Note:** The Vision API now supports offline **asynchronous batch image annotation** for all features. This asynchronous request supports up to 2000 image files and returns response JSON files that are stored in your Cloud Storage bucket. For more information about this feature, refer to [Offline batch image annotation](https://docs.cloud.google.com/vision/docs/batch). 

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Vision API performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Vision API free ](https://console.cloud.google.com/freetrial)

## Face detection requests

### Set up your Google Cloud project and authentication

If you have not created a Google Cloud project, do so now. Expand this section for instructions. 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Vision API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=vision.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




### Detect Faces in a local image

You can use the Vision API to perform feature detection on a local image file.

For REST requests, send the contents of the image file as a [base64 encoded](https://docs.cloud.google.com/vision/docs/base64) string in the body of your request.

For `gcloud` and client library requests, specify the path to a local image in your request. 

### REST

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_IMAGE: The base64 representation (ASCII string) of your binary image data. This string should look similar to the following string: 
    * `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`
Visit the [base64 encode](https://docs.cloud.google.com/vision/docs/base64) topic for more information.
  * RESULTS_INT: (Optional) An integer value of results to return. If you omit the `"maxResults"` field and its value, the API returns the default value of 10 results. This field does not apply to the following feature types: `TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`. 
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "content": "BASE64_ENCODED_IMAGE"
          },
          "features": [
            {
              "maxResults": RESULTS_INT,
              "type": "FACE_DETECTION"
            }
          ]
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
         "https://vision.googleapis.com/v1/images:annotate"

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
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

A `FACE_DETECTION` response includes bounding boxes for all faces detected, landmarks detected on the faces (eyes, nose, mouth, etc.), and confidence ratings for face and image properties (joy, sorrow, anger, surprise, etc.).

#### Response
    
    
    {
      "responses": [
        {
          "faceAnnotations": [
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 1077,
                    "y": 157
                  },
                  {
                    "x": 2146,
                    "y": 157
                  },
                  {
                    "x": 2146,
                    "y": 1399
                  },
                  {
                    "x": 1077,
                    "y": 1399
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 1112,
                    "y": 407
                  },
                  {
                    "x": 1946,
                    "y": 407
                  },
                  {
                    "x": 1946,
                    "y": 1270
                  },
                  {
                    "x": 1112,
                    "y": 1270
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 1368.748,
                    "y": 739.0957,
                    "z": 0.0024604797
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 1660.6105,
                    "y": 751.5844,
                    "z": -117.06496
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 1284.3208,
                    "y": 666.61487,
                    "z": 63.41506
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 1418.9249,
                    "y": 671.49414,
                    "z": -83.82396
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 1556.9579,
                    "y": 672.2199,
                    "z": -139.39935
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 1771.4799,
                    "y": 682.65845,
                    "z": -131.66716
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 1479.6194,
                    "y": 741.87305,
                    "z": -114.84635
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 1443.3151,
                    "y": 917.5109,
                    "z": -194.49301
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 1466.7897,
                    "y": 1025.3483,
                    "z": -130.1202
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 1467.2588,
                    "y": 1147.0403,
                    "z": -109.24505
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 1376.8649,
                    "y": 1066.0856,
                    "z": -6.8136826
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 1652,
                    "y": 1079.3108,
                    "z": -106.93649
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 1485.5554,
                    "y": 1087.2388,
                    "z": -110.68126
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 1571.9475,
                    "y": 944.9213,
                    "z": -124.11806
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 1395.2339,
                    "y": 938.12787,
                    "z": -58.072197
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 1468.4205,
                    "y": 968.8732,
                    "z": -132.09975
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 1357.8658,
                    "y": 711.2427,
                    "z": -14.618992
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 1423.6936,
                    "y": 750.4164,
                    "z": -23.540215
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 1360.5627,
                    "y": 762.87415,
                    "z": -1.2607727
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 1313.72,
                    "y": 739.443,
                    "z": 50.216393
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 1661.6622,
                    "y": 718.6839,
                    "z": -134.17404
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 1730.0901,
                    "y": 763.57104,
                    "z": -116.365845
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 1660.8823,
                    "y": 777.3474,
                    "z": -120.8635
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 1590.8903,
                    "y": 753.5044,
                    "z": -91.84842
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 1345.7522,
                    "y": 640.18243,
                    "z": -27.887913
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 1660.5848,
                    "y": 648.36145,
                    "z": -153.73691
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 1274.1006,
                    "y": 826.2645,
                    "z": 422.6642
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 2014.8041,
                    "y": 908.56537,
                    "z": 149.61232
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 1476.2395,
                    "y": 669.9625,
                    "z": -120.59111
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 1477.3256,
                    "y": 1269.3269,
                    "z": -67.748795
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 1336.8848,
                    "y": 1096.2242,
                    "z": 286.73004
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 1863.2197,
                    "y": 1128.6213,
                    "z": 68.90431
                  }
                },
                {
                  "type": "LEFT_CHEEK_CENTER",
                  "position": {
                    "x": 1317.8549,
                    "y": 940.8025,
                    "z": 50.863163
                  }
                },
                {
                  "type": "RIGHT_CHEEK_CENTER",
                  "position": {
                    "x": 1733.4912,
                    "y": 964.073,
                    "z": -112.43947
                  }
                }
              ],
              "rollAngle": 1.5912293,
              "panAngle": -22.01964,
              "tiltAngle": -1.4997566,
              "detectionConfidence": 0.9310801,
              "landmarkingConfidence": 0.5775582,
              "joyLikelihood": "VERY_LIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "VERY_UNLIKELY",
              "blurredLikelihood": "VERY_UNLIKELY",
              "headwearLikelihood": "POSSIBLE"
            },
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 144,
                    "y": 1273
                  },
                  {
                    "x": 793,
                    "y": 1273
                  },
                  {
                    "x": 793,
                    "y": 1844
                  },
                  {
                    "x": 144,
                    "y": 1844
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 181,
                    "y": 1373
                  },
                  {
                    "x": 742,
                    "y": 1373
                  },
                  {
                    "x": 742,
                    "y": 1844
                  },
                  {
                    "x": 181,
                    "y": 1844
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 356.13745,
                    "y": 1635.7034,
                    "z": 0.0045757294
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 557.07324,
                    "y": 1601.1769,
                    "z": -10.258446
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 284.70563,
                    "y": 1599.5238,
                    "z": 28.755493
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 397.47183,
                    "y": 1574.1455,
                    "z": -28.716581
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 484.00983,
                    "y": 1559.5669,
                    "z": -33.509003
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 607.31726,
                    "y": 1551.2396,
                    "z": 11.0225525
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 447.86597,
                    "y": 1603.2458,
                    "z": -40.69277
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 463.15356,
                    "y": 1705.7849,
                    "z": -114.36831
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 475.02646,
                    "y": 1779.54,
                    "z": -85.219086
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 483.2983,
                    "y": 1844.4594,
                    "z": -83.812
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 391.11206,
                    "y": 1824.9432,
                    "z": -34.578503
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 559.85266,
                    "y": 1797.929,
                    "z": -44.700863
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 478.21106,
                    "y": 1807.5089,
                    "z": -76.46759
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 522.9539,
                    "y": 1717.8636,
                    "z": -51.489075
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 414.95767,
                    "y": 1739.2955,
                    "z": -46.75015
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 468.7361,
                    "y": 1739.5958,
                    "z": -78.64168
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 352.39365,
                    "y": 1618.0576,
                    "z": -7.2005444
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 395.81454,
                    "y": 1629.9379,
                    "z": -2.4021797
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 357.511,
                    "y": 1649.6553,
                    "z": -4.4735374
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 316.1426,
                    "y": 1645.2771,
                    "z": 18.701395
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 553.78973,
                    "y": 1582.3448,
                    "z": -17.07942
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 596.6489,
                    "y": 1599.1897,
                    "z": 4.014868
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 558.60706,
                    "y": 1615.964,
                    "z": -15.077105
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 514.8054,
                    "y": 1605.6407,
                    "z": -7.929638
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 336.4973,
                    "y": 1567.6466,
                    "z": -7.853897
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 542.3708,
                    "y": 1536.191,
                    "z": -19.405855
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 231.38948,
                    "y": 1749.3823,
                    "z": 221.4534
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 712.5644,
                    "y": 1670.4897,
                    "z": 199.4929
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 439.35938,
                    "y": 1561.1454,
                    "z": -36.451645
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 501.61096,
                    "y": 1942.0133,
                    "z": -75.04764
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 304.9834,
                    "y": 1892.5361,
                    "z": 114.12407
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 684.92535,
                    "y": 1824.337,
                    "z": 96.13425
                  }
                },
                {
                  "type": "LEFT_CHEEK_CENTER",
                  "position": {
                    "x": 334.5645,
                    "y": 1764.659,
                    "z": -2.0755844
                  }
                },
                {
                  "type": "RIGHT_CHEEK_CENTER",
                  "position": {
                    "x": 609.5919,
                    "y": 1719.6847,
                    "z": -16.861538
                  }
                }
              ],
              "rollAngle": -8.514851,
              "panAngle": -3.096844,
              "tiltAngle": 9.26052,
              "detectionConfidence": 0.5463216,
              "landmarkingConfidence": 0.55711126,
              "joyLikelihood": "VERY_UNLIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "VERY_UNLIKELY",
              "blurredLikelihood": "UNLIKELY",
              "headwearLikelihood": "VERY_UNLIKELY"
            },
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 785,
                    "y": 167
                  },
                  {
                    "x": 1100,
                    "y": 167
                  },
                  {
                    "x": 1100,
                    "y": 534
                  },
                  {
                    "x": 785,
                    "y": 534
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 834,
                    "y": 220
                  },
                  {
                    "x": 1101,
                    "y": 220
                  },
                  {
                    "x": 1101,
                    "y": 506
                  },
                  {
                    "x": 834,
                    "y": 506
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 933.74615,
                    "y": 351.82394,
                    "z": -0.00068986416
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 1005.8836,
                    "y": 329.02396,
                    "z": 43.38338
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 901.93494,
                    "y": 333.3503,
                    "z": -9.714935
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 957.4015,
                    "y": 319.9436,
                    "z": -6.8983736
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 987.50134,
                    "y": 308.46817,
                    "z": 13.108145
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 1031.5519,
                    "y": 298.8843,
                    "z": 65.60683
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 979.4568,
                    "y": 336.0551,
                    "z": 3.8077774
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 1003.45795,
                    "y": 398.80377,
                    "z": -17.351936
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 1000.16614,
                    "y": 432.11664,
                    "z": 5.2740355
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 1004.0378,
                    "y": 456.92422,
                    "z": 13.545323
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 961.922,
                    "y": 448.64325,
                    "z": 11.117096
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 1025.2979,
                    "y": 432.70157,
                    "z": 47.89795
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 1002.51434,
                    "y": 443.3482,
                    "z": 13.021965
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 1015.5027,
                    "y": 402.8421,
                    "z": 28.03568
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 969.764,
                    "y": 413.05563,
                    "z": 3.1156778
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 997.8564,
                    "y": 416.98083,
                    "z": 3.3404813
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 930.542,
                    "y": 343.17078,
                    "z": -6.9020395
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 950.7726,
                    "y": 348.11346,
                    "z": 9.216144
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 933.6862,
                    "y": 359.50848,
                    "z": -1.3347243
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 914.83966,
                    "y": 356.1447,
                    "z": -1.4299142
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 1006.59766,
                    "y": 319.50406,
                    "z": 38.31219
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 1021.45886,
                    "y": 327.68784,
                    "z": 61.100002
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 1009.46686,
                    "y": 336.0832,
                    "z": 43.87975
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 991.17535,
                    "y": 331.97632,
                    "z": 34.4881
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 928.40436,
                    "y": 317.13898,
                    "z": -14.411907
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 1008.5887,
                    "y": 294.364,
                    "z": 32.917953
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 835.18915,
                    "y": 395.7093,
                    "z": 81.31065
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 1024.4136,
                    "y": 360.64178,
                    "z": 182.02446
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 975.5221,
                    "y": 315.06647,
                    "z": 0.31154716
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 1010.74097,
                    "y": 503.23572,
                    "z": 29.966637
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 891.86237,
                    "y": 466.7829,
                    "z": 58.84553
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 1031.9008,
                    "y": 428.13455,
                    "z": 145.42484
                  }
                },
                {
                  "type": "LEFT_CHEEK_CENTER",
                  "position": {
                    "x": 929.4197,
                    "y": 418.09122,
                    "z": 4.574672
                  }
                },
                {
                  "type": "RIGHT_CHEEK_CENTER",
                  "position": {
                    "x": 1033.7278,
                    "y": 390.5432,
                    "z": 65.6329
                  }
                }
              ],
              "rollAngle": -12.077273,
              "panAngle": 27.194477,
              "tiltAngle": -5.252778,
              "detectionConfidence": 0.38126788,
              "landmarkingConfidence": 0.040030442,
              "joyLikelihood": "VERY_UNLIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "LIKELY",
              "blurredLikelihood": "VERY_LIKELY",
              "headwearLikelihood": "VERY_UNLIKELY"
            }
          ]
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectFaces gets faces from the Vision API for an image at the given file path.
    func detectFaces(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	f, err := os.Open(file)
    	if err != nil {
    		return err
    	}
    	defer f.Close()
    
    	image, err := vision.NewImageFromReader(f)
    	if err != nil {
    		return err
    	}
    	annotations, err := client.DetectFaces(ctx, image, nil, 10)
    	if err != nil {
    		return err
    	}
    	if len(annotations) == 0 {
    		fmt.Fprintln(w, "No faces found.")
    	} else {
    		fmt.Fprintln(w, "Faces:")
    		for i, annotation := range annotations {
    			fmt.Fprintln(w, "  Face", i)
    			fmt.Fprintln(w, "    Anger:", annotation.AngerLikelihood)
    			fmt.Fprintln(w, "    Joy:", annotation.JoyLikelihood)
    			fmt.Fprintln(w, "    Surprise:", annotation.SurpriseLikelihood)
    		}
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[FaceAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.FaceAnnotation.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectFaces {
    
      public static void detectFaces() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "path/to/your/image/file.jpg";
        detectFaces(filePath);
      }
    
      // Detects faces in the specified local image.
      public static void detectFaces(String filePath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) imgBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(filePath));
    
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().setContent(imgBytes).build();
        [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.FACE_DETECTION).build();
        [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) request =
            [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().addFeatures(feat).setImage(img).build();
        requests.add(request);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) client = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          [BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html) response = client.batchAnnotateImages(requests);
          List<AnnotateImageResponse> responses = response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__)();
    
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            // For full list of available annotations, see http://g.co/cloud/vision/docs
            for ([FaceAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.FaceAnnotation.html) annotation : res.getFaceAnnotationsList()) {
              System.out.format(
                  "anger: %s%njoy: %s%nsurprise: %s%nposition: %s",
                  annotation.getAngerLikelihood(),
                  annotation.getJoyLikelihood(),
                  annotation.getSurpriseLikelihood(),
                  annotation.getBoundingPoly());
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function detectFaces() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const fileName = 'Local image file, e.g. /path/to/image.png';
    
      const [result] = await client.faceDetection(fileName);
      const faces = result.faceAnnotations;
      console.log('Faces:');
      faces.forEach((face, i) => {
        console.log(`  Face #${i + 1}:`);
        console.log(`    Joy: ${face.joyLikelihood}`);
        console.log(`    Anger: ${face.angerLikelihood}`);
        console.log(`    Sorrow: ${face.sorrowLikelihood}`);
        console.log(`    Surprise: ${face.surpriseLikelihood}`);
      });
    }
    detectFaces();

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_faces(path):
        """Detects faces in an image."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        with open(path, "rb") as image_file:
            content = image_file.read()
    
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
        response = client.face_detection(image=image)
        faces = response.face_annotations
    
        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = (
            "UNKNOWN",
            "VERY_UNLIKELY",
            "UNLIKELY",
            "POSSIBLE",
            "LIKELY",
            "VERY_LIKELY",
        )
        print("Faces:")
    
        for face in faces:
            print(f"anger: {likelihood_name[face.anger_likelihood]}")
            print(f"joy: {likelihood_name[face.joy_likelihood]}")
            print(f"surprise: {likelihood_name[face.surprise_likelihood]}")
    
            vertices = [
                f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
            ]
    
            print("face bounds: {}".format(",".join(vertices)))
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Detect Faces in a remote image

You can use the Vision API to perform feature detection on a remote image file that is located in Cloud Storage or on the Web. To send a remote file request, specify the file's Web URL or Cloud Storage URI in the request body. 

**Caution:** When fetching images from HTTP/HTTPS URLs, Google cannot guarantee that the request will be completed. Your request might fail if the specified host denies the request (for example, due to request throttling or [DoS](https://en.wikipedia.org/wiki/Denial-of-service_attack) prevention), or if Google throttles requests to the site for abuse prevention. **As a best practice, don't depend on externally-hosted images for production applications**. 

### REST

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://cloud-samples-data/vision/face/faces.jpeg

  * RESULTS_INT: (Optional) An integer value of results to return. If you omit the `"maxResults"` field and its value, the API returns the default value of 10 results. This field does not apply to the following feature types: `TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`. 
  * PROJECT_ID: Your Google Cloud project ID.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "imageUri": "CLOUD_STORAGE_IMAGE_URI"
            }
           },
           "features": [
             {
               "maxResults": RESULTS_INT,
               "type": "FACE_DETECTION"
             }
           ]
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
         "https://vision.googleapis.com/v1/images:annotate"

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
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

A `FACE_DETECTION` response includes bounding boxes for all faces detected, landmarks detected on the faces (eyes, nose, mouth, etc.), and confidence ratings for face and image properties (joy, sorrow, anger, surprise, etc.).

#### Response
    
    
    {
      "responses": [
        {
          "faceAnnotations": [
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 1077,
                    "y": 157
                  },
                  {
                    "x": 2146,
                    "y": 157
                  },
                  {
                    "x": 2146,
                    "y": 1399
                  },
                  {
                    "x": 1077,
                    "y": 1399
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 1112,
                    "y": 407
                  },
                  {
                    "x": 1946,
                    "y": 407
                  },
                  {
                    "x": 1946,
                    "y": 1270
                  },
                  {
                    "x": 1112,
                    "y": 1270
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 1368.748,
                    "y": 739.0957,
                    "z": 0.0024604797
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 1660.6105,
                    "y": 751.5844,
                    "z": -117.06496
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 1284.3208,
                    "y": 666.61487,
                    "z": 63.41506
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 1418.9249,
                    "y": 671.49414,
                    "z": -83.82396
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 1556.9579,
                    "y": 672.2199,
                    "z": -139.39935
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 1771.4799,
                    "y": 682.65845,
                    "z": -131.66716
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 1479.6194,
                    "y": 741.87305,
                    "z": -114.84635
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 1443.3151,
                    "y": 917.5109,
                    "z": -194.49301
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 1466.7897,
                    "y": 1025.3483,
                    "z": -130.1202
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 1467.2588,
                    "y": 1147.0403,
                    "z": -109.24505
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 1376.8649,
                    "y": 1066.0856,
                    "z": -6.8136826
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 1652,
                    "y": 1079.3108,
                    "z": -106.93649
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 1485.5554,
                    "y": 1087.2388,
                    "z": -110.68126
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 1571.9475,
                    "y": 944.9213,
                    "z": -124.11806
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 1395.2339,
                    "y": 938.12787,
                    "z": -58.072197
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 1468.4205,
                    "y": 968.8732,
                    "z": -132.09975
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 1357.8658,
                    "y": 711.2427,
                    "z": -14.618992
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 1423.6936,
                    "y": 750.4164,
                    "z": -23.540215
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 1360.5627,
                    "y": 762.87415,
                    "z": -1.2607727
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 1313.72,
                    "y": 739.443,
                    "z": 50.216393
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 1661.6622,
                    "y": 718.6839,
                    "z": -134.17404
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 1730.0901,
                    "y": 763.57104,
                    "z": -116.365845
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 1660.8823,
                    "y": 777.3474,
                    "z": -120.8635
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 1590.8903,
                    "y": 753.5044,
                    "z": -91.84842
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 1345.7522,
                    "y": 640.18243,
                    "z": -27.887913
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 1660.5848,
                    "y": 648.36145,
                    "z": -153.73691
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 1274.1006,
                    "y": 826.2645,
                    "z": 422.6642
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 2014.8041,
                    "y": 908.56537,
                    "z": 149.61232
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 1476.2395,
                    "y": 669.9625,
                    "z": -120.59111
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 1477.3256,
                    "y": 1269.3269,
                    "z": -67.748795
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 1336.8848,
                    "y": 1096.2242,
                    "z": 286.73004
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 1863.2197,
                    "y": 1128.6213,
                    "z": 68.90431
                  }
                },
                {
                  "type": "LEFT_CHEEK_CENTER",
                  "position": {
                    "x": 1317.8549,
                    "y": 940.8025,
                    "z": 50.863163
                  }
                },
                {
                  "type": "RIGHT_CHEEK_CENTER",
                  "position": {
                    "x": 1733.4912,
                    "y": 964.073,
                    "z": -112.43947
                  }
                }
              ],
              "rollAngle": 1.5912293,
              "panAngle": -22.01964,
              "tiltAngle": -1.4997566,
              "detectionConfidence": 0.9310801,
              "landmarkingConfidence": 0.5775582,
              "joyLikelihood": "VERY_LIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "VERY_UNLIKELY",
              "blurredLikelihood": "VERY_UNLIKELY",
              "headwearLikelihood": "POSSIBLE"
            },
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 144,
                    "y": 1273
                  },
                  {
                    "x": 793,
                    "y": 1273
                  },
                  {
                    "x": 793,
                    "y": 1844
                  },
                  {
                    "x": 144,
                    "y": 1844
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 181,
                    "y": 1373
                  },
                  {
                    "x": 742,
                    "y": 1373
                  },
                  {
                    "x": 742,
                    "y": 1844
                  },
                  {
                    "x": 181,
                    "y": 1844
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 356.13745,
                    "y": 1635.7034,
                    "z": 0.0045757294
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 557.07324,
                    "y": 1601.1769,
                    "z": -10.258446
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 284.70563,
                    "y": 1599.5238,
                    "z": 28.755493
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 397.47183,
                    "y": 1574.1455,
                    "z": -28.716581
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 484.00983,
                    "y": 1559.5669,
                    "z": -33.509003
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 607.31726,
                    "y": 1551.2396,
                    "z": 11.0225525
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 447.86597,
                    "y": 1603.2458,
                    "z": -40.69277
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 463.15356,
                    "y": 1705.7849,
                    "z": -114.36831
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 475.02646,
                    "y": 1779.54,
                    "z": -85.219086
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 483.2983,
                    "y": 1844.4594,
                    "z": -83.812
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 391.11206,
                    "y": 1824.9432,
                    "z": -34.578503
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 559.85266,
                    "y": 1797.929,
                    "z": -44.700863
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 478.21106,
                    "y": 1807.5089,
                    "z": -76.46759
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 522.9539,
                    "y": 1717.8636,
                    "z": -51.489075
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 414.95767,
                    "y": 1739.2955,
                    "z": -46.75015
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 468.7361,
                    "y": 1739.5958,
                    "z": -78.64168
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 352.39365,
                    "y": 1618.0576,
                    "z": -7.2005444
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 395.81454,
                    "y": 1629.9379,
                    "z": -2.4021797
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 357.511,
                    "y": 1649.6553,
                    "z": -4.4735374
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 316.1426,
                    "y": 1645.2771,
                    "z": 18.701395
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 553.78973,
                    "y": 1582.3448,
                    "z": -17.07942
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 596.6489,
                    "y": 1599.1897,
                    "z": 4.014868
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 558.60706,
                    "y": 1615.964,
                    "z": -15.077105
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 514.8054,
                    "y": 1605.6407,
                    "z": -7.929638
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 336.4973,
                    "y": 1567.6466,
                    "z": -7.853897
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 542.3708,
                    "y": 1536.191,
                    "z": -19.405855
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 231.38948,
                    "y": 1749.3823,
                    "z": 221.4534
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 712.5644,
                    "y": 1670.4897,
                    "z": 199.4929
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 439.35938,
                    "y": 1561.1454,
                    "z": -36.451645
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 501.61096,
                    "y": 1942.0133,
                    "z": -75.04764
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 304.9834,
                    "y": 1892.5361,
                    "z": 114.12407
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 684.92535,
                    "y": 1824.337,
                    "z": 96.13425
                  }
                },
                {
                  "type": "LEFT_CHEEK_CENTER",
                  "position": {
                    "x": 334.5645,
                    "y": 1764.659,
                    "z": -2.0755844
                  }
                },
                {
                  "type": "RIGHT_CHEEK_CENTER",
                  "position": {
                    "x": 609.5919,
                    "y": 1719.6847,
                    "z": -16.861538
                  }
                }
              ],
              "rollAngle": -8.514851,
              "panAngle": -3.096844,
              "tiltAngle": 9.26052,
              "detectionConfidence": 0.5463216,
              "landmarkingConfidence": 0.55711126,
              "joyLikelihood": "VERY_UNLIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "VERY_UNLIKELY",
              "blurredLikelihood": "UNLIKELY",
              "headwearLikelihood": "VERY_UNLIKELY"
            },
            {
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 785,
                    "y": 167
                  },
                  {
                    "x": 1100,
                    "y": 167
                  },
                  {
                    "x": 1100,
                    "y": 534
                  },
                  {
                    "x": 785,
                    "y": 534
                  }
                ]
              },
              "fdBoundingPoly": {
                "vertices": [
                  {
                    "x": 834,
                    "y": 220
                  },
                  {
                    "x": 1101,
                    "y": 220
                  },
                  {
                    "x": 1101,
                    "y": 506
                  },
                  {
                    "x": 834,
                    "y": 506
                  }
                ]
              },
              "landmarks": [
                {
                  "type": "LEFT_EYE",
                  "position": {
                    "x": 933.74615,
                    "y": 351.82394,
                    "z": -0.00068986416
                  }
                },
                {
                  "type": "RIGHT_EYE",
                  "position": {
                    "x": 1005.8836,
                    "y": 329.02396,
                    "z": 43.38338
                  }
                },
                {
                  "type": "LEFT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 901.93494,
                    "y": 333.3503,
                    "z": -9.714935
                  }
                },
                {
                  "type": "RIGHT_OF_LEFT_EYEBROW",
                  "position": {
                    "x": 957.4015,
                    "y": 319.9436,
                    "z": -6.8983736
                  }
                },
                {
                  "type": "LEFT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 987.50134,
                    "y": 308.46817,
                    "z": 13.108145
                  }
                },
                {
                  "type": "RIGHT_OF_RIGHT_EYEBROW",
                  "position": {
                    "x": 1031.5519,
                    "y": 298.8843,
                    "z": 65.60683
                  }
                },
                {
                  "type": "MIDPOINT_BETWEEN_EYES",
                  "position": {
                    "x": 979.4568,
                    "y": 336.0551,
                    "z": 3.8077774
                  }
                },
                {
                  "type": "NOSE_TIP",
                  "position": {
                    "x": 1003.45795,
                    "y": 398.80377,
                    "z": -17.351936
                  }
                },
                {
                  "type": "UPPER_LIP",
                  "position": {
                    "x": 1000.16614,
                    "y": 432.11664,
                    "z": 5.2740355
                  }
                },
                {
                  "type": "LOWER_LIP",
                  "position": {
                    "x": 1004.0378,
                    "y": 456.92422,
                    "z": 13.545323
                  }
                },
                {
                  "type": "MOUTH_LEFT",
                  "position": {
                    "x": 961.922,
                    "y": 448.64325,
                    "z": 11.117096
                  }
                },
                {
                  "type": "MOUTH_RIGHT",
                  "position": {
                    "x": 1025.2979,
                    "y": 432.70157,
                    "z": 47.89795
                  }
                },
                {
                  "type": "MOUTH_CENTER",
                  "position": {
                    "x": 1002.51434,
                    "y": 443.3482,
                    "z": 13.021965
                  }
                },
                {
                  "type": "NOSE_BOTTOM_RIGHT",
                  "position": {
                    "x": 1015.5027,
                    "y": 402.8421,
                    "z": 28.03568
                  }
                },
                {
                  "type": "NOSE_BOTTOM_LEFT",
                  "position": {
                    "x": 969.764,
                    "y": 413.05563,
                    "z": 3.1156778
                  }
                },
                {
                  "type": "NOSE_BOTTOM_CENTER",
                  "position": {
                    "x": 997.8564,
                    "y": 416.98083,
                    "z": 3.3404813
                  }
                },
                {
                  "type": "LEFT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 930.542,
                    "y": 343.17078,
                    "z": -6.9020395
                  }
                },
                {
                  "type": "LEFT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 950.7726,
                    "y": 348.11346,
                    "z": 9.216144
                  }
                },
                {
                  "type": "LEFT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 933.6862,
                    "y": 359.50848,
                    "z": -1.3347243
                  }
                },
                {
                  "type": "LEFT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 914.83966,
                    "y": 356.1447,
                    "z": -1.4299142
                  }
                },
                {
                  "type": "RIGHT_EYE_TOP_BOUNDARY",
                  "position": {
                    "x": 1006.59766,
                    "y": 319.50406,
                    "z": 38.31219
                  }
                },
                {
                  "type": "RIGHT_EYE_RIGHT_CORNER",
                  "position": {
                    "x": 1021.45886,
                    "y": 327.68784,
                    "z": 61.100002
                  }
                },
                {
                  "type": "RIGHT_EYE_BOTTOM_BOUNDARY",
                  "position": {
                    "x": 1009.46686,
                    "y": 336.0832,
                    "z": 43.87975
                  }
                },
                {
                  "type": "RIGHT_EYE_LEFT_CORNER",
                  "position": {
                    "x": 991.17535,
                    "y": 331.97632,
                    "z": 34.4881
                  }
                },
                {
                  "type": "LEFT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 928.40436,
                    "y": 317.13898,
                    "z": -14.411907
                  }
                },
                {
                  "type": "RIGHT_EYEBROW_UPPER_MIDPOINT",
                  "position": {
                    "x": 1008.5887,
                    "y": 294.364,
                    "z": 32.917953
                  }
                },
                {
                  "type": "LEFT_EAR_TRAGION",
                  "position": {
                    "x": 835.18915,
                    "y": 395.7093,
                    "z": 81.31065
                  }
                },
                {
                  "type": "RIGHT_EAR_TRAGION",
                  "position": {
                    "x": 1024.4136,
                    "y": 360.64178,
                    "z": 182.02446
                  }
                },
                {
                  "type": "FOREHEAD_GLABELLA",
                  "position": {
                    "x": 975.5221,
                    "y": 315.06647,
                    "z": 0.31154716
                  }
                },
                {
                  "type": "CHIN_GNATHION",
                  "position": {
                    "x": 1010.74097,
                    "y": 503.23572,
                    "z": 29.966637
                  }
                },
                {
                  "type": "CHIN_LEFT_GONION",
                  "position": {
                    "x": 891.86237,
                    "y": 466.7829,
                    "z": 58.84553
                  }
                },
                {
                  "type": "CHIN_RIGHT_GONION",
                  "position": {
                    "x": 1031.9008,
                    "y": 428.13455,
                    "z": 145.42484
                  }
                },
                {
                  "type": "LEFT_CHEEK_CENTER",
                  "position": {
                    "x": 929.4197,
                    "y": 418.09122,
                    "z": 4.574672
                  }
                },
                {
                  "type": "RIGHT_CHEEK_CENTER",
                  "position": {
                    "x": 1033.7278,
                    "y": 390.5432,
                    "z": 65.6329
                  }
                }
              ],
              "rollAngle": -12.077273,
              "panAngle": 27.194477,
              "tiltAngle": -5.252778,
              "detectionConfidence": 0.38126788,
              "landmarkingConfidence": 0.040030442,
              "joyLikelihood": "VERY_UNLIKELY",
              "sorrowLikelihood": "VERY_UNLIKELY",
              "angerLikelihood": "VERY_UNLIKELY",
              "surpriseLikelihood": "VERY_UNLIKELY",
              "underExposedLikelihood": "LIKELY",
              "blurredLikelihood": "VERY_LIKELY",
              "headwearLikelihood": "VERY_UNLIKELY"
            }
          ]
        }
      ]
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // detectFaces gets faces from the Vision API for an image at the given file path.
    func detectFacesURI(w io.Writer, file string) error {
    	ctx := context.Background()
    
    	client, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return err
    	}
    
    	image := vision.NewImageFromURI(file)
    	annotations, err := client.DetectFaces(ctx, image, nil, 10)
    	if err != nil {
    		return err
    	}
    	if len(annotations) == 0 {
    		fmt.Fprintln(w, "No faces found.")
    	} else {
    		fmt.Fprintln(w, "Faces:")
    		for i, annotation := range annotations {
    			fmt.Fprintln(w, "  Face", i)
    			fmt.Fprintln(w, "    Anger:", annotation.AngerLikelihood)
    			fmt.Fprintln(w, "    Joy:", annotation.JoyLikelihood)
    			fmt.Fprintln(w, "    Surprise:", annotation.SurpriseLikelihood)
    		}
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Vision API Quickstart Using Client Libraries](https://docs.cloud.google.com/vision/docs/detect-labels-image-client-libraries). For more information, see the [ Vision API Java reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview).

**Note:** For Java **Spring framework** users, [Spring Cloud Google Cloud](https://docs.cloud.google.com/vision/docs/adding-spring) offers a way to automatically configure authentication settings and client objects to use Vision API. 
    
    
    import com.google.cloud.vision.v1.[AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html);
    import com.google.cloud.vision.v1.[AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html);
    import com.google.cloud.vision.v1.[BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html);
    import com.google.cloud.vision.v1.[FaceAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.FaceAnnotation.html);
    import com.google.cloud.vision.v1.[Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html);
    import com.google.cloud.vision.v1.[Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html);
    import com.google.cloud.vision.v1.[ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html);
    import com.google.cloud.vision.v1.[ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DetectFacesGcs {
    
      public static void detectFacesGcs() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String filePath = "gs://your-gcs-bucket/path/to/image/file.jpg";
        detectFacesGcs(filePath);
      }
    
      // Detects faces in the specified remote image on Google Cloud Storage.
      public static void detectFacesGcs(String gcsPath) throws IOException {
        List<AnnotateImageRequest> requests = new ArrayList<>();
    
        [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html) imgSource = [ImageSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.html).newBuilder().[setGcsImageUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageSource.Builder.html#com_google_cloud_vision_v1_ImageSource_Builder_setGcsImageUri_java_lang_String_)(gcsPath).build();
        [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html) img = [Image](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.html).newBuilder().[setSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Image.Builder.html#com_google_cloud_vision_v1_Image_Builder_setSource_com_google_cloud_vision_v1_ImageSource_)(imgSource).build();
        [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html) feat = [Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).newBuilder().setType([Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.Feature.html).Type.FACE_DETECTION).build();
    
        [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html) request =
            [AnnotateImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageRequest.html).newBuilder().addFeatures(feat).setImage(img).build();
        requests.add(request);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html) client = [ImageAnnotatorClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageAnnotatorClient.html).create()) {
          [BatchAnnotateImagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html) response = client.batchAnnotateImages(requests);
          List<AnnotateImageResponse> responses = response.[getResponsesList](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchAnnotateImagesResponse.html#com_google_cloud_vision_v1_BatchAnnotateImagesResponse_getResponsesList__)();
    
          for ([AnnotateImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.AnnotateImageResponse.html) res : responses) {
            if (res.hasError()) {
              System.out.format("Error: %s%n", res.getError().getMessage());
              return;
            }
    
            // For full list of available annotations, see http://g.co/cloud/vision/docs
            for ([FaceAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.FaceAnnotation.html) annotation : res.getFaceAnnotationsList()) {
              System.out.format(
                  "anger: %s%njoy: %s%nsurprise: %s%nposition: %s",
                  annotation.getAngerLikelihood(),
                  annotation.getJoyLikelihood(),
                  annotation.getSurpriseLikelihood(),
                  annotation.getBoundingPoly());
            }
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client libraries
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const bucketName = 'Bucket where the file resides, e.g. my-bucket';
    // const fileName = 'Path to file within bucket, e.g. path/to/image.png';
    
    // Performs face detection on the gcs file
    const [result] = await client.faceDetection(`gs://${bucketName}/${fileName}`);
    const faces = result.faceAnnotations;
    console.log('Faces:');
    faces.forEach((face, i) => {
      console.log(`  Face #${i + 1}:`);
      console.log(`    Joy: ${face.joyLikelihood}`);
      console.log(`    Anger: ${face.angerLikelihood}`);
      console.log(`    Sorrow: ${face.sorrowLikelihood}`);
      console.log(`    Surprise: ${face.surpriseLikelihood}`);
    });

### Python

Before trying this sample, follow the Python setup instructions in the [Vision quickstart using client libraries](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries). For more information, see the [Vision Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def detect_faces_uri(uri):
        """Detects faces in the file located in Google Cloud Storage or the web."""
        from google.cloud import vision
    
        client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)()
        image.source.image_uri = uri
    
        response = client.face_detection(image=image)
        faces = response.face_annotations
    
        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = (
            "UNKNOWN",
            "VERY_UNLIKELY",
            "UNLIKELY",
            "POSSIBLE",
            "LIKELY",
            "VERY_LIKELY",
        )
        print("Faces:")
    
        for face in faces:
            print(f"anger: {likelihood_name[face.anger_likelihood]}")
            print(f"joy: {likelihood_name[face.joy_likelihood]}")
            print(f"surprise: {likelihood_name[face.surprise_likelihood]}")
    
            vertices = [
                f"({vertex.x},{vertex.y})" for vertex in face.bounding_poly.vertices
            ]
    
            print("face bounds: {}".format(",".join(vertices)))
    
        if response.error.message:
            raise Exception(
                "{}\nFor more info on error messages, check: "
                "https://cloud.google.com/apis/design/errors".format(response.error.message)
            )
    
    

### gcloud

To perform face detection, use the [`gcloud ml vision detect-faces`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/vision/detect-text) command as shown in the following example:
    
    
    gcloud ml vision detect-faces gs://cloud-samples-data/vision/face/faces.jpeg

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for .NET.](https://googleapis.dev/dotnet/Google.Apis.Vision.v1/latest/api/Google.Apis.Vision.v1.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/docs/libraries) on the client libraries page and then visit the [Vision reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Try it

Try face detection below. You can use the image specified already (`gs://cloud-samples-data/vision/face/faces.jpeg`) or specify your own image in its place. Send the request by selecting **Execute**.

**Request body:**
    
    
    {
      "requests": [
        {
          "features": [
            {
              "maxResults": 10,
              "type": "FACE_DETECTION"
            }
          ],
          "image": {
            "source": {
              "imageUri": "gs://cloud-samples-data/vision/face/faces.jpeg"
            }
          }
        }
      ]
    }

### Open the Google APIs Explorer and send the request

  1. To open the Google APIs Explorer, click **Try it!**.

Try it!

  2. Optional. Modify the existing request body.

  3. To send the request, click **Execute**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
