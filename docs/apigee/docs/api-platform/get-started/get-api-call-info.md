---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-api-call-info/
title: Get information about calls to your APIs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:45.176035+00:00
---

# Get information about calls to your APIs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/get-api-call-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Get information about calls to your APIs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to get information about calls to your APIs, including:

  * The  total number of calls made to all APIs.
  * The total amount of data processed by all APIs.



This information can help you evaluate your Apigee subscription level, as described in [ Subscription entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements).

**Note:** To make the API calls described below, you must have the `apigee.environments.getStats` permission. To learn which Apigee roles have this permission, see [ Apigee roles](https://cloud.google.com/iam/docs/roles-permissions/apigee).

## Total number of calls made to all APIs

To find the total number of calls made to all APIs in a single organization and environment for a given time range, use a [ Metrics API](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/use-analytics-api-measure-api-program-performance) call similar to the one shown below. The result takes into account scenarios in which you have chained proxies together.
    
    
    curl -v "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/stats/?select=sum(message_count)&timeRange=03/01/2023+00:00~03/31/2023+23:59" \
    -H "Authorization: Bearer $TOKEN"

In the above call:

  * ORG is the organization.
  * ENV is the environment.
  * `timeRange` is the time range for the report, in the form `MM/DD/YYYY+HH:MM~MM/DD/YYYY+HH:MM`, where the start date and time and the end date and time are of the form `MM/DD/YYYY+HH:MM`.
  * `$TOKEN` is an environment variable set to your OAuth 2.0 access token, as described in [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20). For information about the `curl` options used in this example, see [Using curl](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#curl). 

**Note:** To find the total number of calls made to your APIs, you must repeat the above call for all your environments and organizations.

The following is an example of the response to the above call:
    
    
    {
      "environments": [
        {
          "metrics": [
            {
              "name": "sum(message_count)",
              "values": [
                "7.44944088E8"
              ]
            }
          ],
          "name": "prod"
        }
      ],
    ...
    }
    

The `values` field of the response contains the number of calls made to the APIs in the organization and environment in the specified time range.

## Total amount of data processed by all APIs

To find the total amount of data processed by all APIs in a single organization and environment for a given time range, use two calls: one for request data and another for response data.

**Note:** The total includes the size of the payload data in the calls, but not header size.

To find the total amount of request data, use a call similar to the following:
    
    
    curl -v "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/stats/?select=sum(request_size)&timeRange=03/01/2023+00:00~03/31/2023+23:59" \
    -H "Authorization: Bearer $TOKEN"

To find the total amount response data, use a call similar to the following:
    
    
    curl -v "https://apigee.googleapis.com/v1/organizations/ORG/environments/ENV/stats/?select=sum(response_size)&timeRange=03/01/2023+00:00~03/31/2023+23:59" \
    -H "Authorization: Bearer $TOKEN"

The variables in these calls are the same as in the previous example.

**Note:** To find the total amount of data processed by your APIs, you must repeat the above calls for all your environments and organizations.

## Note on proxy chaining

If an environment contains multiple proxies [chained together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies), a single call to one of the proxies will be forwarded to the other proxies in the chain. This increases the total count of API calls and the total amount of data processed by all API calls. The commands that return this information, shown in the sections above, take proxy chaining into account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
