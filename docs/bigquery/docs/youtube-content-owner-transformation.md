---
url: https://docs.cloud.google.com/bigquery/docs/youtube-content-owner-transformation/
title: YouTube Content Owner report transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:51.659868+00:00
---

# YouTube Content Owner report transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/youtube-content-owner-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# YouTube Content Owner report transformation

When your YouTube Content Owner or system-managed reports are transferred to BigQuery, the reports are transformed into the following BigQuery tables and views.

When you view the tables and views in BigQuery, the value for suffix is the table suffix you configured when you created the transfer.

## YouTube Content Owner reports

The following sections describe transformations for YouTube Content Owner reports.

### Video reports

The following reports focus on video-level user activity, playback locations, traffic sources, and demographics.

#### User activity

YouTube report: [User activity](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-user-activity)

BigQuery table:
    p_content_owner_basic_a4_suffix
BigQuery view:
    content_owner_basic_a4_suffix

#### User activity by province

YouTube report: [User activity by province](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-province)

BigQuery table:
    p_content_owner_province_a3_suffix
BigQuery view:
    content_owner_province_3_suffix

#### Playback locations

YouTube report: [Playback locations](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-playback-locations)

BigQuery table:
    p_content_owner_playback_location_a3_suffix
BigQuery view:
    content_owner_playback_location_a3_suffix

#### Traffic sources

YouTube report: [Traffic sources](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-traffic-sources)

BigQuery table:
    p_content_owner_traffic_source_a3_suffix
BigQuery view:
    content_owner_traffic_source_a3_suffix

#### Device type and operating system

YouTube report: [Device type and operating system](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-device-type-and-operating-system)

BigQuery table:
    p_content_owner_device_os_a3_suffix
BigQuery view:
    content_owner_device_os_a3_suffix

#### Viewer demographics

YouTube report: [Viewer demographics](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-viewer-demographics)

BigQuery table:
    p_content_owner_demographics_a1_suffix
BigQuery view:
    content_owner_demographics_a1_suffix

#### Content sharing by platform

YouTube report: [Content sharing by platform](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-content-sharing)

BigQuery table:
    p_content_owner_sharing_service_a1_suffix
BigQuery view:
    content_owner_sharing_service_a1_suffix

#### Annotations

YouTube report: [Annotations](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-annotations)

BigQuery table:
    p_content_owner_annotations_a1_suffix
BigQuery view:
    content_owner_annotations_a1_suffix

#### Cards

YouTube report: [Cards](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-cards)

BigQuery table:
    p_content_owner_cards_a1_suffix
BigQuery view:
    content_owner_cards_a1_suffix

#### End screens

YouTube report: [End screens](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-end-screens)

BigQuery table:
    p_content_owner_end_screens_a1_suffix
BigQuery view:
    content_owner_end_screens_a1_suffix

#### Subtitles

YouTube report: [Subtitles](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-subtitles)

BigQuery table:
    p_content_owner_subtitles_a3_suffix
BigQuery view:
    content_owner_subtitles_a3_suffix

#### Combined

