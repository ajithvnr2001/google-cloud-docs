---
url: https://docs.cloud.google.com/transcoder/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Transcoder API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:11.852616+00:00
---

# Troubleshooting  |  Transcoder API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/transcoder/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Transcoder API ](https://docs.cloud.google.com/transcoder/docs)
  * [ Guides ](https://docs.cloud.google.com/transcoder/docs/transcode-video)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Transcoder API. The errors shown on this page are specific to the Transcoder API. For information on generic errors across Google APIs, see the Cloud APIs [Errors](https://docs.cloud.google.com/apis/design/errors) page.

The service reports errors using the [`error`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.error) field of the job resource. This field contains an object of type [`google.rpc.Status`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Status). This object contains additional error information, including the error code, error message, and error details.

Only the first error is returned. If a job encounters multiple errors, you need to fix the returned error and recreate the job to see the next error.

## Cloud Storage permission denied

The following issue occurs when the Transcoder API service account doesn't have read/write permission for input or output on a location in Cloud Storage.
    
    
    {
       "code":7, # HTTP error code 403
       "message":"Permission denied for Google Cloud Storage.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.ErrorInfo",
             "reason":"GCSPermissionDenied",
             "domain":"transcoder.googleapis.com",
             "metadata":{
               "details":"my_service_account@my_project.iam.gserviceaccount.com does
                 not have storage.objects.get access to gs://example/input/video.mp4."
             }
          }
    }
    

To resolve this issue, make sure the automatically created service account has the correct permissions. See [Access to Cloud Storage and Pub/Sub](https://docs.cloud.google.com/transcoder/docs/access-control#access_to_gcs_pubsub) for more information on the service account.

## Pub/Sub permission denied

The following issue occurs when the Transcoder API service account doesn't have the proper permissions for publishing to a Pub/Sub topic.
    
    
    {
       "code":7, # HTTP error code 403
       "message":"Permission denied for PubSub.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.ErrorInfo",
             "reason":"PubSubPermissionDenied",
             "domain":"transcoder.googleapis.com",
             "metadata":{
               "details":"my_service_account@my_project.iam.gserviceaccount.com does not
                 have pubsub.topic.publish access to /projects/test-project/topic/test-topic."
             }
          }
    }
    

To resolve this issue, make sure the automatically-created service account has the correct permissions. See section [Access to Cloud Storage and Pub/Sub](https://docs.cloud.google.com/transcoder/docs/access-control#access_to_gcs_pubsub) for more information on the service account.

## Invalid Pub/Sub destination

The following issue occurs when the Pub/Sub destination is an invalid Pub/Sub topic resource path.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"No video stream found in ffprobe output.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.pubsubDestination.topic",
             "description":"InvalidPubsubDestination"
          }
       ]
    }
    

To resolve this issue, make sure the Pub/Sub topic exists and is specified in the correct format. See [Pub/Sub notifications for job updates](https://docs.cloud.google.com/transcoder/docs/how-to/create-pub-sub) for more information.

## Input not found

The following issue occurs when the input file cannot be found on Cloud Storage.
    
    
    {
        "code": 5, # HTTP error code 404
        "message": "No such object: my-bucket/input.mp4",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "InputNotFound",
            "domain": "transcoder.googleapis.com",
            "metadata": {
              "details": "No such object:  my-bucket/input.mp4"
            }
          }
        ]
    }
    

To resolve this issue, make sure the input file exists, the [`inputUri`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job.FIELDS.input_uri) to the file is correct, and that the Transcoder API service account has permissions to access the file. If the input file exists in a different project, you may need to make the Cloud Storage bucket public (see Cloud Storage [Access control](https://docs.cloud.google.com/storage/docs/access-control) for more information).

## Configuration missing

The following issue occurs when a job configuration field is missing.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"endTimeOffset of atom atom0 not set.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.editList[0].endTimeOffset",
             "description":"ConfigurationMissing"
          }
       ]
    }
    

To resolve this issue, check the [`JobConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) field mentioned in the error message.

## Invalid configuration value

The following issue occurs when the job configuration contains an invalid value.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"config.inputs[1].preprocessingConfig.crop is invalid, the input (input0)
         to have a video track with width and height",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.input[1].processingConfig.crop",
             "description":"InvalidConfigValue"
          }
       ]
    }
    

To resolve this issue, check the [`JobConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) field mentioned in the error message.

## Invalid time offset

The following issue occurs when the start time offset or end time offset in the job configuration is not valid.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"Request field config.editList[0].startTimeOffset is 200s, expected
         start time less than the minimum duration of all inputs for this atom (198.86s).",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.editList[0].startTimeOffset",
             "description":"InvalidTimeOffset"
          }
       ]
    }
    

To resolve this issue, make sure that [`endTimeOffset`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#EditAtom.FIELDS.end_time_offset) is larger than [`startTimeOffset`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#EditAtom.FIELDS.start_time_offset). Both offsets should not exceed the duration of the input files.

## Exceed transcode limits

The following issue occurs when an input or the input configuration exceeds the limits for the service.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"at most 400 GB input.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.editList[0].startTimeOffset",
             "description":"ExceedTranscodeLimit"
          }
       ]
    }
    

