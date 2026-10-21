---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/create/
title: gcloud beta container fleet create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:35.969392+00:00
---

# gcloud beta container fleet create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container fleet create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container fleet create - create a fleet 
SYNOPSIS
    

`gcloud beta container fleet create` [`--async`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE` `--binauthz-policy-bindings`=[`name`=`BINAUTHZ_POLICY`] `--security-posture`=`SECURITY_POSTURE` `--workload-vulnerability-scanning`=`WORKLOAD_VULNERABILITY_SCANNING`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command can fail for the following reasons: 

  * The project specified does not exist. 
  * The project specified already has a fleet. 
  * The active account does not have permission to access the given project. 


EXAMPLES
     To create a fleet in project `example-foo-bar-1` with display name `my-fleet`, run: 
    
    
    gcloud beta container fleet create --display-name=my-fleet --project=example-foo-bar-1

FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--display-name`=`DISPLAY_NAME`
     Display name of the fleet to be created (optional). 4-30 characters, alphanumeric and [ '"!-] only. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Default cluster configurations to apply across the fleet. 
Binary Authorization config. 
`--binauthz-evaluation-mode`=`BINAUTHZ_EVALUATION_MODE`
     Configure binary authorization mode for clusters to onboard the fleet, 
    
    
    gcloud beta container fleet create --binauthz-evaluation-mode=policy-bindings

`BINAUTHZ_EVALUATION_MODE` must be one of: `disabled`, `policy-bindings`. 

`--binauthz-policy-bindings`=[`name`=`BINAUTHZ_POLICY`]
     The relative resource name of the Binary Authorization policy to audit and/or enforce. GKE policies have the following format: `projects/{project_number}/platforms/gke/policies/{policy_id}`. 
Security posture config. 
`--security-posture`=`SECURITY_POSTURE`
     To apply standard security posture to clusters in the fleet, 
    
    
    gcloud beta container fleet create --security-posture=standard

`SECURITY_POSTURE` must be one of: `disabled`, `standard`, `enterprise`. 

`--workload-vulnerability-scanning`=`WORKLOAD_VULNERABILITY_SCANNING`
     To apply standard vulnerability scanning to clusters in the fleet, 
    
    
    gcloud beta container fleet create --workload-vulnerability-scanning=standard

`WORKLOAD_VULNERABILITY_SCANNING` must be one of: `disabled`, `standard`, `enterprise`. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container fleet create](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/create)
    
    
    [gcloud alpha container fleet create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
