---
url: https://docs.cloud.google.com/vision-ai/docs/motion-filtering-model/
title: Motion filtering guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:57.639070+00:00
---

# Motion filtering guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/motion-filtering-model/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Motion filtering guide Stay organized with collections  Save and categorize content based on your preferences. 

The **Motion filter** model allows you to reduce computation time by trimming down long video sections into smaller segments that contain a motion event. This model lets you set the motion sensitivity, the minimum event length, the lookback window, and the cooldown period to adjust the outputs of the motion events to your use case.

## Model parameters

The motion filter model has four control parameters to adjust the event segments and how the model returns them.

Parameter | Description | Flag | Default value | Available values  
---|---|---|---|---  
Minimum event length | The minimum length a motion event will be captured after a motion event has ended in seconds.  | `--min-event-length INT` | 10 (seconds) | 1 - 3600  
Motion detection sensitivity | The sensitivity of the model's motion event filtering. High sensitivity is more responsive to motion and provides more aggressive motion filtering, resulting in more motion detected.  | `--motion-sensitivity STRING` | `"medium"` | `"high"`, `"medium"`, or `"low"`  
Lookback window | The amount of video content (in seconds) the service captures before a detected motion event.  | `--lookback-length INT` | 3 (seconds) | 0 - 300  
Cooldown period | After a motion event ends, a cooldown period with the specified duration occurs. During the cooldown period, the model doesn't register motion events.  | `--cooldown-length INT` | 300 (seconds) | 0 - 3600  
  
### Motion sensitivity

When running the motion filter, motion sensitivity plays the most important role in determining how many segment videos the model creates from a video stream.

The higher the motion detection sensitivity, the more sensitive the model detection is to noise and smaller movements. This higher sensitivity setting is recommended for settings that contain stable lighting and shows smaller moving objects (such as views of people seen from a distance).

Conversely, low sensitivity is least sensitive to lighting interference and small movements. This setting is good for situations that have more lighting interference, such as an outdoor environment. Because this setting is the most aggressive filtering option, it ignores movements from small objects.

### Minimum event length

Minimum event length is the duration of video the model captures after it stops detecting a motion event in the frame. The default value is 10 seconds, but you can specify a time between 1 second and 3,600 seconds. If a new motion is detected during the minimum event length, the new motion is added to the current video segment for the duration of the newly detected motion event _plus_ a new countdown of the minimum event length.

