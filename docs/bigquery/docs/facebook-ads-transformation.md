---
url: https://docs.cloud.google.com/bigquery/docs/facebook-ads-transformation/
title: Facebook Ads report transformation \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:48:15.910248+00:00
---

# Facebook Ads report transformation  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/facebook-ads-transformation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Facebook Ads report transformation 

This document describes how your Facebook Ads reports are transformed when you [run a Facebook Ads transfer to BigQuery](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer).

## Table mapping for Facebook Ads reports

When your Facebook Ads reports are transferred to BigQuery, the reports are transformed into the following BigQuery tables and views.

### `AdAccounts` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id` | ID [KEY] | _String_ | The Id of Ad Account.  
`` | Target | _String_ | The target used to get ad accounts from. This value is `null` - to get all ad accounts.  
`account_id` | AccountId | _String_ | The Id of the Ad Account when viewed directly in Facebook.  
`account_status` | AccountStatus | _Integer_ | Status of the account. 1 = Active, 2 = Disabled, 3 = Unsettled, 7 = Pending Review, 9 = in Grace Period, 101 = temporarily unavailable, 100 = pending closure.  
`age` | Age | _Double_ | Amount of time the ad account has been open, in days.  
`amount_spent` | AmountSpent | _Integer_ | Current total amount spent by the account. This can be reset.  
`balance` | Balance | _Integer_ | Bill amount due.  
`business_city` | BusinessCity | _String_ | City for business address.  
`business_country_code` | BusinessCountryCode | _String_ | Country code for the business address.  
`business_name` | BusinessName | _String_ | The business name for the account.  
`business_state` | BusinessState | _String_ | State abbreviation for business address.  
`business_street` | BusinessStreet | _String_ | First line of the business street address for the account.  
`business_street2` | BusinessStreet2 | _String_ | Second line of the business street address for the account.  
`business_zip` | BusinessZip | _String_ | Zip code for business address.  
`capabilities` | Capabilities | _String_ | Capabilities allowed for this ad account.  
`created_time` | CreatedTime | _Datetime_ | The time the account was created.  
`currency` | Currency | _String_ | The currency used for the account, based on the corresponding value in the account settings.  
`min_campaign_group_spend_cap` | MinCampaignGroupSpendCap | _String_ | The minimum campaign group spend limit.  
`name` | Name | _String_ | Name of the account; note that many accounts are unnamed, so this field may be empty.  
`offsite_pixels_tos_accepted` | OffsitePixelsTosAccepted | _String_ | Indicates whether the offsite pixel Terms Of Service contract was signed.  
`owner` | OwnerId | _String_ | Facebook ID of the owner for the Ad Account.  
`spend_cap` | SpendCap | _Integer_ | The maximum that can be spent by this account after which campaigns will be paused. A value of 0 signifies no spending-cap.  
`timezone_id` | TimezoneId | _String_ | ID for the timezone.  
`timezone_name` | TimezoneName | _String_ | Name for the timezone.  
`timezone_offset_hours_utc` | TimezoneOffsetHoursUTC | _Double_ | Time Zone difference from UTC.  
  
