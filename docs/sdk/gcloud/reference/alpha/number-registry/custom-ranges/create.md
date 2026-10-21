---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/create/
title: gcloud alpha number-registry custom-ranges create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:12.930826+00:00
---

# gcloud alpha number-registry custom-ranges create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha number-registry custom-ranges create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha number-registry custom-ranges create - create a custom range resource 
SYNOPSIS
    

`gcloud alpha number-registry custom-ranges create` `CUSTOM_RANGE` [`--async`] [`--attributes`=[`key`=`KEY`],[`value`=`VALUE`]] [`--description`=`DESCRIPTION`] [`--labels`=[`LABELS`,…]] [`--location`=`LOCATION`] [`--parent-range`=`PARENT_RANGE`] [`--realm`=`REALM`] [`--request-id`=`REQUEST_ID`] [`--ipv4-cidr-range`=`IPV4_CIDR_RANGE` | `--ipv6-cidr-range`=`IPV6_CIDR_RANGE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a custom range resource. 
EXAMPLES
     To create a custom range `my-custom-range` run: 


POSITIONAL ARGUMENTS
    

CustomRange resource - Identifier. The resource name of the CustomRange, in the format `projects/{project}/locations/{location}/customRanges/{custom_range}`. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `custom_range` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `custom_range` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`CUSTOM_RANGE`
     ID of the customRange or fully qualified identifier for the customRange. 

To set the `custom_range` attribute: 

  * provide the argument `custom_range` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--attributes`=[`key`=`KEY`],[`value`=`VALUE`]
     The attributes of the CustomRange. 

`key`
     The key of the attribute. 
`value`
     The value of the attribute. 
`Shorthand Example:`
    
    
    --attributes=key=string,value=string --attributes=key=string,value=string

`JSON Example:`
    
    
    --attributes='[{"key": "string", "value": "string"}]'

`File Example:`
    
    
    --attributes=path_to_file.(yaml|json)

`--description`=`DESCRIPTION`
     The description of the CustomRange. 
`--labels`=[`LABELS`,…]
     User-defined labels. 

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
     For resources [custom_range, parent-range, realm], provides fallback value for resource location attribute. When the resource's full URI path is not provided, location will fallback to this flag value. 
CustomRange resource - The resource name of the parent CustomRange, in the format `projects/{project}/locations/{location}/customRanges/{custom_range}`. If specified, the parent CustomRange must be in the same RegistryBook. This field is mutually exclusive with the `realm` field, as the Realm is inherited from the parent CustomRange. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--parent-range` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--parent-range` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--parent-range`=`PARENT_RANGE`
     ID of the customRange or fully qualified identifier for the customRange. 

To set the `custom-range` attribute: 

  * provide the argument `--parent-range` on the command line. 


Realm resource - The resource name of the Realm associated with the CustomRange, in the format `projects/{project}/locations/{location}/realms/{realm}`. The Realm must be in the same project as the CustomRange. This field must not be set if the `parent_range` field is set, as the Realm will be inherited from the parent CustomRange. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--realm` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--realm` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--realm`=`REALM`
     ID of the realm or fully qualified identifier for the realm. 

To set the `realm` attribute: 

  * provide the argument `--realm` on the command line. 


`--request-id`=`REQUEST_ID`
     An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. 

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

Arguments for the ip cidr range. 

At most one of these can be specified: 

`--ipv4-cidr-range`=`IPV4_CIDR_RANGE`
     The IPv4 CIDR range of the CustomRange. 
`--ipv6-cidr-range`=`IPV6_CIDR_RANGE`
     The IPv6 CIDR range of the CustomRange. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `cloudnumberregistry/v1alpha` API. The full documentation for this API can be found at: <https://docs.cloud.google.com/number-registry/reference/rest>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
