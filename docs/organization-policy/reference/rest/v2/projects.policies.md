---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies
title: REST Resource: projects.policies \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:42.534947+00:00
---

# REST Resource: projects.policies  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  REST Resource: projects.policies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Policy
    * JSON representation
  * Methods



## Resource: Policy

Defines an organization policy that is used to specify constraints for configurations of Google Cloud resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "spec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec))
      },
      "alternate": {
        object ([AlternatePolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.AlternatePolicySpec))
      },
      "dryRunSpec": {
        object ([PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint that this policy configures:

  * `projects/{project_number}/policies/{constraint_name}`
  * `folders/{folder_number}/policies/{constraint_name}`
  * `organizations/{organization_number}/policies/{constraint_name}`

For example, `projects/123/policies/compute.disableSerialPortAccess`.Note: `projects/{projectId}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number.  
`spec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec)`)` Basic information about the organization policy.  
`alternate  
**(deprecated)**` |  `object (`[AlternatePolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.AlternatePolicySpec)`)` This item is deprecated!Deprecated.  
`dryRunSpec` |  `object (`[PolicySpec](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy.PolicySpec)`)` Dry-run policy. Audit-only policy, can be used to monitor how the policy would have impacted the existing and future resources if it's enforced.  
`etag` |  `string` Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This entity tag (ETag) is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/create)`

|  Creates a policy.  
  
### `[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/delete)`

|  Deletes a policy.  
  
### `[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/get)`

|  Gets a policy on a resource.  
  
### `[getEffectivePolicy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/getEffectivePolicy)`

|  Gets the effective policy on a resource.  
  
### `[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/list)`

|  Retrieves all of the policies that exist on a particular resource.  
  
### `[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/patch)`

|  Updates a policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
