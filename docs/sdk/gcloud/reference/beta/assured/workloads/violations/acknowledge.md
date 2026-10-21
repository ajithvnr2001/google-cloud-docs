---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured/workloads/violations/acknowledge/
title: gcloud beta assured workloads violations acknowledge \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:38.506809+00:00
---

# gcloud beta assured workloads violations acknowledge  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/assured/workloads/violations/acknowledge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta assured workloads violations acknowledge Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta assured workloads violations acknowledge - acknowledge an existing Assured Workloads compliance violation 
SYNOPSIS
    

`gcloud beta assured workloads violations acknowledge` (`VIOLATION` : `--location`=`LOCATION` `--organization`=`ORGANIZATION` `--workload`=`WORKLOAD`) `--comment`=`COMMENT` [`--acknowledge-type`=`ACKNOWLEDGE_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Acknowledge an existing Assured Workloads compliance violation. 
EXAMPLES
     To acknowledge an Assured Workloads Violation in the `us-central1` region, belonging to an organization with ID `123`, with workload ID `456`, with violation ID `789` and comment as `test ack`, run: 
    
    
    gcloud beta assured workloads violations acknowledge organizations/123/locations/us-central1/workloads/456/violations/789 --comment="test ack"

POSITIONAL ARGUMENTS
    

Violation resource - The Assured Workloads violation resource to acknowledge. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`VIOLATION`
     ID of the violation or fully qualified identifier for the violation. 

To set the `violation` attribute: 

  * provide the argument `violation` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the violation. 

To set the `location` attribute: 

  * provide the argument `violation` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The parent organization for the violation. 

To set the `organization` attribute: 

  * provide the argument `violation` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


`--workload`=`WORKLOAD`
     The workload for the violation. 

To set the `workload` attribute: 

  * provide the argument `violation` on the command line with a fully specified name; 
  * provide the argument `--workload` on the command line. 


REQUIRED FLAGS
    

`--comment`=`COMMENT`
     Business justification used added to acknowledge a violation. 
OPTIONAL FLAGS
    

`--acknowledge-type`=`ACKNOWLEDGE_TYPE`
     the acknowledge type for specified violation, which is one of: SINGLE_VIOLATION \- to acknowledge specified violation, EXISTING_CHILD_RESOURCE_VIOLATIONS - to acknowledge specified org policy violation and all associated child resource violations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud assured workloads violations acknowledge](https://docs.cloud.google.com/sdk/gcloud/reference/assured/workloads/violations/acknowledge)
    
    
    [gcloud alpha assured workloads violations acknowledge](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/assured/workloads/violations/acknowledge)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
