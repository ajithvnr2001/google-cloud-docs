---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types/
title: Method types \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:38.940061+00:00
---

# Method types  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-method-types/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Method types Stay organized with collections  Save and categorize content based on your preferences. 

Sensitive Data Protection includes different types of methods that you can use to inspect, transform (_de-identify_), discover, and classify data. Using these methods, you can scan data both on and off Google Cloud and optimize the behavior of Sensitive Data Protection for different types of workloads.

Sensitive Data Protection provides the following method types:

  * Content methods
  * Storage methods
  * Hybrid methods
  * Discovery methods



## Inspection and de-identification methods

This section describes the methods that you can use to locate and, optionally, de-identify each piece of data that matches an [information type](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) listed in your [inspection configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig).

### Content methods

_Content methods_ are synchronous, stateless methods. The data to be inspected or transformed is sent directly in the request to the DLP API. Sensitive Data Protection inspection findings or transformed data is returned in the API response. Request data is encrypted in transit and is not stored.

![Content methods data flow showing a client sending data via an
API request to Sensitive Data Protection, which can inspect and classify or
de-identify and transform the data, sending a synchronous API response to the
client.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/concepts-method-types-contentmethods.svg)

#### When to use content methods

The following are some common use cases:

  * **Inspect user input in real time** : Scan form fields, chat messages, or feedback submissions synchronously within web and mobile applications before storing data in databases.
  * **Mask sensitive text before external processing** : De-identify or redact sensitive tokens from text strings synchronously before passing content to third-party APIs or large language models (LLMs).
  * **Redact sensitive data from uploaded images** : Obfuscate sensitive text in image formats (such as JPEG, PNG, or TIFF) by overlaying opaque rectangles on detected PII before displaying or storing the image.
  * **Re-identify tokenized data on demand** : De-tokenize previously pseudonymized tokens in authorized server-side workflows when an authenticated business user requires access to the original plaintext.
  * **Validate data privacy in client-side applications** : Run stateless privacy checks on endpoints without provisioning cloud storage repositories or configuring backend job infrastructure.



To learn more, explore the REST API reference for content methods:

  * [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect)
  * [`content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify)
  * [`content.reidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify)
  * [`image.redact`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact)



### Storage methods

