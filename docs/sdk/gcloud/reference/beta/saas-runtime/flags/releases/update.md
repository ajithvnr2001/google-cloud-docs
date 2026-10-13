---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/saas-runtime/flags/releases/update/
title: gcloud beta saas-runtime flags releases update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:26.149486+00:00
---

# gcloud beta saas-runtime flags releases update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/saas-runtime/flags/releases/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta saas-runtime flags releases update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta saas-runtime flags releases update - update a Flag Release 
SYNOPSIS
    

`gcloud beta saas-runtime flags releases update` (`FLAG_RELEASE` : `--location`=`LOCATION`) [`--annotations`=[`ANNOTATIONS`,…] | `--update-annotations`=[`UPDATE_ANNOTATIONS`,…] `--clear-annotations` | `--remove-annotations`=`REMOVE_ANNOTATIONS`] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the administrative metadata of an existing Flag Release. This command modifies the resource's labels (for categorization and filtering) and annotations (for external tool metadata). 

Note that Flag Releases are immutable snapshots of flag configurations. This command does not modify the flag revisions or the associated UnitKind. To change the flag logic or revisions associated with a UnitKind, you must create a new Flag Release and initiate a Rollout. This architecture ensures that once a release is created, its behavioral payload remains constant while allowing for operational metadata updates. 

EXAMPLES
     To update labels and annotations for a flag release, run: 
    
    
    gcloud beta saas-runtime flags releases update my-release --location=us-central1 --labels=env=prod --annotations=ticket=123

POSITIONAL ARGUMENTS
    

FlagRelease resource - ID of the Flag Release: 
    
    
    "projects/{project}/locations/{location}/flagReleases/{flag_release_id}"

This follows the standard Google Cloud naming scheme (URI). The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `flag_release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`FLAG_RELEASE`
     ID of the flagRelease or fully qualified identifier for the flagRelease. 

To set the `flag_release` attribute: 

  * provide the argument `flag_release` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location ID 

To set the `location` attribute: 

  * provide the argument `flag_release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

Update annotations. 

At most one of these can be specified: 

`--annotations`=[`ANNOTATIONS`,…]
     Set annotations to new value. Unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. Annotations are not queryable and should be preserved when modifying objects. 

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

Or at least one of these can be specified: 

`--update-annotations`=[`UPDATE_ANNOTATIONS`,…]
     Update annotations value or add key value pair. Unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. Annotations are not queryable and should be preserved when modifying objects. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-annotations=string=string

`JSON Example:`
    
    
    --update-annotations='{"string": "string"}'

`File Example:`
    
    
    --update-annotations=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-annotations`
     Clear annotations value and set to empty map. 
`--remove-annotations`=`REMOVE_ANNOTATIONS`
     Remove existing value from map annotations. Sets `remove_annotations` value. `Shorthand Example:`
    
    
    --remove-annotations=string,string

`JSON Example:`
    
    
    --remove-annotations=["string"]

`File Example:`
    
    
    --remove-annotations=path_to_file.(yaml|json)

Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. The labels on the resource, which can be used for categorization. 

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

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. The labels on the resource, which can be used for categorization. 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

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
