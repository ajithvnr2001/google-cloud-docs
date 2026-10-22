---
url: https://docs.cloud.google.com/deployment-manager/docs/migrations/actions/
title: Replacing usage of Actions \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:10.350994+00:00
---

# Replacing usage of Actions  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/migrations/actions/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Replacing usage of Actions Stay organized with collections  Save and categorize content based on your preferences. 

**Alpha**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Actions feature for Google Cloud Deployment Manager is an alpha feature that extends the range of API methods that Deployment Manager can call. The following is an example of what an Action looks like in a configuration:
    
    
    name: action-name
    action: gcp-types/service:service.collection/functionName
    metadata:
      runtimePolicy:
      - CREATE
    properties:
      prop1: val1
      prop2: val2
    

Because this feature is unsupported, we recommend that you **don't** use it in your configurations. We also recommend that you migrate your existing usage of Actions to the following supported alternatives.

# Migrating

The following table lists the recommended steps for replacing Actions, based on the type of Actions you are using:

Action type | Migration recommendation  
---|---  
`gcp-types/storage-v1:storage.buckets.setIamPolicy` | [Replace the Action `storage.buckets.setIamPolicy`](https://docs.cloud.google.com/deployment-manager/docs/migrations/storage-buckets-setiampolicy) with the supported virtual resource `virtual.buckets.iamMemberBinding`.  
Other Identity and Access Management (IAM) policy Actions | Use [an `accessControl` policy](https://docs.cloud.google.com/deployment-manager/docs/configuration/set-access-control-resources).  
`gcp-types/sqladmin-v1beta4:sql.instances.*`, or other `sqladmin` resources | Use the `gcp-types/sqlmin-v1beta4:instances` [resource type](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).  
`gcp-types/serviceusage-v1:serviceusage.services.batchEnable` | Use the `deploymentmanager.v2.virtual.enableService` [resource type](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types).  
`gcp-types/pubsub-v1:pubsub.projects.topics.*` | For Pub/Sub topics, use the corresponding `gcp-types/pubsub-v1:projects.topics` [type](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types). For subscriptions, use `gcp-types/pubsub-v1:projects.subscriptions`.  
`gcp-types/compute-v1:compute.networks.*` | To replace `compute.*` Actions, use `gcp-types/compute-v1:networks` and its related [types and collections](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types).  
All other Actions | Check if there is a corresponding supported [resource type](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-resource-types) or [Google Cloud type provider](https://docs.cloud.google.com/deployment-manager/docs/configuration/supported-gcp-types), and use that instead if there is. Otherwise, you can replace your Actions by [creating custom type providers with custom backends](https://docs.cloud.google.com/deployment-manager/docs/migrations/custom-types-custom-backends).  
  
To request new virtual resources, you can [open an issue](https://issuetracker.google.com/issues/new?component=187078&template=0) in the public issue tracker, or add a comment to [an existing issue](https://issuetracker.google.com/savedsearches/559663).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
