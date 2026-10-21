---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/update/
title: gcloud beta app-lifecycle-manager unit-kinds update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:44.174263+00:00
---

# gcloud beta app-lifecycle-manager unit-kinds update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager unit-kinds update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager unit-kinds update - update a Unit Kind 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager unit-kinds update` `UNIT_KIND` [`--location`=`LOCATION`] [`--saas`=`SAAS`] [`--app-params-group`=`APP_PARAMS_GROUP` `--clear-app-params` `--scope-type`=`SCOPE_TYPE`] [`--clear-default-release` | `--default-release`=`DEFAULT_RELEASE`] [`--dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`] | `--add-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`] `--clear-dependencies` | `--remove-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]] [`--input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] | `--add-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] `--clear-input-variable-mappings` | `--remove-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] | `--add-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`] `--clear-output-variable-mappings` | `--remove-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Unit Kind 
EXAMPLES
     To update the Unit Kind, run: 
    
    
    gcloud beta app-lifecycle-manager unit-kinds update

POSITIONAL ARGUMENTS
    

UnitKind resource - Identifier. The resource name (full URI of the resource) following the standard naming scheme: 
    
    
    "projects/{project}/locations/{location}/unitKinds/{unitKind}" This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways.

To set the `project` attribute: 

  * provide the argument `unit_kind` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `unit_kind` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`UNIT_KIND`
     ID of the unitKind or fully qualified identifier for the unitKind. 

To set the `unit_kind` attribute: 

  * provide the argument `unit_kind` on the command line. 


FLAGS
    

