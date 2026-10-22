---
url: https://docs.cloud.google.com/carbon-footprint/docs/issues/
title: Known issues for Carbon Footprint \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:01.621211+00:00
---

# Known issues for Carbon Footprint  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/carbon-footprint/docs/issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Carbon Footprint ](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Known issues for Carbon Footprint

This page lists known issues for Carbon Footprint. Addressing these issues is on the roadmap of Carbon Footprint.

You can also [check for existing issues](https://issuetracker.google.com/issues?q=componentid:1108255) or [open new issues](https://issuetracker.google.com/issues/new?component=1108255&template=0) using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).

## Limited coverage of Google Cloud services

Carbon Footprint does not cover all Google Cloud services, see the [list of covered services](https://docs.cloud.google.com/carbon-footprint/docs/covered-services).

## New carbon transfer configs create an off-schedule transfer run

When creating a new Carbon Footprint transfer config to [export carbon data to BigQuery](https://docs.cloud.google.com/carbon-footprint/docs/export), the BigQuery Data Transfer Service will create an initial transfer run for the current date. However, because carbon data is only published on the 15th of the month, this initial transfer run may contain no data.

Transfer configs will automatically export carbon data for future months on the 15th of each month. Historical data can be requested via backfill as described [here](https://docs.cloud.google.com/carbon-footprint/docs/export#bigquery).

## Deprecated carbon offsets fields in BigQuery export

The `carbon_offsets_kgCO2e` and `carbon_footprint_total_kgCO2e.after_offsets` fields are deprecated. Due to BigQuery behavior, these columns cannot be removed from existing export tables and will remain in the schema with `NULL` values. These fields won't be populated, in line with Google's transition from carbon offsets to carbon removal technologies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
