---
url: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/data-product-sharing/publish/
title: gcloud biglake data-product-sharing publish \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:27.438134+00:00
---

# gcloud biglake data-product-sharing publish  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/data-product-sharing/publish/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud biglake data-product-sharing publish Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud biglake data-product-sharing publish - publish a Knowledge Catalog Data Product or BigLake tables to external partners 
SYNOPSIS
    

`gcloud biglake data-product-sharing publish` `--connection-catalog`=`CONNECTION_CATALOG` `--sap-federated-identity-provider`=`SAP_FEDERATED_IDENTITY_PROVIDER` `--share`=`SHARE` (`--data-product`=`DATA_PRODUCT` | `--iceberg-catalog`=`ICEBERG_CATALOG`) [`--description`=`DESCRIPTION`] [`--short-description`=`SHORT_DESCRIPTION`] [`--title`=`TITLE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Publish a Knowledge Catalog Data Product or BigLake tables to external partners. 
REQUIRED FLAGS
    

Catalog resource - The delta sharing catalog that contains information about where the data product is published. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--connection-catalog` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--connection-catalog`=`CONNECTION_CATALOG`
     ID of the catalog or fully qualified identifier for the catalog. 

To set the `catalog` attribute: 

  * provide the argument `--connection-catalog` on the command line. 


`--sap-federated-identity-provider`=`SAP_FEDERATED_IDENTITY_PROVIDER`
     The resource name of the Workload Identity Federation (WIF) provider resource representing the SAP federated identity. You must manually grant this identity the necessary IAM permissions (e.g., roles/biglake.viewer) on the underlying catalog. 
`--share`=`SHARE`
     The desired name of the Share as it will be published to 
source 

Exactly one of these must be specified: 

`--data-product`=`DATA_PRODUCT`
     The Knowledge Catalog Data Product to publish. 
Or at least one of these can be specified: 

Catalog resource - The BigLake Iceberg REST Catalog whose tables will be published. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--iceberg-catalog` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


`--iceberg-catalog`=`ICEBERG_CATALOG`
     ID of the catalog or fully qualified identifier for the catalog. 

To set the `catalog` attribute: 

  * provide the argument `--iceberg-catalog` on the command line. 


OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     The optional detailed description of the published share. 
`--short-description`=`SHORT_DESCRIPTION`
     The short, concise description of the published share. Required when publishing an Iceberg catalog. 
`--title`=`TITLE`
     The title of the published share. Required when publishing an Iceberg catalog. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha biglake data-product-sharing publish](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/data-product-sharing/publish)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
