---
url: https://docs.cloud.google.com/looker/docs/send-amazon-s3/
title: Using the Looker Scheduler to deliver content \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:36.000849+00:00
---

# Using the Looker Scheduler to deliver content  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/send-amazon-s3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using the Looker Scheduler to deliver content Stay organized with collections  Save and categorize content based on your preferences. 

> This page is about delivering content from Looks and Explores. For information about scheduling [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards), visit the [Scheduling and sending dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) documentation page.

Looker provides several ways to [share](https://docs.cloud.google.com/looker/docs/sharing-data) content from dashboards, data tables or visualizations from a Look, or Explore queries to the applications and services that are already a part of your workflow. With Looker's scheduling capability, you can send instant, one-time content deliveries or periodic, recurring content deliveries — also called "schedules" — to one of Looker's built-in delivery destinations or to a third-party service that is [integrated with Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#list_of_integrated_services). Built-in delivery destinations include email, webhook, an Amazon S3 bucket, and an SFTP server.

Looker admins and developers play critical roles in configuring schedules so that all Looker users can deliver content. See the following links for documentation that is relevant to each of these roles and to all Looker users.

## Delivery documentation for Looker admins

  * [Enabling user access](https://docs.cloud.google.com/looker/docs/configuring-deliveries) to Looker's content delivery capabilities
  * Managing users' deliveries using the [**Schedules**](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule) page in the **Alerts & Schedules** section of the **Admin** panel
  * Viewing the recent history of the Scheduler's activity from the [Schedule History](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule-history) page in the **Alerts & Schedules** section of the **Admin** panel
  * [Enabling the third-party services](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) that are integrated with Looker through the [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub)



## Delivery documentation for Looker developers

  * [Tagging LookML](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) fields to enable deliveries to some integrated services
  * [Configuring datagroups](https://docs.cloud.google.com/looker/docs/reference/param-model-datagroup#creating_a_datagroup_to_schedule_deliveries_on_the_last_day_of_every_month) that can be used to trigger a content delivery



## Delivery documentation for all Looker users

  * [Delivering dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards)
  * [Delivering Looks and Explores](https://docs.cloud.google.com/looker/docs/delivering-looks-explores)
  * [Scheduling deliveries to the Slack integration](https://docs.cloud.google.com/looker/docs/scheduling-slack)
  * [Viewing deliveries that you have created](https://docs.cloud.google.com/looker/docs/user-schedules)



## Delivery options

Each type of Looker content has unique delivery options, which are summarized in the following table. Click each link to access the relevant documentation for that delivery option.

Content | Delivery Options | Destination Options | Format Options  
---|---|---|---  
[Explore](https://docs.cloud.google.com/looker/docs/delivering-looks-explores) | One-time | 

  * [email](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_email)
  * [webhook](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_webhooks)
  * [Amazon S3 bucket](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_amazon_s3_buckets)
  * [SFTP server](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_sftp_servers)
  * [Admin-enabled integrations ](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_third-party_integrations)

| Data Table, Visualization, CSV, XLSX, JSON, Text, HTML  
[Look](https://docs.cloud.google.com/looker/docs/delivering-looks-explores) | One-time, Recurring | 

  * [email](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_email)
  * [webhook](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_webhooks)
  * [Amazon S3 bucket](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_amazon_s3_buckets)
  * [SFTP server](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_sftp_servers)
  * [Admin-enabled integrations](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#delivery_options_for_third-party_integrations)

| Data Table, Visualization, CSV, XLSX, JSON, Text, HTML  
[Dashboard](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) | One-time, Recurring | 

  * [email](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#email)
  * [webhook](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#webhook)
  * [Amazon S3 bucket](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#amazon_s3)
  * [SFTP server](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#sftp)
  * [Admin-enabled integrations](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards#integrated_service_destinations)

| PDF, Visualization, CSV ZIP file  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
