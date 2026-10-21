---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/scopes/namespaces/create/
title: gcloud beta container fleet scopes namespaces create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:16:16.906158+00:00
---

# gcloud beta container fleet scopes namespaces create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet/scopes/namespaces/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container fleet scopes namespaces create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container fleet scopes namespaces create - create a fleet namespace 
SYNOPSIS
    

`gcloud beta container fleet scopes namespaces create` (`NAMESPACE` : `--scope`=`SCOPE`) [`--labels`=[`KEY`=`VALUE`,…]] [`--namespace-labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command can fail for the following reasons: 

  * The project specified does not exist. 
  * The project has a fleet namespace with the same name. 
  * The caller does not have permission to access the given project. 


EXAMPLES
     To create a fleet namespace with name `NAMESPACE` in the active project, run: 
    
    
    gcloud beta container fleet scopes namespaces create NAMESPACE

To create a fleet namespace in fleet scope `SCOPE` in project `PROJECT_ID` with name `NAMESPACE`, run: 
    
    
    gcloud beta container fleet scopes namespaces create NAMESPACE --scope=SCOPE --project=PROJECT_ID

POSITIONAL ARGUMENTS
    

Namespace resource - The group of arguments defining the Fleet Namespace. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `NAMESPACE` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `NAMESPACE` on the command line with a fully specified name; 
  * global is the only supported location. 



This must be specified. 

`NAMESPACE`
     ID of the namespace or fully qualified identifier for the namespace. 

To set the `namespace` attribute: 

  * provide the argument `NAMESPACE` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--scope`=`SCOPE`
     the 

To set the `scope` attribute: 

  * provide the argument `NAMESPACE` on the command line with a fully specified name; 
  * provide the argument `--scope` on the command line. 


FLAGS
    

`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--namespace-labels`=[`KEY`=`VALUE`,…]
     List of namespace-level label KEY=VALUE pairs to add. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container fleet scopes namespaces create](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/namespaces/create)
    
    
    [gcloud alpha container fleet scopes namespaces create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/scopes/namespaces/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
