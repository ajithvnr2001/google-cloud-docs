---
url: https://docs.cloud.google.com/channel/docs/codelabs/setup/
title: Technical setup \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:51.079724+00:00
---

# Technical setup  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/codelabs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ Guides ](https://docs.cloud.google.com/channel/docs/overview)



Send feedback 

#  Technical setup Stay organized with collections  Save and categorize content based on your preferences. 

## Before you begin

Before starting, you need the following:

  * Super admin access to your reseller domain. For more information, see how to [access the Cloud Channel API](https://docs.cloud.google.com/channel/docs/access-api).

  * Access to the Google Cloud console and the Partner Sales Console.




## Step 1: Prepare the Partner Sales Console

Before you can use the API, you must accept the terms and conditions of the Channel Services platform.

Log in to the [Partner Sales Console](https://channelservices.cloud.google.com) at least once as an administrator of the reseller domain. The first time you sign in, you must accept the reseller terms of service, if applicable. If you accepted specific terms of service offline, this step isn't applicable to you.

You can accept additional terms of service on the [Terms page](https://accounts.google.com/AccountChooser?continue=https%3A%2F%2Fchannelservices.cloud.google.com%2Fsettings%2Fterms) of the Partner Sales Console.

**Note:** You need your Account ID, found in the Partner Sales Console Settings page, for API integration.

## Step 2: Configure your Google Cloud project

To use any Google API, you must have a Google Cloud project.

### Create a Google Cloud project

To create a project, navigate to the [Projects](https://console.cloud.google.com/project) area of your Google Cloud console and click add_box**Create Project**.

For more detailed instructions on creating a project, and for a list of best practices, see our [Creating and managing projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) guide.

Most resellers create Google Cloud projects under their main Google Cloud organization instead of under the reseller domain. Accessing data from the reseller domain is granted by setting up domain-wide delegation to let a service account access data from the reseller domain.

Give the project a descriptive name. The project ID is an arbitrary identifier that does not affect your ability to call the Cloud Channel API.

### Enable the API

Navigate to the [API Library](https://console.cloud.google.com/apis/library) section in the Google Cloud console and enable the [Cloud Channel API](https://console.cloud.google.com/apis/library/cloudchannel.googleapis.com).

### Create a service account

To create your service account, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  1. Click add_box**Create Service Account**.
  2. Enter the **Service account name** (and optional **Service account description**) then click **Create**.
  3. Click **Continue** to skip the **Grant service account access to project** option.
  4. Skip the **Grant users access to this service account** section and click **Done** to finish account creation.



After you create your account, create a service account key:

  1. In the Google Cloud console, click the email address for the service account that you created.
  2. Click **Keys**.
  3. Click **Add key** , then click **Create new key**.
  4. Click **Create**. A JSON key file is downloaded to your computer.

Make sure to store the key file securely, because it can be used to authenticate as your service account. You can move and rename this file however you would like.

  5. Click **Close**.




You can delete and create private key files from the Service accounts page.

## Step 3: Authorize the service account for the reseller domain

You need your service account's Client ID for this section. From the more_vert**Actions** menu, select **Manage details** and copy your **Unique ID**.

Go to the [Domain-wide delegation page](https://accounts.google.com/AccountChooser?continue=https%3A%2F%2Fadmin.google.com%2Fac%2Fowl%2Fdomainwidedelegation) using your reseller domain's super-admin account.

  * Click **Add new** and enter your service account's ID in the **Client ID** field.
  * Enter `https://www.googleapis.com/auth/apps.order` in the **OAuth Scopes** field.
  * Click **Authorize** to allow your service account to use the Cloud Channel API in the context of your Channel Services account.

**Note:** If you use additional APIs in your final integration, you might have more than one scope for your service account's client.

Then click **Authorize** so your service account can use the Cloud Channel API in the context of your Channel Services account.

**Note:** You might have to enable more APIs and add more scopes in other codelabs. Your final integration might have more than one scope for your service account's client.

## Next steps

Now that you have an initial technical integration, you can discover the API by reading the [Cloud Channel API documentation](https://docs.cloud.google.com/channel/docs/reference/rest).

**Note:** If you also have a Test Partner Sales Console, follow steps one through four with your test reseller domain. Make sure to create a separate project since Google APIs have per-project quotas. Sharing a project across environments might cause your test accounts to impact the quotas on your production account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
