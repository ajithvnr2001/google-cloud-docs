---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview/
title: Apigee Spaces overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:38.744402+00:00
---

# Apigee Spaces overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/apigee-spaces-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Spaces overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to use Apigee Spaces to implement granular [Identity and Access Management](https://docs.cloud.google.com/iam/docs) control over your Apigee organization resources.

Apigee Spaces enables identity-based isolation and grouping of API resources within an Apigee organization. With Apigee Spaces, you can have granular IAM control over access to your API proxies, shared flows and API products.

You can create multiple Spaces in the same organization for different teams, development projects, or environments and set the IAM controls for each Space. Any API resources created under a Space will inherit the IAM policies applied to that Space.

## When to use Apigee Spaces

Managing IAM permissions for multiple teams working within a single Apigee organization can be complex. Using Spaces can simplify IAM administration with granular controls and simplified permissions for accessing organization resources. 

With Spaces, you can host multiple teams in an Apigee organization where: 

  * Each team maintains their own independent set of API proxies, shared flows, and API products. 
  * Team members have read/write access to the set of API proxies, shared flows, and API products. 
  * Members of _another_ team can be granted specific access (read, or read/write, or trace/debug access) to one or more of the API proxies, shared flows, or API products. 
  * Multiple teams can access a common set of API proxies, shared flows, and API products with fine-grained permissions. 



Apigee Spaces can be used with Apigee [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) and [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) organizations, including [Apigee hybrid-enabled](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/what-is-hybrid) organizations. Spaces can be used with Apigee organizations that have [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#summary) enabled. Apigee hybrid organizations must use hybrid version 1.13 or higher. For information on upgrading to version 1.13, see [Upgrade your Apigee hybrid organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade).

## Benefits of Apigee Spaces

There are several benefits to using Apigee Spaces, including: 

  * **Improved security** : Using Spaces can improve security by allowing you to control access to resources at a granular level. You can grant different users and groups access to different Spaces, and control which resources are available in each Spaces. This helps isolate and protect access to sensitive data or resources.
  * **Simplified management** : Spaces can help you simplify your management tasks by providing a way to logically group your resources. You can manage all of the resources in a Space together, and you can easily see which users and groups have access to each resource.
  * **Increased flexibility** : Spaces give you flexibility in how you manage your Apigee resources. You can create as many Spaces as you need and you can move resources between spaces as needed, letting you adapt to changing needs.



Spaces provide the ability to introduce resource isolation at a team level, providing a clear separation of resources associated with different teams operating within the same Apigee organization. In addition, IAM policies can be applied at the Space level, eliminating the need to manage permissions individually for every API proxy, shared flow, and API product.

## Limitations

The following limitations apply to Apigee Spaces: 

  * To use Apigee Spaces, Apigee hybrid customers must use hybrid version 1.13 or higher. For information on upgrading to version 1.13, see [Upgrade your Apigee hybrid organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/upgrade).
  * The following limits apply when using Apigee Spaces: 
    * There is a maximum of 20 Spaces per Apigee organization.
    * There is a limit of 10 queries per second (QPS) for `list` operations for API proxy, API product, and shared flow endpoints.

For more information about Apigee limits, see [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#spaces).




## What's next

  * Learn how to [Create and manage Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/create-spaces).
  * Discover how to [Manage API resources in Apigee Spaces](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/spaces/manage-space-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
