---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollout-kinds/create/
title: gcloud beta app-lifecycle-manager rollout-kinds create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:36.757400+00:00
---

# gcloud beta app-lifecycle-manager rollout-kinds create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/rollout-kinds/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager rollout-kinds create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager rollout-kinds create - create a Rollout Kind 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager rollout-kinds create` `ROLLOUT_KIND` `--unit-kind`=`UNIT_KIND` [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`] [`--unit-filter`=`UNIT_FILTER`] [`--update-unit-kind-strategy`=`UPDATE_UNIT_KIND_STRATEGY`] [`--error-budget-allowed-count`=`ERROR_BUDGET_ALLOWED_COUNT` `--error-budget-allowed-percentage`=`ERROR_BUDGET_ALLOWED_PERCENTAGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Rollout Kind 
EXAMPLES
     To create the Rollout Kind, run: 
    
    
    gcloud beta app-lifecycle-manager rollout-kinds create

POSITIONAL ARGUMENTS
    

RolloutKindId resource - Identifier. The resource name (full URI of the resource) following the standard naming scheme: 
    
    
    "projects/{project}/locations/{location}/rolloutKinds/{rollout_kind_id}" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `rollout_kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `rollout_kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`ROLLOUT_KIND`
     ID of the rolloutKindId or fully qualified identifier for the rolloutKindId. 

To set the `rollout_kind` attribute: 

  * provide the argument `rollout_kind` on the command line. 


REQUIRED FLAGS
    

UnitKind resource - UnitKind that this rollout kind corresponds to. Rollouts stemming from this rollout kind will target the units of this unit kind. In other words, this defines the population of target units to be upgraded by rollouts. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--unit-kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--unit-kind`=`UNIT_KIND`
     ID of the unitKind or fully qualified identifier for the unitKind. 

To set the `unit_kind` attribute: 

  * provide the argument `--unit-kind` on the command line. 


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
     For resources [rollout_kind, unit-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--rollout-orchestration-strategy`=`ROLLOUT_ORCHESTRATION_STRATEGY`
     The strategy to use for executing rollouts. 
`--unit-filter`=`UNIT_FILTER`
     CEL(https://github.com/google/cel-spec) formatted filter string against Unit. The filter will be applied to determine the eligible unit population. This filter can only reduce, but not expand the scope of the rollout. 
`--update-unit-kind-strategy`=`UPDATE_UNIT_KIND_STRATEGY`
     The config for updating the unit kind. By default, the unit kind will be updated on the rollout start. `UPDATE_UNIT_KIND_STRATEGY` must be one of: 

`never`
     Never update the unit kind. 
`on-start`
     Update the unit kind strategy on the rollout start. 
Arguments for the error budget. 
The configuration for error budget. If the number of failed units exceeds max(allowed_count, allowed_ratio * total_units), the rollout will be paused. 
`--error-budget-allowed-count`=`ERROR_BUDGET_ALLOWED_COUNT`
     The maximum number of failed units allowed in a location without pausing the rollout. 
`--error-budget-allowed-percentage`=`ERROR_BUDGET_ALLOWED_PERCENTAGE`
     The maximum percentage of units allowed to fail (0, 100] within a location without pausing the rollout. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `saasservicemgmt/v1beta1` API. The full documentation for this API can be found at: <https://cloud.google.com/saas-runtime/docs>
NOTES
     This command is currently in beta and might change without notice. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
