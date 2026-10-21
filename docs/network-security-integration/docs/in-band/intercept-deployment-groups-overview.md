---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview/
title: Intercept deployment groups overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:21.894047+00:00
---

# Intercept deployment groups overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-deployment-groups-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Intercept deployment groups overview Stay organized with collections  Save and categorize content based on your preferences. 

An _intercept deployment group_ is a global, project-scoped resource representing a service producer's packet inspection offerings. An intercept deployment group contains one or more zonal intercept deployments. A service consumer references an intercept deployment group when they create an intercept endpoint group.

For a complete overview of the service producer resources, see [Service producer](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview#service-producer).

## Specifications

Intercept deployment groups have the following specifications:

  * An intercept deployment group is a global, per-project resource.

  * The name of an intercept deployment group has the following format:
        
        projects/PROJECT_ID/locations/global/interceptDeploymentGroups/DEPLOYMENT_GROUP_ID
        

For example, the name for the intercept deployment group with the ID `example-intercept-deployment-group` in project `example-project` is `projects/example-project/locations/global/interceptDeploymentGroups/example-intercept-deployment-group`.

  * A single single intercept deployment group can be referenced by multiple consumer intercept endpoint groups, inspecting traffic from multiple VPC networks.

  * The intercept deployment group only offers packet inspection capabilities in the zones where its intercept deployments are located. If an intercept deployment group doesn't contain an intercept deployment in a zone, then the service producer doesn't offer packet inspection in that zone. intercepted.

  * To delete an intercept deployment group, you must delete all the intercept deployments in that intercept deployment group.




## Identity and Access Management roles

The following table describes the Identity and Access Management (IAM) roles required for managing the intercept deployment groups:

Management task | Necessary role  
---|---  
Create an intercept deployment group  | Intercept Deployment Admin role (`networksecurity.interceptDeploymentAdmin`) on the project where the intercept deployment group is created.  
Modify an existing intercept deployment group  | Intercept Deployment Admin role (`networksecurity.interceptDeploymentAdmin`) on the project where the intercept deployment group is created.  
View details about the intercept deployment group in a project  | Any of the following roles for the project: 

  * Intercept Deployment Admin role (`networksecurity.interceptDeploymentAdmin`)
  * Intercept Deployment Viewer role (`networksecurity.interceptDeploymentViewer`)

  
View all the intercept deployment groups in your project  | Any of the following roles for the project: 

  * Intercept Deployment Admin role (`networksecurity.interceptDeploymentAdmin`)
  * Intercept Deployment Viewer role (`networksecurity.interceptDeploymentViewer`)

  
Delete an intercept deployment group  | Intercept Deployment Admin role (`networksecurity.interceptDeploymentAdmin`) on the project.   
Use an intercept deployment group (for service consumers)  | Intercept Deployment External User role (`networksecurity.interceptDeploymentExternalUser`) on the project.   
  
## Quotas

To view quotas associated with intercept deployment groups, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage intercept deployment groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-deployment-groups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
