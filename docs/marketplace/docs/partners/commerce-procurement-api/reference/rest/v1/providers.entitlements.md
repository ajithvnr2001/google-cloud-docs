---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements
title: REST Resource: providers.entitlements \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:24:52.052198+00:00
---

# REST Resource: providers.entitlements  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: providers.entitlements Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Entitlement
    * JSON representation
  * EntitlementState
  * Consumer
    * JSON representation
  * Methods



## Resource: Entitlement

Represents a procured product of a customer.

JSON representation  
---  
      
    
    {
      "name": string,
      "account": string,
      "provider": string,
      "product": string,
      "quoteExternalName": string,
      "productExternalName": string,
      "plan": string,
      "offer": string,
      "newPendingOffer": string,
      "newOfferStartTime": string,
      "offerDuration": string,
      "newPendingOfferDuration": string,
      "offerEndTime": string,
      "newOfferEndTime": string,
      "newPendingPlan": string,
      "state": enum ([EntitlementState](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState)),
      "inputProperties": {
        object
      },
      "updateTime": string,
      "createTime": string,
      "usageReportingId": string,
      "messageToUser": string,
      "consumers": [
        {
          object ([Consumer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Consumer))
        }
      ],
      "subscriptionEndTime": string,
      "orderId": string,
      "entitlementBenefitIds": [
        string
      ],
      "cancellationReason": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the entitlement. Entitlement names have the form `providers/{providerId}/entitlements/{entitlement_id}`.  
`account` |  `string` Output only. The resource name of the account that this entitlement is based on, if any.  
`provider` |  `string` Output only. The identifier of the service provider that this entitlement was created against. Each service provider is assigned a unique provider value when they onboard with Cloud Commerce platform.  
`product  
**(deprecated)**` |  `string` This item is deprecated!Output only. The identifier of the entity that was purchased. This may actually represent a product, quote, or offer. We strongly recommend that you use the following more explicit fields: productExternalName, quoteExternalName, or offer.  
`quoteExternalName` |  `string` Output only. The identifier of the quote that was used to procure. Empty if the order is not purchased using a quote.  
`productExternalName` |  `string` Output only. The identifier of the product that was procured.  
`plan` |  `string` Output only. The identifier of the plan that was procured. Required if the product has plans.  
`offer` |  `string` Output only. The name of the offer that was procured. Field is empty if order wasn't made using an offer. Format: 'projects/{project}/services/{service}/privateOffers/{offer}' OR 'projects/{project}/services/{service}/standardOffers/{offer}', depending on whether the offer is private or public. The {service} in the name is the listing service of the offer. It could be either the product service that the offer is referencing, or a generic private offer parent service. We recommend that you don't build your integration to rely on the meaning of this {service} part.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, this field is populated with the upcoming offer.
  * If the entitlement is in the state ENTITLEMENT_ACTIVE, ENTITLEMENT_PENDING_CANCELLATION, ENTITLEMENT_PENDING_PLAN_CHANGE, or ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL, this field is populated with the current offer.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, then this field is populated with the latest offer that the order was associated with.

  
`newPendingOffer` |  `string` Output only. Upon a pending plan change, the name of the offer that the entitlement is switching to. Only exists if the pending plan change is moving to an offer. This field isn't populated for entitlements which aren't active yet. Format: 'projects/{project}/services/{service}/privateOffers/{offer}' OR 'projects/{project}/services/{service}/standardOffers/{offer}', depending on whether the offer is private or public.The {service} in the name is the listing service of the offer. It could be either the product service that the offer is referencing, or a generic private offer parent service. We recommend that you don't build your integration to rely on the meaning of this {service} part.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, ENTITLEMENT_ACTIVE or ENTITLEMENT_PENDING_CANCELLATION, then this field is empty.
  * If the entitlement is in the state ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL or ENTITLEMENT_PENDING_PLAN_CHANGE, then this field is populated with the upcoming offer.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, then this is empty.

  
`newOfferStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the new offer becomes effective. This field is populated even if the entitlement isn't active yet. If there's no upcoming offer, the field is empty.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, this field isn't populated when the entitlement isn't yet approved. After the entitlement is approved, this field is populated with the effective time of the upcoming offer.
  * If the entitlement is in the state ENTITLEMENT_ACTIVE or ENTITLEMENT_PENDING_CANCELLATION, this field isn't populated.
  * If the entitlement is in the state ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL, this field isn't populated, because the entitlement change is waiting on approval.
  * If the entitlement is in the state ENTITLEMENT_PENDING_PLAN_CHANGE, this field is populated with the expected effective time of the upcoming offer, which is in the future.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, then this field is empty.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`offerDuration` |  `string` Output only. The offer duration of the current offer, in ISO 8601 duration format. This is empty if the entitlement wasn't made using an offer, or if the offer has a specified end date instead of a duration.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, and the upcoming offer doesn't have a specified end date, then this field is populated with the duration of the upcoming offer. Otherwise, this field is empty.
  * If the entitlement is in the state ENTITLEMENT_ACTIVE, ENTITLEMENT_PENDING_CANCELLATION, ENTITLEMENT_PENDING_PLAN_CHANGE, or ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL, and the current offer doesn't have a specified end date, then this field contains the duration of the current offer. Otherwise, this field is empty.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, and the offer doesn't have a specified end date, then this field is populated with the duration of the latest offer that the order was associated with. Otherwise, this field is empty.

  
`newPendingOfferDuration` |  `string` Output only. The duration of the new offer, in ISO 8601 duration format. This field is populated for pending offer changes. It isn't populated for entitlements which aren't active yet. If the offer has a specified end date instead of a duration, this field is empty.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, ENTITLEMENT_ACTIVE, or ENTITLEMENT_PENDING_CANCELLATION, this field is empty.
  * If the entitlement is in the state ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL or ENTITLEMENT_PENDING_PLAN_CHANGE, and the upcoming offer doesn't have a specified end date, then this field is populated with the duration of the upcoming offer. Otherwise, this field is empty.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, then this field is empty.

  
`offerEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. End time for the current term of the Offer associated with this entitlement. The value of this field can change naturally over time due to auto-renewal, even if the offer isn't changed.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, then: 
    * If the entitlement isn't approved yet approved, and the offer has a specified end date, then this field is populated with the expected end time of the upcoming offer, in the future. Otherwise, this field is empty.
    * If the entitlement is approved, then this field is populated with the expected end time of the upcoming offer, in the future. This means that this field and the field offer_duration can both exist.
  * If the entitlement is in the state ENTITLEMENT_ACTIVE or ENTITLEMENT_PENDING_CANCELLATION, then this field is populated with the expected end time of the current offer, in the future. This field's value is set regardless of whether the offer has a specific end date or a duration. This means that this field and the field offer_duration can both exist.
  * If the entitlement is in the state ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL or ENTITLEMENT_PENDING_PLAN_CHANGE: 
    * If the entitlement's pricing model is usage based and the associated offer is a private offer whose term has ended, then this field reflects the ACTUAL end time of the entitlement's associated offer (in the past), even though the entitlement associated with this private offer does not terminate at the end of that private offer's term.
    * Otherwise, this is the expected end date of the current offer, in the future.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, then this field is populated with the end time, in the past, of the latest offer that the order was associated with. If the entitlement was cancelled before any offer started, then this field is empty.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`newOfferEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the new offer, determined from the offer's specified end date. If the offer des not have a specified end date then this field is not set. This field is populated even if the entitlement isn't active yet. If there's no upcoming offer, the field is empty.

  * If the entitlement is in the state ENTITLEMENT_ACTIVATION_REQUESTED, ENTITLEMENT_ACTIVE, or ENTITLEMENT_PENDING_CANCELLATION, then this field is empty.
  * If the entitlement is in the state ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL or ENTITLEMENT_PENDING_PLAN_CHANGE, and the upcoming offer has a specified end date, then this field is populated with the expected end time of the upcoming offer, in the future. Otherwise, this field is empty.
  * If the entitlement is in the state ENTITLEMENT_CANCELLED, then this field is empty.

Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`newPendingPlan` |  `string` Output only. The identifier of the pending new plan. Required if the product has plans and the entitlement has a pending plan change.  
`state` |  `enum (`[EntitlementState](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState)`)` Output only. The state of the entitlement.  
`inputProperties  
**(deprecated)**` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` This item is deprecated!Output only. The custom properties that were collected from the user to create this entitlement.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`usageReportingId` |  `string` Output only. The consumerId to use when reporting usage through the Service Control API. See the consumerId field at [Reporting Metrics](https://cloud.google.com/service-control/reporting-metrics) for more details.This field is present only if the product has usage-based billing configured.  
`messageToUser` |  `string` Provider-supplied message that is displayed to the end user. Currently this is used to communicate progress and ETA for provisioning. This field can be updated only when a user is waiting for an action from the provider, i.e. entitlement state is `[EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVATION_REQUESTED)` or `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL)`.This field is cleared automatically when the entitlement state changes.  
`consumers[]` |  `object (`[Consumer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Consumer)`)` Output only. The resources using this entitlement, if applicable.  
`subscriptionEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. End time for the subscription corresponding to this entitlement.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`orderId` |  `string` Output only. The order ID of this entitlement, without any `orders/` resource name prefix.  
`entitlementBenefitIds[]` |  `string` Output only. The entitlement benefit IDs associated with the purchase.  
`cancellationReason` |  `string` Output only. The reason the entitlement was cancelled. If this entitlement wasn't cancelled, this field is empty. Possible values include "unknown", "expired", "user-cancelled", "account-closed", "billing-disabled" (if the customer has manually disabled billing to their resources), "user-aborted", and "migrated" (if the entitlement has migrated across products). Values of this field are subject to change, and we recommend that you don't build your technical integration to rely on these fields.  
  
## EntitlementState

Indicates the current state of an entitlement.

Enums  
---  
`ENTITLEMENT_STATE_UNSPECIFIED` | Default state of the entitlement. It's only set to this value when the entitlement is first created and has not been initialized.  
`ENTITLEMENT_ACTIVATION_REQUESTED` | Indicates that the entitlement has been created, but it hasn't yet become active. The entitlement remains in this state until it becomes active.If the entitlement requires provider approval, a notification is sent to the provider for the activation approval. If the provider doesn't approve, the entitlement is removed. If approved, the entitlement transitions to the `[EntitlementState.ENTITLEMENT_ACTIVE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVE)` state after either a short processing delay or, if applicable, at the scheduled start time of the purchased offer.Plan changes aren't allowed in this state. Instead, customers are expected to cancel the corresponding order and place a new order.  
`ENTITLEMENT_ACTIVE` | Indicates that the entitlement is active. The procured item is now usable and any associated billing events will start occurring. Entitlements in this state WILL renew. The analogous state for an unexpired but non-renewing entitlement is ENTITLEMENT_PENDING_CANCELLATION.In this state, the customer can decide to cancel the entitlement, which would change the state to `[EntitlementState.ENTITLEMENT_PENDING_CANCELLATION](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_CANCELLATION)`, and then `[EntitlementState.ENTITLEMENT_CANCELLED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_CANCELLED)`.The user can also request a change of plan, which will transition the state to `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE)`, and then back to `[EntitlementState.ENTITLEMENT_ACTIVE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVE)`.  
`ENTITLEMENT_PENDING_CANCELLATION` | Indicates that the entitlement will expire at the end of its term. This could mean the customer has elected not to renew this entitlement or the customer elected to cancel an entitlement that only expires at term end.The entitlement typically stays in this state if the entitlement/plan allows use of the underlying resource until the end of the current billing cycle. Once the billing cycle completes, the resource will transition to `[EntitlementState.ENTITLEMENT_CANCELLED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_CANCELLED)` state.The resource cannot be modified during this state.  
`ENTITLEMENT_CANCELLED` | Indicates that the entitlement was cancelled. The entitlement can now be deleted.  
`ENTITLEMENT_PENDING_PLAN_CHANGE` | Indicates that the entitlement is currently active, but there is a pending plan change that is requested by the customer. The entitlement typically stays in this state, if the entitlement/plan requires the completion of the current billing cycle before the plan can be changed. Once the billing cycle completes, the resource will transition to `[EntitlementState.ENTITLEMENT_ACTIVE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVE)`, with its plan changed.  
`ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL` | Indicates that the entitlement is currently active, but there is a plan change request pending provider approval. If the provider approves the plan change, then the entitlement will transition either to `[EntitlementState.ENTITLEMENT_ACTIVE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVE)` or `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE)` depending on whether current plan requires that the billing cycle completes.If the provider rejects the plan change, then the pending plan change request is removed and the entitlement stays in `[EntitlementState.ENTITLEMENT_ACTIVE](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVE)` state with the old plan.  
`ENTITLEMENT_SUSPENDED` | Indicates that the entitlement is suspended either by Google or provider request.This can be triggered for various external reasons (e.g. expiration of credit card on the billing account, violation of terms-of-service of the provider etc.). As such, any remediating action needs to be taken externally, before the entitlement can be activated.This is not yet supported.  
  
## Consumer

A resource using (consuming) this entitlement.

JSON representation  
---  
      
    
    {
      "project": string
    }  
  
Fields  
---  
`project` |  `string` A project name with format `projects/<project number>`.  
  
## Methods  
  
---  
  
### `[approve](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/approve)`

|  Approves an entitlement that is in the `[EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVATION_REQUESTED)` state.  
  
### `[approvePlanChange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/approvePlanChange)`

|  Approves an entitlement plan change that is in the `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL)` state.  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/get)`

|  Gets a requested `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)` resource.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/list)`

|  Lists `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`s for which the provider has read access.  
  
### `[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/patch)`

|  Updates an existing `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`.  
  
### `[reject](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/reject)`

|  Rejects an entitlement that is in the `[EntitlementState.ENTITLEMENT_ACTIVATION_REQUESTED](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_ACTIVATION_REQUESTED)` state.  
  
### `[rejectPlanChange](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/rejectPlanChange)`

|  Rejects an entitlement plan change that is in the `[EntitlementState.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#EntitlementState.ENUM_VALUES.ENTITLEMENT_PENDING_PLAN_CHANGE_APPROVAL)` state.  
  
### `[suspend](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements/suspend)`

|  Requests suspension of an active `[Entitlement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference/rest/v1/providers.entitlements#Entitlement)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-20 UTC."],[],[]] 
