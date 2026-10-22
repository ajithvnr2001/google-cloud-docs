---
url: https://docs.cloud.google.com/api-gateway/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:10.512611+00:00
---

# Quotas and limits  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Resources ](https://docs.cloud.google.com/api-gateway/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This page describes API Gateway's quota limits.

## Limits on APIs, API configs, and gateways

API Gateway enforces the following limits on APIs, API configs, and gateways:

  * **APIs** \- 50 total
  * **API Configs** \- 100 per API
  * **Gateways** \- 50 per region



If you attempt to create a second API config before the first API config creation for the same API completes, one or both configs may not be available for later use in a Gateway.

## Request rate limits

A rate limit of 10,000,000 quota units per 100 seconds per service producer project is enforced by default. One quota unit is consumed for each call to [`services.check`](https://docs.cloud.google.com/service-control/reference/rest/v1/services/check) and for each operation reported by [`services.report`](https://docs.cloud.google.com/service-control/reference/rest/v1/services/report).

**Note:** API Gateway employs efficient caching algorithms so it doesn't call Service Control every time your API is called. So while the default limit is 10,000,000 per 100 seconds, your API can support a much higher volume.

## Payload size limits

The following limits apply specifically to max payload size for traffic through deployed gateways:

Limit | Amount  
---|---  
Request size | 32 megabytes  
Response size | 32 megabytes*  
gRPC transcoding response size | 1 megabyte  
gRPC transcoding request size | 1 megabyte  
  
* Streamed and chunked responses are exempt from this limit. See Streaming.

## Streaming

Streaming is supported in Public Preview on gateways created with streaming enabled. Streaming allows gateways to serve Server-Sent Events (SSE), WebSockets, gRPC bidirectional streaming, and incremental response delivery (HTTP/2 DATA frames or HTTP/1.1 chunked transfer encoding). Streamed and chunked responses are exempt from the 32 MB response size limit, while the 32 MB request size limit still applies. For more information, see [Configure streaming](https://docs.cloud.google.com/api-gateway/docs/streaming-configure).

## Header size limits

The following limits apply specifically to max header size for traffic through deployed gateways:

Limit | Amount  
---|---  
Request headers size | 60 kilobytes  
  
The backend service called by API Gateway may have lower limits.

## How to increase quota

Cloud Quotas adjustment requests are subject to review. If your quota adjustment request requires review, you receive an email acknowledging receipt of your request. If you need further assistance, respond to the email. After reviewing your request, you receive an email notification indicating whether your request was approved.

### Console

To adjust a quota value, follow these steps:

  1. In the Google Cloud console, go to the **IAM & Admin > Quotas & System Limits** page: 

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

If prompted to select a project, select the project that you want to adjust. 
  2. Find the quota value that you want to update in the **Quota** column and select the checkbox next to the quota that you want to update.

If needed, use the **Filter** search box to search for your quota.

  3. Click create**Edit** and the **Quota changes** dialog appears. 

  4. Enter the quota value that you want in the **New value** field. Some quota values have a unit of measurement; if this applies, select the unit that you want in the adjacent list. Click **Done**.

Optional: If you see a checkbox with the text `I understand that this request will remove any overrides`, it means that adjusting the quota value to a number equal to or greater than the default will remove the previous [quota override](https://docs.cloud.google.com/docs/quotas/view-manage#create_override). If this is what you want, select the checkbox and proceed.

  5. To increase your quota value greater than the number indicated on the dialog, select **Apply for higher quota**.

     1. In the **Quota changes** form, enter the updated quota value that you want in the **New value** field. If a **Request description** field appears, enter a description. Click **Done**.

     2. If a **Next** button appears, click **Next** and fill out your contact details in the screen that follows.

  6. Click **Submit request**.




If you find that you can't request an adjustment from the console, request the increase from [Cloud Customer Care](https://docs.cloud.google.com/support).

To learn more about how the quota increase process works, see [About quota adjustments](https://docs.cloud.google.com/docs/quotas/overview#about_increase_requests).

#### Batching requests for higher quota values

You can batch requests for higher quota by selecting the checkbox next to each quota that you want to include. However, batching requests can increase the amount of time it takes for Google Cloud to review your request.

To reduce review time, group quota adjustment requests by product and area. For example, if you want to request adjustments to networking and Compute Engine VM quotas, create one request for the networking quotas and another request for the Compute Engine VM quotas. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
