---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooter/
title: Troubleshoot using the Policy Troubleshooter \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:27.185445+00:00
---

# Troubleshoot using the Policy Troubleshooter  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/troubleshooter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Troubleshoot using the Policy Troubleshooter Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the Policy Troubleshooter to triage and analyze an end user's access.

Chrome Enterprise Premium lets you create advanced rules at the enterprise level that provide context-based application access. When multiple access rules are applied to resources, from location restrictions to device rules, it can make it difficult to understand how the policies are evaluated and why a user has or doesn't have access to the target resource. This is where triaging and analyzing a user's access is important.

The Policy Troubleshooter helps you identify why access succeeds or fails, and if required, change the policy and instruct the end user to modify their context to allow access or remove the binding to deny unexpected access. The Policy Troubleshooter is a valuable tool for organizations that need to apply multiple rules to multiple resources for different groups of users.

## Before you begin

To maximize the effectiveness of the Policy Troubleshooter, verify that you have the Security Reviewer role (`roles/iam.securityReviewer`). This lets you read all applicable Cloud IAM policies.

To troubleshoot access for a device, you must have permission to view its details. If policies associated with the target resource contain device policies, such as an access level that requires the device to be encrypted, you might not get accurate results unless the permission to retrieve the device details of the target principal is verified. Google Workspace Super Admin, Services Admin, and Mobile Admin typically have access to view device details. To allow a user who is not a Super, Service, or Mobile Admin to troubleshoot access, complete the following steps:

  1. [Create a custom Google Workspace administrator role](https://support.google.com/a/answer/2406043/create-edit-and-delete-custom-admin-roles) that contains **Services > Mobile Device Management > Manage Devices and Settings** privilege (located under **Admin Console Privileges**).
  2. Assign the role to users by using the Admin console.



To troubleshoot access to a resource given by a Google Cloud group, you must have permission to view its members. If the policies contain a group, you should have the permission to view the details of the group before opening it. Google Workspace Super Admins and Group Admins typically have access to view group membership. To allow a user who is not a Super or Group admin to troubleshoot access, complete the following steps:

  1. [Create a custom Google Workspace administrator role](https://support.google.com/a/answer/2406043/create-edit-and-delete-custom-admin-roles) that contains **Groups > Read** privilege (located under **Admin API Privileges**).
  2. Assign the role to the user. This lets the user view the membership of all groups within your domain, and more effectively troubleshoot access.



Custom Role permission is optional. If you don't have permission to view a custom role, then you might not be able to tell whether a principal has access to it from bindings with custom roles.

## Troubleshooter workflow overview

### Troubleshooting denied access

To troubleshoot denied access, you can turn on the feature for an IAP resource in the IAP settings by clicking the three dots to the right of the IAP protected application, **Settings** , and then selecting **Generate a troubleshooting URL**. To maximize the effectiveness of the Policy Troubleshooter, verify that you have the IAP Settings Admin role (`roles/iap.settingsAdmin`). This lets you retrieve and update the IAP settings of all the IAP resources.

Troubleshooting URLs are only presented on the default 403 pages, when enabled.

The Policy Troubleshooter provides a user interface where you can view the detailed evaluation results of all effective policies for the target IAP resource. When a user's access fails, the 403 page shows a troubleshooter URL. When visited, the Policy Troubleshooter shows the details of the failing bindings and the analysis of the failing access levels, if they exist in the bindings. You can also use the troubleshooter to see a detailed view of a user's access to a resource.

#### User access denied

When a user doesn't have the permission or doesn't satisfy the condition required to access an IAP resource, the user is directed to a 403 access denied error page. The 403 page includes a troubleshooting URL that can either be copied and sent manually to the application owner or security administrator, or the user can click **Send Email** in the user interface.

When a user clicks **Send Email** , an email is sent to the support email address (supportEmail) that is configured on the OAuth consent screen. For more information about configuring the OAuth consent screen, see [Programmatically creating OAuth clients for IAP](https://docs.cloud.google.com/iap/docs/programmatic-oauth-clients).

#### Troubleshooting failed access

When you receive the link for a failed access request from an end user, you can click the URL, which will open in the default browser. If you are not signed in to the Google Cloud console in your default browser, you might be redirected to another sign-in page to access the Policy Troubleshooter analysis page.

The Policy Troubleshooter analysis page provides a summarized view, an IAM policy view, and table that each show the context for a user and the device, such as principal address, device ID, the IAP resource being accessed.

The summarized view provides an aggregate view of all the relevant policy and membership findings. The IAM policy view provides a list of the effective IAM bindings` evaluation results, granted or not, together with a high level view of where the failures occurred, such as **Principal not a member and does not meet conditions**.

To further analyze the failed access, you can view **Binding details**. Within the **Binding Details** , you can see the binding components, **Role** , **Principal** , and **Condition**. The component that has sufficient permissions will note **No action required**. Components where access failed, the gaps in permissions are explicitly explained, such as **Principal Category: Please add Principal to the below groups**.

Note that in the user interface, the **Relevant bindings** section is turned on by default. The bindings listed in the **Relevant bindings** section are not a comprehensive list, but instead are the most relevant bindings that might be of interest to you when troubleshooting a specific access issue. The effective policies associated with a specific resource might contain a lot of bindings not relevant to your resource, such as a Cloud Storage permission granted at the project level. Irrelevant details are filtered out.

You can further investigate a failed **Condition** by looking into the **Access Level Explanations**. The **Access Level** details point out where the failure occurred and suggest fixes to resolve the failure. You can propagate the necessary actions back to the user or fix the policies, if necessary. For example, you can send the following action back to the user: **Request failed because the device is not corporate owned**.

#### Enabling the troubleshooting URL for your custom `Access Denied` error page

You can add the Policy Troubleshooter URL to your customer `Access Denied` error page by completing the following steps:

  1. Redirect your users to your custom page instead of the default IAP error page by completing the following step: [Setting a custom access denied error page](https://cloud.google.com/iap/docs/customizing#setting_a_custom_access_denied_error_page).
  2. Turn on the Policy Troubleshooter URL feature in the IAP settings.



After you configure the `access denied` page URL in the IAP settings, the Policy Troubleshooter URL is embedded as an **escaped** query parameter. Verify that you **unescape** the escaped query parameter before opening it. The key of the query parameter is `troubleshooting-url`.

### Proactively troubleshooting user access

You can use the Policy Troubleshooter, located in the Security panel of the Chrome Enterprise Premium landing page, to troubleshoot hypothetical events and gain insight and visibility into your security policies. For example, you can check a user's access to a particular IAP protected resource and investigate whether or not it is really required. Another example is when you make a policy change to an IAP protected resource and you want to verify that the Super Admin still has access. You can go to the Google Admin Device Console to get the device ID owned by the Super Admin, and then use the device ID in the Policy Troubleshooter to verify access.

By troubleshooting hypothetical requests, you can verify that a user has the right permissions to access an IAP resource before a real deny event occurs. You can do so by using the user email, target IAP resource, and any optional request contexts, including IP address, timestamp, device ID, or device context.

When troubleshooting hypothetical requests using the device ID, ensure the device belongs to the target principal email. You can get the Device ID from the IAP Audit Log or by going to **Google Admin Console - > Devices > Mobile and endpoints > Devices**.

When troubleshooting hypothetical requests using device context, the following attributes are supported by the troubleshooter:

  * `is_secured_with_screenlock`
  * `encryption_status`
  * `os_type`
  * `os_version`
  * `verified_chrome_os`
  * `is_admin_approved_device`
  * `is_corp_owned_device`



## Common troubleshooting scenarios

Following are some common scenarios that you might encounter when working with the Policy Troubleshooter:

  * You provide an actionable item to the end user after troubleshooting, such as instructing the end user to switch to a corporate-owned device or update the operating system.
  * You discover that you didn't assign the right permission to the end user, so you create a new binding for the target principal in the IAP interface (`roles/iap.httpsResourceAccessor`).
  * You discover that you created an access level incorrectly for the following example reasons: 
    * You created complicated nested attribute restrictions, such as corporate subnetworks, that no longer apply because employees are now working from home.
    * You applied incorrect access level parameters. For example, you specified that users can create a custom level with vendor restrictions but compared attributes with different types. For example, `device.vendors["vendorX"].data.["should_contain_boolean_value"] == "true"`. Note that the left side returns a boolean value while the right side returns a string `true`. Because of the inequivalent attributes, it is difficult to detect the error in the policy construct. The Policy Troubleshooter helps by explaining that this is evaluated to be an error with detailed partial evaluation results on both sides.



## Troubleshooter intended behavior

Troubleshooting is done on the restricted accesses using the current policies and device information with the current timestamp. Therefore, if you synced your device or changed the policies after the restricted access denial, you are not troubleshooting using the old contexts and data. You are troubleshooting using the current contexts and data.

## Tips for troubleshooting bindings

For any components (Role, Principal, Condition) of any bindings with authorization errors, grant the necessary permissions if you want to check the troubleshooting results of such bindings.

If role check fails in a binding, complete the following actions:

  * Check other bindings or create a new binding by using the IAP interface to grant the `roles/iap.httpsResourceAccessor` role to the principal with applied access levels, if necessary.
  * If it is a custom role, you can add the target permission to the custom role to grant the permission (after you fix any principal failures and any condition failures, when applicable). Note that adding permissions to an existing custom role might grant other bindings with this custom role with more permissions than needed. Don't do this unless you are aware of the scope of the custom role and the risk of your operation.
  * If it is not a custom role, check other bindings or create a new binding by using the IAP interface to grant the `roles/iap.httpsResourceAccessor` role to the principal with applied access levels, if necessary.



If role check succeeds but principal check fails, complete the following actions:

  * If the members contain a group, you can add the principal to the group to grant the permissions (after you fix any condition failures, when applicable). Note that adding principal to an existing group might grant the group more permission than needed. Don't do this unless you are aware of the scope of the group and the risk of your operation.
  * If the members don't contain a group, check other bindings or create a new binding by using the IAP interface to grant the `roles/iap.httpsResourceAccessor` to the principal with applied access levels, if necessary.



If the role and principal check succeed but the condition fails, check the troubleshooting details of each individual access level listed under the condition, if the condition only consists of access levels connected with the OR logical operator.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
