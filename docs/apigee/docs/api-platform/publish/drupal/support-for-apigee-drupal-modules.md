---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/support-for-apigee-drupal-modules/
title: Support process for Apigee Drupal 10 modules \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:55.424965+00:00
---

# Support process for Apigee Drupal 10 modules  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/drupal/support-for-apigee-drupal-modules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Support process for Apigee Drupal 10 modules Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Apigee modules for Drupal 10 are open source projects that enable a self-hosted developer portal option for Apigee and Apigee hybrid customers. Customers are responsible for hosting and maintaining portals that leverage these modules. As the maintenance status of the Apigee modules for Drupal 10 is [ "Actively maintained"](https://www.drupal.org/node/1066982), all bug reports, tasks, and feature requests are best submitted as issues in GitHub where they will be addressed by maintainers. 

This document covers the [Apigee client for PHP](https://github.com/apigee/apigee-client-php) and the following Apigee Drupal 10 modules: 

  * [Apigee](https://www.drupal.org/project/apigee_edge)
  * [Apigee Monetization](https://www.drupal.org/project/apigee_m10n)
  * [Apigee Developer Portal Kickstart](https://www.drupal.org/project/apigee_devportal_kickstart)
  * [Apigee API Catalog](https://www.drupal.org/project/apigee_api_catalog)



## Version Conventions

The Apigee modules follow the [Drupal release naming conventions](https://www.drupal.org/node/1015226), indicating the stability of each release. For example, releases listed as **alpha** or **beta** are not considered ready for production use, but are available for testing and feedback for the project.

## Critical Bugs

Stable or official releases are considered stable code suitable for production use. Any critical bug in the Apigee modules (not due to configuration or code changes) that might cause data inconsistency, broken functionality, security issues, performance issues, or production impact is covered by the standard support process for Apigee and Apigee hybrid customers. Customers can report a critical bug in the Apigee modules through the [Apigee support portal](https://cloud.google.com/apigee/support/). 

## Other Bugs or Feedback

For other bugs, questions, or feedback, open an issue in the GitHub project (see project page links above). Similarly, if you have a feature or improvement to suggest, open an issue in the related GitHub project. Pull requests are welcomed and encouraged! Please follow the contribution guidelines for each project and open an issue documenting your intended improvement before you write code, in order to facilitate discussion. There may be unanticipated use cases that could impact other users of the project. 

For any issue, it is important to add steps to reproduce the behavior with a minimal install of Drupal core. We cannot address issues that we cannot replicate. If the issue is not reproducible in our system, it could be due to configuration or code changes. 

## Infrastructure and Hosting

Google does not support the infrastructure or hosting of your Drupal site itself, such as: 

  * Server setup and installation 
  * Performance issues unrelated to the Apigee API 
  * Investigation of server errors 
  * Security issues 
  * SMTP/email issues 
  * Code/database backups



If you do not have the resources to host and maintain a server and database yourself, consider using one of our recommended hosting providers. You can also engage with one of our preferred vendors to get expert help on designing or maintaining your own infrastructure. To learn more, contact your Apigee account representative. 

## Custom Development and Configuration

A Drupal site is a fully-customizable application and bugs may be created by unintended configurations or custom code changes to the system. We will address questions and offer guidance for any issues pertaining to the Apigee modules, but Google cannot support all possible custom development or deployments you might choose for your system. Custom code must be maintained and supported by your development team. Examples include: 

  * SEO optimizations 
  * Installation and validation of non-Apigee provided modules and themes to site 
  * Custom theme and module creation



If you do not have Drupal expertise in-house, consider contacting a Google representative to learn how an implementation partner might help. 

## Software and System Maintenance

The maintenance of your infrastructure and site is not covered by support. We strongly encourage all developers and site owners to follow [best security practices](https://www.drupal.org/security/secure-configuration) and keep Drupal core code, as well as contributed modules and plugins, up-to-date. The Drupal Update module can notify administrators when security and regular updates impacting the site are released. See [ Keeping Track of Updates](https://www.drupal.org/docs/user_guide/en/security-announce.html) for more information. Site owners can also track security releases, incidents, and vulnerabilities pertaining to Drupal core and contributed projects on [Drupal's official security advisories page](https://www.drupal.org/security). Subscribe via RSS or follow [@drupalsecurity](https://twitter.com/drupalsecurity) on Twitter. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
