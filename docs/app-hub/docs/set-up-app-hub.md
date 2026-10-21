---
url: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub/
title: Choose your application setup model \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:05:57.668911+00:00
---

# Choose your application setup model  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Choose your application setup model Stay organized with collections  Save and categorize content based on your preferences. 

To organize your infrastructure resources into App Hub applications, you must define an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary). This boundary can be a folder containing one or more projects, or a single project, aligning with your organization's [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

Within this boundary, App Hub can discover and manage Google Cloud resources, letting you group them into applications by registering them as [services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service) and [workloads](https://docs.cloud.google.com/app-hub/docs/key-concepts#workload). A key part of this setup is the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project), a specific Google Cloud project that serves as the central point for managing APIs, access control, billing, and quotas for your applications.

This page guides you through selecting the best setup model for your application management boundary by detailing the benefits, considerations, and feature differences among the setup alternatives.

## Compare setup models

The following table provides a comparison between projects and folders for your application management boundary:

**Feature** | **Single-project boundary** ([Preview](https://cloud.google.com/products#product-launch-stages)) | **Folder-level boundary** | **Host project (Legacy)**  
---|---|---|---  
**Recommendation** | New users or small organizations where all application components reside in a single project. | Large organizations with multiple projects contained in a single folder, where you want to align application management with your organizational structure. | Supported model for existing users to manage application components from multiple projects that aren't contained in a single folder.  
**Boundary extent** | A single Google Cloud project | All descendant projects within a Google Cloud folder | A manually-managed set of service projects that define a multiple-project boundary  
**Management** | App Hub discovers supported resources within the project automatically. You can register those resources as services or workloads of applications. | Projects within the folder are automatically added to the boundary. You can register supported resources from those descendant projects as services or workloads of applications. | You must manually attach service projects to the host project to add them to the boundary. You can register supported resources from those service projects as services or workloads of applications.  
**Primary use case** | Small applications, initial adoption, or teams managing infrastructure resources within a single project. | Alignment of application management with your organizational structure by business unit, environment, or team. | Scenarios where application components are spread across projects that don't share a common folder.  
**Application-centric Google Cloud feature support** | Limited support | Full support | Limited support  
**Setup complexity** | Low: Requires a single project. | Medium: Requires a folder structure. | High: Requires manual linking of all projects to the boundary.  
**Setup guide** | [Set up a single project](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-single-project) | [Set up a folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) | [Set up a host project (Legacy)](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project)  
  
## Plan your resource hierarchy for application management

Effective application management in App Hub builds directly upon your existing [resource hierarchy in Google Cloud](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). When you choose a folder or project as an [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary), App Hub's application management layer respects the standard hierarchical rules and inheritance policies of Google Cloud.

The way you define your application management boundary impacts the availability of features across Application-centric Google Cloud products. For details, see Feature support by boundary type.

### How applications align with the Google Cloud resource hierarchy

Think of App Hub's data model as an overlay on the Google Cloud resource hierarchy:

  * **Permissions are inherited:** IAM roles and permissions for applications are granted on the management project, and standard [IAM inheritance rules](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#inheritance) from your resource hierarchy apply.
  * **Metadata is centralized:** The management project centralizes application metadata, such as application owners, criticality, and environment, adding an application-aware layer to your resource management.



The choice of your application management boundary fundamentally shapes how you organize your components in App Hub applications. As illustrated in **Figure 1** , defining your application management boundary on a parent folder, such as _F1_ , lets applications within that folder include resources from projects directly within it, such as _P10_ and _P11_ , as well as from projects within nested folders, such as _P20_ and _P21_ within _F2_.

![An application with
projects P10 and P20, spanning folder levels.](https://docs.cloud.google.com/static/resource-manager/img/app-folder-top.png)

**Figure 1.** The application management boundary is defined on a parent folder.

As illustrated in **Figure 2** , if you define your application management boundary on the nested folder _F2_ , applications in that folder can use resources from projects within it, such as _P20_ and _P21_. If you want to include resources from projects in the parent folder _F1_ , such as _P10_ , you must move that project to _F2_.

![An application with
projects P10 and P20, but P10 has moved to folder F2.](https://docs.cloud.google.com/static/resource-manager/img/app-folder-child.png)

**Figure 2.** The application management boundary is defined on a nested folder.

### Feature support by boundary type

The following table compares product support for each boundary setup model.

Boundary type | App Hub project type | Product support  
---|---|---  
**Single project** ([Preview](https://cloud.google.com/products#product-launch-stages)) | Host project | 

  * App Hub
  * Application Monitoring

  
Management project | 

  * App Hub
  * Application Design Center
  * Application Monitoring
  * Security Command Center

  
**Folder level** | Management project | 

  * App Hub
  * Application Design Center
  * Application Monitoring
  * Cloud Hub
  * Cost Explorer
  * Gemini Cloud Assist
  * [Other Application-centric Google Cloud products](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud)

  
**Multiple projects** | Host project | 

  * App Hub
  * Application Monitoring

  
  
## What's next

  * [Set up a single project](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-single-project)
  * [Set up a folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder)
  * [Set up a host project (Legacy)](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project)
  * [App Hub IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions)
  * [App Hub overview](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
