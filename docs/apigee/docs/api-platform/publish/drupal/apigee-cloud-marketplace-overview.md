---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-overview/
title: Deploy a Drupal-based developer portal for Apigee from Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:01:39.189467+00:00
---

# Deploy a Drupal-based developer portal for Apigee from Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Deploy a Drupal-based developer portal for Apigee from Cloud Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**CAUTION: Deployment disruption for Apigee Drupal Portal via Cloud Marketplace**

We are transitioning the Apigee Drupal Portal Marketplace solution to use Infrastructure Manager instead of Cloud Deployment Manager. During this transition period, some deployment and management functionalities might be unavailable.

See the [Known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#495305258) for more information.

Customers who wish to deploy the open source Apigee Developer Portal Kickstart to their own Google Cloud project can use this click-to-deploy solution available through [ Google Cloud Marketplace](https://console.cloud.google.com/marketplace). The Google cloud project-based solution deploys a Drupal-based developer portal profile that can be used with your Apigee organizations to publish your API documentation and API products. The customer-managed [Drupal 9](https://www.drupal.org/about/9) profile leverages [ Apigee's open source Drupal modules](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/open-source-drupal-8) in conjunction with Google Cloud's hosting capabilities. 

## Drupal-based portal for Apigee with Cloud security

Apigee customers using VPC Service Controls have the option to host their developer portal on Google Cloud from within their own Google Cloud project. Publish your APIs securely by deploying a portal within your project's VPC Service Controls perimeter and integrate with Apigee using Apigee's open source Drupal modules. The Apigee Developer Portal Kickstart available in Cloud Marketplace simplifies this process using click-through configuration and bundled deployments. 

**NOTE** : Customers who do not require VPC Service Controls may want to consider leveraging a Drupal hosting partner to reduce their operational overhead. This solution will provision the Google Cloud components necessary to deploy a Drupal-based developer portal using Apigee Kickstart. This is a self-managed solution, and customers are responsible for capacity planning, maintaining Drupal module updates, and other operational tasks. See [ Choosing a hosting provider](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/open-source-drupal-8#choose_your_hosting_provider) for Apigee-recommended options.

## Key Benefits

The Apigee Developer Portal Kickstart solution in Cloud Marketplace: 

  * Simplifies installing and running a Drupal-based developer portal on Google Cloud.
  * Can be configured to work within a VPC Service Controls perimeter.
  * Leverages Cloud services and Drupal open source communities to extend developer portal functionality.
  * Supports self-service compliance options for FedRAMP, PCI, or HIPAA.



## Cloud services architecture

Below is a high level diagram of the Cloud services components involved in the Apigee Developer Portal Kickstart:

![high level architecture diagram of the portal solution](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/drupal-based-developer-portal-diagram.png)

## Configuration options

The click-to-deploy template streamlines custom configuration of your portal. Update your configuration after launch with [ Deployment Manager](https://console.cloud.google.com/dm/deployments), or using the [ Cloud Service dashboard](https://console.cloud.google.com/home/dashboard).

Configure the following available options for your Drupal-based portal: 

**Zone** | Choose the deployment region for the portal's Compute Engine instances.   
---|---  
**Machine Type** | Select the machine type for the portal's Compute Engine instances.   
**Service Account** | Use an existing service account or create a new service account.   
**Boot Disk Type** | Specify the storage type of the portal's Compute Engine instances.   
**Boot Disk Size** | Specify the storage size of the portal's Compute Engine instances.   
**Network** | Optionally configure HTTPS with external certificate provider [nip.io](https://nip.io/).   
**Logging and Monitoring** | Enable or disable Cloud Logging and Cloud Monitoring.   
**Encryption** | Choose Google-owned and Google-managed encryption keys or CMEK for Cloud SQL instances.   
  
## Technical specifications

The Apigee Developer Portal Kickstart runs on [Compute Engine](https://cloud.google.com/compute/docs) and utilizes these third-party services and tools: 

  * [Drupal 9](https://www.drupal.org/about/9)
  * [Debian 12](https://www.debian.org/)
  * [PHP 7 (OS default, 7.3+)](https://www.php.net/downloads)
  * [NGINX 1.14.2](https://www.nginx.com/)
  * [MySQL-Client 1.0.5](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-overview/)
  * [Composer](https://getcomposer.org/)
  * [Drush](https://www.drush.org/latest/)
  * [Apigee Kickstart Composer](https://www.drupal.org/project/apigee_devportal_kickstart)

## What's next

    * Walk through deployment of [ Apigee Developer Portal Kickstart from Cloud Marketplace](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/get-started-cloud-marketplace).
    * Learn more about [ Customize the Apigee Developer Portal Kickstart solution in Cloud Marketplace](https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/apigee-cloud-marketplace-customize).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