To resolve this issue, make sure the job configuration stays within the [service limits](https://docs.cloud.google.com/transcoder/docs/concepts/overview#limits).

## Video missing

The following issue occurs when no video stream is specified in the configuration or no video is detected in the input file.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"No video stream found in ffprobe output.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.input",
             "description":"VideoMissing"
          }
       ]
    }
    

To resolve this issue, check that a video stream is specified in the [job configuration](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) and that the input file contains a video stream.

## Audio missing

The following issue occurs when no audio track is specified in the [`editList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.edit_list) or no audio track is detected in the input file.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"atom atom0 does not have any inputs (input0) with an audio track.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.editList[0].input[0]",
             "description":"AudioMissing"
          }
       ]
    }
    

To resolve this issue, check that an audio track is specified in the job configuration and that the input file contains an audio track.

## Text missing

The following issue occurs when a [text stream](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#ElementaryStream.FIELDS.text_stream) is specified, but no text track is available in the edit list or in the input file.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"atom atom0 does not have any inputs (input0) with a text track.",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.editList[0].input[0]",
             "description":"TextMissing"
          }
       ]
    }
    

If a text track is specified in the job configuration, make sure one exists in the [`editList`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#FIELDS.edit_list) and the input file. See an [example configuration](https://docs.cloud.google.com/transcoder/docs/concepts/config-examples#text_stream).

## Valid track or channel missing

The following issue occurs when the input track or channel in an elementary stream mapping doesn't refer to a valid audio/text stream track or channel.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"Request field config.elementaryStreams[0].mapping[0].channels[0].inputs[0].track
         is 2, no valid audio track available, expected an index to a valid audio track in input
         input0.",
       "details":[
             "@type":"type.googleapis.com/google.rpc.BadRequest",
             "field":"config.elementaryStreams[0].mapping[0].channels[0].inputs[0].track",
             "description":"ValidTrackOrChannelMissing"
       ]
    }
    

To resolve this issue, check the input video/audio/text and the elementary stream mapping (see [example stream mappings](https://docs.cloud.google.com/transcoder/docs/concepts/stream-mappings)).

## Unsupported input

The following issue occurs when the input file is corrupt or not in a supported format.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"Input files are not supported",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "UnsupportedInput",
            "domain": "transcoder.googleapis.com",
            "metadata": {
              "details": "Input is not supported. Input key = example_key, input uri = gs://example/input/video.mp4."
            }
          }
        ]
    }
    

To resolve this issue, check that the input file is valid and in a [supported format](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).

## Malformed input

The following issue occurs when the input file is malformed and cannot be decoded.
    
    
    {
       "code":3, # HTTP error code 400
       "message":"Input is malformed and cannot be decoded.",
       "details": [
          {
            "@type": "type.googleapis.com/google.rpc.ErrorInfo",
            "reason": "MalformattedInput",
            "domain": "transcoder.googleapis.com",
            "metadata": {
              "details": "Input is malformed. Input key = example_key, input uri = gs://example/input/video.mp4."
            }
          }
        ]
    }
    

To resolve this issue, check that the input file is valid and in a [supported format](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).

## Internal error

The following issue occurs when an internal service error prevented the job from completing successfully.
    
    
    {
       "code":13, # HTTP error code 500
       "message":"InternalError",
       "details":[
          {
             "@type":"type.googleapis.com/google.rpc.ErrorInfo",
             "reason":"InternalError",
             "domain":"transcoder.googleapis.com",
             "metadata":{
                "details":"Failed to transcode job"
             }
          }
       ]
    }
    

To try to resolve the issue, do the following:

  1. Check that the input file is valid and in a [supported format](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).
  2. Check that the [`JobConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) is free from errors.
  3. Retry the job in a [different location](https://docs.cloud.google.com/transcoder/docs/locations).
  4. Retry the job with [`optimization`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#optimizationstrategy) disabled.



See [Getting support](https://docs.cloud.google.com/transcoder/docs/getting-support) for further support options.

## Quality issues

If you encounter poor video or audio quality in the output, such as artifacts, missing frames, A/V synchronization issues, it might be due to input file characteristics like non-standard packaging or encoding. Here are some steps you can take to mitigate these issues:

  1. Check that the input file is valid and in a [supported format](https://docs.cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats).
  2. Check that the [`JobConfig`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig) is free from errors and uses the [recommended encoding profiles](https://docs.cloud.google.com/transcoder/docs/concepts/config-examples#transcoding-multiple-profiles).
  3. Retry the job with [`optimization`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#optimizationstrategy) disabled.
  4. Retry the job with [`fillContentGaps`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job) set to `true` and [`frameRateConversion`](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/JobConfig#framerateconversionstrategy) set to `DROP_DUPLICATE`.



See [Getting support](https://docs.cloud.google.com/transcoder/docs/getting-support) for further support options.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
