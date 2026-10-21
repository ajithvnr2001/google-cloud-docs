---
url: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete/
title: gcloud resource-manager tags bindings delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:11:48.377788+00:00
---

# gcloud resource-manager tags bindings delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud resource-manager tags bindings delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud resource-manager tags bindings delete - deletes a TagBinding 
SYNOPSIS
    

`gcloud resource-manager tags bindings delete` `--parent`=`PARENT` `--tag-value`=`TAG_VALUE` [`--async`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Deletes a TagBinding given the TagValue and the parent resource that the TagValue is attached to. The parent must be given as the full resource name. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>. The TagValue can be represented with its numeric id or its namespaced name of {parent_namespace}/{tag_key_short_name}/{tag_value_short_name}. 
EXAMPLES
     To delete a TagBinding between tagValue/111 and Project with name ``//cloudresourcemanager.googleapis.com/projects/1234`` run: 
    
    
    gcloud resource-manager tags bindings delete --tag-value=tagValue/123 --parent=//cloudresourcemanager.googleapis.com/projects/1234

To delete a binding between TagValue test under TagKey ``env`` that lives under ``organizations/789`` and Project with name ``//cloudresourcemanager.googleapis.com/projects/1234`` run: 
    
    
    gcloud resource-manager tags bindings delete --tag-value=789/env/test --parent=//cloudresourcemanager.googleapis.com/projects/1234

REQUIRED FLAGS
    

`--parent`=`PARENT`
     Full resource name of the resource attached to the tagValue. 
`--tag-value`=`TAG_VALUE`
     Tag value name or namespaced name. The name should be in the form tagValues/{numeric_id}. The namespaced name should be in the form {org_id}/{tag_key_short_name}/{short_name} where short_name must be 1-63 characters, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (`), dots (.), and alphanumerics between. `
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--location`=`LOCATION`
     Region or zone of the resource to unbind from the TagValue. This field is not required if the resource is a global resource like projects, folders and organizations. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha resource-manager tags bindings delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/resource-manager/tags/bindings/delete)
    
    
    [gcloud beta resource-manager tags bindings delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/resource-manager/tags/bindings/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
