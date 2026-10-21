---
url: https://docs.cloud.google.com/knowledge-catalog/docs/locations/
title: Knowledge Catalog locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:11:19.113122+00:00
---

# Knowledge Catalog locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/locations/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Resources ](https://docs.cloud.google.com/knowledge-catalog/docs/resources)



Send feedback 

#  Knowledge Catalog locations Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Knowledge Catalog (formerly Dataplex Universal Catalog) resource, such as an [entry group](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-groups), [entry type](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#entry-types), [aspect type](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspect-types), or [data scan](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview), you select the location where its metadata is stored and accessed. Choosing the right location is critical for data residency compliance, performance, and resource reuse.

### Why location is important

Choosing the appropriate location for your Knowledge Catalog resources is important for the following reasons:

  * **Data residency and compliance:** If your organization is subject to strict data residency (DRZ) regulations, you must store metadata and resource definitions in specific geographic domains or regions to comply with localized policies.

  * **Latency and availability:** Selecting a region close to your primary data sources (such as BigQuery datasets or Cloud Storage buckets) and your end users reduces lookup latency and improves metadata ingestion reliability.

  * **Resource reuse:** Deciding whether a resource is local to a region or shared globally affects how you can reuse metadata templates across different locations.




### Guidelines for choosing locations

Resources in Knowledge Catalog can be created in a **regional** location (such as `us-central1` or `europe-west3`), a **multi-region** location (such as `us` or `eu`), or the **global** location.

#### Regional locations

A regional location restricts the resource definition and its metadata storage to that specific region:

  * **Benefits:** Provides strict data residency compliance (DRZ). Technical metadata for regional Google Cloud sources (such as BigQuery or Cloud Storage) is automatically harvested and stored within the same physical region.

  * **Limitations:** Regional types (such as custom entry types or aspect types) can only be applied to entry groups and entries within the exact same region. They can't be shared or reused across multiple regions.




#### Multi-region locations

A multi-region location encompasses multiple physical regions within a geographic area (such as `us` or `eu`):

  * **Benefits:** Allows metadata for entry groups and entries to span multiple physical regions within the geographic domain.

  * **Limitations:** DataScans (such as data quality and data profiling scans) aren't supported in multi-region locations. You must create DataScans in a regional location.




#### Global location

The `global` location is a virtual location where metadata definitions are replicated across Google Cloud regions globally:

  * **Benefits:** Promotes maximum reusability. A `global` aspect type or entry type can be applied to entries located in any region. It's ideal for defining unified corporate metadata standards without duplicating templates in separate regions.

  * **Limitations:** Doesn't guarantee that metadata remains in a single geographic jurisdiction, which might violate strict data residency compliance requirements.




### Constraints and limitations

When organizing your metadata, keep the following constraints in mind:

  * **Immutable location:** You can't modify the location of a resource (such as an entry group, entry type, or aspect type) after it is created.

  * **Location compatibility checks:** For more details on compatibility, see [Project and location constraints](https://docs.cloud.google.com/knowledge-catalog/docs/metadata-overview#project-location-constraints).

    * The location of an entry must match the location of its associated entry group and entry type—or the entry type must be `global`.

    * An aspect added to an entry or entry link must be based on an aspect type in the same location, or the aspect type must be `global`.

    * An entry type or entry link type must be composed of aspect types stored in the same location as the entry type, or the aspect types must be `global`.




## Regions

The following table lists the regions where Knowledge Catalog is available. Regions are added regularly. For updates, check the [Knowledge Catalog release notes](https://docs.cloud.google.com/knowledge-catalog/docs/release-notes).

Region name | Region description | Data lineage available  
---|---|---  
`asia-east1` | Taiwan | Yes  
`asia-east2` | Hong Kong | Yes  
`asia-northeast1` | Tokyo | Yes  
`asia-northeast2` | Osaka | Yes  
`asia-northeast3` | Seoul | Yes  
`asia-south1` | Mumbai | Yes  
`asia-south2` | Delhi | Yes  
`asia-southeast1` | Singapore | Yes  
`asia-southeast2` | Jakarta | Yes  
`africa-south1` | Johannesburg | Yes  
`australia-southeast1` | Sydney | Yes  
`australia-southeast2` | Melbourne | Yes  
`eu` | Multiple regions in European Union | Yes  
`europe-central2` | Warsaw | Yes  
`europe-north1` | Finland | Yes  
`europe-north2` | Stockholm | Yes  
`europe-southwest1` | Madrid | Yes  
`europe-west1` | Belgium | Yes  
`europe-west2` | London | Yes  
`europe-west3` | Frankfurt | Yes  
`europe-west4` | Netherlands | Yes  
`europe-west6` | Zurich | Yes  
`europe-west8` | Milan | Yes  
`europe-west9` | Paris | Yes  
`europe-west10` | Berlin | Yes  
`europe-west12` | Turin | Yes  
`me-central1` | Doha | Yes  
`me-central2` | Dammam | Yes  
`me-west1` | Tel Aviv | Yes  
`northamerica-northeast1` | Montreal | Yes  
`northamerica-northeast2` | Toronto | Yes  
`northamerica-south1` | Mexico | Yes  
`southamerica-east1` | Sao Paulo | Yes  
`southamerica-west1` | Santiago | Yes  
`us` | Multiple regions in United States | Yes  
`us-central1` | Iowa | Yes  
`us-east1` | South Carolina | Yes  
`us-east4` | Northern Virginia | Yes  
`us-east5` | Columbus | Yes  
`us-south1` | Dallas | Yes  
`us-west1` | Oregon | Yes  
`us-west2` | Los Angeles | Yes  
`us-west3` | Salt Lake City | Yes  
`us-west4` | Las Vegas | Yes  
  
### BigQuery Omni regions for data lineage

Data lineage is available in the following [BigQuery Omni regions](https://docs.cloud.google.com/bigquery/docs/omni-introduction):

Region name | Region description  
---|---  
`aws-ap-northeast-2` | AWS - Asia Pacific (Seoul)  
`aws-ap-southeast-2` | AWS - Asia Pacific (Sydney)  
`aws-eu-central-1` | AWS - Europe (Frankfurt)  
`aws-eu-west-1` | AWS - Europe (Ireland)  
`aws-us-east-1` | AWS - US East (N. Virginia)  
`aws-us-west-2` | AWS - US West (Oregon)  
`azure-eastus2` | Azure - East US 2  
  
## What's next

  * Learn more about [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions) in Google Cloud.
  * See the full list of [Google Cloud locations](https://cloud.google.com/about/locations/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