### `AdInsights` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`` | Target | _String_ | The Id of the Account to get insights for.  
`date_start` | DateStart | _Date_ | The starting date to retrieve insights. In the Facebook UI, this is the Report Start field.   
`date_stop` | DateEnd | _Date_ | The ending date to retrieve insights. In the Facebook UI, this is the Report End field.   
`` | TimeIncrement | _String_ | The number of days of data aggregation. This value is set to 1.  
`` | Level | _String_ | The level to represent the results at. This value is set to `ad`.  
`account_currency` | AccountCurrency | _String_ | The currency that is being used by the ad account.  
`action_attribution_windows` | ActionAttributionWindows | _String_ | A comma separated list that determines what is the attribution window for the actions. For example, 28d_click means the API returns all actions that happened 28 days after someone clicked on the ad. This option is set at [1d_view,28d_click].  
`account_id` | AdAccountId | _String_ | The Id of the Ad Account that is associated with the report row.  
`account_name` | AdAccountName | _String_ | The name of the Ad Account that is associated with the report row.  
`campaign_id` | CampaignId | _String_ | The Id of the Campaign that is associated with the report row.  
`campaign_name` | CampaignName | _String_ | The name of the Campaign that is associated with the report row.  
`adset_id` | AdSetId | _String_ | The Id of the Ad Set that is associated with the report row.  
`adset_name` | AdSetName | _String_ | The name of the Ad Set that is associated with the report row.  
`ad_id` | AdId | _String_ | The Id of the Ad that is associated with the report row.  
`ad_name` | AdName | _String_ | The name of the Ad that is associated with the report row.  
`buying_type` | BuyingType | _String_ | The method by which target ads are paid for in your campaigns.  
`clicks` | Clicks | _Long_ | The total number of clicks on your ad. Depending on what you're promoting, this can include Page likes, event responses or app installs. In the Facebook UI, this is the Clicks (All) field.  
`conversion_rate_ranking` | ConversionRateRanking | _String_ | The conversion rate ranking.  
`cost_per_estimated_ad_recallers` | CostPerEstimatedAdRecallers | _Decimal_ | The average cost per additional person that we estimate will recall seeing your ad if asked within 2 days.  
`cost_per_inline_link_click` | CostPerInlineLinkClick | _Decimal_ | The average cost per click on links in the ad.  
`cost_per_inline_post_engagement` | CostPerInlinePostEngagement | _Decimal_ | The average cost per engagement on the post.  
`cost_per_unique_click` | CostPerUniqueClick | _Decimal_ | The average cost per unique click for these ads, calculated as the amount spent divided by the number of unique clicks received.  
`cost_per_unique_inline_link_click` | CostPerUniqueInlineLinkClick | _Decimal_ | The average you paid for each unique inline link click.  
`cpc` | CPC | _Decimal_ | The average cost per click for these ads, calculated as the amount spent divided by the number of clicks received.  
`cpm` | CPM | _Decimal_ | The average cost that you've paid to have 1,000 impressions on your ad.  
`cpp` | CPP | _Decimal_ | The average cost that you've paid to have your ad served to 1,000 unique people.  
`ctr` | CTR | _Double_ | The number of clicks you received divided by the number of impressions. In the Facebook UI, this is the CTR (All) % field.  
`estimated_ad_recall_rate` | EstimatedAdRecallRate | _Double_ | The estimated number of people who recall your ad divided by the number of people your ad reached.  
`estimated_ad_recallers` | EstimatedAdRecallers | _Double_ | The additional number of people that we estimate will remember seeing your ads if asked within 2 days.  
`frequency` | Frequency | _Double_ | The average number of times that your ad was served to each person.  
`impressions` | Impressions | _Long_ | The number of times that your ad was served. On mobile apps an ad is counted as served the first time it's viewed. On all other Facebook interfaces, an ad is served the first time it's placed in a person's News Feed or each time it's placed in the right column.  
`inline_link_clicks` | InlineLinkClicks | _Long_ | Total number of clicks on links in the ad.  
`inline_link_click_ctr` | InlineLinkClicksCounter | _Double_ | The click-through rate for inline clicks to link.  
`inline_post_engagement` | InlinePostEngagement | _Long_ | The total number of engagements on the post.  
`instant_experience_clicks_to_open` | InstantExperienceClicksToOpen | _Long_ | Corresponds to the instant_experience_clicks_to_open field from the META API.  
`instant_experience_clicks_to_start` | InstantExperienceClicksToStart | _Long_ | Corresponds to the instant_experience_clicks_to_start field from the META API.  
`instant_experience_outbound_clicks` | InstantExperienceOutboundClicks | _Long_ | Corresponds to the instant_experience_outbound_clicks field from the META API.  
`objective` | Objective | _String_ | The objective you selected for your campaign. Your objective reflects the goal you want to achieve with your advertising.  
`quality_ranking` | QualityRanking | _String_ | The quality ranking.  
`reach` | Reach | _Long_ | The number of people your ad was served to.  
`spend` | Spend | _Decimal_ | The total amount you've spent so far.  
`` | UniqueClicks | _Long_ | The total number of unique people who have clicked on your ad. For example, if 3 people click the same ad 5 times, it counts as 3 unique clicks.  
`` | UniqueCTR | _Double_ | The number of people who clicked on your ad divided by the number of people you reached. For example, if you received 20 unique clicks and your ad was served to 1,000 unique people, your unique click-through rate would be 2%.  
`inline_link_clicks` | UniqueInlineLinkClicks | _Long_ | The number of unique inline link clicks that your ad got. In the Facebook UI, this is the Unique Clicks to Link field.  
`` | UniqueInlineLinkClickCounter | _Double_ | The click-through rate for unique inline clicks to link.  
`` | UniqueLinkClicksCounter | _Double_ | The unique click-through rate for clicks to link. The number of people who clicked on the link in your ad that directs people off Facebook divided by the number of people you reached. For example, if you received 20 unique clicks to link and your ad was shown to 1,000 unique people, your unique click-through rate would be 2%.  
`` | Checkins | _Int_ | The number of checkins attributed to the Ad.  
`` | EventResponses | _Int_ | The number of event responses attributed to the Ad.  
`inline_link_clicks` | LinkClicks | _Int_ | The number of link clicks attributed to the Ad.  
`` | OfferSaves | _Int_ | The number of receive offers attributed to the Ad.  
`outbound_clicks` | OutboundClicks | _Int_ | The number of outbound clicks attributed to the Ad.  
`` | PageEngagements | _Int_ | The number of page engagements attributed to the Ad.  
`` | PageLikes | _Int_ | The number of page likes attributed to the Ad.  
`` | PageMentions | _Int_ | The number of page mentions attributed to the Ad.  
`` | PagePhotoViews | _Int_ | The number of photo views attributed to the Ad.  
`` | PostComments | _Int_ | The number of post comments attributed to the Ad.  
`` | PostEngagements | _Int_ | The number of post engagements attributed to the Ad.  
`` | PostShares | _Int_ | The number of post shares attributed to the Ad.  
`` | PostReactions | _Int_ | The number of post reactions attributed to the Ad.  
`` | PageTabViews | _Int_ | The number of tab views attributed to the Ad.  
`` | Region | _String_ | The region someone viewed the Ad from. This is a breakdown field.  
`` | Video3SecondViews | _Int_ | The number of video views attributed to the Ad. Views count if at least 3 seconds or the entire video (if the video is less than 3 seconds) were played.  
**Generic Breakdowns**  
`` | Age | _String_ | The age range for the metrics in this row.  
`` | Gender | _String_ | The gender for the metrics in this row.  
`` | Country | _String_ | The country for the metrics in this row.  
`` | Region | _String_ | The region someone viewed the ad from.  
`` | FrequencyValue | _String_ | The number of times an ad in your Reach and Frequency campaign was served to each person.  
`` | HStatsByAdvertiserTZ | _String_ | Time period over which the stats were taken for the advertiser.  
`` | HStatsByAudienceTZ | _String_ | Time period over which the stats were taken for the audience.  
`` | ImpressionDevice | _String_ | The devices used to view the Ad.  
`` | PlatformPosition | _String_ | The position on the platform.  
`` | PublisherPlatform | _String_ | The platforms the ads were published on.  
`` | ProductId | _String_ | The product Id advertised in the Ad.  
  
