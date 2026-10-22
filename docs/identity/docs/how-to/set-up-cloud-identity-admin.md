---
url: https://docs.cloud.google.com/identity/docs/how-to/set-up-cloud-identity-admin/
title: Quickstart: Set up Cloud Identity as a Google Cloud administrator \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:12.016203+00:00
---

# Quickstart: Set up Cloud Identity as a Google Cloud administrator  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/set-up-cloud-identity-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Cloud Identity as a Google Cloud admin

This document shows you how to set up Cloud Identity and become a Google Cloud administrator who can manage Google Cloud users and resources. Setting up Cloud Identity is one of the first steps that you'll take when creating a Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

For more information about the differences between these services, see [Compare Cloud Identity features and editions](https://docs.cloud.google.com/identity/docs/editions).

## Requirements

  * **Cloud Identity Free** : You need your company's domain name and the administrator username and password to your domain registrar to get started.
  * **Cloud Identity Premium** : You need your company's domain name to get started, or you need to purchase a domain during sign-up.
  * Cloud Identity Free and Premium provide identity management without Workspace Gmail inbox hosting. To receive system notifications (such as Google Cloud project migration invitations), the customer's domain must have an active external email service or mail forwarding configured for their administrator email address.



## Sign up for Cloud Identity Free

#### If you're a Google Workspace customer

  1. [Sign in](https://admin.google.com/) with an administrator account to the Google Admin console.

If you aren't using an administrator account, you can't access the Admin console.

  2. Go to **Billing > Buy or upgrade**.

Make sure that you have the [Billing management](https://support.google.com/a/answer/1219251#api) administrator privilege.

  3. In **Categories** , click **Cloud Identity**.

  4. In **Cloud Identity Free** , click **Get Started**.

  5. Follow the guided instructions.




#### If you're not a Google Workspace customer

  1. Go to the following sign-up page: <https://workspace.google.com/gcpidentity/signup?sku=identitybasic>
  2. Follow the guided instructions.



## Sign up for Cloud Identity Premium

#### If you're a Google Workspace customer

  1. [Sign in](https://admin.google.com/) with an administrator account to the Google Admin console.

If you aren't using an administrator account, you can't access the Admin console.

  2. Go to **Billing > Buy or upgrade**.

Make sure that you have the [Billing management](https://support.google.com/a/answer/1219251#api) administrator privilege.

  3. Click **Cloud Identity**.

  4. Next to **Cloud Identity Premium** , click **Start Free Trial**.

  5. Follow the guided instructions.




#### If you're not a Google Workspace customer

  1. Go to the following sign-up page: <https://workspace.google.com/gcpidentity/signup?sku=identitypremium>
  2. Follow the guided instructions.



## Create your Cloud Identity account and first administrator user

To create your Cloud Identity account and first administrator user using the Setup Wizard:

  1. For **About you** , enter your first and last name in the **Name** field.
  2. In **Current email address you use for work** , enter your email address.

This email address will be used as a recovery address. _It must be different_ from the address you create that you'll use as your admin account for Cloud Identity.

  3. In the **About your business** section, for **Business or organization name** , enter your company name.

  4. In the **Country/Region** list, choose the appropriate country or region.

  5. To set up your domain, click **Next**.

  6. In the **Your Cloud Identity Domain** window, add the domain that you've already purchased for your company. You'll later need to verify that you own the domain.

  7. In the **Create your Cloud Identity account** window, enter a username and password. This account is your Cloud Identity administrator account and must be different from the email address you entered in step 2. As a best practice, we recommend that you enter a username with the following format: `admin@example.com`




For more details and instructions about verifying your domain, see [Verify your domain for Cloud Identity](https://docs.cloud.google.com/identity/docs/how-to/verify-domain).

Congratulations! You successfully enabled Cloud Identity and created your first user.

## Finishing setup

After you create your Cloud Identity account and verify your domain, you're returned to the Google Cloud console. Before you continue, you'll need to accept the Cloud Identity Agreement on behalf of your organization. You're then directed to the **Identity** page.

You now have a fully functioning Cloud Identity account. But you'll also have the option to complete a few more setup steps in the console, described in this document.

**Note** : Later, you might want to return to the Google Admin console to add more users and create groups. For instructions, see [Manage users](https://support.google.com/a/topic/7555732).

## About your Cloud Identity organization

Your Cloud Identity organization is created after you finish your signup and setup steps for your Cloud Identity service. This maps a Cloud Identity account from the Admin console to Google Cloud, and is used to group all of your projects for billing and management purposes. For example, using your Cloud Identity organization you can restrict project access only to Cloud Identity users.

The super administrator who created the Google Cloud organization resource is assigned the **Organization Administrator** role, which lets them manage organization settings and assign policies at the highest level.

## Migrate projects and billing accounts and set permissions

**Important:**

  * Complete steps 1–2 from your non-administrator Google Cloud account. This account is typically a personal Gmail account.
  * Complete steps 3–6 from your Cloud Identity administrator account.



To migrate content from a previous account, follow these steps:

#### Step 1: Grant access to billing accounts

Follow these steps to migrate projects and billing accounts from accounts outside of your Cloud Identity organization to your new Cloud Identity organization. We recommend that you open this page in a separate tab to use as reference while completing the steps.

  1. Sign in to the Google Cloud account that has the existing billing account you want to connect to.
  2. Grant your organization administrator from Cloud Identity access to this billing account. 
     1. Go to the left nav and open **Billing**.
     2. Navigate to the billing account that you want to connect to.
     3. Add the Organization administrator of your Cloud Identity as a Billing administrator.



#### Step 2: Grant access to projects

You can grant access to projects one at a time or using the bulk permissions UI. Step 1 walks through the one-at-a-time method, while step 2 walks through the bulk method.

  1. Grant your organization administrator _Owner_ access to projects.  
Navigate to the **IAM and Admin** page for the projects you want to migrate, and add your organization admin's account as _Owner_.
  2. Set Bulk permissions (optional).  
Navigate to the **IAM and Admin** section and click **Manage Resources** or **All projects** from the left navigation. From the Manage Resources view, select all the projects you want to migrate and use the Identity and Access Management (IAM) panel to add your new account as _Owner_ to these projects.



#### Step 3: Sign in to your Cloud Identity account, and accept the project invitations

Sign in to your Cloud Identity account and check your email.

For the projects you're migrating, you must accept the project invitation sent by email to your new account. You must click the link in each email for each project that you're migrating.

**Important:** project invitations are sent to the MX provider that is configured for the domain. If an email host is not set up on the domain, users won't be able to receive the project invitation links required to complete migration.

#### Step 4: Go to Google Cloud, sign in with your Cloud Identity account, and remove access

  1. Remove access to the billing account.  
Navigate to the billing account you connected from your old account, and remove access for any user accounts that are not within your company's domain, including your _@gmail.com_ account.
  2. Remove access to projects. 
     1. Navigate to the **IAM and Admin** page, and click **Manage Resources**.
     2. From the **Manage Resources** page, select **No organization** from the drop-down list next to the filter control.
     3. The projects from your old account are displayed with a yellow warning icon. Select these projects and use the IAM panel to remove access for any accounts that are not within your company's domain, including your _@gmail.com_ account.



#### Step 5: Migrate projects

  1. Navigate to the **IAM and Admin** section, and click **Manage Resources**.
  2. From the Manage Resources page, click **No organization** from the drop-down list next to the filter control. The projects from your old account are displayed with a yellow warning icon.
  3. Select these projects from your old account, and click **Migrate** from the top bar, or click the icon for each project.



After the migration is finished, your projects will be moved to your company's organization. You must switch the **No organization** drop-down to your company's organization to view the projects.

#### Step 6: Set permissions

  1. Navigate to the **IAM and Admin** section, and select your organization from the top bar drop-down list. This will allow you to set IAM permissions that will affect all projects under your organization.
  2. From the IAM page, add your Admin users and grant them the appropriate roles.



For more details, see also [ Configuring permissions on Google Cloud](https://cloud.google.com/docs/permissions-overview).

## Activate a Cloud Billing account

Free trial users: After you set up Cloud Identity, [check your billable status](https://docs.cloud.google.com/free/docs/free-cloud-features#confirm-status-of-account) to verify that you have remaining free trial credits. When the [free trial offer ends](https://docs.cloud.google.com/free/docs/free-cloud-features#end), you can [activate a full, paid Cloud Billing account](https://docs.cloud.google.com/free/docs/free-cloud-features#how-to-upgrade) to continue to use Google Cloud resources that require a Cloud Billing account. To learn more about the free trial, see [Free cloud features and trial offer](https://docs.cloud.google.com/free/docs/free-cloud-features).

## Troubleshooting steps

While signing up for Cloud Identity with your domain, you might encounter one of the following error messages. Based on the message, try the following solutions.

#### "This domain is already in use."

If you receive this message when trying to sign up for Cloud Identity, it might be because:

  * You have a Google Workspace account with this domain and tried to sign up for Cloud Identity Premium from a marketing page or third party. Instead, you need to sign up for Cloud Identity Premium with this domain from the Billing section of your Google Admin console. [Learn more](https://docs.cloud.google.com/identity/docs/how-to/add-cloud-identity-licenses-to-your-organizations-googlenbspworkspace-account).
  * You have an account for Cloud Identity Free edition through Google Cloud with this domain, and tried to sign up for Cloud Identity Premium from a marketing page or third party. Instead, you need to sign up for Cloud Identity Premium with this domain from the Billing section of your Google Admin console. [Learn more](https://docs.cloud.google.com/identity/docs/how-to/upgrade-or-downgrade-cloud-identity).
  * You recently removed this domain from another Google Account. It can take 24 hours (or 7 days if you purchased your account from a third party) before you can use the domain with a new account.
  * You or someone in your organization already created a Cloud Identity or Google Workspace account with your domain. Try [resetting the administrator password](https://support.google.com/a/answer/33561). Then we'll send an email to the secondary email you provided when you signed up, with details on how to access the account.
  * You're using the domain with another Cloud Identity account you own. If so, [remove the domain](https://support.google.com/a/answer/183028) from the other account.



#### "This domain has been registered and is in the process of ownership verification."

If you receive this message when trying to sign up for Cloud Identity, it might be because:

  * You or someone in your organization already created a Cloud Identity or Google Workspace account with your domain and is in the process of domain verification (which can take up to 72 hours). Try [resetting the administrator password](https://support.google.com/a/answer/33561). Then, we'll send an email to the secondary email you provided when you signed up, with details on how to access the account.
  * You're using the domain with another Cloud Identity account you own. If so, [remove the domain](https://support.google.com/a/answer/183028) from the other account.



#### "This domain name doesn't exist yet."

You're getting this error message because the domain hasn't yet been registered with a domain host. 

If you already registered your domain name with a domain host, check that the spelling of the domain name you entered matches the registered name. Keep in mind that it can take up to 72 hours for [Whois directories](https://support.google.com/a/answer/2573637#O) to be updated with your new domain ownership.

#### "Cloud Identity does not currently support this domain name."

The domain that you're trying to sign up with isn't supported by Cloud Identity policies. Sign up with another domain name.

## What's next

  * [Verify your domain](https://docs.cloud.google.com/identity/docs/how-to/verify-domain)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
