---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project/
title: Create your project \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:21.436263+00:00
---

# Create your project  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/creating-gcp-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Create your project Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** If you are deploying a new Python web service to Google Cloud, we recommend getting started with [Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service).

To deploy your app to App Engine, you must create a Google Cloud project and your App Engine application resources.

The Google Cloud project is a top-level container that holds your App Engine application and other Google Cloud resources.

The App Engine application is a resource that you must create to enable App Engine. The App Engine application resource defines the region in which you want to run your web service and store its related settings, credentials, and metadata. Only a single App Engine application resource can be created per Google Cloud project and the specified region cannot be changed after those resources are created.

If you already have a Google Cloud project with App Engine and the Cloud Build API enabled, you can continue to [Writing Your Web Service](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service).

## Create a Google Cloud project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Run the following `gcloud` command to enable App Engine and create the associated application resources. Note that the location you select cannot be changed later. 
         
         [gcloud app create](https://docs.cloud.google.com/sdk/gcloud/reference/app/create)

  15. Due to [changes in the default behavior for how Cloud Build uses service accounts](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates) in new projects, and [secure-by-default organization policy changes](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations), you might need to grant additional roles to your deploying service account. For more information on granting specific roles, see the [troubleshooting guide](https://docs.cloud.google.com/appengine/docs/standard/troubleshooter/deployment#default-sa-permissions).



### App Engine locations

App Engine is _regional_ , which means the infrastructure that runs your apps is located in a specific region, and Google manages it so that it is available redundantly across [all of the zones within that region](https://docs.cloud.google.com/docs/geography-and-regions).

Meeting your latency, availability, or durability requirements are primary factors for selecting the region where your apps are run. You can generally select the region nearest to your app's users, but you should consider [the locations where App Engine is available](https://cloud.google.com/about/locations/#region) as well as the [locations](https://cloud.google.com/about/locations/#region) of the other Google Cloud products and services that your app uses. Using services across multiple locations can affect your app's latency as well as its [pricing](https://cloud.google.com/appengine/pricing).

You cannot change an app's region after you set it.

**Note:** Two locations, which are called `europe-west` and `us-central` in App Engine commands and in the Google Cloud console, are called `europe-west1` and `us-central1`, respectively, elsewhere in Google documentation.

If you already created an App Engine application, you can view its region by doing one of the following:

  * Run the `gcloud app describe` command.

  * Open the [App Engine Dashboard in the Google Cloud console](https://console.cloud.google.com/appengine). The region appears near the top of the page.




OK

## Next steps

Now that your Google Cloud project is set up, you're ready to write a basic web service.

[ Next Write your web service  arrow_forward  ](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/writing-web-service)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
