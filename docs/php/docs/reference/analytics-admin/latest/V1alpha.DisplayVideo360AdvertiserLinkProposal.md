---
url: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal
title: Google Analytics Admin V1alpha Client - Class DisplayVideo360AdvertiserLinkProposal (0.34.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:55:05.701266+00:00
---

# Google Analytics Admin V1alpha Client - Class DisplayVideo360AdvertiserLinkProposal (0.34.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.DisplayVideo360AdvertiserLinkProposal

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Admin V1alpha Client - Class DisplayVideo360AdvertiserLinkProposal (0.34.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.34.3 (latest)  0.33.0  0.32.0  0.31.3  0.30.0  0.29.1  0.28.1  0.27.0  0.26.0  0.25.2  0.24.2  0.23.0  0.22.5  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Admin V1alpha Client class DisplayVideo360AdvertiserLinkProposal.

A proposal for a link between a Google Analytics property and a Display & Video 360 advertiser.

A proposal is converted to a DisplayVideo360AdvertiserLink once approved. Google Analytics admins approve inbound proposals while Display & Video 360 admins approve outbound proposals.

Generated from protobuf message `google.analytics.admin.v1alpha.DisplayVideo360AdvertiserLinkProposal`

## Namespace

Google \ Analytics \ Admin \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
Identifier. The resource name for this DisplayVideo360AdvertiserLinkProposal resource. Format: properties/{propertyId}/displayVideo360AdvertiserLinkProposals/{proposalId} Note: proposalId is not the Display & Video 360 Advertiser ID  
`↳ advertiser_id` |  `string`   
Immutable. The Display & Video 360 Advertiser's advertiser ID.  
`↳ link_proposal_status_details` |  `[LinkProposalStatusDetails](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.LinkProposalStatusDetails)`   
Output only. The status information for this link proposal.  
`↳ advertiser_display_name` |  `string`   
Output only. The display name of the Display & Video Advertiser. Only populated for proposals that originated from Display & Video 360.  
`↳ validation_email` |  `string`   
Input only. On a proposal being sent to Display & Video 360, this field must be set to the email address of an admin on the target advertiser. This is used to verify that the Google Analytics admin is aware of at least one admin on the Display & Video 360 Advertiser. This does not restrict approval of the proposal to a single user. Any admin on the Display & Video 360 Advertiser may approve the proposal.  
`↳ ads_personalization_enabled` |  `Google\Protobuf\BoolValue`   
Immutable. Enables personalized advertising features with this integration. If this field is not set on create, it will be defaulted to true.  
`↳ campaign_data_sharing_enabled` |  `Google\Protobuf\BoolValue`   
Immutable. Enables the import of campaign data from Display & Video 360. If this field is not set on create, it will be defaulted to true.  
`↳ cost_data_sharing_enabled` |  `Google\Protobuf\BoolValue`   
Immutable. Enables the import of cost data from Display & Video 360. This can only be enabled if campaign_data_sharing_enabled is enabled. If this field is not set on create, it will be defaulted to true.  
  
### getName

Identifier. The resource name for this DisplayVideo360AdvertiserLinkProposal resource. Format: properties/{propertyId}/displayVideo360AdvertiserLinkProposals/{proposalId} Note: proposalId is not the Display & Video 360 Advertiser ID

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Identifier. The resource name for this DisplayVideo360AdvertiserLinkProposal resource. Format: properties/{propertyId}/displayVideo360AdvertiserLinkProposals/{proposalId} Note: proposalId is not the Display & Video 360 Advertiser ID

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdvertiserId

Immutable. The Display & Video 360 Advertiser's advertiser ID.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAdvertiserId

Immutable. The Display & Video 360 Advertiser's advertiser ID.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLinkProposalStatusDetails

Output only. The status information for this link proposal.

**Returns**  
---  
**Type** | **Description**  
`[LinkProposalStatusDetails](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.LinkProposalStatusDetails)|null` |   
  
### hasLinkProposalStatusDetails

### clearLinkProposalStatusDetails

### setLinkProposalStatusDetails

Output only. The status information for this link proposal.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[LinkProposalStatusDetails](https://docs.cloud.google.com/php/docs/reference/analytics-admin/latest/V1alpha.LinkProposalStatusDetails)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdvertiserDisplayName

Output only. The display name of the Display & Video Advertiser.

Only populated for proposals that originated from Display & Video 360.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setAdvertiserDisplayName

Output only. The display name of the Display & Video Advertiser.

Only populated for proposals that originated from Display & Video 360.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getValidationEmail

Input only. On a proposal being sent to Display & Video 360, this field must be set to the email address of an admin on the target advertiser. This is used to verify that the Google Analytics admin is aware of at least one admin on the Display & Video 360 Advertiser. This does not restrict approval of the proposal to a single user. Any admin on the Display & Video 360 Advertiser may approve the proposal.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setValidationEmail

Input only. On a proposal being sent to Display & Video 360, this field must be set to the email address of an admin on the target advertiser. This is used to verify that the Google Analytics admin is aware of at least one admin on the Display & Video 360 Advertiser. This does not restrict approval of the proposal to a single user. Any admin on the Display & Video 360 Advertiser may approve the proposal.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAdsPersonalizationEnabled

Immutable. Enables personalized advertising features with this integration.

If this field is not set on create, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\BoolValue|null` |   
  
### hasAdsPersonalizationEnabled

### clearAdsPersonalizationEnabled

### getAdsPersonalizationEnabledUnwrapped

Returns the unboxed value from `getAdsPersonalizationEnabled()`

Immutable. Enables personalized advertising features with this integration. If this field is not set on create, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`bool|null` |   
  
### setAdsPersonalizationEnabled

Immutable. Enables personalized advertising features with this integration.

If this field is not set on create, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\BoolValue`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### setAdsPersonalizationEnabledUnwrapped

Sets the field by wrapping a primitive type in a Google\Protobuf\BoolValue object.

Immutable. Enables personalized advertising features with this integration. If this field is not set on create, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool|null`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCampaignDataSharingEnabled

Immutable. Enables the import of campaign data from Display & Video 360.

If this field is not set on create, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\BoolValue|null` |   
  
### hasCampaignDataSharingEnabled

### clearCampaignDataSharingEnabled

### getCampaignDataSharingEnabledUnwrapped

Returns the unboxed value from `getCampaignDataSharingEnabled()`

Immutable. Enables the import of campaign data from Display & Video 360. If this field is not set on create, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`bool|null` |   
  
### setCampaignDataSharingEnabled

Immutable. Enables the import of campaign data from Display & Video 360.

If this field is not set on create, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\BoolValue`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### setCampaignDataSharingEnabledUnwrapped

Sets the field by wrapping a primitive type in a Google\Protobuf\BoolValue object.

Immutable. Enables the import of campaign data from Display & Video 360. If this field is not set on create, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool|null`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCostDataSharingEnabled

Immutable. Enables the import of cost data from Display & Video 360.

This can only be enabled if campaign_data_sharing_enabled is enabled. If this field is not set on create, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\BoolValue|null` |   
  
### hasCostDataSharingEnabled

### clearCostDataSharingEnabled

### getCostDataSharingEnabledUnwrapped

Returns the unboxed value from `getCostDataSharingEnabled()`

Immutable. Enables the import of cost data from Display & Video 360. This can only be enabled if campaign_data_sharing_enabled is enabled. If this field is not set on create, it will be defaulted to true.

**Returns**  
---  
**Type** | **Description**  
`bool|null` |   
  
### setCostDataSharingEnabled

Immutable. Enables the import of cost data from Display & Video 360.

This can only be enabled if campaign_data_sharing_enabled is enabled. If this field is not set on create, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\BoolValue`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### setCostDataSharingEnabledUnwrapped

Sets the field by wrapping a primitive type in a Google\Protobuf\BoolValue object.

Immutable. Enables the import of cost data from Display & Video 360. This can only be enabled if campaign_data_sharing_enabled is enabled. If this field is not set on create, it will be defaulted to true.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool|null`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
