---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/subscriptions/pull/
title: gcloud alpha pubsub subscriptions pull \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:00:30.329223+00:00
---

# gcloud alpha pubsub subscriptions pull  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/subscriptions/pull/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha pubsub subscriptions pull Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha pubsub subscriptions pull - pulls one or more Cloud Pub/Sub messages from a subscription 
SYNOPSIS
    

`gcloud alpha pubsub subscriptions pull` `SUBSCRIPTION` [`--auto-ack`] [`--max-messages`=`MAX_MESSAGES`; default=1] [`--return-immediately` | `--no-wait`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Returns one or more messages from the specified Cloud Pub/Sub subscription, if there are any messages enqueued. 

By default, this command returns only one message from the subscription. Use the `--limit` flag to specify the max messages to return. 

Please note that this command is not guaranteed to return all the messages in your backlog or the maximum specified in the --limit argument. Receiving fewer messages than available occasionally is normal. 

POSITIONAL ARGUMENTS
    

Subscription resource - Name of the subscription to pull messages from. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `subscription` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SUBSCRIPTION`
     ID of the subscription or fully qualified identifier for the subscription. 

To set the `subscription` attribute: 

  * provide the argument `subscription` on the command line. 


FLAGS
    

`--auto-ack`
     Automatically ACK every message pulled from this subscription. Use --no-auto-ack to disable this flag. 
`--max-messages`=`MAX_MESSAGES`; default=1
     (DEPRECATED) The maximum number of messages that Cloud Pub/Sub can return in this response. 

`--max-messages` is deprecated. Please use --limit instead. 

Pull timeout behavior. 

At most one of these can be specified: 

`--return-immediately`
     If this flag is set, the system responds immediately with any messages readily available in memory buffers. If no messages are available in the buffers, returns an empty list of messages as response, even if having messages in the backlog. Do not set this flag as it adversely impacts the performance of pull. Use --no-return-immediately to disable this flag. 
`--wait`
     (DEPRECATED) Wait (for a bounded amount of time) for new messages from the subscription, if there are none. 

`--wait` is deprecated. This flag is non-operational, as the wait behavior is now the default. Enabled by default, use `--no-wait` to disable. 

LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud pubsub subscriptions pull](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/pull)
    
    
    [gcloud beta pubsub subscriptions pull](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/pull)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
