---
url: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/update/
title: gcloud eventarc google-api-sources update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:20:43.941329+00:00
---

# gcloud eventarc google-api-sources update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud eventarc google-api-sources update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud eventarc google-api-sources update - update an Eventarc Google API source 
SYNOPSIS
    

`gcloud eventarc google-api-sources update` (`GOOGLE_API_SOURCE` : `--location`=`LOCATION`) [`--async`] [`--logging-config`=`LOGGING_CONFIG`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-crypto-key` | `--crypto-key`=`CRYPTO_KEY`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--clear-project-subscriptions` | `--[no-]organization-subscription` | `--project-subscriptions`=`GAS_PROJECT_SUBSCRIPTION`,[…]] [`--destination-message-bus`=`DESTINATION_MESSAGE_BUS` : `--destination-message-bus-project`=`DESTINATION_MESSAGE_BUS_PROJECT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update an Eventarc Google API source. 
EXAMPLES
     To update the Google API source `my-google-api-source` in location `us-central1` with destination message bus `my-message-bus`, run: 
    
    
    gcloud eventarc google-api-sources update my-google-api-source --location=us-central1 --destination-message-bus=my-message-bus

To update the Google API source `my-google-api-source` in location `us-central1` with `INFO` level logging, run: 
    
    
    gcloud eventarc google-api-sources update my-google-api-source --location=us-central1 --logging-config=INFO

To update the Google API source `my-google-api-source` in location `us-central1` with a Cloud KMS CryptoKey, run: 
    
    
    gcloud eventarc google-api-sources update my-google-api-source --location=us-central1 --crypto-key=projects/PROJECT_ID/locations/KMS_LOCATION/keyRings/KEYRING/cryptoKeys/KEY

POSITIONAL ARGUMENTS
    

Google API source resource - The Google API source to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `google_api_source` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`GOOGLE_API_SOURCE`
     ID of the Google API source or fully qualified identifier for the Google API source. 

To set the `google-api-source` attribute: 

  * provide the argument `google_api_source` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location for the Eventarc Google API source, which should be one of the supported regions. Alternatively, set the [eventarc/location] property. 

To set the `location` attribute: 

  * provide the argument `google_api_source` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--logging-config`=`LOGGING_CONFIG`
     The logging config of the Google API source. `LOGGING_CONFIG` must be one of: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-crypto-key`
     Remove the previously configured crypto key. The channel will continue to be encrypted using Google-managed keys. 
`--crypto-key`=`CRYPTO_KEY`
     Fully qualified name of the crypto key to use for customer-managed encryption. If this is unspecified, Google-managed keys will be used for encryption. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud eventarc google-api-sources update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud eventarc google-api-sources update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
At most one of these can be specified: 

`--clear-project-subscriptions`
     Clear the project subscriptions for the resource. 
`--[no-]organization-subscription`
     The organization subscription for the resource. Use `--organization-subscription` to enable and `--no-organization-subscription` to disable. 
`--project-subscriptions`=`GAS_PROJECT_SUBSCRIPTION`,[…]
     The project subscriptions for the resource. 
Message bus resource - The destination message bus of the Google API source. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `location` attribute: 

  * provide the argument `--destination-message-bus` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 


`--destination-message-bus`=`DESTINATION_MESSAGE_BUS`
     ID of the message bus or fully qualified identifier for the message bus. 

To set the `message-bus` attribute: 

  * provide the argument `--destination-message-bus` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--destination-message-bus-project`=`DESTINATION_MESSAGE_BUS_PROJECT`
     Project ID of the Google Cloud project for the message bus. 

To set the `project` attribute: 

  * provide the argument `--destination-message-bus` on the command line with a fully specified name; 
  * provide the argument `--destination-message-bus-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta eventarc google-api-sources update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/eventarc/google-api-sources/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
