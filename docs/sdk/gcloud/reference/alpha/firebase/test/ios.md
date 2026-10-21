---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/
title: gcloud alpha firebase test ios \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:16.689298+00:00
---

# gcloud alpha firebase test ios  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha firebase test ios Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha firebase test ios - command group for iOS application testing 
SYNOPSIS
    

`gcloud alpha firebase test ios` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Explore physical iOS devices and iOS versions which are available as test targets. Also run tests against your iOS app on these devices, monitor your test progress, and view detailed test results in the Firebase console. 
EXAMPLES
     To see a list of available iOS devices and supported iOS versions, run: 
    
    
    [gcloud alpha firebase test ios models list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/models/list)

To view information about a specific iOS model, run: 
    
    
    [gcloud alpha firebase test ios models describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/models/describe) MODEL_ID

To view details about all iOS versions, run: 
    
    
    [gcloud alpha firebase test ios versions list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/versions/list)

To view information about a specific iOS version, run: 
    
    
    [gcloud alpha firebase test ios versions describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/versions/describe) VERSION_ID

To view all options available for iOS tests, run: 
    
    
    [gcloud alpha firebase test ios run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/run) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[locales](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/locales)`
     `(ALPHA)` Explore iOS locales available for testing. 
`[models](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/models)`
     `(ALPHA)` Explore iOS models available in the Test Environment catalog. 
`[versions](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/versions)`
     `(ALPHA)` Explore iOS versions available for testing. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[list-device-capacities](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/list-device-capacities)`
     `(ALPHA)` List capacity information for iOS models & versions. 
`[run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/ios/run)`
     `(ALPHA)` Invoke a test in Firebase Test Lab for iOS and view test results. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud firebase test ios](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/ios)
    
    
    [gcloud beta firebase test ios](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/ios)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
