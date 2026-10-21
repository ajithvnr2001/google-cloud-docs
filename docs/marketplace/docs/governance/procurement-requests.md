---
url: https://docs.cloud.google.com/marketplace/docs/governance/procurement-requests/
title: Manage requests to procure products \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:42.214834+00:00
---

# Manage requests to procure products  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/procurement-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Manage requests to procure products Stay organized with collections  Save and categorize content based on your preferences. 

After you've [turned on Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/product-requests), your users can request that you procure products within your organization. These requests are called _procurement requests_. When a procurement request is created, you receive a notification, and can review and authorize their request.

After you approve or deny a request, Cloud Marketplace sends an email to the requester with the status of their request and any message that you included. This email doesn't include your contact information and can't be used to message you, and replies to the notification aren't forwarded to administrators.

Multiple people can request the same product. If you see multiple requests for the same product in your **Pending** tab, you must approve or deny each request to move it to the corresponding relevant tab.

## Before you begin

  * You must have the required [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/marketplace/docs/governance/product-requests#requirements) to receive procurement request notifications.

  * You must have the required [IAM permissions](https://docs.cloud.google.com/marketplace/docs/governance/product-requests#requirements) to procure products for each Cloud Billing account in your organization.


**Note:** If [Marketplace User Access Restrictions](https://docs.cloud.google.com/marketplace/docs/governance/strict-user-access) is turned on, administrators require [additional permissions](https://docs.cloud.google.com/marketplace/docs/governance/strict-user-access#required-permissions) to manage access requests.

## Review a procurement request

Accounts with the `consumerprocurement.orders.place` IAM permission for an organization can view all of that organization's procurement requests, and can complete or deny requests.

Procurement requests are associated with both a user and a project, so you can receive multiple requests for the same product.

To review a request, complete the following steps:

  1. Open the procurement request. You can access this from the email, or view all requests by opening the **Marketplace governance** page and then clicking **Manage procurement requests**.

  2. Review the details of the procurement request.




### Approve a procurement request

To approve a procurement request, follow the preceding steps to review the request, and then complete the following additional steps:

  1. From the request's **Resolve request** dialog, click **Accept request**.

  2. To go directly to the page to purchase the product, click the **Procure** button that appears.

  3. To procure the product, complete the form that appears.

  4. After you've procured the product, return to the **Resolve request** dialog to enter a message to the requester, including any information that they need to access the product or to contact an administrator.

  5. After you've entered your message, click **Send and finish**.




### Deny a procurement request

To deny a procurement request, follow the preceding steps to review the request, and then complete the following additional steps:

  1. In the **Resolve request** dialog, click **Deny request**

  2. Enter a message to the requester explaining the rationale behind your decision.

  3. Click **Deny**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
