---
url: https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/create/
title: gcloud essential-contacts create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:26:42.809276+00:00
---

# gcloud essential-contacts create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud essential-contacts create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud essential-contacts create - create an essential contact 
SYNOPSIS
    

`gcloud essential-contacts create` `--email`=`EMAIL` `--language`=`LANGUAGE` `--notification-categories`=[`NOTIFICATION_CATEGORIES`,…] [`--folder`=`FOLDER` | `--organization`=`ORGANIZATION` | `--project`=`PROJECT`] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To create a contact in the current project, run: 
    
    
    gcloud essential-contacts create --email=contact-email@example.com --notification-categories=technical,product-updates --language=en-US

To create a contact in the folder with id ``456``, run: 
    
    
    gcloud essential-contacts create --email=contact-email@example.com --notification-categories=technical,product-updates --language=en-US --folder=456

To create a contact in the organization with id ``456``, run: 
    
    
    gcloud essential-contacts create --email=contact-email@example.com --notification-categories=technical,product-updates --language=en-US --organization=456

REQUIRED FLAGS
    

`--email`=`EMAIL`
     email address of contact. 
`--language`=`LANGUAGE`
     preferred language of contact. Must be a valid ISO 639-1 language code. 
`--notification-categories`=[`NOTIFICATION_CATEGORIES`,…]
     list of notification categories contact is subscribed to. `NOTIFICATION_CATEGORIES` must be one of: `all`, `billing`, `legal`, `notification-category-unspecified`, `product-updates`, `security`, `suspension`, `technical`, `technical-incidents`. 
OPTIONAL FLAGS
    

At most one of these can be specified: 

`--folder`=`FOLDER`
     folder number where contacts are set. If neither --project, --folder, nor \--organization are provided then the config property [core/project] will be used as the resource. 
`--organization`=`ORGANIZATION`
     organization number where contacts are set. If neither --project, --folder, nor \--organization are provided then the config property [core/project] will be used as the resource. 
`--project`=`PROJECT`
     project number or id where contacts are set. If neither --project, --folder, nor \--organization are provided then the config property [core/project] will be used as the resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha essential-contacts create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/essential-contacts/create)
    
    
    [gcloud beta essential-contacts create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/essential-contacts/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
