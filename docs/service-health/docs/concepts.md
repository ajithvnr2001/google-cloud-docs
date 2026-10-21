---
url: https://docs.cloud.google.com/service-health/docs/concepts/
title: Personalized Service Health concepts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:10.790123+00:00
---

# Personalized Service Health concepts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Personalized Service Health concepts Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the key concepts and terms used within Personalized Service Health (PSH). Understanding these concepts helps you effectively interpret events and configure alerts.

### Service health event

A service health **event** ([v1](https://docs.cloud.google.com/service-health/docs/reference/rest/v1/projects.locations.events#resource:-event),[v1beta](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/projects.locations.events#resource:-event)) is any disruptive event impacting a Google Cloud product that is relevant to your projects or resources. Examples include network outages, configuration errors, and performance issues.

Each event contains details about the overall impact of the event, updates from Google, and information specific to your Google Cloud project.

### Incident

**Incidents** are emerging and active Google Cloud service outages or degradations relevant to your projects. It is a category of a service health event.

An incident includes the following:

  * **Incident impact** : Details of the scope of the event, such as impacted Google Cloud products and locations.
  * **Updates from Google Cloud** : Periodic updates from Google Cloud support.
  * **Personalized relevance** : Incident's relevance to your Google Cloud project.
  * **Symptoms, workarounds, and ETAs** : Information to help assess impact, apply a workaround, or learn more about the root cause.



An incident may have an **incident report** , which includes the factors that contributed to the incident, and the steps Google Cloud plans to take to prevent similar incidents from reoccurring. Incident reports are available for incidents that meet the following conditions:

  * The incident has global impact or is affecting a significant percentage of customer projects across one or more regions.
  * One or more products are unavailable or severely degraded.



### Event states and detailed states

An event has two fields indicating their state. The values for these fields change as the event evolves.

  * **Event state** : Indicates the overall state of the event. It can be one of the following:

    * **Active** : Event is actively affecting Google Cloud and will continue to receive updates.
    * **Closed** : Event is no longer affecting any Google Cloud product, or has been merged with another event.
  * **Detailed state** : Provides more information on the state of the event. It applies to incidents only, and can be one of the following values depending on the event state:

    * **Emerging** : Google engineers are actively investigating the incident to determine the impact. An emerging incident will become either a confirmed or resolved incident once the impact assessment is complete. An active incident can be an emerging incident.

Support for emerging incidents is available for Google Cloud networking products only.

    * **Confirmed** : The incident is confirmed by Google engineers and impacting at least one Google Cloud product. Ongoing status updates will be provided until it is resolved.

An active incident can be a confirmed incident.

    * **Merged** : The incident was merged into a parent incident. All further updates will be published to the parent only.

    * **Resolved** : The incident is no longer affecting any Google Cloud product after action was taken. There will be no further updates.

A closed incident is usually a resolved incident.

    * **False positive** : Upon investigation, Google engineers concluded that the incident is not affecting a Google Cloud product. This state can change if the incident is reviewed again.

    * **Auto-closed** : The incident was automatically closed because of the following reasons:

      * The impact of the incident could not be confirmed.
      * The incident was intermittent or resolved itself.

The incident does not have a resolution because no action or investigation happened. If it is intermittent, the incident may reopen.




### Granular disruption status

During a multi-product or multi-location incident, individual products or locations might recover before the overall incident is resolved. Personalized Service Health provides **granular disruption status** at the per-product and per-location level to reflect partial recovery while an incident is active. Granular disruption status is available for both project-level events and organization-level events.

A product or location can have one of the following granular disruption statuses:

  * **Affected** : The product or location is experiencing disruption due to the incident.
  * **Resolved** : The specific product or location is no longer experiencing disruption and has recovered.



#### Distinction between event states and granular status

It is important to distinguish between the overall event state, the detailed state, and the granular disruption status of individual products or locations:

  * **Overall event state and detailed state** : Apply to the incident as a whole. An incident remains **Active** (with a detailed state such as **Confirmed**) as long as at least one product or location remains **Affected**. An incident transitions to **Closed** (with a detailed state of **Resolved**) only after all associated products and locations have reached **Resolved** status.
  * **Granular disruption status** : Applies independently to each affected product or location. An individual product or location can transition to **Resolved** while the overall event state remains **Active**.



When an incident is **Merged** into a parent incident, the granular disruption statuses of the child incident are cleared, and the child incident delegates granular status to the parent incident as the single source of truth.

**Note:** Alerts configured in Cloud Logging apply to overall event revisions and state changes, not to isolated granular status transitions for individual products or locations.

### Relevance

Personalized Service Health assesses the impact of all incidents to your project. If the incident's impact to your project is possible or confirmed, it becomes available in the Service Health dashboard and API.

**Relevance** describes how an incident impacts your project. The relevance may change as the incident progresses.

Relevance can have the following values:

  * **Impacted** : The incident is verified to be impacting your project. Available for [some Google Cloud products only](https://docs.cloud.google.com/service-health/docs/supported-products-locations).
  * **Related** : The incident has a direct connection with your project and impacts a Google Cloud product in a location your project uses.
  * **Partially Related** : The incident is associated with a Google Cloud product your project uses, but the incident may not be impacting your project. For example, the incident may be impacting a Google Cloud product that your project uses, but in a location that your project does not use.
  * **Not Impacted** : The incident is not impacting your project.
  * **Unknown** : The impact to your project is not known at this point.



### Product Identity Names and Display Names (Alpha and Beta only)

To let administrators quickly pinpoint operations without requiring local mappings of product identifiers, event entries in `v1alpha` and `v1beta` releases provide display strings inside referenced resources.

Specifically within the `Product` objects specified on standard payloads (located inside the `impact` collections on both `Event` and `OrganizationEvent`), two new properties assist in identification:

  * **`display_name` (string)**: An `OUTPUT_ONLY` tag exposing human-readable product titles suited for customer readouts (such as `"Google Cloud SQL"`).
  * **`previous_display_names` (repeated string)**: An `OUTPUT_ONLY` array detailing all titles this specific resource supported formerly. This maintains continuity in tracing events back through active rebrandings.

**Note:** The `display_name` and `previous_display_name` fields are for display purposes and may change as a result of product rebranding. For programmatic logic (API calls and alerting policies), use stable product IDs.

Product display fields are deferred on the `vGA (v1)` surface for maximum system stability.

To determine correct immutable identifiers for usage in filters and alerts:

  1. Open the [Supported products and locations](https://docs.cloud.google.com/service-health/docs/supported-products-locations) guide.
  2. Find the target Google Cloud product in the table.
  3. Copy the value listed under **Product ID**.



Alternatively, determine correct immutable identifiers directly from API payloads:

  1. Make an API call returning event resources (such as `projects.locations.events.list`).
  2. Inspect the `impact` block mappings in the resulting JSON array.
  3. Extract the string present in the `product` property. This value indicates the stable product ID, independent of varying display names.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
