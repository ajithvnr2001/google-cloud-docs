---
url: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilineitem
title: Interface protos.google.ads.admanager.v1.ILineItem (0.14.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:11.166107+00:00
---

# Interface protos.google.ads.admanager.v1.ILineItem (0.14.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/admanager/protos.google.ads.admanager.v1.ilineitem

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.ads.admanager.v1.ILineItem (0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.12.0  0.11.0  0.7.0  0.6.0  0.1.0 

Properties of a LineItem.

## Package

[@google-ads/admanager](https://docs.cloud.google.com/nodejs/docs/reference/admanager/latest/overview.html)

## Properties 

### allowedFormats
    
    
    allowedFormats?: (google.ads.admanager.v1.LineItemAllowedFormatEnum.LineItemAllowedFormat[]|null);

LineItem allowedFormats

### allowOverbook
    
    
    allowOverbook?: (boolean|null);

LineItem allowOverbook

### appliedLabels
    
    
    appliedLabels?: (google.ads.admanager.v1.IAppliedLabel[]|null);

LineItem appliedLabels

### archived
    
    
    archived?: (boolean|null);

LineItem archived

### autoExtensionDays
    
    
    autoExtensionDays?: (number|null);

LineItem autoExtensionDays

### budget
    
    
    budget?: (google.type.IMoney|null);

LineItem budget

### childContentEligibility
    
    
    childContentEligibility?: (google.ads.admanager.v1.ChildContentEligibilityEnum.ChildContentEligibility|keyof typeof google.ads.admanager.v1.ChildContentEligibilityEnum.ChildContentEligibility|null);

LineItem childContentEligibility

### companionDeliveryOption
    
    
    companionDeliveryOption?: (google.ads.admanager.v1.CompanionDeliveryOptionEnum.CompanionDeliveryOption|keyof typeof google.ads.admanager.v1.CompanionDeliveryOptionEnum.CompanionDeliveryOption|null);

LineItem companionDeliveryOption

### competitiveConstraintScope
    
    
    competitiveConstraintScope?: (google.ads.admanager.v1.ExclusionScopeEnum.ExclusionScope|keyof typeof google.ads.admanager.v1.ExclusionScopeEnum.ExclusionScope|null);

LineItem competitiveConstraintScope

### contractedUnitsBought
    
    
    contractedUnitsBought?: (number|Long|string|null);

LineItem contractedUnitsBought

### costType
    
    
    costType?: (google.ads.admanager.v1.LineItemCostTypeEnum.LineItemCostType|keyof typeof google.ads.admanager.v1.LineItemCostTypeEnum.LineItemCostType|null);

LineItem costType

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

LineItem createTime

### creativePlaceholders
    
    
    creativePlaceholders?: (google.ads.admanager.v1.ICreativePlaceholder[]|null);

LineItem creativePlaceholders

### creativeRotationType
    
    
    creativeRotationType?: (google.ads.admanager.v1.CreativeRotationTypeEnum.CreativeRotationType|keyof typeof google.ads.admanager.v1.CreativeRotationTypeEnum.CreativeRotationType|null);

LineItem creativeRotationType

### creativeTargetings
    
    
    creativeTargetings?: (google.ads.admanager.v1.ICreativeTargeting[]|null);

LineItem creativeTargetings

### customFieldValues
    
    
    customFieldValues?: (google.ads.admanager.v1.ICustomFieldValue[]|null);

LineItem customFieldValues

### customPacingCurve
    
    
    customPacingCurve?: (google.ads.admanager.v1.ICustomPacingCurve|null);

LineItem customPacingCurve

### customVastExtension
    
    
    customVastExtension?: (string|null);

LineItem customVastExtension

### dealInfo
    
    
    dealInfo?: (google.ads.admanager.v1.ILineItemDealInfo|null);

LineItem dealInfo

### deliveryForecastSource
    
    
    deliveryForecastSource?: (google.ads.admanager.v1.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource|keyof typeof google.ads.admanager.v1.LineItemDeliveryForecastSourceEnum.LineItemDeliveryForecastSource|null);

LineItem deliveryForecastSource

### deliveryIndicator
    
    
    deliveryIndicator?: (google.ads.admanager.v1.IDeliveryIndicator|null);

LineItem deliveryIndicator

### deliveryRateType
    
    
    deliveryRateType?: (google.ads.admanager.v1.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType|keyof typeof google.ads.admanager.v1.LineItemDeliveryRateTypeEnum.LineItemDeliveryRateType|null);

LineItem deliveryRateType

### discount
    
    
    discount?: (google.ads.admanager.v1.ILineItemDiscount|null);

LineItem discount

### displayName
    
    
    displayName?: (string|null);

LineItem displayName

### effectiveAppliedLabels
    
    
    effectiveAppliedLabels?: (google.ads.admanager.v1.IAppliedLabel[]|null);

LineItem effectiveAppliedLabels

### endTime
    
    
    endTime?: (google.protobuf.ITimestamp|null);

LineItem endTime

### endTimeUnlimited
    
    
    endTimeUnlimited?: (boolean|null);

LineItem endTimeUnlimited

### environmentType
    
    
    environmentType?: (google.ads.admanager.v1.EnvironmentTypeEnum.EnvironmentType|keyof typeof google.ads.admanager.v1.EnvironmentTypeEnum.EnvironmentType|null);

LineItem environmentType

### externalLineItemId
    
    
    externalLineItemId?: (string|null);

LineItem externalLineItemId

### frequencyCaps
    
    
    frequencyCaps?: (google.ads.admanager.v1.IFrequencyCap[]|null);

LineItem frequencyCaps

### goal
    
    
    goal?: (google.ads.admanager.v1.IGoal|null);

LineItem goal

### grpSettings
    
    
    grpSettings?: (google.ads.admanager.v1.IGrpSettings|null);

LineItem grpSettings

### lineItemType
    
    
    lineItemType?: (google.ads.admanager.v1.LineItemTypeEnum.LineItemType|keyof typeof google.ads.admanager.v1.LineItemTypeEnum.LineItemType|null);

LineItem lineItemType

### maxVideoCreativeDuration
    
    
    maxVideoCreativeDuration?: (google.protobuf.IDuration|null);

LineItem maxVideoCreativeDuration

### missingCreatives
    
    
    missingCreatives?: (boolean|null);

LineItem missingCreatives

### name
    
    
    name?: (string|null);

LineItem name

### notes
    
    
    notes?: (string|null);

LineItem notes

### order
    
    
    order?: (string|null);

LineItem order

### orderDisplayName
    
    
    orderDisplayName?: (string|null);

LineItem orderDisplayName

### priority
    
    
    priority?: (number|null);

LineItem priority

### rate
    
    
    rate?: (google.type.IMoney|null);

LineItem rate

### repeatedCreativeServingEnabled
    
    
    repeatedCreativeServingEnabled?: (boolean|null);

LineItem repeatedCreativeServingEnabled

### reservationStatus
    
    
    reservationStatus?: (google.ads.admanager.v1.LineItemReservationStatusEnum.LineItemReservationStatus|keyof typeof google.ads.admanager.v1.LineItemReservationStatusEnum.LineItemReservationStatus|null);

LineItem reservationStatus

### reserveOnCreation
    
    
    reserveOnCreation?: (boolean|null);

LineItem reserveOnCreation

### roadblockingType
    
    
    roadblockingType?: (google.ads.admanager.v1.RoadblockingTypeEnum.RoadblockingType|keyof typeof google.ads.admanager.v1.RoadblockingTypeEnum.RoadblockingType|null);

LineItem roadblockingType

### sameAdvertiserExceptionEnabled
    
    
    sameAdvertiserExceptionEnabled?: (boolean|null);

LineItem sameAdvertiserExceptionEnabled

### secondaryGoals
    
    
    secondaryGoals?: (google.ads.admanager.v1.IGoal[]|null);

LineItem secondaryGoals

### skipCrossSellingRuleWarningChecks
    
    
    skipCrossSellingRuleWarningChecks?: (boolean|null);

LineItem skipCrossSellingRuleWarningChecks

### skipInventoryCheck
    
    
    skipInventoryCheck?: (boolean|null);

LineItem skipInventoryCheck

### skippableAdType
    
    
    skippableAdType?: (google.ads.admanager.v1.SkippableAdTypeEnum.SkippableAdType|keyof typeof google.ads.admanager.v1.SkippableAdTypeEnum.SkippableAdType|null);

LineItem skippableAdType

### sponsorshipExclusivityEnabled
    
    
    sponsorshipExclusivityEnabled?: (boolean|null);

LineItem sponsorshipExclusivityEnabled

### startTime
    
    
    startTime?: (google.protobuf.ITimestamp|null);

LineItem startTime

### stats
    
    
    stats?: (google.ads.admanager.v1.ILineItemStats|null);

LineItem stats

### status
    
    
    status?: (google.ads.admanager.v1.LineItemComputedStatusEnum.LineItemComputedStatus|keyof typeof google.ads.admanager.v1.LineItemComputedStatusEnum.LineItemComputedStatus|null);

LineItem status

### targetEndTime
    
    
    targetEndTime?: (google.protobuf.ITimestamp|null);

LineItem targetEndTime

### targeting
    
    
    targeting?: (google.ads.admanager.v1.ITargeting|null);

LineItem targeting

### thirdPartyMeasurementSettings
    
    
    thirdPartyMeasurementSettings?: (google.ads.admanager.v1.IThirdPartyMeasurementSettings|null);

LineItem thirdPartyMeasurementSettings

### updateSource
    
    
    updateSource?: (string|null);

LineItem updateSource

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

LineItem updateTime

### valueCpm
    
    
    valueCpm?: (google.type.IMoney|null);

LineItem valueCpm

### viewabilityProviderCompanies
    
    
    viewabilityProviderCompanies?: (string[]|null);

LineItem viewabilityProviderCompanies

### webPropertyCode
    
    
    webPropertyCode?: (string|null);

LineItem webPropertyCode

### youtubeKidsRestricted
    
    
    youtubeKidsRestricted?: (boolean|null);

LineItem youtubeKidsRestricted

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
