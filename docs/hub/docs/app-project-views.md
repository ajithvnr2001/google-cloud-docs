---
url: https://docs.cloud.google.com/hub/docs/app-project-views/
title: Application views and project views \u00a0|\u00a0 Cloud Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:22:06.435592+00:00
---

# Application views and project views  |  Cloud Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/hub/docs/app-project-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Hub ](https://docs.cloud.google.com/hub/docs)
  * [ Guides ](https://docs.cloud.google.com/hub/docs/overview)



Send feedback 

#  Application views and project views Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Hub can display data for resources in a Google Cloud project or an App Hub application.

Viewing data in individual projects makes it difficult to understand resource relationships and dependencies that span across multiple projects. To understand these relationships, [App Hub applications](https://docs.cloud.google.com/app-hub/docs/key-concepts#application) let you group related resources together across projects so that you can understand resource interactions and analyze, monitor, manage, and troubleshoot in an application-centric way.

The data that is available on a Cloud Hub page depends on the type of data that you are viewing.

## Resources in a project

When you select a regular Google Cloud project in the project picker, Cloud Hub displays data for resources in that project.

You must have the permissions required to view the data in the selected project.

## Applications

When you select a [folder configured for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications) or its management project from the project picker, you can view data for an application that you created under that project.

Several pages in Cloud Hub show data for multiple applications:

  * Deployments: Displays deployment notifications and updates for applications in the folder.
  * App Topology: Displays query results for all applications, services, or workloads that meet the query criteria.



Folders enabled for application management have a special icon (![ ](https://docs.cloud.google.com/static/hub/images/app-folder.png)). The management project for that folder also has a unique icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)).

To create your applications, you can use [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) to group together your existing Google Cloud resources or [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview) to design and deploy new applications.

To learn about required permissions for viewing application data, see [Access control with IAM](https://docs.cloud.google.com/hub/docs/access-control).

## Support for applications and project resources

The following table shows which types of data are available for each main section of Cloud Hub.

**Note:** Cloud Hub doesn't support [legacy host projects](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).Page | Applications in a project | Applications in a folder | Project resources | [Home](https://docs.cloud.google.com/hub/docs/home) |  | check | check  
---|---|---|---  
[Deployments](https://docs.cloud.google.com/hub/docs/deployments) |  | check |   
[Health & troubleshooting](https://docs.cloud.google.com/hub/docs/health) |  | check | check  
[Security & compliance](https://docs.cloud.google.com/hub/docs/security) |  | check | check  
[Optimization](https://docs.cloud.google.com/hub/docs/optimize) |  | check | check  
[Maintenance](https://docs.cloud.google.com/hub/docs/maintenance) |  | check | check  
[Quotas & reservations](https://docs.cloud.google.com/hub/docs/quotas-reservations) |  |  | check  
[Support](https://docs.cloud.google.com/hub/docs/support) |  |  | check  
[App Topology](https://docs.cloud.google.com/hub/docs/support) | check | check | check  
  
If you navigate between pages in Cloud Hub, the selected project or application persists if both pages support that type of data. If you want to review data for multiple applications or projects, consider using a dedicated browser tab for each application or project that you want to view.

## What's next

  * [Set up App Hub](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder)
  * [Set up App Design Center](https://docs.cloud.google.com/application-design-center/docs/setup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
