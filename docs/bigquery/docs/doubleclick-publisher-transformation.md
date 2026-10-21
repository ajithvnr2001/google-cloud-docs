---
url: https://docs.cloud.google.com/bigquery/docs/doubleclick-publisher-transformation/
title: Google Ad Manager report transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:12:01.287586+00:00
---

# Google Ad Manager report transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/doubleclick-publisher-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Ad Manager report transformation

When your Google Ad Manager (formerly known as DoubleClick for Publishers) data transfer files are transferred to BigQuery, the files are transformed into the BigQuery tables and views described in this document.

When you view the tables and views in BigQuery, the value for network_code is your Ad Manager network code.

## Data transfer files

The reports in the following sections provide detailed information about your Ad Manager network activity.

### Network requests

Ad Manager files: [NetworkRequests](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillRequests](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkRequests_network_code  
p_NetworkBackfillRequests_network_code
BigQuery views:
     NetworkRequests_network_code  
NetworkBackfillRequests_network_code

### Network code serves

Ad Manager files: [NetworkCodeServes](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillCodeServes](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkCodeServes  
p_NetworkBackfillCodeServes_network_code
BigQuery views:
     NetworkCodeServes  
NetworkBackfillCodeServes_network_code

### Network impressions

Ad Manager files: [NetworkImpressions](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillImpressions](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkImpressions_network_code  
p_NetworkBackfillImpressions_network_code
BigQuery views:
     NetworkImpressions_network_code  
NetworkBackfillImpressions_network_code

### Network clicks

Ad Manager files: [NetworkClicks](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillClicks](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkClicks_network_code  
p_NetworkBackfillClicks_network_code
BigQuery views:
     NetworkClicks_network_code  
NetworkBackfillClicks_network_code

### Network active views

Ad Manager files: [NetworkActiveViews](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillActiveViews](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkActiveViews_network_code  
p_NetworkBackfillActiveViews_network_code
BigQuery views:
     NetworkActiveViews_network_code  
NetworkBackfillActiveViews_network_code

### Network backfill bids

Ad Manager file: [NetworkBackfillBids](https://support.google.com/admanager/answer/1733124)

BigQuery table:
     p_NetworkBackfillBids_network_code
BigQuery view:
     NetworkBackfillBids_network_code

### Network video conversions

Ad Manager files: [NetworkVideoConversions](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillVideoConversions](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkVideoConversions_network_code  
p_NetworkBackfillVideoConversions_network_code
BigQuery views:
     NetworkVideoConversions_network_code  
NetworkBackfillVideoConversions_network_code

### Network rich media conversions

Ad Manager files: [NetworkRichMediaConversions](https://support.google.com/admanager/answer/1733124) and [NetworkBackfillRichMediaConversions](https://support.google.com/admanager/answer/1733124)

BigQuery tables:
     p_NetworkRichMediaConversions_network_code  
p_NetworkBackfillRichMediaConversions_network_code
BigQuery views:
     NetworkRichMediaConversions_network_code  
NetworkBackfillRichMediaConversions_network_code

### Network activities

Ad Manager file: [NetworkActivities](https://support.google.com/admanager/answer/1733124)

BigQuery table:
     p_NetworkActivities_network_code
BigQuery view:
     NetworkActivities_network_code

## Match tables

The tables in the following sections contain attribute fields and metadata for your account.

### Ad category

Ad Manager file: [AdCategory](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableAdCategory_network_code
BigQuery view:
    MatchTableAdCategory_network_code

### Ad unit

Ad Manager file: [AdUnit](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableAdUnit_network_code
BigQuery view:
    MatchTableAdUnit_network_code

### Audience segment

Ad Manager file: [AudienceSegment](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableAudienceSegment_network_code
BigQuery view:
    MatchTableAudienceSegment_network_code

### Audience segment category

Ad Manager file: [AudienceSegmentCategory](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableAudienceSegmentCategory_network_code
BigQuery view:
    MatchTableAudienceSegmentCategory_network_code

### Bandwidth group

Ad Manager file: [BandwidthGroup](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableBandwidthGroup_network_code
BigQuery view:
    MatchTableBandwidthGroup_network_code

### Browser

Ad Manager file: [Browser](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableBrowser_network_code
BigQuery view:
    MatchTableBrowser_network_code

### Browser language

Ad Manager file: [BrowserLanguage](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableBrowserLanguage_network_code
BigQuery view:
    MatchTableBrowserLanguage_network_code

### Company

Ad Manager file: [Company](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableCompany_network_code
BigQuery view:
    MatchTableCompany_network_code

### Device capability

Ad Manager file: [DeviceCapability](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableDeviceCapability_network_code
BigQuery view:
    MatchTableDeviceCapability_network_code

### Device category

Ad Manager file: [DeviceCategory](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableDeviceCategory_network_code
BigQuery view:
    MatchTableDeviceCategory_network_code

### Device manufacturer

Ad Manager file: [DeviceManufacturer](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableDeviceManufacturer_network_code
BigQuery view:
    MatchTableDeviceManufacturer_network_code

### Exchange rate (deprecated)

Ad Manager file: [ExchangeRate](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    None
BigQuery view:
    None

### Geo target

Ad Manager file: [GeoTarget](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableGeoTarget_network_code
BigQuery view:
    MatchTableGeoTarget_network_code

### Line item

Ad Manager file: [LineItem](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableLineItem_network_code
BigQuery view:
    MatchTableLineItem_network_code

### Mobile carrier

Ad Manager file: [MobileCarrier](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableMobileCarrier_network_code
BigQuery view:
    MatchTableMobileCarrier_network_code

### Mobile device

Ad Manager file: [MobileDevice](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableMobileDevice_network_code
BigQuery view:
    MatchTableMobileDevice_network_code

### Mobile device submodel

Ad Manager file: [MobileDeviceSubmodel](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableMobileDeviceSubmodel_network_code
BigQuery view:
    MatchTableMobileDeviceSubmodel_network_code

### Operating system

Ad Manager file: [OperatingSystem](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableOperatingSystem_network_code
BigQuery view:
    MatchTableOperatingSystem_network_code

### Operating system version

Ad Manager file: [OperatingSystemVersion](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableOperatingSystemVersion_network_code
BigQuery view:
    MatchTableOperatingSystemVersion_network_code

### Order

Ad Manager file: [Order](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableOrder_network_code
BigQuery view:
    MatchTableOrder_network_code

### Placement

Ad Manager file: [Placement](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTablePlacement_network_code
BigQuery view:
    MatchTablePlacement_network_code

### Programmatic buyer

Ad Manager file: [ProgrammaticBuyer](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableProgrammaticBuyer_network_code
BigQuery view:
    MatchTableProgrammaticBuyer_network_code

### Proposal retraction reason

Ad Manager file: [ProposalRetractionReason](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableProposalRetractionReason_network_code
BigQuery view:
    MatchTableProposalRetractionReason_network_code

### Third-party company

Ad Manager file: [ThirdPartyCompany](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableThirdPartyCompany_network_code
BigQuery view:
    MatchTableThirdPartyCompany_network_code

### Time zone

Ad Manager file: [TimeZone](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableTimeZone_network_code
BigQuery view:
    MatchTableTimeZone_network_code

### User

Ad Manager file: [User](https://developers.google.com/doubleclick-publishers/docs/pqlreference#matchtables)

BigQuery table:
    p_MatchTableUser_network_code
BigQuery view:
    MatchTableUser_network_code

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
