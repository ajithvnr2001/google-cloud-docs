---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/flags/revisions/create/
title: gcloud beta app-lifecycle-manager flags revisions create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:27.868488+00:00
---

# gcloud beta app-lifecycle-manager flags revisions create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/flags/revisions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager flags revisions create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager flags revisions create - create Flag Revision 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager flags revisions create` `FLAG_REVISION` `--flag`=`FLAG` [`--annotations`=[`ANNOTATIONS`,…]] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new flag revision resource. Flag revisions act as immutable snapshots of a flag's configuration (variants, rules, and allocations) at a specific point in time. 

This snapshot is a required prerequisite for creating a Flag Release and initiating a Flag Rollout. Creating a revision ensures that the configuration state is frozen and safely decoupled from the live flag definition during the rollout process. 

EXAMPLES
     To create a Flag Revision for a flag named `my-flag` in the `global` location, run: 
    
    
    gcloud beta app-lifecycle-manager flags revisions create my-revision-v1 --flag=my-flag --location=global

To create a revision using a fully qualified resource name for the revision ID, run: 
    
    
    gcloud beta app-lifecycle-manager flags revisions create projects/my-project/locations/global/flagRevisions/my-revision-v1 --flag=my-flag

To create a revision with metadata for tracking, run: 
    
    
    gcloud beta app-lifecycle-manager flags revisions create prod-ready-rev --flag=search-optimizations --location=us-central1 --labels=env=prod,owner=search-team --annotations=ticket=123

POSITIONAL ARGUMENTS
    

FlagRevision resource - Flag Revision ID. Google Cloud resource name (full URI of the resource) following the standard naming scheme: 
    
    
    "projects/{project}/locations/{location}/flagRevisions/{flag_revision_id}" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `flag_revision` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `flag_revision` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`FLAG_REVISION`
     ID of the flagRevision or fully qualified identifier for the flagRevision. 

To set the `flag_revision` attribute: 

  * provide the argument `flag_revision` on the command line. 


REQUIRED FLAGS
    

Flag resource - Name (ID) of the Flag this is a revision of. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--flag` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--flag` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--flag`=`FLAG`
     ID of the flag or fully qualified identifier for the flag. 

To set the `flag` attribute: 

  * provide the argument `--flag` on the command line. 


OPTIONAL FLAGS
    

`--annotations`=[`ANNOTATIONS`,…]
     Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --annotations=string=string

`JSON Example:`
    
    
    --annotations='{"string": "string"}'

`File Example:`
    
    
    --annotations=path_to_file.(yaml|json)

`--labels`=[`LABELS`,…]
     Labels on the resource, which can be used for categorization. 

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
     For resources [flag, flag_revision], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
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
