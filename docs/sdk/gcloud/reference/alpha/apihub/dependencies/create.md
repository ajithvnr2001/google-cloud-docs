---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/dependencies/create/
title: gcloud alpha apihub dependencies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:46.703482+00:00
---

# gcloud alpha apihub dependencies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/dependencies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apihub dependencies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apihub dependencies create - create a Dependency 
SYNOPSIS
    

`gcloud alpha apihub dependencies create` (`DEPENDENCY` : `--location`=`LOCATION`) (`--consumer-external-api-resource-name`=`CONSUMER_EXTERNAL_API_RESOURCE_NAME` | `--consumer-operation-resource-name`=`CONSUMER_OPERATION_RESOURCE_NAME`) (`--supplier-external-api-resource-name`=`SUPPLIER_EXTERNAL_API_RESOURCE_NAME` | `--supplier-operation-resource-name`=`SUPPLIER_OPERATION_RESOURCE_NAME`) [`--attributes`=[`ATTRIBUTES`,…]] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a dependency 

Note: The positional argument for Dependency ID is currently not supported. Please use the --dependency flag to specify the Dependency ID. 

EXAMPLES
     To create a dependency with the ID `my-dependency`, run: 
    
    
    gcloud alpha apihub dependencies create --dependency=my-dependency --consumer=projects/my-project/locations/us-central1/apis/my-api/versions/v1/operations/get-users --supplier=projects/my-project/locations/us-central1/apis/other-api/versions/v1/operations/list-items --project=my-project --location=us-central1

POSITIONAL ARGUMENTS
    

Dependency resource - Identifier. The name of the dependency in the API Hub. 

Format: `projects/{project}/locations/{location}/dependencies/{dependency}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `dependency` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DEPENDENCY`
     ID of the dependency or fully qualified identifier for the dependency. 

To set the `dependency` attribute: 

  * provide the argument `dependency` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the dependency resource. 

To set the `location` attribute: 

  * provide the argument `dependency` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Reference to an entity participating in a dependency. 

This must be specified. 

Arguments for the identifier. 

At most one of these can be specified: 

`--consumer-external-api-resource-name`=`CONSUMER_EXTERNAL_API_RESOURCE_NAME`
     The resource name of an external API in the API Hub. 

Format: `projects/{project}/locations/{location}/externalApis/{external_api}`

`--consumer-operation-resource-name`=`CONSUMER_OPERATION_RESOURCE_NAME`
     The resource name of an operation in the API Hub. 

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

Reference to an entity participating in a dependency. 

This must be specified. 

Arguments for the identifier. 

At most one of these can be specified: 

`--supplier-external-api-resource-name`=`SUPPLIER_EXTERNAL_API_RESOURCE_NAME`
     The resource name of an external API in the API Hub. 

Format: `projects/{project}/locations/{location}/externalApis/{external_api}`

`--supplier-operation-resource-name`=`SUPPLIER_OPERATION_RESOURCE_NAME`
     The resource name of an operation in the API Hub. 

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

OPTIONAL FLAGS
    

`--attributes`=[`ATTRIBUTES`,…]
     The list of user defined attributes associated with the dependency resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource. 

`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 

`enumValues`
     The attribute values associated with a resource in case attribute data type is enum. 

`values`
     The attribute values in case attribute data type is enum. 

`description`
     The detailed description of the allowed value. 
`displayName`
     The display name of the allowed value. 
`id`
     The ID of the allowed value. 

  * If provided, the same will be used. The service will throw an error if the specified id is already used by another allowed value in the same attribute resource. 
  * If not provided, a system generated id derived from the display name will be used. In this case, the service will handle conflict resolution by adding a system generated suffix in case of duplicates. 



This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. 

`immutable`
     When set to true, the allowed value cannot be updated or deleted by the user. It can only be true for System defined attributes. 
`jsonValues`
     The attribute values associated with a resource in case attribute data type is JSON. 

`values`
     The attribute values in case attribute data type is string or JSON. 
`stringValues`
     The attribute values associated with a resource in case attribute data type is string. 

`values`
     The attribute values in case attribute data type is string or JSON. 
`uriValues`
     The attribute values associated with a resource in case attribute data type is URL, URI or IP, like gs://bucket-name/object-name. 

`values`
     The attribute values in case attribute data type is string or JSON. 
`Shorthand Example:`
    
    
    --attributes=string={enumValues={values=[{description=string,displayName=string,id=string,immutable=boolean}]},jsonValues={values=[string]},stringValues={values=[string]},uriValues={values=[string]}}

`JSON Example:`
    
    
    --attributes='{"string": {"enumValues": {"values": [{"description": "string", "displayName": "string", "id": "string", "immutable": boolean}]}, "jsonValues": {"values": ["string"]}, "stringValues": {"values": ["string"]}, "uriValues": {"values": ["string"]}}}'

`File Example:`
    
    
    --attributes=path_to_file.(yaml|json)

`--description`=`DESCRIPTION`
     Human readable description corresponding of the dependency. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `apihub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud apihub dependencies create](https://docs.cloud.google.com/sdk/gcloud/reference/apihub/dependencies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
