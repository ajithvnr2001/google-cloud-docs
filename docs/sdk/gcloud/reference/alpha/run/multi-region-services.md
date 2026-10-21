---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/
title: gcloud alpha run multi-region-services \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:18:49.251162+00:00
---

# gcloud alpha run multi-region-services  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha run multi-region-services Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha run multi-region-services - manage your Cloud Run multi-region services 
SYNOPSIS
    

`gcloud alpha run multi-region-services` `COMMAND` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The gcloud run multi-region-services command group lets you deploy container images to Google Cloud Run across multiple regions at once. 
EXAMPLES
     To deploy your container, use the `gcloud run multi-region-services deploy` command: 
    
    
    gcloud alpha run multi-region-services deploy <service-name> --image <image_name> --regions [region-list] For more information, run:
    [gcloud run deploy](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) --help

FLAGS
    

`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/delete)`
     `(ALPHA)` Deletes a multi-region service. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/describe)`
     `(ALPHA)` Command to describe a multi-region service. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/list)`
     `(ALPHA)` List available multi-region services. 
`[replace](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/replace)`
     `(ALPHA)` Create or Update multi-region service from YAML. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/update)`
     `(ALPHA)` Update environment variables, add/remove regions, and other configuration settings in Multi-Region Services. 
`[update-traffic](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/multi-region-services/update-traffic)`
     `(ALPHA)` Adjust the traffic assignments for a Cloud Run Multi-Region service. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud run multi-region-services](https://docs.cloud.google.com/sdk/gcloud/reference/run/multi-region-services)
    
    
    [gcloud beta run multi-region-services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/multi-region-services)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