_Storage methods_ are designed to inspect data stored on Google Cloud in systems like [Cloud Storage](https://docs.cloud.google.com/storage), [BigQuery](https://docs.cloud.google.com/bigquery), and [Firestore in Datastore mode (Datastore)](https://docs.cloud.google.com/datastore). To enable storage inspection, you create a Sensitive Data Protection job using the [`dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource. Each job runs as a managed service to inspect data and then perform [Sensitive Data Protection actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) such as save or publish findings. In addition to these optional actions, Sensitive Data Protection creates and stores details about the job including job status, bytes scanned, and summary findings per infoType. You can manage jobs using the DLP API or Sensitive Data Protection in the [Google Cloud console](https://console.cloud.google.com/security/sensitive-data-protection).

![Storage methods data flow showing Sensitive Data Protection inspecting
data on a Google Cloud storage repository, and then either saving or publishing
findings.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/concepts-method-types-storagemethods.svg)

#### When to use storage methods

The following are some common use cases:

  * **Scan large-scale analytical tables** : Inspect petabyte-scale datasets in BigQuery using distributed, serverless batch scanning.
  * **Audit unstructured file repositories** : Inspect documents, archives, and media files stored in Cloud Storage buckets to locate unencrypted or misplaced sensitive data.
  * **Track historical scan results and trends** : Persist detailed inspection findings directly into BigQuery tables to track findings over time and generate compliance audit trails.
  * **Trigger event-driven remediation workflows** : Stream scan completion events and high-risk finding alerts to Pub/Sub to start automated security response playbooks.
  * **Sample large datasets for cost efficiency** : Configure sampling limits or row limits to estimate data risk posture across large databases without scanning entire datasets.



To learn more, explore the REST API reference for the [`projects.dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource. You specify the storage details in the [`StorageConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#storageconfig) object.

### Hybrid methods

_Hybrid methods_ are a set of asynchronous API methods that allow you to scan payloads of data sent from virtually any source for sensitive information and store the findings in Google Cloud. Hybrid methods are similar to content methods in that the data you want to inspect is included in one or more inspection requests; however, unlike content methods, _hybrid methods_ do not return inspection results in the API response. Instead, inspection results are processed server-side asynchronously and results are tabulated and stored in a manner similar to storage methods.

To enable hybrid inspection, you create a Sensitive Data Protection job using the [`dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource. Each _hybrid_ job runs as a managed service to listen for inspection requests and performs [Sensitive Data Protection actions](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-actions) such as save or publish findings. In addition to these optional actions, Sensitive Data Protection creates and stores details about the job including job status, bytes scanned, and summary findings per infoType. You can manage jobs using the DLP API or Sensitive Data Protection in the [Google Cloud console](https://console.cloud.google.com/security/sensitive-data-protection).

![Hybrid jobs data flow showing your application sending data from
an external source to Sensitive Data Protection, Sensitive Data Protection inspecting
the data, and then either saving or publishing
findings.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/concepts-method-types-hybrid.svg)

#### When to use hybrid methods

The following are some common use cases:

  * **Inspect data in hybrid and multi-cloud environments** : Stream data from on-premises databases, bare-metal servers, or other cloud providers into Sensitive Data Protection while keeping finding reports centralized in Google Cloud.
  * **Audit custom application data pipelines** : Send streaming data from custom crawlers, microservices, or ETL pipelines to Sensitive Data Protection without managing local scanner worker fleets.
  * **Sanitize workloads during cloud migration** : Continuously inspect and tokenize sensitive assets during live database replication from legacy systems into Google Cloud.
  * **Centralize multi-cloud compliance reporting** : Aggregate inspection results across disparate operating environments into a single BigQuery dataset for unified governance.
  * **Process custom file types and proprietary formats** : Extract text client-side from proprietary binary formats and stream the extracted payloads to Sensitive Data Protection for inspection.



To learn more, explore the REST API reference for the [`projects.dlpJobs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs) resource. You specify the data source in the `hybridOptions` field of the [`StorageConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#storageconfig) object.

## Discovery methods

_Discovery methods_ allow you to configure [sensitive data discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) to generate _data profiles_. Data profiles provide insights to help you determine where sensitive data resides in your organization, what kind of sensitive data you are storing, and whether that data has access controls in place.

You can configure discovery to scan data stored on Google Cloud in systems like BigQuery, Cloud SQL, Cloud Storage, and Vertex AI. If you have a Security Command Center Enterprise activation, you can also use Sensitive Data Protection to scan data from other cloud providers.

You can specify actions that you want Sensitive Data Protection to perform after each discovery scan. For example, you can send scan results to other Google Cloud services—like Security Command Center and Google Security Operations—to increase your visibility into your organization's data security posture. You can configure the discovery service to tag your profiled resources to automatically grant or deny IAM access to those resources. You can also export the data profiles to BigQuery. You can connect the exported profiles to Data Studio to [view the premade report](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles#use_a_premade_report). You can also create your own custom queries and reports.

To enable discovery, you create a [`DiscoveryConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs) resource. Discovery runs based on the scope and frequency that you set in the discovery configuration. For information about where Sensitive Data Protection stores the generated profiles, see [Data residency considerations](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency).

You can manage the discovery configurations, data profiles, and Cloud SQL connections using the DLP API or the [Google Cloud console](https://console.cloud.google.com/security/sensitive-data-protection).

![Discovery data flow showing Sensitive Data Protection discovering data from
various data sources and sending data profiles to various Google Cloud
services.](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/concepts-method-types-discoverymethods.svg)

### When to use discovery methods

The following are some common use cases:

  * **Automate organization-wide data discovery** : Continuously scan and profile all data assets across BigQuery, Cloud SQL, and Cloud Storage without writing individual scan jobs or schedules.
  * **Identify high-risk data repositories** : Generate data risk and data sensitivity scores for tables and buckets to prioritize data protection and governance initiatives.
  * **Enforce dynamic access controls with data tags** : Automatically tag profiled resources based on discovered infoTypes to grant or restrict access using Identity and Access Management policies.
  * **Feed data security posture management** : Send discovery profile insights to Security Command Center and Google Security Operations to correlate data risks with infrastructure threats.
  * **Visualize compliance posture with executive dashboards** : Export data profiles to BigQuery and connect premade Data Studio dashboards to monitor sensitive data distribution across the organization, folders and projects.



To learn more, explore the REST API reference for the following:

  * Discovery configurations

    * [`organizations.locations.discoveryConfigs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs)
    * [`projects.locations.discoveryConfigs`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs)
  * Connections

Connections are relevant only to [discovery for Cloud SQL](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#cloud-sql).

    * [`organizations.locations.connections`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections)
    * [`projects.locations.connections`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections)
  * Data profiles

    * [`organizations.locations.projectDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.projectDataProfiles)
    * [`projects.locations.projectDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.projectDataProfiles)
    * [`organizations.locations.fileStoreDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles)
    * [`projects.locations.fileStoreDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles)
    * [`organizations.locations.tableDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles)
    * [`projects.locations.tableDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles)
    * [`organizations.locations.columnDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles)
    * [`projects.locations.columnDataProfiles`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.columnDataProfiles)



## What's next

  * Read the how-to guides to get started with inspecting text and images for sensitive data, as well as redacting sensitive data from text and images: 
    * [Inspecting text for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-text)
    * [Inspecting structured text for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-structured-text)
    * [Inspecting images for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images)
    * [Redacting sensitive data from images](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images)
    * [De-identifying sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data)
  * For more information about inspecting storage and how to use actions, see [Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).
  * For more information about sensitive data discovery, see [Data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles)
  * Review [pricing](https://docs.cloud.google.com/sensitive-data-protection/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
