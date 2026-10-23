---
url: https://docs.cloud.google.com/knowledge-catalog/docs/dbt-transfer/
title: Import metadata from dbt Core \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:00.755997+00:00
---

# Import metadata from dbt Core  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/dbt-transfer/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Import metadata from dbt Core Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you import operational, semantic, and lineage metadata from dbt Core, dbt Cloud, and MetricFlow by using the Google Cloud CLI and your dbt artifact files. Instead of leaving transformation metadata siloed in the dbt ecosystem, you can centralize it to help data engineers, analytics engineers, and data stewards discover and govern enterprise data.

## Imported metadata and use cases

Because dbt Core operates as a transformation engine rather than a storage system like Oracle or PostgreSQL, importing its metadata supports different use cases. You import Oracle or PostgreSQL metadata to answer "What raw data do we have?", and you import dbt Core metadata to answer "How is our data transformed, is it reliable, and what does it mean to the business?"

When you run the dbt integration, you capture the following metadata:

  * **Technical metadata** : discover enterprise data by exploring key resources (sources, seeds, models) and their technical properties (column names, data types, row counts).
  * **Business and semantic metadata** : provide context for BI tools and AI agents by exploring business definitions and logic powered by dbt MetricFlow, such as semantic models, metrics, and saved queries.
  * **Operational and data quality metadata** : monitor pipeline health and troubleshoot data issues by exploring execution metadata such as timing, success or failure status, data freshness, and test results.
  * **Lineage and relationship metadata** : perform downstream impact analysis and root-cause tracing by exploring transformation graphs (DAGs) and dependencies between dbt resources, physical lineage that tracks and links physical transformation blocks, join keys and dynamic joins, and parent-child relationships.
  * **Consumption metadata** : troubleshoot issues with how downstream applications consume transformed data by exploring metadata captured in exposures that map how data is used outside of dbt.



