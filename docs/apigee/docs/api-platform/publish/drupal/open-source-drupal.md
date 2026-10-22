---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/open-source-drupal/
title: Build your portal using Drupal 10 \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:14.056965+00:00
---

# Build your portal using Drupal 10  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/open-source-drupal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Build your portal using Drupal 10 Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

For those who want more control over the experience provided by the [developer portals integrated into Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal), Drupal 10 provides a powerful open-source, enterprise-level content management system (CMS). Using Apigee's modules for Drupal 10, you can build a fully customized developer portal with greater flexibility and control over the developer experience. Because the Drupal 10 projects and these modules are open-source, you can extend and contribute to their development and leverage the knowledge of the Apigee and Drupal communities.

## Get up and running quickly with Apigee Kickstart

The fastest way to get a developer portal site up and running with Apigee is to use the Apigee Developer Portal Kickstart. Apigee Developer Portal Kickstart is a Drupal distribution that enables you to quickly evaluate using Drupal 10 to create an Apigee developer portal. The Kickstart bundles together all of the open source Apigee Drupal modules and libraries that you need to create a portal, configure a connection to Apigee or hybrid, showcase your API products, and publish your API reference documentation.

### Get Started

Instructions for installing the Kickstart distribution can be found on Drupal.org at [Apigee Developer Portal Kickstart](https://www.drupal.org/docs/8/modules/apigee-developer-portal-kickstart). The Kickstart installer will prompt you for all the information needed to install Drupal 10 core, configure your connection to Apigee, and get your site up and running with a customizable theme. The Kickstart also includes preconfigured Drupal page entities for your developer portal homepage, API catalog page, and **Get Started** page. Modules for FAQs, Blogs and Forums to build your developer community are also included.

### Customize your developer portal

The Kickstart distribution includes a customizable home page, **Get Started** page, and API catalog page. Each of these pages can be modified to reflect your company's brand, logo, and customized developer experience.

  * To customize the logo and color scheme of your developer portal, see [Customize your developer portal](https://www.drupal.org/docs/8/modules/apigee-developer-portal-kickstart/customize-your-developer-portal).
  * To create new content on your portal pages, see [Edit the content and layout of your pages](https://www.drupal.org/docs/8/modules/apigee-developer-portal-kickstart/customize-your-developer-portal#s-edit-the-content-and-layout-of-your-portal-pages).
  * To get started with FAQs, Blogs, or Forums, see [Create an FAQ](https://www.drupal.org/docs/8/modules/apigee-developer-portal-kickstart/create-an-faq).



For additional customizations or page development, refer to the following sources:

  * [Drupal 9 Documentation](https://www.drupal.org/docs/9)
  * [Drupal Community](https://www.drupal.org/community)
  * Third-party with expertise in Drupal 10



### Publish your API Documentation with the Apigee API Catalog

Apigee's API Catalog module lets you document your APIs in your Drupal 10 developer portal using OpenAPI specifications and Apigee SmartDocs. Publishing API documentation to your portals makes it easy for developers to learn, test, and evaluate your APIs.

For more information on using the integrated Apigee API Catalog with SmartDocs in your Drupal 10 developer portal, see [Document your APIs](https://www.drupal.org/docs/8/modules/apigee-developer-portal-kickstart/document-your-apis).

### Choose your hosting provider

Using the open source Apigee Drupal 10 modules provides you with complete control over the developer experience in your portal. With this self-managed option, you are responsible for hosting and maintaining the portal sites leveraging these modules. You can choose a provider to manage and host your developer portal, such as [Pantheon](https://pantheon.io/), [Acquia](https://www.acquia.com/), or another provider.

For more information on working with Pantheon to host your Drupal 10 developer portal, see [Pantheon powers Apigee Drupal-based Developer Portals](https://pantheon.io/product/apigee-pantheon-partnership).

For more information on working with Acquia to host your Drupal 10 developer portal, see [Apigee and Acquia partner together to deliver development portals](https://www.acquia.com/landing/apigee-and-acquia-partner-together-deliver-development-portals).

## About the Apigee modules supported for Drupal 10

The following table summarizes the Drupal 10 projects that are available for use with Apigee and their corresponding GitHub Issue Queues for reporting issues. Contributions are appreciated, as outlined in the contribution guidelines for each project.

Project | Description | Issues?  
---|---|---  
[Apigee Edge](https://www.drupal.org/project/apigee_edge) | Enables you to connect your Drupal developer portal to your Apigee or hybrid org. Includes the following submodules: 

  * **API product RBAC** enables administrators to [configure access permissions to API products](https://www.drupal.org/docs/8/modules/apigee-edge/configure-access-permissions-to-api-products).
  * **Debug** enables administrators to [configure and manage Apigee debug logs](https://www.drupal.org/docs/8/modules/apigee-edge/monitor-apigee-edge-debug-logs).
  * **Teams** enables developers to be organized into teams.

| [Report issue](https://github.com/apigee/apigee-edge-drupal/issues)  
[Apigee Client Library for PHP](https://github.com/apigee/apigee-client-php) | Makes it easy to develop PHP clients that call the Apigee API. | [Report issue](https://github.com/apigee/apigee-client-php/issues)  
[Apigee Monetization](https://www.drupal.org/project/apigee_m10n) | Enables you to create a developer portal for an Apigee monetized organization.  | [Report issue](https://github.com/apigee/apigee-m10n-drupal/issues)  
[Apigee Developer Portal Kickstart](https://www.drupal.org/project/apigee_devportal_kickstart) | Enables you to get started quickly using Drupal 10 to create an Apigee developer portal. The Kickstart distribution includes Drupal 10, Apigee, the Apigee Client Library for PHP, the Apigee API Catalog, and customizable themes and templates. | [Report issue](https://github.com/apigee/apigee-devportal-kickstart-drupal/issues)  
[Apigee API Catalog](https://www.drupal.org/project/apigee_api_catalog) | Enables you to document your APIs using OpenAPI specifications and SmartDocs.  | [Report issue](https://github.com/apigee/apigee-api-catalog-drupal/issues)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
