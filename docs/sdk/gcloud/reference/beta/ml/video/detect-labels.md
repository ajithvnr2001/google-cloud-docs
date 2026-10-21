---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/video/detect-labels/
title: gcloud beta ml video detect-labels \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:45:10.457793+00:00
---

# gcloud beta ml video detect-labels  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/video/detect-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml video detect-labels Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml video detect-labels - detect general labels for videos 
SYNOPSIS
    

`gcloud beta ml video detect-labels` `INPUT_PATH` [`--async`] [`--detection-mode`=`DETECTION_MODE`; default="shot"] [`--output-uri`=`OUTPUT_URI`] [`--region`=`REGION`] [`--segments`=[`SEGMENTS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Detect general categories in videos, such as modes of transportation or animals. Use the --detection-mode flag to control whether labels are detected for shots, frames, or both. 
EXAMPLES
     To detect labels in video file 'gs://my_bucket/input_file.mp4': 
    
    
    gcloud beta ml video detect-labels gs://my_bucket/input_file.mp4

POSITIONAL ARGUMENTS
    

`INPUT_PATH`
     Path to the video to be analyzed. Must be a local path or a Google Cloud Storage URI. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--detection-mode`=`DETECTION_MODE`; default="shot"
     The mode of label detection requested. `DETECTION_MODE` must be one of: 

`frame`
     Detect labels at the per-frame level. 
`shot`
     Detect labels at the per-shot level. 
`shot-and-frame`
     Detect labels at both the per-shot and per-frame level. 
`--output-uri`=`OUTPUT_URI`
     Location to which the results should be written. Must be a Google Cloud Storage URI. 
`--region`=`REGION`
     Optional Cloud region where annotation should take place. If no region is specified, a region will be determined based on video file location. `REGION` must be one of: `asia-east1`, `europe-west1`, `us-east1`, `us-west1`. 
`--segments`=[`SEGMENTS`,…]
     Segments from the video which you want to analyze (by default, the entire video will be treated as one segment). Must be in the format START1:END1[,START2:END2,…] (inclusive). START and END of segments must be a properly formatted duration string of the form `HhMmSs` where: 
    
    
    *  H is the number of hours from beginning of video
    *  M is the number of minutes from the beginning of video
    *  S is the number of seconds from the beginning of the video

H, M and S can be specified as ints or floats for fractional units (to microsecond resolution). Unit chars (e.g. `h`, `m` or `s`) are required. Microseconds can be specified using fractional seconds e.g. 0.000569s == 569 microseconds. 

Examples: 

0s:23.554048s,24s:29.528064s 

0:1m40s,3m50s:5m10.232265s 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `videointelligence/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/video-intelligence/docs/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ml video detect-labels](https://docs.cloud.google.com/sdk/gcloud/reference/ml/video/detect-labels)
    
    
    [gcloud alpha ml video detect-labels](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/video/detect-labels)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
