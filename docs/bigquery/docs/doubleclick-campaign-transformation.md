---
url: https://docs.cloud.google.com/bigquery/docs/doubleclick-campaign-transformation/
title: Campaign Manager report transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:53:29.465377+00:00
---

# Campaign Manager report transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/doubleclick-campaign-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Campaign Manager report transformation

When your Campaign Manager (formerly known as DoubleClick Campaign Manager) data transfer files are transferred to BigQuery, the files are transformed into the following BigQuery tables and views.

When you view the tables and views in BigQuery, the value for campaign_manager_id is your Campaign Manager Network, Advertiser, or Floodlight ID.

**Campaign Manager file** | **BigQuery table** | **BigQuery view**  
---|---|---  
**Data Transfer files** |  |   
[impression](https://developers.google.com/doubleclick-advertisers/dtv2/reference/file-format) | p_impression_campaign_manager_id | impression_campaign_manager_id  
[click](https://developers.google.com/doubleclick-advertisers/dtv2/reference/file-format) | p_click_campaign_manager_id | click_campaign_manager_id  
[activity](https://developers.google.com/doubleclick-advertisers/dtv2/reference/file-format) | p_activity_campaign_manager_id | activity_campaign_manager_id  
[rich_media](https://developers.google.com/doubleclick-advertisers/dtv2/reference/file-format) | p_rich_media_campaign_manager_id | rich_media_campaign_manager_id  
**Match Tables** |  |   
[activity_cats](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#activity_cats) | p_match_table_activity_cats_campaign_manager_id | match_table_activity_cats_campaign_manager_id  
[activity_types](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#activity_types) | p_match_table_activity_types_campaign_manager_id | match_table_activity_types_campaign_manager_id  
[ads](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#ads) | p_match_table_ads_campaign_manager_id | match_table_ads_campaign_manager_id  
[ad_placement_assignments](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#ad_placement_assignments) | p_match_table_ad_placement_assignments_campaign_manager_id | match_table_ad_placement_assignments_campaign_manager_id  
[advertisers](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#advertisers) | p_match_table_advertisers_campaign_manager_id | match_table_advertisers_campaign_manager_id  
[assets](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#assets) | p_match_table_assets_campaign_manager_id | match_table_assets_campaign_manager_id  
[browsers](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#browsers) | p_match_table_browsers_campaign_manager_id | match_table_browsers_campaign_manager_id  
[campaigns](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#campaigns) | p_match_table_campaigns_campaign_manager_id | match_table_campaigns_campaign_manager_id  
[cities](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#cities) | p_match_table_cities_campaign_manager_id | match_table_cities_campaign_manager_id  
[creatives](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#creatives) | p_match_table_creatives_campaign_manager_id | match_table_creatives_campaign_manager_id  
[creative_ad_assignments](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#creative_ad_assignments) | p_match_table_creative_ad_assignments_campaign_manager_id | match_table_creative_ad_assignments_campaign_manager_id  
[custom_creative_fields](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#custom_creative_fields) | p_match_table_custom_creative_fields_campaign_manager_id | match_table_custom_creative_fields_campaign_manager_id  
[paid_search](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#paid_search) | p_match_table_paid_search_campaign_manager_id | match_table_paid_search_campaign_manager_id  
[designated_market_areas](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#designated_market_areas) | p_match_table_designated_market_areas_campaign_manager_id | match_table_designated_market_areas_campaign_manager_id  
[keyword_value](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#keyword_value) | p_match_table_keyword_value_campaign_manager_id | match_table_keyword_value_campaign_manager_id  
null user ID reason categories | Unsupported | Unsupported  
rich media standard event and event type IDs | Unsupported | Unsupported  
[custom_rich_media](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#custom_rich_media) | p_match_table_custom_rich_media_campaign_manager_id | match_table_custom_rich_media_campaign_manager_id  
[operating_systems](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#operating_systems) | p_match_table_operating_systems_campaign_manager_id | match_table_operating_systems_campaign_manager_id  
[placements](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#placements) | p_match_table_placements_campaign_manager_id | match_table_placements_campaign_manager_id  
[placement_cost](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#placement_cost) | p_match_table_placement_cost_campaign_manager_id | match_table_placement_cost_campaign_manager_id  
[sites](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#sites) | p_match_table_sites_campaign_manager_id | match_table_sites_campaign_manager_id  
[states](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#states) | p_match_table_states_campaign_manager_id | match_table_states_campaign_manager_id  
[custom_floodlight_variables](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#custom_floodlight_variables) | p_match_table_custom_floodlight_variables_campaign_manager_id | match_table_custom_floodlight_variables_campaign_manager_id  
[landing_page_url](https://developers.google.com/doubleclick-advertisers/dtv2/reference/match-tables#landing_page_url) | p_match_table_landing_page_url_campaign_manager_id | match_table_landing_page_url_campaign_manager_id  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
