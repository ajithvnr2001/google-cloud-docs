---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/data-products/data-assets/create/
title: gcloud alpha dataplex data-products data-assets create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:17:34.063045+00:00
---

# gcloud alpha dataplex data-products data-assets create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataplex/data-products/data-assets/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha dataplex data-products data-assets create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha dataplex data-products data-assets create - create a Dataplex data asset resource 
SYNOPSIS
    

`gcloud alpha dataplex data-products data-assets create` (`DATA_ASSET` : `--data-product`=`DATA_PRODUCT` `--location`=`LOCATION`) `--resource`=`RESOURCE` [`--access-groups`=`ACCESS_GROUPS`] [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Dataplex data asset resource. 
EXAMPLES
     To create a Dataplex data asset `test-da` in data product `test-dp` in location `us-central1` with resource "//SERVICE_NAME/projects/MY_PROJECT/datasets/MY_DATASET/tables/MY_TABLE", run: 
    
    
    gcloud alpha dataplex data-products data-assets create test-da --data-product=test-dp --location=us-central1 --resource=//SERVICE_NAME/projects/MY_PROJECT/datasets/MY_DATASET/tables/MY_TABLE

POSITIONAL ARGUMENTS
    

Data asset resource - Arguments and flags that specify the Dataplex Data Asset you want to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `data_asset` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`DATA_ASSET`
     ID of the data asset or fully qualified identifier for the data asset. 

To set the `data_asset` attribute: 

  * provide the argument `data_asset` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--data-product`=`DATA_PRODUCT`
     Identifier of the Dataplex Data Product resource. To set the `data-product` attribute: 

  * provide the argument `data_asset` on the command line with a fully specified name; 
  * provide the argument `--data-product` on the command line. 


`--location`=`LOCATION`
     Location of the Dataplex resource. To set the `location` attribute: 

  * provide the argument `data_asset` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `dataplex/location`. 


REQUIRED FLAGS
    

`--resource`=`RESOURCE`
     Full resource name of the cloud resource represented by the data asset. 
OPTIONAL FLAGS
    

`--access-groups`=`ACCESS_GROUPS`
     Access groups configurations for this data asset. Each access group config should be a JSON string. Expected schema: { "id": "group-id", "iam_roles": ["role-1", "role-2"] } 
`--async`
     Return immediately, without waiting for the operation in progress to complete. 
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
    
    
    [gcloud dataplex data-products data-assets create](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/data-products/data-assets/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
