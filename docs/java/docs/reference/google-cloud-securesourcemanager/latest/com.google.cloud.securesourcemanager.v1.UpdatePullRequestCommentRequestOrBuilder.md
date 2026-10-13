---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.UpdatePullRequestCommentRequestOrBuilder
title: Interface UpdatePullRequestCommentRequestOrBuilder (0.69.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:27:58.618246+00:00
---

# Interface UpdatePullRequestCommentRequestOrBuilder (0.69.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.UpdatePullRequestCommentRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdatePullRequestCommentRequestOrBuilder (0.69.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.69.0 (latest)  0.65.0  0.64.0  0.63.0  0.61.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.50.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.34.0  0.33.0  0.32.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface UpdatePullRequestCommentRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPullRequestComment()
    
    
    public abstract PullRequestComment getPullRequestComment()

Required. The pull request comment to update.

` .google.cloud.securesourcemanager.v1.PullRequestComment pull_request_comment = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PullRequestComment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.PullRequestComment)` | The pullRequestComment.  
  
### getPullRequestCommentOrBuilder()
    
    
    public abstract PullRequestCommentOrBuilder getPullRequestCommentOrBuilder()

Required. The pull request comment to update.

` .google.cloud.securesourcemanager.v1.PullRequestComment pull_request_comment = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PullRequestCommentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.PullRequestCommentOrBuilder)` |   
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Optional. Field mask is used to specify the fields to be overwritten in the pull request comment resource by the update. Updatable fields are `body`.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Optional. Field mask is used to specify the fields to be overwritten in the pull request comment resource by the update. Updatable fields are `body`.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasPullRequestComment()
    
    
    public abstract boolean hasPullRequestComment()

Required. The pull request comment to update.

` .google.cloud.securesourcemanager.v1.PullRequestComment pull_request_comment = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pullRequestComment field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Optional. Field mask is used to specify the fields to be overwritten in the pull request comment resource by the update. Updatable fields are `body`.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
