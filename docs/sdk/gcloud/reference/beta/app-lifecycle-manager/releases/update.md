---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/releases/update/
title: gcloud beta app-lifecycle-manager releases update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:16.611685+00:00
---

# gcloud beta app-lifecycle-manager releases update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/releases/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager releases update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager releases update - update a Release 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager releases update` (`RELEASE` : `--location`=`LOCATION`) [`--input-variable-defaults`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] | `--add-input-variable-defaults`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`] `--clear-input-variable-defaults` | `--remove-input-variable-defaults`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--upgradeable-from-releases`=[`UPGRADEABLE_FROM_RELEASES`,…] | `--add-upgradeable-from-releases`=[`ADD_UPGRADEABLE_FROM_RELEASES`,…] `--clear-upgradeable-from-releases` | `--remove-upgradeable-from-releases`=[`REMOVE_UPGRADEABLE_FROM_RELEASES`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Release 
EXAMPLES
     To update the Release, run: 
    
    
    gcloud beta app-lifecycle-manager releases update

POSITIONAL ARGUMENTS
    

Release resource - Identifier. The resource name (full URI of the resource) following the standard naming scheme: 
    
    
    "projects/{project}/locations/{location}/releases/{release}" The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `release` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location ID 

To set the `location` attribute: 

  * provide the argument `release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

Update input_variable_defaults. 

At most one of these can be specified: 

`--input-variable-defaults`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Set input_variable_defaults to new value. Mapping of input variables to default values. Maximum 100. 

`type`
     Name of a supported variable type. Supported types are string, int, bool. 
`value`
     String encoded value for the variable. 
`variable`
     Name of the variable from actuation configs. 
`Shorthand Example:`
    
    
    --input-variable-defaults=type=string,value=string,variable=string --input-variable-defaults=type=string,value=string,variable=string

`JSON Example:`
    
    
    --input-variable-defaults='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --input-variable-defaults=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-input-variable-defaults`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Add new value to input_variable_defaults list. Mapping of input variables to default values. Maximum 100. 

`type`
     Name of a supported variable type. Supported types are string, int, bool. 
`value`
     String encoded value for the variable. 
`variable`
     Name of the variable from actuation configs. 
`Shorthand Example:`
    
    
    --add-input-variable-defaults=type=string,value=string,variable=string --add-input-variable-defaults=type=string,value=string,variable=string

`JSON Example:`
    
    
    --add-input-variable-defaults='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --add-input-variable-defaults=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-input-variable-defaults`
     Clear input_variable_defaults value and set to empty list. 
`--remove-input-variable-defaults`=[`type`=`TYPE`],[`value`=`VALUE`],[`variable`=`VARIABLE`]
     Remove existing value from input_variable_defaults list. Mapping of input variables to default values. Maximum 100. 

`type`
     Name of a supported variable type. Supported types are string, int, bool. 
`value`
     String encoded value for the variable. 
`variable`
     Name of the variable from actuation configs. 
`Shorthand Example:`
    
    
    --remove-input-variable-defaults=type=string,value=string,variable=string --remove-input-variable-defaults=type=string,value=string,variable=string

`JSON Example:`
    
    
    --remove-input-variable-defaults='[{"type": "string", "value": "string", "variable": "string"}]'

`File Example:`
    
    
    --remove-input-variable-defaults=path_to_file.(yaml|json)

Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels. 

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
     Update labels value or add key value pair. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels. 

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

Update upgradeable_from_releases. 

At most one of these can be specified: 

`--upgradeable-from-releases`=[`UPGRADEABLE_FROM_RELEASES`,…]
     Set upgradeable_from_releases to new value. 
Or at least one of these can be specified: 

`--add-upgradeable-from-releases`=[`ADD_UPGRADEABLE_FROM_RELEASES`,…]
     Add new value to upgradeable_from_releases list. 
At most one of these can be specified: 

`--clear-upgradeable-from-releases`
     Clear upgradeable_from_releases value and set to empty list. 
`--remove-upgradeable-from-releases`=[`REMOVE_UPGRADEABLE_FROM_RELEASES`,…]
     Remove existing value from upgradeable_from_releases list. 
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
