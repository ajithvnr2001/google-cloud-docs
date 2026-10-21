---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/flags/create/
title: gcloud beta app-lifecycle-manager flags create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:41.829300+00:00
---

# gcloud beta app-lifecycle-manager flags create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/app-lifecycle-manager/flags/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta app-lifecycle-manager flags create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta app-lifecycle-manager flags create - create Flag 
SYNOPSIS
    

`gcloud beta app-lifecycle-manager flags create` `FLAG` `--flag-value-type`=`FLAG_VALUE_TYPE` `--key`=`KEY` `--unit-kind`=`UNIT_KIND` [`--annotations`=[`ANNOTATIONS`,…]] [`--description`=`DESCRIPTION`] [`--evaluation-spec`=[`allocations`=`ALLOCATIONS`],[`attributes`=`ATTRIBUTES`],[`defaultTarget`=`DEFAULTTARGET`],[`rules`=`RULES`]] [`--flag-set`=`FLAG_SET`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--state`=`STATE`] [`--variants`=[`booleanValue`=`BOOLEANVALUE`],[`description`=`DESCRIPTION`],[`doubleValue`=`DOUBLEVALUE`],[`id`=`ID`],[`integerValue`=`INTEGERVALUE`],[`stringValue`=`STRINGVALUE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new feature flag resource. Flags define toggleable features or configurations that can be evaluated at runtime by applications. 
EXAMPLES
     To create a simple boolean flag with a default `Disabled` state, run: 
    
    
    gcloud beta app-lifecycle-manager flags create my-feature-flag --key=enable_new_feature --flag-value-type=bool --unit-kind=my-service-unit --variants='[{"id": "Enabled", "booleanValue": true}, {"id":
    "Disabled", "booleanValue": false}]' \
       --evaluation-spec='{"defaultTarget": "Disabled"}' \
       --location=global

To create a simple boolean flag including a flag set, description, state, and the default variants and evaluation spec, run: 
    
    
    gcloud beta app-lifecycle-manager flags create beta-feature --key=beta_rollout --flag-value-type=bool --unit-kind=my-service-unit --flag-set=my-flag-set --description="A beta feature flag" --state=in-development --location=global

To create a percentage rollout (10% Enabled) using a `userID` attribute, run: 
    
    
    gcloud beta app-lifecycle-manager flags create beta-feature --key=beta_rollout --flag-value-type=bool --unit-kind=my-service-unit --variants='[{"id": "Enabled", "booleanValue": true}, {"id":
    "Disabled", "booleanValue": false}]' \
       --evaluation-spec='{"allocations": [{"id": "p10",
    "randomizedOn": "userID", "slots": [{"variant": "Disabled",
    "weight": 90}, {"variant": "Enabled", "weight": 10}]}],
    "defaultTarget": "p10", "attributes":
    ["projects/my-project/locations/global/flagAttributes/id-attr"]}' \
       --location=global

To create an integer flag for a retry limit, run: 
    
    
    gcloud beta app-lifecycle-manager flags create retry-limit --key=max_retries --flag-value-type=int --unit-kind=my-service-unit --variants='[{"id": "Low", "integerValue": 3}, {"id": "High",
    "integerValue": 10}]' \
       --evaluation-spec='{"defaultTarget": "Low"}' --location=global

To create a double flag for a discount percentage, run: 
    
    
    gcloud beta app-lifecycle-manager flags create discount-percentage --key=discount_percentage --flag-value-type=double --unit-kind=my-service-unit --variants='[{"id": "Zero", "doubleValue": 0.0}, {"id":
    "TenPercent", "doubleValue": 0.1}, {"id": "TwentyPercent",
    "doubleValue": 0.2}]' \
       --evaluation-spec='{"defaultTarget": "Zero"}' --location=global

To create a string flag for a theme color, run: 
    
    
    gcloud beta app-lifecycle-manager flags create header-color --key=header_color --flag-value-type=string --unit-kind=my-service-unit --variants='[{"id": "Blue", "stringValue": "blue"}, {"id":
    "Red", "stringValue": "red"}]' \
       --evaluation-spec='{"defaultTarget": "Blue"}' --location=global

To create a flag with complex targeting rules using a CEL expression and attributes, run: 
    
    
    gcloud beta app-lifecycle-manager flags create beta-feature --key=beta_enabled --flag-value-type=bool --unit-kind=my-service-unit --variants='[{"id": "Enabled", "booleanValue": true}, {"id":
    "Disabled", "booleanValue": false}]' \
       --evaluation-spec='{"rules": [{"id": "internal-testers",
    "condition": "email.endsWith(\"@google.com\")", "target":
    "Enabled"}], "defaultTarget": "Disabled", "attributes":
    ["projects/my-project/locations/global/flagAttributes/email-attr"]}\
    ' --location=global

POSITIONAL ARGUMENTS
    

Flag resource - ID of the Flag: 
    
    
    "projects/{project}/locations/{location}/flags/{flag_id}"

