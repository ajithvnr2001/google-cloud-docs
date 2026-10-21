---
url: https://docs.cloud.google.com/deployment-manager/docs/deprecations/composite-types/
title: Composite types deprecation \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:52.778853+00:00
---

# Composite types deprecation  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/deprecations/composite-types/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Composite types deprecation Stay organized with collections  Save and categorize content based on your preferences. 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [composite types](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types) feature for Google Cloud Deployment Manager will be shut down on **February 22, 2022**. After this date, you won't be able to create deployments that use composite types or update existing deployments that use composite types.

# Shutdown timetable

The following table lists the shutdown schedule for composite types. If you have a critical dependency on composite types and would like to opt-out of one or more of service fault simulations, please request exemption [here](https://forms.gle/6HPHiB9pUqjUbuZa8). 

Date | Event  
---|---  
**October 4th-5th, 2021** | Service fault simulation - all composite type operations will temporarily fail for a day between 11AM on October 4th 2021 PDT and 11AM on October 5th 2021 PDT.  
**October 18th-25th, 2021** | Service fault simulation - all composite type operations will temporarily fail for a week between 11AM on October 18th 2021 PDT and 11AM on October 25th 2021 PDT.  
**February 22, 2022** | You won't be able to create deployments, or update existing deployments, that use composite types.  
  
To convert your composite types to supported templates, follow [this migration guide](https://docs.cloud.google.com/deployment-manager/docs/migrations/composite-types).  
  
## Service fault simulation

This is a scheduled and temporary feature interruption in which all composite types operations fail. The intent is for customers who have migrated to validate that no remaining dependencies exist on composite types. If you haven't yet migrated away from using composite types, request an exemption [here](https://forms.gle/6HPHiB9pUqjUbuZa8) to be excluded from this simulation. **You must make your exemption request before 10AM PDT on the Wednesday before each scheduled interruption of service.**

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