### `AdInsightsActions` report

`ACTION_COLLECTION` refers to the types of actions people have taken in response to your ad. For a full list of action collections, see [Action collections](https://docs.cloud.google.com/bigquery/docs/facebook-ads-transfer#action_collections).

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`` | Target | _String_ | The Id of the Account to get insights for.  
`date_start` | DateStart | _Date_ | The starting date to retrieve insights for. In the Facebook UI, this is the Report Start field.  
`date_stop` | DateEnd | _Date_ | The ending date to retrieve insights for. In the Facebook UI, this is the Report End field.  
`` | TimeIncrement | _String_ | The number of days of data aggregation. This value is set at 1.  
`` | Level | _String_ | The level to represent the results at. The value is set at `ad`.  
`action_attribution_windows` | ActionAttributionWindows | _String_ | A comma separated list which determines what is the attribution window for the actions. For example, 28d_click means the API returns all actions that happened 28 days after someone clicked on the ad. The default option means [1d_view,7d_click]. Possible values include 1d_view, 7d_view, 28d_view, 1d_click, 7d_click, 28d_click, default.  
`` | ActionCollection | _String_ | This comes from your choice of Action Collections in the transfer.  
`account_id` | AdAccountId | _String_ | The Id of the Ad Account associated with the report row.  
`account_name` | AdAccountName | _String_ | The name of the Ad Account associated with the report row.  
`campaign_id` | CampaignId | _String_ | The Id of the Campaign associated with the report row.  
`campaign_name` | CampaignName | _String_ | The name of the Campaign associated with the report row.  
`adset_id` | AdSetId | _String_ | The Id of the Ad Set associated with the report row.  
`adset_name` | AdSetName | _String_ | The name of the Ad Set associated with the report row.  
`ad_id` | AdId | _String_ | The Id of the Ad associated with the report row.  
`ad_name` | AdName | _String_ | The name of the Ad associated with the report row.  
`ACTION_COLLECTION.value` | ActionValue | _Integer_ | Metric value of default attribution window.  
  
The Facebook Ads plans to update this data type mapping. For more information, see [July 25, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#Jul25-fb-ads).  
`ACTION_COLLECTION.1d_click` | Action1dClick | _String_ | Metric value of attribution window 1 day after clicking the ad.  
`ACTION_COLLECTION.1d_view` | Action1dView | _String_ | Metric value of attribution window 1 day after viewing the ad.  
`ACTION_COLLECTION.7d_click` | Action7dClick | _String_ | Metric value of attribution window 7 days after clicking the ad.  
`ACTION_COLLECTION.7d_view` | Action7dView | _String_ | Metric value of attribution window 7 days after viewing the ad.  
`ACTION_COLLECTION.28d_click` | Action28dClick | _String_ | Metric value of attribution window 28 days after clicking the ad.  
`ACTION_COLLECTION.28d_view` | Action28dView | _String_ | Metric value of attribution window 28 days after viewing the ad.  
`ACTION_COLLECTION.dda` | ActionDDA | _String_ | Metric value of attribution window which is powered by data driven model.  
**Generic Breakdowns**  
`` | Age | _String_ | The age range for the metrics in this row.  
`` | Gender | _String_ | The gender for the metrics in this row.  
`` | Country | _String_ | The country for the metrics in this row.  
`` | Region | _String_ | The region someone viewed the ad from.  
`` | FrequencyValue | _String_ | The number of times an ad in your Reach and Frequency campaign was served to each person.  
`` | HStatsByAdvertiserTZ | _String_ | Time period over which the stats were taken for the advertiser.  
`` | HStatsByAudienceTZ | _String_ | Time period over which the stats were taken for the audience.  
`` | ImpressionDevice | _String_ | The devices used to view the Ad.  
`` | PlatformPosition | _String_ | The position on the platform.  
`` | PublisherPlatform | _String_ | The platforms the ads were published on.  
`` | ProductId | _String_ | The product Id advertised in the Ad.  
**Action Breakdowns**  
| ActionType | _String_ | The kind of actions taken on your ad after your ad was served to someone, even if they didn't click it.  
| ActionCanvasComponentName | _String_ | Name of a component within a Canvas ad.  
| ActionCarouselCardId | _String_ | The ID of the specific carousel card that people engaged with when they saw your ad.  
| ActionCarouselCardName | _String_ | The specific carousel card that people engaged with when they saw your ad. The cards are identified by their headlines.  
| ActionDestination | _String_ | The destination where people go after clicking on your ad.  
| ActionDevice | _String_ | The device on which the conversion event you are tracking occurred.  
| ActionReaction | _String_ | The number of reactions on your ads or boosted posts.  
| ActionTargetId | _String_ | The id of destination where people go after clicking on your ad.  
| ActionVideoSound | _String_ | The sound status (on/off) when user watches your video ad.  
| ActionVideoType | _String_ | Video metrics breakdown.  
| ActionConvertedProductId | _String_ | Converted product ids - for Collaborative Ads.  
  
### `AdInsightsMMM` report

**Note:** As of July 06, 2026, support for the `AdInsightsMMM` report is temporarily disabled. For more information, see [July 06, 2026](https://docs.cloud.google.com/bigquery/docs/transfer-changes#Jul06-fb-ads).**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
``| Target|  _String_|  The ID of the Account to get insights for.  
``| TimeIncrement|  _String_|  The number of days of data aggregation.  
`account_id`| AccountId|  _String_|  The ID of the Ad Account associated with the row.  
`campaign_id`| CampaignId|  _String_|  The ID of the Campaign associated with the row.  
`adset_id`| AdSetId|  _String_|  The ID of the Ad Set associated with the row.  
`date_start`| DateStart|  _Date_|  The starting date for insights retrieval.  
`date_stop`| DateEnd|  _Date_|  The ending date for insights retrieval.  
`impressions`| Impressions|  _Long_|  The number of times the ad was served.  
`spend`| Spend|  _Decimal_|  The total amount spent.  
`country`| Country|  _String_|  The country for the metrics.  
`region`| Region|  _String_|  The region from which the ad was viewed.  
`dma`| DMA|  _String_|  The Designated Market Area for the metrics.  
`device_platform`| DevicePlatform|  _String_|  The platform of the device used.  
`platform_position`| PlatformPosition|  _String_|  The position on the platform.  
`publisher_platform`| PublisherPlatform|  _String_|  The publisher platform.  
`creative_media_type`| CreativeMediaType|  _String_|  The type of media used in the creative.  
  
### `Ads` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the Ad.  
``| Target|  _String_|  The target field used to retrieve the ad.  
`name`| Name|  _String_|  The name of the Ad.  
`status`| AdStatus|  _String_|  The status of the Ad.  
`bid_info`| BidInfo|  _String_|  Bid information associated with the Ad.  
`bid_type`| BidType|  _String_|  Bid type associated with the Ad.  
`campaign_id`| CampaignId|  _String_|  The ID of the campaign.  
`adset_id`| AdSetId|  _String_|  The ID of the ad set.  
`creative`| AdCreativeId|  _String_|  The ID of the ad creative.  
`configured_status`| ConfiguredStatus|  _String_|  The configured status of the Ad.  
`created_time`| CreatedTime|  _Datetime_|  The creation time of the Ad.  
`updated_time`| UpdatedTime|  _Datetime_|  The last update time of the Ad.  
`conversion_specs`| ConversionSpecs|  _String_|  Conversion specifications.  
`failed_delivery_checks`| FailedDeliveryChecks|  _String_|  Information regarding failed delivery checks.  
`recommendations`| Recommendations|  _String_|  Recommendations for the Ad.  
`tracking_specs`| TrackingSpecs|  _JSON_|  Tracking specifications.  
`ad_active_time`| AdActiveTime|  _String_|  Active time parameters.  
`ad_schedule_end_time`| AdScheduleEndTime|  _Datetime_|  Scheduled end time.  
`ad_schedule_start_time`| AdScheduleStartTime|  _Datetime_|  Scheduled start time.  
`bid_amount`| BidAmount|  _Integer_|  The bid amount.  
`last_updated_by_app_id`| LastUpdatedByAppId|  _String_|  App ID that last updated the ad.  
`preview_shareable_link`| PreviewShareableLink|  _String_|  Shareable preview link.  
`source_ad_id`| SourceAdId|  _String_|  The source Ad ID.  
  
### `AdCreatives` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the ad creative.  
``| Target|  _String_|  The target field.  
`name`| Name|  _String_|  The name of the creative.  
`applink_treatment`| ApplinkTreatment|  _String_|  Deep link treatment for the ad creative.  
`body`| Body|  _String_|  The body text of the ad block.  
`call_to_action_type`| CallToActionType|  _String_|  Type of call to action.  
`effective_instagram_media_id`| EffectiveInstagramMediaId|  _String_|  Effective ID of the Instagram media.  
`image_hash`| ImageHash|  _String_|  The hash of the associated image.  
`image_url`| ImageUrl|  _String_|  The URL to the creative image.  
`instagram_permalink_url`| InstagramPermalinkUrl|  _String_|  Permalink URL for Instagram.  
`instagram_user_id`| InstagramUserId|  _String_|  Instagram user ID.  
`link_og_id`| LinkOgId|  _String_|  Open Graph ID of the link.  
`link_url`| LinkUrl|  _String_|  The landing page URL.  
`object_id`| ObjectId|  _String_|  The associated object ID.  
`object_story_id`| ObjectStoryId|  _String_|  Object story ID.  
`object_type`| ObjectType|  _String_|  The type of the object.  
`object_url`| ObjectUrl|  _String_|  URL of the object.  
`page_id`| PageId|  _String_|  The associated Facebook Page ID.  
`product_set_id`| ProductSetId|  _String_|  Product set ID.  
`run_status`| RunStatus|  _String_|  The run status of the creative.  
`source_instagram_media_id`| SourceInstagramMediaId|  _String_|  Source Instagram media ID.  
`template_url`| TemplateUrl|  _String_|  Template URL.  
`thumbnail_url`| ThumbnailUrl|  _String_|  Thumbnail URL.  
`title`| Title|  _String_|  The title text of the ad creative.  
`url_tags`| UrlTags|  _String_|  URL tags parameters.  
`adlabels`| AdLabels|  _String_|  Labels associated with the creative.  
`object_story_spec.link_data`| ObjectStorySpecLinkData|  _JSON_|  Link data specification.  
`object_story_spec.photo_data`| ObjectStorySpecPhotoData|  _JSON_|  Photo data specification.  
`object_story_spec.video_data`| ObjectStorySpecVideoData|  _JSON_|  Video data specification.  
`object_story_spec.text_data`| ObjectStorySpecTextData|  _JSON_|  Text data specification.  
`object_story_spec.template_data`| ObjectStorySpecTemplateData|  _JSON_|  Template data specification.  
  
### `AdSets` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the Ad Set.  
``| Target|  _String_|  The target field.  
`name`| Name|  _String_|  The name of the Ad Set.  
`budget_remaining`| BudgetRemaining|  _Integer_|  The remaining budget.  
`campaign_id`| CampaignId|  _String_|  The associated Campaign ID.  
`status`| AdSetStatus|  _String_|  The Ad Set status.  
`billing_event`| BillingEvent|  _String_|  Billing event criteria.  
`created_time`| CreatedTime|  _Datetime_|  Ad Set creation time.  
`daily_budget`| DailyBudget|  _Integer_|  The daily budget limit.  
`lifetime_budget`| LifetimeBudget|  _Integer_|  The lifetime budget limit.  
`end_time`| EndTime|  _Datetime_|  Scheduled end time.  
`start_time`| StartTime|  _Datetime_|  Scheduled start time.  
`updated_time`| UpdatedTime|  _Datetime_|  Time when the Ad Set was last updated.  
`recommendations`| Recommendations|  _String_|  Recommendations for the Ad Set.  
`targeting.genders`| TargetingGenders|  _String_|  Targeted genders.  
`targeting.age_max`| TargetingAgeMax|  _Integer_|  Targeted maximum age.  
`targeting.age_min`| TargetingAgeMin|  _Integer_|  Targeted minimum age.  
`targeting.countries`| TargetingCountries|  _String_|  Targeted countries.  
`targeting.location_types`| TargetingLocationTypes|  _String_|  Targeted location types.  
`targeting.regions`| TargetingRegions|  _String_|  Targeted regions or states.  
`targeting.cities`| TargetingCities|  _String_|  Targeted cities.  
`targeting.zips`| TargetingZips|  _String_|  Targeted zip codes.  
`targeting.custom_locations`| TargetingCustomLocations|  _String_|  Targeted custom locations.  
`targeting.geo_markets`| TargetingGeoMarkets|  _String_|  Targeted geographic markets.  
`targeting.interests`| TargetingInterests|  _String_|  Targeted personal interests.  
`targeting.behaviors`| TargetingBehaviors|  _String_|  Targeted user behaviors.  
`targeting.device_platforms`| TargetingDevicePlatforms|  _String_|  Targeted platforms.  
`targeting.publisher_platforms`| TargetingPublisherPlatforms|  _String_|  Targeted publisher platforms.  
`targeting.instagram_positions`| TargetingInstagramPositions|  _String_|  Targeted Instagram placement positions.  
`targeting.page_types`| TargetingPageTypes|  _String_|  Targeted page types.  
`learning_stage_info.status`| LearningStageInfoStatus|  _String_|  Status of the learning stage.  
`learning_stage_info.conversions`| LearningStageInfoConversions|  _Integer_|  Conversions during the learning stage.  
`learning_stage_info.attribution_windows`| LearningStageInfoAttributionWindows|  _String_|  Attribution windows for learning stage.  
`learning_stage_info.last_sig_edit_time`| LearningStageInfoLastSigEditTime|  _Datetime_|  Last significant edit time in learning phase.  
  
### `Campaigns` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the Campaign.  
``| Target|  _String_|  The target field.  
`name`| Name|  _String_|  The name of the Campaign.  
`buying_type`| BuyingType|  _String_|  The buying type.  
`configured_status`| ConfiguredStatus|  _String_|  The configured status.  
`effective_status`| EffectiveStatus|  _String_|  The effective status.  
`status`| Status|  _String_|  The current status of the Campaign.  
`created_time`| CreatedTime|  _Datetime_|  Creation time.  
`objective`| Objective|  _String_|  The selected campaign objective.  
`spend_cap`| SpendCap|  _Integer_|  The maximum lifetime spending cap.  
`daily_budget`| DailyBudget|  _Integer_|  The daily budget.  
`budget_remaining`| BudgetRemaining|  _Integer_|  The remaining budget for the campaign.  
`lifetime_budget`| LifetimeBudget|  _Integer_|  The total lifetime budget.  
`bid_strategy`| BidStrategy|  _String_|  The strategy used for bidding.  
`start_time`| StartTime|  _Datetime_|  Scheduled start time.  
`stop_time`| StopTime|  _Datetime_|  Scheduled stop/end time.  
`updated_time`| UpdatedTime|  _Datetime_|  Last updated time.  
`boosted_object_id`| BoostedObjectId|  _String_|  The ID of any boosted object.  
  
### `AdImages` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the image.  
``| Target|  _String_|  Target field.  
`account_id`| AccountId|  _String_|  Ad account ID owning the image.  
`created_time`| CreatedTime|  _Datetime_|  Creation time of the image.  
`hash`| hash|  _String_|  Unique hash of the image content.  
`height`| height|  _Integer_|  Height of the image in pixels.  
`width`| width|  _Integer_|  Width of the image in pixels.  
`creatives`| AssociatedWithCreatives|  _String_|  Associated creatives info.  
`name`| name|  _String_|  Name identifier for the image.  
`original_height`| OriginalHeight|  _Integer_|  Original uploaded height.  
`original_width`| OriginalWidth|  _Integer_|  Original uploaded width.  
`status`| Status|  _String_|  Validation status of the image.  
`permalink_url`| PermalinkUrl|  _String_|  URL pointing to the image permalink.  
  
### `AdLabels` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the ad label.  
``| Target|  _String_|  Target field.  
`name`| Name|  _String_|  The display name of the label.  
`created_time`| CreatedTime|  _Datetime_|  Time the label was created.  
`updated_time`| UpdatedTime|  _Datetime_|  Time the label was last updated.  
  
### `Businesses` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the business.  
`name`| Name|  _String_|  The name of the business.  
`primary_page`| PrimaryPage|  _String_|  Primary page associated with the business.  
`timezone_id`| TimezoneId|  _String_|  Timezone identifier for the business.  
`link`| Link|  _String_|  Link to the business profile.  
`created_time`| CreatedTime|  _Datetime_|  Business creation time.  
`updated_time`| UpdatedTime|  _Datetime_|  Last updated time.  
  
### `CustomAudiences` report

**Meta API field name** | **Mapped BigQuery field name** | **Type** | **Description**  
---|---|---|---  
`id`| ID|  _String_|  The ID of the custom audience.  
``| Target|  _String_|  The target field.  
`account_id`| AccountID|  _String_|  The ad account ID mapped from Account_ID.  
`name`| Name|  _String_|  The name of the custom audience.  
`description`| Description|  _String_|  Description of the audience.  
`subtype`| Subtype|  _String_|  Subtype category of the audience.  
`time_created`| TimeCreated|  _Datetime_|  Audience creation time.  
`time_updated`| TimeUpdated|  _Datetime_|  Audience last updated time.  
`time_content_updated`| TimeContentUpdated|  _Datetime_|  Time when audience content was last modified.  
`rule`| Rule|  _String_|  Rules used to govern audience membership.  
`rule_aggregation`| RuleAggregation|  _String_|  Aggregation setting for audience rules.  
`approximate_count_lower_bound`| ApproximateCountLowerBound|  _Integer_|  Lower bound approximation for audience size.  
`approximate_count_upper_bound`| ApproximateCountUpperBound|  _Integer_|  Upper bound approximation for audience size.  
`pixel_id`| PixelID|  _String_|  Associated pixel ID.  
`retention_days`| RetentionDays|  _Integer_|  Number of days members are retained.  
`customer_file_source`| CustomerFileSource|  _String_|  The original source of the customer file.  
`data_source`| DataSource|  _JSON_|  Primary data source.  
`delivery_status`| DeliveryStatus|  _JSON_|  Current delivery status.  
`operation_status`| OperationStatus|  _JSON_|  Status of recent operations.  
`permission_for_actions`| PermissionForActions|  _JSON_|  Permissions for actions.  
`is_value_based`| IsValueBased|  _Boolean_|  Flag indicating if audience is value based.  
`opt_out_link`| OptOutLink|  _String_|  Opt out link.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
