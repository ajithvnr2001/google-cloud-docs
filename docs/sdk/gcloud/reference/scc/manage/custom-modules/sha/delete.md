---
url: https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/delete/
title: gcloud scc manage custom-modules sha delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:31:03.694135+00:00
---

# gcloud scc manage custom-modules sha delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/scc/manage/custom-modules/sha/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud scc manage custom-modules sha delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud scc manage custom-modules sha delete - delete a Security Health Analytics custom module 
SYNOPSIS
    

`gcloud scc manage custom-modules sha delete` `MODULE_ID_OR_NAME` [`--validate-only`] [`--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--parent`=`PARENT` | `--project`=`PROJECT_ID_OR_NUMBER`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete a Security Health Analytics custom module. User specifies the custom module as well as the parent of the module to delete. A validation_only flag is optional. When set to true only validations (including IAM checks) will done for the request (module will not be deleted). 
EXAMPLES
     To delete an Security Health Analytics custom module with ID `123456` for organization `123`, run: 
    
    
    gcloud scc manage custom-modules sha delete 123456 --organization=123

To delete a Security Health Analytics custom module with ID `123456` for folder `456`, run: 
    
    
    gcloud scc manage custom-modules sha delete 123456 --folder=456

To delete a Security Health Analytics custom module with ID `123456` for project `789`, run: 
    
    
    gcloud scc manage custom-modules sha delete 123456 --project=789

You can also specify the parent more generally: 
    
    
    gcloud scc manage custom-modules sha delete 123456 --parent=organizations/123

Or just specify the fully qualified module name: 
    
    
    gcloud scc manage custom-modules sha delete organizations/123/locations/global/securityHealthAnalyticsCustomModules/123456

POSITIONAL ARGUMENTS
    

`MODULE_ID_OR_NAME`
     The custom module ID or name. The expected format is {parent}/[locations/global]/securityHealthAnalyticsCustomModules/{module_id} or just {module_id}. Where module_id is a numeric identifier 1-20 characters in length. Parent is of the form organizations/{id}, projects/{id or name}, folders/{id}. 
FLAGS
    

`--validate-only`
     If present, the request is validated (including IAM checks) but no action is taken. 
At most one of these can be specified: 

`--folder`=`FOLDER_ID`
     Folder associated with the custom module. 
`--organization`=`ORGANIZATION_ID`
     Organization associated with the custom module. 
`--parent`=`PARENT`
     Parent associated with the custom module. Can be one of organizations/<id>, projects/<id or name>, folders/<id>
`--project`=`PROJECT_ID_OR_NUMBER`
     Project associated with the custom module. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha scc manage custom-modules sha delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/scc/manage/custom-modules/sha/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
