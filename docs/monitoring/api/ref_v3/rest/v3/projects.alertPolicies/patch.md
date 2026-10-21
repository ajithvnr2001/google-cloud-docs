---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch/
title: Method: projects.alertPolicies.patch \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:11.652528+00:00
---

# Method: projects.alertPolicies.patch  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.alertPolicies.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates an alerting policy. You can either replace the entire policy with a new one or replace only certain fields in the current alerting policy by specifying the fields to be updated via `updateMask`. Returns the updated alerting policy.

Design your application to single-thread API calls that modify the state of alerting policies in a single project. This includes calls to alertPolicies.create, alertPolicies.delete and alertPolicies.patch.

### HTTP request

`PATCH https://monitoring.googleapis.com/v3/{alertPolicy.name}`

### Path parameters

Parameters  
---  
`alertPolicy.name` |  `string` Identifier. Required if the policy exists. The resource name for this policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
    

`[ALERT_POLICY_ID]` is assigned by Cloud Monitoring when the policy is created. When calling the `[alertPolicies.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies/create#google.monitoring.v3.AlertPolicyService.CreateAlertPolicy)` method, do not include the `name` field in the alerting policy passed as part of the request.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. A list of alerting policy field names. If this field is not empty, each listed field in the existing alerting policy is set to the value of the corresponding field in the supplied policy (`alertPolicy`), or to the field's default value if the field is not in the supplied alerting policy. Fields not listed retain their previous value.Examples of valid field masks include `displayName`, `documentation`, `documentation.content`, `documentation.mime_type`, `userLabels`, `user_label.nameofkey`, `enabled`, `conditions`, `combiner`, etc.If this field is empty, then the supplied alerting policy replaces the existing policy. It is the same as deleting the existing policy and adding the supplied policy, except for the following:

  * The new policy will have the same `[ALERT_POLICY_ID]` as the former policy. This gives you continuity with the former policy in your notifications and incidents.
  * Conditions in the new policy will keep their former `[CONDITION_ID]` if the supplied condition includes the `name` field with that `[CONDITION_ID]`. If the supplied condition omits the `name` field, then a new `[CONDITION_ID]` is created.

This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy)`.

### Response body

If successful, the response body contains an instance of `[AlertPolicy](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#AlertPolicy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
