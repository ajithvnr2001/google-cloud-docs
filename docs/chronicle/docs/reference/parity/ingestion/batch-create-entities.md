---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-entities/
title: BatchCreateEntities to ImportEntities APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:32.783244+00:00
---

# BatchCreateEntities to ImportEntities APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BatchCreateEntities to ImportEntities APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API v2 (**`BatchCreateEntities`**) to the modern Chronicle API ([**`ImportEntities`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.entities/import)).

> [!IMPORTANT] The modern `ImportEntities` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized for the target instance resource.

## Protocol and mapping overview

Feature | Legacy API v2 (`BatchCreateEntities`) | Modern Chronicle API (`ImportEntities`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/entities.import`  
  
* * *

## Request payload field-by-field parity

In the legacy Ingestion API v2, callers sent entity batches using `BatchCreateEntitiesRequest`, placing `customer_id`, `log_type`, and `entities` directly at the top level of the request body. In the modern Chronicle API, entities are ingested through `ImportEntitiesRequest`, which scopes the request to the parent instance in the URL path and wraps the entity payload inside an `inline_source` structure.

Legacy field (`BatchCreateEntitiesRequest`) | Modern field (`ImportEntitiesRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_id` | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API v2, customer identification was passed using the `customer_id` request body field. In the modern API, the parent instance is explicitly specified in the request URL: `projects/{project}/locations/{location}/instances/{instance}`.  
— | `inline_source` | `EntitiesInlineSource` (oneof `source`) | **Encapsulation wrapper:** The modern API encapsulates ingested entities inside a `oneof source` container. Inlined entities are provided within `inline_source`.  
`log_type` | `inline_source.log_type` | `string` | **Parity mapped:** The log type identifying the source of the entity telemetry (for example, `OKTA`, `AZURE_AD`, or `ACTIVE_DIRECTORY`). In the modern API, this references a valid `chronicle.googleapis.com/LogType` resource.  
`entities` | `inline_source.entities` | `repeated Entity` | **Parity mapped with canonical resource naming:** Repeated list of entities to be ingested. The entity schema preserves full compatibility with the UDM Entity model (`metadata`, `entity` noun, `relations`, `additional`, `risk_score`, `metric`) while adding an optional canonical resource `name` attribute in the modern schema.  
  
* * *

### Entity structure parity (`backstory.Entity` versus `google.cloud.chronicle.v1main.Entity`)

The schema of each entity in `inline_source.entities` retains complete structural alignment with the legacy UDM entity format:

Entity field | Field type | Parity and migration notes  
---|---|---  
`name` | `string` | **New field:** Canonical resource name of the entity (`projects/{project}/locations/{location}/instances/{instance}/entities/{entity}`).  
`metadata` | `EntityMetadata` | **Direct mapping:** Contains entity metadata including `product_entity_id`, `collected_timestamp`, `creation_timestamp`, `interval`, `vendor_name`, `product_name`, `product_version`, `entity_type`, `feed`, and threat/IOC intelligence metadata.  
`entity` | `Noun` | **Direct mapping:** The primary UDM Noun representing the entity (such as `user`, `asset`, `resource`, `file`, `process`, `domain_name`, `url`, or `ip_address`).  
`relations` | `repeated Relation` | **Direct mapping:** Defines directed or bidirectional relationships between this entity and related entities (for example, `OWNS`, `ADMINISTERS`, `MEMBER`, `EXECUTES`, `DOWNLOADED_FROM`, or `CONTACTS`).  
`additional` | `google.protobuf.Struct` | **Direct mapping:** Dynamic structured JSON object for supplemental attributes that cannot be accommodated within standard UDM fields.  
`risk_score` | `EntityRisk` | **Direct mapping:** Contextual risk scoring details associated with the entity.  
`metric` | `Metric` | **Direct mapping:** Numerical and statistical metrics associated with the entity when `entity_type` is `METRIC`.  
  
* * *

## Response payload field-by-field parity

Both endpoints return an empty confirmation payload upon successful receipt of the entities.

Legacy field (`BatchCreateEntitiesResponse`) | Modern field (`ImportEntitiesResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation and queuing of the entity batch.  
  
* * *

## Key differences

  * **Resource-scoped URL vs. global endpoint:**
    * Legacy `BatchCreateEntities` sent requests to a global endpoint (`/v2/entities:batchCreate`), requiring callers to supply `customer_id` in the request body.
    * Modern `ImportEntities` adopts Google Cloud resource hierarchy standards, placing instance ownership directly in the URL path (`/v1/projects/{project}/locations/{location}/instances/{instance}/entities:import`).
  * **Payload encapsulation (`oneof source`):**
    * Legacy `BatchCreateEntitiesRequest` accepted `log_type` and `entities` directly at the root level of the payload.
    * Modern `ImportEntitiesRequest` wraps the entity batch in an `inline_source` structure (`EntitiesInlineSource`), standardizing the import contract across direct inline uploads and future asynchronous source ingestion.
  * **Modern IAM authorization:**
    * Authentication transitions from legacy Ingestion API keys and partner tokens to standard Google Cloud IAM bearer tokens with granular permission enforcement (`chronicle.googleapis.com/entities.import`).
  * **All-or-nothing batch validation:**
    * Both legacy v2 and modern APIs enforce atomic validation across the entire batch: all entities in the request must be valid for the call to succeed. A validation error in any single entity causes the entire import request to fail.
  * **Schema continuity:**
    * The internal schema of `Entity` remains fully consistent with the Universal Data Model (UDM) Entity definition, ensuring existing entity construction pipelines can migrate to the modern API with minimal transformation beyond payload wrapping.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
