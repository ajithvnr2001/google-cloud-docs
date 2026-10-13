---
url: https://docs.cloud.google.com/chronicle/docs/secops/secops-overview/
title: Google SecOps overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:53.173993+00:00
---

# Google SecOps overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/secops-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps overview

Supported in:

Google SecOps 

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

Google Security Operations is a cloud service, built as a specialized layer on top of Google infrastructure, designed for enterprises to privately retain, analyze, and search the large amounts of security and network telemetry they generate.

Google SecOps normalizes, indexes, correlates, and analyzes the data to provide instant analysis and context on risky activity. Google SecOps can be used to detect threats, investigate the scope and cause of those threats, and provide remediation using prebuilt integrations with enterprise workflow, response, and orchestration platforms.

Google SecOps lets you examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed within your enterprise. You can narrow your search to any specific asset, domain, or IP address to determine if any compromise has taken place.

The Google SecOps platform enables security analysts to analyze and mitigate a security threat throughout its lifecycle by employing the following capabilities:

  * **Collection** : Data is ingested into the platform using forwarders, parsers, OpenTelemetry collectors, connectors, and webhooks.
  * **Detection** : This data is aggregated, normalized using the Unified Data Model (UDM), and linked to detections and threat intelligence.
  * **Investigation** : Threats are investigated through case management, search, collaboration, and [context-aware analytics](https://docs.cloud.google.com/chronicle/docs/detection/context-aware-analytics).
  * **Response** : Security analysts can respond quickly and provide resolutions using automated playbooks and case management.



## Data collection

Google SecOps can ingest numerous security telemetry types through a variety of methods, including the following:

  * **Forwarder** : A lightweight software component, deployed in the customer's network, that supports syslog, packet capture, and existing log management or security information and event management (SIEM) data repositories.
  * **Collector** : A software component, deployed in the customer's network, that supports many data sources routing to Google SecOps.
  * **Ingestion APIs** : APIs that enable logs to be sent directly to the Google SecOps platform, eliminating the need for additional hardware or software in customer environments.

  * **Third-party integrations** : Integration with third-party cloud APIs to facilitate ingestion of logs, including sources like Office 365 and Azure AD.




## Threat analysis

The analytical capabilities of Google SecOps are delivered as a browser-based application. Many of these capabilities are also accessible programmatically through Read APIs. Google SecOps gives analysts a way, when they see a potential threat, to investigate further and determine how best to respond.

## Security and compliance

As a specialized, private layer built over core Google infrastructure, Google SecOps inherits the compute, storage, and security design capabilities of that infrastructure.

To learn more about supported regulatory certifications, industry standards, data residency boundaries (DRZ), and security controls—along with links to their authoritative documentation—see [Supported compliance standards](https://docs.cloud.google.com/chronicle/docs/secops/compliance).

## Summary of Google SecOps features

This section describes some of the features available in Google SecOps.

### Search

  * **UDM Search** : Lets you find UDM events and alerts within your Google SecOps instance.
  * **Raw Log Scan** : Search your raw unparsed logs.
  * **Regular Expressions** : Search your raw unparsed logs using regular expressions.



### Case management

Group related alerts into cases, sort and filter cases queue for triage and prioritization, assign cases, collaborate on every case, case audit and reporting.

### Playbook designer

Build playbooks by selecting predefined actions and dragging and dropping them into the playbook canvas without additional coding. Playbooks also enable you to create dedicated views for each alert type and each SOC role. Case management presents only the data relevant to a specific alert type and user role.

### Graph investigator

Visualize the who, what, and when of an attack, identify opportunities for threat hunting, capture the full picture and take action.

### Dashboard and reporting

Effectively measure and manage operations, demonstrate value to stakeholders, track real-time SOC metrics and KPIs. You can use built-in dashboards and reports or build your own.

### Integrated development environment (IDE)

Security teams with coding skills can modify and enhance existing playbook actions, debug code, build new actions for existing integrations, and create integrations that are not available in the Content Hub.

### Investigative views

  * **Asset view** : Investigate assets within your enterprise and whether or not they have interacted with suspicious domains.
  * **IP Address view** : Investigate specific IP addresses within your enterprise and what impact they have on your assets.
  * **Hash view** : Search for and investigate files based on their hash value.
  * **Domain view** : Investigate specific domains within your enterprise and what impact they have on your assets.
  * **User view** : Investigate users within your enterprise who may have been impacted by security events.
  * **Procedural filtering** : Fine tune information about an asset, including by event type, log source, network connection status, and Top Level Domain (TLD).



### Highlighted information

  * Asset insight blocks highlights the domains and alerts that you might want to investigate further.
  * Prevalence graph shows the number of domains an asset has connected to over a specified time period.
  * Alerts from other popular security products.



### Detection engine

You can use the Google SecOps Detection Engine to automate the process of searching across your data for security issues. You can specify rules to search all of your incoming data and notify you when potential and known threats appear in your enterprise.

### Access control

You can both employ predefined roles and configure new roles to control access to classes of data, alerts, and events stored within your Google SecOps instance. [Identity and Access Management](https://docs.cloud.google.com/iam/docs) provides access control for Google SecOps.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
