---
url: https://docs.cloud.google.com/service-health/docs/service-health-fallback/
title: Use Google Cloud Service Health as a fallback \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:22.638523+00:00
---

# Use Google Cloud Service Health as a fallback  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/service-health-fallback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Use Google Cloud Service Health as a fallback Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use Google Cloud Service Health in the rare event Personalized Service Health itself is unavailable or affected by a disruption, or the impacted product has not yet onboarded to Personalized Service Health.

Google Cloud Service Health provides you with information on ongoing widespread incidents that meet certain criteria. Personalized Service Health will always have the most information available to Google Cloud customers.

Prior to March 24, 2022, Google Cloud Service Health was called Google Cloud Status Dashboard.

## Access Google Cloud Service Health

You can access Google Cloud Service Health through the following:

  * A public status dashboard: [Google Cloud Service Health](https://status.cloud.google.com/)
  * A public [RSS feed](https://status.cloud.google.com/en/feed.atom)
  * The Google Cloud console:

    1. In the Google Cloud console, go to the **Support** > **Cases** page.

[Go to Cases](https://console.cloud.google.com/support/cases)

    2. Using the resource selector on the console toolbar, select the resource for which you'd like to list known issues.

    3. Click the **Known issues** tab.

Known issues also include minor and limited-scope incidents. You can [link a support case to a known issue](https://docs.cloud.google.com/support/docs/customer-care-procedures#link-cases) so that you get regular updates and can communicate with support staff. Support cases are appropriate for issues that don't qualify as incidents or where direct interaction is needed. If you have Premium, Enhanced, or Standard Support, you can report an incident by [creating a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case).




If you are unable to access Google Cloud Service Health through the previous resources, you can use the [Google Cloud Platform Support Questions form](https://support.google.com/cloud/contact/prod_issue).

## Supported Google Cloud Service Health incidents

For most Google Cloud incidents, impacted customers receive incident communications directly through Personalized Service Health in the Google Cloud console. If they meet the alert conditions, these incidents also trigger any [Service Health alerts](https://docs.cloud.google.com/service-health/docs/configure-alerts-cloud-logging) that you have configured.

The global Service Health team monitors the status of products using many different types of signals and updates Google Cloud Service Health in the event of a widespread issue. If needed, they will post a detailed incident analysis report after an incident has been resolved. To learn about how the Support and product engineering teams work together to resolve an incident, see the [incident lifecycle](https://docs.cloud.google.com/service-health/docs/incident-lifecycle).

Incidents that meet any of the following criteria appear in Google Cloud Service Health:

  * Broad, severe public incidents
  * Incidents that occur when the Personalized Service Health dashboard is unavailable



### Broad Severe incident

Google Cloud defines an incident as a Broad Severe incident if it has global impact or affecting a significant percentage of customer projects across multiple regions.

In the rare instance a broad severe incident occurs, we act with urgency to resolve any issues.

During a broad severe incident, the status of the issue is communicated through the [dashboard](https://status.cloud.google.com/). A broad severe incident is marked as cancel **Service outage** on the dashboard. After the issue is resolved, we publish a public incident report that includes the details of the factors that contributed to the incident and the steps we plan to take to prevent such incidents from reoccurring.

In the case of smaller-scoped incidents, a nonpublic report might be made available to customers.

### Issues not listed in Google Cloud Service Health

Google Cloud Service Health provides current and historical status information for any broad severe incident that affects Google Cloud products and services. If you are experiencing an issue that is not listed by Google Cloud Service Health, the issue might be isolated to your projects or instances, or it might impact a limited number of customers. Incidents that have less scope can appear on the [Support Portal](https://support.cloud.google.com/portal/). You can contact Service Health about any issues you are experiencing that are not listed by Google Cloud Service Health.

If you are already using [Personalized Service Health](https://console.cloud.google.com/servicehealth/incidents), check if the issue is listed there to determine if your project or instance is affected.

If you are using the Google Cloud console, in the top toolbar, select help > **Send feedback**.

## Consume Google Cloud Service Health data programmatically

You can build integrations to consume the data displayed by Google Cloud Service Health in the following ways:

  * Through an RSS feed.
  * Through a JSON history file. You can download the [schema for the JSON file](https://status.cloud.google.com/incidents.schema.json) from the public status dashboard.

Use the fields marked **Stable** instead of the fields marked **Unstable**. In general, ID fields are considered **Stable** whereas fields such as display names are considered **Unstable** and might change without warning. Use **Stable** fields when integrating with an external system or building automation. 

If you're trying to programmatically identify incidents impacting a particular set of products, use the product IDs (`affected_products>id`), not their display names. See the [product catalog](https://status.cloud.google.com/products.json) for the mapping between product IDs and product names.

A product ID provides a stable field to key off while allowing the display name of a product to change. You should reference the product ID when programmatically identifying incidents impacting a set of products.




The RSS feed and JSON history file provide incident status information such as the following:

  * Products and locations that the incident impacts
  * Incident start time and end time
  * Overall severity
  * Incident updates that describe how the incident changes over time, including its status and the then impacted locations



### Integrations based on prior Google Cloud Service Health implementations

In both the RSS feed and the JSON file, the regional status information is an addition to the information that was already being published prior to the introduction of regionalized status reporting and change in the name of Google Cloud Service Health. Therefore, we expect your existing integrations to continue working. However, if you want to consume the regional status information through your integrations, then you need to modify them.

Here's a detailed description of how regional information appears in both the RSS feed and JSON file:

  * **RSS feed**

The regional status information is a new addition to the feed information that was provided prior to the introduction of regionalized status. Any locations that are reported as affected are appended to the RSS message.

  * **JSON file**

Prior to the regional status update, Google Cloud published a stream of incidents where each incident contained a list of affected products and a list of status updates for each, if any. These status updates contained an unstructured string field that did or did not contain the location information.

Now, Google Cloud publishes a stream of incidents just as it did before. However, for every incident, each status update contains the following new fields:

    * `updates.affected_locations`: contains a structured list of affected locations at the time the update was posted. Every update record and the `most_recent_update` record contain this field.
    * `currently_affected_locations`: contains the most recent information on the locations that are actively impacted by the incident. Unlike `updates.affected_locations`, this list becomes empty after the incident is resolved (that is, when `end` is set to a non-empty value). 
    * `previously_affected_locations`: contains a list of locations that were previously impacted during an incident, but aren't currently. As the incident progresses, some locations might have an outage resolution. These locations will still exist in the `previously_affected_locations field`. Once the incident is resolved (that is, when `end` is set to a non-empty value), this field contains a list of all locations that were impacted during this incident.



## Find information about past product disruptions and outages

Google Cloud Service Health keeps a record of disruptions and outages for Google Cloud products for up to five years. The [dashboard](https://docs.cloud.google.com/service-health/docs/service-health-fallback/) shows the current status of products by locale. To view information about product disruptions and outages in the last year, click arrow_forward **View incident history**. To view a product's outage history for the last five years, click history **See more** for that product.

## View regionalized status information

Google Cloud Service Health displays the status of all Google Cloud products organized by region and global locale. To view the status for a multi-region, select the region-specific tab.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
