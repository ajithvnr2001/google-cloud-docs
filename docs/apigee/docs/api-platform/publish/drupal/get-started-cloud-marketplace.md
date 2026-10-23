---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/get-started-cloud-marketplace/
title: Get started with Apigee Developer Portal Kickstart from Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:09.839980+00:00
---

# Get started with Apigee Developer Portal Kickstart from Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/get-started-cloud-marketplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Get started with Apigee Developer Portal Kickstart from Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to launch the Apigee Developer Portal Kickstart solution from Cloud Marketplace with _default_ configuration options.

In many cases, there are multiple options for portal customization to suit your scaling, security, or monitoring needs. See [ Customize the Apigee Developer Portal Kickstart solution in Cloud Marketplace](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize) for specific customization options to consider before deploying your portal.

## Before you begin

This tutorial is intended to familiarize you with the steps required for a default portal configuration. Before you deploy a portal for testing or production usage, see [ Customize the Apigee Developer Portal Kickstart solution in Cloud Marketplace](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize) for the prerequisite configuration steps needed for the following tasks: 

  * [Configure a private IP address for using CloudSQL in a VPC network](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize#vpc-service-controls)
  * [Use customer-managed encryption keys for your deployment](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize#cmek)
  * [Connect your portal to an Apigee or Apigee hybrid org](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize#connect)
  * [Configure HTTPS for testing](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize#https)
  * [Launch a production-ready portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize#production)



## Launching a new Apigee Developer Portal Kickstart 

Follow the steps below to configure and deploy the Apigee Developer Portal Kickstart solution from Cloud Marketplace: 

  1. In the Google Cloud console, go to the [ Cloud Marketplace page](https://console.cloud.google.com/marketplace) and select the **Apigee Developer Portal Kickstart** solution.
  2. Click **Launch**.
  3. Configure the **New Apigee Developer Portal deployment**. 
     1. Enter the **Deployment name**. For example, `portal-dev`. The name of your deployment: 
        * Should not exceed 10 characters.
        * Match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. This means that the first character must be a lowercase letter, and all the following characters must be hyphens, lowercase letters, or digits, except the last character, which cannot be a hyphen.
        * See Compute Engine guidelines on [ Naming conventions](https://cloud.google.com/compute/docs/naming-resources#resource-name-format) for addition details.
     2. Select the **Preferred Zone** for your deployment from the dropdown list. For more details regarding Compute Engine resources available in various zones, see [Regions and Zones](https://cloud.google.com/compute/docs/regions-zones). 
     3. Select the **Machine type** for the Compute Engine instance from the dropdown list. The default value is `1vCPU`. 
        * Optional: Click **Customize** to change the selected **Machine type** , **Cores** , and **Memory** for the Compute Engine instance.
        * See [ Creating a VM Instance with a custom machine type](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type)for more information on machine type customization options.
     4. **Create a new Service Account** or **Select an existing Service Account** for the Compute Engine instances in your deployment. The Service Account is used by Compute Engine to access other Google APIs. 
        * To create a new Service account, provide the following information: 
          * **Service account name** : This unique identifier will appear in the service account's email address that is provisioned during creation. For example, `sa-name@project-id.iam.gserviceaccount.com`.
          * **Service account ID** : The ID must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes. 
          * **Service account description** : a brief description of the service account
          * See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts) for additional details.
        * To select an existing Service Account, **Select a Service Account** from the dropdown list of available Service Accounts within your project with the correct roles.
**Note** : The existing Service Account must have the following roles: `
          * roles/storage.objectViewer
          * roles/logging.logWriter
          * roles/runtimeconfig.admin
          * roles/apigee.developerAdmin
          * roles/cloudsql.client
          * roles/monitoring.metricWriter
`
     5. Optional: Configure Boot Disk options: 
        * Select the **Boot disk type** from the dropdown list. The default value is ` Standard Persistent Disk`.
        * Select the **Boot disk size** from the dropdown list. The default value is ` 200GB`.
        * See [Storage options](https://cloud.google.com/compute/docs/disks) for a comparison of storage options and disk pricing.
     6. Optional: Configure **Networking** options: 
        * New portals are provisioned with a default IP address for connecting to the CloudSQL instance.
        * Optionally, select the checkbox to configure HTTPS on the new portal using an `nip.io` domain. [nip.io](https://nip.io/) is a third-party service that can provide a wildcard DNS for an IP address. If you wish to use `nip.io` for development and testing, you can modify the domain in the load balancer configuration prior to production use. See [Using a testing domain](https://cloud.google.com/anthos/run/docs/default-domain) for an example of the steps required. 
     7. Optional: Configure **Cloud Logging and Monitoring** : 
        * Cloud Logging and Cloud Monitoring are enabled for new Apigee Developer Portal Kickstart deployments by default.
        * To disable either Cloud service, uncheck the corresponding box.
        * See the [Cloud Logging](https://cloud.google.com/logging/docs) and [ Cloud Monitoring](https://cloud.google.com/monitoring/docs) documentation for more details on configuration options.
     8. Optional: Configure **Encryption** options: 
        * By default, the Apigee Developer Portal Kickstart uses [Google Managed Encryption Keys](https://cloud.google.com/storage/docs/encryption/default-keys) to secure access to your Cloud SQL instance.
        * To use a configured customer-managed encryption key (CMEK) to secure access to Cloud SQL, enter the **Resource Name of the Encryption key** in the text field.
     9. Click **Deploy**.

Congratulations, you have successfully deployed a Apigee Developer Portal Kickstart!

## Viewing your portal deployment

To see the details of your portal deployment: 

     1. From the Apigee Developer Portal Kickstart page, click **View Past deployments**. This will take you to the [**Deployment Manager**](https://console.cloud.google.com/dm/deployments) dashboard. 
     2. To view the details of a given portal deployment, select the desired portal deployment from the list. The detail page will recommend next steps, link to additional documentation, and provide links and IDs for provisioned Cloud services, including the following: 
        * Instance Group
        * Cloud SQL Instance
        * Filestore Instance
        * Firewall Rule
        * Load Balancer
     3. For more information on managing, updating, and deleting deployments, see the [ Deployment Manager](https://cloud.google.com/deployment-manager/docs) documentation.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this quickstart, you can [delete your deployment](https://console.cloud.google.com/dm/deployments). You can also delete the Google Cloud project used for this tutorial. 

## What's next

     * Additional options for [ Customize the Apigee Developer Portal Kickstart solution in Cloud Marketplace](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize).
     * Learn more about [Support resources](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/get-support-cloud-marketplace) for the Apigee Developer Portal Kickstart solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
