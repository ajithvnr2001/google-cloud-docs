---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/create/
title: gcloud beta app-lifecycle-manager unit-kinds create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:43.692655+00:00
---

# gcloud beta app-lifecycle-manager unit-kinds create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/unit-kinds/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager unit-kinds create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager unit-kinds create - create a Unit Kind 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager unit-kinds create` `UNIT_KIND` `--saas`=`SAAS` [`--default-release`=`DEFAULT_RELEASE`] [`--dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]] [`--input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]] [`--app-params-group`=`APP_PARAMS_GROUP` `--scope-type`=`SCOPE_TYPE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Unit Kind 
EXAMPLES
     To create the Unit Kind, run: 
    
    
    gcloud beta app-lifecycle-manager unit-kinds create

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


REQUIRED FLAGS
    

Saas resource - A reference to the Saas that defines the product (managed service) that the producer wants to manage with App Lifecycle Manager. Immutable once set. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--saas` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--saas` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--saas`=`SAAS`
     ID of the saas or fully qualified identifier for the saas. 

To set the `saas` attribute: 

  * provide the argument `--saas` on the command line. 


OPTIONAL FLAGS
    

Release resource - A reference to the Release object to use as default for creating new units of this Unit Kind (optional). 

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


`--dependencies`=[`alias`=`ALIAS`],[`unitKind`=`UNITKIND`]
     List of other unit kinds that this release will depend on. Dependencies will be automatically provisioned if not found. Maximum 10. 

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

`--input-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100. 

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
     Indicates if this mapping should be used during lookup or not. 
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
     For resources [default-release, saas, unit_kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--output-variable-mappings`=[`from`=`FROM`],[`to`=`TO`],[`variable`=`VARIABLE`]
     List of inputVariables for this release that will either be retrieved from a dependency's outputVariables, or will be passed on to a dependency's inputVariables. Maximum 100. 

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
     Indicates if this mapping should be used during lookup or not. 
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

AppParams contains the parameters for creating an AppHub Application. 
`--app-params-group`=`APP_PARAMS_GROUP`
     Grouping used to construct the name of the AppHub Application. Multiple UnitKinds can specify the same group to use the same Application across their respective units. Corresponds to the app_boundary_id in the ADC composite ApplicationTemplate. Defaults to UnitKind.name 
Scope of an application. 
`--scope-type`=`SCOPE_TYPE`
     Scope Type. `SCOPE_TYPE` must be one of: 

`type-global`
     Global type. 
`type-regional`
     Regional type. 
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
