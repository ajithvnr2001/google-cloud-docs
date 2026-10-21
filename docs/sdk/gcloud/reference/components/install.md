---
url: https://docs.cloud.google.com/sdk/gcloud/reference/components/install/
title: gcloud components install \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:27.802356+00:00
---

# gcloud components install  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/components/install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud components install Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud components install - install one or more Google Cloud CLI components 
SYNOPSIS
    

`gcloud components install` `COMPONENT-IDS` [`COMPONENT-IDS` …] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Ensure that each of the specified components (as well as any dependent components) is installed on the local workstation. Components are installed without performing any upgrades to your existing CLI installation. All components are installed at the current version of your CLI. 

Components that are available for installation can be viewed by running: 
    
    
    [gcloud components list](https://docs.cloud.google.com/sdk/gcloud/reference/components/list)

Installing a given component will also install all components on which it depends. The command lists all components it is about to install, and asks for confirmation before proceeding. 

``gcloud components install`` installs components from the version of the Google Cloud CLI you currently have installed. You can see your current version by running: 
    
    
    [gcloud version](https://docs.cloud.google.com/sdk/gcloud/reference/version)

If you want to update your Google Cloud CLI installation to the latest available version, use: 
    
    
    [gcloud components update](https://docs.cloud.google.com/sdk/gcloud/reference/components/update)

EXAMPLES
     The following command installs ``COMPONENT-1``, ``COMPONENT-2``, and all components that they depend on: 
    
    
    gcloud components install COMPONENT-1 COMPONENT-2

POSITIONAL ARGUMENTS
    

`COMPONENT-IDS` [`COMPONENT-IDS` …]
     The IDs of the components to be installed. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
