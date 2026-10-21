---
url: https://docs.cloud.google.com/vision/docs/detect-labels-image-command-line/
title: Quickstart: Detect labels in an image by using the command line \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:37.001335+00:00
---

# Quickstart: Detect labels in an image by using the command line  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/detect-labels-image-command-line/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/docs/features-list)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Detect labels in an image by using the command line

This page shows you how to send three feature detection and annotation requests to the Vision API using the [REST interface](https://docs.cloud.google.com/vision/docs/reference/rest) and the `curl` command.

Vision API enables easy integration of Google vision recognition technologies into developer applications. You can send image data and desired feature types to the Vision API, which then returns a corresponding response based on the image attributes you are interested in. For more information about the feature types offered, see the [List of all Vision API features](https://docs.cloud.google.com/vision/docs/features-list).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vision API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable vision.googleapis.com

  8. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Vision API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable vision.googleapis.com

  15. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/storage.objectViewer`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Make an image annotation request

After completing the Before you begin steps you can use the Vision API to annotate an image file.

In this example you use curl to send a request to the Vision API using the following image:

**Cloud Storage URI:**
    
    
    gs://**cloud-samples-data/vision/using_curl/shanghai.jpeg**

**HTTPS URL:**
    
    
    https://console.cloud.google.com/storage/browser/**cloud-samples-data/vision/using_curl/shanghai.jpeg**

![Shanghai street image.](https://docs.cloud.google.com/static/vision/docs/images/shanghai_small.jpeg) _Image credit_ : [Steve Long](https://unsplash.com/photos/jNGs6ys7MKk) on [Unsplash](https://unsplash.com/). 

## Create the request JSON

The following `request.json` file demonstrates how to request three `images:annotate` [features](https://docs.cloud.google.com/vision/docs/features-list) and limit the results in the response.

Create the JSON request file with the following text, and save it as a `request.json` plain text file in your working directory:

`request.json`
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "imageUri": "gs://cloud-samples-data/vision/using_curl/shanghai.jpeg"
            }
          },
          "features": [
            {
              "type": "LABEL_DETECTION",
              "maxResults": 3
            },
            {
              "type": "OBJECT_LOCALIZATION",
              "maxResults": 1
            },
            {
              "type": "TEXT_DETECTION",
              "maxResults": 1,
              "model": "builtin/latest"
            }
          ]
        }
      ]
    }

**Field value details**

  * `image.source.gcsImageUri` \- Indicates the image stored in a Cloud Storage bucket. You change this request to `image.source.imageUri` for a publicly available URI, or `image.content` to pass a base64 encoded string representation of an image.
  * `features` \- An object representing a specific feature type. You can request multiple feature types for a single image.
    * `type` \- The [enum value](https://docs.cloud.google.com/vision/docs/reference/rest/v1/Feature#type) specifying a feature.
    * `maxResults` (optional) - A limiting value on the results returned.
    * `model` (optional) - If applicable you can specify either `builtin/stable` (the default if unset) or `builtin/latest` to choose your model. Refer to the [Release notes](https://docs.cloud.google.com/vision/docs/release-notes) topic for a list of recently updated models.



## Send the request

You use curl and the body content from `request.json` to send the request to the Vision API. Enter the following on your command line:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "x-goog-user-project: PROJECT_ID" \
        -H "Content-Type: application/json; charset=utf-8" \
        https://vision.googleapis.com/v1/images:annotate -d @request.json

  * The sample `curl` command uses the `gcloud auth print-access-token` command to get an authentication token.
  * Note that to pass a filename to `curl` you use the `-d` option (for "data") and precede the filename with an `@` sign. This file should be in the same directory in which you execute the `curl` command.



## Interpret the response

You should see a JSON response similar to the one below.

The request JSON body specified `maxResults` for each annotation type. Consequently, you will see the following in the response JSON:

  * three `labelAnnotations` results
  * one `textAnnotations` result (shortened for clarity)
  * one `localizedObjectAnnotations` result



**Response**

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 100},{"x": 100,"y": 100},{"y": 100}] for an image that is 100 pixels by 100 pixels**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/docs/reference/rest/v1/images/annotate#boundingpoly). 
    
    
    {
      "responses": [
        {
          "**labelAnnotations** ": [
            {
              "mid": "/m/09g5pq",
              "description": "People",
              "score": 0.9504782,
              "topicality": 0.9504782
            },
            {
              "mid": "/m/01c8br",
              "description": "Street",
              "score": 0.8911568,
              "topicality": 0.8911568
            },
            {
              "mid": "/m/079bkr",
              "description": "Mode of transport",
              "score": 0.89089024,
              "topicality": 0.89089024
            }
          ],
          "**textAnnotations** ": [
            {
              "locale": "zh",
              "description": "牛牛面馆\n",
              "boundingPoly": {
                "vertices": [
                  {
                    "x": 159,
                    "y": 212
                  },
                  {
                    "x": 947,
                    "y": 212
                  },
                  {
                    "x": 947,
                    "y": 354
                  },
                  {
                    "x": 159,
                    "y": 354
                  }
                ]
              }
            },
            ...
          ],
          "fullTextAnnotation": {
            "pages": [
              {
                ...
                    "paragraphs": [
                      {
                        ...
                        "words": [
                          {
                            ...
                            "symbols": [
                              {
                                ...
                    ],
                    "blockType": "TEXT"
                  }
                ]
              }
            ],
            "text": "牛牛面馆\n"
          },
          "**localizedObjectAnnotations** ": [
            {
              "mid": "/m/01g317",
              "name": "Person",
              "score": 0.94413143,
              "boundingPoly": {
                "normalizedVertices": [
                  {
                    "x": 0.26063988,
                    "y": 0.46869153
                  },
                  {
                    "x": 0.40736017,
                    "y": 0.46869153
                  },
                  {
                    "x": 0.40736017,
                    "y": 0.8957791
                  },
                  {
                    "x": 0.26063988,
                    "y": 0.8957791
                  }
                ]
              }
            }
          ]
        }
      ]
    }

### Label detection results

  1. description: "People", score: 0.950
  2. description: "Street", score: 0.891
  3. description: "Mode of transport", score: 0.890

![Shanghai street image containing label detection results.](https://docs.cloud.google.com/static/vision/docs/images/shanghai_labels.png)_Image credit_ : [Steve Long](https://unsplash.com/photos/jNGs6ys7MKk) on [Unsplash](https://unsplash.com/) (_annotations added_). 

### Text detection results

  * text: 牛牛面馆\n
  * vertices: (x: 159, y: 212), (x: 947, y: 212), (x: 947, y: 354), (x: 159, y: 354 )

![Shanghai street image containing text detection results.](https://docs.cloud.google.com/static/vision/docs/images/shanghai_text.png)_Image credit_ : [Steve Long](https://unsplash.com/photos/jNGs6ys7MKk) on [Unsplash](https://unsplash.com/) (_annotations added_). 

### Object detection results

  * name: "Person", score: 0.944
  * normalized vertices: (x: 0.260, y: 0.468), (x: 0.407, y: 0.468), (x: 0.407, y: 0.895), (x: 0.260, y: 0.895)

![Shanghai street image containing object detection results.](https://docs.cloud.google.com/static/vision/docs/images/shanghai_object.png)_Image credit_ : [Steve Long](https://unsplash.com/photos/jNGs6ys7MKk) on [Unsplash](https://unsplash.com/) (_annotations added_). 

Congratulations! You've sent your first request to the Vision API.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

Optional: Revoke credentials from the gcloud CLI. 
    
    
    gcloud auth revoke

## What's next

  * See a list of [all feature types](https://docs.cloud.google.com/vision/docs/features-list) and their uses. 
  * Get started with the Vision API in your language of choice by using a [Vision API Client Library](https://docs.cloud.google.com/vision/docs/quickstart-client-libraries).
  * Use the [How-to guides](https://docs.cloud.google.com/vision/docs/how-to) to learn more about specific features, see example annotations, and get annotations for an individual file or image.
  * Learn about batch [image](https://docs.cloud.google.com/vision/docs/batch) and [file](https://docs.cloud.google.com/vision/docs/file-small-batch) (PDF/TIFF/GIF) annotation.
  * Browse through a comprehensive list of client library code [samples](https://docs.cloud.google.com/vision/docs/samples).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
