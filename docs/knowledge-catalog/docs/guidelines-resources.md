---
url: https://docs.cloud.google.com/knowledge-catalog/docs/guidelines-resources/
title: Guidelines to name a Knowledge Catalog resource \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:31:45.180817+00:00
---

# Guidelines to name a Knowledge Catalog resource  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/guidelines-resources/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Guidelines to name a Knowledge Catalog resource Stay organized with collections  Save and categorize content based on your preferences. 

A Google Cloud resource is any component that you create or use within Google Cloud. These resources form the building blocks of your applications and systems running on the platform.

For more information on general Google Cloud resource naming, see [Resource names](https://google.aip.dev/122).

## Resource naming format

The following table lists the full resource name formats for Knowledge Catalog resources:

Resource | Full resource name format  
---|---  
[Entry group](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-groups) | `projects/{PROJECT_ID}/locations/{LOCATION}/entryGroups/{ENTRY_GROUP_ID}`  
[Entry](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entries) | `projects/{PROJECT_ID}/locations/{LOCATION}/entryGroups/{ENTRY_GROUP_ID}/entries/{ENTRY_ID}`  
[Entry type](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-types) | `projects/{PROJECT_ID}/locations/{LOCATION}/entryTypes/{ENTRY_TYPE_ID}`  
[Aspect type](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types) | `projects/{PROJECT_ID}/locations/{LOCATION}/aspectTypes/{ASPECT_TYPE_ID}`  
[Entry link](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#entry-links) | `projects/{PROJECT_ID}/locations/{LOCATION}/entryGroups/{ENTRY_GROUP_ID}/entryLinks/{ENTRY_LINK_ID}`  
[Metadata job](https://docs.cloud.google.com/knowledge-catalog/docs/import-metadata#components) | `projects/{PROJECT_ID}/locations/{LOCATION}/metadataJobs/{METADATA_JOB_ID}`  
[Metadata feed](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-change-feeds-overview#terminology) | `projects/{PROJECT_ID}/locations/{LOCATION}/metadataFeeds/{METADATA_FEED_ID}`  
[Glossary](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries#glossary) | `projects/{PROJECT_ID}/locations/{LOCATION}/glossaries/{GLOSSARY_ID}`  
[Glossary category](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries#category) | `projects/{PROJECT_ID}/locations/{LOCATION}/glossaries/{GLOSSARY_ID}/categories/{GLOSSARY_CATEGORY_ID}`  
[Glossary term](https://docs.cloud.google.com/knowledge-catalog/docs/manage-glossaries#term) | `projects/{PROJECT_ID}/locations/{LOCATION}/glossaries/{GLOSSARY_ID}/terms/{GLOSSARY_TERM_ID}`  
[Data product](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview) | `projects/{PROJECT_ID}/locations/{LOCATION}/dataProducts/{DATA_PRODUCT_ID}`  
[Data domain](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview) | `projects/{PROJECT_ID}/locations/{LOCATION}/dataDomains/{DATA_DOMAIN_ID}`  
[Lineage process](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-model-process) | `projects/{PROJECT_ID}/locations/{LOCATION}/processes/{PROCESS_ID}`  
[Lineage run](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-model-run) | `projects/{PROJECT_ID}/locations/{LOCATION}/processes/{PROCESS_ID}/runs/{RUN_ID}`  
[Lineage event](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage#lineage-model-event) | `projects/{PROJECT_ID}/locations/{LOCATION}/processes/{PROCESS_ID}/runs/{RUN_ID}/lineageEvents/{LINEAGE_EVENT_ID}`  
  
## Resource name components

The following sections provide a breakdown of each component.

### Project ID

The value must be the [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects), available from the Google Cloud console. For example, `my-cool-project` is a project ID, while `123456789123` is a project number.

### Location

The value must be one of the supported Knowledge Catalog locations. For a list of available locations, see [Knowledge Catalog locations](https://docs.cloud.google.com/knowledge-catalog/docs/locations).

### Resource ID

Resource paths contain unique identifier (`ID`) segments for each resource and its parent resources in the hierarchy. The following sections explain the naming guidelines and formatting requirements for each type of resource ID.

#### Standard resource IDs

Except for entry IDs and data lineage resource IDs, all resource ID variables, such as {ENTRY_GROUP_ID} and {GLOSSARY_ID}, must conform to the following guidelines:

  * Start with a lowercase letter.
  * Contain between 1 and 63 characters.
  * Contain only lowercase letters, numbers, hyphens, and underscores.
  * End with a number or a lowercase letter.



#### System entry groups

**Note:** System-defined entry groups start with an `@` symbol. For example, the `ENTRY_GROUP_ID` for an automatically ingested BigQuery resource is `@bigquery`. 

#### Entry IDs

The naming guidelines for an {ENTRY_ID} are different:

  * Contain up to 4000 characters.
  * Use an entry ID format based on the Google Cloud [full resource name](https://cloud.google.com/apis/design/resource_names#full_resource_name). The format is the full resource name of the resource without the prefix double slashes in the API service name part. This allows retrieval of entries using their associated resource name.

For example:

    * If the full resource name of a Looker instance is `//looker.googleapis.com/projects/my-project/locations/us-central1/instances/my-instance`, then the suggested {ENTRY_ID} is `looker.googleapis.com/projects/my-project/locations/us-central1/instances/my-instance`.



#### Data lineage resource IDs

Data lineage resources represent a hierarchy of data transformation operations:

  * **Process ID ({PROCESS_ID})**: Identifies the definition of a data transformation (such as a specific SQL query or ETL pipeline).
  * **Run ID ({RUN_ID})**: Identifies a single execution instance of a parent process.
  * **Lineage event ID ({LINEAGE_EVENT_ID})**: Identifies a discrete data movement event between sources and targets that occurred during a run.



When you create custom lineage resources through the API, the variables {PROCESS_ID}, {RUN_ID}, and {LINEAGE_EVENT_ID} must conform to the following guidelines:

  * Contain up to 200 characters.
  * Contain only letters (case-sensitive), numbers, hyphens, underscores, colons, and dots.



For automated lineage (such as BigQuery queries, Managed Service for Apache Spark, or OpenLineage ingestion), Knowledge Catalog generates these IDs automatically.

### BigQuery entry names

When you interact with BigQuery resources through the Knowledge Catalog APIs, you must use specific formatting for the entry group ID and entry ID.

  * **Entry group ID** : `@bigquery`
  * **Entry ID** : `bigquery.googleapis.com/projects/{PROJECT_ID}/datasets/{DATASET_ID}/tables/{TABLE_ID}`



#### Example

If your BigQuery table is `projects/test-project/datasets/test_dataset/tables/test_table`, the fully qualified Knowledge Catalog entry name is the following:

`projects/{PROJECT_ID}/locations/{LOCATION}/entryGroups/@bigquery/entries/bigquery.googleapis.com/projects/test-project/datasets/test_dataset/tables/test_table`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
