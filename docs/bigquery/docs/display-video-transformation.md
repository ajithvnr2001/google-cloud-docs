---
url: https://docs.cloud.google.com/bigquery/docs/display-video-transformation/
title: Display & Video 360 data transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:03:42.805360+00:00
---

# Display & Video 360 data transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/display-video-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Display & Video 360 data transformation

When your Display & Video 360 data are transferred to BigQuery, they are transformed into the following BigQuery tables and views.

When you view the tables and views in BigQuery, the value for displayvideo_id is your Display & Video 360 partner or advertiser ID.

**Display & Video 360 resource** | **BigQuery table** | **BigQuery view**  
---|---|---  
**Data Transfer files**  
[Impression](https://developers.google.com/bid-manager/dtv2/reference/file-format) | p_Impression_displayvideo_id | Impression_displayvideo_id  
[Click](https://developers.google.com/bid-manager/dtv2/reference/file-format) | p_Click_displayvideo_id | Click_displayvideo_id  
[Activity](https://developers.google.com/bid-manager/dtv2/reference/file-format) | p_Activity_displayvideo_id | Activity_displayvideo_id  
**DV360 API Resource (v3)**  
[Partner](https://developers.google.com/display-video/api/reference/rest/v3/partners#resource:-partner) | p_Partner_displayvideo_id | Partner_displayvideo_id  
[Advertiser](https://developers.google.com/display-video/api/reference/rest/v3/advertisers#resource:-advertiser) | p_Advertiser_displayvideo_id | Advertiser_displayvideo_id  
[LineItem](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.lineItems#LineItem) | p_LineItem_displayvideo_id | LineItem_displayvideo_id  
[LineItemTargeting](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.lineItems/bulkListAssignedTargetingOptions#LineItemAssignedTargetingOption) | p_LineItemTargeting_displayvideo_id | LineItemTargeting_displayvideo_id  
[Campaign](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.campaigns#Campaign) | p_Campaign_displayvideo_id | Campaign_displayvideo_id  
[CampaignTargeting](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.campaigns.targetingTypes.assignedTargetingOptions#AssignedTargetingOption) | p_CampaignTargeting_displayvideo_id | CampaignTargeting_displayvideo_id  
[InsertionOrder](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.insertionOrders#InsertionOrder) | p_InsertionOrder_displayvideo_id | InsertionOrder_displayvideo_id  
[InsertionOrderTargeting](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.insertionOrders.targetingTypes.assignedTargetingOptions#AssignedTargetingOption) | p_InsertionOrderTargeting_displayvideo_id | InsertionOrderTargeting_displayvideo_id  
[AdGroup](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.adGroups#AdGroup) | p_AdGroup_displayvideo_id | AdGroup_displayvideo_id  
[AdGroupTargeting](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.adGroups/bulkListAdGroupAssignedTargetingOptions#AdGroupAssignedTargetingOption) | p_AdGroupTargeting_displayvideo_id | AdGroupTargeting_displayvideo_id  
[AdGroupAd](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.adGroupAds#AdGroupAd) | p_AdGroupAd_displayvideo_id | AdGroupAd_displayvideo_id  
[Creative](https://developers.google.com/display-video/api/reference/rest/v3/advertisers.creatives#resource:-creative) | p_Creative_displayvideo_id | Creative_displayvideo_id  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
