---
url: https://docs.cloud.google.com/marketplace/docs/governance/access-requests/
title: Manage requests to add products to your private marketplace \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:20.512732+00:00
---

# Manage requests to add products to your private marketplace  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/access-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Manage requests to add products to your private marketplace Stay organized with collections  Save and categorize content based on your preferences. 

Your users can request to add Cloud Marketplace products to your organization's private marketplace, if the following are true:

  * You're using [Google Cloud Private Marketplace](https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace) to manage which products your users can view and use.

  * You've [turned on Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/product-requests).




These requests are called _access requests_. When a user creates an access request, your organization's Commerce Organization Governance Administrators get a notification, and they can review and authorize the request.

When you approve an access request, you must also select which collection to add the product to.

When you approve or deny a request, Cloud Marketplace sends an email to the requester with the status of their request and any message that you included. This email doesn't include your contact information and can't be used to message you, and replies to the notification aren't forwarded to administrators.

Multiple people can request the same product. If you see multiple requests for the same product in your **Pending** tab, you must approve or deny each request to move it to the corresponding relevant tab.

## Review an access request

Accounts with the [required roles](https://docs.cloud.google.com/marketplace/docs/governance/product-requests#requirements) for an organization can view all of that organization's access requests, and can complete or deny requests.

Access requests are associated with both a user and a project, so you can receive multiple requests for the same product.

To review a request, complete the following steps:

  1. Open the access request. You can access this from the email, or view all access requests by opening the **Marketplace governance** page and then clicking **Manage access requests**.

  2. Review the details of the access request.




### Approve an access request

To approve an access request, follow the preceding steps to review the request, and then complete the following additional steps:

  1. Click **Accept request**.

  2. From the drop-down, select which Google Cloud Private Marketplace collection you want to add the product to.

  3. In the access request, enter a message to the requester, including any information that they need to access the product or to contact an administrator.

  4. Click **Send and finish**.




### Deny an access request

To deny an access request, follow the preceding steps to review the request, and then complete the following additional steps:

  1. Click **Deny request**.

  2. In the access request, enter a message to the requester.

  3. Click **Deny**.




After you've denied an access request, users can request access to the product again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
