---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/describe/
title: gcloud alpha access-context-manager perimeters dry-run describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:53.504182+00:00
---

# gcloud alpha access-context-manager perimeters dry-run describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/dry-run/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha access-context-manager perimeters dry-run describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha access-context-manager perimeters dry-run describe - display the dry-run mode configuration for a Service Perimeter 
SYNOPSIS
    

`gcloud alpha access-context-manager perimeters dry-run describe` (`PERIMETER` : `--policy`=`POLICY`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The dry-run mode configuration is presented as a diff against the enforcement mode configuration. '+' indicates additions in `spec`,'-' indicates removals from `status` and entries without either of those indicate that they are the same across the dry-run and the enforcement mode configurations. When a particular field is completely empty, it will not be displayed. 

Note: When this command is executed on a Service Perimeter with no explicit dry-run mode configuration, the effective dry-run mode configuration is inherited from the enforcement mode configuration, and thus, the enforcement mode configuration is displayed in such cases. 

EXAMPLES
     To display the dry-run mode configuration for a Service Perimeter: 
    
    
    gcloud alpha access-context-manager perimeters dry-run describe my-perimeter

Sample output: 
    
    
    ===
      name: my_perimeter
      title: My Perimeter
      type: PERIMETER_TYPE_REGULAR
      resources:
    +   projects/123
    -   projects/456
        projects/789
      restrictedServices:
    +   bigquery.googleapis.com
    -   storage.googleapis.com
        bigtable.googleapis.com
      vpcAccessibleServices:
    +   allowedServices:
    +     bigquery.googleapis.com
    -     storage.googleapis.com
    +   enableRestriction: true

POSITIONAL ARGUMENTS
    

Perimeter resource - The service perimeter to describe. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`PERIMETER`
     ID of the perimeter or fully qualified identifier for the perimeter. 

To set the `perimeter` attribute: 

  * provide the argument `perimeter` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--policy`=`POLICY`
     The ID of the access policy. 

To set the `policy` attribute: 

  * provide the argument `perimeter` on the command line with a fully specified name; 
  * provide the argument `--policy` on the command line; 
  * set the property `access_context_manager/policy`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud access-context-manager perimeters dry-run describe](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/describe)
    
    
    [gcloud beta access-context-manager perimeters dry-run describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
