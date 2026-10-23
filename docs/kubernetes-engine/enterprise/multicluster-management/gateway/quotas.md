---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/quotas/
title: Quotas and limits for connect gateway \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:40.576002+00:00
---

# Quotas and limits for connect gateway  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Quotas and limits for connect gateway Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the quotas and system limits that apply to the connect gateway. Knowing these quotas and system limits helps you plan your workload traffic, avoid authentication errors, and request quota increases when necessary.

This document is for Admins and architects and Platform admins and operators who manage and administer compute resources across teams. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common Google Kubernetes Engine user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This document lists the quotas and system limits that apply to fleet management.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



## Quotas and limits for connect gateway

The connect gateway has the following quotas and limits:

  * **Request limit:** the connect gateway limits usage to 2,400 requests per minute per _fleet_. Google Cloud applies this limit to the [fleet host project](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#fleet-host-project), regardless of how many projects have clusters registered to the fleet.
  * **Active streams limit:** the connect gateway supports a maximum of 10 active streams per fleet host project.
  * **Request header size limit:** there is an 8 KB limit for the request header size. If you use Google Groups to manage access to the connect gateway, the gateway includes user group information in the request header. If a user is a member of many groups, especially groups with long names, the size of the request header can exceed the 8 KB limit and cause authentication errors. For more information, see the [troubleshooting documentation](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#troubleshooting).



There are no limits on the amount of data transferred through the gateway in each request.

To view quota usage and limits for your projects, or request a quota adjustment, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
