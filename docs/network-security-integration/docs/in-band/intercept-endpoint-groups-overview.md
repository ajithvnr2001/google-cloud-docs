---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview/
title: Intercept endpoint groups and associations overview \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:10.028410+00:00
---

# Intercept endpoint groups and associations overview  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/intercept-endpoint-groups-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Intercept endpoint groups and associations overview Stay organized with collections  Save and categorize content based on your preferences. 

An _intercept endpoint group_ is a global, project-wide resource that lets a consumer access a producer's interception service. Each intercept endpoint group is associated with a single intercept deployment group on the producer side.

An _intercept endpoint group association_ is a global, project-wide resource that represents a consumer's VPC network to be inspected by a specific intercept endpoint group. For each VPC that requires packet inspection, consumers create an intercept endpoint group association.

This page provides a detailed overview of intercept endpoint groups and intercept endpoint group associations.

## Specifications

Intercept endpoint groups have the following specifications:

  * An intercept endpoint group is a global, project-wide resource.
  * The name of an intercept endpoint group is configured in the following format:
        
        projects/PROJECT_ID/locations/global/interceptEndpointGroups/ENDPOINT_GROUP_ID
        

For example, the unique URL identifier for the intercept endpoint group `example-intercept-endpoint-group` in project `example-project` is `projects/example-project/locations/global/interceptEndpointGroups/example-intercept-endpoint-group`.

  * An intercept endpoint group association is a global, project-wide resource.

  * The name of an intercept endpoint association is configured in the following format:
        
        projects/PROJECT_ID/locations/global/interceptEndpointAssociations/ENDPOINT_GROUP_ASSOCIATION_ID
        

For example, the name for the intercept endpoint association ID `example-intercept-endpoint-association` in project `example-project` is `projects/example-project/locations/global/interceptEndpointAssociations/example-intercept-endpoint-association`.

  * You can use an intercept endpoint group across one or more VPCs in different projects in an organization.

  * To enable interception for a VPC network, create an intercept endpoint group association and the required firewall rules.




## Identity and Access Management roles

The following table describes the Identity and Access Management (IAM) roles required for managing the intercept endpoint groups:

Ability | Necessary role  
---|---  
Create an intercept endpoint group  | Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`) on the project.  
Modify an existing intercept endpoint group  | Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`) on the project.  
View details of an intercept endpoint group  | Any of the following roles for the project: 

  * Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`)
  * Intercept Endpoint Viewer role (`roles/networksecurity.interceptEndpointViewer`)

  
View all intercept endpoint groups  | Any of the following roles for the project: 

  * Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`)
  * Intercept Endpoint Viewer role (`roles/networksecurity.interceptEndpointViewer`)

  
  
The following table describes the Identity and Access Management (IAM) roles required for managing the intercept endpoint group associations:

Ability | Necessary role  
---|---  
Create an intercept endpoint group association  |  Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`) on the project where the intercept endpoint group association is created.  Intercept Endpoint User role (`roles/networksecurity.interceptEndpointUser`) on the project, which represents permissions to associate the VPC (which the user is an administrator of) to the intercept endpoint group (which is a project-owned resource, not necessarily owned by the VPC owner).   
Modify an existing intercept endpoint group association  | Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`) on the project where the VPC network exists.   
View details of an intercept endpoint group association  |  Any of the following roles: 

  * Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`)
  * Intercept Endpoint Viewer role (`roles/networksecurity.interceptEndpointViewer`)

  
View all intercept endpoint group associations  | Any of the following roles: 

  * Intercept Endpoint Admin role (`roles/networksecurity.interceptEndpointAdmin`)
  * Intercept Endpoint Viewer role (`roles/networksecurity.interceptEndpointViewer`)

  
  
## Quotas

To view quotas associated with intercept endpoint groups, see [Quotas and limits](https://docs.cloud.google.com/network-security-integration/docs/quotas).

## What's next

  * [Create and manage intercept endpoint groups](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-intercept-endpoint-groups)
  * [Create and manage intercept endpoint group associations](https://docs.cloud.google.com/network-security-integration/docs/in-band/configure-endpoint-group-associations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
