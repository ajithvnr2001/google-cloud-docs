---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create/
title: gcloud beta app-lifecycle-manager rollouts create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:40.970335+00:00
---

# gcloud beta app-lifecycle-manager rollouts create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollouts/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager rollouts create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager rollouts create - create a Rollout 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager rollouts create` `ROLLOUT` (`--flag-release`=`FLAG_RELEASE` | `--release`=`RELEASE`) [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--rollout-kind`=`ROLLOUT_KIND`] [`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`] [`--unit-filter`=`UNIT_FILTER`] [`--control-action`=`CONTROL_ACTION` : `--[no-]retry-failed-operations`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Rollout 
EXAMPLES
     To create the Rollout, run: 
    
    
    gcloud beta app-lifecycle-manager rollouts create

POSITIONAL ARGUMENTS
    

RolloutId resource - Identifier. The resource name (full URI of the resource) following the standard naming scheme: 
    
    
    "projects/{project}/locations/{location}/rollout/{rollout_id}" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `rollout` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`ROLLOUT`
     ID of the rolloutId or fully qualified identifier for the rolloutId. 

To set the `rollout` attribute: 

  * provide the argument `rollout` on the command line. 


REQUIRED FLAGS
    

Exactly one of these must be specified: 

FlagRelease resource - Name of the Flag Release that gets rolled out to target Units. Required if no other type of release is specified. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--flag-release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--flag-release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--flag-release`=`FLAG_RELEASE`
     ID of the flagRelease or fully qualified identifier for the flagRelease. 

To set the `flag-release` attribute: 

  * provide the argument `--flag-release` on the command line. 


Release resource - Name of the Release that gets rolled out to target Units. Required if no other type of release is specified. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--release`=`RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `--release` on the command line. 


OPTIONAL FLAGS
    

`--labels`=[`LABELS`,…]
     The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

`--location`=`LOCATION`
     For resources [flag-release, release, rollout, rollout-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
RolloutKindId resource - Name of the RolloutKind this rollout is stemming from and adhering to. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--rollout-kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--rollout-kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--rollout-kind`=`ROLLOUT_KIND`
     ID of the rolloutKindId or fully qualified identifier for the rolloutKindId. 

To set the `rollout-kind` attribute: 

  * provide the argument `--rollout-kind` on the command line. 


`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`
     The strategy to use for executing this rollout. If not provided, the strategy from Rollout Type will be used. 
`--unit-filter`=`UNIT_FILTER`
     CEL(https://github.com/google/cel-spec) formatted filter string against Unit. The filter will be applied to determine the eligible unit population. This filter can only reduce, but not expand the scope of the rollout. If not provided, the unit_filter from the RolloutType will be used. 
RolloutControl provides a way to request a change to the execution of a Rollout by pausing or canceling it. 
`--control-action`=`CONTROL_ACTION`
     Action to be performed on the Rollout. The default behavior is to run the rollout until it naturally reaches a terminal state. `CONTROL_ACTION` must be one of: 

`cancel`
     Cancel the Rollout permanently. 
`pause`
     Pause the Rollout until it is resumed (i.e. RUN is requested). 
`run`
     Run the Rollout until it naturally reaches a terminal state. A rollout requested to run will progress through all natural Rollout States (such as RUNNING -> SUCCEEDED or RUNNING -> FAILED). If retriable errors are encountered during the rollout, the rollout will paused by default and can be resumed by re-requesting this RUN action. 
This flag argument must be specified if any of the other arguments in this group are specified. 
Arguments for the action params. 
Parameters for the RUN action controlling the behavior of the rollout when it is resumed from a PAUSED state. 
`--[no-]retry-failed-operations`
     If true, the rollout will retry failed operations when resumed. This is applicable only the current state of the Rollout is PAUSED and the requested action is RUN. Use `--retry-failed-operations` to enable and `--no-retry-failed-operations` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `saasservicemgmt/v1beta1` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/app-lifecycle-manager>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
