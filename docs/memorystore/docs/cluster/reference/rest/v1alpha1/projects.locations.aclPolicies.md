---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies
title: REST Resource: projects.locations.aclPolicies \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:47.031766+00:00
---

# REST Resource: projects.locations.aclPolicies  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  REST Resource: projects.locations.aclPolicies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AclPolicy
    * JSON representation
    * AclRule
      * JSON representation
    * State
    * ClusterAclPolicyAttachment
      * JSON representation
  * Methods



## Resource: AclPolicy

The ACL policy resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "rules": [
        {
          object ([AclRule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies#AclPolicy.AclRule))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies#AclPolicy.State)),
      "clusterAclPolicyAttachments": [
        {
          object ([ClusterAclPolicyAttachment](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies#AclPolicy.ClusterAclPolicyAttachment))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "version": string,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Full resource path of the ACL policy.  
`rules[]` |  `object (`[AclRule](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies#AclPolicy.AclRule)`)` Required. The ACL rules within the ACL policy.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies#AclPolicy.State)`)` Output only. The state of the ACL policy.  
`clusterAclPolicyAttachments[]` |  `object (`[ClusterAclPolicyAttachment](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies#AclPolicy.ClusterAclPolicyAttachment)`)` Output only. The ACL policy attachment status for each attached cluster.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the ACL policy was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp that the ACL policy was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`version  
**(deprecated)**` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!Output only. Deprecated: Used in drift resolution.  
`etag` |  `string` Output only. Etag for the ACL policy.  
  
### AclRule

A single ACL rule which defines the policy for a user.

JSON representation  
---  
      
    
    {
      "username": string,
      "rule": string
    }  
  
Fields  
---  
`username` |  `string` Required. Specifies the IAM user or service account to be added to the ACL policy. This username will be directly set on the Redis OSS.  
`rule` |  `string` Required. The rule to be applied to the username. Ex: "on >password123 ~* [+@all](mailto:+@all)" The format of the rule is defined by Redis OSS: <https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/>  
  
### State

Represents the different states of an ACL policy.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`ACTIVE` | ACL policy has been created and is fully usable. Since ACL policy creation is synchronous and not an LRO, there is no CREATING state.  
`UPDATING` | ACL policy is being updated.  
`DELETING` | ACL policy is being deleted.  
  
### ClusterAclPolicyAttachment

ClusterAclPolicyAttachment stores the ACL policy status for an attached cluster for the revisions successfully applied, under application or failed.

JSON representation  
---  
      
    
    {
      "cluster": string,
      "aclPolicyRevisionStatuses": [
        {
          object ([AclPolicyRevisionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/AclPolicyRevisionStatus))
        }
      ]
    }  
  
Fields  
---  
`cluster` |  `string` Output only. The resource name of the attached Cluster. Format: "projects/{project}/locations/{location}/clusters/{cluster}"  
`aclPolicyRevisionStatuses[]` |  `object (`[AclPolicyRevisionStatus](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/AclPolicyRevisionStatus)`)` Output only. A list of status for various revisions of this ACL policy on the cluster.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/create)`

|  Creates an ACL policy.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/delete)`

|  Deletes a specific ACL policy.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/get)`

|  Gets the details of a specific Redis Cluster ACL policy.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/list)`

|  Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
  
### `[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/patch)`

|  Updates the ACL policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
