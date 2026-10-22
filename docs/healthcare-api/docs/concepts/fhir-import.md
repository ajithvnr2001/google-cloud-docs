---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-import/
title: FHIR import options \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:56.080900+00:00
---

# FHIR import options  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  FHIR import options Stay organized with collections  Save and categorize content based on your preferences. 

This page describes options for storing large batches of FHIR data in the Cloud Healthcare API.

**Tip:** If you're importing data from an external bulk FHIR server, consider using the Google open source [Bulk FHIR Tools](https://github.com/google/bulk_fhir_tools) to load data directly into the Cloud Healthcare API.

## Import FHIR resources

Use the [`fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method to load FHIR resources from Cloud Storage into the Cloud Healthcare API. The method performs best when loading data into an empty FHIR store without interference from other applications.

To call `fhirStores.import`, see [Importing and exporting FHIR resources using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export).

Consider the following properties of `fhirStores.import` method when deciding whether to use it. If `fhirStores.import` isn't suitable for your application, consider using the [`fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) method to load data. For information about how to call `fhir.executeBundle`, see [Managing FHIR resources using FHIR bundles](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles).

  * The `fhirStores.import` method accepts bundles larger than the [50 MB limit](https://docs.cloud.google.com/healthcare-api/quotas#resource_limits) on `fhir.executeBundle`. However, the size of each individual resource within the bundle is limited to [10 MB](https://docs.cloud.google.com/healthcare-api/quotas#resource_limits).
  * Using `fhirStores.import` removes the complexities of executing large FHIR bundles, such as the following:

    * Breaking up FHIR bundles into smaller bundles
    * Managing multiple bundle schedules
    * Managing transient errors that can be retried at the resource or bundle level

Often, these advantages outweigh the advantages from using bundles.

  * Each resource in the input must contain a client-supplied ID. Each resource is stored using the provided ID regardless of the [`enableUpdateCreate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.enable_update_create) setting on the FHIR store.

  * The import process doesn't enforce referential integrity, regardless of the [`disableReferentialIntegrity`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.disable_referential_integrity) setting on the FHIR store. Not enforcing referential integrity lets you import resources with arbitrary interdependencies without considering grouping or ordering. If the input data contains invalid references or if some resources fail to import, the state of the FHIR store might violate referential integrity.

  * If a resource with a given ID already exists in the store, the most recent version of the resource is overwritten without creating a new historical version. The overwriting occurs regardless of the [`disableResourceVersioning`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.disable_resource_versioning) setting on the FHIR store. If transient failures occur during the import, a successfully imported resource could be overwritten more than once.

  * The import operation is idempotent unless the input data contains multiple valid resources with the same ID but different contents. In that case, after the import completes, the store contains exactly one resource with each ID, but the duplicate entries could contain any version of the contents. For example, importing a million resources with the same ID writes only one resource to the store.

  * The operation result counters don't count duplicate IDs as an error. Each resource in the input counts as one success. This could result in a success count larger than the number of resources in the FHIR store. This often occurs when importing data organized in bundles produced by `Patient-everything` where each bundle contains its own copy of a resource, such as `Practitioner`, that might be referenced by many Patient resources.

  * If some resources fail to import, such as due to parsing errors, successfully imported resources aren't rolled back. For example, if 5 of 100 resources fail to import, the remaining 95 resources are imported into the FHIR store.

  * When using the `BUNDLE` format, the import method rejects bundles with `Bundle.type` of `history`. The import method doesn't apply the bundle processing semantics for batch or transaction bundles. Unlike in `fhir.executeBundle`, transaction bundles aren't executed as a single transaction and bundle-internal references aren't rewritten. The bundle is treated as a collection of resources to be written as provided in `Bundle.entry.resource`, ignoring `Bundle.entry.request`. For example, this allows the import of searchset bundles produced by a FHIR search or `Patient-everything` operation.




## Use FHIR bundles

See [FHIR bundles](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles#fhir_bundles) for an overview of FHIR bundles.

### When to use FHIR bundles

Consider the following characteristics and advantages of using the `fhir.executeBundle` method when deciding whether to use it to store FHIR resources:

  * If it is too costly, either in terms of billing costs or network bandwidth, to build a pipeline that stores data in Cloud Storage and then imports the data using `fhirStores.import`, use `fhir.executeBundle`.
  * When executing bundles, transaction integrity can be enforced.
  * When executing bundles, FHIR profile validation can be enforced.
  * If you need to send [Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) when FHIR create, update, or delete operations occur, use `fhir.executeBundle`. Pub/Sub notifications are not sent when FHIR resources are imported using `fhirStores.import`.
  * If the time at which a particular FHIR resource must be processed is in in seconds or minutes, use `fhir.executeBundle`. If the time at which a particular FHIR resource must be processed is in hours or days, use `fhirStores.import`.
  * If your Google Cloud project has many existing long-running operations (LRO) performing other tasks, you might see better performance with `fhir.executeBundle` over `fhirStores.import`.
  * If the application managing the `fhirStores.import` operation doesn't have a good strategy for the following, use `fhir.executeBundle`:

    * Handling bulk errors
    * Addressing failures on a subset of FHIR resources or entire batches



### When not to use FHIR bundles

Consider the following limitations of `fhir.executeBundle` when determining whether to use it to store FHIR resources:

  * Bundles have the equivalent quota and billing applied to the operations inside the bundle as if the operations were executed outside of the bundle. For example, if a bundle has 10 `POST` operations, 5 `GET` operations, and 1 `DELETE` operation, the quota and billing applied to the bundle is the same as if those operations were executed independently.

As a result, aiming to lower quota limits and FHIR operation costs are not reasons to use bundles instead of `fhirStores.import`.

  * Large transaction bundles might be more likely to have transaction conflicts which leads to data contention and failed operations. For information on how these issues can occur, and how to resolve them, see [Prevent `429 Resource Exhausted operation_too_costly` errors](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#prevent-429).

  * You can achieve and maintain high data throughput using batch bundles, which helps you to avoid data contention. However, batch bundles do not have transactional consistency capabilities, such as [referential integrity](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-referential-integrity)

  * If a bundle is large, even if it's a batch bundle, you might see reduced data throughput. For more information, see [Avoid large transaction bundles](https://docs.cloud.google.com/healthcare-api/docs/best-practices-data-throughput#avoid-large).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
