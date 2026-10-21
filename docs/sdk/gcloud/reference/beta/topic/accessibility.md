---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/accessibility/
title: gcloud beta topic accessibility \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:28.264359+00:00
---

# gcloud beta topic accessibility  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/topic/accessibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta topic accessibility Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta topic accessibility - reference for `Accessibility` features 
DESCRIPTION
     `(BETA)` The `accessibility/screen_reader` property when set to true will change some behavior to make gcloud more screen reader friendly. Currently the following changes are implemented: 

  * For progress trackers, instead of unicode spinners, the phrase 'working' is displayed on stderr, every second while gcloud is working. 
  * For progress bars, progress is displayed as a percentage, outputted to stderr. 
  * For boxed tables, instead of the queried resources being displayed in tables drawn in Unicode, results are rendered as a flattened list of items. Also consider using the --format flag to define your own format. 



To turn this on, run: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) accessibility/screen_reader true

Accessibility support is still in early stages. Please report any issues that you would like fixed using `[gcloud feedback](https://docs.cloud.google.com/sdk/gcloud/reference/feedback)`. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud topic accessibility](https://docs.cloud.google.com/sdk/gcloud/reference/topic/accessibility)
    
    
    [gcloud alpha topic accessibility](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/topic/accessibility)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
