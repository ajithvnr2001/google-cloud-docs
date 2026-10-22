---
url: https://docs.cloud.google.com/compute/docs/instances/create-workload-optimized-instance/
title: Create a Google-configured instance optimized for your workload \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:56.192052+00:00
---

# Create a Google-configured instance optimized for your workload  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-workload-optimized-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a Google-configured instance optimized for your workload Stay organized with collections  Save and categorize content based on your preferences. 

You can use the Google Cloud console to get a Google-configured instance that is optimized for your specific workload. This method of instance creation removes the need for you to manually configure all of your instance properties. Google provides predefined, workload-optimized instance configurations for the following workloads:  Workload type  |  Best used for   
---|---  
Low cost  |  Use this instance for non-production workloads   
Web server  |  Use this instance to host a basic website   
Application server  |  Use this instance to run an application   
In-memory database  |  Use this instance as a database or to perform analytics   
OpenShift mode  |  Use this instance to run an OpenShift cluster node   
Windows  |  Use this instance as a Windows server instance   
SQL server  |  Use this instance as a SQL server instance   
  
## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create instances, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

You can create Google-configured instances that are optimized for your workloads only by using the Google Cloud console.

## Create a Google-configured instance optimized for your workload

When you're creating an instance by using the Google Cloud console, you can choose to create a workload-optimized instance by selecting your workload type. Google then uses a preset configuration that is optimized for that workload type. You can further customize your instance configuration before you finish creating the instance. If you wish to, you can also override any of these preset instance properties with values of your choice.

To create a Google-configured instance that is optimized for your workload, follow these steps:

  1. In the Google Cloud console, go to the **Create an instance** page.

[ Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. Click auto_awesome **Create VM from...**.

  3. In the list that appears, select a preset configuration as follows:

     * If one of the workload types in the **Presets** section suits your use case, select the preset configuration for that workload type. A window appears for that preset configuration.

     * Otherwise, to select from the full list of available preset configurations, click **See all presets...**. Then, on the **Preset VMs** page that appears, select the preset configuration for the workload type that suits your use case. A window appears for that preset configuration.

  4. Optional. To further customize your instance configuration or override any of the preset properties, do one of the following:

     * If you are on the **Create an instance** page, click **Apply preset** and then customize the instance configuration.

     * If you are on the **Preset VMs** page, click **Customize** and then customize the instance configuration.

For more information, see [Create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

  5. To finish creating your instance, click **Create** or **Create now**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
