---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/modify-push-config/
title: gcloud beta pubsub subscriptions modify-push-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:14:15.323764+00:00
---

# gcloud beta pubsub subscriptions modify-push-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/modify-push-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta pubsub subscriptions modify-push-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta pubsub subscriptions modify-push-config - modifies the push configuration of a Cloud Pub/Sub subscription 
SYNOPSIS
    

`gcloud beta pubsub subscriptions modify-push-config` `SUBSCRIPTION` `--push-endpoint`=`PUSH_ENDPOINT` [`--push-auth-service-account`=`SERVICE_ACCOUNT_EMAIL`] [`--push-auth-token-audience`=`OPTIONAL_AUDIENCE_OVERRIDE`] [`--push-no-wrapper` : `--push-no-wrapper-write-metadata`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Modifies the push configuration of a Cloud Pub/Sub subscription. 
POSITIONAL ARGUMENTS
    

Subscription resource - Name of the subscription to modify. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `subscription` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SUBSCRIPTION`
     ID of the subscription or fully qualified identifier for the subscription. 

To set the `subscription` attribute: 

  * provide the argument `subscription` on the command line. 


REQUIRED FLAGS
    

`--push-endpoint`=`PUSH_ENDPOINT`
     A URL to use as the endpoint for this subscription. This will also automatically set the subscription type to PUSH. 
OPTIONAL FLAGS
    

`--push-auth-service-account`=`SERVICE_ACCOUNT_EMAIL`
     Service account email used as the identity for the generated Open ID Connect token for authenticated push. 
`--push-auth-token-audience`=`OPTIONAL_AUDIENCE_OVERRIDE`
     Audience used in the generated Open ID Connect token for authenticated push. If not specified, it will be set to the push-endpoint. 
NoWrapper Config Options. 
`--push-no-wrapper`
     When set, the message data is delivered directly as the HTTP body. Use \--no-push-no-wrapper to disable this flag. 

This flag argument must be specified if any of the other arguments in this group are specified. 

`--push-no-wrapper-write-metadata`
     When true, writes the Pub/Sub message metadata to `x-goog-pubsub-<KEY>:<VAL>` headers of the HTTP request. Writes the Pub/Sub message attributes to `<KEY>:<VAL>` headers of the HTTP request. Use --no-push-no-wrapper-write-metadata to disable this flag. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud pubsub subscriptions modify-push-config](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config)
    
    
    [gcloud alpha pubsub subscriptions modify-push-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/subscriptions/modify-push-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
