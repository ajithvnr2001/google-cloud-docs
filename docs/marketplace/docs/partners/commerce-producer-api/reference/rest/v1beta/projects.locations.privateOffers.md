---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers
title: REST Resource: projects.locations.privateOffers \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:13.252135+00:00
---

# REST Resource: projects.locations.privateOffers  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.privateOffers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PrivateOffer
    * JSON representation
  * SingleProductOffer
    * JSON representation
  * StandardIntervalPrice
    * JSON representation
  * StandardInterval
  * PriceModel
    * JSON representation
  * FlatFee
    * JSON representation
  * Commitment
    * JSON representation
  * Usage
    * JSON representation
  * SkuDiscount
    * JSON representation
  * CustomIntervalPrice
    * JSON representation
  * Installment
    * JSON representation
  * DateTime
    * JSON representation
  * TimeZone
    * JSON representation
  * Feature
    * JSON representation
  * ContractValue
    * JSON representation
  * RevenueShare
    * JSON representation
  * State
  * PublishRequirementGoogleReview
    * JSON representation
  * ResellerContact
    * JSON representation
  * OfferDealType
  * PartnerContact
    * JSON representation
  * Customer
    * JSON representation
  * Term
    * JSON representation
  * StartPolicy
  * EndPolicy
  * Methods



## Resource: PrivateOffer

Message describing PrivateOffer resource.