## Limitations

  * Supports dbt Core v1 (validated against versions 1.11 and 1.12), dbt Core v2, and dbt Fusion.
  * gcloud CLI version 586.0.0 and later support the dbt and Knowledge Catalog integration. To install or update the CLI, see [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * There is no direct connection to dbt Cloud. To import metadata from a dbt Cloud job, get the job's artifacts first. See Import metadata from dbt Cloud runs.
  * Very large or deeply nested schemas are truncated: a single aspect can't exceed the per-aspect size cap, so deeply nested schemas might lose trailing fields.
  * `--aspects-only` can add and refresh metadata, but can't remove it. Deleting a dbt resource requires a full run.
  * This integration supports only dbt lineage events on BigQuery resources in the [Data Lineage API](https://docs.cloud.google.com/knowledge-catalog/docs/about-data-lineage) and graph. dbt entries (sources, seeds, models) for external third-party sources aren't captured in data lineage. 
    * To ingest all dbt lineage events in Data Lineage API, [use the OpenLineage dbt integration](https://pypi.org/project/openlineage-dbt/). Then, integrate OpenLineage with [Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/open-lineage) to import and visualize data lineage from dbt.



## Before you begin

Before you can import metadata from dbt Core and MetricFlow, complete the following tasks:

  1. Grant the required roles and permissions.
  2. Enable the Dataplex API.
  3. Meet the dbt prerequisites.
  4. Create the destination [entry group](https://docs.cloud.google.com/knowledge-catalog/docs/ingest-custom-sources#create-entry-group) if it does not already exist.
  5. Understand the Cloud Storage roles.



### IAM roles and permissions

To create and manage a Knowledge Catalog connector job, you need Identity and Access Management (IAM) roles that grant permissions for Knowledge Catalog and Cloud Storage.

To get the permissions that you need to configure a dbt connector, ask your administrator to grant you the following IAM roles:

  * To create and manage entry groups and entry links: [Dataplex Catalog Admin](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`), [Dataplex Catalog Editor](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`), or [Dataplex Entry Group Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`) on the project.
  * To execute the dbt `gcloud` command and create metadata import jobs: Follow the principle of least privilege and grant the following roles:

    * [Dataplex Metadata Job Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`) on the project.
    * [Dataplex Entry Group Importer](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupImporter) (`roles/dataplex.entryGroupImporter`) on the target entry group or the project. If you also import entry links, grant [Dataplex Entry Group Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryGroupOwner) (`roles/dataplex.entryGroupOwner`) on the project instead. Also grant [Dataplex Entry Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.entryOwner) (`roles/dataplex.entryOwner`) on each project that holds the BigQuery tables your dbt models write to. For custom roles, the entry link permissions are `dataplex.entryGroups.useReferenceEntryLink`, `dataplex.entryGroups.useSchemaJoinEntryLink`, and `dataplex.entryLinks.reference`.

Alternatively, you can grant the [Dataplex Catalog Admin](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.catalogAdmin) (`roles/dataplex.catalogAdmin`) role and the [Dataplex Metadata Job Owner](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles#dataplex.metadataJobOwner) (`roles/dataplex.metadataJobOwner`) role on the project.

  * To upload transformed metadata to the output staging bucket (`--storage-uri`): [Storage Object Creator](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectCreator) (`roles/storage.objectCreator`) or [Storage Object Admin](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectAdmin) (`roles/storage.objectAdmin`) on the staging bucket.

  * To read dbt artifacts from an input Cloud Storage bucket (`--artifacts-path`, if using Cloud Storage): [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectViewer) (`roles/storage.objectViewer`) or [Storage Object Admin](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectAdmin) (`roles/storage.objectAdmin`) on the input artifacts bucket. If you have the Storage Object Admin role, the Storage Object Viewer role is not required.

  * To view dbt metadata: [Dataplex Catalog Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) on the project.

  * To view logs in Cloud Logging: [Logs Viewer](https://docs.cloud.google.com/iam/docs/understanding-roles#logging.viewer) (`roles/logging.viewer`) on the project.




If you have the necessary permissions to manage IAM access in your project, you can grant these roles to your own user account by running the following `gcloud` commands:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_EMAIL" \
        --role="roles/dataplex.metadataJobOwner"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="user:USER_EMAIL" \
        --role="roles/dataplex.entryGroupOwner"
    
    gcloud storage buckets add-iam-policy-binding gs://STAGING_BUCKET \
        --member="user:USER_EMAIL" \
        --role="roles/storage.objectCreator"
    

If you run the import using a service account, such as in an automated CI/CD pipeline, you can grant these roles to the service account by running the following `gcloud` commands:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role="roles/dataplex.metadataJobOwner"
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role="roles/dataplex.entryGroupOwner"
    
    gcloud storage buckets add-iam-policy-binding gs://STAGING_BUCKET \
        --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
        --role="roles/storage.objectCreator"
    

Additionally, you must grant the Knowledge Catalog service agent (`service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com`) the [Storage Object Viewer](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#storage.objectViewer) (`roles/storage.objectViewer`) role on the output staging Cloud Storage bucket (`--storage-uri`) so that the import job can read the staged metadata file:
    
    
    gcloud storage buckets add-iam-policy-binding gs://STAGING_BUCKET \
        --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-dataplex.iam.gserviceaccount.com" \
        --role="roles/storage.objectViewer"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `USER_EMAIL`: your user account email address.
  * `SERVICE_ACCOUNT_EMAIL`: your service account email address.
  * `STAGING_BUCKET`: the name of your output staging Cloud Storage bucket (`--storage-uri`).
  * `PROJECT_NUMBER`: your Google Cloud project number.



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Enable APIs

Enable the Dataplex API.

[Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=dataplex.googleapis.com)

### dbt prerequisites

To import the full set of dbt metadata, we recommend producing all four dbt JSON artifact files. Only `manifest.json` is required; the others enrich the import and the transform degrades gracefully without them:

  * [`manifest.json`](https://docs.getdbt.com/reference/artifacts/manifest-json?version=1.12) (required): Core project structure and execution graph. Also carries the MetricFlow semantic models, metrics, and saved queries.
  * [`catalog.json`](https://docs.getdbt.com/reference/artifacts/catalog-json?version=1.12): Column names and data types. Without `catalog.json`, the schema aspect is imported with untyped columns.
  * [`run_results.json`](https://docs.getdbt.com/reference/artifacts/run-results-json?version=1.12): Test outcomes and execution metadata.
  * [`sources.json`](https://docs.getdbt.com/reference/artifacts/sources-json?version=1.12): Source freshness.



In your local terminal, Cloud Shell, or automated CI/CD environment where dbt is installed, go to the dbt project root directory and execute the following dbt commands in order against a single profile and target to generate the full set of dbt metadata artifact JSON files:

  * **For dbt Core 2.x and dbt Fusion** :

    1. `dbt source freshness`
    2. `dbt build`
    3. `dbt parse --write-catalog`

**Warning:** Don't use `dbt docs generate` on dbt Core 2.x or dbt Fusion. It doesn't write `catalog.json`, and it overwrites `run_results.json` without any test results. `dbt build --write-catalog` doesn't write a catalog either, so use a separate `dbt parse --write-catalog` step.
  * **For dbt Core 1.x** (where `dbt parse` doesn't write a catalog):

    1. `dbt source freshness`
    2. `dbt build`
    3. `dbt docs generate --no-compile`

**Warning:** Without `--no-compile`, `dbt docs generate` overwrites `run_results.json` with a `success` status for every node. Test results from the preceding `dbt build` are lost and the catalog reports every data quality test as passing.

**Note:** When chaining these commands in a shell script, separate them with `;` rather than `&&` (for example, `dbt source freshness; dbt build; dbt parse --write-catalog`). `dbt build` exits with a non-zero status code when a test fails, and runs with failing tests still produce test verdicts that should be imported.

### Understand Cloud Storage roles

Importing dbt metadata involves two distinct Cloud Storage locations that serve different purposes and shouldn't be conflated:

  * **Input (dbt source artifacts)** : Where your generated dbt JSON files reside. This can be a local directory path on your machine or CI runner (such as `./target/` or `.`) or an input Cloud Storage bucket URI prefix (such as `gs://my-dbt-artifacts-bucket/target/`). You provide this path using the `--artifacts-path` flag. The `gcloud` command reads these input files during job preparation. The caller executing the `gcloud` command needs read access (`roles/storage.objectViewer` or `roles/storage.objectAdmin`) if using Cloud Storage. The Knowledge Catalog service agent does not need access to the input artifacts bucket.
  * **Output (Knowledge Catalog import staging bucket)** : A Cloud Storage bucket URI prefix (such as `gs://my-staging-bucket/dbt-imports/`) where the `gcloud` command uploads the transformed metadata import file (`dbt_metadata.jsonl`), and from which the Knowledge Catalog import job reads during ingestion. You provide this URI using the `--storage-uri` flag. The caller executing the `gcloud` command needs write access (`roles/storage.objectCreator` or `roles/storage.objectAdmin`) to upload the file, and the Knowledge Catalog service agent needs read access (`roles/storage.objectViewer`) to import it.



## Import metadata from dbt Cloud runs

Knowledge Catalog doesn't connect to dbt Cloud directly. Because a dbt Cloud job generates the same artifact files as dbt Core, you can import metadata from dbt Cloud by retrieving those artifact files to a local directory or an input Cloud Storage bucket and running the `gcloud` command.

Before retrieving the artifacts, configure the dbt Cloud job to generate the complete artifact set. You can then retrieve the artifact files from a dbt Cloud job run using one of the following methods:

  * Download artifacts from the dbt Cloud console: manually download the artifact files from the job run details page in the dbt Cloud user interface for one-time imports or initial testing.
  * Download artifacts using the dbt platform CLI: execute dbt commands on dbt Cloud from your local terminal to automatically save the generated artifacts to your local project directory during development.
  * Download artifacts using the dbt Administrative API: programmatically retrieve artifacts from completed runs over HTTP for automated, scheduled pipelines.



### Set up the dbt Cloud job

In the dbt Google Cloud console, configure your job settings to generate the complete set of metadata artifacts:

  1. In the **Execution settings** section, select **Run source freshness**. dbt Cloud runs `dbt source freshness` before the job commands to generate `sources.json`.
  2. In the **Commands** section, add `dbt build`.
  3. Add a command to generate `catalog.json` based on your release track: 
     * **For dbt Core 2.x and dbt Fusion release tracks** : add `dbt parse --write-catalog` as a job command.
     * **For dbt Core 1.x release tracks** : add `dbt docs generate --no-compile` as a job command instead of selecting the **Generate docs on run** option. The **Generate docs on run** checkbox runs `dbt docs generate` without `--no-compile`, which overwrites the test results from `dbt build`, as described in dbt prerequisites. Note that if a command step fails, the job also fails, whereas the checkbox step doesn't fail the job.



If `dbt build` fails, for example because a test fails, dbt Cloud skips the commands after it and the run has no `catalog.json`. To always produce one, add the catalog command before `dbt build`. The catalog then describes the tables as they were before the build.

For more information, see [Job commands](https://docs.getdbt.com/docs/deploy/job-commands) and [Release tracks](https://docs.getdbt.com/docs/dbt-versions/dbt-release-tracks) in the dbt documentation.

### Download artifacts from the dbt Google Cloud console

To manually download artifacts from a completed run in the dbt Google Cloud console:

  1. In the dbt Google Cloud console, open the completed job run.
  2. Go to the **Artifacts** tab to view the generated artifact files.
  3. Download `manifest.json`, `catalog.json`, `run_results.json`, and `sources.json` to a local directory.
  4. In your local terminal or Cloud Shell, run the `gcloud` import command described in Configure dbt connectivity and set `--artifacts-path` to the directory containing the downloaded files.



For more information, see [Run visibility](https://docs.getdbt.com/docs/deploy/run-visibility#artifacts-tab) in the dbt documentation.

### Download artifacts using the dbt platform CLI

The dbt platform CLI (formerly the dbt Cloud CLI) executes dbt commands on the dbt Cloud platform from your local terminal and automatically downloads the generated artifacts into the `target/` directory of your local dbt project.

  1. In your local terminal, go to your dbt project root directory and run the three commands listed in dbt prerequisites.
  2. Run the `gcloud` import command described in Configure dbt connectivity and set `--artifacts-path` to the project root or the `target/` directory.



The CLI runs within your development environment using your personal data warehouse credentials, so the generated metadata reflects your development schema rather than production tables built by a scheduled job. Use the CLI for testing or development workflows, and use a deployment job for scheduled production imports.

For more information, see [Install the dbt platform CLI](https://docs.getdbt.com/docs/platform/dbt-cli-installation) in the dbt documentation.

### Download artifacts using the dbt Administrative API

You can use the dbt Administrative API to programmatically retrieve artifacts from any completed job run. The `List Run Artifacts` endpoint returns the file paths generated by a run, and the `Retrieve Run Artifact` endpoint downloads a specific artifact file from the following URL:

`https://ACCESS_URL/api/v2/accounts/ACCOUNT_ID/runs/RUN_ID/artifacts/FILE`

`ACCESS_URL` depends on the region that hosts your dbt Cloud account. Authenticate requests using a dbt Cloud service token. For more information, see the following pages in the dbt documentation:

  * [dbt Administrative API](https://docs.getdbt.com/docs/dbt-apis/admin-api)
  * [Access, Regions, & IP addresses](https://docs.getdbt.com/docs/platform/about-platform/access-regions-ip-addresses)
  * [Service account tokens](https://docs.getdbt.com/docs/dbt-apis/service-tokens)



From your local terminal, Cloud Shell, or automated workflow environment, download `manifest.json`, `catalog.json`, `run_results.json`, and `sources.json` to a local directory or a Cloud Storage bucket, and then run the `gcloud` command described in Configure dbt connectivity against that path.

By default, the artifact endpoint returns artifacts from the final step of the run unless you specify the `step` query parameter. When you configure the job as described in Set up the dbt Cloud job, the final step is `dbt parse --write-catalog` or `dbt docs generate --no-compile`, which only writes `catalog.json` and leaves the other three artifacts intact at the default step.

**Note:** If your job's final command overwrites `run_results.json`, pass the `step` query parameter to request `run_results.json` from the step that ran `dbt build` so that test results are preserved.

#### Retrieve the run ID

To download the artifacts of a specific run, you need its run ID. You can copy the run ID from the run URL in the dbt Google Cloud console, or query the API from your terminal or workflow script for the most recent successful run of a job:

`GET https://ACCESS_URL/api/v2/accounts/ACCOUNT_ID/runs/?job_definition_id=JOB_ID&status=10&order_by=-finished_at&limit=1`

In the query parameters, `status=10` filters for completed runs with a `Success` status. You can poll this endpoint on a schedule to identify the latest successful run, download its artifacts, and execute the `gcloud` import command.

#### Trigger the import using a webhook

Instead of polling the API, you can configure a dbt Cloud webhook to trigger an automated metadata import whenever a job run finishes. The webhook sends a payload to an HTTP endpoint that you provide:

  1. In the dbt Google Cloud console, go to **Account settings** > **Webhooks** and click **Create webhook** (or **Create new webhook**). Configure the webhook subscription: 
     * **Events** : select **Run completed** (`job.run.completed`), which triggers only after the run finishes and its artifacts are available for download.
     * **Jobs** : select the dbt Cloud deployment jobs that you want to monitor.
     * **Endpoint** : enter the HTTPS URL of a service that you run (for example, a Cloud Run service or Cloud Run function).
  2. Save the webhook secret token that dbt Cloud displays. Your service uses this secret to verify the `Authorization` header, which contains an HMAC-SHA256 signature of the request body.
  3. In your service, read `data.runId` from the JSON payload, download the run's artifacts using the Administrative API as described earlier, and run the `gcloud dataplex dbt metadata-jobs create` command.



When implementing your webhook handler, consider the following:

  * dbt Cloud waits at most 10 seconds for a response. Because the metadata import takes several minutes, return an HTTP response first and run the import in the background (for example, as a Cloud Run job or with the `--async` flag).
  * `job.run.completed` also triggers for failed runs, so runs with failing tests are still imported. Don't subscribe to `job.run.errored`, because it can trigger before the run's artifacts are available.



For more information about webhook payloads and signature verification, see [Webhooks for your jobs](https://docs.getdbt.com/docs/deploy/webhooks) in the dbt documentation.

## Configure dbt connectivity

To establish dbt connectivity, you must first run the appropriate dbt commands to generate the metadata artifacts. Once the JSON files are stored and accessible, the import process performs the following actions:

  1. **Read input artifacts** : Read the JSON artifacts generated by dbt Core and MetricFlow from the input location (local directory or Cloud Storage URI specified in `--artifacts-path`).
  2. **Transform metadata** : Transform the content into the Knowledge Catalog metadata import format (`dbt_metadata.jsonl`).
  3. **Upload to staging** : Upload the transformed metadata import file to the output staging Cloud Storage location specified in `--storage-uri`.
  4. **Trigger import job** : Trigger a Knowledge Catalog metadata import job that instructs the Knowledge Catalog service agent to read and ingest the staged metadata from `--storage-uri` into Knowledge Catalog resources.



### Console

  1. In the Google Cloud console, go to the **Knowledge Catalog** **Connectors** page.

[Go to Connectors](https://console.cloud.google.com/dataplex/connectors)

  2. Click **Add connection**.

  3. In the **Connectors** list, select the **dbt Core and MetricFlow** card.

**Note:** Because dbt Core metadata ingestion requires transforming client-side dbt artifact JSON files (`manifest.json`, `catalog.json`, `run_results.json`, `sources.json`) into the Knowledge Catalog import format before ingestion, selecting this card directs you to the CLI or API instructions.
  4. To view your imported dbt assets, go to the **Search** page or view the destination **Entry groups** page.




### gcloud

To create a dbt metadata job, complete the following steps:

  1. Ensure the dbt metadata artifact files are stored locally or in an input Cloud Storage bucket.
  2. Ensure you have an output staging Cloud Storage bucket configured with the appropriate permissions for both the caller and the Knowledge Catalog service agent.
  3. From Cloud Shell, a local terminal, or an automated workflow tool, execute the `gcloud` command:
         
         gcloud dataplex dbt metadata-jobs create my-dbt-import \
             --project=my-project \
             --location=us-central1 \
             --artifacts-path=. \
             --entry-group=dbt-metadata-ingestion \
             --storage-uri=gs://my-bucket/dbt-imports/
         

#### Required flags

     * `--storage-uri=STORAGE_URI`: **(Output/Staging)** Cloud Storage URI prefix (`gs://bucket/path/`) where the transformed JSONL is uploaded to and where the import job reads from during ingestion. The caller must have write access (`roles/storage.objectCreator` or `roles/storage.objectAdmin`), and the Knowledge Catalog service agent must have read access (`roles/storage.objectViewer`).

#### Optional flags

     * `--artifacts-path=ARTIFACTS_PATH`: **(Input)** Path to the source dbt artifacts. This can be a local directory path (such as `.` or `./target`) or a Cloud Storage URI prefix (such as `gs://my-bucket/dbt-artifacts/`). May point at the dbt project root (the `target/` subdirectory is detected automatically) or directly at the directory containing `manifest.json`. Defaults to `.`. If a Cloud Storage URI is provided, the caller must have read access (`roles/storage.objectViewer` or `roles/storage.objectAdmin`) to the input bucket.
     * `--async`: Return immediately, without waiting for the operation in progress to complete.
     * `--entry-group=ENTRY_GROUP`: Short ID of the entry group that receives the dbt entries. Must already exist in the project and location (default is `dbt-metadata-ingestion`).
     * `--aspects-only`: Update only the metadata this dbt run observed and leave the rest of the entry group untouched. No entry is created, deleted, or re-parented, no entry link is emitted, and an aspect whose dbt artifact was absent from this run keeps the value a previous run gave it. Use this for routine, repeated ingestion. See Re-run ingestion.
     * `--include-entry-links`: Emit entry links for dbt relationships. This is enabled by default. To disable it, use `--no-include-entry-links`. The command emits the following entry link types: 
       * `reference`: one resource depends on, describes, or uses another. This covers dbt dependencies between nodes, a test and the resource it tests, a semantic model or metric and the resource it's built on, a node and the project macros it calls, and a node and the BigQuery table it materializes to.
       * `schema-join`: joinable columns declared by a dbt `relationships` test.
     * `--skip-bigquery-link`: Skip `reference` links (dbt node → physical BigQuery table). By default, a `reference` link is emitted for each materialized dbt node (model, seed, snapshot) whose BigQuery dataset lives in the import location (`--location`). dbt sources don't receive a `reference` link to their BigQuery table. Entry links can only reference `@bigquery` entries in that same region, so datasets in another region are skipped automatically. To determine each dataset's region, the command calls the BigQuery API, so the caller needs the `bigquery.datasets.get` permission on those datasets; without it, the command can't skip datasets in other regions and links to them don't resolve. When the BigQuery tables aren't cataloged in Knowledge Catalog, use `--skip-bigquery-link`.
     * `--validate-only`: Build and upload the JSON and validate the metadata job, but don't actually ingest.
  4. Confirm you received a **Created** status.




### REST

To import dbt metadata using the REST API:

  1. Generate the dbt artifacts and transform them into the Knowledge Catalog JSON import file (`dbt_metadata.jsonl`).
  2. Upload the transformed file to your Cloud Storage staging bucket (`gs://BUCKET_NAME/PATH/`).
  3. Call the [`projects.locations.metadataJobs.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/create) method:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/metadataJobs?metadataJobId=JOB_ID \
             -d '{
               "type": "IMPORT",
               "importSpec": {
                 "sourceStorageUri": "gs://BUCKET_NAME/PATH/",
                 "entrySyncMode": "FULL",
                 "aspectSyncMode": "INCREMENTAL",
                 "scope": {
                   "entryGroups": [
                     "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP"
                   ],
                   "entryTypes": [
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-project",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-model",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-source",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-seed",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-snapshot",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-group",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-exposure",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-metric",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-macro",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-semantic-model",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-saved-query",
                     "projects/dataplex-connector-types/locations/global/entryTypes/dbt-test"
                   ],
                   "aspectTypes": [
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-node",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-project",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-model",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-source",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-seed",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-snapshot",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-group",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-exposure",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-metric",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-macro",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-semantic-model",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-saved-query",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-data-quality",
                     "projects/dataplex-connector-types/locations/global/aspectTypes/dbt-model-contracts"
                   ]
                 }
               }
             }'
         

Replace the following:

     * PROJECT_ID: the Google Cloud project ID where your entry group is located.
     * LOCATION: the region of your entry group (for example, `us-central1`).
     * JOB_ID: a unique identifier for the metadata job.
     * BUCKET_NAME/PATH: the Cloud Storage URI prefix where `dbt_metadata.jsonl` was uploaded.
     * ENTRY_GROUP: the short ID of the destination entry group.
  4. To track the status of your import job, use the [`projects.locations.metadataJobs.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.metadataJobs/get) method:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/metadataJobs/JOB_ID
         




After you create the job, Knowledge Catalog schedules the first run according to your configuration, or you can start it manually.

## Re-run ingestion

After the first import, most runs only need to refresh metadata for resources that already exist. Use `--aspects-only` for those runs. It updates only what the dbt run observed and leaves everything else in the entry group alone, so it is safe to run repeatedly, on any schedule, and from more than one job.

**Run a full ingestion** (omit `--aspects-only`) when the set of entries changes:

  * The first ingestion into an entry group.
  * A dbt resource is added, renamed, or deleted.
  * An entry's display name, description, or labels change.
  * The entry hierarchy changes.
  * dbt dependencies change, for example when a `ref()`, `source()`, test, or macro call is added or removed. `--aspects-only` runs don't create or update entry links.
  * You change `--include-entry-links` or `--skip-bigquery-link`.



A full run rewrites every entry's required aspects from the artifacts on disk, so run it from as complete an artifact set as your pipeline can produce.

**Run`--aspects-only`** for routine refreshes:

  * After whichever dbt command your pipeline runs: `dbt build`, `dbt test`, `dbt source freshness`, or a `--select`-narrowed rebuild.
  * A column is added, removed, retyped, or re-described.
  * Model SQL changed and the run also wrote `catalog.json`.
  * New test results or source freshness.



`--aspects-only` can add and refresh metadata, but can't remove it.

## Search and view dbt metadata

### Console

  1. In the Google Cloud console, go to the **Knowledge Catalog** **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In the **Filters** panel, filter for dbt assets:

     * In the **System** section, select **Imported Context**.
     * In the **Managed Connectors** subsection that appears, select **dbt**.
  3. In the search field, enter your query using keyword or natural language search. For example, to view all dbt assets using keyword search, enter `system=DBT` or `system=DBT AND type=dbt-model`.

  4. In the search results, click any dbt asset to open its entry details page to view its schema, lineage, and technical aspects.




### gcloud

  1. To search for dbt entries across your project, use the [`gcloud dataplex entries search` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/search):
         
         gcloud dataplex entries search 'system=DBT' \
             --project=PROJECT_ID
         

To filter by a specific dbt entry type (such as models or sources):
         
         gcloud dataplex entries search 'system=DBT AND type=dbt-model' \
             --project=PROJECT_ID
         

  2. To view the full details and aspects of a specific dbt entry, use the [`gcloud dataplex entries lookup` command](https://docs.cloud.google.com/sdk/gcloud/reference/dataplex/entries/lookup):
         
         gcloud dataplex entries lookup ENTRY_ID \
             --project=PROJECT_ID \
             --location=LOCATION \
             --entry-group=ENTRY_GROUP \
             --view=FULL
         

Replace the following:

     * PROJECT_ID: your Google Cloud project ID.
     * LOCATION: the location of the entry group (for example, `us-central1`).
     * ENTRY_GROUP: the short ID of your destination entry group (for example, `dbt-metadata-ingestion`).
     * ENTRY_ID: the short ID or relative resource name of the dbt entry.



### REST

  1. To search for dbt entries, call the [`projects.locations:searchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) method:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/global:searchEntries \
             -d '{
               "query": "system=DBT"
             }'
         

To filter by a specific dbt resource type:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/global:searchEntries \
             -d '{
               "query": "system=DBT AND type=dbt-model"
             }'
         

  2. To retrieve full metadata details and aspects for a specific entry, call the [`projects.locations.entryGroups.entries.get`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/get) method:
         
         curl -X GET \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP/entries/ENTRY_ID?view=FULL
         

  3. To retrieve LLM context for specific dbt resources, use the [`projects.locations:lookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) API:
         
         curl -X POST \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:lookupContext \
             -d '{
               "resources": [
                 "projects/PROJECT_ID/locations/LOCATION/entryGroups/ENTRY_GROUP/entries/ENTRY_ID"
               ]
             }'
         

Replace the following:

     * PROJECT_ID: your Google Cloud project ID.
     * LOCATION: the location of the entry group (for example, `us-central1`).
     * ENTRY_GROUP: the short ID of your destination entry group (for example, `dbt-metadata-ingestion`).
     * ENTRY_ID: the short ID or relative resource name of the dbt entry.



To list the entry links of a dbt entry, call the [`projects.locations:lookupEntryLinks`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupEntryLinks) method. For example, to retrieve the BigQuery table that a dbt model materializes to:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:lookupEntryLinks?entry=ENTRY_NAME&entryMode=SOURCE&entryLinkTypes=projects/dataplex-types/locations/global/entryLinkTypes/reference"
    

`ENTRY_NAME` is the full resource name of the dbt entry. Results are paginated, with at most 10 links per page.

To learn more about searching for resources, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets). To learn more about query expressions and filters, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/search-syntax).

## What's next

  * Learn how to [Manage connector jobs](https://docs.cloud.google.com/knowledge-catalog/docs/manage-connector-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
