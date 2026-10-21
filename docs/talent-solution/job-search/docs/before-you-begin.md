---
url: https://docs.cloud.google.com/talent-solution/job-search/docs/before-you-begin/
title: Before You Begin \u00a0|\u00a0 Job Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:58.670071+00:00
---

# Before You Begin  |  Job Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/job-search/docs/before-you-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Job Search ](https://docs.cloud.google.com/talent-solution/job-search/docs)
  * [ Guides ](https://docs.cloud.google.com/talent-solution/job-search/docs/basics)



Send feedback 

#  Before You Begin Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Before you can begin using Cloud Talent Solution (CTS), you must enable the API in the Google Cloud Platform (GCP) Console. The steps below walk you through the following actions:

  * Enable CTS on a GCP project. 
    1. Make sure billing is enabled for CTS.
    2. Accept the Data Logging Terms & Conditions.
    3. Create and/or assign one or more service accounts to Cloud Talent Solution.
    4. Download a service account credential key.
  * Set your authentication environment variable.



## GCP Console set-up

  1. Go to the [GCP Console](http://console.cloud.google.com). Navigate to the drop-down menu at the top of the page and choose the GCP project that you'd like to associate with Cloud Talent Solution. If you have previously created one or more projects, they will appear in a list in the pop-up menu. You can either choose a pre-existing project (a check mark will appear next to the project you select) or create a new project by clicking **NEW PROJECT**. For more details on creating a GCP project, please see the [documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/newproject.png)

  2. If you create a new project, you will be prompted to link a billing account to this project. If you are using a pre-existing project, make sure that you have billing enabled. You can access the project's billing information at any time by going to the main navigation menu (the hamburger icon in the upper left corner) and clicking the **Billing** option:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/billing.png)

**Note:** You must enable billing to use Cloud Talent Solution, however you will not be charged unless you exceed the free quota of 1-10,000 API calls per month. See the [pricing](https://cloud.google.com/talent-solution/pricing) page for more details.
  3. Once you have selected a GCP project and linked it to a billing account, you can enable the Cloud Talent Solution API. Go to the main navigation menu and scroll down to the **Artificial Intelligence** section. Click on **Talent Solution** and choose **Overview** from the menu that pops up:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/overview.png)

  4. If you would first like to try the API without linking it to your project, you can choose the **TRY THIS API** option. See the [Job Search API Explorer](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-api-explorer) documentation for more information on using this feature. To enable the Cloud Talent Solution API for use with your GCP project, click **ENABLE** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/enable.png)

  5. The data logging page appears. You must accept the terms & conditions to have full access to CTS features. If you choose not to accept these terms, you'll only be able to use deletion API requests. Click **ENABLE** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/datalogging.png)

  6. You are now prompted to link one or more service accounts to the CTS API. If you are using a project that already has service accounts associated with it, they will appear in a list on this page. Click **CONNECT** next to the account(s) that you want to link to the CTS API. Once you have done this, you can skip ahead to step 8 to make sure that you've downloaded a JSON or P12 credential for that account.

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/serviceaccounts.png)

If your project does not yet have any service accounts, you are prompted to create one. Type a name of your choosing into the **Service account name** box. Your input is automatically populated in the **Service account ID** box. The **Service account description** box is optional but recommended if you plan on associating multiple service accounts with your project. Enter a brief description of the service account into this box, then click **CREATE**.

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/newaccount.png)

  7. The next page allows you to assign a role to your new service account. See the CTS [IAM permissions](https://docs.cloud.google.com/talent-solution/docs/iam) page for full details on the available roles and the permissions allowed to each. Click on the drop-down **Select a role** menu and scroll down to **Cloud Talent Solution**. You can choose a role for this service account from the options in the right-hand column:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/accessroles2.png)

  8. The next page gives you the option to complete several tasks. These are not required but highly recommended. You can grant individual users access to the service account you just created by entering their email addresses. You can also create a private key for the service account. You must use a private key during the [authentication process](https://docs.cloud.google.com/talent-solution/job-search/docs/before-you-begin#set_up_your_environment_variables) when you use the API. If you choose not take these actions now, you can generate a key and add/change individual user information at any time by accessing the service account through the **IAM** option in the main navigation menu.

Click **CREATE KEY** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/createkey.png)

Choose your preferred format from the pop-up menu and click **CREATE** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/createkey2.png)

A new JSON or P12 credential file is automatically downloaded. Store this file in a specific location and make a note of the file path. You will need to point the GOOGLE_APPLICATION_CREDENTIALS environment variable to this file when you go through the [authentication process](https://docs.cloud.google.com/talent-solution/job-search/docs/before-you-begin#set_up_your_environment_variables). This is an essential step for authenticating requests to Cloud Talent Solution.

Once your credential file has downloaded, click **DONE** :

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/createkey3.png)

  9. Your service account now appears on the **Connect service accounts** page. Click **CONNECT** to link it to the CTS API:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/serviceaccounts.png)

  10. The account is now connected, and you're now ready to begin integrating Cloud Talent Solution into your system:

![](https://docs.cloud.google.com/static/talent-solution/job-search/docs/images/welcome-to-cts-2.png)




## Set your authentication environment variable

For more information, see the [GCP authentication documentation](https://docs.cloud.google.com/docs/authentication/production).

## What's next

Install a [client library](https://docs.cloud.google.com/talent-solution/job-search/docs/libraries) or see the [create jobs and companies quickstart](https://docs.cloud.google.com/talent-solution/job-search/docs/quickstart-jobs-and-companies) to begin making API calls.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