YouTube report: [Combined](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#video-combined)

BigQuery table:
    p_content_owner_combined_a3_suffix
BigQuery view:
    content_owner_combined_a3_suffix

### Playlist reports

The following reports contain performance metrics and user activity for playlists.

#### User activity

YouTube report: [User activity](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#playlist-user-activity)

BigQuery table:
    p_content_owner_playlist_basic_a2_suffix
BigQuery view:
    content_owner_playlist_basic_a2_suffix

#### User activity by province

YouTube report: [User activity by province](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#playlist-province)

BigQuery table:
    p_content_owner_playlist_province_a2_suffix
BigQuery view:
    content_owner_playlist_province_a2_suffix

#### Playback locations

YouTube report: [Playback locations](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#playlist-playback-locations)

BigQuery table:
    p_content_owner_playlist_playback_location_a2_suffix
BigQuery view:
    content_owner_playlist_playback_location_a2

#### Traffic sources

YouTube report: [Traffic sources](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#playlist-traffic-sources)

BigQuery table:
    p_content_owner_playlist_traffic_source_a2
BigQuery view:
    content_owner_playlist_traffic_source_a2_suffix

#### Device type and operating system

YouTube report: [Device type and operating system](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#playlist-device-type-and-operating-system)

BigQuery table:
    p_content_owner_playlist_device_os_a2_suffix
BigQuery view:
    content_owner_playlist_device_os_a2_suffix

#### Combined

YouTube report: [Combined](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#playlist-combined)

BigQuery table:
    p_content_owner_playlist_combined_a2_suffix
BigQuery view:
    content_owner_playlist_combined_a2_suffix

### Ad rate reports

The following reports display key ad metrics and transaction rates.

#### Ad rate reports

YouTube report: [Ad rate reports](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#ad-rate-reports)

BigQuery table:
    p_content_owner_ad_rates_a1_suffix
BigQuery view:
    content_owner_ad_rates_a1_suffix

### Estimated revenue reports

The following reports estimate revenue generated at the video and asset levels.

#### Estimated video revenue

YouTube report: [Estimated video revenue](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#estimated-revenue-videos)

BigQuery table:
    p_content_owner_estimated_revenue_a1_suffix
BigQuery view:
    content_owner_estimated_revenue_a1_suffix

#### Estimated asset revenue

YouTube report: [Estimated asset revenue](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#estimated-revenue-assets)

BigQuery table:
    p_content_owner_asset_estimated_revenue_a1_suffix
BigQuery view:
    content_owner_asset_estimated_revenue_a1_suffix

### Asset reports

The following reports focus on asset performance, user engagement, and metadata.

#### User activity

YouTube report: [User activity](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-user-activity)

BigQuery table:
    p_content_owner_asset_basic_a3_suffix
BigQuery view:
    content_owner_asset_basic_a3_suffix

#### User activity by province

YouTube report: [User activity by province](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-province)

BigQuery table:
    p_content_owner_asset_province_a3_suffix
BigQuery view:
    content_owner_asset_province_a3_suffix

#### Video playback locations

YouTube report: [Video playback locations](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-playback-locations)

BigQuery table:
    p_content_owner_asset_playback_location_a3_suffix
BigQuery view:
    content_owner_asset_playback_location_a3_suffix

#### Traffic sources

YouTube report: [Traffic sources](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-traffic-sources)

BigQuery table:
    p_content_owner_asset_traffic_source_a3_suffix
BigQuery view:
    content_owner_asset_traffic_source_a3_suffix

#### Device type and operating system

YouTube report: [Device type and operating system](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-device-type-and-operating-system)

BigQuery table:
    p_content_owner_asset_device_os_a3_suffix
BigQuery view:
    content_owner_asset_device_os_a3_suffix

#### Viewer demographics

YouTube report: [Viewer demographics](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-viewer-demographics)

BigQuery table:
    p_content_owner_asset_demographics_a1_suffix
BigQuery view:
    content_owner_asset_demographics_a1_suffix

#### Content sharing by platform

YouTube report: [Content sharing by platform](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-content-sharing)

BigQuery table:
    p_content_owner_asset_sharing_service_a1_suffix
BigQuery view:
    content_owner_asset_sharing_service_a1_suffix

#### Annotations

YouTube report: [Annotations](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-annotations)

BigQuery table:
    p_content_owner_asset_annotations_a1_suffix
BigQuery view:
    content_owner_asset_annotations_a1_suffix

#### Cards

YouTube report: [Cards](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-cards)

BigQuery table:
    p_content_owner_asset_cards_a1_suffix
BigQuery view:
    content_owner_asset_cards_a1_suffix

#### End screens

YouTube report: [End screens](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-end-screens)

BigQuery table:
    p_content_owner_asset_end_screens_a1_suffix
BigQuery view:
    content_owner_asset_end_screens_a1_suffix

#### Combined

YouTube report: [Combined](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#asset-combined)

BigQuery table:
    p_content_owner_asset_combined_a3_suffix
BigQuery view:
    content_owner_asset_combined_a3_suffix

### Reach reports

The following reports cover audience reach metrics for your channel content.

#### Reach basic

YouTube report: [Reach basic](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#reach-reports)

BigQuery table:
    p_content_owner_reach_basic_a1_suffix
BigQuery view:
    content_owner_reach_basic_a1_suffix

#### Reach combined

YouTube report: [Reach combined](https://developers.google.com/youtube/reporting/v1/reports/content_owner_reports#reach-reports)

BigQuery table:
    p_content_owner_reach_combined_a1_suffix
BigQuery view:
    content_owner_reach_combined_a1_suffix

## YouTube system-managed reports

The following sections describe transformations for reports managed by the YouTube system.

### Financial summary reports

The following reports summarize payments and billing data for your network.

#### Monthly payments summary

YouTube report: [Monthly payments summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/financial-summaries#monthly-payments-summary)

BigQuery table:
    p_content_owner_payments_summary_a1_suffix
BigQuery view:
    content_owner_payments_summary_a1_suffix

### Ad revenue reports

The following reports provide summaries of advertising revenue across different dimensions like country, video, and asset.

#### Monthly global ad revenue summary

YouTube report: [Monthly global ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-global-ad-revenue-summary)

BigQuery table:
    p_content_owner_global_ad_revenue_summary_a1_suffix
BigQuery view:
    content_owner_global_ad_revenue_summary_a1_suffix

#### Monthly country ad revenue summary

YouTube report: [Monthly country ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-country-ad-revenue-summary)

BigQuery table:
    p_content_owner_country_ad_revenue_summary_a1_suffix
BigQuery view:
    content_owner_country_ad_revenue_summary_a1_suffix

#### Monthly day ad revenue summary

YouTube report: [Monthly day ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-day-ad-revenue-summary)

BigQuery table:
    p_content_owner_day_ad_revenue_summary_a1_suffix
BigQuery view:
    content_owner_day_ad_revenue_summary_a1_suffix

#### Weekly global ad revenue summary

YouTube report: [Weekly global ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-global-ad-revenue-summary)

BigQuery table:
    p_content_owner_global_ad_revenue_summary_weekly_a1_suffix
BigQuery view:
    content_owner_global_ad_revenue_summary_weekly_a1_suffix

#### Weekly country ad revenue summary

YouTube report: [Weekly country ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-country-ad-revenue-summary)

BigQuery table:
    p_content_owner_country_ad_revenue_summary_weekly_a1_suffix
BigQuery view:
    content_owner_country_ad_revenue_summary_weekly_a1_suffix

#### Weekly day ad revenue summary

YouTube report: [Weekly day ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-day-ad-revenue-summary)

BigQuery table:
    p_content_owner_day_ad_revenue_summary_weekly_a1_suffix
BigQuery view:
    content_owner_day_ad_revenue_summary_weekly_a1_suffix

#### Aggregate ad revenue per video

YouTube report: [Aggregate ad revenue per video](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#aggregate-ad-revenue-per-video)

BigQuery table:
    p_content_owner_ad_revenue_summary_a1_suffix
BigQuery view:
    content_owner_ad_revenue_summary_a1_suffix

#### Weekly video ad revenue summary

YouTube report: [Weekly video ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-video-ad-revenue-summary)

BigQuery table:
    p_content_owner_ad_revenue_summary_weekly_a1_suffix
BigQuery view:
    content_owner_ad_revenue_summary_weekly_a1_suffix

#### Weekly video ad revenue

YouTube report: [Weekly video ad revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-video-ad-revenue)

BigQuery table:
    p_content_owner_ad_revenue_raw_weekly_a1_suffix
BigQuery view:
    content_owner_ad_revenue_raw_weekly_a1_suffix

#### Daily ad revenue per video

YouTube report: [Daily ad revenue per video](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#daily-ad-revenue-per-video)

BigQuery table:
    p_content_owner_ad_revenue_raw_a1_suffix
BigQuery view:
    content_owner_ad_revenue_raw_a1_suffix

#### Aggregate ad revenue per asset

YouTube report: [Aggregate ad revenue per asset](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#aggregate-ad-revenue-per-asset)

BigQuery table:
    p_content_owner_asset_ad_revenue_summary_a1_suffix
BigQuery view:
    content_owner_asset_ad_revenue_summary_a1_suffix

#### Daily ad revenue per asset

YouTube report: [Daily ad revenue per asset](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#daily-ad-revenue-per-asset)

BigQuery table:
    p_content_owner_asset_ad_revenue_raw_a1_suffix
BigQuery view:
    content_owner_asset_ad_revenue_raw_a1_suffix

#### Monthly claim ad revenue summary

YouTube report: [Monthly claim ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-claim-ad-revenue-summary)

BigQuery table:
    p_content_owner_claim_ad_revenue_summary_a1_suffix
BigQuery view:
    content_owner_claim_ad_revenue_summary_a1_suffix

#### Weekly claim ad revenue summary

YouTube report: [Weekly claim ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-claim-ad-revenue-summary)

BigQuery table:
    p_content_owner_claim_ad_revenue_summary_weekly_a1_suffix
BigQuery view:
    content_owner_claim_ad_revenue_summary_weekly_a1_suffix

#### Monthly claim ad revenue

YouTube report: [Monthly claim ad revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-claim-ad-revenue)

BigQuery table:
    p_content_owner_claim_ad_revenue_raw_a1_suffix
BigQuery view:
    content_owner_claim_ad_revenue_raw_a1_suffix

#### Weekly claim ad revenue

YouTube report: [Weekly claim ad revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#weekly-claim-ad-revenue)

BigQuery table:
    p_content_owner_claim_ad_revenue_raw_weekly_a1_suffix
BigQuery view:
    content_owner_claim_ad_revenue_raw_weekly_a1_suffix

#### Monthly global ad adjustment revenue summary

YouTube report: [Monthly global ad adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-global-ad-adjustment-revenue-summary)

BigQuery table:
    p_content_owner_global_ad_adjustment_revenue_summary_a1_suffix
BigQuery view:
    content_owner_global_ad_adjustment_revenue_summary_a1_suffix

#### Monthly asset ad adjustment revenue summary

YouTube report: [Monthly asset ad adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-asset-ad-adjustment-revenue-summary)

BigQuery table:
    p_content_owner_asset_ad_adjustment_revenue_summary_a1_suffix
BigQuery view:
    content_owner_asset_ad_adjustment_revenue_summary_a1_suffix

#### Monthly asset ad adjustment revenue

YouTube report: [Monthly asset ad adjustment revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-asset-ad-adjustment-revenue)

BigQuery table:
    p_content_owner_asset_ad_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_asset_ad_adjustment_revenue_raw_a1_suffix

#### Monthly video ad adjustment revenue summary

YouTube report: [Monthly video ad adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-video-ad-adjustment-revenue-summary)

BigQuery table:
    p_content_owner_ad_adjustment_revenue_summary_a1_suffix
BigQuery view:
    content_owner_ad_adjustment_revenue_summary_a1_suffix

#### Monthly video ad adjustment revenue raw

YouTube report: [Monthly video ad adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-video-ad-adjustment-revenue-raw)

BigQuery table:
    p_content_owner_ad_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_ad_adjustment_revenue_raw_a1_suffix

#### Monthly claim ad adjustment revenue summary

YouTube report: [Monthly claim ad adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-claim-ad-adjustment-revenue-summary)

BigQuery table:
    p_content_owner_claim_ad_adjustment_revenue_summary_a1_suffix
BigQuery view:
    content_owner_claim_ad_adjustment_revenue_summary_a1_suffix

#### Monthly claim ad adjustment revenue

YouTube report: [Monthly claim ad adjustment revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-claim-ad-adjustment-revenue)

BigQuery table:
    p_content_owner_claim_ad_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_claim_ad_adjustment_revenue_raw_a1_suffix

#### Monthly country ad adjustment revenue summary

YouTube report: [Monthly country ad adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-country-ad-adjustment-revenue-summary)

BigQuery table:
    p_content_owner_country_ad_adjustment_revenue_summary_a1_suffix
BigQuery view:
    content_owner_country_ad_adjustment_revenue_summary_a1_suffix

#### Monthly day ad adjustment revenue summary

YouTube report: [Monthly day ad adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/ads#monthly-day-ad-adjustment-revenue-summary)

BigQuery table:
    p_content_owner_day_ad_adjustment_revenue_summary_a1_suffix
BigQuery view:
    content_owner_day_ad_adjustment_revenue_summary_a1_suffix

### Subscription revenue reports

The following reports summarize music and non-music subscription revenue across videos and assets.

#### Monthly music revenue summary

YouTube report: [Monthly music revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-revenue-summary)

BigQuery table:
    p_content_owner_country_music_red_revenue_summary_a1_suffix
BigQuery view:
    content_owner_country_music_red_revenue_summary_a1_suffix

#### Monthly music label video revenue

YouTube report: [Monthly music label video revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-video-revenue)

BigQuery table:
    p_music_content_owner_red_revenue_raw_a1_suffix
BigQuery view:
    music_content_owner_red_revenue_raw_a1_suffix

#### Monthly music label assets revenue

YouTube report: [Monthly music label assets revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-assets-revenue)

BigQuery table:
    p_music_content_owner_asset_red_revenue_raw_a1_suffix
BigQuery view:
    music_content_owner_asset_red_revenue_raw_a1_suffix

#### Monthly music label subscriber revenue summary

YouTube report: [Monthly music label subscriber revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-subscriber-revenue-summary)

BigQuery table:
    p_music_content_owner_subscriber_red_revenue_summary_a1_suffix
BigQuery view:
    music_content_owner_subscriber_red_revenue_summary_a1_suffix

#### Monthly music publisher revenue summary

YouTube report: [Monthly music publisher revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-publisher-revenue-summary)

BigQuery table:
    p_publisher_content_owner_music_red_revenue_summary_a1_suffix
BigQuery view:
    publisher_content_owner_music_red_revenue_summary_a1_suffix

#### Monthly music publisher subscription revenue summary

YouTube report: [Monthly music publisher subscription revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-publisher-subscription-revenue-summary)

BigQuery table:
    p_publisher_content_owner_subscriber_red_revenue_summary_a1_suffix
BigQuery view:
    publisher_content_owner_subscriber_red_revenue_summary_a1_suffix

#### Monthly music publisher non-music subscription revenue summary

YouTube report: [Monthly music publisher non-music subscription revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-publisher-non-music-subscription-revenue-summary)

BigQuery table:
    p_publisher_content_owner_non_music_red_revenue_summary_a1_suffix
BigQuery view:
    publisher_content_owner_non_music_red_revenue_summary_a1_suffix

#### Monthly music label music revenue summary

YouTube report: [Monthly music label music revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-music-revenue-summary)

BigQuery table:
    p_music_content_owner_country_music_red_revenue_summary_a1_suffix
BigQuery view:
    music_content_owner_country_music_red_revenue_summary_a1_suffix

#### Monthly subscriptions music video revenue

YouTube report: [Monthly subscriptions music video revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-subscriptions-music-video-revenue)

BigQuery table:
    p_content_owner_music_red_revenue_raw_a1_suffix
BigQuery view:
    content_owner_music_red_revenue_raw_a1_suffix

#### Monthly subscriptions music assets revenue

YouTube report: [Monthly subscriptions music assets revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-subscriptions-music-assets-revenue)

BigQuery table:
    p_content_owner_music_asset_red_revenue_raw_a1_suffix
BigQuery view:
    content_owner_music_asset_red_revenue_raw_a1_suffix

#### Weekly music revenue summary

YouTube report: [Weekly music revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#weekly-music-revenue-summary)

BigQuery table:
    p_music_content_owner_country_music_red_revenue_summary_weekly_a1_suffix
BigQuery view:
    music_content_owner_country_music_red_revenue_summary_weekly_a1_suffix

#### Weekly music label videos revenue

YouTube report: [Weekly music label videos revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#weekly-music-label-videos-revenue)

BigQuery table:
    p_music_content_owner_red_revenue_raw_weekly_a1_suffix
BigQuery view:
    music_content_owner_red_revenue_raw_weekly_a1_suffix

#### Weekly music label assets revenue

YouTube report: [Weekly music label assets revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#weekly-music-label-assets-revenue)

BigQuery table:
    p_music_content_owner_asset_red_revenue_raw_weekly_a1_suffix
BigQuery view:
    music_content_owner_asset_red_revenue_raw_weekly_a1_suffix

#### Monthly non-music summary

YouTube report: [Monthly non-music summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-non-music-summary)

BigQuery table:
    p_content_owner_country_non_music_red_revenue_summary_a1_suffix
BigQuery view:
    content_owner_country_non_music_red_revenue_summary_a1_suffix

#### Monthly music label non-music revenue summary

YouTube report: [Monthly music label non-music revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-non-music-revenue-summary)

BigQuery table:
    p_music_content_owner_country_non_music_red_revenue_summary_a1_suffix
BigQuery view:
    music_content_owner_country_non_music_red_revenue_summary_a1_suffix

#### Monthly subscriptions non-music videos revenue

YouTube report: [Monthly subscriptions non-music videos revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-subscriptions-non-music-videos-revenue)

BigQuery table:
    p_content_owner_non_music_red_revenue_raw_a1_suffix
BigQuery view:
    content_owner_non_music_red_revenue_raw_a1_suffix

#### Monthly subscriptions non-music assets revenue

YouTube report: [Monthly subscriptions non-music assets revenue](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-subscriptions-non-music-assets-revenue)

BigQuery table:
    p_content_owner_non_music_asset_red_revenue_raw_a1_suffix
BigQuery view:
    content_owner_non_music_asset_red_revenue_raw_a1_suffix

#### Weekly non-music revenue summary

YouTube report: [Weekly non-music revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#weekly-non-music-revenue-summary)

BigQuery table:
    p_music_content_owner_country_non_music_red_revenue_summary_weekly_a1_suffix
BigQuery view:
    music_content_owner_country_non_music_red_revenue_summary_weekly_a1_suffix

#### Monthly music label asset subscription adjustment revenue raw

YouTube report: [Monthly music label asset subscription adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-asset-subscription-adjustment-revenue-raw)

BigQuery table:
    p_music_content_owner_asset_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    music_content_owner_asset_red_adjustment_revenue_raw_a1_suffix

#### Monthly subscriptions adjustment music video raw

YouTube report: [Monthly subscriptions adjustment music video raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-subscriptions-adjustment-music-video-raw)

BigQuery table:
    p_music_content_owner_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    music_content_owner_red_adjustment_revenue_raw_a1_suffix

#### Monthly music label country music subscription adjustment revenue summary

YouTube report: [Monthly music label country music subscription adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-country-music-subscription-adjustment-revenue-summary)

BigQuery table:
    p_music_content_owner_country_music_red_adjustment_revenue_summary_a1_suffix
BigQuery view:
    music_content_owner_country_music_red_adjustment_revenue_summary_a1_suffix

#### Monthly music label country non-music subscription adjustment revenue summary

YouTube report: [Monthly music label country non-music subscription adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-label-country-non-music-subscription-adjustment-revenue-summary)

BigQuery table:
    p_music_content_owner_country_non_music_red_adjustment_revenue_summary_a1_suffix
BigQuery view:
    music_content_owner_country_non_music_red_adjustment_revenue_summary_a1_suffix

#### Monthly non-music asset subscription adjustment revenue raw

YouTube report: [Monthly non-music asset subscription adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-non-music-asset-subscription-adjustment-revenue-raw)

BigQuery table:
    p_content_owner_non_music_asset_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_non_music_asset_red_adjustment_revenue_raw_a1_suffix

#### Monthly non-music subscription adjustment revenue raw

YouTube report: [Monthly non-music subscription adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-non-music-subscription-adjustment-revenue-raw)

BigQuery table:
    p_content_owner_non_music_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_non_music_red_adjustment_revenue_raw_a1_suffix

#### Monthly music video subscription adjustment revenue raw

YouTube report: [Monthly music video subscription adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-video-subscription-adjustment-revenue-raw)

BigQuery table:
    p_content_owner_music_video_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_music_video_red_adjustment_revenue_raw_a1_suffix

#### Monthly music asset subscription adjustment revenue raw

YouTube report: [Monthly music asset subscription adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-asset-subscription-adjustment-revenue-raw)

BigQuery table:
    p_content_owner_music_asset_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    content_owner_music_asset_red_adjustment_revenue_raw_a1_suffix

#### Monthly music publisher asset subscription adjustment revenue raw

YouTube report: [Monthly music publisher asset subscription adjustment revenue raw](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-publisher-asset-subscription-adjustment-revenue-raw)

BigQuery table:
    p_publisher_content_owner_asset_red_adjustment_revenue_raw_a1_suffix
BigQuery view:
    publisher_content_owner_asset_red_adjustment_revenue_raw_a1_suffix

#### Monthly music publisher country non-music subscription adjustment revenue summary

YouTube report: [Monthly music publisher country non-music subscription adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-publisher-country-non-music-subscription-adjustment-revenue-summary)

BigQuery table:
    p_publisher_content_owner_country_non_music_red_adjustment_revenue_summary_a1_suffix
BigQuery view:
    publisher_content_owner_country_non_music_red_adjustment_revenue_summary_a1_suffix

#### Monthly music publisher country music subscription adjustment revenue summary

YouTube report: [Monthly music publisher country music subscription adjustment revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/subscriptions#monthly-music-publisher-country-music-subscription-adjustment-revenue-summary)

BigQuery table:
    p_publisher_content_owner_country_music_red_adjustment_revenue_summary_a1_suffix
BigQuery view:
    publisher_content_owner_country_music_red_adjustment_revenue_summary_a1_suffix

### YouTube Shorts revenue reports

The following reports summarize revenue and engagement metrics for YouTube Shorts.

#### Monthly YouTube Shorts music label content owner revenue summary

YouTube report: [Monthly YouTube Shorts music label content owner revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-music-label-content-owner-revenue-summary)

BigQuery table:
    p_music_content_owner_shorts_revenue_summary_a1_suffix
BigQuery view:
    music_content_owner_shorts_revenue_summary_a1_suffix

#### Monthly YouTube Shorts music publisher content owner revenue summary

YouTube report: [Monthly YouTube Shorts music publisher content owner revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-music-publisher-content-owner-revenue-summary)

BigQuery table:
    p_publisher_content_owner_shorts_revenue_summary_a1_suffix
BigQuery view:
    publisher_content_owner_shorts_revenue_summary_a1_suffix

#### Monthly YouTube Shorts global ad revenue summary

YouTube report: [Monthly YouTube Shorts global ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-global-ad-revenue-summary)

BigQuery table:
    p_content_owner_shorts_global_ad_revenue_summary_a2_suffix
BigQuery view:
    content_owner_shorts_global_ad_revenue_summary_a2_suffix

#### Daily YouTube Shorts ad revenue summary

YouTube report: [Daily YouTube Shorts ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#daily-youtube-shorts-ad-revenue-summary)

BigQuery table:
    p_content_owner_shorts_day_ad_revenue_summary_a2_suffix
BigQuery view:
    content_owner_shorts_day_ad_revenue_summary_a2_suffix

#### Monthly YouTube Shorts country ad revenue summary

YouTube report: [Monthly YouTube Shorts country ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-country-ad-revenue-summary)

BigQuery table:
    p_content_owner_shorts_country_ad_revenue_summary_a2_suffix
BigQuery view:
    content_owner_shorts_country_ad_revenue_summary_a2_suffix

#### Monthly YouTube Shorts ad revenue summary

YouTube report: [Monthly YouTube Shorts ad revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-ad-revenue-summary)

BigQuery table:
    p_content_owner_shorts_ad_revenue_summary_a2_suffix
BigQuery view:
    content_owner_shorts_ad_revenue_summary_a2_suffix

#### Monthly YouTube Shorts subscriptions revenue summary

YouTube report: [Monthly YouTube Shorts subscriptions revenue summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-subscriptions-revenue-summary)

BigQuery table:
    p_content_owner_shorts_red_revenue_summary_a1_suffix
BigQuery view:
    content_owner_shorts_red_revenue_summary_a1_suffix

#### Monthly YouTube Shorts subscriptions revenue video summary

YouTube report: [Monthly YouTube Shorts subscriptions revenue video summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/shorts#monthly-youtube-shorts-subscriptions-revenue-video-summary)

BigQuery table:
    p_content_owner_shorts_red_revenue_video_summary_a1_suffix
BigQuery view:
    content_owner_shorts_red_revenue_video_summary_a1_suffix

### Tax withholding reports

The following reports show tax withholding calculations and summaries.

#### Tax withholding

YouTube report: [Tax withholding](https://developers.google.com/youtube/reporting/v1/reports/system_managed/taxes#tax-withholding)

BigQuery table:
    p_content_owner_tax_withholding_a1_suffix
BigQuery view:
    content_owner_tax_withholding_a1_suffix

### Video reports

The following reports contain daily metadata and summaries for videos.

#### Daily video metadata (version 1.4)

YouTube report: [Daily video metadata (version 1.4)](https://developers.google.com/youtube/reporting/v1/reports/system_managed/videos#daily-video-metadata-version-1.4)

BigQuery table:
    p_content_owner_video_metadata_a4_suffix
BigQuery view:
    content_owner_video_metadata_a4_suffix

### Asset reports

The following reports detail daily network assets and asset conflicts.

#### Daily asset report

YouTube report: [Daily asset report](https://developers.google.com/youtube/reporting/v1/reports/system_managed/assets#daily-asset-report-version-1.3)

BigQuery table:
    p_content_owner_asset_a3_suffix
BigQuery view:
    content_owner_asset_a3_suffix

#### Daily asset conflicts

YouTube report: [Daily asset conflicts](https://developers.google.com/youtube/reporting/v1/reports/system_managed/assets#daily-asset-conflicts-version-1.3)

BigQuery table:
    p_content_owner_asset_conflict_a3_suffix
BigQuery view:
    content_owner_asset_conflict_a3_suffix

### Reference reports

The following reports track active reference files and metadata.

#### Weekly references

YouTube report: [Weekly references](https://developers.google.com/youtube/reporting/v1/reports/system_managed/references#weekly-references)

BigQuery table:
    p_content_owner_active_references_a1_suffix
BigQuery view:
    content_owner_active_references_a1_suffix

### Claims reports

The following reports provide daily summaries of active claims.

#### Daily claims (Version 1.2)

YouTube report: [Daily claims (Version 1.2)](https://developers.google.com/youtube/reporting/v1/reports/system_managed/claims#daily-claims-version-1.2)

BigQuery table:
    p_content_owner_active_claims_a3_suffix
BigQuery view:
    content_owner_active_claims_a3_suffix

#### Monthly ad revenue audio claims

YouTube report: [Monthly ad revenue audio claims](https://developers.google.com/youtube/reporting/v1/reports/system_managed/claims#monthly-ad-revenue-audio-claims)

BigQuery table:
    p_content_owner_claim_audio_tier_revenue_raw_a1_suffix
BigQuery view:
    content_owner_claim_audio_tier_revenue_raw_a1_suffix

#### Monthly ad revenue audio claims summary

YouTube report: [Monthly ad revenue audio claims summary](https://developers.google.com/youtube/reporting/v1/reports/system_managed/claims#monthly-ad-revenue-audio-claims-summary)

BigQuery table:
    p_content_owner_claim_audio_tier_revenue_summary_a1_suffix
BigQuery view:
    content_owner_claim_audio_tier_revenue_summary_a1_suffix

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
