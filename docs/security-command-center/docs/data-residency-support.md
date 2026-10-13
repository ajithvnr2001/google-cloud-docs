---
url: https://docs.cloud.google.com/security-command-center/docs/data-residency-support/
title: Plan for data residency \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:42.445550+00:00
---

# Plan for data residency  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/data-residency-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Plan for data residency Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

_Data residency_ gives you more control over where your Security Command Center data is located. This document provides essential information about how Security Command Center supports data residency.

The following definitions apply to this document:

  * A _location_ is a Google Cloud [region or multi-region](https://cloud.google.com/about/locations) that corresponds to the location in which your data resides.
  * The meaning of the term _your data_ is equivalent to the meaning of the term "Customer Data" in the _Data Location_ item in the Google Cloud [General Service Terms](https://cloud.google.com/terms/service-terms).



To learn how to work with Security Command Center resources when data residency is enabled, see [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints).

## Supported data locations

This section describes the data locations that you can use for Security Command Center and related services.

### Security Command Center data locations

When you enable data residency, the Security Command Center API supports the following Google Cloud multi-regions as data locations:

European Union (`eu`)
    Data resides in any Google Cloud region within member states of the European Union.
Kingdom of Saudi Arabia (KSA) (`sa`)
    Data resides in any Google Cloud region in KSA.
United States (`us`)
    Data resides in any Google Cloud region in the United States.

If you use the Standard or Premium service tier, then upgrading to the Enterprise tier does not change the location of your Security Command Center data. If you did not enable Security Command Center data residency for the Standard or Premium tier, then you cannot enable it when you upgrade to the Enterprise tier. 

For more information about Security Command Center locations, see [Products available by location](https://cloud.google.com/about/locations#multi-region).

If you need to specify a default location for data residency that Security Command Center doesn't support, then contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact).

### Google SecOps data locations

For Google Security Operations, data residency is always enabled. To find out where Google SecOps data resides, see the [list of Google SecOps locations](https://cloud.google.com/terms/secops/data-residency).

**Note:** By default, data residency controls for Google SecOps are enforced when data is at rest. If you need these controls to be enforced when data is in use or in transit, then contact your account representative.

## Supported features and launch stages

If you enable data residency, some features might not be available, depending on the service tier that you're using.

### Enterprise tier

For the Enterprise service tier of Security Command Center, the following features aren't available:

  * AI Discovery service in KSA
  * Gemini inventory in KSA
  * [Cloud Infrastructure Entitlement Management (CIEM) for external cloud providers](https://docs.cloud.google.com/security-command-center/docs/ciem-overview)
  * **Resources scanned** counts on the [Compliance](https://console.cloud.google.com/security/command-center/compliance) page in the Google Cloud console 

Applies only if you use Security Health Analytics for compliance management. 

  * Model Armor in KSA
  * [Mandiant Attack Surface Management](https://docs.cloud.google.com/security/products/attack-surface-management)



### Premium tier

For the Premium service tier of Security Command Center, the following features aren't available:

  * AI Discovery service in KSA
  * Gemini inventory in KSA
  * **Resources scanned** counts on the [Compliance](https://console.cloud.google.com/security/command-center/compliance) page in the Google Cloud console 

Applies only if you use Security Health Analytics for compliance management. 

  * Model Armor in KSA



### Standard tier

For the Standard service tier of Security Command Center, the following features aren't available:

  * AI Discovery service in KSA
  * **Resources scanned** counts on the [Compliance](https://console.cloud.google.com/security/command-center/compliance) page in the Google Cloud console 

Applies only if you use Security Health Analytics for compliance management. 

  * Model Armor in KSA



### Detectors

Some detectors in [Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/cloud-run-threat-detection-overview#detectors) and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview#detectors) can't be enabled when you enable data residency for a specific location.

### Pre-GA features and services

As stated in the _Pre-GA Offerings Terms_ item in the [General Service Terms](https://cloud.google.com/terms/service-terms), the _Data Location_ terms do not apply to pre-[General Availability](https://cloud.google.com/products#product-launch-stages) (GA) features and services.

## Requirements for data residency

This section explains the requirements for using data residency in Security Command Center and related services.

### Requirements for Security Command Center

You can enable data residency for Security Command Center when you [activate Security Command Center for an organization for the first time](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation). You can change the data residency configuration for the Standard and Premium service tiers.

**Important:** For the Enterprise service tier, before you activate Security Command Center with data residency controls, you must contact your Google Cloud account representative and schedule a date and time when you will activate Security Command Center. After activation, your account representative will help ensure that your Google SecOps instance is configured to fully support data residency controls. Contact your Google Cloud account representative if you have questions. 

Data residency requires you to use the Security Command Center v2 API. If data residency is enabled, then you can't use earlier versions of the Security Command Center API.

If you don't enable data residency when you activate Security Command Center, then Security Command Center doesn't restrict your data to any particular location, and it's stored in accordance with the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms).

If the Security Command Center Standard tier was automatically activated in your organization, and then you deploy an organization policy that restricts resource locations, Security Command Center might be deactivated. You must reactivate it manually.

To change the data residency configuration before deploying this organization policy, see [Modify data residency or data encryption configuration](https://docs.cloud.google.com/security-command-center/docs/modify-data-residency-encryption).

For additional information, see [Data residency considerations after the Standard tier is auto-activated](https://docs.cloud.google.com/security-command-center/docs/migrate-standard-legacy#data-residency).

### Requirements for Google SecOps

For Google SecOps, data residency is enabled by default. You can't disable data residency for Google SecOps.

**Note:** By default, data residency controls for Google SecOps are enforced when data is at rest. If you need these controls to be enforced when data is in use or in transit, then contact your account representative.

## How and when data residency is enforced

When you enable data residency for Security Command Center, some Security Command Center data is kept within a specified location when it's in one of the following states:

  * _At rest_ : Committed to persistent storage
  * _In use_ : In memory
  * _In transit_ : In memory or on the wire, _and_ [encrypted with Transport Layer Security (TLS)](https://docs.cloud.google.com/docs/security/encryption-in-transit#end-user-to-gcp-service) by a client outside of Google

**Note:** By default, data residency controls for Google SecOps are enforced when data is at rest. If you need these controls to be enforced when data is in use or in transit, then contact your account representative.

After you enable data residency and select a data location, Security Command Center does the following:

  * When a finding is created for a resource that resides in the specified location, the finding always resides in your data location.
  * When a finding is created for a resource that resides in another location, the finding eventually resides in your data location. However, the finding might temporarily reside in a different region.
  * When you create specific types of configuration resources in your data location, they reside in that location.
  * In cases where Security Command Center stores data that is not _Customer Data_ , as defined in the _Data Location_ item in the Google Cloud [General Service Terms](https://cloud.google.com/terms/service-terms), Security Command Center stores the data in accordance with the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms).



## Security Command Center resources and data residency

The following list explains how Security Command Center applies data residency controls to Security Command Center resources. If a resource isn't listed here, then it's not subject to data residency controls and is stored in accordance with the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms).

BigQuery exports
    

[BigQuery export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query) are subject to data residency controls. Use the [regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints) to create and manage these configuration resources.

The Security Command Center API represents BigQuery export configurations as [`BigQueryExport`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.bigQueryExports#resource:-bigqueryexport) resources.

Continuous exports
    

[Continuous export configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) are subject to data residency controls. Use the [regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints) to create and manage these configuration resources.

The Security Command Center API represents continuous export configurations as [`NotificationConfig`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.notificationConfigs#resource:-notificationconfig) resources.

Findings
    

Findings are subject to data residency controls.

When a finding is created for a resource that resides in the data location that you selected, the finding always resides in the same location.

When a finding is created for a resource that resides in another location, the finding eventually resides in the data location that you selected. However, the finding might reside in a different region at the time that it's created.

To keep all findings in your data location, always create all of your Google Cloud resources in that location.

Google SecOps resources
    

[All Google SecOps resources](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) are subject to data residency controls. Use the [regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints) to create and manage these configuration resources.

**Note:** By default, data residency controls for Google SecOps are enforced when data is at rest. If you need these controls to be enforced when data is in use or in transit, then contact your account representative.
Mute rules
    

[Mute rule configurations](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings) are subject to data residency controls. Use the [regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints) to create and manage these configuration resources.

The Security Command Center API represents mute rule configurations as [`MuteConfig`](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.locations.muteConfigs#resource:-muteconfig) resources.

Other Security Command Center resources and settings
    

Security Command Center resources and settings that are missing from this list, such as those that define which services are enabled or which tier is active, aren't subject to data residency controls. This data is stored in accordance with the [Google Cloud Platform Terms of Service](https://cloud.google.com/terms).

## Create or view data in a location

When data residency is enabled, you must specify a location when you create or view any data that's subject to data residency controls. Security Command Center automatically chooses a location for findings that it creates.

You can create or view data in only one location at a time. For example, if you list findings in the United States (`us`) location, then you won't see findings in the European Union (`eu`) location.

To learn how to create or view data that's subject to data residency controls, see [About the jurisdictional Google Cloud console](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#jurisdictional-console) and [Tools for regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints#tools).

## What's next

  * Learn how to [activate Security Command Center for an organization](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation).
  * Find out how to use [Security Command Center regional endpoints](https://docs.cloud.google.com/security-command-center/docs/regional-endpoints).
  * Enable Security Command Center to [stream findings to BigQuery](https://docs.cloud.google.com/security-command-center/docs/how-to-analyze-findings-in-big-query).
  * Set up [continuous exports](https://docs.cloud.google.com/security-command-center/docs/how-to-export-data#continuous_exports) from Security Command Center to Pub/Sub.
  * Create a [mute rule](https://docs.cloud.google.com/security-command-center/docs/manage-mute-rules#create_a_mute_rule) for findings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
