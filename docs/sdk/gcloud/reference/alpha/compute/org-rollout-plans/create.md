---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-rollout-plans/create/
title: gcloud alpha compute org-rollout-plans create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:19:03.349712+00:00
---

# gcloud alpha compute org-rollout-plans create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/org-rollout-plans/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha compute org-rollout-plans create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha compute org-rollout-plans create - create an organization rollout plan 
SYNOPSIS
    

`gcloud alpha compute org-rollout-plans create` (`NAME` : `--organization`=`ORGANIZATION`) `--waves-from-file`=`WAVES_FROM_FILE` [`--description`=`DESCRIPTION`] [`--location-scope`=`LOCATION_SCOPE`; default="ZONAL"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Google Compute Engine organization rollout plan. 
EXAMPLES
     To create an organization rollout plan named `my-org-rollout-plan` from a wave definition file named `waves.json` under organization `123456789`, run: 
    
    
    gcloud alpha compute org-rollout-plans create my-org-rollout-plan --organization=123456789 --waves-from-file=waves.json

POSITIONAL ARGUMENTS
    

Organization rollout plan resource - Name of the organization rollout plan to create. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`NAME`
     ID of the organization rollout plan or fully qualified identifier for the organization rollout plan. 

To set the `name` attribute: 

  * provide the argument `name` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--organization`=`ORGANIZATION`
     The Google Cloud organization ID. 

To set the `organization` attribute: 

  * provide the argument `name` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. 


REQUIRED FLAGS
    

`--waves-from-file`=`WAVES_FROM_FILE`
     Path to a YAML or JSON file containing the wave definitions for the organization rollout plan. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     An optional description of this organization rollout plan. 
`--location-scope`=`LOCATION_SCOPE`; default="ZONAL"
     The location scope of the organization rollout plan. `LOCATION_SCOPE` must be one of: `ZONAL`, `REGIONAL`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta compute org-rollout-plans create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/org-rollout-plans/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
