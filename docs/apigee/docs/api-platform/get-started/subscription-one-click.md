---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/subscription-one-click/
title: Provision Apigee with one click \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:48:38.242823+00:00
---

# Provision Apigee with one click  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/subscription-one-click/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provision Apigee with one click Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can provision a new Apigee Subscription organization with just one click, using smart default configuration settings.

**Note:** This option could be disabled if your project has a CMEK [ organization policy constraint](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/using-org-policies). 

## Before you begin

Before you provision your Apigee Subscription organization: 

  1. Review and complete the steps described in these topics: 
     * [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites)
     * [Get started in the Google Cloud console](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/wizard-select-project)
  2. Ensure there is an available VPC network in the Google Cloud project you will use to provision Apigee. To view available VPC networks in your project, go to the **VPC Networks** page: 

[Go to VPC networks](https://cloud.google.com/console/networking/networks/list)

If there is no available network in your project, you may encounter an error during provisioning. For more details, see Troubleshoot one-click provisioning.




## Provision Apigee with one click

To start one-click provisioning for a new Apigee Subscription organization: 

  1. Go to the **Welcome to Apigee API management** page in the Google Cloud console. 

[Go to Apigee API Management](https://cloud.google.com/console/apigee/welcome)

  2. Click **Set up with defaults**. 

When you select this one-click option, Apigee does the following: 

     * Enables the required APIs 
       * [API hub API](https://console.cloud.google.com/apis/library/apihub.googleapis.com)
       * [Apigee API](https://console.cloud.google.com/apis/library/apigee.googleapis.com)
       * [Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)
       * [Cloud Key Management Service (KMS) API](https://console.cloud.google.com/apis/library/cloudkms.googleapis.com)
       * [Service Networking API](https://console.cloud.google.com/apis/library/servicenetworking.googleapis.com)
     * Creates the following configurable resources: 
       * **Default networking** : This resource uses the default authorized network and subnetwork in your Google Cloud project and automatically allocates IP ranges for network peering and runtime IPs.
       * **A Google-managed domain** : This includes the `nip.io` wildcard DNS service and a Google-managed SSL certificate to secure your domain.
     * Creates the following permanent resources: 
       * **Google-managed encryption key** : This resource includes encryption keys for runtime database and runtime disk encryption. **Note:** If you create this permanent resource using **Set up with defaults** for one-click provisioning, you cannot go back and change the encryption key selections. Apigee does not support updating the encryption key selections after provisioning is complete. For example, if Google-owned and Google-managed encryption keys are created using this option, you cannot change to Customer-managed encryption later.
       * **API hub** instance: A new [API hub instance](https://docs.cloud.google.com/apigee/docs/apihub/what-is-api-hub) is created in the same project and region as your Apigee organization. If you need API hub with customer-managed encryption keys, you must delete the auto-provisioned API hub instance and create a new API hub instance in the same project and region as your Apigee organization.
  3. The **Provisioning Apigee** page displays when provisioning begins. You can monitor progress and view the approximate time remaining to complete from this page. Provisioning may take up to **one hour**. 

Once the required APIs are enabled, as indicated by check_circle **Enabled** , you can leave the page. A notification will appear in the Google Cloud console when the provisioning operation completes.

  4. When provisioning completes, the **Apigee Dashboard** page displays. Congratulations! You can begin exploring Apigee!



## Troubleshoot one-click provisioning

If the resources required to provision Apigee are not available in your Google Cloud project, you may encounter an error message after clicking **Set up with defaults** on the **Welcome to Apigee API management** page, as shown below: 

![Error message during one-click provisioning](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/default-network-error.png)

You may encounter this message if: 

  * There is no available VPC network in the Google Cloud project you are using to provision Apigee.
  * Your Google Cloud organization has a policy restricting the creation of resources in the region used for Apigee provisioning. For more information, see [ Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview). 



If you encounter this error, we recommend clicking **Customize your setup** to customize the required resources created for Apigee in your project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
