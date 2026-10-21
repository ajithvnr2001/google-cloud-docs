---
url: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/delta-sharing/catalogs/update/
title: gcloud biglake delta-sharing catalogs update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:27.900402+00:00
---

# gcloud biglake delta-sharing catalogs update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/biglake/delta-sharing/catalogs/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud biglake delta-sharing catalogs update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud biglake delta-sharing catalogs update - update a BigLake Delta Sharing catalog 
SYNOPSIS
    

`gcloud biglake delta-sharing catalogs update` `CATALOG` [`--connector-endpoint`=`CONNECTOR_ENDPOINT`] [`--cross-cloud-cache`=`MODE`] [`--invitation-code`=`INVITATION_CODE`] [`--invitation-url`=`INVITATION_URL`] [`--kms-key`=`KMS_KEY`] [`--refresh-interval`=`REFRESH_INTERVAL`] [`--service-directory-name`=`SERVICE_DIRECTORY_NAME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a BigLake Delta Sharing catalog. 
EXAMPLES
     To update the Cloud KMS key of a BigLake Delta Sharing catalog named `my-catalog`, run: 
    
    
    gcloud biglake delta-sharing catalogs update my-catalog --kms-key=projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-new-key

POSITIONAL ARGUMENTS
    

Catalog resource - The Delta Sharing catalog to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `catalog` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`CATALOG`
     ID of the catalog or fully qualified identifier for the catalog. 

To set the `catalog` attribute: 

  * provide the argument `catalog` on the command line. 


FLAGS
    

`--connector-endpoint`=`CONNECTOR_ENDPOINT`
     The SAP BDC Connector Endpoint. 
`--cross-cloud-cache`=`MODE`
     Whether to enable caching of remote data on Google Cloud. This may result in data being temporarily persisted on Google Cloud. `MODE` must be one of: `disabled`, `enabled`. 
`--invitation-code`=`INVITATION_CODE`
     The SAP BDC Invitation Code. 
`--invitation-url`=`INVITATION_URL`
     The combined invitation URL containing both endpoint and code. 
`--kms-key`=`KMS_KEY`
     Cloud KMS key name for encryption of resources in the catalog. 
`--refresh-interval`=`REFRESH_INTERVAL`
     The interval for refreshing metadata from the remote catalog (e.g. 300s or 5m). 
`--service-directory-name`=`SERVICE_DIRECTORY_NAME`
     The service directory resource name for private networking. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `biglake/delta_v1` API. The full documentation for this API can be found at: <https://cloud.google.com/bigquery/>
NOTES
     This variant is also available: 
    
    
    [gcloud alpha biglake delta-sharing catalogs update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/biglake/delta-sharing/catalogs/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
