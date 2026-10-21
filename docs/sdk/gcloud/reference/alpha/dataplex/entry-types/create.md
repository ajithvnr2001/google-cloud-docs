---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entry-types/create/
title: gcloud alpha dataplex entry-types create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:43.178043+00:00
---

# gcloud alpha dataplex entry-types create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/entry-types/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex entry-types create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex entry-types create - create a Dataplex Entry Type 
SYNOPSIS
    

`gcloud alpha dataplex entry-types create` (`ENTRY_TYPE` : `--location`=`LOCATION`) [`--description`=`DESCRIPTION`] [`--display-name`=`DISPLAY_NAME`] [`--labels`=[`KEY`=`VALUE`,…]] [`--platform`=`PLATFORM`] [`--required-aspects`=[`type`=`TYPE`]] [`--system`=`SYSTEM`] [`--type-aliases`=[`TYPE_ALIASES`,…]] [`--async` | `--validate-only`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Entry Type is a template for creating Entries. 
EXAMPLES
     To create Entry Type `test-entry-type` in project `test-dataplex` at location `us-central1`, with description `test description`, displayName `test display name` and required aspect type `projects/test-dataplex/locations/us-central1/aspectTypes/test-aspect-type`, run: 
    
    
    gcloud alpha dataplex entry-types create test-entry-type --location=us-central1 --project=test-project --description='test description' --display-name='test display name' --required-aspects=type='projects/test-dataplex/locations/us-central1/aspectTypes/test-aspect-type'

POSITIONAL ARGUMENTS
    

Entry type resource - Arguments and flags that define the Dataplex entry type you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `entry_type` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`ENTRY_TYPE`
     ID of the entry type or fully qualified identifier for the entry type. 

To set the `entry_type` attribute: 

  * provide the argument `entry_type` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Dataplex resource. 

To set the `location` attribute: 

  * provide the argument `entry_type` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


FLAGS
    

`--description`=`DESCRIPTION`
     Description of the Entry Type. 
`--display-name`=`DISPLAY_NAME`
     Display name of the Entry Type. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--platform`=`PLATFORM`
     The platform that Entries of this type belongs to. 
`--required-aspects`=[`type`=`TYPE`]
     Required aspect type for the entry type. 
`--system`=`SYSTEM`
     The system that Entries of this type belongs to. 
`--type-aliases`=[`TYPE_ALIASES`,…]
     Indicates the class this Entry Type belongs to. 
At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--validate-only`
     Validate the create action, but don't actually perform it. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex entry-types create](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
