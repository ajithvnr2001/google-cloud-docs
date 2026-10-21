---
url: https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription/
title: Step 2: Add people to the subscription \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:14.637523+00:00
---

# Step 2: Add people to the subscription  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Step 2: Add people to the subscription Stay organized with collections  Save and categorize content based on your preferences. 

A Data Studio Pro subscription can include specific users as well as Google Groups. You can add users when you first create the subscription or [come back and do so later](https://docs.cloud.google.com/data-studio/edit-a-pro-subscription). You can also remove users at any time.

## Before you begin

Before adding users to the Pro subscription, ensure that you have the required permissions.

### Required permissions

  * **Pro subscription management:** To add or remove people on an existing subscription, your Google Cloud user account needs the Owner (`roles/owner`) or Looker Studio Pro Manager (`roles/lookerstudio.proManager`) Identity and Access Management role on the associated Google Cloud project. For complete details on required administrative permissions, including configuring custom roles, see [Data Studio Pro roles and permissions](https://docs.cloud.google.com/data-studio/about-pro-roles-and-permissions).
  * **Google Group permissions:** To add a Google Group, you must have [permission to view group members](https://support.google.com/a/answer/166149). You don't need to be a member of the group yourself. For more information, see [Set permissions for managing members and content](https://support.google.com/a/users/answer/9886284).
  * **Add everyone option:** To select the option to add everyone in your organization's domain, you must have the [Workspace Super Admin](https://support.google.com/a/answer/2405986#super_admin) role.



### User account prerequisites and limitations

  * **Managed accounts only:** Each Pro user must be a Google Workspace or Cloud Identity user with a [Managed Google Account](https://support.google.com/work/android/answer/6371476). You can assign licenses only to managed accounts that belong to the same organization as the Google Cloud project that is associated with Data Studio Pro. You can't include users from outside your organization in the subscription, unless you enable [external organization access](https://docs.cloud.google.com/data-studio/enable-trusted-orgs). Any external users in a Google Group are excluded from the subscription. Even when you allow external domains, cross-organizational subscription assignment is restricted to individual user accounts; you can't add Google Groups that originate outside your organization to the subscription.
  * **No automatic assignment:** Existing Google Cloud project users aren't automatically added to your Pro subscription. If you have already assigned users to the Project associated with Data Studio, you must add each user or Google Group explicitly, or add everyone in your domain.
  * **Group restrictions:** Adding identity mapped groups isn't supported. Assign only standard Google Groups or individual users.

**Important note on suspended users:** Data Studio Pro licenses are provisioned automatically based on Google Group membership. If you suspend a user's Google Workspace account (for example, when an employee leaves the company), you must also remove that user from the Google Group associated with your Data Studio Pro subscription. If a suspended user remains in the Google Group, Data Studio Pro will continue to assign a license to them, and you will continue to be billed for that seat. Removing the user from the group will automatically revoke the license and update your billing count. 

## Add specific users and groups

To add individual users to the Data Studio Pro subscription, enter their email addresses. To add teams or departments, enter their Google Group aliases.

## Add everyone in your organization's domain

To buy individual Pro licenses for everyone in your organization, select **Add everyone in your organization's domain**.

Adding everyone in your domain doesn't change the [subscription model](https://docs.cloud.google.com/data-studio/pro-subscription-overview). Your Data Studio Pro subscription remains based on individual named user licenses rather than monthly active users.

## Add users from other organizations

To include users from external Google Cloud organizations or partner domains in your subscription, you must first enable the **Trusted Orgs** feature. Once your external domain allowlist is set up, you assign Pro licenses to external users right here in the exact same field by entering their individual email addresses.

If you haven't enabled external organization access yet, complete the prerequisite setup first: [Enable cross-organizational access with Trusted Orgs](https://docs.cloud.google.com/data-studio/enable-trusted-orgs).

* * *

## Troubleshoot "Enter a valid email address" error

When you assign licenses in the Google Cloud console, you might see an `Enter a valid email address` error even when you provide a valid email address for a user in your organization. This situation typically occurs if you lack sufficient `Group View Permission` in the Google Admin console.

To resolve this issue, use one of the following options:

  * **Assign licenses in Data Studio** : Assign users directly through the Data Studio interface at [datastudio.google.com](https://datastudio.google.com). In the navigation panel, select **Pro subscription** to manage license assignments.
  * **Update permissions in the Google Admin console** : Ask your Workspace administrator to grant you organization-wide permissions to view all members.
  * **Use a Google Group** : Create a Google Group for the users to whom you want to assign licenses. Ensure that you have **Viewer** permissions for that group and then assign the license to the group in the Google Cloud console.



## Related resources

  * Next: [Step 3: Buy additional Data Studio Pro licenses](https://docs.cloud.google.com/data-studio/step-3-buy-additional-pro-licenses)
  * Previous: [Step 1: Select a Google Cloud project](https://docs.cloud.google.com/data-studio/step-1-select-a-google-cloud-project)
  * [Start a new Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
