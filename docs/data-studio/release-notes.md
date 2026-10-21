---
url: https://docs.cloud.google.com/data-studio/release-notes/
title: Data Studio release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:14.062934+00:00
---

# Data Studio release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/release-notes/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data Studio release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Data Studio. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality regarding Data Studio. You might also be interested in the [Looker release notes](https://docs.cloud.google.com/looker/docs/release-notes). 

For releases earlier than May 2023, visit the [historical release notes](https://docs.cloud.google.com/data-studio/historical-release-notes) page. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/data-studio-release-notes.xml) directly. 

## September 24, 2026

Feature

**Bulk styling**

You can customize all series, dimensions, or metrics at once, or select an individual item to style it separately. Styles that you set for an individual item override styles that you set for all items.

For more information, see the [Line chart and combo chart reference](https://docs.cloud.google.com/data-studio/line-chart-and-combo-chart-reference), [Time series reference](https://docs.cloud.google.com/data-studio/time-series-reference), and [Table reference](https://docs.cloud.google.com/data-studio/table-reference).

Feature

**Connect to PostgreSQL (Private IP)**

You can connect Data Studio to PostgreSQL databases on Cloud SQL by using a private IP address. Private IP connections keep your database traffic on a private network instead of the public internet.

For more information, see [Connect to PostgreSQL](https://docs.cloud.google.com/data-studio/connect-to-postgresql).

Deprecated

**MySQL 5.6 and 5.7 deprecation**

Support for MySQL 5.6 and 5.7 in the MySQL connector is ending:

  * Creating new data sources that connect to MySQL 5.6 or 5.7 won't be possible after February 26, 2027.
  * Data sources or reports that use MySQL 5.6 or 5.7 might not properly load data after February 26, 2027.



For more information, see [Connect to MySQL](https://docs.cloud.google.com/data-studio/connect-to-mysql).

Feature

**Partner connection launch update**

The following partner connectors have been added to the Data Studio Connector Gallery:

  * [Facebook Ads Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwiyh8LyfZyQ8aG5Fp39pCsIEccpSsK-w3j8y6N-ZB3-rZJX9-aUP9C0e1F5PivZ_Uv) By Langquang. Sources: Facebook Ads
  * [Nextdoor](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx5xGzeuSxYpDnwhsjnEmprY9sB2h294iHRjaW4YoGxdc023iTwWfNVZQmxpIBe_CtzXA) By Windsor.ai. Sources: Nextdoor
  * [Attentive](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz9s4Rb2k13vtaOIg9ZdqeEArMsmzI1ch3qfwGLP4DYgypHWJ_oHEpYKmDlJepMRV7x) By Windsor.ai. Sources: Attentive
  * [Contractors Cloud](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz0G_xUNoIowgyV5SkOZrr6xknZbC-RrGQ68iyJt8Slhv4UrMB6hXx7_jkPniZuo9fxQw) By Windsor.ai. Sources: Contractors Cloud
  * [AppLovin](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwa_VfDqwKV4nU-g91I3Du2yNkUjGo6IZrsS_SeU2nHWx0nnAZWWulop_gjr6se5C0l) By Windsor.ai. Sources: AppLovin
  * [SEOmonitor](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwrkqEETu9VxmB6PY9qjlewyPaHdOeIVv-CmeqNMIUMB_8869OUENmB2kXa-duMY9kl) By SEOmonitor. Sources: SEOmonitor
  * [SimilarWeb](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxeFsVMVREcnL3ONWeGosaa_PxhjKR7CVJYvCuE93sQEpka6Yf9oPohdv_D4LLSvEGr) By Windsor.ai. Sources: SimilarWeb
  * [Salesforce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxNSTS9Oxw51dEWq547XhMy73Sw44hFa6w2gK-dYOchos0do-ovfa9buYXSUn6q9reJzA) By Dataslayer. Sources: Salesforce
  * [Facebook Ads (Meta Ads)](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwg5L8WnTzgsyCMHmKhyGoX1OadvEpaGeothozHT7ae4nNKim0hfATfgIojdpSL1xKC) By Datablaster. Sources: Meta Ads
  * [Google Search Console](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw3JAdju3IIS5dA47OcoGjShqKNQ_Z9N0r24m-FPdlX1gQa_-ld2tbbIhaTh69DCM3Qqw) By Data Bloo. Sources: Google Search Console
  * [CleverReach](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxljd9HY3q4bpQLfC_RdgImEcv7-ZvieLYsE53biXnKF8V5C1HVCSAqOKBoxsk4gCIO3Q) By Power My Analytics. Sources: CleverReach
  * [Cin7 Core AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyunnrPcqWgRkYHecPxUfGrZTQnFuK9jynShqfP5ig3OdT0KS8A_ztUIwFup0gBHZ6kxA) By Jivrus Technologies. Sources: Cin7
  * [Mangools AI Search Watcher](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwcwpBC1B5lfxYrqd_80uzzwnxWaOjKKo7ArfjglcnnreHZ-3WTwUVTMyIayLT-mmp0UQ) By Mangools.com. Sources: Mangools
  * [Amazon Vendor Central](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx2W2J3Wc7U9ExmzjSBV0q2RtRR_DwLzpNP7xcP4TtxHoA5lBPQsExmLlde7qQHKy5OWw) By Power My Analytics. Sources: Amazon
  * [快客-Microsoft Ads 串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwe2lMdXwfn76g7H0G3MnUrYmkerlw5koa5Q-69AcT0ty_fZCXjMDW8PBJrryUlYj0b) By 黑客數位. Sources: Bing Ads
  * [Leadinfo](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby1g9ueAD9P0wfa-EI5h_PYZU4W4bpHxkit_X5Vt-5iuY5QXxap3_pftCvbvPtlypgOow) By Leadinfo. Sources: Leadinfo



## August 13, 2026

Announcement

The following features are rolling out over the next week.

Feature

**Fullscreen charts**

You can view individual charts in fullscreen mode. Click the fullscreen button in the chart header to expand the chart. This feature is not available for scorecards and gauge charts.

Feature

**Rotate components**

You can rotate text boxes, images, and shapes in Data Studio. Report creators can rotate these components on a non-responsive canvas and can reset the rotation to 0 degrees.

Feature

**Center labels on stacked bar charts**

You can position labels in the center of stacked bar charts. If insufficient space is available to center the label within the bar, the label is displayed outside the bar.

For more information, see the [Bar chart and column chart reference](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference).

Feature

**Search for settings**

You can search for settings in the **Setup** and **Style** tabs of the [properties panel](https://docs.cloud.google.com/data-studio/properties-panel).

Feature

**Copy chart as image**

You can copy a chart as a PNG image to your clipboard.

Feature

**Bubble chart border color**

You can modify the border color of bubbles in bubble charts.

## July 30, 2026

Announcement

The following features are rolling out over the next week.

Feature

**Conversational Analytics is generally available**

Conversational Analytics in Data Studio is now generally available. You can now filter your [data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-data-agents#start-a-conversation-with-an-agent) by the Google Cloud project to which they belong. Agents that require additional permissions are now displayed with an **Unavailable** label.

Feature

**Email notifications when sharing Conversational Analytics data agents**

When you [share data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents#share-data-studio-users) that were created in BigQuery with Data Studio users, you can opt to send an email to notify those users of their access to the agent.

## June 18, 2026

Feature

**Viewer data refresh**

Report editors can now allow report viewers to manually refresh report data. When editors enable the new **Viewer data refresh** option in [report settings](https://docs.cloud.google.com/data-studio/report-settings#viewer-data-refresh), viewers can refresh data for a component by right clicking the component, or refresh data for a report by selecting the option in the three-dot menu.

## June 11, 2026

Feature

**Pro feature: Security and compliance enhancements**

The following features are now available to help you meet your organization's security and compliance needs. These features are only available for Data Studio Pro.

  * **[Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/data-studio/cmek)** : Use your own cryptographic keys to protect Data Studio Pro assets.
  * **[Customer-managed storage](https://docs.cloud.google.com/data-studio/cms)** : Store your file uploads in your own Cloud Storage bucket and your data extracts in your own BigQuery dataset.
  * **[Data residency](https://docs.cloud.google.com/data-studio/data-residency)** : Keep your data physically within a geographical area.



## June 01, 2026

Feature

**Regionalization in CA in Data Studio**

Conversational Analytics in Data Studio now supports multi-region BigQuery data agents.

[Learn more about Conversational Analytics in Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-overview).

## May 14, 2026

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Openindex Site](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbypxa6ZjcAKHSyQFALmy4m1-9cNIW4YLKL2HemTOJeiy1CnaYeJQUMEUxt6Fe9XKJsXOw) By Openindex. Sources: Openindex Sitesearch
  * [Ahrefs Brand Radar](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxJvi7w56sGS855CGOXK-oQIBuZ2BDz-8n7ifI758oRiKjV39kws6kCvOkWsCKYHx4d) By Ahrefs. Sources: Ahrefs
  * [Microsoft Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz6zs1e9LzXaZePukLJ-F2MJRHk2N5K9ohIiTwVoqhjaMUMg7zTXYznrjjzqrx7Y-BT) By Data Conductor. Sources: Bing Ads
  * [Reddit Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzGMe3Yn0P3dGxtCZwzmd21WgK2F2F0mPVdedSA4gPNMs3YcESmcbwwX7UtzvbBkP0hyg) By Data Conductor. Sources: Reddit Ads
  * [App Store Connect Reviews](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbywpcD8bmcshgM7Sqr3TRR6EYbCeaNZ57cdb7YnGEvLKrID6-VmqFkzA2UBkWg_FV_Duw) By EMLLC. Sources: Apple Itunes
  * [mailXpert Reports](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby7eY3auBjCgJUG5aZwWM4uGDGs7Gs4URiemim1An06sYC7ydaivfHFFnMQbNOL01ke) By mailXpert GmbH. Sources: Mailxpert
  * [Eskimi](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxI6EJby6RZz5NhT0ZeeZiYmsI3jmoKsK7P025LARGLNt0LoUO0dlkPQTTk6FzRybxyrg) By Supermetrics. Sources: Eskimi
  * [Gong](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwCyG96mBk9SgpKUE8t8JubAhhtnFNGR-liWaC1yaAan2KbHqy8CTvrfPgEXo2tvQhc9g) By Supermetrics. Sources: Gong
  * [Odoo](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwxy6_6ZLC1nabJ97Td_gf398Qkf5jaASJ8B4wukgf-6m8GvqD4cbU1MAd3iRYDVfmJ) By Supermetrics. Sources: Odoo
  * [快客-SHOPLINE 串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyJdIrq1gBRfMB65wHqMizU-pxCgjeEsvtj8Pa-LZp0F0TLyRdYWGzoCDLOAuI1KIm0Dg) By 黑客數位. Sources: Shopline



Feature

**Improved chart configuration for series limits and grouping**

For Area, Bar, Column, Line, Combo, Pie, Time Series, and Treemap charts, configuration settings for limiting the number of series displayed have moved from the **Style** tab to a new **Display** section in the **Setup** tab of the **Properties** panel. This new **Display** section lets you configure **Top N or Bottom N** series to display and includes the option to aggregate remaining results into a single category. This feature was formerly called "**Group others** " and is now labeled **Group the rest as "Others"**.

## April 30, 2026

Deprecated

**Ads Location Extension fields deprecation**

The following location extension fields in the Google Ads and New Search Ads 360 connectors are deprecated and will stop serving data on May 4, 2026:

  * Affiliate location address line 1
  * Affiliate location address line 2
  * Affiliate location business name
  * Affiliate location city
  * Affiliate location country code
  * Affiliate location phone number
  * Affiliate location postal code
  * Affiliate location province
  * Store location address line 1
  * Store location address line 2
  * Store location business name
  * Store location city
  * Store location country code
  * Store location phone number
  * Store location postal code
  * Store location province



Reports that use these fields will return an error. To avoid disruption, you must update your reports and data sources to use the corresponding **Asset location** fields:

  * "Asset location address line 1"
  * "Asset location address line 2"
  * "Asset location business name"
  * "Asset location city"
  * "Asset location country code"
  * "Asset location phone number"
  * "Asset location postal code"
  * "Asset location province"



[Learn more about Ads location assets](https://support.google.com/google-ads/answer/2404182).

## April 16, 2026

Feature

**Data Studio rebrand and updated home page**

We've rebranded Looker Studio as Data Studio. We've also updated the home page to give you a single place to access your Data Studio reports and data sources, BigQuery conversational agents, and data apps built in Colab notebooks. For more information, [see our blog](https://cloud.google.com/blog/products/data-analytics/looker-studio-is-data-studio).

Feature

**Gemini in Looker is now Gemini in Data Studio.**

[Learn more about Gemini in Data Studio.](https://docs.cloud.google.com/data-studio/gemini-overview)

Feature

**Share your BigQuery data agents to Data Studio**

Available in preview, you can [create data agents in BigQuery](https://docs.cloud.google.com/bigquery/docs/create-data-agents) and then publish them automatically to Data Studio for use with [Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents).

Feature

**A new Conversational Analytics experience**

Available in preview, Conversational Analytics offers a new experience with the following changes:

  * Conversational Analytics is now available to all Data Studio users.
  * Conversational Analytics no longer requires that Gemini in Data Studio (formerly, Gemini in Looker) is enabled.
  * You can consume data agents that were created in BigQuery, but can no longer create data agents directly in Data Studio.



To access your past conversations and data agents, you can switch back to the legacy view of Conversational Analytics as needed.

[Learn more about the differences between the legacy and new Conversational Analytics experiences.](https://docs.cloud.google.com/data-studio/conversational-analytics-overview#legacy-new-experience)

Feature

**Pro feature: Manage sharing policy for assets in team workspaces**

In Looker Studio Pro team workspaces, assets such as reports and data sources might not have an individual owner. This can make it difficult to manage sharing permissions for those assets, especially if the person who created the asset leaves your organization.

If an asset is located in a team workspace or folder, a Policy User may be designated for that asset. Looker Studio uses the Policy User's account to determine which organizational sharing policies apply.

[Learn more about Policy Users](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports#how_policy_users_work).

## March 23, 2026

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [LinkedIn Ads - Free](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbw0Zp7XTHptRua3qYL7libAaqb4zcuUfDjGzVvumCsf6ehZ4D3loh40iqTEAePuh0MWbA) by Data Bloo. Sources: Linkedin Ads
  * [Bing Webmaster Tools - Free](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbzv55V76IUMmpU4JmlarDvI5_ESb1RCbdrxT94qgvNohT-Hhnq-qopt1Upb5uPMef4W) by Data Bloo. Sources: Bing Webmaster
  * [Surfer AI Visibility](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbwnHyCmyHRwsedwa6ScbuaXA6qr3khXPxfC8QmdffOAuAiPAt_5ZS-g1fZKUzpyphOI) by Surfer SEO. Sources: Surfer SEO
  * [Airtable](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbysg0xvcvnWkLHm7sMEpMeg4GbSj6tFe_QLTmu8Anq0exQCCbWujj5jEquQkmQMQvWk_w) by Windsor.ai. Sources: Airtable
  * [Apsis One](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbwNYVdU9Lqrv7NVXze57iYMwYwtQIUqsC8yMqkmmwl23w2V2AtmJcpbpTgG3UxdKRiT7Q) by Windsor.ai. Sources: Apsis
  * [Writesonic GEO](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbyajIohcwJS5Ri8T5A-stqdX-02-xvzFgOVrQl05DAeHi8vnlH7Dc8ZKapgC4DFf77K) by Writesonic. Sources: Writesonic
  * [Metricool](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbz71DjunH_TABnMqgrjQeuyqOYMyvrgvhOu1DXfk0np6Z8mk61srVPsp6BWCJUmh4X8) by Windsor.ai. Sources: Facebook Insigths
  * [Reddit Ads](https://lookerstudio.google.com/c/datasources/create?connectorId=AKfycby4pYclYR9vo5vB9Kemz_oIQNaTx5Ga9WOSkpt900EeHI4rhSPNFrQeXAn7m8mpSnpw3A) by Reporting Ninja. Sources: Reddit Ads



## March 16, 2026

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [SE Ranking: Domain Analysis](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyoI781s9aLmME0rL5BybPZKGE1DfyO4be7lJJTk37gkeDbm1KZZ9leCeo3eIfpKDNnxA) by SE Ranking. Sources: SE Ranking
  * [HighLevel](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwz3uCUtcyXcSaI5HbD3_CKkfXtC6pHFiYbH8OJOZ_fMxIaXIX39GGmWfgojQMlM9p_cw) by The Data Students. Sources: HighLevel
  * [Google Ads Keyword Planner](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzCyEmM1cx0ddiUDzMcTwwK9MTjdvr5ema_TXksfw4yo8TiNkZGK91JgZyu0EmD6tL7sQ) by Supermetrics. Sources: Google Adwords
  * [Plausible](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwLgnT6AO94-jQJDDxXdPzscV1kJR5BL1pJJV3n1-gBWEeTKcqbUs5ron1oOF_Aa5bT) by Supermetrics. Sources: Plausible Analytics
  * [Axon](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwlee3JN-dsCre-Dk48Vd6QPuox68a3r5xvDBpMCSpkyXPxI3GK9gbaQualAPCUujdnmg) by AppLovin by Supermetrics. Sources: Axon
  * [Eloqua](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwq8yr-rNUUH4Q81iNnNgdL5VkqWu7Mukpho-10z1rx-f02BePGNlIGmuKarCEZ_30Z) by Supermetrics. Sources: Eloqua
  * [YouGov BrandIndex](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxV8RM9OPp5NLGrYjW-94ZyBVWSpSa5ToNuCuPPhdr8pAQ-u6vhzZe-rTXlsjL8Qz0G9A) by Windsor.ai. Sources: YouGov BrandIndex
  * [Commercetools](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzt_64a--CQOCegiZNj2EbjtTL8IstMKB4nn6G8Uqiidltwyha8l7psP-xp50oYA2vw3Q) by Windsor.ai. Sources: Commerce Tools
  * [PostHog](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyLQhrcKSaW-OWOgmaLKbJjQ5-iCM_uflrg69t85uRWJ2ztntCCsGvIBfSZk0cK6Hh7ew) by Windsor.ai. Sources: PostHog
  * [BoxCast](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwAHP5OFi63Ns6ZMjUIwoFyIdPMnI3_5jKB1Bb3SMoFbdToqzJzRZGBAyDsC7-XURUenw) by Windsor.ai. Sources: BoxCast
  * [Visma Economic](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzPKxjtKnUTN6i79jpPNryO4Kd_hw4H4sf88SpL03-H66WTCa0yER5fd0vNNOg1Ga7E) by Windsor.ai. Sources: Visma Economic
  * [Rocket.Chat ](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyxeQ93bDQU-GitiRfrrgNigewXcTDgXp5qTr9n5ObXsa6Mq0J09rXyJrdnHVYVpfStcw)by Windsor.ai. Sources: Rocket Chat
  * [MediaGo](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxRo7jariGDX1iwFy47UwkvHOjT1T-yogXJsjfze-fmSwib1-kBz9nfimn4TUsGHTANtg) by Windsor.ai. Sources: MediaGo
  * [MNTN](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyaVuEWbyYtfj_Gh8VHRmz4aEc73gJmKJZ1U0AX8QZEix4Ow6kYIovIkWJsvqnA7ZKfYA) by Supermetrics. Sources: MNTN
  * [Facebook Ads](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwxZ2TyYkA2MuRC5luGQ0IKdIZ8fqzqPnQoKABsDl_5CQQGRvYFb4Fs-mpqZrmLdmsQ) by My Pro Metrics. Sources: Facebook Ads
  * [SE Ranking: AI Search](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxl5pAEsvW6OvIGYW5g52eFM7eY7hq7D39stQhPflMBC6VIeMV8ri839s5XgC5m6yW4) by SE Ranking. Sources: SE Ranking
  * [SE Ranking: Website Audit ](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxt15nabAn9mtk9vC7Qlx1y_FtqV_QELU25zxw6CBIPH1fS9SgNrbCf9UOvknO7334p2Q)by SE Ranking. Sources: SE Ranking
  * [Meta Ads Data](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzYiaXfct2gqqK3eM7QEek2vYvFyjaKgk-iK9_I3c2wMRUWLE1Gm1oI1YEpYkyhOz3F) by Mercury. Sources: Facebook Ads
  * [快客-Shopify 串接 ](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxU243pVFLKWoJtG6MQurT_PHzilnguy-ig8XQLrGev1Ca76vlgeMcFE1bbZz-rkv1xSA)by 黑客數位. Sources: Shopify
  * [SE Ranking: Keywords](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyluIKgHrlpOOQsCKPt44SLGF-l0KwQIzOnQP4YELhutV9bDEaeWDSyjK2IKIMV5367) by SE Ranking. Sources: SE Ranking
  * [Pinterest ](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwjKjix-k_fYVAkwdmv8YqR2r14lLFl-8ZxnL3eI4v96dvS1Zi4t8asdmLkzDy59Qee)by Master Metrics. Sources: Pinterest



## March 09, 2026

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Peaka](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzAkhGsKvv3xV6qO10BPjS4DCBuCwF6-6cHnOVEONufpGh6LH6mAnTSocuiYV6cpv3j) by Peaka. Sources: Peaka
  * [Google Search Console](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxaTO9XShCgBKdCoZ5TCxw363lTpUdiRIhdBPoPY8pstIBpkSoG2M_lYHZ8o81K77y8Vg) by Porter Metrics. Sources: Google Search Console
  * [Vista Social](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyOsYCtmZhfwXJo2ZOczdbJ_8whHPlPCsDtp_w7u4FSzfafSk3NfC6EoKdROcrTEk0Q) by Vista Social. Sources: Google Analytics
  * [OtterlyAI](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwy_SdUOJsCQoH2NC52qRW5pX4Vj1FbFbKf8AMtLTuzsXtXgjtP3FmBfiAsoLEC7NFA) by Otterly AI. Sources: Otterly
  * [Livedune](https://lookerstudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyOX0sK2KfuVNaDS16_cdd5iUDJposy6Ww6GF9ZzjLtHQ8RwGvHqE85ebwBoNeE4YGd6g) by Livedune. Sources: Livedune



## March 06, 2026

Feature

**Correction: CSV connector enhancement available to all users**

Enhancements to the [CSV connector](https://docs.cloud.google.com/data-studio/upload-csv-files) user interface are available to all Data Studio users. This feature was previously announced as being available only to Data Studio Pro users.

## February 12, 2026

Feature

**Additional search parameters**

When searching for reports or data sources, you can filter search results by the following parameters:

  * Type
  * Owner
  * Location
  * Date Modified



Feature

**Pro feature: Change the billing account**

You can change the Google Cloud billing account that is associated with a Looker Studio Pro subscription without interrupting access to your Pro assets.

[Learn how to change the Pro billing account](https://docs.cloud.google.com/data-studio/change-billing-account).

## February 05, 2026

Feature

**Now displaying Conversational Analytics reasoning**

After you enter your query, click **Show reasoning** to see a plain text explanation of the steps that Conversational Analytics took to interpret your query.

See [Show reasoning](https://docs.cloud.google.com/data-studio/conversational-analytics-looker-studio-data#show-reasoning) for more information.

Feature

**Link to chart in report**

You can now link to a specific component, like a chart or control, in your report.

See [Link to a component](https://docs.cloud.google.com/data-studio/link-to-a-page#link_to_a_component) for more information.

Feature

**Looker Studio Pro for Google Workspace**

You can purchase a Looker Studio Pro subscription from the Google Workspace Admin console.

[Learn more about Looker Studio Pro for Workspace](https://support.google.com/a/answer/16695590).

Feature

**Export chart to image**

You can now export a chart to an image by saving it as a PNG file or by copying it to your clipboard.

See [Export data from a chart](https://docs.cloud.google.com/data-studio/export-data-from-a-chart) for more information.

## January 15, 2026

Feature

**Show and hide individual charts and components**

You can hide individual charts and components for all viewers or for a subset of viewers.

See [Hide report components for viewers](https://docs.cloud.google.com/data-studio/hide-report-components) for more information.

Feature

**Cross data source filtering**

This feature lets you override default field IDs so that controls on a report can filter charts that are based on different data sources.

[Learn more about using controls across data sources](https://docs.cloud.google.com/data-studio/use-controls-across-data-sources).

Feature

**Histogram chart**

You can visualize your data using histogram charts. Histograms are useful for understanding the shape, center, and spread of your data, which in turn can lead to insights that might be hidden in other types of charts, such as pie charts and bar charts.

See the [Histogram reference](https://docs.cloud.google.com/data-studio/histogram-reference) for more information.

## December 23, 2025

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Walmart Connect (Search)](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycby_xocEYcq3ExlUWou1dYimI_GSmng_K3XLUe91QJfjCpJ4jyfPec0xwJiGidnD0qtK) By Supermetrics. Sources: Walmart
  * [Ecwid](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbw63zvfWMvjRnbCWzndGoXDNQ8_YpZtw5buNpwR8axalHbnJWo4P8xTIYu0OYpdRpsR8g) By Supermetrics. Sources: Ecwid
  * [Bitrix24 BI](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzUoCZuMLzQ2-MsxxJdnFUtrEVgWN5UMRl6XT_MD8hc3Ixm9_lanhMZnPlYOrp7epGv) By Bitrix24. Sources: Bitrix24
  * [Zen AI - Google Ads](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxYFaFFq4gwsF40zBWaMB2oGnztTlBd8qDv5ecQp8uOIFUMMQgvhmP1jXehcVkSrOCn) By Zen AI. Sources: Google Adwords
  * [G2](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxy1wsBER4Su5hJG5L3LrfR-Kv8wCdiTvXb1-K3085pgW5qu0qKTwFDJxAgAU7eHwT7) By Dataslayer. Sources: G2
  * [TikTok Ads](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwkfb_SRAdkZz8dDnSBVEpHEJmSf9f_GQaKpKzvDkshTuTeMx0Nn5ITlW5dvKRyPNBD) By Pro Plugg. Sources: Tiktok
  * [Mentionlytics](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyKdcq8JKHWuduHxxpPavi6dK0-8cLiMIhBNPv98SA5GRhGJ1R0pfhoxbpeuapiugBg) By Mentionlytics Ltd. Sources: Mentionlytics
  * [Shopee](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwgGYEZgfEuYPWLi8aYFFTaVF1yrHrUOp-u19vM0lkWyc1pF64FKbvQvArxOA4VgqJ8kg) Ads By Supermetrics. Sources: Shopee
  * [Odoo Attendance AppiWorks](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbx-MwMWtaKLhocCVMKckTw9dwBJPgFVpR3aTqgwlANycH9Bu5MsQ4mZpLGXpwWeAZ5S) By Jivrus Technologies. Sources: Odoo Attendance
  * [Squarespace Commerce](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyL6viOBhJKrz9pkjx9_LsJ27eHdxRxAEQ2OgR7zNRF0F0ZPFFoeVdOOB5o8mZgvxicVA) By Supermetrics. Sources: Squarespace
  * [Wix Commerce](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxjrbLfpLUFmx3a9mlubnGAVl67M_aKgaOTA72lJWVwav6E6sG5upg2vPVhyeBjL7QAag) By Supermetrics. Sources: Wix Site Data
  * [SISTRIX Toolbox Data](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxoeJCApl5PlFxpDkCzVh41SyM66ElBur4I-EOiO2o8lrw9QeGA1j8WnKJLeXf_khixtw) By SISTRIX GmbH. Sources: Sistrix Toolbox
  * [Sprinklr](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwsorYTwObAzde5dg7KRFKPcTlbqY4zZjEQO7PdDQaOdGOTeulZw4EN9dhy6te3KDC5iw) By Supermetrics. Sources: Sprinklr
  * [Facebook Insights](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwHuccCK6JlvMSaE5hRO6EuPHhcXwuHftRLnUqGPheZGLk3Mchxqf7jjH4cVpJIl73d) By Data House. Sources: Facebook Ads
  * [Bluesky Insights](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycby5rCuXgKeSR6HxhI4sfpCDKkMzhGUKsW4ojD-2K0lKNtTViRVHNs6dtGY6v_AEmNRA) By Digital Data School. Sources: Bluesky



## December 11, 2025

Feature

**Pro feature: Share and schedule reports with Slack**

You can now [send Looker Studio reports to Slack channels and Slack users](https://cloud.google.com/data-studio/slack) on your Slack workspaces. This feature is now out of preview, and remains available only to Pro users.

Feature

**Expand tables to show all rows**

When downloading or scheduling a report, you can now configure table visualizations to expand to display up to 2,000 rows.

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Bionic](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyYyLrOKZTsVxJXDa_rtgOBAMB5OP25fItahHVWpt_V3URQGtL6bWmj5zpRySFuEhZl) By Bionic Advertising Systems. Sources: Bionic
  * [AI Search - Workduo](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbydPMhgUsBE9Xei5zKRsMk6em5TFowQ7ApNn3gGyYgy20K4ZeULx3x5gzot3waudO5x) By Workduo. Sources: Workday
  * [Zoom](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzy2oOq30g15Xx_e4sczv8urbuZRqLt-J6vFmludalOkch1gtqSchLOBZ1kAsy5EXmk) By Windsor.ai. Sources: Zoom
  * [Bing Ads](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbx1dnYsG4ixIzHYhVV64BbHXtwU8gNPdaQpvcOeM3IlEm8VEAW5Vtf5kQ6uOqRfcD0imw) By Master Metrics. Sources: Bing
  * [快客-Cyberbiz 串接](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxbedCQYaYROkY_PnPaohwjPBoJxb32UMt2dashE98xomU5L55driNgeTlt2JXxVZLt) By 黑客數位. Sources: Cyberviz
  * [GoHighLevel](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxXtvJOpR2NpjT06-wvdXxha9ZxTYTTl4ZHLN8i70yCWFsjWjtd2Hs6UQak6CGh3w_R) By Windsor.ai. Sources: HighLevel
  * [Walmart Connect (Display) ](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbz-KHDiIfoxdx1qLlIlwzhEjyfPHt-8d37eq85bosE6hYEKYZhGlwHsYUdqoI9HyfNa)By Supermetrics. Sources: Wada



## December 05, 2025

Feature

**Pro feature: Schedule hourly report delivery and alerts**

Users of Looker Studio Pro can create hourly schedules for [report delivery](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery) and [alerts](https://docs.cloud.google.com/data-studio/create-alerts-on-a-chart).

## November 13, 2025

Feature

**New shapes**

The **Shapes** menu has been enhanced and expanded to include new shape types for report editors. See [Add text, images, lines, and shapes to your report](https://cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports#add-shapes) to learn more.

Feature

**Modernized timeline chart**

[Timeline charts](https://docs.cloud.google.com/data-studio/timeline-chart-reference) have a new modernized look by default and give you new options for customizing bar corner radius, axes, and grid.

Feature

**Filter control default values now accept parameters**

You can now use parameters as default values in [filter controls](https://cloud.google.com/data-studio/drop-down-list-and-fixed-size-list-control).

## November 06, 2025

Feature

**Looker connector enhancements**

The Looker connector now supports query results of up to 75,000 rows. The Looker connector also supports exports of up to 75,000 rows of data.

[Learn more about the limits of the Looker connector.](https://cloud.google.com/data-studio/limits-of-the-looker-connector)

Feature

**Conditional formatting for bars in bar charts**

You can now use [conditional formatting](https://cloud.google.com/data-studio/use-conditional-formatting-rules) on bar charts that use [modern charts](https://cloud.google.com/data-studio/modern-charts).

Feature

**Pro feature: Cloud Audit Logs**

Looker Studio Pro logs are now available in the Logs Explorer within the Google Cloud console.

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Google Ads with AI ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby3UAD0XBUnkphNODSThkFtLPkcOYkPyjWIQjNRK1uL8lysqeW2JrB3g01ZzpYPrkFG6Q)By Picometrics. Sources: Google Adwords
  * [DataTrue v2 ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwqbL7hblpix15aFjw7cCP-ZQ1OWR1czrR0E27Q2KKZaFrAq3sWpp4Lf5x1QwAI7Ydv)By DataTrue. Sources: DataTrue
  * [Lazada Ads ](http://lookerstudio.google.com/c/datasources/create?connectorId=AKfycbyWlSLq6YPAITvM-beqsNtDzfAuy_1vlIJZL3bMN1qWZVAaOwCkVHvJnwvxIMO036Beww)By Supermetrics. Sources: Lazada
  * [OmniWallet](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyQyXDpWLw4opurQzr6jD4JrKM1xWOJxwzOeOqPynRE97SfyDhesp4uUxg7r98Nj5Bs) By Dataslayer. Sources: OmniWallet
  * [TikTok Shop](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwWGY9lnaNbN1nmG22dlYdIIdOysS0EoO5VdqQi8X9Xa_dwNLOWQ9-ajvD2DnDzuVuftQ) By Catchr. Sources: Tiktok
  * [Local Viking](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyCcSPS1Nn4iKuQbg3apV37RGf9XIISNg4A7iN4uuSLrbCxueDqJKDUrz8huOSNAjw) By Local Viking. Sources: Local Viking
  * [Sprout Social](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz-Z8Q-EA_DZMdtsK2Q8y88wV4YoaO7WbC1ScMVo8AYmAPSxTtLL1zkYe8Dlydc8bPT) By Windsor.ai. Sources: SproutSocial
  * [TikTok Shop](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwCoQTFhTegtKQC6txTrT2TQW5zIhWq9-pUGfNgCooRgNbP_C3cjP1cb1J8QzBRaFooWg) By Windsor.ai. Sources: Tiktok Shop
  * [Hurma By Hurma](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx_vskKFf605onuL2BQtYwKFAJ_HtGVRuZNTIdqz-pxqSNNFvEk_rCbVVIQB5HETvsV3Q). Sources: Custom JSON
  * [Google Sheets By Supermetrics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbywumdWEe4eeYlrrxe36PEX1wbe73Tdv1fklVk_WKgQiLaQuLjqVYAtZwRiAGwylyLR). Sources: Google Drive



Feature

**More data from Google Ads**

You can visualize the following metrics using the [Google Ads connector](https://cloud.google.com/data-studio/connect-to-google-ads):

  * Conversions (Platform comparable)
  * Conv. value (Platform comparable)
  * Conv. value / cost (Platform comparable)
  * Cost / conv. (Platform comparable)



## October 30, 2025

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Spotify Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwR-miifksERqS7lMjiTazGziKqjKGzDlcgUSIh1pgu9D44oujskaVa_dH3jxk6PzdB) by Dataslayer. Sources: Spotify Ads Studio
  * [Amazon Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwj34XShbwrvIvD80r4O1hPfJhmIT4MyrufaGLIZ7O1fdKpOngJwRUYELHJ2Kd_7oVCDg) by Dataslayer. Sources: Amazon Ads
  * [Zoho](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwrDpzIrsawTL3Q5sNb7V4zYeC4YnQmXCVfpZD4jo-KikeRJGKdMIKT18_4uqAG2UtWDQ) by Dataslayer. Sources: Zoho CRM
  * [Lazada Commerce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyfT8Zow-HVyofJTbdzC2kQK_cu2GyguqW3Q-jpop9cyD_iqEXx2dfBQWRH54hM77Nxcw) by Supermetrics. Sources: Supermetrics
  * [Google Sheets](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbweOFmmcwVCMX7Ztuf43DFa_ZRlGe-WRx42Q1JIoZRrGQp9IWUvhlNhYHSHPyJtvJZQ) by Porter Metrics. Sources: Google Drive
  * [OWOX Data Marts](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz6kcYn3qGuG0jVNFjcDnkXvVDiz4hewKdAFjOm-_d4VkKVcBidPjqZO991AvGL3FtM4A) by OWOX. Sources: Owox Data Mart
  * [Close CRM](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwEEiTbWi5t1uJUGqTfI7V2xTSVJh9Td7FnLDQjE98cX_RwNDTxT_SsGFOx8UJKy0sB) by Supermetrics. Sources: Close
  * [Centra](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw263f4ssbUAj5tpgK9Pku6eOz35pW80T4lPo46cZBBTYkJ5Wn4i2FvagOlg6sRb6gw) by Supermetrics. Sources: Centra
  * [BMS Monitoring](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzkOpFnVzObPoimJk0J4gNjhuIeS3s-iUda6mwGwNcjz5m_YdBDfvGC4NW-PiqR7v_p) by BMS. Sources: BMS
  * [Vibe](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw521HWPONl6boUDoOsBfVdCHGDrw0bIlRWXqgaHeFl1hMNYGxPcHj0bOzt1_zZIMXM) by Supermetrics. Sources: Vibe
  * [Power My Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbztUN74F880Usj83EIIPIAovGMVTcEPw2BeqezyrIYmoPaxiZTkCAkMZA1izoXyOGwP-Q) by Power My Analytics. Sources: Constant Contact
  * [Zen AI - Meta Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz_PfwpONjz4jgSbL0olsmjd6uGxKOncqB50HwLSkOcQUnCnBkow3D4dVpnvd62M1R7XQ) by Zen AI. Sources: Facebook Ads



Feature

**Pro feature: CSV connector enhancement**

Introducing new user experience enhancements for the CSV connector.

[Learn more about the CSV connector](https://cloud.google.com/data-studio/upload-csv-files-to-looker-studio).

**Note:** This feature is being released gradually. You might not see it right away.

## October 16, 2025

Feature

**Pro feature: Share and schedule reports with Slack**

You can now [send Looker Studio reports to Slack channels and Slack users](https://cloud.google.com/data-studio/slack) on your Slack workspaces. This feature is only available to Looker Studio Pro users, and is available in Preview.

Feature

**Vertical stacking in responsive reports**

Responsive reports now support vertical stacking. You can add multiple components to a column within a section. [Learn more about creating responsive reports](https://docs.cloud.google.com/data-studio/create-a-responsive-report).

## October 02, 2025

Feature

**Double-click to resize chart margins**

You can now double-click the chart boundaries of a time, a bar, a line, an area, or a scatter chart to reset the boundaries to their default settings.

Feature

**More data from Google Ads**

You can visualize the following fields using the the [Google Ads connector](https://docs.cloud.google.com/data-studio/connect-to-google-ads):

  * Conversions (by conv. date)
  * Conv. value (by conv. date)
  * All conv. (by conv. date)
  * All conv. value (by conv. date)
  * New vs. returning customers
  * Gross profit
  * Gross profit margin



## September 25, 2025

Feature

**Looker connector enhancements**

Looker data sources now display the names of fields without their prepended view names. Fields are now nested under their corresponding views.

[Learn more about how Looker Explore data appears in Looker Studio](https://docs.cloud.google.com/data-studio/looker-explore-data-on-a-looker-studio-report).

Announcement

**Partner connection launch update** The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Odoo Appointment AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyKBjl1L9qGPkR-ERD4_BLQolUiCALNF7ppooIKVsg8FHM6B1OwQ3XjnU-BpPm6Sj_4hA) by Jivrus Technologies. Sources: Odoo Appointments
  * [Snowflake](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzSAJfSriuVnEgcbc2z9A_-SnEQUrRhoUeZudlMo_t85zRzdriQ7wrrdMl3cAAB4-t9) by Supermetrics. Sources: Snowflake
  * [GA4 Annotations](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyWc3cRhp0s7dBwqFP1HNNQMJgPbRtZoLoeU1-qEvFpIO3uUTlQqFHRGzAIi6hjwHGQ) by ReallyGoodData. Sources: Google Analytics
  * [800.com Call Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwFxudGjImI2xkftCwjNjlXofJys5t0moeiaC2OiYa2jDhGLzNKzWqlVWbJInrDUGkf) by [800.com](http://800.com/). Sources: 800com
  * [TikTok Shop](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyhewrvIcVbREi1zLgeRkcoN7j1kksA9b5avAZ4d5OcN43qwuIRpKEU7P_pAzwRU3vZ3Q) by Supermetrics. Sources: Tiktok Shop
  * [seoClarity Keyword Details](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzvh7g6vDntUVul6HqdZ4ZvbhCchnJGwbwiwTrNQlsmSXwKWkrKkNVktd4d0Ix9JY-t) by seoClarity. Sources: Seoclarity
  * [seoClarity Domain Summary](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxVxqmXgZ9TIXxl53hh9d9VWBJNMx6v9l7WE11MpeBA44znnIL5N64RNd6NaHak5ohfIw) by seoClarity. Sources: Seoclarity



The following partner connectors were released during the week of Sep 15, 2025: 

  * [Odoo Subscription AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxMRNCFSH7HapyVJ7bVqy5xO6RG2uhhGmJghsWu7j-VUgKLb0z7trA--1tGQnsy0lIi) by Jivrus Technologies. Sources: OdOo Subscription
  * [Amazon DSP](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxI7H3509PmHuXeMH0tTPP8eNdXZSX-S557j6vGsiBO7WuE4j0FBXmCWLm8HeetGX5L) by Dataslayer. Sources: Amazon Ads
  * [Etsy](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyy47DbcXHBaT030gT2DaP5BVF695ackMNZ--R0xYddjCRvFamIhPlEXg0ZvIVsu9g6) by Power My Analytics. Sources: Etsy
  * [SeoSamba CRM](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby830zJaL54q2fBJD0-TUvQqbmDgmu8rn7zIrpyQ0iIw0Tkw3m5a7A6zcAJqdx-eHajFQ) by SeoSamba. Sources: Seosamba CRM
  * [Google BigQuery](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyScsUpnZ0qg5-27_nFnoK6lv-MFFjAhZeCq5cB-e1qcpucAuqRMB7v7Y3EkzIg_XysgA) by Supermetrics. Sources: Google BigQuery
  * [Microsoft Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxfiswH68PUPg49b4HYo67snSv6ryTYVs6nbv6kDvfVdlthnV4Ctk87IpeqST-kADi-) by Porter Metrics. Sources: Microsoft Ads
  * [Outbrain DSP](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx0daIKIS3Y8eQkSoMvCceTwM0Og1UGIMbSBp4R5pi8JuKhKL-vnDEDfIEKTl8R0WCT) by Catchr. Sources: Outbrain
  * [The Trade Desk](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzAxz0lvl8vvnyWF7MuK6vP9hQ2LsdWbBPNjqR-SUOj-L8AG7ZiLMPTERGIC0Mag3DxQQ) by Catchr. Sources: The Trade Desk
  * [Close.com](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzgWpNdMcGAFgg0dHRmXTF8KB78QzIkJQjSvmXQHwUnWHU6Dc-1k9Y8sm9RflEoJTnFRA) by Windsor.ai. Sources: Close
  * [Odoo Invoice AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzEmnybF5t-t_0x5DjpPH2rfUSOcPiDu_CeOEggi4r18nGy5zRHyuGaZZhAG4FnogsN) by Jivrus Technologies. Sources: Odoo Invoice



Change

**User interface change: "Add quick filter" is now "Add filter"**

We've made a wording change to the filter bar in the report editor. The button label that previously said "Add quick filter" is now "Add filter." The functionality of quick filters hasn't changed. [Learn more about quick filters](https://docs.cloud.google.com/data-studio/add-a-quick-filter).

Feature

**Table charts support up to 10 sort fields**

Report editors can now configure up to 10 sort fields for table charts. 

[Learn more about configuring sort fields for table charts](https://docs.cloud.google.com/data-studio/table-reference#default-sort).

## September 11, 2025

Change

**Looker Studio Explorer (beta) feature deprecation**

The Looker Studio Explorer (beta) feature is being deprecated and will no longer be available. 

**NO ACTION is required**. Existing explorations that were created with the Explorer will be converted to reports automatically.

[Learn more about the deprecation timeline and details](https://docs.cloud.google.com/data-studio/explorer-sunset).

Breaking

**Hyperlinks and images are disabled for data sources that use Viewer's Credentials**

When you enable [Viewer's Credentials](https://docs.cloud.google.com/data-studio/data-credentials-article#viewers-credentials) for a data source, Looker Studio won't render hyperlinks or images in dimensions from that data source.

This limitation does not apply if the report creator and the viewer are members of the same [team workspace](https://docs.cloud.google.com/data-studio/about-team-workspaces).

Feature

**Treemap chart improvements**

Improvements to Treemap charts include the following:

  * A new [**Fields** section in the **Setup** tab](https://docs.cloud.google.com/data-studio/treemap-reference#fields) that lets report editors specify a dimension or a metric to use as the basis for chart coloring
  * New [color options](https://docs.cloud.google.com/data-studio/treemap-reference#color-by) that are based on the selection in the **Fields** section
  * A new [**Border radius** setting](https://docs.cloud.google.com/data-studio/treemap-reference#treemap) that lets report editors control the border radius of tree branches
  * A new [**Label** section in the **Style** tab](https://docs.cloud.google.com/data-studio/treemap-reference#treemap)



Change

**[Pro feature] Number of scheduled reports increased to 200**

You can create a maximum of 200 schedules per Looker Studio Pro report.

Feature

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [HubSpot](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzLO9Joey9S8pWji3AEcDzMS9uNL_mEoeIk9-DVmnigCmRYFZZQ4EOs-vWQwHrWkytM) by Adzviser. Sources: Hubspot
  * [Amazon Seller Central](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw_WtmPOiq-SvHp8iyukc_tof6n9ln77qpYFnPFxLktTiNGruZPAq_DAqUZceUZIB167w) by Adzviser. Sources: Amazon
  * [Amazon Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzjoSyVodFAKjAGzL8OEPMRQz58veiyWlEhih2FoDvkE2bspkh-XpoOH_G-i_aEx7YoTw) by Adzviser. Sources: Amazon Ads



## August 28, 2025

Feature

**Vertical stacking in responsive reports**

Responsive reports now support vertical stacking. You can add multiple components to a column within a section.

## August 21, 2025

Feature

**Sort table charts by up to 10 fields**

Report creators can now set up to sort 10 fields for table charts, including fields that are not selected in the chart.

[Learn more about sorting table charts.](https://docs.cloud.google.com/data-studio/table-reference#sort)

**NOTE: This feature was not released on 8/21, and will instead be included in a later release.**

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Shopify](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz4pWVRzSmsZW5GTiNRCIpoht5cIvXdVKZZOaqxEfn0o2AeiUu03FvmuF2eVjLf9g) by Master Metrics
  * [Tienda Nube](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzy6be4NcuLE1dPNEEe2lYloTtOeTMKKdg1PiNUhSsBKI4WHNdeDlzvUnP0x-IJMU5C1w) by Master Metrics
  * [Google Merchant Center](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyH7vTUbfM8dee-rd81Kz_26ocBFSoYk5ashmL-iS_DTHOKC3VpV6jYDioapM0VnW9-) by Dataslayer
  * [Google Keyword Planner](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx_qZeerLIkOSSKF4qfh_DHegtRtfqY3LkNIZ2iDck99LOu4kASb5tGYMuWEwDCXjhOAA) by Dataslayer
  * [Mangools SERPWatcher](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxuzqyOw81C5Sx4fgdVOKzlbb0x69yG8KMDB1TBeAjkYZ9RAZKYRAsFsuSmlo7yiUa1) by Mangools.com
  * [Pipedrive](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzc5VI3ryJ9r5Co7W6gNhHWCQ60p5rgv1JQkaHTHwSLaDvVDunEAFY2ey0RhRvWBhez) by Master Metrics
  * [Facebook ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyJwICE7-IUO7G-yqJH4iITJdy-qiBwP7GR3BNaVMczYA5Gl1nTBCBmvKVnE5grXZEJLg) by Middly
  * [Google Merchant Center](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzwXq_I2JzUW7fP30S8Yt3yw4uuL7a-42QA01Gs9iffFzmS-M7tTkqGqJUiGVO-MogMXQ) by Windsor.ai
  * [FB Page Data with AI ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx-evkBGl7tOmW2bcZI8uRyXRN8ptAeJTS2DBG0ohaevHOGEDtcdw50vdZOOh3eedHzYw)by Picometrics
  * [LinkedIn Ads with AI](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwXBQ2mJsc6zzvMRDCWF7FjFJ6ZM3uI8WEx7pRrJw_pYTBdVTOqeUK4Z0fw6xVlLEr5dw) by Picometrics
  * [快客-GA4串接 ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwtc-WNl6I2iqns2CQpY34pAYt06imqcWEwsOnrbTkQUPMj0SS1lEdvl1m5tVG0Aat2gQ)by 黑客數位
  * [seoClarity Keyword Tags](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwUeVIqa3zSmvfOllVOl1UxuyyXWDA3QyBIteGXbgtk6QpfCEBCiz-rVQqHRi1BWhuKtA) by seoClarity
  * [GA4 with AI insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwobh-FYFmkvolmDFbwiNe4In4bCXdbybZqmVk0AvwD8HXpZUY_d9Vf3tEqpsytvx_A) by Picometrics
  * [Tracktest Company Results](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxz_-3GaMOZCSqIWbgkUYHVw90nLr5UnEEN3lOzaM9w6wlnRX6SerL_rAYqogqJ6Dk) by Tracktest s.r.o.
  * [快客-GAds 串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby-veEILFCeH1iAWDuRoS4nECtdAcd7AIQetfQw0uwf8qTgqB_eHdqBtzXj-_t9RHjD) by 黑客數位
  * [Salesforce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbze1haIhtOD6hugcWx0fXEkHzvhUfppQtMxgsotU8BBGq0KdBziOvaYWx-5cQGWBxkmBA) by Adzviser



Feature

**Looker connector respects LookML`value_format` property**

When you're using the Looker connector, value formats that you apply using the `value_format` LookML property will now be displayed in Looker Studio reports. You can [view and edit the value format](https://docs.cloud.google.com/data-studio/format-fields-in-reports) as usual. 

Note that the syntax for [conditional formatting using `value_format`](https://docs.cloud.google.com/looker/docs/best-practices/how-to-conditional-formatting-with-value_format) is not supported in Looker Studio.

## August 14, 2025

Feature

**Background colors for bar and column chart labels**

You can now set a data-label background color for any bar-label-position option for column and bar charts.

[Learn more about data labels for bar charts and column charts](https://docs.cloud.google.com/data-studio/bar-chart-and-column-chart-reference#data-label).

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [快客-Thread 社群洞察](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx-5v5c23SZHmYYdn8rtPMdrtp2AR6pZkv0Etf04ubhuWVDKLpWn-Pae_ASAwrt9jHM) by 黑客數位
  * [Beeswax](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzWMxaRfmrDUBM8W6RYqnzetrRWMr2SQOYJrb861wWO8NfknNcOXge1pAlczWzJtxdNvQ) by Supermetrics
  * [PrestaShop](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwr_429EhHgwlwhLOW3nejQC6WyQv_NGynlq7pl9zzsj0K25Yv00w8oJsWmAfidKqRt9A) by Supermetrics
  * [Moloco DSP](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx58ajkmtC2EAZGCi15-6BA7JKOnT4rlKZ-VUN8DT1dFzVgaUGKO8U8D48Hu8lSrdm1Eg) by Supermetrics
  * [Google Merchant Center](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz5TU7acC_WVTZl-kwkt2YDVIU4rtcbjvf4xgu6TiplRk47ZNEe-C1ZgGLmsZbOGIsA1Q) by Power My Analytics
  * [Shopee Commerce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzKH1iA7BPT-zrgf0V1bgGab2bSEQ8qYmjs-s_5bzZOX_67nVJv47zdA6hvZ_FZce9plw) by Supermetrics
  * [Ad & Analytics Datastore](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyngerwlFcmxNb8g4LxrYEicQdYhEux4MhAqN45XL7U-UZTdAoja__n9xCxBqNm76Q) by ReportDash
  * [WooCommerce AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw9YFaxOvx3lAcvDFh7sZCAIKZ0nT_CglD5PqkrpVZgUxdIaYN-83HVt2hoCDCL6fU) by Jivrus Technologies
  * [快客-Threads 社群洞察](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwWt-0PJVJFUj5cCF2fUhukdIWCLbmgWcrtfd7NO28jMQTs3yhGEq7bjMPlzeyrD6q8) by 黑客數位
  * [快客-META 社群串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyDyKIBhESiCiYzKL02Sz_hp-vtoXosSP5G5k9FEzqq6ruEVVh0e7AnW8YhqtB5PPo-) by 黑客數位
  * [快客-GSC 串接 ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwupviNFLmEC_0AIs2h6kvd6ifnYU4Qu6aYvnc584isNINAIROrLuZPY4IPwgoCWRhj)by 黑客數位
  * [快客-LINE Lap 串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz2CiCtnLB2HbXvYbWkY2Btf9Lrkr2QZHsgsx7z60eY6CmOABAdQhuEwG-QLg3wuvPoNw) by 黑客數位
  * [Odoo Expense AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxc76_HThU2ehU6JPBbyZAo40P4LQlNfbKKEtCcq2nHXu8TLbDxQIW-D7RcA14YJd18wg) by Jivrus Technologies
  * [Facebook Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzJb-naOdFHqAyDt5fmEmOPFopqAZHtoo1sNDQZyy_vGf6o43H5rnN3hG3pFkrEZfJaQw) by AlkhwarizmiMetrics
  * [Salesforce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzGGmFRG-H_tCX5GCiWTq_25S0uhoBzuuOJYOX5U9Y1_Gzgd4H81cq_uH69gOiRNXm7hg) by Power My Analytics
  * [Google My Business](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzvalrID7qdJPwE_OUddBcD_jnXhAm41NVD2wc44FeH0ni3EqVpI3MBJWQ8TtZWzeJ5) by Master Metrics
  * [Azure Table](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwu9gC-ppIJ_krBx2WjplRWcaY_Ebv1K4o4n3NvUd22b5TzoF742n7SN1C2CG88KiHf) by Windsor.ai
  * [快客-META串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwmgGYSudETSGmrsNkLf89mI2vSwJQ3BMI3lb-x6wOW1XtPIkduF24SBc8mWUef4IkV) by 黑客數
  * [Instagram Business Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzWDrMXgZfi7e_jQpUnRscxLoeleFLlu4M4L3uVoq2-pqc0_9tCbIiQH6EwfkVwKZiV) by AlkhwarizmiMetrics
  * [Deputy](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzFPblJ7VhZ91weXvyjuWTS6SxSEw8ry_-2-5MekXCgLnE2Y3ZjHPmycvSwodxzQqLI) by smblytics LLC
  * [Onfleet](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyQ9Vf3ofsv2ZHjPaPQn4RGVsXHQdtYHpMW39gMOlKXI_FwnMQhsVZb-lvwkW3y2ysK) by mblytics LLC
  * [Yoom](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyhQ9KGAIgFDilNDduQdEh719X1lYIKn3VITLQErLJX2ahCs8z8oFs5I0KsCbH1fuNDwA) by Yoom Inc.
  * [Shopify - Cratos.ai](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbym5Xi083ojxkJNBG5sDPsaF4VDpOa4wMOTmdMmcNSNxy7lNcc7djjfALIJAXoWzZui) by Cratos.ai
  * [Snapchat Ads - Cratos.ai](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyBjDhWfO87jav7CkYjHN7JU7sbITii4HG-pmKVob4Z6xJPk3g10GqFHrHt4yHXJ2AwWA) by Cratos.ai
  * [Linkedin Ads - Cratos.ai](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyyGddnNyWxhQ1aNunXbaW_9IQsEpcKmI2Ts6fqK0Rdbv2iBjZtIgGTey2GGadjvcpYXA) by Cratos.ai
  * [Google My Business - Free](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyR64HkgLS64iITb4Oq9YkP1Qd4vkMszYP4UyrsOQ4VyqORSX7PhTZyGVptdcyxsx8) by Data Bloo
  * [STAT Rankings: Site](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxGFCBfCYbIMo87BcSR8EGdL9xanIkn_nPOovl3C4U8H8WUjXQ9aQYRpYmUiMu1Yn0dHw) by Moz, Inc.
  * [STAT Ranking Distrib: Site](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyqBusDrpHK7NWZOSnxVJwO_jekZGhbDveAVVVcPz2pmykQ1iymQJbSTMMq2--8bwv8) by Moz, Inc.
  * [STAT SoV: Site](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzQtHLKe_ChzC2BE03mJLcMoGu7wHdVX-haKLXzlaSUsnfOHIvRaX88JQ_xpJgBg2eemA) by Moz, Inc.
  * [STAT Rankings: Tag](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwBovDqr6J8xdsOw5_RUXemk1AQeU41G40K2Kdl0qzp5-woliEJy_JZvmMeLh_itOkxkQ) by Moz, Inc.
  * [STAT Ranking Distrib: Tag](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyLjP87uj3RJnDLAWa9ceKIwseVguTV5t-FhTGCF92n3XiZFrUmoNWFZO2rOveecWm91g) by Moz, Inc.
  * [STAT SoV: Tag](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwk-PW71bJXDM9TbBRTj8s4Dz9YVzdYd2n0y4MPQ-7l2ZzzDg-apv2o8CTiuAJOHaPtbg) by Moz, Inc.
  * [Zid Stores](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx0VcwERl2DTT4XR6YJDLIDMYggvyNMYuZs0LHBXEbiRrkCqqsIK-ih4HyZ4utYwkH_) by AlkhwarizmiMetrics
  * [Tiktok Ads - Cratos.ai](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyj9tISTP01rOX26y-yu79goaB2uh8--kv_3M19_EPac2x5vAhXLXd1BCS1cx0JCvXY) by Cratos.ai
  * [Plausible Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz88iSK4B6V-VoaiwocFu2dDp3CBRM0arAZoDjQ97SroAt9RtzgS6z3UCxpjJDi0ieVjQ) by Plausible Analytics
  * [Salla Stores](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyYmQrwSV6AICXJKLmAcQiMjNPz1rj1DCB9VYpqTcfMvEmXs8fOnuXGamX_RYhTQ65K) by AlkhwarizmiMetrics
  * [LinkedIn Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby_34rTtFWxsR2u7JKQWRoPrnDAIyjP0qknJ-RxfCBBCzzAxy15VnPR7GdLQRUWwptX) by AlkhwarizmiMetrics
  * [TikTok GMV](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw9I9a9u4dmSgcWI88Z9-89Wyz0_qML732iTmuEfIvsTtsenM89w48OcJmQO4v0cw8R) by Catchr
  * [Xandr](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyTBLL1tEFu2iaRmgl0ZeSe2142Ql_bWKgFTnkSfot1J9hQsXZM0gS0hM3ccLmzvYLf) by Catchr
  * [Google DV 360](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxAg51dlRGm7mBH5nk7j-v2ZOYai1c88sasjQMoA1Xk1CTQl8XsRUaYfav_REulWBWw) by Catchr
  * [Facebook Page Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwu4mqzjaqv2vElxmwWqu_akTZw5In1CImb3tmcBhpSdbaVwOkfpX4DraiyJSu6_L9H) by AlkhwarizmiMetrics
  * [Kommo](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwrRFH5keyxT6tMTfVlO0V3aHBqE97VYsdti4Dy_5EtAMlDBZGV4nswb7j5Q42y-iNLsQ) by Master Metrics



## August 07, 2025

Feature

**Looker connector enhancements**

Looker connector support for selected [calculated field functions](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector) is now [generally available](https://cloud.google.com/products#product-launch-stages).

Feature

**Conditional formatting in query result chips**

You can now apply conditional formatting to change the background color and text color of query result chips.

Feature

**Data label improvements for waterfall charts**

Report creators can now specify the position of data labels for waterfall charts along with the level of data label text contrast. 

[Learn more about waterfall chart data label options](https://docs.cloud.google.com/data-studio/waterfall-chart-reference).

Feature

**Custom columns and custom dimensions in New Search Ads 360 Connector**

The New Search Ads 360 connector now supports custom columns and custom dimensions. You can add any of your saved Search Ads 360 custom columns and custom dimensions to Looker Studio reports and join them with other fields in tables and charts.

## July 25, 2025

Announcement

**Pro feature: The Code Interpreter is now available in Preview**

The [Code Interpreter in Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter) is available in [Preview](https://cloud.google.com/products#product-launch-stages) for Looker Studio Pro subscriptions. The Code Interpreter translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations. The Code Interpreter is disabled by default.

## July 24, 2025

Feature

**New report canvas sizes**

Two new preset canvas size options are available, letting you control the width and height of your report on the screen. The new options are size A4, available in portrait or landscape orientations.

[Learn more about report and page layout options.](https://docs.cloud.google.com/data-studio/report-and-page-layout#canvas_size)

Feature

**New alt text field for images**

You can now [add alt text to report images](https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports#add_images) to make them accessible to screen readers. See the [Web Content Accessibility Guidelines (WCAG) guidelines on alt text](https://www.wcag.com/blog/good-alt-text-bad-alt-text-making-your-content-perceivable/#What_is_alt_text_and_who_does_it_benefit) for more information about writing alt text.

Feature

**Looker connector enhancements**

Additional [calculated field functions](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector) are now available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

**Add descriptions to reports**

You can now add text descriptions to a report. The report search now matches the report title as well as the description.

Feature

**Performance improvement for BigQuery data sources**

Report viewers may notice improved performance when the report uses a BigQuery data source.

The BigQuery connector supports short query optimized mode. In this mode, when BigQuery determines it can finish a query quickly, BigQuery prioritizes returning immediate results instead of creating a BigQuery job. Short query optimized mode may apply in the following situations:

  * When the data source uses Viewer's Credentials
  * When the data source uses Owner's Credentials but you are not the credential owner. 



There is no change in user experience or report behavior for data source credential owners.

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Google Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzSwavmpb_HOJ-mGTQh58_JV1lqbY8tOcvry3mi_kFOESRMIb9UDCTimctyOo9lMBL4SQ) by Detrics
  * [Facebook Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxEIVPCXZyTPZtOtQPQl0nPfgtEwdKKDFGTt8GYSN2q9aKaTakYIlKf8lqYeyNGGcUm) by Master Metrics
  * [Instagram Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyrOltbWEyCaf6MLjLwsX_a7ny5xyCbGY4nrm0pyukmPLA9wD63ESClQ3UtETodJSS1) by Master Metrics
  * [Youtube](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxa0z7PzIBswipUWcFWPN5LRce5Rvb0KbSuR-hN05InreICPCvyso359bGFrG7_063i) by Master Metrics
  * [Google Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx8LrzHexCTkTBGu5AJntmDe-q8IYWKMxF0DfphW9s6P4YdPh9OHDUk9nGWNqffyCuoPQ) by Master Metrics
  * [Google Analytics 4](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwZ-OALYuQvZPoMf4Zs3cRFBAgfc-lll8TYKN2qF6WDSpj6PrXqb9gScu2z_k_HOQK4Rg) by Master Metrics
  * [Dashbo](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx0NZ5e2MMISr6toZCb7PoxooYfIFuDdQwCW4oWnpxjtNfwR80SkV8aAiibLnKlCRTEDA) by Dashbo
  * [Odoo Sign AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxCH6kb7jGrVV36u6ZBiweYnJVWWKQd7tE1mZu7GVG_Vw6dmot89sL86giHoND-rh0t8g) by Jivrus Technologies
  * [快客-GSC 串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby-SaBW_LVIVAyuI7q1PQhqqKbwcxp0kaCrCYi0Wj3nVlIJFENFiWOQP_MvfCgpFpY) by 黑客數位 
  * [IntelliKid Systems](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbznaukKHnRM-AtDjqYNKotj8BCXBZdmlcLZw4cIhy67a1NjaJWQWF7Med9GEDAgDSPG) by IntelliKid Systems LLC
  * [Odoo POS AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxDTDWkPSwYKH096FJ-XK-KSr23-aEVeyxGeSgSTnpF3P8Rggd3ar5GgLeY0zK8FkQL) by Jivrus Technologies
  * [Google PageSpeed Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzEvtbGv2c24ZXDnJ55sjQVYfmfvyjJlK-OajreKH_OQVxWq5TGFMahS-O62t76ZBLd) by Supermetrics



Feature

**Highlight charts by filter**

The [Applied Filters panel](https://docs.cloud.google.com/data-studio/about-filter-properties#multiple_filters_on_a_component) now lets you click on a filter to highlight all charts that the filter applies to.

## July 17, 2025

Feature

**Report abuse**

Looker Studio report viewers can now [report abusive content](https://docs.cloud.google.com/data-studio/report-abuse). Content is automatically reviewed, and content that is reported as abusive is hidden or deleted.

Feature

**Performance improvement for BigQuery data sources**

**Note:** This feature has been delayed and is currently not available. (Release note updated on July 21, 2025.)

Report viewers may notice improved performance when the report uses a BigQuery data source.

The BigQuery connector supports short query optimized mode. In this mode, when BigQuery determines that it can finish a query quickly, BigQuery prioritizes returning immediate results instead of creating a BigQuery job. Short query optimized mode may apply in the following situations:

  * When the data source uses Viewer's Credentials
  * When the data source uses Owner's Credentials but you are not the credential owner



There is no change in user experience or report behavior for data source credential owners.

## July 10, 2025

Feature

**New alignment option for Cartesian charts**

The new **Align with grid** setting lets you set the alignment of the chart legend with the position of the chart grid, instead of aligning with the chart title. 

This setting is available for Cartesian charts in reports that [have modern charts enabled](https://docs.cloud.google.com/data-studio/modern-charts).

## June 26, 2025

Breaking

**Don't display data in comparison metrics when Group others is enabled**

The **Group others** option could display incorrect data when used with [comparison metrics](https://docs.cloud.google.com/data-studio/add-comparison-metrics-and-running-totals#differences_between_running_calculations_and_calculated_fields). Comparison metric fields now display the string `no data` when the **Group others** option is enabled on a chart.

Feature

**Looker connector enhancements**

The Looker connector can now connect to a [private IP (private services access) only](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) Looker (Google Cloud core) instance or to a [private IP (Private Service Connect)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) Looker (Google Cloud core) instance [using the Looker instance ID](https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil).

## June 18, 2025

Feature

**Updates to Assets: search API endpoint**

The Assets: search API endpoint now includes a `previousPageToken` attribute in its response. This token allows API users to paginate forwards and backwards through the result set.

## June 03, 2025

Announcement

**Pro feature: Gemini in Looker is enabled by default**

For Looker Studio Pro subscriptions that are created on or after June 3, 2025, [Gemini in Looker](https://docs.cloud.google.com/looker/docs/overview-gemini) is enabled automatically. Looker Studio users with the [appropriate permissions](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-looker-for-looker-studio#before_you_begin) can manage enablement on the **Gemini in Looker** page under **User Settings**.

## May 29, 2025

Feature

**Pro feature: Code Interpreter is enabled by default**

The [Code Interpreter](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter) for [Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics) is now enabled by default when the Gemini in Looker and Trusted Tester features settings are enabled for the Google Cloud project that is associated with a Looker Studio Pro subscription. The Code Interpreter in Conversational Analytics is a Preview feature that translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations.

Looker Studio users with the [appropriate permissions](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-looker-for-looker-studio#before_you_begin) can manage enablement on the **Gemini in Looker** page under **User Settings**.

## May 22, 2025

Feature

**Chart Properties panel improvements**

New improvements to the **Properties** panel **Setup** and **Style** tabs let users [customize charts](https://docs.cloud.google.com/data-studio/types-of-charts) with a more organized and user-friendly flow.

Feature

**New user consent flow for BigQuery data sources**

When you're querying BigQuery data sources with **Viewer** credentials, a new user consent flow is available to verify that your email credentials can be logged.

## May 15, 2025

Feature

**Set links to open in new tabs for pivot tables and table charts**

The new **Open links in new tab** option lets report editors specify whether [hyperlinks that are included in the data](https://docs.cloud.google.com/data-studio/hyperlinks-in-data) will open in a new tab.

**Open links in new tab** option is available only for [pivot tables](https://docs.cloud.google.com/data-studio/pivot-table-reference) and [table charts](https://docs.cloud.google.com/data-studio/table-reference) in reports that [have modern charts enabled](https://docs.cloud.google.com/data-studio/modern-charts).

Feature

**Looker connector filter enhancements**

The Looker connector now supports the **Matches (advanced)** filter condition for text and number filter types, in addition to the data and time filter type. This support applies to filters from Looker data sources that are defined in LookML models with the [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) and [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) parameters.

[Learn more about how Looker Studio interprets LookML filters.](https://docs.cloud.google.com/data-studio/looker-explore-data-on-a-looker-studio-report#more_about_filters_that_are_always_or_conditionally_required)

Change

**Limiting inappropriate content in schedules**

Looker Studio now checks for potentially inappropriate content in the subject and message fields while creating and updating schedules. You won't be able to save a schedule until the flagged content is removed.

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Sitechecker](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz6shR1jlgb2y7Kyt4hgN3SDH9_Lu4JbPdMuYKCqJKlLEewlLFYTDgaElN6Yh1xmkU) by Sitechecker
  * [Smart Copilot](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzVAtcp_Xwux-Wcgr0BccgEj9lMRqo1lH6CiKA8ger-55FuvFIrFmT6_rRnJ4QM2UkznA) by Make Me Win
  * [Odoo Contacts AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxr6CoCBi0nHQItFmFbu_rRievJmpMSIpZsjjQcSpgQBj_3yMyGtDc75--LFigO0E2R) by Jivrus Technologies
  * [Odoo Documents AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby7YLZEyluLYvS3jsE9PEfQyLeFFQLSx7hqDxWdMcOW_1sbJEmRifFatMdH7joZoxTShA) By Jivrus Technologies
  * [ChurchSuite](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxorifrpBLNhfdQ6flwtaHrdKrllenBQxziS7-hc3JmK547GXnEZ6mRSLYd-8Jfc5GT) by Growing Healthier Churches
  * [Lumar](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwVqp4qzyUtZWLDUCwhoW4K2X_XV-tkh0EEHvtV2oWsnqer0bBkHk6oHs_2tAnKc0zLOQ) by Lumar
  * [Yandex Metrica](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwnEaadOsJdVpAXMxAH4fdDCse1BBD4kzAWOJBjy8D9h47mG1AlBgMsZUKJWmqj6VL8Eg) by Windsor.ai
  * [Everflow](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw9dMSVopi5DRZheZBm8kCl45Xu5cpV8eaGgv-hQgBPDhwzdZa7JYfR3JGZFnY6ZTCYgw) by Windsor.ai



## May 08, 2025

Feature

**New grid lines options for cartesian charts**

New grid line options let you set colors and line styles for individual axis grid lines, which makes it easier to distinguish between left or right y-axis grid lines. 

The new grid line options are available only for cartesian charts in reports that [have modern charts enabled](https://docs.cloud.google.com/data-studio/modern-charts).

## April 17, 2025

Feature

**Looker connector enhancements**

You can now authorize the Looker connector to use the BigQuery OAuth credentials that you use with Looker, letting you view and interact with Looker Explores that use BigQuery data in Looker Studio. [Learn more about how to authorize Looker data sources to use BigQuery OAuth credentials](https://docs.cloud.google.com/data-studio/view-and-interact-with-looker-data-on-a-looker-studio-report#authorize_looker_data_source_bq).

## April 10, 2025

Announcement

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Netsuite](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzy2dBNd9Sp9VRQbGmgDPvfy5iMojzhHhCWV1esba6n8OiAFoHqrnDTM_A3s3y3N-7k) by Windsor.ai
  * [Simplesat](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby3G-wdMKbXT4idMTuo9GT_50-uqmF1cizjeOk-57ytc0EQY5gZ8eKJq3wHv7A4nr8L) by Simplesat
  * [Pinterest Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyR6Y29IgkuWb5Z8sVDLHtU2nn1WuHMuK4PGS9YYz6CWlfBFpLPevTFYdWhSTZUtmpS) by Porter Metrics
  * [Recharge](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxX3s0nfyWZQgEq4iflIk9GuF-VYp4Ojx3qiaTNyTyV1NmTswV9zNuWZ7D1P9QVvZMH) by Supermetrics
  * [Hurma](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyOHUyqGxz0cAmUS9nXmThmLYpPykah8PuLY2ZEVmZMui27xxKoAeF02epybK5P0w1SaA) by Hurma
  * [Shopware 6 Order Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwVhJwiMqvsdJ2Gxctv-a17eIB7B7yG9EHWsA6FcIWA2gFwIXdIuUsjkCFj316Ub7X-lA) by SHOPSY
  * [Instagram Public](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyKfCCzp4blMdcNr0yjhAYnYp5WmqsXh0ZxTM2jO8m_iZdBxc3XmThgS5W7cnSZnL0LXA) by Windsor.ai



## March 31, 2025

Feature

**Modern charts general availability**

**Modern charts** offers new chart styling, new default theme colors, new chart configuration options, new axis customization options, and new chart settings that give report creators greater control over how data is curated and presented to users.

This feature is now generally available and is the default for all new Looker Studio reports. Existing reports [must be upgraded to use modern charts](https://docs.cloud.google.com/data-studio/modern-charts#enabling-modern-charts). [Classic report themes](https://docs.cloud.google.com/data-studio/modern-charts#classic_themes_for_reports) are still available in the **Themes** panel.

[Learn more about modern charts](https://docs.cloud.google.com/data-studio/modern-charts).

Feature

**Looker connector enhancements**

(This launch has been postponed. This update was added on June 23, 2025.)

The following enhancements to the Looker connector are now generally available:

  * The Looker connector can now connect to a [private IP (private services access) only](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) Looker (Google Cloud core) instance or to a [private IP (Private Service Connect)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) Looker (Google Cloud core) instance [using the Looker instance ID](https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil).



Feature

**Responsive reports**

You can now select between **Freeform** and **Responsive** layouts when creating a report. 

  * The freeform report layout is the default option. This layout is tailored for desktop screens. 
  * The [responsive report layout](https://docs.cloud.google.com/data-studio/create-a-responsive-report) scales well across many different screen sizes. Choose this layout if you expect your users to regularly view the report on a tablet or other mobile device.



Feature

**Query results variables**

[Query result variables](https://docs.cloud.google.com/data-studio/query-result-variables) let you insert data directly into text elements.You can choose a cell from a table as a "query result" to insert into a text element, and Looker Studio will keep the result up to date.

Change

**YouTube Connector update**

On March 31, 2025, YouTube changed the way views are calculated. [Learn more about this change](http://support.google.com/youtube?p=shorts_viewcount).

## March 24, 2025

Feature

**Looker connector enhancements**

The following enhancements to the Looker connector are available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * The Looker connector can now connect to a [private IP (private services access) only](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections) Looker (Google Cloud core) instance or to a [private IP (Private Service Connect)](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) Looker (Google Cloud core) instance [using the Looker instance ID](https://docs.cloud.google.com/looker/docs/looker-core-connect-to-private-ip-lsp-sil).
  * The Looker connector now supports [some calculated field functions](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector).



Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [SEMSTORM Reports](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzgmX4x055XhIV4jH4Aca7mUpJP4vo5BOlXmefGpo8q13RAF3DIAn1s_JKt4wfIxtmWGw) by SEMSTORM
  * [Pango](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxzH4zUQWBxMYerEkI4GRcbTlHsmHB8ALP-zW7hqgYX2mH4poc5pVe9-wGqfIo8ZR48) by Pango Solutions AB
  * [AppsFlyer](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyAdWws80lCF3hq87Xrip3tc3jctxhrL8wfOqrsNw-Rdpgor0qOYFRvpzUkxqPftiUX) by Dataslayer
  * [Vista Social](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwFVur9fCbEg5oWrDaFO4gGR06O_WSaTO7Wr0ll0l3MdpxOhalIaCuUEFEEE1xg6exY) by Vista Social
  * [Linkedin Pages -Free](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzHToyZ3-Jqph1AZQeOtTfM2ozwLvDOHgoiAsBnCxsLLwIo1M-SehYwxvp2W8pPkxH0) by Data Bloo
  * [WooCommerce - Free](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwtr5I-bBKAiehgHPhCn8gUBjjJb1m0rrMyN3mVHf4mQwBEpslFc3_HX64sKitJwaYz) by Data Bloo



## March 20, 2025

Breaking

**Quotas for scheduled emails**

Looker Studio now limits the number of recipients to whom a user can send scheduled emails per day and per month. See the [Quotas for scheduled email delivery](https://docs.cloud.google.com/data-studio/schedule-automatic-report-delivery#quotas_for_scheduled_email_delivery) section for more information. If you have Looker Studio Pro, no such quotas apply. However, any reports in the Owned by me folder are considered to be personal reports and will be subject to quotas. To resolve this, you can [upgrade a report to Looker Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-looker-studio-content-to-looker-studio-pro).

Breaking

**Scheduled email updates**

The following features are now available only for Looker Studio Pro reports:

  * **Send Now:** The ability to immediately send a report with email using the "Send Now" option is available only for Pro reports.
  * **Custom Subject and Messages:** The option to customize the email subject and message is available only for Pro reports. Any custom messages in existing schedules will be preserved, but you will no longer be able to edit them.
  * **Image in Preview:** A preview of the report will be added to emails only for Pro reports.



These features are also unavailable for reports in the Owned by me folder, even if you have Looker Studio Pro. To resolve this, you can [upgrade a report to Looker Studio Pro](https://docs.cloud.google.com/data-studio/upgrade-looker-studio-content-to-looker-studio-pro).

Feature

**Preview your data**

The data source editor displays a [preview of the data](https://docs.cloud.google.com/data-studio/preview-your-data) in your fields. This feature is now generally available.

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Reddit Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwtr5I-bBKAiehgHPhCn8gUBjjJb1m0rrMyN3mVHf4mQwBEpslFc3_HX64sKitJwaYz) by Dataslayer
  * [Odoo Accounting AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzakU8nMwxHiBANBw-V4l4W1ZmHcZTe4Akir0-aAzMXeW0bs9PYx0Hu72BeZscdcPRXUA) by Jivrus Technologies
  * [Spotify Advertising](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxl8DVaMYb8ybKVqY21s6geS7rEQQgV97-eZ2BsPuUxxPK3DjLH695_8Yk9prR3q_E3) by Power My Analytics
  * [Instagram Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyNVaqT-I1KvCXUNI7KT0jM2wf4dHomly8zSNwOvdeVSvgtY4FmTRHszPhjxFzpOelB) by Data Bloo
  * [Niteco Performance Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyV2Mrl3iENGrzPSlqu0UJTkiIQLzDw0OXjq0STzB_GMX1nqYzTho3qJdDhTw__P5r-) by Niteco Group
  * [Yahoo! Japan Display](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyr2gz6Qw8xOqD3NN7FQwlX7YaDwI-faUe9VQmmaN-6DvOVS-d9U7fAg7nHlW0s-UOY-Q) by Catchr
  * [Line Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbycGYRT92vASkFw-5LmPB0lizc4hBznHAs3A_vl50s7GC4DTjSPCNaoHL4hn755CUEt) by Catchr Sources
  * [Yahoo! Japan Search Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxsLT7LiiDjMVzVz61mqM_engUeMwbdfwvPdHod6fa70HNDitKLEFy40Kq5yo-hOhhr) by Catchr
  * [Oracle AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbymhW7d5mmLgOvB-RcNZ5RshPiRE6q4uaZnfpMlyCVL8JvSZzyVsZdeBvWc7x-r9AJpOw) by Jivrus Technologies
  * [Trackingplan](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwFaGuE9xN7mA8OWmENpxmyunCgXiZXPbWoIpoj4o1h3IDqCngB9fUTzVnGIK2dFOn6) by Trackingplan
  * [Facebook Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyUSloOa_HCC2CauqUm85cskRlp0vaQsi1YwKTC_v2VpgLEOjD7QYJRgREmcPzxxjN4) by Master Metrics
  * [YouTube Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwvLm8_wrvmxyksDQ-ekkh8dCrwqMIk53KISq1ha9qRwtvN_0o1M4BI3yt2VM7s282XpQ) by everythingData
  * [YouTube Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyedf6guDQ8MXX__JIJoHm1L7JTdolwQmGdyES8HIu1DTmVd6g-tIKDMUts8VuxjCo) by Two Minute Reports
  * [X Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwCCTPVuekeR6DLiQqunOCpLdpu9RKIhyXzHXPfNL-ipYcTGp71gV7-NiYMMpNeeXc) by Two Minute Reports
  * [Google Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx1Lf0tY2yOltKcA8Ilovo7TlcYshhYiaNcct2S2IVfYAZbU4II7RiI5-AFGADyu5Wq) by everythingData
  * [Hubspot](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxbTGH-MlvciFZTgCcRz03RNLki0WyyNnFYvGPQ4jOFMjBfoPB2JnlrBp7WIiCQG0Zd) by everythingData
  * [IOT Dashzoom](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwtJ17Ec3wbIk0XubPgChS2__X25_h3angMR2ITch7JE5AeEEOXKGCqdWqK1tihdTYq) by Dashzoom
  * [ad:personam Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyKfj7bmURN_WyWMXh0GNCDVDpXCsm8CfHRXTqcB46VavtQEyAb427AO0RGCKtIVirC) by ad:personam GmbH
  * [快客-Thread 社群洞察](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxSGrZA2-YBfIGuaXBTp_IBmyiaCoElqZvpw5JFdO81jXM9jgx7lValA1EW-Gthjtzz) by 黑客數位
  * [Datastore AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwB6kgDTLZrwqLCAjt5v_Kl-FY_zKrIYbwRbQ-ebwREAiFEG4WTM1B6aRgbHwjJTNYbvA) by Jivrus Technologies
  * [Google PageSpeed](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx5DNLzA-bwZXAZlTNeZ7UTTv9Loz8PP2udL3jsJsNkeREVeM-TFGYOnaI-3_dsnw43VA) by Catchr
  * [Yelp Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxbCrbs-K6kxRaYb6HpLK_CSeqSg08RVPlqoJTL5LfxrJGqjTAQ8hVsM5XSSff1WlF1sw) by Catchr
  * [Xero](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxyxSUlL6CzgYu8Vgx_n6kcaFmjFjJM1bRMdY4ZasrbyXWDZ9In_SaG315nzo2vOrsCrA) by Windsor.ai
  * [Google Trends](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby97jWW0vb1OJJnivEJpiYMAJPq5EN1uT8BsvdRThX0gN6aac9Mmke2OSZyR4Yv-euy) by Catchr
  * [Appstore Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyOAPyDVyYoCs1jGw2NJxIZoQL5aO5mRooaEmvbbz_ejLy-2MupqFbWkiYVIX1HEIZAnw) by Catchr
  * [Branch](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxdB9QH76mzCwdKoYVKSV7G0Mzg7YdHbCaMeyAYXPjHpF116rGeKhP0NtE1eD2XJnvm) by Catchr
  * [Airbnb Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxHR-9XGaD8Q9e0AHsy1DmjApZtSbPAdwwFtaZSVFtLKioV88JCsIIETE5E1tl_BYYoFA) by Catchr
  * [Booking Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxSTsYcAxtFJ1s7zUgGxkIgbKoRuMAZvortmbA4Gfw5HTb1MrUKpXtqIZiFkFdKSSnj7w) by Catchr
  * [Facebook Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwES0IkPJJGQAb63nE6gmO2kRfiTp59Cp5ZHk1Hl3QD9D8Udv8VTukip5AYawAc0aeE) by Catchr
  * [Glassdoor Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzHQ1r1AB7Zjz3xnwuQATNsg8mGwNPcbcdjbK52Ajq6mX38hLDgXqKm4VpsldlGmW0mDw) by Catchr
  * [Capterra Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxZSYqiGCcVnyVblRdCN3LfOePO9_d3TTIi07sfnYEbU1iNjTizGR0JDjhuvlEmCHQg) by Catchr
  * [g2 Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz-EAxQNG13oO8tpVlI1-i20LlAZQKCC0cP9GcF0fnB0LFylcXG2b7TVK9A1V-dx-EPzQ) by Catchr
  * [Indeed Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzPcWp9hvyu85kGccaOQ-i-PRHWgIaLdRQ4bK922SAZr4zu_m0HaTZ7Cj8HNNi7uLjj) by Catchr
  * [Tripadvisor Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzEkQhq1NMdo8RnJyKC9Oc0Rh-NdxcAUU9Y-3dBb4tJCfXeaBm0VQZwQeQtAETiaXpWmA) by Catchr
  * [Google Play Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw58z-Z347BrkKbIvWPuBilwTI3vf2ySU1LQsR3qlJCVtX6Yn4-3HILXXvMppCO41CNTQ) by Catchr
  * [Trustpilot Review](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby-9EKGuxpQBG3SHcaQguP7L-6kZ8vvfkIE8WcVp_x9agy3sgh0cYt7NmCMQ93QE4qdRA) by Catchr
  * [DynamoDB AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby6WKaDJkVpv_C7PCjpM4U1Bowkx8nK7uV63qz-pIfOv9dDdOoUb8on9dqWhd_yPXkZ) by Jivrus Technologies
  * [快客-Instagram 社群洞察](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwQ-k3WZcl851WFQe2ckSENkDLK0qupV8ELnIm9Jranp42DKIucHP6F-e91Vt29vZAg) by 黑客數位
  * [Capterra PPC](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzbT8dVRhyhnRPKVVQaVGgH_lS1wE3KxaoEhqbcIS8IpFeNYIaRVEkle4AwLpcmKWDy) by everythingData
  * [ProfitWell](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyvcB6FFpEYdEwQI39mBCD40NeB42RsIOXYmZKwJ_CD-U_iNWe0SeRO1Xbtuwpeo7hC7w) by Catchr
  * [Zoho CRM](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyIsYFI5glWCc0upZURgc28V7ldw8CClUZBdtZxGx_pwaTiG333vVPaqJDX2o67vzwQ5g) by Catchr
  * [ChartMogul](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyWzJtecrXLZeB9hhrw4tC6UqgH02wsVp1VrL-mdSVMhXG2RU_gw0W2FLTWe9EUc4Ww) by Catchr
  * [HubSpot](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxdr-RZ8Ozf6lVdjJYAf20U3oZ-UA3DHr3qAuXF5E65RhvgBMLP3kVk-vrWKiTzbMGZCA) by Dataslayer



## March 17, 2025

Feature

**Looker connector enhancements**

More Looker permissions have been propagated to Looker Studio and can now be granted to Looker Studio Pro users to perform the following the tasks on Looker Studio reports that are built with the Looker connector:

  * Scheduling report deliveries
  * Create alerts
  * Download and export chart and report data



[Learn more about permissions to use the Looker connector.](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions)

## March 13, 2025

Breaking

**Looker Gemini permission now enforced**

The [`gemini_in_looker`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#gemini_in_looker) Looker permission, available only in the Looker Gemini role, is now being enforced in Looker. This permission is required to use [Conversational Analytics](https://docs.cloud.google.com/data-studio/query-your-data-in-natural-language-gemini).

[Learn more about Gemini in Looker.](https://docs.cloud.google.com/looker/docs/overview-gemini)

Feature

**Improved event logging for Looker-based reports**

When data is downloaded or exported from a Looker Studio report that uses at least one Looker data source, the connector type for all charts in the report will be included in the Looker Studio audit log.

[Learn more about Looker Studio log events](https://support.google.com/a/answer/9690662) (opens in the Google Workspace Help Center).

## March 06, 2025

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Google AdSense ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbytZ8cOs8U5ERzWLxDBMGDFIKm9_qZuEst5zw250BxLhYwWi3PQDCuYTwEe-cl5lAY) by Kentaro Shiomi SOURCES: GOOGLE_ADSENSE
  * [PostgreSQL](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxl1patK5LYBUyxaufdHuSzttckBFbHb8CSmtivt3Gnf1ceDdBo1UCQOkyrpdSH5yNc) by Windsor.ai SOURCES: POSTGRESQL
  * [Redshift](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxSxDk4YbaD22QTjDnytMdMN16AK1dGCMOxupvzGlKw_skDqMsf-ytJ7py6cAo4dO9I) by Windsor.ai SOURCES: AMAZON_REDSHIFT
  * [MongoDB](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzTe58p51C0DTdU1Zf5HtSu6HyrepJkaRbsDkejk8h24RCDP2ivKC5VJv_DdCb211vGaQ) by Windsor.ai SOURCES: MONGODB
  * [Snowflake](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwkA1OuH5M5zaTTexJ8e0--cTwfBHm1ga_Y0rVtw4-LdSjaSSc61FhkzA3odlVoTATw) by Windsor.ai SOURCES: SNOWFLAKE
  * [快客-META串接](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwT8efc-SbgTTA-AmyghP8aM-bUvxeSZtDrPiHKvNqPVdn8EztLt_yddn21NOacSOJP) by 黑客數位 SOURCES: FACEBOOK_ADS
  * [Drip](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyDgp75njN2WJY1wF1kjfopwZ5vNY7LlguUlkpLIMKahN5PJc-Ks7M6F-p80KqeT_EvlA) by Jivrus Technologies SOURCES: DRIP
  * [Really Simple Systems](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbww8qs7bOJY8_3V28eZvbcV-S_kS140EDNESGgrxK1GZPxB2rxW_J_lQrC2eqRPQZU) by Jivrus Technologies SOURCES: REALLY_SIMPLE_SYSTEMS
  * [Survey Sparrow](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxvvN7kgPUCF9DNHB-nnRXSawlKh-nRWZBWhDZbUioS10L8T5WcQluNVdKSnS1aT8F3) by Windsor.ai SOURCES: SURVEYSPARROW
  * [TikTok Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyACEVyxgQFaOcsk0KZP4Ec15maeBKIuwdpzFocPNDd3N2BSSc7HBUNPa2Y5Eil09_WcA) by Porter Metrics SOURCES: TIKTOK
  * [Walmart US](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwJsVXS0nGpSaimMd0h15-FrI565AXy8pqoICl3EUenlnbvWA-FpAOHH0FAOE-_EM5FMQ) by Windsor.ai SOURCES: WALMART
  * [Threads Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx9Kuh-yTWPndJp_tYR45jtiUgj_lPGarXz149jynqqTfLMGtYLW1T1G86-tavXdCxg) by Supermetrics SOURCES: THREADS
  * [Active Campaign](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxuWVIMi0CKEtNKHVSwtGKr5sIED7Q_ZG083LEoKgrOaSDAFnVRyTIDQiRnjy84hRUKGA) by Power My Analytics SOURCES: ACTIVECAMPAIGN
  * [Odoo CRM AppiWorks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzEW-khdC2QXKdvBnkxH1v6imrejRqUJL8B_ACWNXZudDJ13NCwLY_rL2-fyRavGIqO) by Jivrus Technologies SOURCES: ODOO-CRM



## February 13, 2025

Feature

**Sort by multiple columns**

Viewers can now sort table charts by multiple columns by clicking multiple column headers while holding the Shift key.

[Learn more about table charts.](https://docs.cloud.google.com/data-studio/table-reference)

## February 06, 2025

Announcement

**Looker Studio documentation has a new home**

Looker Studio documentation has moved from Help Center to Google Cloud. [Visit the new documentation site to learn more about the move.](https://docs.cloud.google.com/data-studio/new-studio-docs)

Feature

**Modern charts in public preview**

The new **Modern charts** public preview offers new chart styling, new default chart configuration options, and new chart settings that give report creators greater control over how data is curated and presented to users.

[Learn more about Modern charts.](https://docs.cloud.google.com/data-studio/modern-charts)

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Refinaria by Totvs](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzgGhg0Viryztzh-_uJzSAZ0q8leD591XqBBKSGBcwysmEIhBEWLJBd-hpANX6ZoZCW0w) by TOTVS S.A.
  * [Prestashop Connector](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzn47DTUC3y4wXH1-c5mornvg9-K9R3gxr9yfTP_8LNrtaj9g4RoJD3NYjbtlpIn_j34Q) by SOLEDIS
  * [Magento](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzZfZ75ND1SfOZvfYB16B5tTWOuHQmqgQbIOhFce_hbtoDOXyUvxj8euB_xnt4-ebKJTA) by Catchr
  * [TikTok Ads CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxkwl6cHx6VlRe3NsVSSp-dSoYs1ebmcKeU-t-D-V3saYrg-gT7YdCqvYppGi7RszKn) by Kondiment Worldwide SRL
  * [GA CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzjqkvCsIbpYKMRDmm6UAH0LIkQh0hjy3hpFMORcXxo5UIVKsc_rLdZm6KdqRbvkHk9) by Kondiment Worldwide SRL
  * [IG Insights CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxh-uUayMeXGuymo3ng_HFB2xX_vUExptMtjkFAmDvIbp0oFYGXyY13jWJBazsZYK-Xbw) by Kondiment Worldwide SRL
  * [FB Insights CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwx8_Uk_PLRE9O9Clh7it1DKvZhFpn6s7Ok6wrFvcLGv4m25cUipifXF7MevYf06o7WKQ) by Kondiment Worldwide SRL
  * [Google Ads CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwKkv96nMoCSwlzCuoJNbDrsEYdRu8Vb8yaZoojjPGk9WiTiwHhs7v5l8eTifDksejy) by Kondiment Worldwide SRL
  * [FB Ads CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby0a1f2lLElLLgNl0H67XCHq1Rh4juIHlJcgbhswK_zeCWiAqxmRGJgE01CnAqQeShx) by Kondiment Worldwide SRL
  * [TT Organic CMMNDR Private](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwMHMYuoPDAUIIRvNOMJnY8GHpO34kib646c7j0WZ2T66XfjTvpN0nKOwA_sfIsurTu) by Kondiment Worldwide SRL
  * [Piano Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyg6U07ARpuqdYQj5nd3iU9N7RCQyHEFwBrV1J3ug2BzaLqURtzwjG5FOqKthupmJSHoQ) by Piano
  * [BigCommerce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz75MnczxXbzuEHbMBmNnb43fu0OlZJwnShmWXG5-OUQozBlTBFEEGgigW6Pxp2uaVq) by Catchr
  * [Snapchat Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwoKZFG4t0HEyJTlP8domBZUIgm9CNPSs7Wo48tHFKUpqt4Z5MnUdo08bLOBBUZ0EWWAw) by Reporting Ninja
  * [Gravity Forms](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwtr-w2zTyhBVUmptaLAOaBb_gXpROxtTCCEtRZJy5SS_2PnxlyQU5yhsOLFvd46NxV7w) by Windsor.ai
  * [LinkedIn Company Pages](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyhmD_qVCTVb9h7cu72CzZS-NPSI3FLcndDGBvOd8Kv-2noNUZrMwJ5589oyVRpzpah0g) by Adzviser
  * [LogicGate Risk Cloud®](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxEdSxtFh3ejyzXQZ0FCrBNFukDQQfitF1hU7KvY5gyvJOeU9JCKZN_MXf-XsevNkbj) by LogicGate



## January 23, 2025

Announcement

**Correction**

The **Modern charts in preview** feature description was removed from release notes on January 29, 2025.

Feature

**Pivot sort by any**

Users can [sort a pivot table](https://docs.cloud.google.com/data-studio/pivot-table-reference#sorting) by any metric or calculated field in a data source.

Change

**Is Any** filter condition option for Looker data sources

Previously, when the value of some filter parameters was left blank in a Looker data source's underlying LookML, Looker Studio would interpret the blank value incorrectly. With the addition of the **Is Any** filter condition option, Looker Studio treats blank LookML filter values as expected by assigning those filters a default condition that allows any value.

[Learn more about how Looker Studio interprets LookML filters.](https://docs.cloud.google.com/data-studio/looker-explore-data-on-a-looker-studio-report#more_about_filters_that_are_always_or_conditionally_required)

## January 09, 2025

Feature

**Increased field count limits for Looker**

You can now include up to 100 dimensions and up to 100 metrics in table charts that are [connected to a Looker data source](https://support.google.com/looker-studio/answer/15583342).

Feature

**Warnings for external links**

When users click an external link, Looker Studio displays a redirect notice.

## December 19, 2024

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [TikTok Organic](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycby_ya8-Qn2v8_kwtDgWJOxxb5dh_xC-75FbxedfCRD40CWP9W9wsKNInozPaJyxYAHH) by Chartica.co.uk
  * [Google Ads - Cratos.ai](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbybXecEmVQ-iFxRyORo-Mby5NSiAJHxTFTXSZmIN4amzpUhskVuUwJra_9L27v52gS9PQ) by Cratos.software
  * [Klaviyo](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyNideD5Vijda9uOKFCeS1rXlCLQY_TqDuQWlJ9wM3cib-zVFuRNKcq-ruNSAi7ecoG) by Adzviser
  * [Google Merchant Center](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbx50Z1PD54AHaU6H0O3Qze-JRBieZX7ZpipOkxZVN6f25n3u-qXsjaoKfFtiFE-PC8) by Adzviser
  * [Google My Business](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxQhTyqNIeYKzaWc8Gfs73y7IKVGwVirt6CGJcq6ZEjRV8SVbN8zHUYlbwT1yfDXCOQ) by Adzviser
  * [Mailchimp](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyccrkf9WJQcjiMw75HysMb1kLC4P1E6XPvzJZu5msWPgXFKWiH245fT0kji3AeF5Sj) by Adzviser
  * [WooCommerce](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwgfzyo2YVE9hFhmxCZdC9--PoFuXJkUSXISBEyTRC7tIGZa2e3eBU2EcIBOv2kM-RogA) by Adzviser
  * [Shopify](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbxY_fXDIDAGYY6f8iy67Km7P5OM8Y3PKZY7KVzZAaGVOVDaRt4fGGYvgbEx5tKOZUio) by Adzviser
  * [Microsoft Ads](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzoyAxOXqpFbuA9Vpe9jy9ePv7WRIR3IoBRHk3InT4Nl6CS6Xj8s8VjTnjVld-m5wg5LQ) by Adzviser
  * [Awin](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwmFnFCYuYODAjCCSd7wmQAJS5ZsjiikQfljDDS-IlH0qGh4D0ON0GzTvGGQ6NnIVM9YQ) by Catchr.io
  * [Strava](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycby7hZYpxx-dEvvV6r3TdO2II483BNkIUzcYrKcyenJHtnivJnlsKeF4ibiLDJeVuWZ6Tw) by Windsor.ai
  * [Harvest](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwCLFeu3NN5FEsFDmaqaXgbiBW28jbVXu6e-tXuyKZ0s_Msb86wvnovSkY7L6cbHqMt1A) by Windsor.ai
  * [CoinGecko Coins](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbz-RM4H7CHmCbZ3tIJS32laHcrBF40dtZ8dGCwQ_hV1BuHe2QoiN8UKUGr3phNLL6CC1g) by Windsor.ai
  * [Whatagraph](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyoU_6CHaRDSb20BQvTtjrDp36kSxuqY5eaIIgmSrUZGFUCSZGb7YwDvc2_3L8J6pap) by Whatagraph.com
  * [Simpli.fi](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyUNbCUMHVQvvCZCxiDG-8DxKVAQ2QFmngjc2PiH0vUmWf-1C6s6Mcpa0veNM7yfZ4SXg) by Windsor.ai
  * [Line Ads](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzU4TaDXEF_ss1Xrm2F0t_c03QVwhCnA5l5RhuR4mifs1o6qugLZs8IDAyZI9GISJY) by Windsor.ai
  * [BigCommerce](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbw0VTWDZ1IoVlVZoEDroiquIeFgpS_SSBlsRyd1SgB7VAzdzdB-6t5lDGIomfkdnqpu) by Supermetrics.com
  * [Zoho CRM (ZOHO)](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbwZf5iuPJqJPut5wKApwSo67qpn3WbibaT_jgkQ9mkLskL0tkCITk-DZqkxWQGRELP7LQ) by Supermetrics.com
  * [Omnisend](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzMucgPd4mXR40GKBfRe4wwApOo2Q-GFTbNm2bFDuXtRbttHJnAJyV90EVKfGEdnJcf) by Windsor.ai
  * [Prestashop](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycby-eAzCzW-OW_Qz22M3awuAk8HujAWzEpDyll5QcRwhPQkx4w8v68rHjYVPzoCl7g4xZg) by Catchr.io



## December 17, 2024

Feature

**Gemini in Looker enhancements**

When [creating a calculated field with Gemini assistance](https://support.google.com/looker-studio/answer/14196955), Looker Studio now suggests sample prompts to help you get started.

Feature

**Preview your data**

The data source editor displays a [preview of the data](https://support.google.com/looker-studio/answer/15446333) in your fields. This feature is available for the following data sources:

  * [Google BigQuery](https://support.google.com/looker-studio/answer/6370296)
  * [Google Sheets](https://support.google.com/looker-studio/answer/6370353)
  * [Looker](https://support.google.com/looker-studio/answer/12388266)
  * [Microsoft Excel](https://support.google.com/looker-studio/answer/14953315)
  * [CSV upload](https://support.google.com/looker-studio/answer/7333350)



Feature

**Dimensions in scorecard charts**

You can now choose whether to display a dimension or a metric as the [primary field in a scorecard chart](https://support.google.com/looker-studio/answer/7193479#primary-field). When a dimension is selected as the primary field, you can also select a different field for sorting the dimension values.

Feature

**Improved hide/remove data source fields**

We've improved the functionality of hiding and removing fields from a data source:

  * You can remove any field from a data source. (Previously, you could only remove calculated fields.)
  * Hiding or removing a field from a data source prevents report viewers from accessing metadata about that field. Field metadata includes information such as the field name and type of connector that is used to access that field.



These improvements help you control access to your organization's sensitive information while still promoting data democratization.

[Learn more about data governance in Looker Studio.](https://support.google.com/looker-studio/answer/15682067)

Feature

**Proportional heights for inverted triangle funnels**

You can now use the [**Use proportional heights**](https://support.google.com/looker-studio/answer/15406345#funnel-chart-options) setting to display the value of categories in a funnel chart by varying the height of each bar when you select the **inverted triangle funnel** style option. Larger values have taller bars while smaller values have shorter bars.

Feature

**Warnings for external links**

When users click an external link, Looker Studio displays a redirect notice.

**Note:** This feature is being released gradually. You might not see it right away.

## December 12, 2024

Breaking

**Updated Admin Console setting**

The **Let editors set owner's credentials for data source access** setting has been renamed to **Allow users in this org to be the credential owner for any data source**. This setting now exhibits the following changes in behavior, which may be breaking for some users:

  * If a Looker Studio administrator turns off this setting, any existing data sources that have a data source owner within the organization and that were configured to use **Owner's Credentials** must use **Viewer's Credentials**. Users who don't have access to a data source's underlying data may lose access to any Looker Studio content that is based on that data source. Re-enabling this setting restores the original **Owner's Credentials** to those data sources.



[Learn more about this setting.](https://support.google.com/looker-studio/answer/14340218)

Feature

**New condition option for filters on date or time data type dimensions**

Report editors can now specify a value and a unit of time for the following filter conditions with [date or time data type](https://support.google.com/looker-studio/answer/6401549) dimensions:

  * Is in the Last
  * Is Before
  * Is On or After
  * Is Previous
  * Is This
  * Is Next
  * Is in the Month
  * Is in the Year



[Learn more about filter conditions.](https://support.google.com/looker-studio/answer/7327641#date-and-time-conditions)

Feature

**Looker connector filter enhancements**

Looker data sources now support a **Matches (advanced)** filter option with [date or time data type](https://support.google.com/looker-studio/answer/6401549) dimensions.

[Learn more about the Looker connector.](https://support.google.com/looker-studio/topic/12387669)

Change

**Changes to New Search Ads 360 connector field names**

These New Search Ads 360 connector fields were renamed to resolve a naming conflict:

  * The field previously named **Conv. value** is now named **Client account conv. value**.
  * The field previously named **Conv. value / click** is now named **Client account conv. value / click**.



The original **Conv. value** field remains unchanged and continues to be the correct field name.

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Heureka.cz náklady](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbykqKWzcGQmu8e5lOYa7BMaSR-6OrUL2U12GiGKQH2DuWFgseEiaQzwkUI45yhWJkPw) by METRIXANA
  * [Heureka.cz Sortiment report](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx3ZyeDbTXWU1WHp-tdTSqlJLtVHrb1kVMjvwud6KJ-qpPoRzSEVeM9B9-9KLKE9xQp) by METRIXANA
  * [Shoptet produkty](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxhhtksufyEcsUMvNE2U0TYzyUzt0293Ro2nV1VS7Hz9-NxMU33JoIw1g1bMMDntz6wYw) by METRIXANA
  * [Shoptet objednávky](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyGo8ehVwDMxYqequU2aqNOq2ULeRlnc9j-nfuyd9MQw_DgPZddONMGA-rXieQi0G23rA) by METRIXANA
  * [BigQuery](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyApV5CX5VrFVf4v1T9zaOqHlI9TnJDGnan2_IPoV4VSvy_khL95xDV3WiQU9-wVnr8) by Windsor.ai
  * [LinkedIn Page Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzwIMaRIt__C-ptYNIwqRlWwnTFuHgTIm6ExMakKnDnvRwiG162eKVlVysHTUaAuRxDfg) by Doodlytics
  * [Vibe](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwa5qv-MXydPhYDgaLdxzOPNJmHHPwHh4D7ORSgin9-HjwZTlxtYmDsw9HWLniqX2B09A) by Windsor.ai
  * [Partnerize](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxQ8sofXXoFuNSlDgoQU1qYyErncqp-Io7ckpo-DjEhTUTe0naJzvsRptGCGMFUihmr) by Windsor.ai
  * [Adtraction](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw28HgjoOP-E6csNS3BrmYNSFekI34GztbF0Qg42RE5UhI6rTfF7rE0Jsbv1cAiLFfG) by Windsor.ai
  * [MNTN](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxPriRhtSuebVbQjOocv7VqAu2BcfBsoqPoppCGL3S8Ser6CtojknMm0BG2VI-q4rQ) by Windsor.ai
  * [Income Access](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzunOQuR08SVIq-lIv2jO9yJNBzIjO7dlR7DYElyn430nY2EDmLOvwwc4VzZMcs9FEXEw) by Windsor.ai
  * [Square](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw2Ta4QLJd3nk3vQuB3YvD585kX-nS_6bxNd5r8V5cRonwGGUmriX4lxhrSOJ3aZjVt1w) by Windsor.ai
  * [Calendly](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyuInN0-XM4HCIw_S2Xwx74U_CReWBsHMrBXSsPezQxqvX_bdyS-8wcoGiNvjLOk1St) by The Data Students
  * [Cin7 Core](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzpiRV4tT9rn12Od107mjFDxuEzR-5wnZb2XZ_vp_mb1kp0eU8lpPOHF0FwQSjGcGNC) by Jivrus Technologies
  * [Pipedrive](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyYqutCRqODLx67oIgaEvY02eXe0tWE3U0fVzG2L0Bz-3kbi6_W9SrGx2P1L2Rp0N1rnQ) by Supermetrics
  * [TrueClicks PPC Audit](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx-dD2F9q6InbVo1yVCISKbuL5snZ3pD-y2oXlxWLd5Ous8ddFPK5fkzfpS0kc5yvX7) by TrueClicks
  * [J+Search - Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzAlGtucH0J6j1bGzInwrSOxIZjVSFE3hZAwjtUs_zKcdE2bcdVfC2s1XQyiIkAhbc) by Jellyfish
  * [Mixpanel](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz9bdZOKHHapqfc-rlBBCtFPVMWQQdTj_DCwvMMdfSybXNW65dPhrNwa5Yzv0vScTj61g) by Windsor.ai
  * [ShareASale](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwz_90rKKhRx89gujTG9RYIEJ8wZexvYiYxsdgDrRnDIrQkekgKaqq9NIkTZcZ1M4zO) by Windsor.ai
  * [Branch.io](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwduENNNOv0y4Z9nZWhC3mKeKpyMfakY0fMSvCkGdDBgBV6KGln3ROyvVrAqcXTQTPDfw) by Windsor.ai
  * [Marcode](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyBsJ6Mr_bf5MYFXGPi7XoxaCKzCT4TvZ5n_Wgq4dbObPCLsgtGKKaOokv7VdOtVRwr) by Marcode
  * [Search Ads 360](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyun6R0MvHC2L5dQbN2yTJ9pysbJspHAQIhSgaYazYh-ZcunNGHVe3kRHSH1k_7b6lpBA) by Supermetrics
  * [WorkMeter](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzdLiVJ3AW8FnKXhL6NSI4DGYCWTRCDo7p4DxfI8HcFFHhhHhxT4TXjatfT_3Lirm4ZzA) by WorkMeter, S.L.
  * [Heureka.sk náklady](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzaLma1nlQ1iSrrrvMTAU41KCAQUfWPnXIHs4lp7d2DtL_UoqmP1t9BvGzac-MfiVtArg) by METRIXANA
  * [LinkedIn Ads Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyTRZVZcMYz9JcquZIZhYbfBzPNiAt8MwfI572hadlP3wNMxn0zjyfp4_29jh13Yy1nog) by Doodlytics
  * [Pinterest Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyRPI5EMFnGF-3WcbtxM0H-Vejb64fad2djOq-tMKDy-YIDWOQM9ECIvkU8GlV_GVEYoQ) by Detrics
  * [Recharge](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxC0PyQcuKBE3k9JORHCHsqbkZ4uy2DBbSuIZR9eA1W_MpkYucDCKx9dIdkzD8Yd6o52Q) by Windsor.ai



## December 05, 2024

Announcement

**Looker Studio Labs**

Learn the fundamentals of Looker Studio and Looker Studio Pro by using these Cloud Skills Boost Labs: 

  * [Create a report in Looker Studio](https://www.cloudskillsboost.google/focuses/88311?catalog_rank=%7B%22rank%22%3A5%2C%22num_filters%22%3A1%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=39838896)
  * [Looker Studio Pro Essentials](https://www.cloudskillsboost.google/course_templates/1185?catalog_rank=%7B%22rank%22%3A10%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&search_id=39810892)



Announcement

**New Conversational Analytics guide**

A new educational resource is available in Looker Studio to guide you through how to use [Conversational Analytics](https://support.google.com/looker-studio/answer/15000279), a [Gemini in Looker](https://support.google.com/looker-studio/answer/15067516) feature.

Select **Create** > **Conversation** to get started.

Feature

**Autogenerated titles for charts**

When you enable the **Show title** option for a chart, Looker Studio [automatically generates a chart title](https://support.google.com/looker-studio/answer/7165560#autogenerate) by default. The title is based on both the chart type and the fields that are used. You can add a custom title to a chart by entering it into the **Title** field.

Feature

**More data from New Search Ads 360**

You can visualize the following fields using the [New Search Ads 360 connector](https://support.google.com/looker-studio/answer/11601902):

  * Conversions (by conv. time)
  * All conv. rate
  * Cost / client account conv.
  * Google Ads Auction-time bidding
  * Currency code



## November 21, 2024

Feature

**Let report viewers see all filters**

Report editors can [let report viewers see all of the filters applied to a report](https://support.google.com/looker-studio/answer/7326859), including filters that viewers can't edit.

Feature

**Filter value suggestions**

When defining filters on charts, pages, or reports that use **Equal to (=)** or **In** conditions, report editors can select from a list of possible filter values that are provided from the underlying data. Filter suggestions are supported for all data connectors and can be disabled during filter creation.

[Learn more about filter properties.](https://support.google.com/looker-studio/answer/6291066)

Feature

**Looker connector filter enhancements**

The following features are now available for use with the [Looker connector](https://support.google.com/looker-studio/topic/1238766): 

  * Filter-only fields can be set as a report control and a quick filter.
  * Looker Studio displays suggestions for filter values based on the data source's LookML [`suggest_dimension`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-dimension) and [`suggest_explore`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggest-explore) definitions when **Equal to (=)** and **In** conditions are used.



## October 31, 2024

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Oktopost](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxhymgwRSZCYil8iQC3AVs2jEhwGRfrypVxYVW7_U1dYArYQprYxZai5NBNCGeg0qZUuw) by Oktopost
  * [Jepto - GMB/GBP Free](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzD14aWfSu0DBU_5f0OWjA_TdrZzQQ31ytrwfsVC-nz9-WnDzIsnSQZVESm1Uw8o7ONVQ) by Jepto
  * [Instagram Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwtn_0-pzdeJOl0YGglIa0AxF7Tm2qaj3-YMR_Ba928gCHDIDe1KKSpus9CxXSmoOn_Pg) by Detrics
  * [Bing Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyDrrpLhi1f5EH3wM9t7jGXDceuZjGwgvemFh1oRNkeD15Za04NBMk36hwg4B5FZj9pwg) by Detrics
  * [LinkedIn Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzTC0tALUVNd-sfCEbsrcyxGFVe2pxWh0AIqr25qOjjyML19qoGwVsFp2L3N-S0___tDg) by Detrics
  * [X Ads (Twitter) ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwmQ2LStLoelRPEgWu7gJi51IHKhS_9jqwv0iZa27gXp7YcyoPQrTwqMsxSBQRFDI5S)by Detrcs
  * [Insites](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwDeepZLEKJkX-jyBoxpT7ZxYdQZ-B7woKFdSqjWgInKmRBiBja4US5jZREpLKtEGjc) by Insites
  * [LinkedIn Ads ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwbAuIJg8WrbFYh6U1F5xepomQhDlQcAGesD39Me4pfxvNlYQ0vL2SzJ7y27gnqYcXK)by Pro Plugg
  * [TikTok Organic ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzDEZHujXrCV1mtLTmn-jt6Kj0Nw8vOWM3W6RSFNG5c6PDjK8EZ5mct2tA43cHcoCLS_g)by Power My Analytics
  * [Nightwatch SEO Tracker ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw19GwE8YPuSlryMIrKxok4FOpD9esKxKEty5hv4v-YnyxOUU9_cllhz-gfdl0lTUit)by Nightwatch
  * [MongoDB AppiWorks ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxSrhRS0mBgJ4xp_T9mvvtAcV9_T_LZAmEqjTjMTTl6teApA1aRZ0qlXOneFpoXDeSOTg)by Jivrus Technologies
  * [Google Merchant Center](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzUjEzzyx9FrsEBvau8sHNY3529Vs_bJDyb8JQwkc603YtPOit7mPIQlb_vqZcb1rLG) by Adformatic



Feature

**Text wrapping for pivot table row headers**

You can now choose to wrap row header text in pivot table charts by [enabling the **Wrap text** option](https://support.google.com/looker-studio/answer/7516660#row-header) in the **Style** tab.

## October 24, 2024

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Heureka.sk Sortiment report](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxd2rishmBKSgVcTzZyvwu-77Uga_1zoDp6rJyid2TuuCDkrs1dPdgNrOOTPaOpyUqLeQ) by METRIXANA
  * [Auth0](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwjt4VbUvQ2l-pSmhboQS-per_ckrJjBdyuPhoLwtZ1WzVflILmNBltNyDf0hqbla7z) by Windsor.ai
  * [CJ Affiliate](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwJ603F8y1OVACWiD9-fhxm9oWD8qh09nuZLrmZwJjrLMz6fXnjZBDoifOTXs0fr-vr) by Supermetrics
  * [WooCommerce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwSLNldIFqlBi9sG6qC16AK_GVzJrG5osTAIPN5JNoXhsGZjCuj7lMUnNPm9OAlEjaO) by Supermetrics
  * [TikTok Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyi42kQpuHT_esupH6Wq_H6jZxKZEKVXyf2IhcT8LNjGUCaNgsouRZep1vLGOVKZk3H) by Detrics



## October 10, 2024

Change

**Cart conversion fields**

The following cart conversion are now available in the New Search Ads 360 connector:

  * Orders (Cart)
  * Avg. cart size
  * Avg. order value
  * Cross-sell cost of goods sold
  * Cross-sell gross profit
  * Cross-sell revenue
  * Cross-sell units sold
  * Lead cost of goods sold
  * Lead gross profit
  * Lead revenue
  * Lead units sold
  * Cost of goods sold
  * Gross profit
  * Revenue (Cart)
  * Units sold (Cart)



## September 26, 2024

Announcement

**Partner connection launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [ReQues](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbya4S1_MEt2PmgV0kfk8VFDMgJrogoV-OmVYFlEh2-C2MTVZNzbsTVjh3VcoVbRarlOgw)t by ReGuest Srl
  * [Insightly](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxLeKZtENCGWHJOznqGfz2Kfi48QH4Bx5vVzT9j2tZr7UT1XXNf6r3kEUJ5-E-Bv-pf) by Windsor.ai
  * [Zendesk Sell](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxLpwFqBoOp98m2X6F0dXMyUVXWslqgvBc53vRreqTALxDtJh-fGRX7r3sgIcrRsGtQeQ) by Windsor.ai
  * [Customer.io](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzgfKJPw-EfIEMGVrOfMSoZBl4mtSTuo9F1S2B-_F9WJedqD0PKTBMwOrroh2SMiP1kWw) by Windsor.ai
  * [Digistorm](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzMe3rJY1x9tf_83H2Uhz62izL-V0yjgA8Hzb4t9LBWwxTw1cVndRsrBVeDisLjEmhM) by Windsor.ai
  * [Yahoo Finance](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz7lBFXrWNc5b24fWUdoHXv6H6GJcyPDhuxQAeRO9bPcdGosf31c9Uqp4B_FvT9EsJd) by Windsor.ai



Feature

**New funnel chart option**

The new funnel chart option lets you visualize how a metric changes over events in a sequential process.

[Learn more about funnel charts in Looker Studio](https://support.google.com/looker-studio/answer/15406345).

Feature

**Microsoft Excel connector available**

The [Microsoft Excel connector](https://support.google.com/looker-studio/answer/14953315) lets you access the data stored in an Excel worksheet.

## September 19, 2024

Announcement

**Partner Connector launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Heureka.sk náklady](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyKC8TpOwapdLviJKycOWDTvm4MUht854WYqm5Ce-GOzop9dqPaagkqsq3hIJF_Fm1s) by METRIXANA
  * [GrowthPlatform](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwBGMpp7_pYFgGxKWbLt_y3Q6G0vXMdrDNI-Ox3GzYVEhLtt0WmhE2uthpksVqI9xVSaA) by BizSpring
  * [Google Play Console](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyZfD2xG0E_tFtUYkYQZxs2o7UCDLO-LalktY-1kMhf4_f9fsJwkHxATGHETWkKb2Xj3A) by Supermetrics
  * [FaceBook Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzwayLrF1YuSTgrrLJsFJZDtE7IStkVhXm0KYqFMKFGmjoXDfkkbuWLaeuXb00C4-hfSg) by Data Conductor
  * [LinkedIn Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw0v3sO20LHMldAlWXrSuS29yGya7oNRFyknuBoBvPoGi-S0lZR28xsP5lw4eEmqLk2) by Data Conductor
  * [Adobe Analytics 2.0](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxXom0Azcc1ImRulH5C7wyjuJnvkX-J8gcEjSPeIObaE0Nm8fyxPr1raNI-3wpxT-Is) by Windsor.ai
  * [lemlist](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbylRUzl_F494_FULfaI7DMAxNwSppZG7sLEldMA6LgsT10f_Q3Hjg1OMHy5q8Ikzt2NDg) by Windsor.ai
  * [GitLab](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxwtrp-MUaS3RE5lG_SOo6nwtpb6-xdu0cII0wcpFdj8DxPBXx8_VI2vWSqmvO-lw51sQ) by Windsor.ai
  * [ChartMogul](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxMt7MSSjCiOcCTYBhh82LrKWD6LG6sFyX1SVFsx90I527JOXVejhvk9CsfC_nfW7PE) by Windsor.ai
  * [BambooHR](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyJtQ4KLOHnKCIpfD2UdCXWzHIbWk8SxRkUDJtaWMbVU8vdHEa1QfZKdF5O8nX-51H8-w) by Windsor.ai
  * [CoinMarketCap](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyAwY8B_AA4SRmJ20LV41YyXOfqXOqu_om10q-KkGnNsnpicdNRx1v_ElYl2jvIV68a) by Windsor.ai
  * [Alpha Vantage](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwdZKRkfl6PuxhK6ky3GFNfQqz-_r3sP6H4gnrRJvNznshge7H8Z15NPrrdHmVgxp1t) by Windsor.ai



## September 12, 2024

Announcement

**Partner Connector launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Meta Ads](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyWcGtR5SrrnvJlt_RrszgOlW8xLwtZrEvba49DgnY-7Fi3jKdx8_F67WLWkT5kT0PMIw) By Detrics
  * [Similarweb Rank Tracker](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbzkvC3sx4X1y9fgJmQUgnJA0DPMvizlT8KXVTKpCMI3Y1tmlz1zXppe1K2rO44Ae-yOTg) By Similarweb
  * [The Trade Desk](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyjf6DP6s9T2RszJMVAoAusek0qyRcp7d1O4OuBpm01pLEFNADwQskx1W6omIlbItIS) By Power My Analytics
  * [Pinterest Organic](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbz65G4cin2fJdcb7Sgg2WXpRvV4-5P52UyytvXApuUU4oXfF3sFUlQ41EeW2zASsEvS7w) By Reporting Ninja
  * [Salesmate](https://datastudio.google.com/c/u/0/datasources/create?connectorId=AKfycbyID-M5biAbMRE1UEC6-SdVDJhFWdHNpzcGZ8CGmdazzX4ykIG_Zv2QsLwXRLPXEZ2E) By Salesmate



Feature

**Public Preview of Gemini in Looker Conversational Analytics**

You can [query data in natural language](https://support.google.com/looker-studio/answer/15000279). The Conversational Analytics feature is a Gemini-powered data querying experience that makes it easier to find answers, explore data, and share insights using natural language. This feature is now available in [Public Preview](https://cloud.google.com/products#product-launch-stages).

Learn more about [Gemini in Looker](https://support.google.com/looker-studio/answer/15067516) and how to [enable it in Looker Studio](https://support.google.com/looker-studio/answer/15067638).

Feature

**Text wrapping for pivot table column headers**

You can choose to wrap column header text in pivot table charts by [enabling the **Wrap text** option](https://support.google.com/looker-studio/answer/7516660#column-header) in the **Style** tab.

## September 05, 2024

Change

**Gemini in Looker now available for Looker Studio content**

Looker Studio Pro users can now [create calculated fields](https://support.google.com/looker-studio/answer/14196955) and [generate Google Slides](https://support.google.com/looker-studio/answer/14198075) from Looker Studio content using Gemini assistance. Gemini in Looker no longer requires content to be associated with a Looker Studio Pro subscription.

For more information about Gemini in Looker, see the [Gemini in Looker overview](https://support.google.com/looker-studio/answer/15067516).

## August 30, 2024

Announcement

**Community migration is complete**

The Looker Studio Help community migration to Google Cloud is complete. To ask questions and participate in conversations with fellow Looker Studio users and experts, [visit the new community](https://www.googlecloudcommunity.com/gc/Looker-Studio/bd-p/looker-studio-pro).

## August 22, 2024

Announcement

**Partner Connector launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Adobe Commerce (Magento)](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyZYD15OviKcVrq_vDOLYydbx9XcIjWveAXrJa_7JwUZmCI6VwQrAPwGAliJeGqTVi_Vg) By Supermetrics
  * [CTM: Call Log](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzuTKJOIL06VUo5glApm0I_lY_WKzgw4s3xz9Pp7aAWrF3aegzfH5W_ecU-bOD5jwdz) By CallTrackingMetrics LLC
  * [Piano Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyPODMcUxMlOjjLnkcQv3N7SchS_VKDGgTZjLFVG4ffzVPatkQjIRXbka-8wrvgz-4) By Catchr
  * [ClickUp](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwkB62NNfSM0Pn5hmZs4LAf8y3nsMY3Ll5-iyo0dRhGSiYZoM3lxVcp1JWH73qOsDbu) By Bay Leaf Digital
  * [TikTok](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz72u7FgG48z0ukcp6z_mGwwD3DU1jJjCdbQU960qWeWvr-WKrEAQoiOxFEo0wtp8Ho) By Gladior B.V.
  * [WooCommerce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzFIr8-FRv5ASNWAqLM2_lugB34OLWqEKEvinZmJNCp4V2G8a7mfDXOxv3aiBgGFHt2) By Data Bloo
  * [Apresenta.me](https://datastudio.google.com/c/datasources/create?connectorId=AKfycby9ZSrGximpIgJgOQIhMgYkx9Yf6kN8E0v9qHOFhEovyzmVM0nIuyFiEKLSdBrWfFmH1Q) By Apresenta.me
  * [Semactic SEO Data](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwIQtG7Y9bX9_aHUEGaSq9_ryzcApG3YKN6M3D_7pJzMSaHPx2dO-Daq2d0BAz7aZ-6cw) By Semactic
  * [Piwik PRO Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyu-93CLj3XD1Jei1e9sZy9mN3_t1aisy2uX1njXTFx5GflCQchzc7ByJkl_OGmad3L) By Piwik PRO
  * [Metrihub](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxwDgjGeHRA2lY-9Vb2T9ptEwTq4EPleA1bURAIQNiGNpm8ZX8UPTlqqm2W4Kyg6ake) By Metrihub
  * [Klaviyo](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzt4nhSO9YSbOGdAaYPX2Q6fRWA5cvTGhn8kSjA4jayp8hDtCnAqL5cfBK8A8EKBmS1rQ) By Power My Analytics
  * [Similarweb website analysis](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxdtM7daUXIGu6lbO_6P5yyZIig6Sbme6fq0OivP4r3fl8EnJAaGxS9PUns1kTbLK2r) By Similarweb



Feature

**Conditional formatting for collapsed pivot table charts**

You can now [apply single color conditional formatting](https://support.google.com/looker-studio/answer/9528890#use-single-color-formatting-on-a-pivot-table-chart) to [collapsed](https://support.google.com/looker-studio/answer/7516660#expand-collapse) pivot table charts.

## August 15, 2024

Announcement

**New Looker and Looker Studio shared terms and concepts glossary**

A new [Looker and Looker Studio shared terms and concepts glossary](https://docs.cloud.google.com/looker/docs/looker-and-studio-shared-terms-glossary) is available. This resource compares and contrasts terms and concepts that are used in common between Looker and Looker Studio, including some that have similar-seeming naming conventions but different functionality.

Feature

**Sort list controls by any metric**

[List controls](https://support.google.com/looker-studio/answer/11335992) now support sorting the options on any metric, rather than just the reference metric.

## August 08, 2024

Feature

**New formatting options for the bin calculated field type**

New formatting options for the [**Bin** calculated field type](https://support.google.com/looker-studio/answer/15067705) let you customize the appearance of ad hoc numeric tiers. These options include: 

  * **Interval "[x,y)"** — This format displays the range including x, and up to but not including y.
  * **Integer "x to y"** — This format must be used with discrete integer values (such as age). 
  * **Relational " >= x and < y"** — This format is best used with continuous numbers (such as dollars).



## August 01, 2024

Feature

**Audit logging for Gemini in Looker**

You can view Gemini in Looker log events in the Admin Console (Security Investigation Tool). Gemini in Looker can be enabled for Looker Studio Pro subscriptions, which are associated with a Google Cloud project. To see which Google Cloud projects have Gemini in Looker enabled, as well as those with Gemini in Looker's Trusted Tester capabilities, filter the log by choosing the **Setting name** attribute and view the entries in the **Project ID** column.

Learn more about [Looker Studio log events](https://support.google.com/looker-studio/answer/9690662).

## July 18, 2024

Announcement

**Partner Connector launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Facebook Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyMbZsruZcpyeE0z5iL9Y4_1I_KfN4XdkwN7WAoOxJj5bbrw5kOn2OeMngFq_iJT1pGfg) By "DAXRM"
  * [Pitchbox Daily Outreach Activity](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyLE5nz8oKcR_e2e3WtUNIYUJTuldTB69UVgLE33McyGfv63V9PuVU94OMmhMDFIBNmNA) By Pitchbox
  * [Wrike](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw8_DZASQb1IaUrd9pCbk6H-hmSoA-uJUtJ299wzYAdB18PN_jrZ9-IajcshY6kfy4meQ) By Windsor.ai
  * [Cart.com](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyhU15Q2SQ_hh3dmXpCPRdlVW6fF2Wu7RiqSYHLwkkMOMp3y7cO9IBvo6JUb30gOK_S8Q) By Windsor.ai
  * [Metabase](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx_f-_YgOmievzdozLivz2IP7gEo6DdIqhJD7qY3HN6X5pfv_wkI42PdQJVXJRnJa6E8A) By Windsor.ai
  * [SurveyMonkey](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxYKFsl-HYl48T8-1HpDdjteuCO_EjX0aUVZUJtotDLN3-eXOM1YzCI_hnE1uwOb3Gv0Q) By Windsor.ai
  * [Okta](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbytreYa56Pj_ASuijAyia2UqlTn-cgmvcoPWeRZT9MZpjw3QEVXeSCVSfZx8HSlzsM) By Windsor.ai
  * [Chargebee](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxNbTf9C7_p8KNaDxrQtnVcQWBI_dmEx_ACy_Qogk4zO5D3kP1Qf1fLs_GmQ5bhuD_fOg) By Windsor.ai
  * [Mailerlite](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxQ-Jk89Mv8ztE4phRCUtbfgGlSBDegkIGCtEZjOlZfshq1DgKVnQRur4BcSqlzUsd8nw) By Windsor.ai
  * [Clickup](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz1dRGGD7k4WbENAdr81e3EoQu0lK4nWX0lnXCiaLr21Q6ZoGh1yPXE8CjPsqCmgXOT9Q) By Windsor.ai
  * [Courier](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzIfNhD82wb8AWnWmU3srR5L9oMg8i4xJgpsM6e7NuLbukprEfBDxR1xM4LjjOiXahz) By Windsor.ai
  * [Play console connector](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzv7nIoALgijR5SqgCv0gvDsG-CDDWVbk_xDumhcw_jiOnoy4Wqmws2h4BJFrop9Ek) By Multivariate Tech
  * [Dynamics 365](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwSSsf6AsOV_xRzI48nU2nxCnAXli1awZMKYX87raYVTDikKuFUa7CwBbB2jf54MEWJiQ) By Windsor.ai
  * [AdRoll](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzljXqJyWuiZvBA4AurHOuOeOo_pODizsmqBd1j6req2TFEd7cPYCVHYffRhy2EruMG) By Catchr



Feature

**Ads Location Extension Fields**

The following asset location fields are available in the Google Ads and New Search Ads 360 connectors:

  * Asset location address line 1
  * Asset location address line 2
  * Asset location business name
  * Asset location city
  * Asset location country code
  * Asset location phone number
  * Asset location postal code
  * Asset location province



## July 11, 2024

Announcement

**Partner Connector launch update**

The following partner connectors have been added to the [Looker Studio Connector Gallery](https://datastudio.google.com/data):

  * [Typeform](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzoWcI_Kl10PiKerTCByS-wHssR4g1EAwbN6rIH103UZlt6ys3vJSUNMDhPQ28rsqeB) By Windsor.ai
  * [Google Search Console](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbypgthRBAupJIK5of4aMaEMo9neVBWCto16ul7ofXEuwdzQumBSXkPlTotTGidsP1St) By Catchr
  * [Clockify](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxArxHCN_oT5WFK7KygU-IP2qWIdpKf_Lm7WYAOOGdF5PorWKQ28J6poI2v4MoX0neNQw) By Windsor.ai
  * [GitLab](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzn9sU4cmefuowdvwHyBbf1-XIF-ZEy8eMHOzJf0cCGpJeqPUZpzK1kiHADzMRD5d7O) By Windsor.ai
  * [AppFollow](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx-pIYjuliH96lvz-qk74l0BQFnHio5HE1xfswK_Pa0ntj2HZshF2vsruoGLYuAEC1iWg) By Windsor.ai
  * [Monday](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxYR-PQVaI-fVkffbPgJX8ElQsVi1tCKp0HDyfJmRcBCKkXIzgGfyv-e-P1NfhXRTM2) By Windsor.ai
  * [Agorapulse Social Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzX9XveoMaDYlBlskUrA336S-dqW44bQMJ_GAJQ0CN36uohZ8ZFRLzEzaMlww7e1cNK9A) By Agorapulse
  * [Oktopost](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxuC9gsts0glUQtOSFSiGLKYV3l5UBfJrBtpucLleIaNDB34iihUjaXINiMOKwOe0px5A) By Oktopost
  * [LinkedIn Business Manager](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbymHWL1imzyVH8UbcwQIPC3MOVYiypUPiyILgbLEO_TkTbX3fWNPe9KWWqixMlsTjs) By Power My Analytics
  * [Facebook Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwNtbrGjiKzZ1Ak8IlwZkuB3fek3VsJxVOKniLEmL2BE9UodtxogMtaGRTeQlTYBP1e2A) By Doodlytics
  * [Instagram Insights](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwNXpRcAXcYl_XZsrjtT9WL7lzpoNfRlpxNJeXW8PQ1p_N8d-S-WWMWI_X-oIMqdxbvaA) By Doodlytics
  * [Facebook Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyv3_7vUvPJcT2qyuTl_rYwy5_CvMh9L_Gd3pbeBsAxEDbfN8AjivtAYJ9A7ALvYUrg) Insights By Doodlytics
  * [Pardot](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbymUwgeVk64GrvciW1qwksITWLhynkqElFz9y149MfEFmViZBzlYgkqvmZRe5biulIo) By Catchr
  * [ConvertKit](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzPjadsNwfbvlICMmca_74LXtNmfzZadxaMQso32Vij0FW4YYMzXQlmTRzsgy0Z9_kwew) By Windsor.ai
  * [Delighted](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbydB9rKGbkDDNvQJ_fi12Ar-kt0VeXMg1suw5frqL_nSafpKTL6iNgywso1WZnlaLsu) By Windsor.ai
  * [Everhour](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbymnZBZyq4Bo9GiyoOhK3vquL58DOhEtasAclvDke9aB-RlLriGoqKVo7s9Nl_MHJvh) By Windsor.ai
  * [Linnworks](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxzMx95sVwHFsmuUiiIdLObf4lQAuz3H-zYYntHgvTV2AfqdysQ4NZVulTYTyYYCGPMrA) By Windsor.ai
  * [s.i.m.b.a Google Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxkRXZtmZ15PmCNr5RsYzNO2jrtfax-rVeUeiPpLxcG9kiMPR8mm0s2AwSRZtRipEsTkg) By s.i.m.b.a
  * [s.i.m.b.a Google Analytics](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzZq3773Hqg-jVAmajtuaI45izGj4wv2Q3jRRTFotLNM66htPEN8_nKsOoth7GrMFXa) By s.i.m.b.a
  * [s.i.m.b.a LinkedIn Page](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz84VQS835j8ryOouY0XKwIVonQ88pae0bZa-c9E_Ih3stsA-SbyMOXwEZYUEq3msUx) By Simba
  * [s.i.m.b.a LinkedIn Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzfkzVJPE5xmYwjvMuePbw3XkgFjveFf29JRDpnak-UZMC8NH7dc6DZ4In1p7PWCtUysA) By s.i.m.b.a
  * [MINT ARM](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzTnW19AiOfKY1vwroR0QrFC7qYtyBq0pCUk4S_M0CbKbOHEKrS0-kX8UVG5Knf92rp) By MINT
  * [WooCommerce](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxSnZ1b_vhs3s1d875bqI1kT1m9sM5ImRx7Ci64FHdg-Iyn9Q3_hOmKxmFwPBrSDz5qew) By Windsor.ai
  * [Bing Webmaster Tool](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw-MCXYt7UWP_YeI_xJvxNR0HjTD_TUdR242uc3ms9c1ORR0BWz54gQKzr616zaJkth) By Catchr



Feature

**Pro feature: Gemini in Looker public preview features**

The following [Gemini in Looker](https://docs.cloud.google.com/gemini/docs/looker/overview) features are now available in [Public Preview](https://cloud.google.com/products#product-launch-stages):

  * [Create calculated fields](https://support.google.com/looker-studio/answer/14196955): Create custom fields and calculations in Looker Studio without prerequisite knowledge or experience with Looker Studio formula language.
  * [Add Looker Studio content to Google Slides](https://support.google.com/looker-studio/answer/14198075): Import components from your Looker Studio reports into a Google Slides presentation.



Learn more about [Gemini in Looker](https://support.google.com/looker-studio/answer/15067516) and how to [enable it in Looker Studio](https://support.google.com/looker-studio/answer/15067638).

Deprecated

**Search Ads 360 connector deprecation complete**

The Search Ads 360 connector deprecation that was announced on April 2, 2024 is complete. Please use the [New Search Ads 360 connector](https://support.google.com/looker-studio/answer/11601902).

## June 13, 2024

Feature

**Group Others available in more chart types**

The **Group Others** chart setting lets you aggregate results that are outside of specified limits into a category labeled **Others**. This checkbox lets you compare data against the context of the remaining results. 

**Group Others** is supported for the following chart types:

  * [Table charts](https://support.google.com/looker-studio/answer/7189044#number-of-rows)
  * [Time series charts](https://support.google.com/looker-studio/answer/7059697#number-of-series)
  * [Bar charts and column charts](https://support.google.com/looker-studio/answer/7165560#group-others)
  * [Pie charts](https://support.google.com/looker-studio/answer/7187587#group-others)
  * [Line charts and combo charts](https://support.google.com/looker-studio/answer/7398001#number-of-series)
  * [Area charts](https://support.google.com/looker-studio/answer/7206478#number-of-series)
  * [Pivot table charts](https://support.google.com/looker-studio/answer/7516660#group-others)
  * [Treemap charts](https://support.google.com/looker-studio/answer/9381697#group-others)



Feature

**Expanded data label customization options**

The **Data label** section in the **Style** tab of the **Properties** panel provides expanded customization options, including font type, font color, font size, and font styling, as well as background color, opacity, and border radius settings. These options are supported for the following chart types:

  * [Area charts](https://support.google.com/looker-studio/answer/7206478#data-label)
  * [Bar charts and column charts](https://support.google.com/looker-studio/answer/7165560#data-label)
  * [Line charts and combo charts](https://support.google.com/looker-studio/answer/7398001#data-label)
  * [Time series charts](https://support.google.com/looker-studio/answer/7059697#data-label)



Feature

**New Color by tooltip option for Timeline charts**

You can use the **Color by tooltip** style option to color [timeline charts](https://support.google.com/looker-studio/answer/14748665#color-by) by tooltip dimension values.

Feature

**New Bin calculated field type**

The [**Bin** calculated field type](https://support.google.com/looker-studio/answer/15067705) lets you create ad hoc numeric tiers for numeric dimensions without needing to develop `CASE WHEN` expressions in calculated fields or logic in SQL.

## June 06, 2024

Announcement

**Partner Connector launch update**

The following partner connectors have been added to the [Looker Studio Report Gallery](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzmEI_JMI6i2Ig2kTJ-NAFAotwAwfKIylOuDjA43iGUqJzoYGlCA1GBCEUVtU9agCxO):

  * [Google Ads Account Explorer](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbz3gQEtOegidEvJZzWT7h75u9bKpyVtjyVN15TwmiiUuZ2WEQ9MWPv8FH4Iq6LJyEX_) by Supermetrics
  * [TrueClicks PPC Audit](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyoefJGoUBOpeIcakWzWSjFjNDed733LttGYXuakmbxmHqwnefDD75q6tUWyEmp4Xsz) by Trueclicks
  * [Pitchbox Project Status](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw4Ubz-P8y7O-3sUBcJoIydjStKPnZ4kJ13Cn1Hr2PwdCcDN6FuTqVKMjK8TUcPu8qvKA) by Pitchbox
  * [Pitchbox Outreach Activity](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyrnAOMhZevl_tWB37KiXeOylXKt7xQfxO8kHCU4hAR1hYPR8GN-NgXCspYFJZA-ziobw) by Pitchbox.com
  * [Pitchbox Campaigns Data](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwwr5ym8Cc1iKzkC1Upb15hqCAKnVIEpaZNFdBH0uQfccKqoIv3UDdmvZWO3VsAUZP9Hw) by Pitchbox.com
  * [Pitchbox Link Monitoring](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxMkbVHVFAyd-bVhAKlCPra4gQoLUBTyOI47OrWF9LBFkDJlxYwPRCUi8ttYdcNK52x) by Pitchbox.com
  * [LinkedIn Company Pages ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwb-mQqA4X8O_WenAxN6l-t1yaIQdT0zQ_CBb0IWywTT-0gCtM0Y1n0JOBBK7zrNGQi)By Railsware Products Studio, LLC
  * [Microsoft Advertising](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzw7Xi68Xe7yk_LgpiRDmrEzAvJT0wEmRI0rJw1wPZkUxC-hH64m4YUBtfAnA3ew-B0) By Railsware Products Studio, LLC.
  * [Facebook Public Data ](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbyqf55DgFpHikPBNqwgWtbCm1ikOqxHQe9FBstaW8B7pKkCs6m6Cw6hW8u6sQmlDzDO)By Railsware Products Studio, LLC.
  * [Instagram Insights By Railsware Products Studio](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwGkl_vRgZuRXhvo69W6ApDhQsLCNOKttadEnizz8ciz3II7NZI7H5xrE34uRcgOluz), LLC.
  * [X / Twitter Public Data](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzRMkXH2wgN9vKjWM0tHSKjUkpPfD3ZMpjH726MpRUx9IDSAOi-RfGedVgMONJMTx_xTg) by Catchr.io
  * [Bing Webmaster Tools](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwsudXwRInD2RRlPggicVSAVzK8v8cLrskJwCTcCMOtshpIKsU-H_J39Gag1SlT3uAHeg) by Daxrm
  * [Microsoft Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxF4n2uRr9GdXEBxSTDS4ivxGCsUd2RwKPzn_cVBdq9PazLVR-c8EjHNq6rJujOFnUZ) by Daxrm
  * [Instagram Public Data](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbw8_QbnsEeLGgMl7zg0M_XVAmI_RyCp1Aq15arB6SnCr4pGTUXcKULWsnweUAt0C63j) by Catchr.io
  * [TikTok Organic](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx8jxq6O_RfT8ObZi-l5o4H3ldzw7E0aty2zP9TMqPR58FKHZk56ZwgseVTDSjVLSBl) by Reportingninja



Feature

**Create totals that ignore canvas filters**

You can configure [totals](https://support.google.com/looker-studio/answer/7189044) and [comparison metrics](https://support.google.com/looker-studio/answer/9372465) to ignore any viewer-applied filters.

## May 30, 2024

Feature

**Looker connector support for filter-only fields**

Filters that are defined in [LookML models](https://docs.cloud.google.com/looker/docs/lookml-terms-and-concepts#model) with the [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) and [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) LookML parameters are now displayed as filter-only fields in Looker Studio charts that use a Looker data source.

[Learn more about LookML filters for Looker data sources](https://support.google.com/looker-studio/answer/12388266#lookml-filters).

## May 23, 2024

Announcement

**Looker Studio forum moved to Google Cloud**

The [Looker Studio Community](https://www.googlecloudcommunity.com/gc/Looker-Studio/The-Looker-Studio-Community-is-BACK-and-better-than-ever/m-p/752090#M78) on Google Cloud is open to all Looker Studio and Looker Studio Pro users to ask questions and interact with fellow Looker Studio customers.

Announcement

**New partner connectors**

The following partner connectors have been added to the [Looker Studio Report Gallery](https://datastudio.google.com/gallery):

  * [Pro Rank Tracker - SEO Data](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzmEI_JMI6i2Ig2kTJ-NAFAotwAwfKIylOuDjA43iGUqJzoYGlCA1GBCEUVtU9agCxO) by F.T.B ONLINE LTD.
  * [CallRail](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbzo0UwoNqN609aZDA3c-EuehbyfX1NFXOaXa5bRG6RPuTbq8iq5eyKMQakSiFhUx5C5) by Catchr.io
  * [Basis](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx2vmtqGJBmBAKQ1KK8qFm6eiTl_QzC1tiO1U339j1xeKG4W_4JIOsmJLbqeXPcUjb6Ag) by Supermetrics
  * [Facebook Ads](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbwfTI0Uhg-CmdcaGE0MYiqEWHfM_BinDJn4ZS5c1u9i31oWhZ4VWnKWU_MYX8CzB81Z) by Adzviser
  * [LinkedIn Revenue Attribution](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbxaClVfnBXmtuN9TFpOzfr6S06lTKhigudDsY4K7MSfK7nYv7uA4mmzCt6tDCYHdiw) by Supermetrics
  * [Pinterest Organic](https://datastudio.google.com/c/datasources/create?connectorId=AKfycbx0QE6stgvRctNpx41udry6iunDi1InScm2uR0QmkfBmiinLomx_XaQvi67E28Zqs6P) by Catchr.io



Feature

**Looker drill fields now available in Looker Studio**

Drill fields and links that are defined with the [`drill_fields`](https://docs.cloud.google.com/looker/docs/reference/param-field-drill-fields) and [`link`](https://docs.cloud.google.com/looker/docs/reference/param-field-link) LookML parameters in Looker are now available to Looker Studio report viewers in the [Drill Actions](https://support.google.com/looker-studio/answer/13872615?sjid=3378916309452597051-NA#access-drill-actions-on-table-charts) menu on Looker Studio table charts.

[Learn more about drill fields in the Looker connector](https://support.google.com/looker-studio/answer/12388266#drill-fields-and-links).

## May 16, 2024

Feature

**New Looker Studio log event attributes**

New event logging attributes are now available for the Looker Studio log event data source. These attributes let Looker Studio administrators audit and monitor how Looker Studio users in their organization interact with schedules and alerts.

[Learn more about audit log events in Looker Studio](https://support.google.com/looker-studio/answer/9690662).

Feature

**Looker data sources now display LookML filters**

Filters that are defined in LookML models with the [`conditionally_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-conditionally-filter) and [`always_filter`](https://docs.cloud.google.com/looker/docs/reference/param-explore-always-filter) LookML parameters are now displayed in Looker Studio charts with a Looker data source.

[Learn more about LookML filters for Looker data sources](https://support.google.com/looker-studio/answer/12388266#lookml-filters).

## May 02, 2024

Feature

**Chart titles**

You can now add a title directly to a chart in Looker Studio. You can customize the title's font, color, size, styling, and positioning within the Title section of the Style tab of the properties panel.

[Learn more about adding and styling titles for charts](https://support.google.com/looker-studio/answer/7206478#stylize-area-chart).

## April 25, 2024

Feature

**Create a Google Cloud project while subscribing to Looker Studio Pro**

You can create a new Cloud project during the Looker Studio Pro subscription process. This project is used to host your Looker Studio Pro content.

[Learn more about linking Looker Studio Pro to a Google Cloud project](https://support.google.com/looker-studio/answer/14615139).

Feature

**Create a Looker Studio report within Google Sheets**

You can [create a Looker Studio report](https://support.google.com/looker-studio/answer/14528488) directly within Google Sheets. To create a report from a Google Sheets worksheet or range, use the Looker Studio extension in Google Sheets.

Feature

**Timeline chart option**

The new timeline chart option lets you visualize the relationships between groups of events and compare the timespans over which these events took place. 

[Learn more about timeline charts in Looker Studio](https://support.google.com/looker-studio/answer/14748665).

## April 18, 2024

Feature

**Viewer role for team workspaces**

The [Viewer role](https://support.google.com/looker-studio/answer/10403868) can now be assigned to members of a team workspace. The Viewer role lets users view existing assets in the team workspace, view folders in the team workspace, and view the team workspace Trash.

Feature

**Pro feature: New Viewer permissions to create scheduled report deliveries**

When sharing a Pro report, Pro users can now [grant users](https://support.google.com/looker-studio/answer/7459147#share-with-users) with a [Viewer role](https://support.google.com/looker-studio/answer/10403868) the [ability to create scheduled deliveries](https://support.google.com/looker-studio/answer/9263641) of the shared report.

## April 02, 2024

Breaking

**Search Ads 360 connector deprecation**

After April 30, 2024, you will no longer be able to create new reports from this connector. Please start using the [New Search Ads 360 connector](https://support.google.com/looker-studio/answer/11601902).

To learn more about this change, read the [Connect to Search Ads 360 (deprecated)](https://support.google.com/looker-studio/answer/9091956) Help Center article.

## March 28, 2024

Announcement

**Looker Studio release notes moved to Google Cloud**

We've changed how we deliver product release notes. Looker Studio release notes are available solely on the Google Cloud release notes platform. 

Release notes prior to this change are preserved in the [historical release notes](http://support.google.com/looker-studio/answer/14605875) page in the Looker Studio Help Center.

Change

**Label fields available in the New Search Ads 360 connector**

You can now include the following New Search Ads 360 fields in your reports:

  * Label (Keyword)
  * Label (Ad)



[Learn more about the New Search Ads 360 connector](https://support.google.com/looker-studio/answer/11601902).

## February 22, 2024

Feature

**Show field descriptions in table chart headers**

You can now let report viewers access field descriptions in tooltips when the **Show field descriptions** option is enabled for table charts. **Show field descriptions** is automatically enabled for charts that are connected to a [Looker](https://support.google.com/looker-studio/answer/12388266) or [Search Ads 360](https://support.google.com/looker-studio/answer/9091956) data source. Field descriptions are sourced from the [Description column](https://support.google.com/looker-studio/answer/7178497#data-source-editor-interface) in the data source.​ 

Learn more about [table chart header options](https://support.google.com/looker-studio/answer/7189044#table-header-style-options).

Announcement

**Looker Studio release notes moving to Google Cloud**

We're changing how we deliver product release notes. Beginning in a few weeks, Looker Studio release notes will be available solely on the Google Cloud release notes platform. 

Cloud release notes offer enhanced features, such as RSS feed support and programmatic access using BigQuery. These features make it easier for customers to stay informed about feature updates. Additionally, Google Cloud customers will have the convenience of accessing updates for related products like Looker and BigQuery in a centralized location.

Release notes prior to this change are preserved in the [historical release notes](http://support.google.com/looker-studio/answer/14605875) page.

[Visit the Cloud Looker Studio release notes now](https://docs.cloud.google.com/looker-studio/docs/release-notes).

## February 01, 2024

Feature

**Pro feature: Folders in team workspaces**

You can use folders and subfolders to organize assets (reports and data sources) in team workspaces. 

[Learn more about using folders to organize assets in team workspaces](https://support.google.com/looker-studio/answer/14271915).

## January 25, 2024

Feature

**Download and third-party access controls in Workspace admin console**

As a Google Workspace or Cloud Identity administrator, you can control whether viewers in your organization can [download](https://support.google.com/looker-studio/answer/14340636) Looker Studio content. You can also restrict users from [enabling data sources that use third-party connectors](https://support.google.com/looker-studio/answer/14339933) or from [adding third-party visualizations](https://support.google.com/looker-studio/answer/14340728) to Looker Studio reports.

Feature

**Custom value formatting**

[Custom value formatting](https://support.google.com/looker-studio/answer/14295042) lets you specify how dimension, metric, and calculated field values appear in charts without sending additional SQL queries to your database. Custom value formatting also includes the option for report creators and editors to specify a value format by using Google Sheets style notation.

## December 21, 2023

Change

**Updates to New Search Ads 360 connector field names**

The display names for several fields in the New Search Ads 360 data source have been updated. New connections to the New Search Ads 360 data source will use the new display names. Existing connections to the New Search Ads 360 data source won't be affected. You can also [manually update](https://support.google.com/looker-studio/answer/6402048#field-properties) the display names for existing data source connections.

Feature

**Connection map visualization**

You can now visualize your location data as sequences of points that are connected by a line in a new Google Maps visualization, called a [connection map](https://support.google.com/looker-studio/answer/9713352#google-connection-map).

Feature

**Add value to reference line or reference band label**

You can now choose to display the value of a [reference line](https://support.google.com/looker-studio/answer/9921462#reference-line-label) or the value range of a [reference band](https://support.google.com/looker-studio/answer/9921462#reference-band-label) in visualizations.

Feature

**Stepped lines for time series charts, line charts, and combo charts**

You can now choose stepped lines for [time series charts](https://support.google.com/looker-studio/answer/7059697) and for [line charts and combo charts](https://support.google.com/looker-studio/answer/7398001).

## December 14, 2023

Feature

**Schedule delivery controls in Workspace admin console**

As a Google Workspace or Cloud Identity administrator, you can [control](https://support.google.com/looker-studio/answer/13889857) where users in your organization can send Looker Studio content.

Feature

**Table chart improvements**

You can now use the following options in [table charts](https://support.google.com/looker-studio/answer/7189044): Transpose the table, Freeze one or more columns, and Resize row height.

Feature

**Custom grouping**

The new [**Group** calculated field type](https://support.google.com/looker-studio/answer/14258973) lets you create ad hoc custom groups for dimensions without needing to develop `CASE WHEN` expressions in calculated fields or logic in SQL.

## November 30, 2023

Announcement

**Updated Looker Studio Terms of Service**

We've updated the [Looker Studio Terms of Service](https://support.google.com/looker-studio/answer/7019158).

## November 16, 2023

Change

**Pivot table metric limit increased to 20**

You can now have up to 20 metrics in a [pivot table](https://support.google.com/looker-studio/answer/7516660).

Feature

**Label fields available in the New Search Ads 360 connector**

You can now include the following [New Search Ads 360](https://support.google.com/looker-studio/answer/11601902) fields in your reports: Label (Account), Label (Campaign), and Label (Ad group).

## November 02, 2023

Feature

**Pro feature: Create alerts on a chart**

Report viewers can [set up an alert on a chart](https://support.google.com/looker-studio/answer/14151372) in a Looker Studio report that will notify the alert creator and chosen recipients when the chart data meets the conditions that are specified in the alert.

Feature

**Drag and tilt Google Maps**

With enabled tilt and optimized graphics, you can now [tilt and rotate Google Maps visualizations](https://support.google.com/looker-studio/answer/9713352#tilt). You can tilt a combo map visualization to display a map layer in three dimensions.

Feature

**View underlying data available to all users**

Looker Studio and Looker Studio Pro users can [view the underlying data](https://support.google.com/looker-studio/answer/13828799) that is available in any chart in a tabular form. This can help you make the best decisions about what to include in the chart. Viewing the underlying data can also help you troubleshoot problems with your reports.

Feature

**Quick filters available to all users**

Originally released as a Looker Studio Pro feature, Looker Studio users can also use [quick filters](https://support.google.com/looker-studio/answer/13676237) to easily change how the data in the report is filtered without changing the report configuration for other users.

Feature

**New map visualization: Combo map**

You can now combine the properties of a filled map and a bubble map in a new Google Maps visualization, called a [combo map](https://support.google.com/looker-studio/answer/9713352#google-combo-map). Combo maps have vector graphics and three-dimensional display features that are enabled by default.

Feature

**New function:`NATIVE_DIMENSION`**

The [`NATIVE_DIMENSION` function](https://support.google.com/looker-studio/answer/14121883) lets you create Google BigQuery SQL expressions in your BigQuery data sources.

## October 19, 2023

Feature

**Visualize your Apigee API analytics data in Looker Studio**

Apigee is a platform for developing and managing APIs. The [Looker Studio Apigee connector](https://support.google.com/looker-studio/answer/11939233) lets you create reports and dashboards that are based on analytics and monetization data and share them with stakeholders and customers.

Feature

**Table Drilling and Table Tooltips**

The Drill Actions experience for table charts provides an updated drill experience for report creators and report viewers. Visit the [Drill into your data article](https://support.google.com/looker-studio/answer/13872615) for more information about the report viewer experience, and visit the [Add drill actions to charts article](https://support.google.com/looker-studio/answer/9319405) for more information about setting up drill actions.

## October 12, 2023

Feature

**Pro feature: Looker Studio Mobile app**

Use the [Looker Studio mobile app](https://support.google.com/looker-studio/answer/13549432) to access your data on the go.

Feature

**Set auto refresh on a report**

As a report editor, you can [configure a report to automatically refresh data](https://support.google.com/looker-studio/answer/14112719), at a predefined cadence, as long as the report is open. This feature helps ensure that business decisions leverage the most up-to-date data.

## October 05, 2023

Feature

**New control type: Dimension control**

The [dimension control](https://support.google.com/looker-studio/answer/14010352) lets report viewers change the dimensions on one or more charts without needing to edit the report.

Feature

**New field available in Google Ads connector**

You can now specify an [Asset Group Name](https://support.google.com/google-ads/answer/10729160) field for a Google Ads data source when you're using the [Google Ads connector](https://support.google.com/looker-studio/answer/7020275).

## October 02, 2023

Feature

**Upgrade to Looker Studio Pro**

You can now subscribe to [Looker Studio Pro](https://support.google.com/looker-studio/answer/13715508) directly by using our self-service upgrade tool.

Feature

**BigQuery native integration in Looker Studio**

[BigQuery native integration in Looker Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio#looker-studio-integration) enables new monitoring features for Looker Studio queries, improves query performance, and supports many BigQuery features. This feature is in preview.

## September 07, 2023

Feature

**Move and delete assets in bulk**

You can now [select multiple Looker Studio assets at once to move or delete](https://support.google.com/looker-studio/answer/12796004). For example, you can move more than one report from Owned by me to a team workspace, or delete multiple items from the Trash simultaneously.

Feature

**Pro feature: View a chart's underlying data**

[Viewing a chart's underlying data](https://support.google.com/looker-studio/answer/13828799) can help you make the best decisions about what data to include in that chart and can also help you troubleshoot problems with your reports.

## August 03, 2023

Change

**Improved thumbnail images**

Thumbnails display a fixed size image of 320 px X 240 px, and if possible, present a view of the entire report page. Previously, thumbnails only showed a portion of the page.

[Learn more about thumbnail images](https://support.google.com/looker-studio/answer/9044629).

Feature

**New chart type: Waterfall chart**

The new [Waterfall chart](https://support.google.com/looker-studio/answer/13642113) lets you visualize how a sequence of positive and negative values adds up to a total.

Feature

**New chart type: Candlestick chart**

The new [Candlestick chart](https://support.google.com/looker-studio/answer/13774427) lets you visualize ranges in your data, including opening and closing values, and the highs and lows of each range.

Feature

**New chart type: Boxplot chart**

The new [Boxplot chart](https://support.google.com/looker-studio/answer/13774660) lets you visualize the distribution and spread of values in your dataset.

## July 27, 2023

Change

**New Looker Studio Pro Help Center article: Best practices and tips for using team workspaces**

The [Best practices and tips for using team workspaces](https://support.google.com/looker-studio/answer/13819955?sjid=9261253590951532063-NA) article describes best practices, tips, and use cases for working with team workspaces. This article provides guidance for creating and using team workspaces efficiently and confidently and sharing content only as necessary, as well as examples of common naming conventions and scenarios.

Change

**Improved single select option for list controls**

The Single select option in drop-down and fixed-size list controls requires you to choose only one option from the list. Previously, you could de-select all options in the control, which returned all values. Now, you can select one and only one value when this option is enabled.

[Learn more about list controls](https://support.google.com/looker-studio/answer/11335992?sjid=9261253590951532063-NA).

Feature

New line improvements let you customize the look and functionality of lines in Looker Studio charts. Improvements include:

  * [Reference bands](https://support.google.com/looker-studio/answer/9921462?sjid=9261253590951532063-NA) that let you compare data against a range of values on your charts
  * Vertical reference line support for [Area](https://support.google.com/looker-studio/answer/7206478?sjid=9261253590951532063-NA#stylize-area-chart) and [Time series charts](https://support.google.com/looker-studio/answer/7059697?sjid=9261253590951532063-NA#stylize-the-chart)
  * Line style options that let you customize the appearance of lines in your charts
  * Moving average trend line that lets you visualize a moving average calculation of the data on your charts



## July 20, 2023

Feature

**Pro feature: Add a quick filter**

Quick filters provide a flexible, ad hoc way to explore your data. Use quick filters to easily change how the data in the report is filtered without changing the report configuration for other users. 

[Learn more about quick filters](https://support.google.com/looker-studio/answer/13676237).

Feature

**Pro feature: Get a personal report link**

A personal report link creates a copy of your report that is only accessible to the person who opens the link. Changes made to either the original or the private report will not affect the other report.

[Learn more about personal report links](https://support.google.com/looker-studio/answer/13627406).

Feature

**Intervals for time series charts**

You can add intervals to time series charts to show how much uncertainty there is in your data. Intervals can be represented as shaded bands (area intervals), boxes, lines, or other shapes, depending on the interval type you specify.

To add an interval to a time series chart, select the Add an interval option in the STYLE section of the properties panel.

[Learn more about intervals](https://support.google.com/looker-studio/answer/13789978)

Change

**New Explore topic in the Help Center**

You can find content that is related to exploring, analyzing, and filtering your data in [this new Explore topic](https://support.google.com/looker-studio/topic/13671305). New and existing content on filters, controls, and chart interactions lives in this topic.

Change

**Changes to Google Ads creative assets reporting**

The Google Ads connector for Looker Studio is aligned with the public Google Ads API for creative assets reporting.

To return accurate results when using Clicks and/or Impressions metrics in combination with creative asset dimensions, be sure to also include Ad Type and Asset ID dimensions in your chart. Otherwise, the chart may show inaccurate results.

Charts that aren't correctly configured will display a message that warns you about the invalid combination of dimensions and metrics.

## July 13, 2023

Feature

**Pro feature: Scheduled delivery using Chat**

Looker Studio Pro users can schedule reports to be delivered using Google Chat. You can send reports to individual recipients or to entire Chat spaces.

Feature

**Pro feature: Filter by email address for scheduled reports**

Looker Studio Pro users can add row-level security to the data in a report scheduled to be delivered through email.

Learn more about [Chat delivery and filter by email address](https://support.google.com/looker-studio/answer/9263641).

Feature

**See report and data source location on the home page**

The Location field on the Looker Studio home page shows where your Looker Studio assets live. For free Looker Studio users, you can see if a report or data source is owned by you or has been shared with you. For Looker Studio Pro users, you'll see whether the asset lives in your My Workspace, lives in a Team Workspace, or has been shared with you directly.

## June 30, 2023

Breaking

**Firewall and database IP address change**

As announced on July 14, 2022, the IP addresses used by Looker Studio to connect to the following databases have changed:

  * Amazon Redshift
  * MySQL
  * PostgreSQL
  * Microsoft SQL Server 2017



The IP addresses to use are:

  * 142.251.74.0/23
  * 2001:4860:4807::/48 (Optional, for platforms that support IPv6)



You may close any of the previously listed addresses. They are no longer used by Looker Studio.

Feature

**Improvements to bar and combo charts**

You can configure the following options for bar charts and combo charts with bars from the **STYLE** tab of the properties panel:

  * For stacked bar charts, 100% stacked bar charts, and combo charts with stacked bars, you can choose between the default Metric value label type and the Stacked label type. For stacked bar charts, you can also choose the Total label type.
  * You can use the Bar label position setting to specify the position of the bar label relative to the bars or columns in the chart.
  * In the Chart spacing section, you can define custom spacing between bars and groups of multiple bars.
  * You can select the Bar border color icon to choose a custom color for bar or column borders.



Learn more about [bar charts](https://support.google.com/looker-studio/answer/7165560) and [combo charts](https://support.google.com/looker-studio/answer/7398001).

Feature

**Audit logging for team workspaces**

You can now view Team Workspace log events in the Admin Console (Security Investigation Tool). To see these events, filter the log by choosing Team Workspace as the asset type.

Learn more about [Looker Studio log events](https://support.google.com/looker-studio/answer/9690662).

## June 16, 2023

Feature

**GA4 API dimensions/metrics**

New Google Analytics 4 data sources that you create get their fields directly from the GA4 API. Previously, GA4 data sources were based on a fixed schema with a predefined list of fields. To see new fields from the GA4 API in an existing data source, [refresh the fields](https://support.google.com/looker-studio/answer/7083608).

**Note:** This update is backwards compatible with the previous version of the connector. Refreshing a Google Analytics 4 data source will preserve the existing schema and simply add new API fields to the data source.

Learn how [connect to Google Analytics](https://support.google.com/looker-studio/answer/6370352).

Change

**Documentation update**

Updated Connect to Google Analytics. Added information and links about the GA4 schema change, and the deprecation of Universal Analytics. Removed information about connecting to Universal Analytics.

## June 08, 2023

Feature

**Dynamic links in navigation buttons**

The URL of a navigation button can be provided dynamically from a dimension value. [Learn more](https://support.google.com/looker-studio/answer/13439618#navigation_button).

## May 18, 2023

Announcement

Starting with this week's release, Looker Studio release notes are available on Google Cloud. You can also find release notes, including localized versions, in the [Looker Studio Help Center](https://support.google.com/looker-studio/answer/11521624).

Feature

**Pause report updates**. You can pause updates to minimize the number of data requests made while building and editing your report. While the report is paused, changes made to the report's data settings are placed on hold until you resume updates. Pausing report updates can potentially save on query costs because Looker Studio only requests the data needed to meet the report configuration as of the time you resumed updates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
