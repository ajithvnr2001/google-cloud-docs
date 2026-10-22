---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-referential-integrity/
title: FHIR referential integrity \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:33.175918+00:00
---

# FHIR referential integrity  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-referential-integrity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  FHIR referential integrity Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the concept of referential integrity as it relates to resources within a FHIR store in the Cloud Healthcare API.

The FHIR store enforces referential integrity on references to other resources within the same store:

  * When creating, updating, or patching a resource, the operation will fail if the resulting content of the resource contains a reference to a resource or resource version that does not exist.
  * When deleting a resource, the operation will fail if there are other resources in the store that reference that resource.



Referential integrity can be disabled by setting the [`disableReferentialIntegrity`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.disable_referential_integrity) option at the time of store creation.

## Exclusions and limitations

The FHIR specification allows various forms of [references](http://hl7.org/fhir/references.html), some of which are not covered by referential integrity:

  * An external reference specified by a URL that does not match the base URL of the FHIR store.
  * A logical reference specified by a business identifier.
  * A reference containing only a human-readable display string.
  * References inside FHIR [extensions](http://hl7.org/fhir/extensibility.html) are only subject to referential integrity if [`complexDataTypeReferenceParsing`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#ComplexDataTypeReferenceParsing) is set to `ENABLED`. This is the default value for new FHIR stores.



Certain API methods can cause referential integrity to be violated under some conditions:

  * FHIR allows references to point to a specific history version of a resource using the form `[resource type]/[resource ID]/_history/[version ID]`. Referential integrity is applied to these references when created or updated, but when using the [`Resource-purge`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-purge) method to remove historical versions of a resource, incoming references are **not** checked.
  * The FHIR [`import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method does not enforce referential integrity. The method may be used either in cases where referential integrity is not required, or where the input is known to satisfy referential integrity. In the latter case, the references inside the FHIR store will reach eventual consistency after every resource is successfully imported.
  * The [`deidentify`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/deidentify) method can potentially create a FHIR store in a state that does not satisfy referential integrity temporarily during the operation, or permanently if filters are used to select a subset of resources.



A state where integrity is being enforced but has been violated by one of the previous cases will cause resource updates to be rejected on a resource that contains an invalid reference, unless the update fixes or removes all invalid references. Such a state might also create difficulties for applications using the store that assume integrity.

## Contained resources

The FHIR specification contains a constraint that every [contained resource](http://hl7.org/fhir/references.html#contained) must be referenced from somewhere within its containing resource (including references from other contained resources), and every reference to a contained resource must be valid. This constraint is enforced separately from referential integrity and cannot be disabled as it is defined in the FHIRPath invariants on each individual resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