![minimum event length diagram](https://docs.cloud.google.com/static/vision-ai/docs/images/min-event-length-diagram.png)

For example, consider a video of a crossroad with two cars moving in the frame. The first car passes by in the first three seconds, and the second car comes two seconds after. If you set the minimum event length to one second, there are two video segments with motion. One video segment contains the first car, while the other segment contains the second car. However, if you set the motion event to three seconds, there is only one resulting video segment with motion. The second car appears in the frame only two seconds after the first car.

When you set the minimum event length, think about how often motion events usually occur in your video and how many video segments you want to save. If motion events happen frequently but you wish to have most motion events saved in separate video segments, then set the minimum event length to a shorter period. If motion events happen infrequently but you want to group events together, set the minimum event length to a longer period to capture multiple events in the same video segment.

### Lookback window

The lookback window is the time just preceding the moment when a motion event is detected. This window is useful when you want to see what happens in the frame seconds before the model detects a motion event. The default value for the lookback window is three seconds, but you can specify between zero and 300 seconds.

You can use a lookback window to see where moving objects originated. You can also use a lookback window to see what was in the frame seconds before the motion event occurred. A lookback window is helpful in situations where there are small moving objects in the frame that don't get detected as a motion event. However, the small moving objects in the frame might have caused the bigger motion events that were detected.

### Cooldown period

A cooldown period is a duration that happens after a motion event and a minimum event length are captured. During the cooldown period, the motion detected doesn't trigger the motion filter. The range of this period is between zero second and 3,600 seconds. The default is set to 300 seconds.

The cooldown period is designed for users to save computation costs. If movements in a frame are expected and you are only interested in learning when the motion happens but don't care what happens afterwards, then a cooldown period is a useful setting.

## Use the model

You can use the motion filter model using the [Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment).

Use the `vaictl` command line tool to enable the model by specifying `applying encoded-motion-filter` and passing in values to set control parameters.

###  Gemini Enterprise Agent Platform Vision SDK 

To send a request using the motion filter model, you must [install the Gemini Enterprise Agent Platform Vision SDK](https://docs.cloud.google.com/vision-ai/docs/cloud-environment#install_the_streams_sdk).

**Note:** You might need to establish user access credentials by running the following command: `gcloud auth application-default login`. [View more information](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login).

Make the following variable substitutions:

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: Your location ID. For example, `us-central1`. [Supported regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). [More information](https://docs.cloud.google.com/about/locations).
  * LOCAL_FILE.EXT: The filename of a local video file. For example, `my-video.mp4`.
  * STREAM_ID: The stream ID that you created in the cluster. For example, `input-stream`.
  * `--motion-sensitivity`: The sensitivity of the motion event filtering. Options are `high`, `medium`, `low`.
  * `--min-event-length`: The minimum duration of a motion event in seconds. The default value is `10` seconds. Available values: `1`-`3600`.
  * `--lookback-length`: The duration of the lookback window before the motion event starts in seconds. The default value is `3` seconds. Available values: `0`-`300`.
  * `--cooldown-length`: The cooldown period after a motion event occurs in seconds. The default value is `300` seconds (5 minutes). Available values: `0`-`3600`.
  * `--continuous-mode`: Whether to send in continuous mode. Default value is `true`.
  * OUTPUT_DIRECTORY: The directory you want to save the output video segment MP4 files.



**View command information**

Use the following command to view more information about the command and its optional parameters:
    
    
    vaictl send video-file applying motion-filter -h
    

**Filter local file content using the motion filter model**

This command sends only video sections where the model detects motion.
    
    
    vaictl -p PROJECT_ID \
          -l LOCATION_ID \
          -c application-cluster-0 \
          --service-endpoint visionai.googleapis.com \
    send video-file  --file-path LOCAL_FILE.EXT \
    applying motion-filter --motion-sensitivity=medium \
          --min-event-length=10 --lookback-length=3 --cooldown-length=0 \
    to streams STREAM_ID --loop
    

**Filter local file content and save output using the motion filter model**

This command uses the `--continuous_mode` flag to output separate video files for every motion segment.
    
    
    vaictl -p PROJECT_ID \
          -l LOCATION_ID \
          -c application-cluster-0 \
          --service-endpoint visionai.googleapis.com \
    send video-file --file-path LOCAL_FILE.EXT **--continuous-mode= false** \
    applying motion-filter --motion-sensitivity=medium \
          --min-event-length=10 --lookback-length=3 --cooldown-length=0 \
    to mp4file --mp4-file-path=OUTPUT_DIRECTORY
    

## Best practices

The motion filter is designed to be a light-weight model to help reduce computation time in decoding encoded videos during transmission. To best operate the filter, place a still camera directly at the objects of interest. Avoid including unimportant moving objects in the background of the frame. For example, a frame that contains background objects like moving trees, constant car flow, or shadows of moving objects detects the motion of these unimportant subjects.

Place objects of interest in the foreground and reduce the amount of background objects with constant movement as much as possible. To summarize:

  * Use a still camera.
  * Make sure to avoid a constant moving background.
  * Minimal movements won't be detected.
  * Make sure objects are sufficiently large.



### Indoor best practices

For indoor environments that have constant lighting and minimal background movement, follow these indoor best practices:

  * Increase sensitivity. Objects in the frame tend to be larger, and there is less noise in the frame as well.
  * Use smaller lookback windows and a shorter event length. Indoor movements are slower, and there is limited space in which movements can occur.



Following these indoor practices enables the motion filter to record object movement in a minimal time.

### Outdoor best practices

For outdoor environments, there are more variables in outdoor scenes that might affect the performance of the filter. For instance, the shadow from a moving tree or changes in sunlight in the frame are detected movement for the motion filter model. Consider the following conditions and the best way to respond to them.

**Situation 1:**

Consider a video that captures a sidewalk where pedestrians walk by occasionally. These movements can be as slow as casual walking or as fast as a skateboard passing. Use the following guidance:

  * Set a minimum window length and lookback window to a longer value. The speed of the motions has a bigger range than the indoor scenario, so increasing the minimum window length and lookback window lets the model capture the full motion event.
  * Set the motion sensitivity higher. An outdoor environment contains more naturally moving objects such as moving trees and shadows. To focus only on objects of interest such as humans and bicycles, set motion sensitivity higher to avoid constant detection of background objects.



**Situation 2:**

Consider a different video that focuses on a street where cars constantly drive by and pedestrians walk by occasionally. Use the following guidance:

  * Set sensitivity to medium or low: A lower sensitivity setting lets the model capture a variety of moving object sizes in the frame.
  * Set the lookback window and minimum event length to a shorter value. Cars and other vehicles on the street move at a significantly faster speed than humans and bikes. Setting a shorter value for these parameters accounts for the fact that the speed of motion is greater, and that objects enter and exit the frame quickly.
  * Set a short cooldown time. Due to the greater speed of motion, the next object might enter the frame shortly after the first object. Consequently a shorter cooldown time accounts for this.



## Limitations

As the motion filter depends largely on the motion vector in each frame, there are certain limitations to keep in mind.

  1. Camera angle: Use a still camera, as a moving camera constantly has motion in its frame.
  2. Object size: Try to frame subjects so that key objects appear large enough in the frame to achieve the best performance by the motion filter.
  3. Lighting: Lighting changes - such as a sudden brightness change in the frame or intense shadow movements - might degrade the model performance. A low dynamic range that results in a similar brightness tone for the overall video, which affects how the model interprets motion and degrades the model performance.
  4. Camera positioning: The model is designed to detect movement in the frame. This includes background movement such as the wind moving a tree or objects out of frame creating shadows. Having a large portion of the frame pointing at background objects that create these movements might impact model performance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
