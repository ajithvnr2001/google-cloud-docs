---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/eventarc/google-api-sources/create/
title: gcloud beta eventarc google-api-sources create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:50.011296+00:00
---

# gcloud beta eventarc google-api-sources create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/eventarc/google-api-sources/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta eventarc google-api-sources create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta eventarc google-api-sources create - create an Eventarc Google API source 
SYNOPSIS
    

`gcloud beta eventarc google-api-sources create` (`GOOGLE_API_SOURCE` : `--location`=`LOCATION`) (`--destination-message-bus`=`DESTINATION_MESSAGE_BUS` : `--destination-message-bus-project`=`DESTINATION_MESSAGE_BUS_PROJECT`) [`--async`] [`--crypto-key`=`CRYPTO_KEY`] [`--labels`=[`KEY`=`VALUE`,…]] [`--logging-config`=`LOGGING_CONFIG`] [`--[no-]organization-subscription` | `--project-subscriptions`=`GAS_PROJECT_SUBSCRIPTION`,[…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create an Eventarc Google API source. 
EXAMPLES
     To create a new Google API source `my-google-api-source` in location `us-central1` with a destination message bus `my-message-bus`, run: 
    
    
    gcloud beta eventarc google-api-sources create my-google-api-source --location=us-central1 --destination-message-bus=my-message-bus

POSITIONAL ARGUMENTS
    

Google API source resource - The Google API source to create. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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


REQUIRED FLAGS
    

Message bus resource - The destination message bus of the Google API source. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `location` attribute: 

  * provide the argument `--destination-message-bus` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `eventarc/location`. 



This must be specified. 

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


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--crypto-key`=`CRYPTO_KEY`
     Fully qualified name of the crypto key to use for customer-managed encryption. If this is unspecified, Google-managed keys will be used for encryption. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--logging-config`=`LOGGING_CONFIG`
     The logging config for the Google API source. `LOGGING_CONFIG` must be one of: `NONE`, `DEBUG`, `INFO`, `NOTICE`, `WARNING`, `ERROR`, `CRITICAL`, `ALERT`, `EMERGENCY`. 
At most one of these can be specified: 

`--[no-]organization-subscription`
     The organization subscription for the resource. Use `--organization-subscription` to enable and `--no-organization-subscription` to disable. 
`--project-subscriptions`=`GAS_PROJECT_SUBSCRIPTION`,[…]
     The project subscriptions for the resource. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud eventarc google-api-sources create](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/google-api-sources/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
