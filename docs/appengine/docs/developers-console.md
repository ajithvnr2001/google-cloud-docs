---
url: https://docs.cloud.google.com/appengine/docs/developers-console/
title: Setting up your Google Cloud project for App Engine \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:23:17.524519+00:00
---

# Setting up your Google Cloud project for App Engine  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/developers-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Setting up your Google Cloud project for App Engine Stay organized with collections  Save and categorize content based on your preferences. 

A Google Cloud project contains your App Engine application as well as other Google Cloud resources.

You can perform all of your administrative tasks from the Google Cloud CLI and the App Engine Admin API, including the common tasks covered in this topic. 

Before you can [deploy your apps](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app) to the App Engine standard environment, you typically need to create or set up the following:

  1. A Google Cloud project
  2. An App Engine application
  3. A billing account



## Creating a project and application

You can select or create a new Google Cloud project and App Engine application to create and manage a collection of settings, credentials, and your app's metadata. App Engine requires all projects to enable billing, but you will only be charged if a project exceeds its [free quota](https://docs.cloud.google.com/appengine/docs/standard/quotas).

Only the [Owner role](https://docs.cloud.google.com/appengine/docs/standard/access-control) has privileges to create an App Engine application in a Google Cloud project and that application must exist before any other account can perform tasks on that application. For example, the App Engine application must be created before an account with the App Engine Deployer role can deploy an app using a service account.

**Important:** Each Google Cloud project can contain only a single App Engine application, and once created you cannot change the [location](https://docs.cloud.google.com/appengine/docs/standard/locations) of your App Engine application.

### gcloud

After installing [Google Cloud CLI](https://docs.cloud.google.com/appengine/docs/standard/setting-up-environment), an account with the Google Cloud project Owner role can run the following `gcloud` commands to create a Google Cloud project and App Engine application:

  1. Run the following command to create a Google Cloud project:
         
         [gcloud projects create](https://docs.cloud.google.com/sdk/gcloud/reference/projects/create) PROJECT_ID

Replace PROJECT_ID with the Google Cloud project ID.

  2. Run the following command to select a region and create an App Engine application:
         
         [gcloud app create](https://docs.cloud.google.com/sdk/gcloud/reference/app/create)

More information about App Engine locations _help_outline_

  3. Enable billing in the Billing page of the Google Cloud console, see Enabling billing for details.

**Tips:**
     * If you deploy your apps with the [`gcloud app deploy` ](https://docs.cloud.google.com/sdk/gcloud/reference/app/deploy) command, the gcloud CLI will ensure that your Google Cloud project includes an App Engine application and prompt you to select a region when needed.
     * To check if an App Engine application exists in your Google Cloud project, you can run the [ `gcloud app describe`](https://docs.cloud.google.com/sdk/gcloud/reference/app/describe) command. 



### API

To programmatically create a Google Cloud project and App Engine application, you use both the Cloud Resource Manager API and App Engine Admin API:

  1. To create a Google Cloud project, see [Creating a New Project](https://docs.cloud.google.com/resource-manager/docs/creating-project).

  2. To create an App Engine application, see [Creating App Engine Applications](https://docs.cloud.google.com/appengine/docs/admin-api/creating-an-application).

  3. Enable billing in the Billing page of the Google Cloud console, see Enabling billing for details.




### Console

**Note:** This is not applicable to Python.

To create a Google Cloud project and App Engine application with billing enabled:

  1. Go to the App Engine page:

[Go to App Engine](https://console.cloud.google.com/projectselector/appengine/create?st=true)

  2. Select or create a Google Cloud project.

  3. In the **Create App** page, select a region, service account, and enable billing:

     1. Select a region to specify where you want to your App Engine application located.  More information about App Engine locations _help_outline_
     2. Select a [service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts) for your app from **Identity and API access**. 
     3. Select or create a billing account to enable billing in your project.



After the App Engine application is created in your project, the **Dashboard** page opens.

### App Engine Locations

App Engine is _regional_ , which means the infrastructure that runs your apps is located in a specific region, and Google manages it so that it is available redundantly across [all of the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your apps are run. You can generally select the region nearest to your app's users, but you should consider [the locations where App Engine is available](https://cloud.google.com/about/locations/#region) as well as the [locations](https://cloud.google.com/about/locations/#region) of the other Google Cloud products and services that your app uses. Using services across multiple locations can affect your app's latency as well as its [pricing](https://cloud.google.com/appengine/pricing).

You cannot change an app's region after you set it.

**Note:** Two locations, which are called `europe-west` and `us-central` in App Engine commands and in the Google Cloud console, are called `europe-west1` and `us-central1`, respectively, elsewhere in Google documentation.

If you already created an App Engine application, you can view its region by doing one of the following:

  * Run the `gcloud app describe` command.

  * Open the [App Engine Dashboard in the Google Cloud console](https://console.cloud.google.com/appengine). The region appears near the top of the page.




OK

## Enabling billing

To deploy your apps, you must enable billing. Your account will not be charged if you stay within your [free quota](https://docs.cloud.google.com/appengine/docs/standard/quotas). If your application needs resources that exceed the free quota, you will be charged for the additional usage.

If you have a billing account when you create a Google Cloud project, then billing is automatically enabled on that project.

To enable billing on a Google Cloud project:

  1. In the Google Cloud console, go to the Billing page:

[Go to Billing](https://console.cloud.google.com/projectselector/billing)

  2. Select or create a Google Cloud project.

  3. Depending on if a billing account exists or if the selected Google Cloud project is associated with an account, the Billing page displays one of the following:

     * If billing is already enabled for the selected Google Cloud project, then the details about the billing account are listed.

     * If no billing account exists, you are prompted to create a billing account and associate it with the selected Google Cloud project.

     * If a billing account exists, you are prompted to enable billing if the selected Google Cloud project is not already associated with a billing account. You can also click **Cancel** and then click **Create account** to create and associate a new billing account.




After you enable billing, there is no limit to the amount that you might be charged. To gain more control over your application's costs, you can create a budget and set alerts.

## Managing billing

Use the Billing page to manage your billing accounts:

  1. Go to the Billing page in the Google Cloud console:

[Go to Billing](https://console.cloud.google.com/billing)

  2. Select the account that you want to manage and then navigate to the corresponding page to perform the following management tasks:

     * See an overview of your billing account, make payments, and add billing account administrators from the **Overview** page.
     * Create budgets and alerts on the **Budgets & alerts** page.
     * View your transaction history and download invoices from the **Transactions** page.
     * Export your billing data to a BigQuery Dataset from the **Billing export** page.
     * Configure your payment account and contacts on the **Payment settings** page.
     * Set the method of payment on the **Payment method** page.



For more information about billing, see the [Pricing](https://cloud.google.com/appengine/pricing#managing) page.

## Creating budgets and setting alerts

You can create a budget for a Google Cloud project to avoid surprises on your bill and monitor all of your Google Cloud charges from one place. With a budget, you can create alerts that send emails to your billing administrators when charges exceed a certain amount.

To create a budget and set alerts in a Google Cloud project:

  1. In the Google Cloud console, go to the Billing page:

[Go to Billing](https://console.cloud.google.com/billing)

  2. Click the billing account for which you want to create a budget.

  3. Click **Budgets & alerts** and then **Create budget** to begin creating a budget for your Google Cloud project.

  4. Define your budget in the **Set budget** section and then specify the percentages for which you want to receive email alerts in the following **Set budget alerts** section.

  5. Click **Save** to set the budget and enable alerts for your Google Cloud project. If you have multiple Google Cloud projects, you must individually set budgets and alerts in each project.




## Setting project ID for a project

You can specify the project ID in a few different ways:

  * By using `gcloud init` when you install the Google Cloud CLI. To view the default project ID of the gcloud CLI, run `gcloud config list`.
  * By using the `gcloud config set project [YOUR_PROJECT_ID]` command to set the default project ID of the gcloud CLI.
  * By using the `--project` flag when you deploy your app, for example: `gcloud app deploy --project [YOUR_PROJECT_ID]`



## Disabling an application

Disable an App Engine application to stop your app from running instances and serving requests. No data loss will occur when you disable your app, nor will any configuration settings change. Simply re-enable your App Engine application to startup instances and continue serving the traffic to your app.

Your app's resources in both the standard and flexible environment are disabled and therefore, won't incur charges. However, billing charges can still occur for the other services in your Google Cloud project, for example you can still incur storage charges for your stored data.

If your app is actively processing a request, it will continue to complete that task and can take up to an hour before your app is completely disabled.

To disable an App Engine application:

  1. Go to the Application settings page:

[Go to Application settings](https://console.cloud.google.com/appengine/settings)

  2. Click **Disable application** and then follow the prompts.




When you want your app to continue serving requests, enable the App Engine application by returning to the same _Application settings_ page and then clicking **Enable application**.

Disabling your application stops all serving requests, but your data and state are retained. You will still be billed for applicable charges already incurred or charges for other services running in your project, such as Cloud SQL. To release all the resources used within the project, shut down your project.

## Shutting down a project

You can disable billing and release all the Google Cloud resources that are being used in your Google Cloud project by shutting down that project.

### gcloud

After installing the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), you run the following `gcloud` command to shut down a Google Cloud project:
    
    
    [gcloud projects delete](https://docs.cloud.google.com/sdk/gcloud/reference/projects/delete) PROJECT_ID

Replace PROJECT_ID with the Google Cloud project ID.

### API

To programmatically shut down your Google Cloud project, see [Shutting Down a Project](https://docs.cloud.google.com/resource-manager/docs/shutting-down-projects) in the Cloud Resource Manager API.

### Console

To shut down a Google Cloud project using the Google Cloud console:

  1. Go to the Projects page:

[Go to Projects](https://console.cloud.google.com/iam-admin/projects)

  2. Select the Google Cloud project that you want to shut down, then click _delete_.




For more information about managing your Google Cloud projects, see [Cloud Resource Manager: creating, shutting down, and restoring projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
