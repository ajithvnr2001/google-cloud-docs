---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/network-profiles/
title: gcloud beta firebase test network-profiles \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:31.909957+00:00
---

# gcloud beta firebase test network-profiles  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/network-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta firebase test network-profiles Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta firebase test network-profiles - explore network profiles available for testing 
SYNOPSIS
    

`gcloud beta firebase test network-profiles` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` A network traffic profile consists of a set of parameters to emulate network conditions when running a test. This feature only works on physical devices. The network shaping parameters are: 

  * `RULE`: Where to apply traffic shaping. The UP rule shapes the connection from the device to the internet. The DOWN rule shapes the connection from the internet to the device. 
  * `DELAY`: The delay in packet transmission, in ms. 
  * `LOSS_RATIO`: The ratio of packets dropped during transmission. 
  * `DUPLICATION_RATIO`: The ratio of packets duplicated during transmission. 
  * `BANDWIDTH`: The average packet transmission rate in kbits/s, as defined by the token bucket algorithm. 
  * `BURST`: The total size, in kbits, by which packets can exceed the bandwidth, as defined by the token bucket algorithm. 


EXAMPLES
     To list all network profiles which can be used for testing, run: 
    
    
    [gcloud beta firebase test network-profiles list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/network-profiles/list)

To view information about a specific network profile, run: 
    
    
    [gcloud beta firebase test network-profiles describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/network-profiles/describe) PROFILE_ID

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/network-profiles/describe)`
     `(BETA)` Describe a network profile. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/firebase/test/network-profiles/list)`
     `(BETA)` List all network profiles available for testing. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud firebase test network-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/firebase/test/network-profiles)
    
    
    [gcloud alpha firebase test network-profiles](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/firebase/test/network-profiles)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
