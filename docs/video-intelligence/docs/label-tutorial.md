---
url: https://docs.cloud.google.com/video-intelligence/docs/label-tutorial/
title: Label Detection Tutorial \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:47.740114+00:00
---

# Label Detection Tutorial  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/label-tutorial/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Label Detection Tutorial Stay organized with collections  Save and categorize content based on your preferences. 

## Audience

This tutorial is designed to help you start exploring and developing applications with the Video Intelligence API. It's designed for people with basic familiarity with Python. You should also be able to follow along with limited programming knowledge. Having walked through this tutorial, you should be able to use the [Reference documentation](https://docs.cloud.google.com/video-intelligence/docs/reference/rest) to create your own basic applications.

This tutorial steps through a Video Intelligence API application using Python code. The purpose here is not to explain the Python client libraries, but to explain how to make calls to the Video Intelligence API using the video label detection feature. Applications in Java and Node.js are essentially similar.

_If you're looking for a code-only example or an example in another language, check out the companion[how-to guide](https://docs.cloud.google.com/video-intelligence/docs/analyze-labels)._

## Prerequisites

This tutorial has the following prerequisites:

  * You've set up a [Video Intelligence API project](https://docs.cloud.google.com/video-intelligence/docs/before-you-begin) in the Google Cloud console.
  * You've set up your environment using a service account and [Application Default Credentials](https://docs.cloud.google.com/video-intelligence/docs/common/auth#set_up_a_service_account).
  * You have basic familiarity with [Python](https://www.python.org/) programming.
  * You've set up your Python development environment.  
It's recommended that you have the latest version of Python, `pip`, and `virtualenv` installed on your system. For instructions, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup) for Google Cloud.
  * You've installed the [Google Cloud client library](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-videointelligence)



## Annotate a video using label detection

This tutorial walks you through a basic Video API application, using a `LABEL_DETECTION` request. A `LABEL_DETECTION` request annotates a video with labels (or "tags") that are selected based on the image content. For example, a video of a train at a crossing may produce labels such as "train", "transportation", "railroad crossing."

The following is the entire code needed for this tutorial. Most comments have been removed from this code to highlight how brief the code is. Instead, comments are provided later as we walk through the code.
    
    
    import argparse
    
    from google.cloud import videointelligence
    
    
    
    def analyze_labels(path):
        """Detects labels given a GCS path."""
        video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
        features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).LABEL_DETECTION]
        operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
            request={"features": features, "input_uri": path}
        )
        print("\nProcessing video for label annotations:")
    
        result = operation.result(timeout=90)
        print("\nFinished processing.")
    
        segment_labels = result.annotation_results[0].segment_label_annotations
        for i, segment_label in enumerate(segment_labels):
            print("Video label description: {}".format(segment_label.entity.description))
            for category_entity in segment_label.category_entities:
                print(
                    "\tLabel category description: {}".format(category_entity.description)
                )
    
            for i, segment in enumerate(segment_label.segments):
                start_time = (
                    segment.segment.start_time_offset.seconds
                    + segment.segment.start_time_offset.microseconds / 1e6
                )
                end_time = (
                    segment.segment.end_time_offset.seconds
                    + segment.segment.end_time_offset.microseconds / 1e6
                )
                positions = "{}s to {}s".format(start_time, end_time)
                confidence = segment.confidence
                print("\tSegment {}: {}".format(i, positions))
                print("\tConfidence: {}".format(confidence))
            print("\n")
    
    
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(
            description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
        )
        parser.add_argument("path", help="GCS file path for label detection.")
        args = parser.parse_args()
    
        analyze_labels(args.path)

This simple application performs the following tasks:

  1. Imports the libraries necessary to run the application.
  2. Takes a video file stored in Cloud Storage URI as an argument and passes it to the `main()` function.
  3. Gets credentials to run the Video Intelligence API service.
  4. Creates a video annotation request to send to the video service.
  5. Sends the request and returns a long-running operation.
  6. Loops over the long-running operation until the video is processed and returns available values.
  7. Parses the response for the service and displays the response to the user.



## Import libraries
    
    
    import argparse
    
    from google.cloud import videointelligence
    

Some standard libraries are imported: `argparse` to allow the application to accept input filenames as arguments and `sys` for formatting output while waiting for API responses. The package `time` is imported to run some simple wait loops.

When using the Video Intelligence API, you'll also need to import the `google.cloud.videointelligence_v1` and its enumeration class, which holds the directory of our API calls.

## Run the application
    
    
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("path", help="GCS file path for label detection.")
    args = parser.parse_args()
    
    analyze_labels(args.path)

Here, the passed argument is parsed for the Cloud Storage URI of the video filename and is passed to the `main()` function.

## Authenticate to the API

Before communicating with the Video Intelligence API service, you need to authenticate your service using previously acquired credentials. Within an application, the simplest way to obtain credentials is to use [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials) (ADC). By default, ADC attempts to obtain credentials from the `GOOGLE_APPLICATION_CREDENTIALS` environment file, which should be set to point to your service account's JSON key file. (You should have set up your service account and environment to use ADC in the [Quickstart](https://docs.cloud.google.com/video-intelligence/docs/getting-started).

