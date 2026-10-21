---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/data-products/create/
title: gcloud alpha dataplex data-products create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:33.540969+00:00
---

# gcloud alpha dataplex data-products create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/data-products/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex data-products create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex data-products create - create a Dataplex data product resource 
SYNOPSIS
    

`gcloud alpha dataplex data-products create` (`DATA_PRODUCT` : `--location`=`LOCATION`) `--display-name`=`DISPLAY_NAME` `--owner-emails`=[`OWNER_EMAILS`,…] [`--access-groups`=`ACCESS_GROUPS`] [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Dataplex data product resource. 

The data product ID must conform to RFC-1034 and contain only lower-case letters (a-z), numbers (0-9), or hyphens, with the first character a letter, the last a letter or a number, and a 63 character maximum. If not provided, a system generated ID will be used. 

EXAMPLES
     To create a Dataplex data product `test-dp` in location `us-central1` with display name "test dp" and owner "test@google.com", run: 
    
    
    gcloud alpha dataplex data-products create test-dp --location=us-central1 --display-name="test dp" --owner-emails="test@google.com"

POSITIONAL ARGUMENTS
    

Data product resource - Arguments and flags that specify the Dataplex Data Product you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `data_product` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATA_PRODUCT`
     ID of the data product or fully qualified identifier for the data product. 

To set the `data_product` attribute: 

  * provide the argument `data_product` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Location of the Dataplex resource. To set the `location` attribute: 

  * provide the argument `data_product` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--display-name`=`DISPLAY_NAME`
     Display name of the Dataplex data product. 
`--owner-emails`=[`OWNER_EMAILS`,…]
     Emails of the data product owners. 
OPTIONAL FLAGS
    

`--access-groups`=`ACCESS_GROUPS`
     List of custom user-defined access groups at the data product level. Each access group should be a JSON string. Expected schema: { "id": "group-id", "display_name": "display-name", "description": "description", "principal": { "google_group": "group-email@example.com" } } 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Description of the Dataplex data product. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `dataplex/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/dataplex/docs>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud dataplex data-products create](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/data-products/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
