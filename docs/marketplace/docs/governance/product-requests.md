---
url: https://docs.cloud.google.com/marketplace/docs/governance/product-requests/
title: Let your users request products \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:46.952661+00:00
---

# Let your users request products  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/product-requests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Let your users request products Stay organized with collections  Save and categorize content based on your preferences. 

To let end-users in your organization request new Cloud Marketplace products for their projects, you can turn on Product Requests. This feature lets users request a product, generating one or more of the following requests:

  * **Procurement request** : If the product is both procurable, and not already procured, a procurement request is created for that product.
  * **Access request** : If Google Cloud Private Marketplace has been [turned on](https://docs.cloud.google.com/marketplace/docs/governance/enable-private-marketplace) for your project, a request to add products to the Private Marketplace is created.



When Product Requests is turned on for an Organization, users can search for products in Google Cloud Marketplace, and then click the **Request product** button to send a message to the accounts with the relevant roles for their organization. The requester can include information about the request in this message, such as a business rationale or a required plan or license. The administrators then review the request and either approve or deny the request, based on their own internal review and procurement processes.

## Required permissions for Product Requests

The following tables list the Identity and Access Management (IAM) roles and permissions that your organization's users and administrators require to use and administer Product Requests.

If you're using email groups in your organization, to ensure that you receive procurement and access request notifications, verify that your groups have mail enabled for notifications.

**Note:** If you're using Workforce Identity Federation in your Google Cloud organization, Google Cloud Marketplace doesn't send email notifications when members of your organization create procurement or access requests.

### IAM roles and permissions for requesting products

**Action** | **Permissions or Roles** | **Level at which role/permission is assigned**  
---|---|---  
Request Product | `consumerprocurement.entitlements.list` | Project, folder, or organization level  
  
### IAM Roles & Permissions for managing product requests

**Action** | **Permissions or Roles** | **Level at which role/permission is assigned**  
---|---|---  
Turn on Product Requests | Commerce Organization Governance Admin (`roles/commerceorggovernance.admin)`) AND Organization Viewer (`roles/resourcemanager.organizationViewer`) roles | Organization level  
Receive procurement request notifications | Billing Account Administrator (`roles/billing.admin`) role | Organization level  
Manage procurement requests | Organization Viewer (`roles/resourcemanager.organizationViewer`) AND either Browser (`roles/browser`) or Viewer (`roles/viewer`) roles, AND `consumerprocurement.orders.place` permission | Organization level  
Receive access request notifications | Commerce Organization Governance Admin (`roles/commerceorggovernance.admin`) role | Organization level  
Manage access requests | either Browser (`roles/browser`) or Viewer (`roles/viewer`) roles, AND Organization Viewer (`roles/resourcemanager.organizationViewer`) AND Commerce Organization Governance Admin (`roles/commerceorggovernance.admin`) roles | Organization level  
  
## Turn on Product Requests

By default, Product Requests is turned off for your organization.

To turn on Product Requests, complete the following steps:

  1. In Cloud Marketplace, click **Marketplace governance**.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  2. In **Governance settings** , click the toggle to turn on Product Requests.

  3. Optionally, you can edit the **Product request instructions** to provide guidelines about the information you need to review requests and procure products. To do this click **Edit Details** , enter your instructions and click **Save details** to finalize your changes.




## What's next

  * For information about managing your users' procurement requests, visit [Manage requests to procure products](https://docs.cloud.google.com/marketplace/docs/governance/procurement-requests).

  * For information about managing your users' access requests, visit [Manage requests to add products to your private marketplace](https://docs.cloud.google.com/marketplace/docs/governance/access-requests).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
