---
url: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access/
title: Troubleshoot SAP BDC access \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:02.489183+00:00
---

# Troubleshoot SAP BDC access  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/troubleshoot-sap-bdc-access/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Troubleshoot SAP BDC access Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to resolve common issues when you integrate SAP Business Data Cloud (BDC) with BigQuery. For the SAP to Google Cloud (Federation) workflow, see the [Lakehouse troubleshooting page](https://docs.cloud.google.com/lakehouse/docs/troubleshoot-cross-cloud-data-access).

## `NOT_FOUND` or `PERMISSION_DENIED` errors when querying tables

This issue occurs when access is revoked on the SAP BDC side. Queries to the affected tables fail and return a "not found" or "permission denied" error originating from the Delta Sharing endpoint.

To resolve this issue, work with your SAP administrator to restore access to the tables. For more information about access management in SAP, see [Working with Data Products in SAP Business Data Cloud Connect](https://help.sap.com/docs/business-data-cloud/sap-business-data-cloud-connect/working-with-data-products-in-sap-business-data-cloud-connect?locale=en-US&version=LATEST) in the SAP documentation.

## Cannot write data to SAP BDC tables

This issue occurs when you attempt to write or modify data in your SAP BDC tables from BigQuery. This integration provides read-only access to SAP BDC data.

To resolve this issue, modify the data directly in SAP BDC.

## Unexpected pricing charges for Delta Sharing API calls

This issue can occur if your Lakehouse catalog synchronizes too frequently with SAP BDC, which calls Delta Sharing APIs to list tables and get table metadata. Those API calls are charged as Lakehouse Class A operations.

To resolve this issue, increase the catalog's refresh interval to reduce the frequency of API calls. For more information about pricing, see [Lakehouse pricing](https://cloud.google.com/products/biglake/pricing).

## SAP cannot find or query published tables

This issue can occur if the Apache Iceberg metadata required by SAP BDC has not been generated correctly in your Cloud Storage bucket.

To resolve this issue, verify that the expected metadata files exist at the storage path backing your table:

  1. List the contents of the `metadata` folder for your table:
         
         gcloud storage ls "gs://BUCKET_NAME/NAMESPACE_NAME/TABLE_NAME/metadata/"

  2. Verify the output contains standard Apache Iceberg metadata files, including:

     * `version-hint.txt`
     * `v*.metadata.json`
     * Manifest files (`.avro`). If these files are missing, check your Iceberg REST catalog configuration or write operations in BigQuery to ensure data and metadata are being successfully materialized to the storage bucket.



## Table publishing fails with missing primary key or nullable field error

This issue occurs when you publish an Apache Iceberg Catalog or a Data Product to SAP BDC, but the tables within the catalog or data product do not have a primary key defined in its Iceberg metadata, or one of the primary key columns is defined as nullable (`required: false`).

When this occurs, publishing fails with one of the following errors:

  * `INVALID_ARGUMENT: Failed to generate Core Schema Notation (CSN) payload: Table 'TABLE_NAME' must have a primary key constraint to be published to SAP.`
  * `INVALID_ARGUMENT: Field COLUMN_NAME is not required, but is referenced in the identifier-field-ids property.`



SAP BDC requires all published tables to define primary key constraints using `identifier-field-ids` in the Iceberg metadata. In accordance with the Apache Iceberg specification, all columns designated in `identifier-field-ids` must also be configured as non-nullable (`required: true`).

To resolve this issue, perform an atomic schema update using the BigLake Iceberg REST API to mark the primary key columns as `required: true` and specify their field IDs in `identifier-field-ids`:

  1. Obtain an access token for authorization:
         
         TOKEN=$(gcloud auth application-default print-access-token)

  2. Send an Iceberg REST schema update commit using Python:
         
         import requests
         
         headers = {
             "Authorization": f"Bearer {TOKEN}",
             "x-goog-user-project": "PROJECT_ID",
             "X-Iceberg-Access-Delegation": "vended-credentials",
             "Content-Type": "application/json",
         }
         url = "https://biglake.googleapis.com/iceberg/v1/restcatalog/v1/projects/PROJECT_ID/catalogs/ICEBERG_CATALOG_ID/namespaces/NAMESPACE_NAME/tables/TABLE_NAME"
         
         # 1. Fetch current metadata
         meta = requests.get(url, headers=headers).json()["metadata"]
         schema = meta["schemas"][0].copy()
         schema["fields"] = [f.copy() for f in schema["fields"]]
         
         # 2. Mark primary key column as required (non-nullable) and set identifier-field-ids
         for f in schema["fields"]:
           if f["name"] == "PRIMARY_KEY_COLUMN_NAME":
             f["required"] = True
         schema["identifier-field-ids"] = [PRIMARY_KEY_FIELD_ID]
         schema["schema-id"] = meta.get("last-schema-id", 0) + 1
         
         # 3. Commit the updated schema
         update_payload = {
             "requirements": [{"type": "assert-table-uuid", "uuid": meta["table-uuid"]}],
             "updates": [
                 {
                     "action": "add-schema",
                     "schema": schema,
                     "last-column-id": meta.get("last-column-id", 0),
                 },
                 {"action": "set-current-schema", "schema-id": -1},
             ],
         }
         response = requests.post(url, headers=headers, json=update_payload)
         response.raise_for_status()

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `ICEBERG_CATALOG_ID`: your Iceberg REST catalog ID.
     * `NAMESPACE_NAME`: your Iceberg namespace name.
     * `TABLE_NAME`: your Iceberg table name.
     * `PRIMARY_KEY_COLUMN_NAME`: the name of the column to set as the primary key.
     * `PRIMARY_KEY_FIELD_ID`: the integer field ID of the primary key column (for example, `1`).



## Queries on SAP fail with permission or not found errors

This issue can occur if access is revoked or permissions are modified in BigQuery after a catalog or Data Product has been published to SAP BDC. Queries to the affected tables will fail on the SAP side, typically with a "not found" or "permission denied" error originating from BigQuery.

To resolve this issue, verify that the Workload Identity Federation principal retains the required roles (like **BigLake Viewer**) and that standard BigQuery dataset or table access is granted. For more information about installing and consuming Data Products in SAP, see [Installing Data Products](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/ea7cb802cbea47b39a441888873c3a49.html?locale=en-US&version=LATEST) in the SAP documentation.

## New tables or metadata changes are not appearing in SAP BDC

This issue can occur when you add new tables or update existing table metadata in your Apache Iceberg REST catalog or Knowledge Catalog Data Product, but the changes are not visible to SAP consumers. While the underlying data remains fresh, metadata updates might require explicit action.

To resolve this issue, execute a new publish action (`gcloud biglake data-product-sharing publish`) for the catalog or Data Product to make the new metadata discoverable in SAP BDC.

## Unable to write data from SAP back to BigQuery

This issue occurs when you attempt to use the published SAP integration to write or modify data in BigQuery from SAP BDC. This integration provides read-only access to BigQuery data from SAP BDC to prevent accidental overwriting of data or security violations.

To resolve this issue, manipulate and write your source data directly using BigQuery or standard Google Cloud pipelines.

## `RESOURCES_NOT_IN_SAME_SERVICE_PERIMETER` errors when querying tables

This issue can occur if your environment has VPC Service Controls enforced, and the perimeter applied on the project restricts the `storage.googleapis.com` service. Because Dremel needs to read the incoming Cloud Storage buckets in the SAP project when querying tables, the request is prohibited since the SAP project is outside your perimeter.

To resolve this issue, configure a VPC Service Controls egress rule. For more information about configuration, see [VPC Service Controls configuration for SAP BDC](https://docs.cloud.google.com/lakehouse/docs/vpc-sc-config-sap-bdc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
