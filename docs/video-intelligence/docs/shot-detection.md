---
url: https://docs.cloud.google.com/video-intelligence/docs/shot-detection/
title: Shot change detection tutorial \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:51.036977+00:00
---

# Shot change detection tutorial  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/shot-detection/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Shot change detection tutorial Stay organized with collections  Save and categorize content based on your preferences. 

## Audience

This tutorial is designed to let you quickly start exploring and developing applications with the Video Intelligence API. It's designed for people familiar with basic programming, though even without much programming knowledge, you should be able to follow along. Having walked through this tutorial, you should be able to use the [Reference documentation](https://docs.cloud.google.com/video-intelligence/docs/reference/rest) to create your own basic applications.

This tutorial steps through a Video Intelligence API application using Python code. The purpose here is not to explain the Python client libraries, but to explain how to make calls to the Video Intelligence API. Applications in Java and Node.js are essentially similar.

_If you're looking for a code-only example or an example in another language, check out the companion[how-to guide](https://docs.cloud.google.com/video-intelligence/docs/analyze-shots)._

## Prerequisites

This tutorial has several prerequisites:

  * You've [set up a Video Intelligence API project](https://docs.cloud.google.com/video-intelligence/docs/before-you-begin) in the Google Cloud console.
  * You've set up your environment using a service account and [Application Default Credentials](https://docs.cloud.google.com/video-intelligence/docs/common/auth#set_up_a_service_account).
  * You have basic familiarity with [Python](https://www.python.org/) programming.
  * Set up your Python development environment. It's recommended that you have the latest version of Python, `pip`, and `virtualenv` installed on your system. For instructions, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup) for Google Cloud Platform.
  * You've installed the [Google Cloud client library](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-videointelligence).



## Annotate a video using shot change detection

This tutorial walks you through a basic Video API application, using a `SHOT_CHANGE_DETECTION` request. A `SHOT_CHANGE_DETECTION` request provides the annotation results:

  * List of all shots that occur within the video
  * For each shot, provide the start and end time of the shot



We'll show the entire code first. (Note that we have removed most comments from this code in order to show you how brief the code is. We'll provide more comments as we walk through the code.)
    
    
    import argparse
    
    from google.cloud import videointelligence
    
    
    
    def analyze_shots(path):
        """Detects camera shot changes."""
        video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
        features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).SHOT_CHANGE_DETECTION]
        operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
            request={"features": features, "input_uri": path}
        )
        print("\nProcessing video for shot change annotations:")
    
        result = operation.result(timeout=120)
        print("\nFinished processing.")
    
    
        for i, shot in enumerate(result.annotation_results[0].shot_annotations):
            start_time = (
                shot.start_time_offset.seconds + shot.start_time_offset.microseconds / 1e6
            )
            end_time = (
                shot.end_time_offset.seconds + shot.end_time_offset.microseconds / 1e6
            )
            print("\tShot {}: {} to {}".format(i, start_time, end_time))
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument("path", help="GCS path for shot change detection.")
        args = parser.parse_args()
    
        analyze_shots(args.path)

This simple application performs the following tasks:

  * Imports the libraries necessary to run the application.
  * Takes a video file stored in Cloud Storage URI as an argument and passes it to the `main()` function.
  * Gets credentials to run the Video Intelligence API service.
  * Creates a video annotation request to send to the video service.
  * Sends the request and returns a long-running operation.
  * Loops over the long-running operation until the video is processed and returns available values.
  * Parses the response for the service and displays response to the user.



We'll go over these steps in more detail below.

## Import libraries
    
    
    import argparse
    
    from google.cloud import videointelligence
    

We import `argparse` to allow the application to accept input filenames as arguments.

For using the Video Intelligence API, we also import the `google.cloud.videointelligence` library, which holds the directory of our API calls and enumeration constants.

## Run your application
    
    
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("path", help="GCS path for shot change detection.")
    args = parser.parse_args()
    
    analyze_shots(args.path)

