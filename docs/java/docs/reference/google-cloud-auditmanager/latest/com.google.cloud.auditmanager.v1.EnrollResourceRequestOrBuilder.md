---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.EnrollResourceRequestOrBuilder
title: Interface EnrollResourceRequestOrBuilder (0.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:51.890011+00:00
---

# Interface EnrollResourceRequestOrBuilder (0.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.EnrollResourceRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EnrollResourceRequestOrBuilder (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.13.0  0.12.0  0.11.0  0.9.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface EnrollResourceRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDestinations(int index)
    
    
    public abstract EnrollResourceRequest.EligibleDestination getDestinations(int index)

Required. Cloud Storage buckets that you can upload your audit reports to during the audit process.

When you enroll an organization or folder, you can choose a Cloud Storage bucket from any project in the organization or folder. If you run an audit at the project level using the service agent at the organization or folder level, all the buckets that are associated with the service agent are available.

` repeated .google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination destinations = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnrollResourceRequest.EligibleDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination)` |   
  
### getDestinationsCount()
    
    
    public abstract int getDestinationsCount()

Required. Cloud Storage buckets that you can upload your audit reports to during the audit process.

When you enroll an organization or folder, you can choose a Cloud Storage bucket from any project in the organization or folder. If you run an audit at the project level using the service agent at the organization or folder level, all the buckets that are associated with the service agent are available.

` repeated .google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination destinations = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDestinationsList()
    
    
    public abstract List<EnrollResourceRequest.EligibleDestination> getDestinationsList()

Required. Cloud Storage buckets that you can upload your audit reports to during the audit process.

When you enroll an organization or folder, you can choose a Cloud Storage bucket from any project in the organization or folder. If you run an audit at the project level using the service agent at the organization or folder level, all the buckets that are associated with the service agent are available.

` repeated .google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination destinations = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EligibleDestination](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination)>` |   
  
### getDestinationsOrBuilder(int index)
    
    
    public abstract EnrollResourceRequest.EligibleDestinationOrBuilder getDestinationsOrBuilder(int index)

Required. Cloud Storage buckets that you can upload your audit reports to during the audit process.

When you enroll an organization or folder, you can choose a Cloud Storage bucket from any project in the organization or folder. If you run an audit at the project level using the service agent at the organization or folder level, all the buckets that are associated with the service agent are available.

` repeated .google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination destinations = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EnrollResourceRequest.EligibleDestinationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestinationOrBuilder)` |   
  
### getDestinationsOrBuilderList()
    
    
    public abstract List<? extends EnrollResourceRequest.EligibleDestinationOrBuilder> getDestinationsOrBuilderList()

Required. Cloud Storage buckets that you can upload your audit reports to during the audit process.

When you enroll an organization or folder, you can choose a Cloud Storage bucket from any project in the organization or folder. If you run an audit at the project level using the service agent at the organization or folder level, all the buckets that are associated with the service agent are available.

` repeated .google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestination destinations = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.auditmanager.v1.EnrollResourceRequest.EligibleDestinationOrBuilder>` |   
  
### getScope()
    
    
    public abstract String getScope()

Required. Organization, folder, or project to enroll in Audit Manager, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



`string scope = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The scope.  
  
### getScopeBytes()
    
    
    public abstract ByteString getScopeBytes()

Required. Organization, folder, or project to enroll in Audit Manager, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`
  * `organizations/{organization}/locations/{location}`



`string scope = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for scope.  
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. If `true`, only validates the request and does not enroll the resource. This executes standard request validation (such as schema, IAM, and destination checks) and skips the apply phase.

Use this field for the following purposes:

  * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
  * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
  * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



`bool validate_only = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
