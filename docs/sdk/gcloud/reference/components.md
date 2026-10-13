---
url: https://docs.cloud.google.com/sdk/gcloud/reference/components/
title: gcloud components \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:34:30.541044+00:00
---

# gcloud components  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud components Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud components - list, install, update, or remove Google Cloud CLI components 
SYNOPSIS
    

`gcloud components` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The gcloud components command group lets you control which tools are installed in the Google Cloud CLI. It can be used to install, update and remove components of the Google Cloud CLI, ensuring a lean, up-to-date installation. 

gcloud components regularly checks whether updates are available for the tools you already have installed, and gives you the opportunity to upgrade to the latest version. 

Certain components have dependencies. gcloud components will install any dependencies, and during removal, any dependant components will be uninstalled automatically. 

EXAMPLES
     To see all available components: 
    
    
    [gcloud components list](https://docs.cloud.google.com/sdk/gcloud/reference/components/list)

To install a component you don't have: 
    
    
    [gcloud components install](https://docs.cloud.google.com/sdk/gcloud/reference/components/install) COMPONENT

To remove a component you no longer need: 
    
    
    [gcloud components remove](https://docs.cloud.google.com/sdk/gcloud/reference/components/remove) COMPONENT

To update all components you have to their latest version: 
    
    
    [gcloud components update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update)

To update all installed components to version 1.2.3: 
    
    
    [gcloud components update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update) --version 1.2.3

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[repositories](https://docs.cloud.google.com/sdk/gcloud/reference/components/repositories)`
     Manage additional component repositories for Trusted Tester programs. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[install](https://docs.cloud.google.com/sdk/gcloud/reference/components/install)`
     Install one or more Google Cloud CLI components. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/components/list)`
     List the status of all Google Cloud CLI components. 
`[reinstall](https://docs.cloud.google.com/sdk/gcloud/reference/components/reinstall)`
     Reinstall the Google Cloud CLI with the same components you have now. 
`[remove](https://docs.cloud.google.com/sdk/gcloud/reference/components/remove)`
     Remove one or more installed components. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update)`
     Update all of your installed components to the latest version. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