Here, we parse the passed argument for the Google Cloud Storage URI of the video filename and pass it to the `main()` function.

## Authenticate to the API

Before communicating with the Video Intelligence API service, you need to authenticate your service using previously acquired credentials. Within an application, the simplest way to obtain credentials is to use [Application Default Credentials](https://docs.cloud.google.com/video-intelligence/docs/common/auth#adc) (ADC). By default, ADC will attempt to obtain credentials from the `GOOGLE_APPLICATION_CREDENTIALS` environment file, which should be set to point to your service account's JSON key file. (You should have set up your service account and environment to use ADC in the [Quickstart](https://docs.cloud.google.com/video-intelligence/docs/getting-started). See [Setting Up a Service Account](https://docs.cloud.google.com/video-intelligence/docs/common/auth#set_up_a_service_account) for more information.)

## Construct the request
    
    
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SHOT_CHANGE_DETECTION]
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": path}
    )

Now that our Video Intelligence API service is ready, we can construct a request to that service. Requests to the Video Intelligence API are provided as JSON objects. See the [Video Intelligence API Reference](https://docs.cloud.google.com/video-intelligence/docs/reference/rest) for complete information on the specific structure of such a request.

This code snippet performs the following tasks:

  1. Constructs the JSON for a POST request to the `annotate_video()` method.
  2. Injects the Google Cloud Storage location of our passed video filename into the request.
  3. Indicates that the `annotate` method should perform a `SHOT_CHANGE_DETECTION`.



## Construct the long-running operation

When we first execute a request against the Video Intelligence API, we do not get an immediate result; instead we get an _operation name_ , stored within the response's `name` field, which we can then use to check for results at a later time.

Passing that operation's name (which is a numerical string) to the Video Intelligence API's _Operations Service_ `operations` method returns the current state of the operation. A sample response is shown below:
    
    
    {
       "response":{
          "@type":"type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse"
       },
       "name":"us-west1.17159971042783089144",
       "metadata":{
          "annotationProgress":[
             {
                "inputUri":"/video/gbikes_dinosaur.mp4",
                "updateTime":"2017-01-27T19:45:54.297807Z",
                "startTime":"2017-01-27T19:45:54.275023Z"
             }
          ],
          "@type":"type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress"
       }
    }
    

Note that the `response` field at this time only contains an `@type` field, denoting the type of that response. Once results are actually available, the response field will contain results of that type.

## Check the operation
    
    
    result = operation.result(timeout=120)
    print("\nFinished processing.")
    

Using the existing operation request for our existing operation, we construct a `while` loop to periodically check the state of that operation. Once our operation has indicated that the operation is `done`, we break out of the loop and can parse the response.

## Parse the response
    
    
    for i, shot in enumerate(result.annotation_results[0].shot_annotations):
        start_time = (
            shot.start_time_offset.seconds + shot.start_time_offset.microseconds / 1e6
        )
        end_time = (
            shot.end_time_offset.seconds + shot.end_time_offset.microseconds / 1e6
        )
        print("\tShot {}: {} to {}".format(i, start_time, end_time))

Once the operation has been completed, the response will contain an [AnnotateVideoResponse](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse), which consists of a list of `annotationResults`, one for each video sent in the request. Because we sent only one video in the request, we take the first `shotAnnotations` of the result. We walk through all the 'segments' for the video.

## Run our application

To run our application, simply pass it the Cloud Storage URI of a video:
    
    
    $ python shotchange.py gs://cloud-samples-data/video/gbikes_dinosaur.mp4
    operationId=us-west1.12468772851081463748
    Operation us-west1.12468772851081463748 started: 2017-01-30T01:53:45.981043Z
    Processing video for shot change annotations:
    Finished processing.
      Shot 0: 0.0 to 5.166666
      Shot 1: 5.233333 to 10.066666
      Shot 2: 10.1 to 28.133333
      Shot 3: 28.166666 to 42.766666
    

Congratulations! You've performed an annotation task using the Video Intelligence API!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
