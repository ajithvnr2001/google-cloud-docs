---
url: https://docs.cloud.google.com/bigquery/docs/youtube-channel-transformation/
title: YouTube Channel report transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:25:18.211783+00:00
---

# YouTube Channel report transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/youtube-channel-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# YouTube Channel report transformation

When your YouTube Channel reports are transferred to BigQuery, the reports are transformed into the following BigQuery tables and views.

When you view the tables and views in BigQuery, the value for suffix is the table suffix you configured when you created the transfer.

**YouTube Channel report** | **BigQuery table** | **BigQuery view**  
---|---|---  
**Video reports** |  |   
[User activity](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-user-activity) | p_channel_basic_a3_suffix | channel_basic_a3_suffix  
[User activity by province](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-province) | p_channel_province_a3_suffix | channel_province_a3_suffix  
[Playback locations](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-playback-locations) | p_channel_playback_location_a3_suffix | channel_playback_location_a3_suffix  
[Traffic sources](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-traffic-sources) | p_channel_traffic_source_a3_suffix | channel_traffic_source_a3_suffix  
[Device type and operating system](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-device-type-and-operating-system) | p_channel_device_os_a3_suffix | channel_device_os_a3_suffix  
[Viewer demographics](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-viewer-demographics) | p_channel_demographics_a1_suffix | channel_demographics_a1_suffix  
[Content sharing by platform](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-content-sharing) | p_channel_sharing_service_a1_suffix | channel_sharing_service_a1_suffix  
[Annotations](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-annotations) | p_channel_annotations_a1_suffix | channel_annotations_a1_suffix  
[Cards](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-cards) | p_channel_cards_a1_suffix | channel_cards_a1_suffix  
[End screens](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-end-screens) | p_channel_end_screens_a1_suffix | channel_end_screens_a1_suffix  
[Subtitles](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-subtitles) | p_channel_subtitles_a3_suffix | channel_subtitles_a3_suffix  
[Combined](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#video-combined) | p_channel_combined_a3_suffix | channel_combined_a3_suffix  
**Playlist reports** |  |   
[User activity](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#playlist-user-activity) | p_playlist_basic_a2_suffix | playlist_basic_a2_suffix  
[User activity by province](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#playlist-province) | p_playlist_province_a2_suffix | playlist_province_a2_suffix  
[Playback locations](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#playlist-playback-locations) | p_playlist_playback_location_a2_suffix | playlist_playback_location_a2_suffix  
[Traffic sources](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#playlist-traffic-sources) | p_playlist_traffic_source_a2_suffix | playlist_traffic_source_a2_suffix  
[Device type and operating system](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#playlist-device-type-and-operating-system) | p_playlist_device_os_a2_suffix | playlist_device_os_a2_suffix  
[Combined](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#playlist-combined) | p_playlist_combined_a2_suffix | playlist_combined_a2_suffix  
**Reach reports** |  |   
[Reach basic](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#reach-reports) | p_channel_reach_basic_a1_suffix | channel_reach_basic_a1_suffix  
[Reach combined](https://developers.google.com/youtube/reporting/v1/reports/channel_reports#reach-reports) | p_channel_reach_combined_a1_suffix | channel_reach_combined_a1_suffix  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
