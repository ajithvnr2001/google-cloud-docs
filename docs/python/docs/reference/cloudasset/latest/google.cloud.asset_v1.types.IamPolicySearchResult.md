---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult
title: Class IamPolicySearchResult (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:29.810326+00:00
---

# Class IamPolicySearchResult (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class IamPolicySearchResult (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    IamPolicySearchResult(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A result of IAM Policy search, containing information of an IAM policy.

## Attributes  
  
---  
**Name** | **Description**  
`resource` |  `str`   
The full resource name of the resource associated with this IAM policy. Example: `//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1`. See `Cloud Asset Inventory Resource Name Format   
`asset_type` |  `str`   
The type of the resource associated with this IAM policy. Example: `compute.googleapis.com/Disk`. To search against the `asset_type`: \- specify the `asset_types` field in your search request.   
`project` |  `str`   
The project that the associated Google Cloud resource belongs to, in the form of projects/{PROJECT_NUMBER}. If an IAM policy is set on a resource (like VM instance, Cloud Storage bucket), the project field will indicate the project that contains the resource. If an IAM policy is set on a folder or organization, this field will be empty. To search against the `project`: \- specify the `scope` field as this project in your search request.   
`folders` |  `MutableSequence[str]`   
The folder(s) that the IAM policy belongs to, in the form of folders/{FOLDER_NUMBER}. This field is available when the IAM policy belongs to one or more folders. To search against `folders`: \- use a field query. Example: `folders:(123 OR 456)` \- use a free text query. Example: `123` \- specify the `scope` field as this folder in your search request.   
`organization` |  `str`   
The organization that the IAM policy belongs to, in the form of organizations/{ORGANIZATION_NUMBER}. This field is available when the IAM policy belongs to an organization. To search against `organization`: \- use a field query. Example: `organization:123` \- use a free text query. Example: `123` \- specify the `scope` field as this organization in your search request.   
`policy` |  `google.iam.v1.policy_pb2.Policy`   
The IAM policy directly set on the given resource. Note that the original IAM policy can contain multiple bindings. This only contains the bindings that match the given query. For queries that don't contain a constrain on policies (e.g., an empty query), this contains all the bindings. To search against the `policy` bindings: \- use a field query: \- query by the policy contained members. Example: `policy:amy@gmail.com` \- query by the policy contained roles. Example: `policy:roles/compute.admin` \- query by the policy contained roles' included permissions. Example: `policy.role.permissions:compute.instances.create`  
`explanation` |  `[google.cloud.asset_v1.types.IamPolicySearchResult.Explanation](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult.Explanation)`   
Explanation about the IAM policy search result. It contains additional information to explain why the search result matches the query.   
  
## Classes 

### Explanation
    
    
    Explanation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Explanation about the IAM policy search result.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
