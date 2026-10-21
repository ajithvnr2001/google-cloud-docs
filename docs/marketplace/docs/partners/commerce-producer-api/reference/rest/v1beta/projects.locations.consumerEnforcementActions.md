---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions
title: REST Resource: projects.locations.consumerEnforcementActions \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:11.990775+00:00
---

# REST Resource: projects.locations.consumerEnforcementActions  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.consumerEnforcementActions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConsumerEnforcementAction
    * JSON representation
  * ProjectAccessRestrictionConfig
    * JSON representation
  * State
  * ConsumerScope
    * JSON representation
  * ProductScope
    * JSON representation
  * DenyReason
    * JSON representation
  * ReasonCode
  * Methods



## Resource: ConsumerEnforcementAction

Represents a partner action taken to enforce the partner's Vendor Agreement.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "etag": string,
      "state": enum ([State](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#State)),
      "createTime": string,
      "updateTime": string,
      "succeedTime": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "consumerScope": {
        object ([ConsumerScope](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ConsumerScope))
      },
      "productScope": {
        object ([ProductScope](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ProductScope))
      },
      "denyReason": {
        object ([DenyReason](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#DenyReason))
      },
    
      // Union field action can be only one of the following:
      "projectAccessRestrictionAction": {
        object ([ProjectAccessRestrictionConfig](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ProjectAccessRestrictionConfig))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the ConsumerEnforcementAction resource.Format: `projects/{project}/locations/{location}/consumerEnforcementActions/{consumerEnforcementAction}`  
`uid` |  `string` Output only. Unique identifier of the resource.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`state` |  `enum (`[State](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#State)`)` Output only. Current lifecycle state of the resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`succeedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the enforcement action succeeded.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. Human-readable display name of the resource. Maximum length is 63 characters.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels for the resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`consumerScope` |  `object (`[ConsumerScope](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ConsumerScope)`)` Required. Immutable. Consumer scope of the enforcement action.  
`productScope` |  `object (`[ProductScope](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ProductScope)`)` Required. Immutable. Product scope of the enforcement action.  
`denyReason` |  `object (`[DenyReason](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#DenyReason)`)` Output only. Reason for denial. Present when the resource state is `DENIED`.  
Union field `action`. Required. The configured enforcement action. `action` can be only one of the following:  
`projectAccessRestrictionAction` |  `object (`[ProjectAccessRestrictionConfig](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ProjectAccessRestrictionConfig)`)` Optional. Immutable. Restricts product access for consumer projects.  
  
## ProjectAccessRestrictionConfig

Configuration for an access restriction that applies to consumer projects.

While an access restriction applies to a project, the project is prevented from being used as the client project in requests accessing services provided by the relevant products. Access restriction is non-destructive, and does not modify the consumer's procurement state. Consumer project access is restored automatically when the restriction is deleted or ceases to apply to a project.

JSON representation  
---  
      
    
    {
      "falsePositiveGuardDisabled": boolean
    }  
  
Fields  
---  
`falsePositiveGuardDisabled` |  `boolean` Optional. Controls whether Google guards against false positives.When enabled, Google will guard against disruptive enforcement actions that could result from false-positive findings of Vendor Agreement violation or unintentionally overbroad enforcement by the partner. Google will make its own determination based on information available to Google as to whether the enforcement action should proceed, and at its discretion may deny the enforcement action. Google may at its discretion provide details about the basis for its determination when a requested enforcement action is denied, but Google is not obligated to do so, and Google may make determinations based on information that cannot be shared with the partner. If the partner does not agree with the determination, the partner can apply a new enforcement action without the guard.  
  
## State

Represents the lifecycle state of the enforcement action.

New values may be added to this enum in future.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. Unused.  
`RUNNING` | The enforcement action is running. This is the initial state of the resource and persists while the `consumerEnforcementActions.create` long-running Operation runs.If the operation is cancelled or otherwise ends before any enforcement effects occur, the resource will be removed. Otherwise, when the operation is done the resource state will resolve to one of the following states.

  * If the enforcement action is accepted and applied successfully, on completion the state will transition to `SUCCEEDED`.
  * If the enforcement action is denied, on completion the state will transition to `DENIED`.
  * If the enforcement action fails after partial application of enforcement effects, the state will transition to `FAILED` to reflect the inconsistent partial enforcement state.

  
`SUCCEEDED` | The enforcement action was accepted and successfully applied. Any ongoing effects of the enforcement action are active.  
`DENIED` | The enforcement action was not accepted and did not take effect for the reason detailed in `denyReason`.  
`FAILED` | A state transition failed due to a transient or internal system error. Enforcement behavior may be inconsistent. Deletion of a resource in this state will remove any ongoing effects.  
  
## ConsumerScope

Specifies the target consumer resource entity for the enforcement action.

JSON representation  
---  
      
    
    {
    
      // Union field target_consumer_entity can be only one of the following:
      "project": string,
      "billingAccount": string,
      "organization": string
      // End of list of possible types for union field target_consumer_entity.
    }  
  
Fields  
---  
Union field `target_consumer_entity`. Required. Exactly one target resource identifier must be set. `target_consumer_entity` can be only one of the following:  
`project` |  `string` Targets a single project resource. The scope of the enforcement action is limited to the specified project.Must exist at the time the enforcement action is created. Must be specified using project_number format.Format: `projects/{project_number}`  
`billingAccount` |  `string` Targets a billing account resource. The scope of the enforcement action covers the billing account and all projects linked to it.This scope is dynamic. Any effects applied at the time the enforcement action is created are applied to the entities in scope at that time. Any ongoing effects of the enforcement action apply to the entities in scope at the relevant time.Must exist at the time the enforcement action is created. This field cannot be used to target a reseller parent billing account.Format: `billingAccounts/{billingAccount}`  
`organization` |  `string` Targets an organization resource. The scope of the enforcement action covers all projects within the organization, as well as all billing accounts within the organization, and all projects linked to those billing accounts.This scope is dynamic. Any effects applied at the time the enforcement action is created are applied to the entities in scope at that time. Any ongoing effects of the enforcement action apply to the entities in scope at the relevant time.Must exist at the time the enforcement action is created.Format: `organizations/{organization}`  
  
## ProductScope

Defines the product scope of the enforcement action.

JSON representation  
---  
      
    
    {
      "aiplatformPublisherId": string
    }  
  
Fields  
---  
`aiplatformPublisherId` |  `string` Optional. Targets all managed model products in AI Platform Model Garden parented by the specified publisher ID.In the AI Platform Model Garden, a `publisher_id` identifies the model publisher. [Partners with products available in Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models) are assigned a unique publisher ID at the time of first onboarding. Only a partner's own publisher ID can be specified. If you do not know your publisher ID, contact partner support for assistance.Format: `{publisher_id}` (e.g. `google`).  
  
## DenyReason

Explanation for why an enforcement action was not applied.

JSON representation  
---  
      
    
    {
      "reasonCode": enum ([ReasonCode](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ReasonCode)),
      "detailMessage": string
    }  
  
Fields  
---  
`reasonCode` |  `enum (`[ReasonCode](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions#ReasonCode)`)` Output only. The reason code. Always present when enforcement is denied.  
`detailMessage` |  `string` Output only. Optional additional human-readable message explaining why the enforcement action was denied.  
  
## ReasonCode

Code indicating why the enforcement action was denied by Google.

Enums  
---  
`REASON_CODE_UNSPECIFIED` | Unspecified reason. Unused.  
`EXEMPT` | The target consumer entity (or a sub-entity lower in the entity hierarchy) is exempt from API-initiated application of the requested enforcement action. To proceed with enforcement against the consumer, contact Google.  
`FALSE_POSITIVE_GUARD` | The enforcement action was denied because false positive guard mode was requested and false positive protection was triggered.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/create)`

|  Creates a ConsumerEnforcementAction resource.  
  
### `[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/delete)`

|  Deletes a ConsumerEnforcementAction resource.  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/get)`

|  Gets a ConsumerEnforcementAction resource by name.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/list)`

|  Lists ConsumerEnforcementActions under a parent location.  
  
### `[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.consumerEnforcementActions/patch)`

|  Updates an existing ConsumerEnforcementAction resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-20 UTC."],[],[]] 
