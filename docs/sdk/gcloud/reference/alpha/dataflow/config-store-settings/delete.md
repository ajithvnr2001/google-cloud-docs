---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow/config-store-settings/delete/
title: gcloud alpha dataflow config-store-settings delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:18.524064+00:00
---

# gcloud alpha dataflow config-store-settings delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow/config-store-settings/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataflow config-store-settings delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataflow config-store-settings delete - delete a Dataflow ConfigStore setting 
SYNOPSIS
    

`gcloud alpha dataflow config-store-settings delete` (`SETTING` : `--folder`=`FOLDER` `--location`=`LOCATION` `--organization`=`ORGANIZATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Delete a Dataflow ConfigStore setting. 
EXAMPLES
     To delete a setting on a project (note: the project must be specified as a project number, not a project ID): 
    
    
    gcloud alpha dataflow config-store-settings delete default_launcher_machine_type --project=123456789012 --location=us-central1

To delete the same setting on a folder or an organization: 
    
    
    gcloud alpha dataflow config-store-settings delete default_launcher_machine_type --folder=123456 --location=us-central1
    
    
    gcloud alpha dataflow config-store-settings delete default_launcher_machine_type --organization=789012 --location=us-central1

POSITIONAL ARGUMENTS
    

Setting resource - The ConfigStore setting to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `setting` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. This resource can be one of the following types: [project_setting, folder_setting, org_setting]. 



This must be specified. 

`SETTING`
     ID of the setting or fully qualified identifier for the setting. 

To set the `setting_id` attribute: 

  * provide the argument `setting` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--folder`=`FOLDER`
     The Google Cloud folder ID. 

To set the `folder` attribute: 

  * provide the argument `setting` on the command line with a fully specified name; 
  * provide the argument `--folder` on the command line. Must be specified for resource of type [folder_setting]. 


`--location`=`LOCATION`
     The location of the ConfigStore setting (e.g. us-central1). 

To set the `location` attribute: 

  * provide the argument `setting` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--organization`=`ORGANIZATION`
     The Google Cloud organization ID. 

To set the `organization` attribute: 

  * provide the argument `setting` on the command line with a fully specified name; 
  * provide the argument `--organization` on the command line. Must be specified for resource of type [org_setting]. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataflow config-store-settings delete](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/config-store-settings/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
