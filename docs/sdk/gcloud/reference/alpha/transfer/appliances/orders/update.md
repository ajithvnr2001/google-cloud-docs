---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/appliances/orders/update/
title: gcloud alpha transfer appliances orders update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:57.046721+00:00
---

# gcloud alpha transfer appliances orders update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/appliances/orders/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha transfer appliances orders update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha transfer appliances orders update - update an order for a transfer appliance 
SYNOPSIS
    

`gcloud alpha transfer appliances orders update` `ORDER` [`--region`=`REGION`] [`--submit`] [`--cmek`=`CMEK` `--display-name`=`DISPLAY_NAME` `--model`=`MODEL` `--offline-export`=[`manifest`=`MANIFEST`],[`source`=`SOURCE`] `--offline-import`=`OFFLINE_IMPORT` `--online-import`=`ONLINE_IMPORT`] [`--address`=[`administrative-area`=`ADMINISTRATIVE-AREA`],[`lines`=`LINES`],[`locality`=`LOCALITY`],[`postal-code`=`POSTAL-CODE`] `--delivery-notes`=`DELIVERY_NOTES` `--order-contact`=[`business`=`BUSINESS`],[`emails`=`EMAILS`],[`name`=`NAME`],[`phone`=`PHONE`] `--shipping-contact`=[`business`=`BUSINESS`],[`emails`=`EMAILS`],[`name`=`NAME`],[`phone`=`PHONE`]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `gcloud alpha transfer appliances orders update` facilitates the update of Transfer Appliance Orders. 
EXAMPLES
     To update the shipping contact of an appliance called `my-appliance`: 
    
    
    gcloud alpha transfer appliances orders update my-appliance --shipping-contact="name=Jane Doe,emails=[jane@example.com],phone=12345678910"

POSITIONAL ARGUMENTS
    

Order resource - The order to update. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `order` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `region` attribute: 

  * provide the argument `order` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line. 



This must be specified. 

`ORDER`
     ID of the order or fully qualified identifier for the order. 

To set the `order` attribute: 

  * provide the argument `order` on the command line. 


FLAGS
    

`--region`=`REGION`
     The location affiliated with the appliance order to update. `REGION` must be one of: `us-central1`, `europe-west1`, `asia-southeast1`. 
`--submit`
     Submits an order that is in draft. 
APPLIANCE FLAGS
    

`--cmek`=`CMEK`
     Customer-managed key which will add additional layer of security. By default data is encrypted with a Google-managed key. 
`--display-name`=`DISPLAY_NAME`
     A mutable, user-settable name for both the appliance and the order. 
`--model`=`MODEL`
     Model of the appliance to order. `MODEL` must be one of: `TA40_RACKABLE`, `TA40_STANDALONE`, `TA300_RACKABLE`, `TA300_STANDALONE`, `TA7`, `EA_STORAGE_7`, `EA_GPU_T4`. 
`--offline-export`=[`manifest`=`MANIFEST`],[`source`=`SOURCE`]
     Configuration for an offline export transfer, where data is downloaded onto the appliance at Google and copied from the appliance at the customer site. 

`source`
     The Cloud Storage bucket or folder where the data is located, in the form of `gs://my-bucket/path/to/folder/`. 
`manifest`
     Specifies the path to the manifest in Cloud Storage. An example path is `gs://bucket_name/path/manifest.csv`. The paths in the manifest file are relative to bucketname. For example, to export `SOURCE_PATH/object1.pdf`, manifest will have `object1.pdf` in the first column, followed by object version (optional). For more information see <https://cloud.google.com/storage-transfer/docs/manifest#object_storage_transfers>. 
`--offline-import`=`OFFLINE_IMPORT`
     Destination for a offline import, where data is loaded onto the appliance at the customer site and ingested at Google. Should be in the form of `gs://my-bucket/path/to/folder/`. 
`--online-import`=`ONLINE_IMPORT`
     Destination for a online import, where data is loaded onto the appliance and automatically transferred to Cloud Storage whenever it has an internet connection. Should be in the form of `gs://my-bucket/path/to/folder/`. 
DELIVERY FLAGS
    

`--address`=[`administrative-area`=`ADMINISTRATIVE-AREA`],[`lines`=`LINES`],[`locality`=`LOCALITY`],[`postal-code`=`POSTAL-CODE`]
     Address where the appliance will be shipped. All fields (or list items) have a maximum of 80 characters. For more information see <https://support.google.com/business/answer/6397478>. 

`lines`
     Line of the postal address that doesn't fit in the other fields. For most countries/regions, the first line will include a street number and street name. You can have up to 5 address lines. 
`locality`
     Generally refers to the city/town portion of the address. 
`administrative_area`
     The state or province where the business is located. Enter the full name (e.g. "California"), common postal abbreviation (e.g. "CA"), or subdivision (ISO 3166-2) code (e.g. "US-CA"). 
`postal_code`
     The postal code of the address. 
`--delivery-notes`=`DELIVERY_NOTES`
     Add any additional details about your order, such as site details and a preference date when the appliance should be delivered. 
`--order-contact`=[`business`=`BUSINESS`],[`emails`=`EMAILS`],[`name`=`NAME`],[`phone`=`PHONE`]
    

`business`
     Name of the business, if applicable. 
`name`
     Name of the primary contact. 
`phone`
     The phone number of the primary contact. Should be given in E.164 format consisting of the country calling code (1 to 3 digits) and the subscriber number, with no additional spaces or formatting, e.g. `15552220123`. 
`emails`
     The email of the primary contact along with any additional email addresses to include with all correspondence. 
`--shipping-contact`=[`business`=`BUSINESS`],[`emails`=`EMAILS`],[`name`=`NAME`],[`phone`=`PHONE`]
    

`business`
     Name of the business, if applicable. 
`name`
     Name of the primary contact. 
`phone`
     The phone number of the primary contact. Should be given in E.164 format consisting of the country calling code (1 to 3 digits) and the subscriber number, with no additional spaces or formatting, e.g. `15552220123`. 
`emails`
     The email of the primary contact along with any additional email addresses to include with all correspondence. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
