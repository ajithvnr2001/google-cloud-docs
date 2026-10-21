---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/video/detect-text/
title: gcloud beta ml video detect-text \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:38:59.819611+00:00
---

# gcloud beta ml video detect-text  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ml/video/detect-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ml video detect-text Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ml video detect-text - detect text in videos 
SYNOPSIS
    

`gcloud beta ml video detect-text` `INPUT_PATH` [`--async`] [`--language-hints`=[`LANGUAGE_HINTS`,…]] [`--output-uri`=`OUTPUT_URI`] [`--region`=`REGION`] [`--segments`=[`SEGMENTS`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Detect text in videos. 
EXAMPLES
     To detect text in video file 'gs://my_bucket/input_file.mp4': 
    
    
    gcloud beta ml video detect-text gs://my_bucket/input_file.mp4

POSITIONAL ARGUMENTS
    

`INPUT_PATH`
     Path to the video to be analyzed. Must be a local path or a Google Cloud Storage URI. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--language-hints`=[`LANGUAGE_HINTS`,…]
     Language hints can be specified if the languages to be detected are known beforehand. It can increase the accuracy of the detection. Language hints must be language codes in BCP-47 format. Automatic language detection is performed if no language hints are provided. 
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
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha ml video detect-text](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ml/video/detect-text)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
