---
url: https://docs.cloud.google.com/sdk/gcloud/reference/components/repositories/
title: gcloud components repositories \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:30.273353+00:00
---

# gcloud components repositories  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/components/repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud components repositories Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud components repositories - manage additional component repositories for Trusted Tester programs 
SYNOPSIS
    

`gcloud components repositories` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List, add, and remove component repositories for Trusted Tester programs. If you are not participating in a Trusted Tester program, these commands are not necessary for updating your Google Cloud CLI installation. 

If you are participating in a Trusted Tester program, you will be instructed on the location of repositories that you should add. These commands allow you to manage the set of repositories you have registered. 

Once you have a repository registered, the component manager will use that location to locate new Google Cloud CLI components that are available, or possibly different versions of existing components that can be installed. 

If you want to revert to a standard version of the Google Cloud CLI at any time, you may remove all repositories and then run: 
    
    
    [gcloud components update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update)

to revert to a standard installation. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[add](https://docs.cloud.google.com/sdk/gcloud/reference/components/repositories/add)`
     Add a new Trusted Tester component repository. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/components/repositories/list)`
     List any Trusted Tester component repositories you have registered. 
`[remove](https://docs.cloud.google.com/sdk/gcloud/reference/components/repositories/remove)`
     Remove a registered Trusted Test component repository. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