Note on OPTIONAL fields: To facilitate saving incomplete draft offers, most fields are categorized as OPTIONAL irrespective of whether they are necessary for a private offer to be valid. Many fields labeled OPTIONAL must be set to publish the offer.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#State)),
      "publishRequirementGoogleReview": {
        object ([PublishRequirementGoogleReview](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PublishRequirementGoogleReview))
      },
      "createTime": string,
      "updateTime": string,
      "publishTime": string,
      "acceptTime": string,
      "cancelTime": string,
      "endTime": string,
      "cancellationNote": string,
      "resellerContact": {
        object ([ResellerContact](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#ResellerContact))
      },
      "internalNote": string,
      "offerDealType": enum ([OfferDealType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#OfferDealType)),
      "title": string,
      "customerNote": string,
      "partnerContact": {
        object ([PartnerContact](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PartnerContact))
      },
      "customer": {
        object ([Customer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Customer))
      },
      "acceptDeadlineTime": {
        object ([DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime))
      },
      "term": {
        object ([Term](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Term))
      },
    
      // Union field content can be only one of the following:
      "singleProductOffer": {
        object ([SingleProductOffer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#SingleProductOffer))
      }
      // End of list of possible types for union field content.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource.  
`state` |  `enum (`[State](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#State)`)` Output only. The state of the private offer.  
`publishRequirementGoogleReview` |  `object (`[PublishRequirementGoogleReview](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PublishRequirementGoogleReview)`)` Output only. Information about the Google review process. Present only when the offer is determined to require review by Google.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`publishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the offer transitioned to PUBLISHED state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`acceptTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the offer transitioned to ACCEPTED state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cancelTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the offer transited to CANCELLED state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the offer ended. This can only be set for offers with `ENDED` state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`cancellationNote` |  `string` Output only. Internal note supplied when the offer was cancelled. Present only for cancelled offers and only if a note was supplied.  
`resellerContact` |  `object (`[ResellerContact](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#ResellerContact)`)` Output only. Information about the reseller contact. Present only for offers created by a reseller.  
`internalNote` |  `string` Optional. Unstructured text content that is not visible to the customer. Intended to be used by partners for storing notes about the private offer. Maximum length: 1500 characters.  
`offerDealType` |  `enum (`[OfferDealType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#OfferDealType)`)` Optional. The type of the deal transacted with the offer.The deal type is not visible to customers.Must be present to publish the offer.  
`title` |  `string` Optional. A title that describes the offer and helps your customers identify it. This title will be visible to the customer. Maximum length: 256 characters. Must be present to publish the offer.  
`customerNote` |  `string` Optional. Unstructured text content that is visible to the customer. Maximum length: 120 characters.  
`partnerContact` |  `object (`[PartnerContact](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PartnerContact)`)` Optional. Information about the partner contact. Must be provided when publishing the offer.  
`customer` |  `object (`[Customer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Customer)`)` Optional. Information identifying the intended recipient of the offer. Must be provided when publishing the offer.  
`acceptDeadlineTime` |  `object (`[DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime)`)` Optional. Deadline for acceptance of published offers. A published offer not accepted by this time will expire. Only day boundaries in the America/Los_Angeles time zone are supported. Must be present to publish the offer.When publishing an offer the deadline must be set to a time in the future not more than 3 months from the time of publishing. For example, if the offer is published on 03/05 at 1PM, then the deadline must be at or before 06/05 12AM America/Los_Angeles time.The deadline must also be:

  * Before or equal to the scheduled start time of this offer (if `term.scheduled_start_time` is set and the term's start policy is `SCHEDULED_START_TIME`).
  * Before or equal to the scheduled end time of this offer, if `term.scheduled_end_time` is set and the term's end policy is `SCHEDULED_END_TIME`.
  * Before or equal to the upcoming installment start times on this offer.
  * Before or equal to the amended offer's end time, if the offer amends another private or standard offer.
  * Before or equal to the start time of the next pending installment of the amended offer, if amending a private offer with custom installments. For example, if the amended offer has installments on 01/01, 02/01, 03/01, 04/01, and today is 02/15, then this offer's `acceptDeadlineTime` must be at or before 03/01.

In addition, if the offer amends another private offer, but there is already an accepted upcoming amendment against that private offer, then this deadline must be before or equal to the start time of the accepted upcoming offer. For example, today is 02/15, and this offer (offer C) amends private offer A, and private offer B has already been accepted which also amends private offer A. Private offer B has a start time of 03/01. Then this deadline must be at or before 03/01. Otherwise, on 03/01, private offer B would take effect, superseding offer A. This would mean offer C is no longer amending the currently active offer (Offer A), which is required for valid amendments.Once the offer is published, this field is still updatable to extend the deadline of the offer. However, the extension is still limited to be at most 3 months from the time of publishing.  
`term` |  `object (`[Term](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Term)`)` Optional. Configuration for the offer term. Must be set when publishing the offer.  
Union field `content`. The content for the offer. Additional forms of content may be supported in future. To publish the offer a content value must be provided. `content` can be only one of the following:  
`singleProductOffer` |  `object (`[SingleProductOffer](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#SingleProductOffer)`)` Optional. Configurations for the offer that is associated with a single product.  
  
## SingleProductOffer

Configurations for the offer that is associated with a single product.

JSON representation  
---  
      
    
    {
      "baseStandardOffer": string,
      "serviceLevel": string,
      "resellerPrivateOfferPlanId": string,
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Feature))
        }
      ],
      "effectiveInstallmentTimeline": [
        {
          object ([Installment](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Installment))
        }
      ],
      "contractValue": {
        object ([ContractValue](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#ContractValue))
      },
      "revenueShare": {
        object ([RevenueShare](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#RevenueShare))
      },
    
      // Union field amended_offer can be only one of the following:
      "amendedPrivateOffer": string,
      "amendedStandardOffer": string
      // End of list of possible types for union field amended_offer.
    
      // Union field price can be only one of the following:
      "standardIntervalPrice": {
        object ([StandardIntervalPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#StandardIntervalPrice))
      },
      "customIntervalPrice": {
        object ([CustomIntervalPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#CustomIntervalPrice))
      }
      // End of list of possible types for union field price.
    }  
  
Fields  
---  
`baseStandardOffer` |  `string` Optional. The StandardOffer this PrivateOffer is based on. Must be in the same project as the private offer, and must be effective at the time of publishing. Must be present to publish the offer.Format: projects/{project}/locations/{location}/services/{service}/standardOffers/{standard_offer}  
`serviceLevel` |  `string` Output only. The service level (also known as the 'plan') of the base standard offer. The value is populated at publish time from the base standard offer.  
`resellerPrivateOfferPlanId` |  `string` Output only. Present for offers created by a reseller from a reseller private offer plan (RPOP). When set, contains the ID of the originating RPOP. Not included for `PRIVATE_OFFER_VIEW_BASIC`.  
`features[]` |  `object (`[Feature](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Feature)`)` Optional. The custom product features to display for this offer. Feature `displayName` values must be unique to publish the offer. The set of features specified here should generally include all features included in the base service level, with optionally customized values, but is not required to match exactly and may include additional features.  
`effectiveInstallmentTimeline[]` |  `object (`[Installment](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Installment)`)` Output only. The effective installment timeline of the offer. Not included for `PRIVATE_OFFER_VIEW_BASIC`. Included for `PRIVATE_OFFER_VIEW_FULL` if all necessary information is available to generate the timeline, and if the offer has 'standardIntervalPrice' of 'MONTHLY_PRORATED', 'MONTHLY_NOT_PRORATED', 'QUARTERLY_NOT_PRORATED', or 'YEARLY_NOT_PRORATED'.  
`contractValue` |  `object (`[ContractValue](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#ContractValue)`)` Output only. Contract value of the offer. Not included for `PRIVATE_OFFER_VIEW_BASIC`.  
`revenueShare` |  `object (`[RevenueShare](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#RevenueShare)`)` Output only. Revenue share information for this Private Offer. Not included for `PRIVATE_OFFER_VIEW_BASIC`.  
Union field `amended_offer`. An existing offer to be superseded by this private offer. `amended_offer` can be only one of the following:  
`amendedPrivateOffer` |  `string` Optional. An existing private offer that will be superseded by this offer. Unless the private offer is for a product type that supports [multiple active orders](https://cloud.google.com/marketplace/docs/partners/offers/multiple-offers), an amendment private offer must be transacted if and only if the destination customer billing account already contains an active order for the same product. The offer to be superseded must be the offer associated with an active order.Amendments generally fall into one of two scenarios:

  1. **Active Order / Ended Offer** : The term of the amended offer has ended but it is still associated with an active order. The new offer must amend the ended private offer.
  2. **Active Order / Active Offer** : The term of the amended offer is still active and the associated order is active. Similar to above, the new offer must amend the currently active offer (unless "multiple active orders" are supported).

If this is set, then the `baseStandardOffer` parent service must match the parent service of the `baseStandardOffer` in the `amendedPrivateOffer`.**Active Term Restrictions** : If the term of the amended private offer has _NOT_ ended, then the following compatibility rules apply:

  * **Price Model Compatibility** : 
    * Flat Fee (with or without usage) offers can amend Flat Fee offers.
    * Usage-only or CUD offers can amend usage-only offers.
    * Commitment-based offers must amend offers of the same price model subtype (e.g., "additional usage at list price" vs "all usage discounted").
  * **Billing Frequency Compatibility** : Determined by `standardInterval` or `customIntervalPrice`. 
    * If the amended offer has a custom billing frequency, the new offer must also have a custom frequency.
    * If the amended offer has a standard frequency (Monthly, Quarterly, or Yearly), the new offer must maintain the same frequency or transition to a custom frequency.
    * Switching between different standard frequencies (e.g., Monthly to Quarterly) is not supported.
    * For Monthly frequency, switching between `MONTHLY_PRORATED` and `MONTHLY_NOT_PRORATED` is supported, unless the offer's `term.end_policy` is `MATCH_AMENDED_OFFER`.
    * For usage-only offers, there are no billing frequency restrictions.

Other criteria for offer amendment are detailed elsewhere.  
`amendedStandardOffer` |  `string` Optional. An existing standard offer that will be superseded by this offer. An amendment private offer must be transacted if the destination customer billing account already contains an active order for the same product, and otherwise cannot be transacted. The offer to be superseded must be the offer associated with the active order.If this is set, then the `baseStandardOffer` must contain the same parent service as the parent service of the `amendedStandardOffer`. The price model of this offer must be compatible with the price model of the `amendedStandardOffer`:

  * Flat Fee, or Flat Fee with usage offers can amend Flat Fee or Flat Fee with usage standard offers.
  * Usage-only offers, or CUD offers can amend usage-only standard offers.

Other criteria for offer amendment are detailed elsewhere.  
Union field `price`. The price of the offer. A price must be set when publishing the offer. `price` can be only one of the following:  
`standardIntervalPrice` |  `object (`[StandardIntervalPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#StandardIntervalPrice)`)` Optional. Price configurations for offers with standard intervals. A price must be set when publishing the offer.  
`customIntervalPrice` |  `object (`[CustomIntervalPrice](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#CustomIntervalPrice)`)` Optional. Price configurations for offers with custom intervals. Custom interval corresponds to "custom billing frequency", see <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule>. A price must be set when publishing the offer.  
  
## StandardIntervalPrice

Price configurations for offers with standard intervals.

JSON representation  
---  
      
    
    {
      "standardInterval": enum ([StandardInterval](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#StandardInterval)),
      "priceModel": {
        object ([PriceModel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PriceModel))
      }
    }  
  
Fields  
---  
`standardInterval` |  `enum (`[StandardInterval](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#StandardInterval)`)` Optional. The standard interval of the offer. Must be present to publish unless the price model is usage-only.  
`priceModel` |  `object (`[PriceModel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PriceModel)`)` Optional. The price model of the offer. Must be present to publish the offer.  
  
## StandardInterval

The options for offers with standard intervals.

Enums  
---  
`STANDARD_INTERVAL_UNSPECIFIED` | The private offer does not have an interval. If this is set, then the offer is "usage-only". Field `term.duration_months` must be positive.  
`MONTHLY_POSTPAY` | The schedule of the monthly postpay offers. This type of offer has "Monthly" billing frequency (see <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule)>. No longer supported as of May 2024. Cannot be used to publish new offers.This item is deprecated!  
`MONTHLY_PRORATED` | Monthly installments with proration. This type of offer has "Monthly" billing frequency (see <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule)>. For example, if the offer starts on 04/15, and the offer duration is 3 months, the following installments will be created: All dates represent the start of that day in the America/Los_Angeles time zone.If this is set:

  * The `PriceModel.subscription` oneof must be set.
  * Field `term.duration_months` must be positive.

  
`MONTHLY_NOT_PRORATED` | Monthly installments without proration. This type of offer has "Monthly" billing frequency (see <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule)>. For example, if the offer starts on 04/15, and the offer duration is 3 months, the following installments will be created: All dates represent the start of that day in the America/Los_Angeles time zone.If this is set:

  * The `PriceModel.subscription` oneof must be set.
  * Field `term.duration_months` must be positive.

  
`QUARTERLY_NOT_PRORATED` | Quarterly installments which are not prorated. This type of offer has "Quarterly" billing frequency (see <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule)>. For example, if the offer starts on 01/15, and the offer duration is 3 quarters, the following installments will be created: All dates represent the start of that day in the America/Los_Angeles time zone.If this is set:

  * The `PriceModel.subscription` oneof must be set.
  * Field `term.duration_months` must be positive.

  
`YEARLY_NOT_PRORATED` | Yearly installments which are not prorated. This type of offer has "Yearly" billing frequency (see <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-payment-schedule)>. For example, if the offer starts on 01/15/2025, and the offer duration is 3 years, the following installments will be created: All dates represent the start of that day in the America/Los_Angeles time zone.If this is set:

  * The `PriceModel.subscription` oneof must be set.
  * Field `term.duration_months` must be positive.

  
  
## PriceModel

The price model of the private offer.

Private offers are referred to as having different kinds of price models based on the combination of fields set in the price model. The following terminology is used in documentation and other reference material.

  * Usage-based: the price model does not set `flatFee`
  * Usage-only: the price model sets only `usage`
  * CUD (committed use discount): the price model sets `commitment`
    * Commitment discount with additional usage at list price: The price model sets `commitment` and not `usage`.
    * Commitment with all usage discounted: The price model sets `commitment` and `usage`.
  * Flat fee: the price model sets only `flatFee`
  * Flat fee with usage: the price model sets `flatFee` and `usage`



See <https://docs.cloud.google.com/marketplace/docs/partners/offers/select-pricing-model#CUD> for the price models.

JSON representation  
---  
      
    
    {
      "usage": {
        object ([Usage](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Usage))
      },
    
      // Union field subscription can be only one of the following:
      "flatFee": {
        object ([FlatFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#FlatFee))
      },
      "commitment": {
        object ([Commitment](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Commitment))
      }
      // End of list of possible types for union field subscription.
    }  
  
Fields  
---  
`usage` |  `object (`[Usage](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Usage)`)` Optional. The price configurations for the usage part. If this field is set, the `Commitment.discount_percent` must be unset. A private offer can apply a discount to all usage or to a usage commitment, but not both. Must be unset when the base standard offer's price model includes no usage SKUs.  
Union field `subscription`. The price configurations for the subscription part. `subscription` can be only one of the following:  
`flatFee` |  `object (`[FlatFee](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#FlatFee)`)` Optional. The price configurations for the flat fee subscription. Must be unset when the base standard offer's price model does not include subscription SKUs.  
`commitment` |  `object (`[Commitment](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Commitment)`)` Optional. The price configurations for the commitment based subscription. Must be unset when the base standard offer's price model includes subscription SKUs.  
  
## FlatFee

The price configurations for the flat fee subscriptions.

JSON representation  
---  
      
    
    {
      "flatFeeOverride": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
    }  
  
Fields  
---  
`flatFeeOverride` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Optional. Flat fee overriding the default flat fee in the base standard offer. Value cannot be negative. The currency must be "USD" and precision is limited to cents. Must be present to publish the offer, if the parent message is set. The maximum allowed value is 1,000,000,000 USD.  
  
## Commitment

The price configurations for the commitment based subscriptions.

JSON representation  
---  
      
    
    {
      "commitmentAmount": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      },
      "discountPercent": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      },
      "additionalCredit": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      },
      "discardPreviousCreditBalance": boolean
    }  
  
Fields  
---  
`commitmentAmount` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Optional. The commitment balance that the customer will receive. Value cannot be negative. The currency must be "USD" and precision is limited to cents. Must be present to publish the offer, if the parent message is set. The maximum allowed value is 1,000,000,000 USD.If the current offer amends a private offer where the term has not ended, and if the field `singleProductOffer.standard_interval_price.price_model.commitment.commitment_amount` is set on both the current offer and the amended private offer, then the commitment amount must be equal or higher on the current offer, compared to the amended private offer.  
`discountPercent` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Optional. The discount percent on `commitmentAmount`.For example, `10` means a discount of 10%. If the original `commitmentAmount` is $100 then the discounted amount will be $90. The customer is charged $90 and receives $100 in credits.All reported usage will be charged at the standard price. If this field is set, the `priceModel.usage` must be unset. A private offer can apply a discount to all usage or to a usage commitment, but not both.Must be between 0 and 100 inclusive, with precision up to 2 decimal places. If this field is set, then the allowed pattern for 'value' is `^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$`. Examples of valid values: "0", "100.0", "12.34", "40.0". Example of invalid values: ".3", "-1", "100.1", "12.345", "+12", "".Must be present to publish the offer.  
`additionalCredit` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Optional. Additional credit granted to the customer. Additional credits are only supported for custom interval offers. Equivalent behavior can be achieved for standard interval offers by varying the `commitmentAmount` and `discountPercent`.Value cannot be negative. The currency must be "USD" and precision is limited to cents. The maximum allowed value is 1,000,000 USD.  
`discardPreviousCreditBalance` |  `boolean` Optional. Whether to discard the previous credit balance when the associated installment starts. If not set, the previous credit balance will be rolled over to the current installment.If there are no previous installments, then the value of this field will not matter - since it has no effect when no credits exist.  
  
## Usage

The price for the usage SKUs.

JSON representation  
---  
      
    
    {
      "defaultDiscountPercent": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      },
      "skuDiscounts": [
        {
          object ([SkuDiscount](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#SkuDiscount))
        }
      ]
    }  
  
Fields  
---  
`defaultDiscountPercent` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Optional. The default discount percent for usage SKUs. An unset default discount percent is equivalent to 0 (no discount).Must be between 0 and 100 inclusive, with precision up to 2 decimal places. If this field is set, then the allowed pattern for 'value' is `^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$`. Examples of valid values: "0", "100.0", "12.34", "40.0". Example of invalid values: ".3", "-1", "100.1", "12.345", "+12", "".  
`skuDiscounts[]` |  `object (`[SkuDiscount](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#SkuDiscount)`)` Optional. The discounts for the specific SKUs that override the `defaultDiscountPercent`.  
  
## SkuDiscount

The discount for a specific SKU.

JSON representation  
---  
      
    
    {
    
      // Union field target can be only one of the following:
      "sku": string,
      "cloudBillingSku": string
      // End of list of possible types for union field target.
    
      // Union field discount can be only one of the following:
      "discountPercent": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      }
      // End of list of possible types for union field discount.
    }  
  
Fields  
---  
Union field `target`. Required. The SKU to which the discount applies. `target` can be only one of the following:  
`sku` |  `string` Optional. The name of a partner SKU from this API.Must refer to a SKU in the price model of the base standard offer. Inclusion in the base price model can occur either directly or indirectly via inclusion in an included SkuGroup.Currently, standard offer price models include only partner SKUs in the same project as the standard offer. This may change.Format: projects/{project}/locations/{location}/services/{service}/skus/{sku}  
`cloudBillingSku` |  `string` Optional. The name of a Google SKU from the Cloud Billing API.Used for partner products sold by Google, such as Premium Operating System Images sold for use in Compute Engine. This is not common. SKUs of this type are not present on this API and can instead be found on the Cloud Billing API or at <https://cloud.google.com/skus>.Must refer to a SKU in the price model of the base standard offer. Google SKUs are always referenced in standard offers via SkuGroups.Format: services/{service}/skus/{sku}  
Union field `discount`. The discount for the SKU. `discount` can be only one of the following:  
`discountPercent` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Optional. The discount percent for the SKU. For example, `10` means a discount of 10%. If the original SKU price is $100/hour then the discounted price will be $90/hour.Must be between 0 and 100 inclusive, with precision up to 2 decimal places. If this field is set, then the allowed pattern for 'value' is `^([0-9]{1,2}(\\.\\d{1,2})?|100(\\.0{1,2})?)$`.Examples of valid values: "0", "100.0", "12.34", "40.0". Example of invalid values: ".3", "-1", "100.1", "12.345", "+12", and "". Must be present to publish the offer.  
  
## CustomIntervalPrice

Price configurations for offers with custom intervals.

JSON representation  
---  
      
    
    {
      "installments": [
        {
          object ([Installment](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Installment))
        }
      ]
    }  
  
Fields  
---  
`installments[]` |  `object (`[Installment](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#Installment)`)` Optional. The installments that make up the installment timeline. All installments must have the same form of price model (e.g. all commitment, or all flat fee). A subscription must be present under the price model for every installment.Must contain at least one installment to publish the offer.  
  
## Installment

An installment of the offer.

JSON representation  
---  
      
    
    {
      "startTime": {
        object ([DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime))
      },
      "priceModel": {
        object ([PriceModel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PriceModel))
      }
    }  
  
Fields  
---  
`startTime` |  `object (`[DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime)`)` Optional. The start time of the installment. Each installment must have a unique start time with one exception: When the `term.start_policy` of the offer's term is `IMMEDIATE`, the `startTime` of the first installment must be unset. The actual start time is not recorded in the offer and instead is determined by the time the resulting order became active.When the `term.start_policy` of the offer's term is `SCHEDULED_START_TIME`, then the first installment's `startTime` must match `term.scheduled_start_time`.If the `term.end_policy` of the offer's term is `SCHEDULED_END_TIME`, then installment `startTime` must be before `term.scheduled_end_time`. If it's `AFTER_DURATION`, then installment `startTime` must be before the time calculated by adding the `term.duration_months` to the start time of the offer.The `startTime` of the installments cannot be before the `acceptDeadlineTime` of the offer.Installment start times must be in strictly increasing chronological order.  
`priceModel` |  `object (`[PriceModel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#PriceModel)`)` Optional. The price model of the installment. All installments must have the same form of price model.  
  
## DateTime

Represents civil time (or occasionally physical time).

This type can represent a civil time in one of a few possible ways:

  * When utcOffset is set and timeZone is unset: a civil time on a calendar day with a particular offset from UTC.
  * When timeZone is set and utcOffset is unset: a civil time on a calendar day in a particular time zone.
  * When neither timeZone nor utcOffset is set: a civil time on a calendar day in local time.



The date is relative to the Proleptic Gregorian Calendar.

If year, month, or day are 0, the DateTime is considered not to have a specific year, month, or day respectively.

This type may also be used to represent a physical time if all the date and time fields are set and either case of the `time_offset` oneof is set. Consider using `Timestamp` message for physical time instead. If your use case also would like to store the user's timezone, that can be done in another field.

This type is more flexible than some applications may want. Make sure to document and validate your application's limitations.

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer,
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer,
    
      // Union field time_offset can be only one of the following:
      "utcOffset": string,
      "timeZone": {
        object ([TimeZone](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#TimeZone))
      }
      // End of list of possible types for union field time_offset.
    }  
  
Fields  
---  
`year` |  `integer` Optional. Year of date. Must be from 1 to 9999, or 0 if specifying a datetime without a year.  
`month` |  `integer` Optional. Month of year. Must be from 1 to 12, or 0 if specifying a datetime without a month.  
`day` |  `integer` Optional. Day of month. Must be from 1 to 31 and valid for the year and month, or 0 if specifying a datetime without a day.  
`hours` |  `integer` Optional. Hours of day in 24 hour format. Should be from 0 to 23, defaults to 0 (midnight). An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Optional. Minutes of hour of day. Must be from 0 to 59, defaults to 0.  
`seconds` |  `integer` Optional. Seconds of minutes of the time. Must normally be from 0 to 59, defaults to 0. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Optional. Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999, defaults to 0.  
Union field `time_offset`. Optional. Specifies either the UTC offset or the time zone of the DateTime. Choose carefully between them, considering that time zone data may change in the future (for example, a country modifies their DST start/end dates, and future DateTimes in the affected range had already been stored). If omitted, the DateTime is considered to be in local time. `time_offset` can be only one of the following:  
`utcOffset` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` UTC offset. Must be whole seconds, between -18 hours and +18 hours. For example, a UTC offset of -4:00 would be represented as { seconds: -14400 }.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeZone` |  `object (`[TimeZone](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#TimeZone)`)` Time zone.  
  
## TimeZone

Represents a time zone from the [IANA Time Zone Database](https://www.iana.org/time-zones).

JSON representation  
---  
      
    
    {
      "id": string,
      "version": string
    }  
  
Fields  
---  
`id` |  `string` IANA Time Zone Database time zone. For example "America/New_York".  
`version` |  `string` Optional. IANA Time Zone Database version number. For example "2019a".  
  
## Feature

Additional details used to describe customization of the service level.

Features are used to distinguish service levels of the same product. When a product has a single service level, all details can be contained in the product documentation. When a product has multiple service levels, each service level can be assigned a distinct set of features to distinguish the key differences between the service levels.

In addition to customizing pricing and other transaction details, a private offer may include customization of partner-managed product behavior. When this is the case, the details of the custom behavior are described using features.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "value": string
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Human readable display text characterizing the feature. Should be sufficiently detailed to identify the feature, allowing features to be correlated across separate offers and service levels. Must be non-empty to publish the offer. The maximum allowed length is 128 characters. Allows characters from the following Unicode Property Classes: Letters, Numbers, Punctuation, Symbols, and Separators  
`value` |  `string` Optional. Human readable display text reflecting the value of the feature. Used for variable features not captured by the displayName alone. The maximum allowed length is 3000 characters. Allows characters from the following Unicode Property Classes: Letters, Numbers, Punctuation, Symbols, and Separators  
  
## ContractValue

The contract value of the offer.

JSON representation  
---  
      
    
    {
      "totalContractValue": {
        object ([Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money))
      }
    }  
  
Fields  
---  
`totalContractValue` |  `object (`[Money](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Money)`)` Output only. The total contract value of the offer. This will be set for all non-draft private offers, as long as 'PRIVATE_OFFER_VIEW_FULL' is requested. For DRAFT private offers, this will be populated only when the end user's billing account is set and when the pricing and term configuration is sufficiently complete to allow for a calculation.  
  
## RevenueShare

Revenue Share information for a Private Offer. For more details about the revenue share, including how the value is determined, see <https://docs.cloud.google.com/marketplace/docs/partners/revenue-share-scenarios>.

Not included for `PRIVATE_OFFER_VIEW_BASIC`, or for DRAFT private offers.

For non-draft private offers, these fields are populated based on the following:

  * Offers published after April 20, 2025 will always have revenue share fields populated.
  * Offers published on or before April 20, 2025 will only have revenue share fields populated if they were associated with an active, unexpired order on that date.

JSON representation  
---  
      
    
    {
      "currentTermVendorNetRevenuePercent": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      },
      "renewalTermVendorNetRevenuePercent": {
        object ([Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal))
      }
    }  
  
Fields  
---  
`currentTermVendorNetRevenuePercent` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Output only. The revenue share currently in effect.The range of the value is between 0 and 100. For example, 80 means the Vendor's current term revenue share is 80%. The vendor will keep 80% of the revenue. .  
`renewalTermVendorNetRevenuePercent` |  `object (`[Decimal](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/Decimal)`)` Output only. The expected revenue share for the renewal term. Not included if the offer does not have renewal terms.The range of the value is between 0 and 100. For example, 80 means the Vendor's current term revenue share is 80%. The vendor will keep 80% of the revenue after renewal. .  
  
## State

State of an offer.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`DRAFT` | The default state after creation when the offer can be edited. In all other states, the contents of the offer cannot be edited.  
`PUBLISHING` | The offer is publishing. Publishing will complete when all publishing requirements are satisfied.  
`PUBLISHED` | The offer has been published and is available to the customer to accept.  
`ACCEPTED` | The offer has been accepted by the customer.  
`CANCELLED` | The offer was cancelled by the provider before it was transacted. Cancelled offers can no longer be accepted by the customer.  
`EXPIRED` | The offer expired without being accepted by the customer. Expired offers can no longer be accepted by the customer.  
`ENDED` | The offer has ended.Ended offers were accepted and active in the past, but have now reached the end of their term or have been terminated.  
  
## PublishRequirementGoogleReview

Information about the Google review process.

JSON representation  
---  
      
    
    {
      "reviewApproveTime": string
    }  
  
Fields  
---  
`reviewApproveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The approval time of the Google review process.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ResellerContact

Contact information for a reseller.

JSON representation  
---  
      
    
    {
      "contact": string,
      "email": string
    }  
  
Fields  
---  
`contact` |  `string` Output only. The name of the reseller contact for this offer.  
`email` |  `string` Output only. The email of the reseller contact for this offer.  
  
## OfferDealType

The type of the deal transacted with the offer. The deal type of an offer is a factor in determining the offer's revenue share.

Enums  
---  
`OFFER_DEAL_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`CHANNEL_SHIFT` | The offer corresponds to a preexisting commercial arrangement for a workload on Google Cloud that is being transferred to the Cloud Marketplace.  
`MIGRATION` | The offer corresponds to a preexisting commercial arrangement for a workload previously not on Google Cloud that is being transferred to Google Cloud.  
`NATIVE_RENEWAL` | The offer corresponds to a renewal of a deal initially transacted on the Google Cloud Marketplace.  
`NEW` | The offer corresponds to a new deal transacted on the Google Cloud Marketplace.This value is not allowed if the offer amends another private offer where the term has not ended, and the amended private offer has a deal type of `MIGRATION`, `CHANNEL_SHIFT` or `NATIVE_RENEWAL`.  
  
## PartnerContact

Contact information for the partner representative.

JSON representation  
---  
      
    
    {
      "contact": string,
      "email": string
    }  
  
Fields  
---  
`contact` |  `string` Optional. Display text identifying the partner sales contact. Displayed to the customer. Must be provided when publishing the offer. Maximum length: 256 characters.  
`email` |  `string` Optional. The email address of the partner sales contact. Displayed to the customer. The format of the provided email address is validated when publishing the offer, but no verification is performed that the email address actually exists, accepts email, or is otherwise functional.  
  
## Customer

Information about the customer.

JSON representation  
---  
      
    
    {
      "entityTitle": string,
      "contact": string,
      "email": string,
      "address": string,
      "targetBillingAccount": string
    }  
  
Fields  
---  
`entityTitle` |  `string` Optional. A string identifying the customer's entity (for example, the customer's organization or company name). Must be provided when publishing the offer. Maximum length: 256 characters.  
`contact` |  `string` Optional. A string identifying the customer contact. Must be provided when publishing the offer. Maximum length: 256 characters.  
`email` |  `string` Optional. Email of customer contact. If provided, it must be a well-formed email address.  
`address  
**(deprecated)**` |  `string` This item is deprecated!Output only. Legal address of the customer organization. This field can no longer be set, but it is preserved to return the data from existing offers where address is set.  
`targetBillingAccount` |  `string` Optional. The customer's billing account targeted by the offer. The private offer once published can be accepted by a billing administrator of the target billing account. If the customer accepts the offer and later moves the resulting order to a new billing account, this field will continue to reflect the original billing account to which the private offer was extended. Must be provided when publishing the offer.To publish this private offer:

  * The billing account must exist.
  * The billing account must not be in a free trial.
  * The billing account must comply with Marketplace Reselling Policies.
  * Reseller parent billing accounts are prohibited. Reseller subaccounts are prohibited unless the service is enabled for reselling.

Format: billingAccounts/012345-567890-ABCDEF  
  
## Term

Configurations for the offer term and renewal options. Extending a private offer to a customer that covers a given term constitutes a guarantee to the customer that the product will remain available to them for the duration of the term.

JSON representation  
---  
      
    
    {
      "startPolicy": enum ([StartPolicy](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#StartPolicy)),
      "scheduledStartTime": {
        object ([DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime))
      },
      "endPolicy": enum ([EndPolicy](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#EndPolicy)),
      "effectiveTermEndTime": {
        object ([DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime))
      },
    
      // Union field end_policy_data can be only one of the following:
      "durationMonths": integer,
      "scheduledEndTime": {
        object ([DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime))
      }
      // End of list of possible types for union field end_policy_data.
    
      // Union field renewal can be only one of the following:
      "maxRenewalCount": integer,
      "unlimitedRenewal": boolean
      // End of list of possible types for union field renewal.
    }  
  
Fields  
---  
`startPolicy` |  `enum (`[StartPolicy](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#StartPolicy)`)` Optional. Defines when the resulting order should start. Must be set when publishing the offer.  
`scheduledStartTime` |  `object (`[DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime)`)` Optional. The scheduled start time of the offer. Cannot exceed one year from the time of publish.If the start policy is `SCHEDULED_START_TIME`, a future time at a day boundary in the America/Los_Angeles time zone must be provided when publishing the offer.If the offer amends another private or standard offer, then the scheduled start time must be:

  * Before or equal to the amended offer's end time if the offer's end policy is not MATCH_AMENDED_OFFER. Otherwise, it has to be strictly before the amended offer's end time.
  * Before or equal to the start time of the next pending installment of the amended offer, if amending a private offer with custom installments. For example, if the amended offer has installments on 01/01, 02/01, 03/01, 04/01, and today is 02/15, then the new offer's `scheduledStartTime` must be at or before 03/01.

  
`endPolicy` |  `enum (`[EndPolicy](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#EndPolicy)`)` Optional. Defines when an offer should end. Must be set when publishing the offer.  
`effectiveTermEndTime` |  `object (`[DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime)`)` Output only. The expected end time of the current offer term.At the end of each offer term, an offer associated with an active order will either renew or end. When an offer renews, a new term begins and this value changes to reflect the end time of the new term. When an offer ends this value is no longer set and instead `endTime` is set.When the term of an offer ends and the offer does not renew, the associated order also ends if the base standard offer has a subscription price model. Otherwise, the associated order does not end and remains active.Not included for PRIVATE_OFFER_VIEW_BASIC. Included for PRIVATE_OFFER_VIEW_FULL when the offer has not ended and either the offer has started or the value can be derived from other fields.For offers that have not started, this field is set when one of the following conditions is true.

  * The offer sets `term.scheduled_end_time`.
  * The offer sets `term.scheduled_start_time` and `term.duration_months`, the offer's `term.end_policy` is not `MATCH_AMENDED_OFFER`, and the offer does not have standardInterval set to `MONTHLY_POSTPAY`.

  
Union field `end_policy_data`. Extra data for the end policy. `end_policy_data` can be only one of the following:  
`durationMonths` |  `integer` Optional. Duration in months of the offer term. The offer will end on the same day of the month after this duration. If that date is not available, the offer will end on the last day of the month. For example, if the offer starts on 01/31/2024 and the duration is 13 months, the offer will end on 02/28/2025. Must be set to publish the offer if the end policy is `AFTER_DURATION` or `MATCH_AMENDED_OFFER`, and must be a positive value.The maximum possible offer duration, including all renewal terms, cannot exceed 7 years. For example, if `durationMonths` is 9 and `term.max_renewal_count` is 9, then the maximum possible offer duration is 90 months and exceeds the 7 year limit.  
`scheduledEndTime` |  `object (`[DateTime](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers#DateTime)`)` Optional. Specified end time of the offer. Must be set to publish the offer if the end policy is `SCHEDULED_END_TIME`. When set, the time must be in the future and at a day boundary in the America/Los_Angeles time zone, and must be after `term.scheduled_start_time` if applicable.  
Union field `renewal`. Defines the renewal policy for the offer. `renewal` can be only one of the following:  
`maxRenewalCount` |  `integer` Optional. The max number of renewals allowed, after the initial term ends. This field is only relevant to standard interval offers with interval of 'MONTHLY_PRORATED', 'MONTHLY_NOT_PRORATED', 'QUARTERLY_NOT_PRORATED' or 'YEARLY_NOT_PRORATED'. Other types of offers cannot be renewed.For example, if the initial term is 1 year and the max renewals is 3, the customer can renew the offer for up to 3 additional years after the initial term ends. Customers control whether they renew the offer.Allowing a customer to renew an offer does not constitute a guarantee to the customer that the offered product will still be available to be renewed at the renewal date.An offer with a max renewal count of 0 cannot be renewed. Must be non-negative.  
`unlimitedRenewal  
**(deprecated)**` |  `boolean` This item is deprecated!Output only. Deprecated: This field can only be true on existing offers with standard interval of 'MONTHLY_POSTPAY'. As of May 2024, we no longer allow unlimited renewals.  
  
## StartPolicy

Defines when an offer should start.

Enums  
---  
`START_POLICY_UNSPECIFIED` | Default value. This value is unused.  
`IMMEDIATE` | The resulting order starts immediately upon the customer's acceptance of the offer, if no partner approval is required, or else immediately after the partner approves the purchase if order approval is required. This enum value cannot be combined with `term.scheduled_start_time`.  
`SCHEDULED_START_TIME` | The resulting order starts at the scheduled start time.  
  
## EndPolicy

Defines when an offer should end.

Enums  
---  
`END_POLICY_UNSPECIFIED` | Default value. This value is unused.  
`AFTER_DURATION` | Offer ends after the specified duration. If this is set, then `durationMonths` must be positive.  
`SCHEDULED_END_TIME` | Offer ends at the schduled time.  
`MATCH_AMENDED_OFFER` | Offer coterms to the amended offer - the offer ends at the end of the amended offer's termFor example, if the amended offer starts on 01/15/24, and has a duration of 6 months, then it ends on 07/15/24. If the current offer coterms to the previous offer, and the current offer starts on 05/06/24, then it will still end on 07/15/24. Assuming the current offer renews 3 times, then the terms on the current offer will be:

  1. 05/06/24 - 07/15/24 (First term, ends on 07/15 to coterm with the amended offer)
  2. 07/15/24 - 01/15/25 (First renewal term)
  3. 01/15/25 - 07/15/25 (Second renewal term)
  4. 07/15/25 - 01/15/26 (Third renewal term)

As a contrast, if the current offer does not coterm with the amended offer (such as when `endPolicy` is `AFTER_DURATION`), then the terms will be:

  1. 05/06/24 - 11/06/24 (First term, ends on 11/06, no coterming)
  2. 11/06/24 - 05/06/25 (First renewal term)
  3. 05/06/25 - 11/06/25 (Second renewal term)
  4. 11/06/25 - 05/06/26 (Third renewal term)

If this is set, then the following conditions must be met:

  * `singleProductOffer.amended_private_offer` must be set, and the amended private offer must not be ended.
  * The proration policy must not change (e.g., you cannot switch between `MONTHLY_PRORATED` and `MONTHLY_NOT_PRORATED`).
  * The current offer must not have custom intervals (where `customIntervalPrice` is set).
  * `term.duration_months` must match the amended private offer's duration.
  * The amended private offer must not have a standard interval of `MONTHLY_POSTPAY`.

This is currently not supported.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/cancel)`

|  Cancels the target PrivateOffer.  
  
### `[create](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/create)`

|  Creates a new PrivateOffer in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/delete)`

|  Deletes the target PrivateOffer.  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/get)`

|  Gets details of a single PrivateOffer.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/list)`

|  Lists PrivateOffers for the given parent.  
  
### `[patch](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/patch)`

|  Updates the target PrivateOffer.  
  
### `[publish](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/publish)`

|  Publishes the target PrivateOffer.  
  
### `[resolveAmendmentTarget](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.privateOffers/resolveAmendmentTarget)`

|  Resolves the existing offer that must be amended when creating a new PrivateOffer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-13 UTC."],[],[]] 
