---
url: https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-metadata-change-feeds/
title: Troubleshoot metadata change feeds \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:08.061536+00:00
---

# Troubleshoot metadata change feeds  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/troubleshoot-metadata-change-feeds/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Troubleshoot metadata change feeds Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you troubleshoot and resolve common issues with Knowledge Catalog (formerly Dataplex Universal Catalog) metadata change feeds.

## Metadata change feeds creation errors

This section describes how to resolve errors that you might encounter when you create metadata change feeds.

### Permission denied errors

You receive a `PERMISSION_DENIED` error when trying to create a metadata change feed.

The issue occurs because you or the Knowledge Catalog service account might be missing required permissions.

To resolve this issue, review these requirements:

  * Ensure that you have the `dataplex.metadataFeeds.create` permission.

  * Ensure that you have the `dataplex.entryGroups.export` permission on the scope of the feed (Organization, Project, or Entry Group).

  * Ensure that the Knowledge Catalog service account (`service-{PROJECT_NUMBER}@gcp-sa-dataplex.iam.gserviceaccount.com`) has the `roles/pubsub.publisher` role on the destination Pub/Sub topic.




### VPC Service Controls errors

You receive a `PERMISSION_DENIED` or VPC Service Controls error when creating a feed.

To resolve the issue, check that the metadata change feed and the resources it monitors belong to the same VPC Service Controls perimeter:

  * If the feed is organization-scoped, only projects within the same perimeter are monitored.

  * If the feed is project-scoped or entry-group-scoped, ensure that all specified projects or entry groups are in the same perimeter as the project where you are creating the feed.




## Notification delivery issues

This section describes how to resolve issues with notification delivery.

### Notifications not received

You are not receiving notifications in your Pub/Sub topic. This can be caused by several factors:

  * **Missing permissions** : the Knowledge Catalog service account lost the `roles/pubsub.publisher` role on the topic.

  * **Activation delay** : a newly created or updated feed can take up to 10 minutes to become active.

  * **Topic deleted** : if the destination Pub/Sub topic is deleted, Knowledge Catalog stops publishing.

  * **Scope or filter mismatch** : the changes might not match the configured scope or filters.




To resolve the issue, check the following:

  * Verify that the Knowledge Catalog service account has the `roles/pubsub.publisher` role on the topic.

  * Wait at least 10 minutes after creating or updating a feed.

  * Check if the Pub/Sub topic exists. If it was deleted, you must recreate it.

  * Review your feed configuration to ensure the scope and filters match the metadata changes you expect to receive.




### Duplicate notifications

You receive duplicate notification messages. Knowledge Catalog ensures "at least once" delivery, which means duplicate messages might occur, especially during retries.

Configure your subscriber application to handle potential duplicates. You can use the `messageId` or the change timestamp to identify and deduplicate messages.

## Content issues

This section describes how to resolve issues with the content of metadata change feed notifications.

### Missing full metadata in payload

The notification message contains only the resource name and change type, but not the full metadata or the specific changes.

This is because by design, metadata change feed notifications provide "change signatures" (what changed) rather than the full payload. This keeps messages lightweight and avoids payload size limits.

Use the resource name provided in the notification to call the Dataplex API (for example, [`GetEntry`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get)) and retrieve the current state of the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
