---
url: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks
title: REST Resource: accounts.channelPartnerLinks \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:44:29.825834+00:00
---

# REST Resource: accounts.channelPartnerLinks  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  REST Resource: accounts.channelPartnerLinks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ChannelPartnerLink
    * JSON representation
  * ChannelPartnerLinkState
  * PartnerAdvantageInfo
    * JSON representation
  * ProductAuthorization
    * JSON representation
  * SellType
  * AuthorizedProductFamily
  * Region
  * State
  * Methods



## Resource: ChannelPartnerLink

Entity representing a link between distributors and their indirect resellers in an n-tier resale channel.

JSON representation  
---  
      
    
    {
      "name": string,
      "resellerCloudIdentityId": string,
      "linkState": enum ([ChannelPartnerLinkState](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#ChannelPartnerLinkState)),
      "inviteLinkUri": string,
      "createTime": string,
      "updateTime": string,
      "publicId": string,
      "channelPartnerCloudIdentityInfo": {
        object ([CloudIdentityInfo](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/CloudIdentityInfo))
      },
      "partnerAdvantageInfo": {
        object ([PartnerAdvantageInfo](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#PartnerAdvantageInfo))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Resource name for the channel partner link, in the format accounts/{account_id}/channelPartnerLinks/{id}.  
`resellerCloudIdentityId` |  `string` Required. Cloud Identity ID of the linked reseller.  
`linkState` |  `enum (`[ChannelPartnerLinkState](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#ChannelPartnerLinkState)`)` Required. State of the channel partner link.  
`inviteLinkUri` |  `string` Output only. URI of the web page where partner accepts the link invitation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of when the channel partner link is created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp of when the channel partner link is updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`publicId` |  `string` Output only. Public identifier that a customer must use to generate a transfer token to move to this distributor-reseller combination.  
`channelPartnerCloudIdentityInfo` |  `object (`[CloudIdentityInfo](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/CloudIdentityInfo)`)` Output only. Cloud Identity info of the channel partner (IR).  
`partnerAdvantageInfo` |  `object (`[PartnerAdvantageInfo](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#PartnerAdvantageInfo)`)` Output only. Partner Advantage information for this Channel Partner (IR).  
  
## ChannelPartnerLinkState

ChannelPartnerLinkState represents state of a channel partner link.

Enums  
---  
`CHANNEL_PARTNER_LINK_STATE_UNSPECIFIED` | Not used.  
`INVITED` | An invitation has been sent to the reseller to create a channel partner link.  
`ACTIVE` | Status when the reseller is active.  
`REVOKED` | Status when the reseller has been revoked by the distributor.  
`SUSPENDED` | Status when the reseller is suspended by Google or distributor.  
  
## PartnerAdvantageInfo

Partner Advantage information for a Channel Partner.

JSON representation  
---  
      
    
    {
      "productAuthorization": [
        {
          object ([ProductAuthorization](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#ProductAuthorization))
        }
      ]
    }  
  
Fields  
---  
`productAuthorization[]` |  `object (`[ProductAuthorization](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#ProductAuthorization)`)` A list of this Channel Partner's product authorizations.  
  
## ProductAuthorization

The product and region pairs that a reseller may be authorized to sell.

JSON representation  
---  
      
    
    {
      "sellType": enum ([SellType](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#SellType)),
      "authorizedProductFamily": enum ([AuthorizedProductFamily](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#AuthorizedProductFamily)),
      "region": enum ([Region](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#Region)),
      "state": enum ([State](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#State))
    }  
  
Fields  
---  
`sellType` |  `enum (`[SellType](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#SellType)`)` The type of reseller this ProductAuthorization corresponds to.  
`authorizedProductFamily` |  `enum (`[AuthorizedProductFamily](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#AuthorizedProductFamily)`)` The family of Google products that the reseller may be authorized to sell.  
`region` |  `enum (`[Region](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#Region)`)` The region where this reseller is authorized to sell this product family.  
`state` |  `enum (`[State](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#State)`)` The state of this product authorization.  
  
## SellType

The type of reseller this ProductAuthorization corresponds to.

Enums  
---  
`SELL_TYPE_UNSPECIFIED` | Default value. Does not display if there are no errors.  
`ONE_TIER` | Reseller sells directly through Google.  
`TWO_TIER` | Reseller sells through a distributor.  
  
## AuthorizedProductFamily

The family of Google products that the reseller may be authorized to sell.

Enums  
---  
`AUTHORIZED_PRODUCT_FAMILY_UNSPECIFIED` | Default value. Does not display if there are no errors.  
`GOOGLE_CLOUD_PLATFORM` | Google Cloud  
`CHROME_ENTERPRISE` | Chrome. Deprecated: Use `[AuthorizedProductFamily.CHROME](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#AuthorizedProductFamily.ENUM_VALUES.CHROME)` instead.This item is deprecated!  
`GOOGLE_WORKSPACE` | Google Workspace  
`GOOGLE_MAPS_PLATFORM` | Google Maps  
`CHROME` | Chrome  
`GOOGLE_WORKSPACE_FOR_EDUCATION` | Google Workspace for Education  
  
## Region

The region where this reseller is authorized to sell this product family.

Enums  
---  
`REGION_UNSPECIFIED` | Default value. Does not display if there are no errors.  
`ANZ` | Australia & New Zealand  
`CEE` | Central & Eastern Europe  
`DACH` | Germany, Austria, & Switzerland  
`FRANCE` | France  
`GLOBAL` | Global  
`INDIA` | India  
`JAPAN` | Japan  
`LATAM_BRAZIL` | LATAM - Brazil  
`LATAM_SPANISH_SPEAKING` | LATAM - Spanish speaking  
`NE` | Northern Europe  
`NORTH_AMERICA` | North America  
`OTHER_ASIA_PACIFIC` | Other Asia Pacific  
`SEEMEA` | Southern Europe and Emerging Markets  
`UK_AND_I` | UK & Ireland  
  
## State

The state of this product authorization.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. Does not display if there are no errors.  
`INTERESTED` | The default status for an authorization. Stays set while the partner works on the authorization tasks.  
`ACTIVE` | Shows that the partner has completed their requisite tasks and can sell the product family in the corresponding region.  
`SUBMITTED` | Set when a partner submits the authorization for Google's review.  
`INACTIVE` | Used to indicate the authorization is no longer active.  
`SUSPENDED` | Used when a partner no longer meets the authorization requirements. Stays set while the partner works on meeting the requirements.  
`REJECTED` | Indicates that the application was rejected.  
`OFFBOARDING` | Used when the partner is no longer authorized to do business, regardless of reason.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks/create)`

|  Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel.  
  
### `[get](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks/get)`

|  Returns the requested `[ChannelPartnerLink](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#ChannelPartnerLink)` resource.  
  
### `[list](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks/list)`

|  List `[ChannelPartnerLink](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks#ChannelPartnerLink)`s belonging to a distributor.  
  
### `[patch](https://docs.cloud.google.com/channel/docs/reference/rest/v1alpha1/accounts.channelPartnerLinks/patch)`

|  Updates a channel partner link.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-03 UTC."],[],[]] 
