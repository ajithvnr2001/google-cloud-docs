---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/
title: gcloud beta access-context-manager perimeters dry-run \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:51:48.395340+00:00
---

# gcloud beta access-context-manager perimeters dry-run  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta access-context-manager perimeters dry-run Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta access-context-manager perimeters dry-run - enable management of dry-run mode configuration for Service Perimeters 
SYNOPSIS
    

`gcloud beta access-context-manager perimeters dry-run` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` A Service Perimeter describes a set of Google Cloud Platform resources which can freely import and export data amongst themselves, but not externally, by default. 
    
    
    A dry-run mode configuration (also known as the Service Perimeter
    `spec`) makes it possible to understand the impact of any changes to a
    VPC Service Controls policy change before committing the change to the
    enforcement mode configuration.
    
    
    Note: For Service Perimeters without an explicit dry-run mode
    configuration, the enforcement mode configuration is used as the dry-run
    mode configuration, resulting in no audit logs being generated.

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create)`
     `(BETA)` Create a dry-run mode configuration for a new or existing Service Perimeter. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/delete)`
     `(BETA)` Mark the Service Perimeter as deleted in the dry-run mode. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/describe)`
     `(BETA)` Display the dry-run mode configuration for a Service Perimeter. 
`[drop](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/drop)`
     `(BETA)` Reset the dry-run mode configuration of a Service Perimeter. 
`[enforce](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce)`
     `(BETA)` Enforces a Service Perimeter's dry-run configuration. 
`[enforce-all](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/enforce-all)`
     `(BETA)` Enforces the dry-run mode configuration for all Service Perimeters. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/list)`
     `(BETA)` List the effective dry-run configuration across all Service Perimeters. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update)`
     `(BETA)` Update the dry-run mode configuration for a Service Perimeter. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud access-context-manager perimeters dry-run](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run)
    
    
    [gcloud alpha access-context-manager perimeters dry-run](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