## Construct the request
    
    
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.LABEL_DETECTION]
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": path}
    )

Now that the Video Intelligence API service is ready, you can construct a request to that service. Requests to the Video Intelligence API are provided as JSON objects. See the [Video Intelligence API Reference](https://docs.cloud.google.com/video-intelligence/docs/reference/rest) for complete information on the specific structure of such a request.

This code snippet performs the following tasks:

  1. Constructs the JSON for a POST request to the `annotate_video()` method.
  2. Injects the Cloud Storage location of the passed video filename into the request.
  3. Indicates that the `annotate` method should perform `LABEL_DETECTION`.



## Check the operation
    
    
    result = operation.result(timeout=90)
    print("\nFinished processing.")

Using the existing operation request for the existing operation, a `while` loop is constructed to periodically check the state of that operation. Once the operation has indicated that the operation is `done`, the response is parsed.

## Parse the response
    
    
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print("Video label description: {}".format(segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print(
                "\tLabel category description: {}".format(category_entity.description)
            )
    
        for i, segment in enumerate(segment_label.segments):
            start_time = (
                segment.segment.start_time_offset.seconds
                + segment.segment.start_time_offset.microseconds / 1e6
            )
            end_time = (
                segment.segment.end_time_offset.seconds
                + segment.segment.end_time_offset.microseconds / 1e6
            )
            positions = "{}s to {}s".format(start_time, end_time)
            confidence = segment.confidence
            print("\tSegment {}: {}".format(i, positions))
            print("\tConfidence: {}".format(confidence))
        print("\n")

Once the operation has been completed, the response will contain the result within an [AnnotateVideoResponse](https://docs.cloud.google.com/video-intelligence/docs/reference/rest/Shared.Types/AnnotateVideoResponse), which consists of a list of `annotationResults`, one for each video sent in the request. Because only one video was sent in the request, the first `segmentLabelAnnotations` of the results is taken, all the labels in `segmentLabelAnnotations` are looped through. By using only `segmentLabelAnnotations`, this tutorial displays only video-level annotations. Each `segment_label` includes a description (`segment_label.description`), a list of entity categories (`segment_label.category_entities`), and a list of segments identifying the start/end time of the label occurrences in the video (should be one segment spanning the whole video or video segment for the case of `segment_label_annotations`).
    
    
    {
       "name":"us-west1.12089999971048628582",
       "metadata":{
          "@type":"type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoProgress",
          "annotationProgress":[
             {
                "inputUri":"gs://YOUR_BUCKET/YOUR_OBJECT",
                "updateTime":"2020-01-31T01:49:52.498015Z",
                "startTime":"2020-01-31T01:49:43.056481Z"
             }
          ]
       },
       "done": true,
       "response":{
          "@type":"type.googleapis.com/google.cloud.videointelligence.v1.AnnotateVideoResponse",
          "annotationResults":[
             {
                "inputUri":"gs://YOUR_BUCKET/YOUR_OBJECT",
                "segmentLabelAnnotations": [
                  {
                    "entity": {
                      "entityId": "/m/01yrx",
                      "languageCode": "en-US"
                    },
                    "segments": [
                      {
                        "segment": {
                          "startTimeOffset": "0s",
                          "endTimeOffset": "14.833664s"
                        },
                        "confidence": 0.98509187
                      }
                    ]
                  },
                   ...
                ]
             }
          ]
       }
    }
    

Because only one video was sent in the request, the first `description` of the first result is printed.

## Run your application

To run your application, simply pass it the Cloud Storage URI of a video:
    
    
    $ python labels.py gs://YOUR_BUCKET/YOUR_OBJECT
    Operation us-west1.4757250774497581229 started: 2020-01-30T01:46:30.158989Z
    Operation processing ...
    The video has been successfully processed.
    
    Video label description: urban area
            Label category description: city
            Segment 0: 0.0s to 38.752016s
            Confidence: 0.946980476379
    
    
    Video label description: traffic
            Segment 0: 0.0s to 38.752016s
            Confidence: 0.94105899334
    
    
    Video label description: vehicle
            Segment 0: 0.0s to 38.752016s
            Confidence: 0.919958174229
    ...
     

## Output

Below is an example of a possible output. 
    
    
    Processing video for label annotations:
    
    
    
    Finished processing.
    Video label description: crowd
            Label category description: people
            Segment 0: 0.0s to 60.24s
            Confidence: 0.527720749378
    
    
    
    
    
    Video label description: official
            Label category description: person
            Segment 0: 0.0s to 60.24s
            Confidence: 0.372822880745
    
    
    
    
    
    Video label description: audience
            Label category description: people
            Segment 0: 0.0s to 60.24s
            Confidence: 0.501719772816
    
    
    
    
    
    Video label description: news
            Segment 0: 0.0s to 60.24s
            Confidence: 0.867252230644
    
    
    
    
    
    Video label description: people
            Label category description: person
            Segment 0: 0.0s to 60.24s
            Confidence: 0.46747264266
    
    
    
    
    
    Video label description: politics
            Segment 0: 0.0s to 60.24s
            Confidence: 0.319397002459
    
    
    
    

Congratulations! You've performed an annotation task using the Video Intelligence API!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