This follows the standard Google Cloud naming scheme (URI). This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `flag` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `flag` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`FLAG`
     ID of the flag or fully qualified identifier for the flag. 

To set the `flag` attribute: 

  * provide the argument `flag` on the command line. 


REQUIRED FLAGS
    

`--flag-value-type`=`FLAG_VALUE_TYPE`
     The type of the flag's value, e.g. BOOLEAN (required). `FLAG_VALUE_TYPE` must be one of: 

`bool`
     The flag's value type is a boolean. 
`double`
     The flag's value type is a double. 
`int`
     The flag's value type is an integer. 
`string`
     The flag's value type is a string. 
`--key`=`KEY`
     Flag key used in client runtime evaluation (required). Max length: 256 bytes. 
UnitKind resource - Reference to the UnitKind that can consume this Flag. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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

To set the `unit-kind` attribute: 

  * provide the argument `--unit-kind` on the command line. 


OPTIONAL FLAGS
    

`--annotations`=[`ANNOTATIONS`,…]
     Unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. Annotations are not queryable and should be preserved when modifying objects. 

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

`--description`=`DESCRIPTION`
     A description of the flag. Max length: 500 bytes. 
`--evaluation-spec`=[`allocations`=`ALLOCATIONS`],[`attributes`=`ATTRIBUTES`],[`defaultTarget`=`DEFAULTTARGET`],[`rules`=`RULES`]
     Specification of how the Flag value should be evaluated. 

`allocations`
     A list of allocations. 

`description`
     A description of the allocation. Max length: 500 bytes. 
`id`
     Id of the allocation. Max length: 128 bytes. 
`randomizedOn`
     Key of the context attribute that is used for traffic splitting. 
`slots`
     Slots defines the weighted distribution of variants. 

`variant`
     Variant of the allocation slot. 
`weight`
     Weight defines the proportion of traffic to allocate to the variant, relative to other slots in the same allocation. 
`attributes`
     Names of the context attributes that are used in the evaluation rules and allocations. 
`defaultTarget`
     Default variant for the flag. 
`rules`
     Define the logic for evaluating the flag against a given context. The rules are evaluated sequentially in their specified order. 

`condition`
     A Common Expression Language (CEL cel.dev) expression evaluated against the evaluation context. For example: `plan == "premium" && country == "DE"`. 
`id`
     A unique identifier for the rule. 
`target`
     The ID of the variant to return if the condition evaluates to true. 
`Shorthand Example:`
    
    
    --evaluation-spec=allocations=[{description=string,id=string,randomizedOn=string,slots=[{variant=string,weight=int}]}],attributes=[string],defaultTarget=string,rules=[{condition=string,id=string,target=string}]

`JSON Example:`
    
    
    --evaluation-spec='{"allocations": [{"description": "string", "id": "string", "randomizedOn": "string", "slots": [{"variant": "string", "weight": int}]}], "attributes": ["string"], "defaultTarget": "string", "rules": [{"condition": "string", "id": "string", "target": "string"}]}'

`File Example:`
    
    
    --evaluation-spec=path_to_file.(yaml|json)

`--flag-set`=`FLAG_SET`
     Flag set this flag belongs to. 
`--labels`=[`LABELS`,…]
     The labels on the resource, which can be used for categorization. 

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
     For resources [flag, unit-kind], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
`--state`=`STATE`
     Current state of the flag. `STATE` must be one of: 

`active`
     The flag is in the active state. 
`cleanup`
     The flag is in the cleanup state and ready to be deleted. 
`in-development`
     The flag is currently in development. 
`sunsetting`
     The flag is in the sunsetting state, indicating it is being phased out. 
`--variants`=[`booleanValue`=`BOOLEANVALUE`],[`description`=`DESCRIPTION`],[`doubleValue`=`DOUBLEVALUE`],[`id`=`ID`],[`integerValue`=`INTEGERVALUE`],[`stringValue`=`STRINGVALUE`]
     A list of variants. Variant is an identifier for a value (name assigned to a value). 

`booleanValue`
     Value is a single boolean flag value for the variant. 
`description`
     A description of the variant. Max length: 500 bytes. 
`doubleValue`
     Value is a single double flag value for the variant. 
`id`
     Id of the variant. Max length: 128 bytes. 
`integerValue`
     Value is a single integer flag value for the variant. 
`stringValue`
     Value is a single string flag value for the variant. Max length: 500 bytes. 
`Shorthand Example:`
    
    
    --variants=booleanValue=boolean,description=string,doubleValue=float,id=string,integerValue=int,stringValue=string --variants=booleanValue=boolean,description=string,doubleValue=float,id=string,integerValue=int,stringValue=string

`JSON Example:`
    
    
    --variants='[{"booleanValue": boolean, "description": "string", "doubleValue": float, "id": "string", "integerValue": int, "stringValue": "string"}]'

`File Example:`
    
    
    --variants=path_to_file.(yaml|json)

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
