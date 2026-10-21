---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/scopes/describe/
title: gcloud alpha container fleet scopes describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:27:40.335105+00:00
---

# gcloud alpha container fleet scopes describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/scopes/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container fleet scopes describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container fleet scopes describe - describe a fleet scope 
SYNOPSIS
    

`gcloud alpha container fleet scopes describe` (`SCOPE` : `--location`=`LOCATION`) [`--show-cluster-upgrade` | `--show-linked-cluster-upgrade`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Describe a Fleet Scope. 
EXAMPLES
     First retrieve the ID of the scope using the command below. The output of this command lists all the fleet's members, with their unique IDs in the Names column: 
    
    
    [gcloud alpha container fleet scopes list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/scopes/list)

Then describe it: 
    
    
    gcloud alpha container fleet scopes describe SCOPE_NAME

POSITIONAL ARGUMENTS
    

Scope resource - The scope to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `scope` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SCOPE`
     ID of the scope or fully qualified identifier for the scope. 

To set the `scope` attribute: 

  * provide the argument `scope` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location name. 

To set the `location` attribute: 

  * provide the argument `scope` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * global is the only supported location. 


FLAGS
    

Rollout Sequencing 

At most one of these can be specified: 

`--show-cluster-upgrade`
     Shows the cluster upgrade feature information for the current scope. 

To view the cluster upgrade feature information for ``SCOPE_NAME``, run: 
    
    
    gcloud alpha container fleet scopes describe SCOPE_NAME --show-cluster-upgrade

`--show-linked-cluster-upgrade`
     Shows the cluster upgrade feature information for the current scope as well as information for all other scopes linked in the same rollout sequence (provided that the caller has permission to view the upstream and downstream scopes that exist in other fleets). This displays cluster upgrade information for scopes in the current scope's rollout sequence in order of furthest upstream to downstream. 

To view the cluster upgrade feature information for the rollout sequence containing ``SCOPE_NAME``, run: 
    
    
    gcloud alpha container fleet scopes describe SCOPE_NAME --show-linked-cluster-upgrade

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gkehub/v1alpha` API. The full documentation for this API can be found at: <https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container fleet scopes describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/describe)
    
    
    [gcloud beta container fleet scopes describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/scopes/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
