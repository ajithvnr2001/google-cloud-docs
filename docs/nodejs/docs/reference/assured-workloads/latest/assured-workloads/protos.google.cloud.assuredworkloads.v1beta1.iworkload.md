---
url: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload
title: Interface protos.google.cloud.assuredworkloads.v1beta1.IWorkload (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:33.616413+00:00
---

# Interface protos.google.cloud.assuredworkloads.v1beta1.IWorkload (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1beta1.iworkload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.assuredworkloads.v1beta1.IWorkload (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.6.2  3.5.0  3.4.1  3.2.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.6 

Properties of a Workload.

## Package

[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)

## Properties 

### billingAccount
    
    
    billingAccount?: (string|null);

Workload billingAccount

### cjisSettings
    
    
    cjisSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.ICJISSettings|null);

Workload cjisSettings

### complianceRegime
    
    
    complianceRegime?: (google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime|keyof typeof google.cloud.assuredworkloads.v1beta1.Workload.ComplianceRegime|null);

Workload complianceRegime

### compliantButDisallowedServices
    
    
    compliantButDisallowedServices?: (string[]|null);

Workload compliantButDisallowedServices

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Workload createTime

### displayName
    
    
    displayName?: (string|null);

Workload displayName

### enableSovereignControls
    
    
    enableSovereignControls?: (boolean|null);

Workload enableSovereignControls

### etag
    
    
    etag?: (string|null);

Workload etag

### fedrampHighSettings
    
    
    fedrampHighSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IFedrampHighSettings|null);

Workload fedrampHighSettings

### fedrampModerateSettings
    
    
    fedrampModerateSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IFedrampModerateSettings|null);

Workload fedrampModerateSettings

### il4Settings
    
    
    il4Settings?: (google.cloud.assuredworkloads.v1beta1.Workload.IIL4Settings|null);

Workload il4Settings

### kajEnrollmentState
    
    
    kajEnrollmentState?: (google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState|keyof typeof google.cloud.assuredworkloads.v1beta1.Workload.KajEnrollmentState|null);

Workload kajEnrollmentState

### kmsSettings
    
    
    kmsSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IKMSSettings|null);

Workload kmsSettings

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Workload labels

### name
    
    
    name?: (string|null);

Workload name

### provisionedResourcesParent
    
    
    provisionedResourcesParent?: (string|null);

Workload provisionedResourcesParent

### resources
    
    
    resources?: (google.cloud.assuredworkloads.v1beta1.Workload.IResourceInfo[]|null);

Workload resources

### resourceSettings
    
    
    resourceSettings?: (google.cloud.assuredworkloads.v1beta1.Workload.IResourceSettings[]|null);

Workload resourceSettings

### saaEnrollmentResponse
    
    
    saaEnrollmentResponse?: (google.cloud.assuredworkloads.v1beta1.Workload.ISaaEnrollmentResponse|null);

Workload saaEnrollmentResponse

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
