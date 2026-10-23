---
url: https://docs.cloud.google.com/video-intelligence/docs/streaming/action-recognition/
title: Action recognition \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:04.197814+00:00
---

# Action recognition  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/streaming/action-recognition/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/video-intelligence/docs/annotate-video-command-line)



Send feedback 

#  Action recognition Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Action recognition identifies different actions from video clips, such as walking or dancing. Each of the actions may or may not be performed throughout the entire duration of the video.

## Using an AutoML model

### Before you begin

For background on creating an AutoML model, check out the Vertex AI [Beginner's guide](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide#video). For instructions on how to create your AutoML model, see [Video data](https://docs.cloud.google.com/vertex-ai/docs/training-overview#video_data) in "Develop and use ML models" in the Vertex AI documentation.

### Use your AutoML model

The following code sample demonstrates how to use your [AutoML model](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide#video) for action recognition using the streaming client library.

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import io
    
    from google.cloud import videointelligence_v1p3beta1 as videointelligence
    
    # path = 'path_to_file'
    # project_id = 'project_id'
    # model_id = 'automl_action_recognition_model_id'
    
    client = videointelligence.StreamingVideoIntelligenceServiceClient()
    
    model_path = "projects/{}/locations/us-central1/models/{}".format(
        project_id, model_id
    )
    
    automl_config = videointelligence.StreamingAutomlActionRecognitionConfig(
        model_name=model_path
    )
    
    video_config = videointelligence.StreamingVideoConfig(
        feature=videointelligence.StreamingFeature.STREAMING_AUTOML_ACTION_RECOGNITION,
        automl_action_recognition_config=automl_config,
    )
    
    # config_request should be the first in the stream of requests.
    config_request = videointelligence.StreamingAnnotateVideoRequest(
        video_config=video_config
    )
    
    # Set the chunk size to 5MB (recommended less than 10MB).
    chunk_size = 5 * 1024 * 1024
    
    def stream_generator():
        yield config_request
        # Load file content.
        # Note: Input videos must have supported video codecs. See
        # https://cloud.google.com/video-intelligence/docs/streaming/streaming#supported_video_codecs
        # for more details.
        with io.open(path, "rb") as video_file:
            while True:
                data = video_file.read(chunk_size)
                if not data:
                    break
                yield videointelligence.StreamingAnnotateVideoRequest(
                    input_content=data
                )
    
    requests = stream_generator()
    
    # streaming_annotate_video returns a generator.
    # The default timeout is about 300 seconds.
    # To process longer videos it should be set to
    # larger than the length (in seconds) of the video.
    responses = client.streaming_annotate_video(requests, timeout=900)
    
    # Each response corresponds to about 1 second of video.
    for response in responses:
        # Check for errors.
        if response.error.message:
            print(response.error.message)
            break
    
        for label in response.annotation_results.label_annotations:
            for frame in label.frames:
                print(
                    "At {:3d}s segment, {:5.1%} {}".format(
                        frame.time_offset.seconds,
                        frame.confidence,
                        label.entity.entity_id,
                    )
                )

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
