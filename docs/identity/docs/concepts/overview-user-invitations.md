---
url: https://docs.cloud.google.com/identity/docs/concepts/overview-user-invitations/
title: User Invitation API overview \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:19.596334+00:00
---

# User Invitation API overview  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/concepts/overview-user-invitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# User Invitation API overview

The Cloud Identity User Invitation API allows you to identify and manage unmanaged accounts as part of onboarding users to your Google Workspace or Cloud Identity domain.

**Beta**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Unmanaged accounts are defined by the following criteria:

  * the email address is a consumer account and it's the primary email address of the account, and
  * the domain of the email address matches an existing verified Google Workspace or Cloud Identity domain



These accounts generally exist because one of the customer's users has signed up for consumer Google services using their work or educational email address. When the customer then signs up for Google Workspace or Cloud Identity and provisions a user account with the same primary email address as an existing unmanaged account, that unmanaged account becomes conflicted and needs to be resolved.

The User Invitation API makes key resolution tasks automatable:

  * Determine if a given email address is eligible to join the customer's domain (must meet both criteria)
  * Send ad-hoc or batch email invitations to eligible email addresses so they can join the customer's domain
  * Retrieve a list of unmanaged accounts, filterable by their invitation state. All unmanaged accounts on the customer's domain are treated as unsent user invitations (`state==NOT_YET_SENT`) until they are sent.
  * Look up a specific invitation by email address
  * Cancel already-sent invitations



The user invitation flow allows both the end user and the administrator to ensure that any data created using the consumer account is managed by the correct entity:

  * If the end user has business-related data under the consumer account and accepts the invitation, the administrator can take ownership and manage the data according to the customer's policies.
  * If the end user's data is not business-related and they decline, the invitation gives the user notice that they may need to rename the email address later if the admin creates a new Google account for them. The administrator can create a new managed account and evict the primary email address of the consumer account, creating the conflict. The end user will then be asked to rename their email address to another email address every time they log in to their personal Google account.



## Next steps

Here are a few next steps you might take:

  * To set up the API, refer to [Setting up the User Invitation API](https://docs.cloud.google.com/identity/docs/how-to/setup-user-invitations).
  * To understand how account conflict resolution works in the Admin Console, read [Find and manage existing accounts](https://support.google.com/a/answer/6178640) in the Google Admin Help Center.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
