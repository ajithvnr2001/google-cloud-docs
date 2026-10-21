---
url: https://docs.cloud.google.com/data-studio/invite-others-to-your-reports/
title: Invite others to your reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:48:44.814945+00:00
---

# Invite others to your reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/invite-others-to-your-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Invite others to your reports Stay organized with collections  Save and categorize content based on your preferences. 

Share your reports with other people by sending them an email invitation to visit Data Studio. You can invite specific people or Google Groups. You can also share more broadly by letting anyone who has the link access your Data Studio reports.

**Note:** Google Workspace and Cloud Identity administrators can control how users in their organization share Data Studio assets. [Learn more about setting sharing permissions](https://support.google.com/a/answer/9699595). This page covers sharing reports so that users can view or edit them by using Data Studio.

## Organizational sharing policies

**Data Studio Pro feature**

The features and functionality described in this page are available to Data Studio Pro users.

[Get Data Studio Pro.](https://docs.cloud.google.com/data-studio/about-pro)

Google Workspace and Cloud Identity administrators can use policies to restrict how users in their organization share Data Studio assets. For assets located in a team workspace or folder, Data Studio may use a _Policy User_ to check for and enforce these sharing policies.

### How Policy Users work

If an asset is located in a team workspace or folder, a Policy User may be designated for that asset. Data Studio uses the Policy User's account to determine which organizational sharing policies apply.

These policies may restrict sharing options or disable certain features for that asset.

When a user moves an asset into a team workspace or folder, that user becomes the Policy User for that asset. If the asset is moved out of all team workspaces and folders, the Policy User designation is removed.

### Designate yourself as the Policy User for an asset

If you are an owner of the asset but not the Policy User, you can make yourself the Policy User by following these steps:

  1. Navigate to the asset.
  2. Click person_add **Share**.
  3. Click the **Settings** gear icon to open the **Advanced Sharing Settings** modal.
  4. In the **Advanced Sharing Settings** modal, click **Make me policy user**.



## How to share a report

To share a report, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. View or edit the report that you want to share.
  3. Click person_add **Share**. The **Share with people and groups** dialog appears.

**Tip:** Alternatively, you can [select a button to invite users](https://docs.cloud.google.com/data-studio/add-buttons#report_actions) to view or collaborate, if available.

To share from the **Reports** or **Data sources** home page, locate the asset you want to share. Click the 3-dot **More** icon more_vert and then click **Share**.

## How sharing reports works

When you share reports, consider the following scenarios:

  * No login is required for a user to view a report that is shared with public link sharing.
  * A Google login **is** required for a user to view or edit a report that's been shared using their email address or Google Group.
  * Sharing a report with embedded data sources lets other editors use and edit those data sources in that report.
  * Sharing a report doesn't automatically share any reusable data sources that are added to that report. 
    * To learn how to share a reusable data source, see [Share reusable data sources](https://docs.cloud.google.com/data-studio/share-reusable-data-sources).
    * Sharing a report's reusable data sources is NOT required to let others view or edit the report.
  * To share a report, you must have the Owner or Editor role for the report.



## Share with specific users and groups

To share with specific users or groups, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. View or edit the report that you want to share.
  3. Click person_add **Share**. The **Share with people and groups** dialog appears.
  4. Under **Add people** , enter the names or email addresses of the people with whom you want to share. You can also share with [Google Groups](https://groups.google.com/).
  5. Select the [access permission](https://docs.cloud.google.com/data-studio/roles-and-permissions) for the users and groups whom you've specified:

     * **Can edit** : Users can edit the asset, create and edit schedules and alerts, and share the asset with others.

     * **Can view** : Users can see the asset but can't edit or share it with others.

> **Data Studio Pro feature**
> 
> If the report is a Data Studio Pro report, and you are a Data Studio Pro user, you can assign the **Can create schedules** permission to users and groups who have a [**Viewer** role](https://docs.cloud.google.com/data-studio/roles-and-permissions), even if those users are not Data StudioPro users. This permission allows those users to create and edit schedules on the report.
> 
> If you cancel Data Studio Pro, those users will retain the **Can create schedules** permission, but you will not be able to assign the **Can create schedules** permission to any other users.
> 
> [Learn more about Data Studio Pro](https://docs.cloud.google.com/data-studio/about-pro)

  6. To set different permissions for different users, use the role drop-down menu next to their name.

  7. By default, people whom you invite receive an email with a link to the asset that you're sharing. To share without sending an email, clear the **Notify people** checkbox.

  8. Click **Send**.




> ### Using Looker Studio in your organization?
> 
> If your organization uses Google Workspace or Google Cloud Identity to manage Data Studio, your administrator may restrict sharing of Data Studio and Data Studio Pro content to other users within your organization. If that's the case, you'll see an error message if you try to share externally. You may also no longer see the public link-sharing option.

## Share with non-Google Accounts

To directly invite people to access your report, they must have a Google Account. To share with non-Google Accounts, you have several options:

  1. Ask the person you're sharing with if they have a Google Account that you can share with. This could be one of two account types: 
     * A personal account that ends in `@gmail.com`
     * A work or school account that they use for Google products like Gmail, Drive, Docs, Sheets, or Slides
  2. If the person doesn't have a Google Account, they'll need to sign up for one before you can share the report with them.
  3. To help them sign up, send them this link: <https://accounts.google.com/signupwithoutgmail>
  4. Use another sharing method, such as link sharing or [emailing a PDF](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery).

**Note:** Google Accounts don't have to use a gmail.com address. You can [associate any existing email address with a Google Account](https://help.google.com/accounts/answer/176347).

## Public link sharing

Link sharing lets you distribute your reports more widely than by directly inviting individual people or groups. For example, you can turn link sharing on to share Data Studio reports with non-Google Accounts; include links in emails, blogs, or social posts; or embed links on your website.

**Important:** When you share a report using a public link, any embedded data sources within that report will also be accessible to anyone who has the link. To prevent viewers from accessing the data source, you should make the data source reusable instead of embedded.

### Get a shareable link

To get a shareable link, follow these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. View or edit the report that you want to share.
  3. Click person_add **Share**. The **Share with people and groups** dialog appears.
  4. Under **Link settings** , use the drop-down menu to select the link-sharing option that best meets your needs.
  5. Click **Copy link**.



#### Link-sharing options

If you are a standard user of Data Studio, you have the following link-sharing options:

  * **Anyone on the Internet can find and view**
  * **Anyone on the Internet can find and edit**
  * **Anyone with the link can view**
  * **Anyone with the link can edit**
  * **Off - Only specific people can access**



### Google Workspace link-sharing options

If you are a Google Workspace user, your link-sharing options may be restricted to users who are in your domain.

## Who gets access requests?

When a user tries to view a report that has not been shared with them, they will see a page that tells them that they can't access the report. The user can click **Request Access** on that page to send an email to the following Data Studio roles on that report:

  * For reports in the no-cost version of Data Studio, or Data Studio Pro reports in a user's Sandbox location, the request is sent to the report Owner.
  * For reports in a Data Studio Pro team workspace, the request is sent to **all** Managers of that workspace.



## Troubleshooting

This section provides guidance on common issues that you may encounter when sharing Data Studio assets.

### 500 Internal error when sharing Workspace assets

If you encounter a 500 "Internal error encountered" message when attempting to share Data Studio Pro assets located within a Workspace with users outside of your organization, this may be due to your organization's "Domain restricted sharing" policy.

Data Studio Pro assets in a Workspace are subject to your organization's sharing policies. If domain-restricted sharing is enforced, you may be prevented from sharing assets with external users, even if you are part of a group that has an exception for external sharing on standard assets.

To share Data Studio Pro Workspace assets externally when domain-restricted sharing is enforced, try one of the following workarounds:

  * **Temporarily modify the organization policy** : Ask your administrator to temporarily remove the organization policy containing the domain restriction constraint, grant access to the external users, and then re-apply the organization policy.
  * **Grant access to a Google Group** : 
    1. Create a Google Group within your organization's domain.
    2. Ask your Google Workspace administrator to turn off domain restriction for that group.
    3. Add the external user or service account to this Google Group.
    4. Share the Data Studio Pro asset with the Google Group.



## Limits of sharing

You can share Data Studio and Data Studio Pro assets with a maximum of 1,500 _principals_. (Principals include individual email addresses and Google Groups.)

This limit comes from [Identity and Access Management (IAM) quotas and limits](https://cloud.google.com/iam/quotas#limits).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
