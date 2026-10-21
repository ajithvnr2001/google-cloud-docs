---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/attributes/create/
title: gcloud alpha apihub attributes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:45.288190+00:00
---

# gcloud alpha apihub attributes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/apihub/attributes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha apihub attributes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha apihub attributes create - create an Attribute 
SYNOPSIS
    

`gcloud alpha apihub attributes create` (`ATTRIBUTE` : `--location`=`LOCATION`) `--data-type`=`DATA_TYPE` `--display-name`=`DISPLAY_NAME` `--scope`=`SCOPE` [`--allowed-values`=[`description`=`DESCRIPTION`],[`displayName`=`DISPLAYNAME`],[`id`=`ID`],[`immutable`=`IMMUTABLE`]] [`--cardinality`=`CARDINALITY`] [`--description`=`DESCRIPTION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create an attribute 
EXAMPLES
     To create an attribute with the ID `my-attribute`, run: 
    
    
    gcloud alpha apihub attributes create --attribute=my-attribute --display-name="My Attribute" --scope=api --data-type=string --project=my-project --location=us-central1

POSITIONAL ARGUMENTS
    

Attribute resource - Identifier. The name of the attribute in the API Hub. 

Format: `projects/{project}/locations/{location}/attributes/{attribute}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `attribute` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ATTRIBUTE`
     ID of the attribute or fully qualified identifier for the attribute. 

To set the `attribute` attribute: 

  * provide the argument `attribute` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the attribute resource. 

To set the `location` attribute: 

  * provide the argument `attribute` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--data-type`=`DATA_TYPE`
     The type of the data of the attribute. `DATA_TYPE` must be one of: 

`enum`
     Attribute's value is of type enum. 
`json`
     Attribute's value is of type json. 
`string`
     Attribute's value is of type string. 
`uri`
     Attribute's value is of type uri. 
`--display-name`=`DISPLAY_NAME`
     The display name of the attribute. 
`--scope`=`SCOPE`
     The scope of the attribute. It represents the resource in the API Hub to which the attribute can be linked. `SCOPE` must be one of: 

`api`
     Attribute can be linked to an API. 
`api-operation`
     Attribute can be linked to an API Operation. 
`definition`
     Attribute can be linked to a definition. 
`dependency`
     Attribute can be linked to a Dependency. 
`deployment`
     Attribute can be linked to a Deployment. 
`external-api`
     Attribute can be linked to a ExternalAPI. 
`plugin`
     Attribute can be linked to a Plugin. 
`spec`
     Attribute can be linked to a Spec. 
`version`
     Attribute can be linked to an API version. 
OPTIONAL FLAGS
    

`--allowed-values`=[`description`=`DESCRIPTION`],[`displayName`=`DISPLAYNAME`],[`id`=`ID`],[`immutable`=`IMMUTABLE`]
     The list of allowed values when the attribute value is of type enum. This is required when the data_type of the attribute is ENUM. The maximum number of allowed values of an attribute will be 1000. 

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
`Shorthand Example:`
    
    
    --allowed-values=description=string,displayName=string,id=string,immutable=boolean --allowed-values=description=string,displayName=string,id=string,immutable=boolean

`JSON Example:`
    
    
    --allowed-values='[{"description": "string", "displayName": "string", "id": "string", "immutable": boolean}]'

`File Example:`
    
    
    --allowed-values=path_to_file.(yaml|json)

`--cardinality`=`CARDINALITY`
     The maximum number of values that the attribute can have when associated with an API Hub resource. Cardinality 1 would represent a single-valued attribute. It must not be less than 1 or greater than 20. If not specified, the cardinality would be set to 1 by default and represent a single-valued attribute. 
`--description`=`DESCRIPTION`
     The description of the attribute. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `apihub/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/apigee/docs/api-hub/what-is-api-hub>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud apihub attributes create](https://docs.cloud.google.com/sdk/gcloud/reference/apihub/attributes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
