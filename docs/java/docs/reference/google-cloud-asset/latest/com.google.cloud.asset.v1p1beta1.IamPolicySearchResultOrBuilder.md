---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1p1beta1.IamPolicySearchResultOrBuilder
title: Interface IamPolicySearchResultOrBuilder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:22.399369+00:00
---

# Interface IamPolicySearchResultOrBuilder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1p1beta1.IamPolicySearchResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface IamPolicySearchResultOrBuilder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.2-SNAPSHOT  3.6.0  3.4.1  3.3.1  3.2.17 
    
    
    public interface IamPolicySearchResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExplanation()
    
    
    public abstract IamPolicySearchResult.Explanation getExplanation()

Explanation about the IAM policy search result. It contains additional information that explains why the search result matches the query.

`.google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation explanation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[IamPolicySearchResult.Explanation](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation)` | The explanation.  
  
### getExplanationOrBuilder()
    
    
    public abstract IamPolicySearchResult.ExplanationOrBuilder getExplanationOrBuilder()

Explanation about the IAM policy search result. It contains additional information that explains why the search result matches the query.

`.google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation explanation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[IamPolicySearchResult.ExplanationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-asset/latest/com.google.cloud.asset.v1p1beta1.IamPolicySearchResult.ExplanationOrBuilder)` |   
  
### getPolicy()
    
    
    public abstract Policy getPolicy()

The IAM policy attached to the specified resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constraint on policies (e.g. an empty query), this contains all the bindings.

`.google.iam.v1.Policy policy = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.Policy` | The policy.  
  
### getPolicyOrBuilder()
    
    
    public abstract PolicyOrBuilder getPolicyOrBuilder()

The IAM policy attached to the specified resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constraint on policies (e.g. an empty query), this contains all the bindings.

`.google.iam.v1.Policy policy = 4;`

**Returns**  
---  
**Type** | **Description**  
`com.google.iam.v1.PolicyOrBuilder` |   
  
### getProject()
    
    
    public abstract String getProject()

The project that the associated Google Cloud resource belongs to, in the form of `projects/{project_number}`. If an IAM policy is set on a resource \-- such as a Compute Engine instance or a Cloud Storage bucket -- the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, the project field will be empty.

`string project = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The project.  
  
### getProjectBytes()
    
    
    public abstract ByteString getProjectBytes()

The project that the associated Google Cloud resource belongs to, in the form of `projects/{project_number}`. If an IAM policy is set on a resource \-- such as a Compute Engine instance or a Cloud Storage bucket -- the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, the project field will be empty.

`string project = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for project.  
  
### getResource()
    
    
    public abstract String getResource()

The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the resource associated with this IAM policy.

`string resource = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resource.  
  
### getResourceBytes()
    
    
    public abstract ByteString getResourceBytes()

The [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name) of the resource associated with this IAM policy.

`string resource = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resource.  
  
### hasExplanation()
    
    
    public abstract boolean hasExplanation()

Explanation about the IAM policy search result. It contains additional information that explains why the search result matches the query.

`.google.cloud.asset.v1p1beta1.IamPolicySearchResult.Explanation explanation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the explanation field is set.  
  
### hasPolicy()
    
    
    public abstract boolean hasPolicy()

The IAM policy attached to the specified resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constraint on policies (e.g. an empty query), this contains all the bindings.

`.google.iam.v1.Policy policy = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the policy field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
