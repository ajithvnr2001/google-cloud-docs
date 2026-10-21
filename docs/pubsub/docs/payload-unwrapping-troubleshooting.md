---
url: https://docs.cloud.google.com/pubsub/docs/payload-unwrapping-troubleshooting/
title: Troubleshoot payload unwrapping \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:59.846045+00:00
---

# Troubleshoot payload unwrapping  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/payload-unwrapping-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Troubleshoot payload unwrapping Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with [payload unwrapping](https://docs.cloud.google.com/pubsub/docs/payload-unwrapping).

## HTTP status code errors

When using payload unwrapping, common HTTP status code errors can occur. You can monitor the errors with the [`push_request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#pubsub/subscription/push_request_count) metric.

### 400 bad request

The following error occurs when Pub/Sub can't process the request due to a misconfiguration or missing data. 
    
    
    400 Bad Request
    

This error occurs due to several reasons. The following are some of the most common causes of the error:

  * The payload (message data) doesn't match the expected request format specified by the HTTP endpoint.
  * The necessary headers to process the request are missing.
  * An incorrect HTTP endpoint is configured for the subscription.



To resolve this issue, try the following solutions:

  * Check the format of your payload (message data). Make sure it matches the expected request format specified by the HTTP endpoint.
  * Check that the request contains the required headers. If the headers are missing, you might need to add them in the message attributes. For example, you might need to include `Content-Type`, but others may be necessary as well.
  * Confirm that the HTTP endpoint configured for your subscription is valid.
  * Enable [Dead Letter Queue (DLQ)](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) on your push subscription. This redirects individual messages that can't be delivered. It's helpful to enable DLQ if you see a small number of 400 errors that you want to inspect. 



### 401 unauthorized / 403 forbidden

The following error occurs when Pub/Sub can't process the request due to incorrect or invalid credentials.
    
    
    401 unauthorized / 403 forbidden
    

This error occurs because the push subscription isn't authenticated.

To resolve this issue, try the following solutions:

  * Enable [Push authentication](https://docs.cloud.google.com/pubsub/docs/push#authentication). Using Push authentication is important if you are integrating with Cloud Run or App Engine.

If push authentication doesn't work with your solution, then you might need to add your own authorization key or API key in the publish message attributes.




### 415 Unsupported Media Type

The following error occurs when Pub/Sub can't process the request because the payload format is in an unsupported format.
    
    
    415 Unsupported Media Type
    

This error occurs due to several reasons. The following are some of the most common causes of the error:

  * The endpoint is missing the required media-type header. 



To resolve this issue, try the following solution:

  * Your endpoint likely requires a `Content-Type` header. By default, payload unwrapping doesn't set a media type header. You can set a `Content-Type` header by attaching it as a [publish message attribute](https://docs.cloud.google.com/pubsub/docs/payload-unwrapping).



### 431 request header fields too large / 413 content too large

The following error occurs when Pub/Sub can't process the request because the content sent in the request is too large.
    
    
    431 request header fields too Large / 413 content too large
    

This error occurs if the [attributes in a Pub/Sub message](https://docs.cloud.google.com/pubsub/quotas#resource_limits) exceed the [header limit size of a server](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Size_limits).

To resolve these issues, try the following solutions:

  * Turn off [**Write metadata**](https://docs.cloud.google.com/pubsub/docs/payload-unwrapping#how_payload_unwrapping_works).
  * Enable [Dead Letter Queue (DLQ)](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic) on your push subscription. This redirects individual messages that can't be delivered. After, your subscription continues to operate, but the messages with errors are redirected to a separate topic for further analysis.



## Check if payload unwrapping is enabled

  1. In the Google Cloud console, go to the **Subscriptions** page.

[Open Pub/Sub subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click the name of your service.

The service detail page opens.

  3. In the configuration table, find the following values: **Message data unwrapping** and **Write message metadata**.

The status of payload wrapping (enabled or disabled) is displayed in the corresponding table row.




## What's next

  * If you still have issues with payload unwrapping, see [Getting support](https://docs.cloud.google.com/pubsub/docs/getting-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
