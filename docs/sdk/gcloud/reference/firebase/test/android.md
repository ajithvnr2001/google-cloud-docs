---
url: https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/
title: gcloud firebase test android \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:47.369484+00:00
---

# gcloud firebase test android  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud firebase test android Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud firebase test android - command group for Android application testing 
SYNOPSIS
    

`gcloud firebase test android` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Explore physical and virtual Android models, Android OS versions, and Android locales which are available as test targets. Also run tests against your Android app on these devices, monitor your test progress, and view detailed test results in the Firebase console. 
EXAMPLES
     To see a list of available Android devices, their form factors, and supported Android OS versions, run: 
    
    
    [gcloud firebase test android models list](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/list)

To view more detailed information about a specific Android model, run: 
    
    
    [gcloud firebase test android models describe](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/models/describe) MODEL_ID

To view details about available Android OS versions, such as their code names and release dates, run: 
    
    
    [gcloud firebase test android versions list](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/list)

To view information about a specific Android OS version, run: 
    
    
    [gcloud firebase test android versions describe](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions/describe) VERSION_ID

To view the list of available Android locales which can be used for testing internationalized applications, run: 
    
    
    [gcloud firebase test android locales list](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales/list)

To view information about a specific locale, run: 
    
    
    [gcloud firebase test android locales describe](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales/describe) LOCALE

To view all options available for running Android tests, run: 
    
    
    [gcloud firebase test android run](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/run) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[locales](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/locales)`
     Explore Android locales available for testing. 
`[models](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/models)`
     Explore Android models available in the Test Environment catalog. 
`[versions](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/versions)`
     Explore Android versions available for testing. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[list-device-capacities](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/list-device-capacities)`
     List capacity information for Android models & versions. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/android/run)`
     Invoke a test in Firebase Test Lab for Android and view test results. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha firebase test android](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/android)
    
    
    [gcloud beta firebase test android](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/android)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