`--location`=`LOCATION`
     For resources [default-release, saas, unit_kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
Saas resource - A reference to the Saas that defines the product (managed service) that the producer wants to manage with App Lifecycle Manager. Immutable once set. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--saas` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--saas` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--saas`=`SAAS`
     ID of the saas or fully qualified identifier for the saas. 

To set the `saas` attribute: 

  * provide the argument `--saas` on the command line. 


AppParams contains the parameters for creating an AppHub Application. 
`--app-params-group`=`APP_PARAMS_GROUP`
     Grouping used to construct the name of the AppHub Application. Multiple UnitKinds can specify the same group to use the same Application across their respective units. Corresponds to the app_boundary_id in the ADC composite ApplicationTemplate. Defaults to UnitKind.name 
`--clear-app-params`
     Set unitKind.appParams back to default value. 
Scope of an application. 
`--scope-type`=`SCOPE_TYPE`
     Scope Type. `SCOPE_TYPE` must be one of: 

`type-global`
     Global type. 
`type-regional`
     Regional type. 
Update default_release. 

At most one of these can be specified: 

`--clear-default-release`
     Clear default_release value and set to null. 
Release resource - Set default_release to new value. 

A reference to the Release object to use as default for creating new units of this Unit Kind. 

If not specified, a new unit must explicitly reference which release to use for its creation. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--default-release` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--default-release` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--default-release`=`DEFAULT_RELEASE`
     ID of the release or fully qualified identifier for the release. 

To set the `release` attribute: 

  * provide the argument `--default-release` on the command line. 


Update dependencies. 

At most one of these can be specified: 

`--dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     Set dependencies to new value. List of other unit kinds that this release will depend on. Dependencies will be automatically provisioned if not found. Maximum 10\. 

`alias`
     An alias for the dependency. Used for input variable mapping. 
`unitKind`
     The unit kind of the dependency. 
`Shorthand Example:`
    
    
    --dependencies=alias=string,unitKind=string --dependencies=alias=string,unitKind=string

`JSON Example:`
    
    
    --dependencies='[{"alias": "string", "unitKind": "string"}]'

`File Example:`
    
    
    --dependencies=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     Add new value to dependencies list. List of other unit kinds that this release will depend on. Dependencies will be automatically provisioned if not found. Maximum 10. 

`alias`
     An alias for the dependency. Used for input variable mapping. 
`unitKind`
     The unit kind of the dependency. 
`Shorthand Example:`
    
    
    --add-dependencies=alias=string,unitKind=string --add-dependencies=alias=string,unitKind=string

`JSON Example:`
    
    
    --add-dependencies='[{"alias": "string", "unitKind": "string"}]'

`File Example:`
    
    
    --add-dependencies=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-dependencies`
     Clear dependencies value and set to empty list. 
`--remove-dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     Remove existing value from dependencies list. List of other unit kinds that this release will depend on. Dependencies will be automatically provisioned if not found. Maximum 10. 

`alias`
     An alias for the dependency. Used for input variable mapping. 
`unitKind`
     The unit kind of the dependency. 
`Shorthand Example:`
    
    
    --remove-dependencies=alias=string,unitKind=string --remove-dependencies=alias=string,unitKind=string

`JSON Example:`
    
    
    --remove-dependencies='[{"alias": "string", "unitKind": "string"}]'

`File Example:`
    
    
    --remove-dependencies=path_to_file.(yaml|json)

Update input_variable_mappings. 

At most one of these can be specified: 

`--input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Set input_variable_mappings to new value. List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100. 

`from`
     Output variables which will get their values from dependencies. 

`dependency`
     Required, Alias of the dependency that the outputVariable will pass its value to. 
`outputVariable`
     Required, Name of the outputVariable on the dependency. 
`to`
     Input variables whose values will be passed on to dependencies. 

`dependency`
     Required, Alias of the dependency that the inputVariable will pass its value to. 
`ignoreForLookup`
     Tells App Lifecycle Manager if this mapping should be used during lookup or not. 
`inputVariable`
     Required, Name of the inputVariable on the dependency. 
`variable`
     Required, name of the variable. 
`Shorthand Example:`
    
    
    --input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --input-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --input-variable-mappings=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Add new value to input_variable_mappings list. List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100. 

`from`
     Output variables which will get their values from dependencies. 

`dependency`
     Required, Alias of the dependency that the outputVariable will pass its value to. 
`outputVariable`
     Required, Name of the outputVariable on the dependency. 
`to`
     Input variables whose values will be passed on to dependencies. 

`dependency`
     Required, Alias of the dependency that the inputVariable will pass its value to. 
`ignoreForLookup`
     Tells App Lifecycle Manager if this mapping should be used during lookup or not. 
`inputVariable`
     Required, Name of the inputVariable on the dependency. 
`variable`
     Required, name of the variable. 
`Shorthand Example:`
    
    
    --add-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --add-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --add-input-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --add-input-variable-mappings=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-input-variable-mappings`
     Clear input_variable_mappings value and set to empty list. 
`--remove-input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Remove existing value from input_variable_mappings list. List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100\. 

`from`
     Output variables which will get their values from dependencies. 

`dependency`
     Required, Alias of the dependency that the outputVariable will pass its value to. 
`outputVariable`
     Required, Name of the outputVariable on the dependency. 
`to`
     Input variables whose values will be passed on to dependencies. 

`dependency`
     Required, Alias of the dependency that the inputVariable will pass its value to. 
`ignoreForLookup`
     Tells App Lifecycle Manager if this mapping should be used during lookup or not. 
`inputVariable`
     Required, Name of the inputVariable on the dependency. 
`variable`
     Required, name of the variable. 
`Shorthand Example:`
    
    
    --remove-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --remove-input-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --remove-input-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --remove-input-variable-mappings=path_to_file.(yaml|json)

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

Update output_variable_mappings. 

At most one of these can be specified: 

`--output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Set output_variable_mappings to new value. List of outputVariables for this unit kind will be passed to this unit's outputVariables. Maximum 100. 

`from`
     Output variables which will get their values from dependencies. 

`dependency`
     Required, Alias of the dependency that the outputVariable will pass its value to. 
`outputVariable`
     Required, Name of the outputVariable on the dependency. 
`to`
     Input variables whose values will be passed on to dependencies. 

`dependency`
     Required, Alias of the dependency that the inputVariable will pass its value to. 
`ignoreForLookup`
     Tells App Lifecycle Manager if this mapping should be used during lookup or not. 
`inputVariable`
     Required, Name of the inputVariable on the dependency. 
`variable`
     Required, name of the variable. 
`Shorthand Example:`
    
    
    --output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --output-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --output-variable-mappings=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Add new value to output_variable_mappings list. List of outputVariables for this unit kind will be passed to this unit's outputVariables. Maximum 100. 

`from`
     Output variables which will get their values from dependencies. 

`dependency`
     Required, Alias of the dependency that the outputVariable will pass its value to. 
`outputVariable`
     Required, Name of the outputVariable on the dependency. 
`to`
     Input variables whose values will be passed on to dependencies. 

`dependency`
     Required, Alias of the dependency that the inputVariable will pass its value to. 
`ignoreForLookup`
     Tells App Lifecycle Manager if this mapping should be used during lookup or not. 
`inputVariable`
     Required, Name of the inputVariable on the dependency. 
`variable`
     Required, name of the variable. 
`Shorthand Example:`
    
    
    --add-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --add-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --add-output-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --add-output-variable-mappings=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-output-variable-mappings`
     Clear output_variable_mappings value and set to empty list. 
`--remove-output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     Remove existing value from output_variable_mappings list. List of outputVariables for this unit kind will be passed to this unit's outputVariables. Maximum 100. 

`from`
     Output variables which will get their values from dependencies. 

`dependency`
     Required, Alias of the dependency that the outputVariable will pass its value to. 
`outputVariable`
     Required, Name of the outputVariable on the dependency. 
`to`
     Input variables whose values will be passed on to dependencies. 

`dependency`
     Required, Alias of the dependency that the inputVariable will pass its value to. 
`ignoreForLookup`
     Tells App Lifecycle Manager if this mapping should be used during lookup or not. 
`inputVariable`
     Required, Name of the inputVariable on the dependency. 
`variable`
     Required, name of the variable. 
`Shorthand Example:`
    
    
    --remove-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string --remove-output-variable-mappings=from={dependency=string,outputVariable=string},to={dependency=string,ignoreForLookup=boolean,inputVariable=string},variable=string

`JSON Example:`
    
    
    --remove-output-variable-mappings='[{"from": {"dependency": "string", "outputVariable": "string"}, "to": {"dependency": "string", "ignoreForLookup": boolean, "inputVariable": "string"}, "variable": "string"}]'

`File Example:`
    
    
    --remove-output-variable-mappings=path_to_file.(yaml|json)

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
