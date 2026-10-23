---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/personas-and-serverless-iam-roles/
title: Personas and serverless IAM roles \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:05.088436+00:00
---

# Personas and serverless IAM roles  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/personas-and-serverless-iam-roles/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Personas and serverless IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows Spark developers, Spark administrators, and Spark viewers how to get the permissions they need to start using Managed Service for Apache Spark serverless serverless [batch workloads and interactive sessions](https://docs.cloud.google.com/managed-spark/docs/serverless-overview).

Persona | Who they are in the organization | What they need from IAM  
---|---|---  
Spark developer | The builder and consumer of the platform. Writes and runs PySpark and Spark jobs, develops in notebooks and sessions, reads and writes datasets, and monitors and troubleshoots their workloads. Includes data engineers, data scientists, and developers. | Permissions to submit, run, monitor, and troubleshoot workloads, and to read and write the data that their jobs touch.  
Spark administrator | The platform owner and manager. Sets up the project, decides how workloads authenticate, onboards Spark developers, manages shared service accounts, and enforces organization guardrails and least privilege. Also called the platform administrator. | Permissions to grant access to others, configure execution identity (end-user credentials or a shared service account), and manage project-wide serverless resources.  
Spark viewer | The observer and auditor of the platform. Tracks job completion, execution history, metrics, and dashboards without submitting or modifying workloads. Includes analysts, project managers, FinOps, and compliance auditors. | Read-only permissions to view batches, sessions, operations, and status dashboards.  
The Spark administrator does one-time project setup and grants roles, the Spark developer submits and manages workloads, and the Spark viewer monitors status, execution metrics, and dashboards.

## Choose a runtime version

The recommended runtime version depends on the Apache Spark version that your workloads run on.

  * **Runtime`3.x` (Recommended)**: uses Spark `4` and has simpler onboarding and usage. By default, workloads run as the submitting user with the user's end-user credentials (EUC), which requires the grant of a single IAM role to the user. Administrators can configure workload custom service accounts for more advanced usage.

  * **Runtime`2.x`**: uses Spark `3.5` and uses separate submitter and workload accounts. By default, the submitter is the user identity, and the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) is the workload identity. Administrators can configure custom workload service accounts for finer-grained access control.




For more information, see [Managed Service for Apache Spark runtime releases](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions).

### Feature comparison

Runtime `3.x` upgrades `2.x` components and capabilities, and provides a simplified setup:

Capability and workflow | Runtime `3.x` (recommended) | Runtime `2.x`  
---|---|---  
Apache Spark version | Spark 4 | Spark 3.5 (and earlier `3.x`)  
Interactive development | Spark Connect sessions (industry-standard interactive Spark client) | Jupyter sessions  
R batch workloads | `sparklyr` | SparkR batches  
Execution identity | End-user credentials (EUC)1 | Service account 1  
Storage for job staging | Not required (managed internally) | Cloud Storage staging buckets  
Log output format | Structured JSON format (`jsonPayload`) | Plain text format (`textPayload`)  
  
1 Runtime `3.x` defaults to the submitter's end-user credentials (EUC) unless a custom service account is specified for the workload or session. Runtime `2.x` defaults to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) unless a custom service account is specified for the workload or session.

### Common data and service roles

Managed Service for Apache Spark typically to read from and write to other Google Cloud services. This section lists roles associated with commonly accessed services.

  * **Runtime`3.x`** (default EUC identity): Grant roles to the Spark developer (user or group).
  * **Runtime`2.x`:** Grant roles to the workload service account (the Compute Engine default service account or a custom workload service account).

Service or API | Role | Purpose  
---|---|---  
**Cloud Storage** | `roles/storage.objectViewer`  
`roles/storage.objectAdmin` | Read input data and staged scripts.  
Write output data.  
**BigLake and Lakehouse runtime catalog** | `roles/biglake.viewer`  
`roles/biglake.editor`  
`roles/biglake.admin` | Query and manage open table formats, such as Apache Iceberg and Delta Lake, using the BigLake REST catalog (Lakehouse REST Catalog (LRC)).  
**Bigtable** | `roles/bigtable.reader`  
`roles/bigtable.user` | Read Bigtable tables.  
Read and write Bigtable data.  
**Dataproc Metastore (DPMS)** | `roles/metastore.metadataViewer`  
`roles/metastore.editor` | Read Hive metadata.  
Manage metadata schemas and tables.  
  
DPMS is a legacy metastore. Customers are encouraged to use the BigLake Lakehouse REST Catalog (LRC).  
  
BigQuery offers many fine-grained IAM roles and resource-level ACLs. For more information, see [BigQuery IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control).

### Grant roles

The following section contains instructions on how to grant roles for each of the personas associated with setting up, submitting, and monitoring Managed Service for Apache Spark serverless 3.x and 2.x batch workloads and interactive sessions.

### Runtime 3.x

By default, `3.x` workloads run under the submitting user's end-user credentials (EUC). Administrators grant a single role to the user, and no shared service accounts or staging buckets are required. Administrators can configure custom service accounts when dedicated service identities are required.

### Developer

### Spark developer (runtime 3.x)

As a Spark developer, you can use runtime `3.x` with your user credentials to develop, submit, monitor and troubleshoot Spark workloads, and to access data directly

  1. Request the serverless editor role. Ask your administrator to grant you `roles/dataproc.serverlessEditor` on the project.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/dataproc.serverlessEditor"
         

This role lets you submit, monitor, troubleshoot, and cancel Spark batch workloads and interactive Spark Connect sessions.

  2. Get access to data and services. Because the workload runs as you, your identity needs access to the services and datasets your Spark application touches (see Common data and service roles).

For example, grant yourself read access to an input Cloud Storage bucket:
         
         gcloud storage buckets add-iam-policy-binding gs://INPUT_BUCKET \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/storage.objectViewer"
         

  3. Submit a test workload. Submit a test batch workload to confirm your setup.
         
         gcloud dataproc batches submit spark \
           --region=REGION \
           --version=3.0 \
           --class=org.apache.spark.examples.SparkPi \
           --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
           -- 1000
         

Notes:

     * If this is your first time submitting a `3.x` workload under end-user credentials (EUC), you are prompted for one-time OAuth consent. Grant the consent, and then resubmit the workload.

     * If your project does not have a `default` VPC network, use the `subnet` flag or field to specify your regional subnet (see [Managed Service for Apache Spark serverless network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless)).

     * For an end-to-end example of running PySpark workloads and configuring the required permissions across Cloud Storage, BigLake, and BigQuery, see [Transform data and write to an Apache Iceberg table](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-to-iceberg).




#### Custom workload service accounts (runtime 3.x)

Use a custom service account with runtime `3.x` when your organization requires workloads to run under a dedicated, auditable identity instead of end-user credentials (see [IAM service account best practices](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)).

  1. Get permission to run workloads as the custom service account. Ask your administrator to grant you `roles/iam.serviceAccountUser` on the custom service account.
         
         gcloud iam service-accounts add-iam-policy-binding \
           WORKLOAD_SA_EMAIL \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  2. Specify the custom service.
         
         gcloud dataproc batches submit spark \
           --region=REGION \
           --service-account=WORKLOAD_SA_EMAIL \
           --version=3.0 \
           --class=org.apache.spark.examples.SparkPi \
           --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
           -- 1000
         

  3. Grant dataset access. When using a custom service account, grant data-level roles directly to `WORKLOAD_SA_EMAIL` (see Common data and service roles).




### Administrator

### Spark administrator (runtime 3.x)

As a Spark administrator, you set up the project, decide how workloads authenticate, and grant access to Spark developers.

Workloads use the named `default` VPC subnet automatically. If your project lacks a `default` network or uses custom VPCs, see [Managed Service for Apache Spark serverless network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless) to set up and specify a subnet for workloads and sessions.

#### Enable runtime 3.x with end-user credentials (recommended)

This is the least-privilege, lowest-maintenance setup. Each Spark developer runs workloads as their user identity; administrators don't need to set up and manage workload service accounts.

  1. Grant `roles/dataproc.serverlessEditor` to Spark developers.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/dataproc.serverlessEditor"
         

  2. Grant `roles/dataproc.serverlessViewer` to read-only viewers.

Grant this role to auditors, dashboard consumers, and team members who need to monitor job status and logs without submitting or modifying workloads.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:VIEWER_EMAIL" \
           --role="roles/dataproc.serverlessViewer"
         

  3. Ensure developer access to data.

By default, runtime `3.x` workloads run as the submitting user. Grant data access roles, such as `roles/storage.objectViewer` or `roles/storage.objectAdmin`, to the Spark developer or to the Google group that includes Spark developers (see Common data and service roles).




#### Enable workload custom service accounts (runtime 3.x)

Use a custom service account with runtime `3.x` when you need workloads to run under a dedicated, auditable identity instead of end-user credentials (see [IAM service account best practices](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)).

  1. Grant `roles/iam.serviceAccountUser` on the workload custom service account.
         
         gcloud iam service-accounts add-iam-policy-binding \
           WORKLOAD_SA_EMAIL \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  2. Grant `roles/dataproc.serverlessNode` to the workload custom service account.

This role lets the service account manage compute node pools and communicate with Spark applications during workload execution:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:WORKLOAD_SA_EMAIL" \
           --role="roles/dataproc.serverlessNode"
         

  3. Grant access to application data.

Grant data-level roles directly to the workload service account so it can read and write application datasets (see Common data and service roles). If your workloads use staged scripts or custom JARs, also grant read access on the corresponding Cloud Storage buckets.




#### Enable submitter custom service accounts (runtime 3.x)

Use a submitter custom service account when automated systems (such as Managed Service for Apache Airflow, Cloud Scheduler, or CI or CD pipelines) submit workloads without an interactive human user.

  * In this scenario, the submitter service account runs the `gcloud` command that starts the job. Here's an example using `gcloud`:
        
        gcloud dataproc batches submit spark \
          --service-account=WORKLOAD_SA_EMAIL \
          ...
        

  * The workload service account runs the Spark code on the compute nodes and accesses application datasets.

    1. Grant `roles/dataproc.serverlessEditor` to the submitter custom service account.
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="serviceAccount:SUBMITTER_SA_EMAIL" \
      --role="roles/dataproc.serverlessEditor"
    

When using runtime `3.x` with a submitter custom service account, a custom workload service account is needed to run the workload; the runtime cannot fall back to end-user credentials (EUC) since there is no interactive end user. The job must run as a specified workload service account (`--service-account`).



  1. Grant `roles/iam.serviceAccountUser` on the workload custom service account.
         
         gcloud iam service-accounts add-iam-policy-binding \
           WORKLOAD_SA_EMAIL \
           --member="serviceAccount:SUBMITTER_SA_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  2. Configure the workload custom service account. Grant `roles/dataproc.serverlessNode` and application data roles to `WORKLOAD_SA_EMAIL`.




#### Spark administrator roles reference (runtime 3.x)

The following table summarizes the roles to grant with runtime `3.x`.

Submitter | Workload identity | Grant to submitter | Grant to workload service account  
---|---|---|---  
End user (default) | End user (EUC) | `roles/dataproc.serverlessEditor` (+ data roles on user) | _(none—no SA used)_  
End user | Custom SA | `roles/dataproc.serverlessEditor` \+ `roles/iam.serviceAccountUser` on custom SA | `roles/dataproc.serverlessNode` \+ data roles  
Custom SA (automation) | Custom SA | `roles/dataproc.serverlessEditor` \+ `roles/iam.serviceAccountUser` on custom SA | `roles/dataproc.serverlessNode` \+ data roles  
  
### Viewer

### Spark viewer (runtime 3.x)

As a Spark viewer, you view batch workloads, interactive sessions, execution metrics, logs, and status dashboards without submitting or modifying workloads.

Ask your administrator to grant you `roles/dataproc.serverlessViewer`.
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:VIEWER_EMAIL" \
      --role="roles/dataproc.serverlessViewer"
    

This role gives read-only access to view serverless batch workloads, interactive sessions, and operation status.

### Detailed permissions

### Detailed permissions (runtime 3.x)

This section lists the IAM permissions included in IAM roles associated with runtime `3.x`.

#### Serverless Editor role (`roles/dataproc.serverlessEditor`)

This role with its permissions provides read and write access to runtime `3.x` serverless batch workloads and interactive sessions.

Permission | Description  
---|---  
`dataproc.batches.create` | Create and submit new batch workloads.  
`dataproc.batches.get` | Get batch workload status and details.  
`dataproc.batches.list` | List all batch workloads in a project or region.  
`dataproc.batches.delete` | Delete completed or terminated batches.  
`dataproc.batches.cancel` | Cancel a running batch workload.  
`dataproc.sessions.create` | Create interactive Spark Connect sessions.  
`dataproc.sessions.get` | Get session status and details.  
`dataproc.sessions.list` | List all sessions in a project or region.  
`dataproc.sessions.delete` | Delete terminated sessions.  
`dataproc.sessions.terminate` | Terminate a running interactive session.  
`dataproc.operations.get` | Poll asynchronous operation status (required by the `gcloud` CLI).  
  
#### Serverless Node role (`roles/dataproc.serverlessNode`)

Provides node pool management and internal Spark communication permissions for runtime `3.x` custom workload service accounts.

This roles with its permissions are required when using a custom workload service account with runtime `3.x`. Workloads running under default `3.x` end-user credentials (EUC) don't use a workload service account.

Permission | Description  
---|---  
`dataproc.batches.sparkApplicationWrite` | Spark application communication for batch workloads.  
`dataproc.sessions.sparkApplicationWrite` | Spark application communication for interactive sessions.  
`dataprocrm.nodePools.create` | Create compute node pools.  
`dataprocrm.nodePools.delete` | Delete compute node pools.  
`dataprocrm.nodePools.resize` | Scale node pools dynamically.  
`dataprocrm.nodePools.get` | Read node pool status.  
`dataprocrm.nodePools.list` | List node pools.  
`dataprocrm.nodePools.update` | Update node pool configuration.  
`dataprocrm.nodePools.deleteNodes` | Remove specific nodes from a pool.  
`dataprocrm.nodes.list` | List nodes in a pool.  
`dataprocrm.nodes.delete` | Delete nodes upon task completion.  
`dataprocrm.nodes.get` | Read node status.  
`dataprocrm.nodes.heartbeat` | Report node health and heartbeats.  
`dataprocrm.nodes.mintOAuthToken` | Mint OAuth tokens for node operations.  
`dataprocrm.operations.get` | Check infrastructure operation status.  
  
#### Serverless Viewer role (`roles/dataproc.serverlessViewer`)

This role with its permissions are required when using runtime `3.x` with a submitter custom service account. They provide read-only access to runtime `3.x` serverless batch workloads, interactive sessions, and operation status.

Permission | Description  
---|---  
`dataproc.batches.get` | Read batch workload status and details.  
`dataproc.batches.list` | List batch workloads.  
`dataproc.sessions.get` | Read session status and details.  
`dataproc.sessions.list` | List sessions.  
`dataproc.operations.get` | Read operation status.  
`dataproc.operations.list` | List operations.  
  
#### Service account delegation role (`roles/iam.serviceAccountUser`)

Allows a user or automated system to attach and run workloads as a custom service account. The workload executes with the permissions and resource access granted to that service account rather than the submitting user's end-user credentials (EUC).

Permission | Description  
---|---  
`iam.serviceAccounts.actAs` | Allows the submitter to run workloads as the specified service account.  
  
### Runtime 2.x

By default, runtime `2.x` workloads run as the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account). The submitter (the user or automated system) acts as this account when running workloads or sessions.

### Developer

### Spark developer (runtime 2.x)

As a Spark developer using runtime `2.x`, you develop, submit, monitor, and troubleshoot Spark workloads, and access data. Because the workload runs as a service account rather than your user identity, an administrator grants you the IAM Editor role and the Service Account User role to run workloads as the workload service account.

  1. Request the editor role. Ask your administrator to grant you `roles/dataproc.editor` on the project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/dataproc.editor"
         

  2. Request delegation permission. Ask your administrator to grant you `roles/iam.serviceAccountUser` on the workload service account.

The default workload service account is the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), `PROJECT_NUMBER-compute@developer.gserviceaccount.com`:
         
         gcloud iam service-accounts add-iam-policy-binding \
           PROJECT_NUMBER-compute@developer.gserviceaccount.com \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  3. Get staging bucket access. The runtime `2.x` submitter needs permission to upload scripts and JARs, and the workload service account needs permission to manage temporary files and logs. These permissions are contained in the `roles/storage.objectAdmin` role.
         
         # Grant submitter access to upload staged files
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/storage.objectAdmin"
         
         # Grant workload service account access for staging, temporary files, and logs
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
           --role="roles/storage.objectAdmin"
         

  4. Submit a test batch workload. Submit a test batch workload to confirm your setup.
         
         gcloud dataproc batches submit spark \
           --region=REGION \
           --version=2.2 \
           --class=org.apache.spark.examples.SparkPi \
           --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
           -- 1000
         

Notes:

     * Because your workload runs as the workload service account, that account, not your user account, needs access to the data that your job reads and writes (see Common data and service roles).

     * If your project does not have a `default` VPC network, use the `subnet` flag or field to specify your regional subnet (see [Managed Service for Apache Spark serverless network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless)).

     * For an end-to-end example of running PySpark workloads and configuring the required permissions across Cloud Storage, BigLake, and BigQuery, see [Transform data and write to an Apache Iceberg table](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-to-iceberg).




#### Custom workload custom service accounts (runtime 2.x)

Use a custom service account when your organization requires workloads to run under a dedicated, auditable identity instead of the shared [Compute Engine default service_account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) (see [IAM service account best practices](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)).

  1. Get permission to run workloads as the custom service account. Ask your administrator to grant you `roles/iam.serviceAccountUser` on the custom service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
           WORKLOAD_SA_EMAIL \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  2. Specify the custom service account with the `--service-account` flag when submitting workloads.
         
         gcloud dataproc batches submit spark \
           --region=REGION \
           --service-account=WORKLOAD_SA_EMAIL \
           --version=2.2 \
           --class=org.apache.spark.examples.SparkPi \
           --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
           -- 1000
         

  3. **Dataset access:** If your workload cannot access datasets, grant the workload custom service account (not your user account) the required data access roles (see Common data and service roles).




### Administrator

### Spark administrator (runtime 2.x)

As a Spark administrator, you set up the project, configure service accounts, and grant access to Spark developers.

Workloads use the named `default` VPC subnet automatically. If your project lacks a `default` network or uses custom VPCs, see [Managed Service for Apache Spark serverless network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless) to set up and specify a subnet for workloads and sessions.

#### Enable default runtime 2.x

With default runtime `2.x`, workloads run as the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

  1. Grant `roles/dataproc.editor` to the developer.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/dataproc.editor"
         

  2. Grant `roles/iam.serviceAccountUser` on the default service account.
         
         gcloud iam service-accounts add-iam-policy-binding \
           PROJECT_NUMBER-compute@developer.gserviceaccount.com \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  3. Grant `roles/dataproc.worker` to the workload service account.

This role lets the service account register the [VM agent](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job), lease and execute compute tasks, and emit logs and metrics to Cloud Logging and Cloud Monitoring:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
           --role="roles/dataproc.worker"
         

  4. Grant `roles/storage.objectAdmin` for staging bucket storage.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" \
           --role="roles/storage.objectAdmin"
         

  5. Grant dataset access to the workload service account.

Grant data-level roles to the workload service account to let it access Spark application datasets (see Common data and service roles).




#### Enable workload custom service accounts (runtime 2.x)

Use a workload custom service account with runtime `2.x` to isolate workloads instead of using the shared Compute Engine default service account.

  1. Grant `roles/iam.serviceAccountUser` on the custom service account to the developer.
         
         gcloud iam service-accounts add-iam-policy-binding \
           WORKLOAD_SA_EMAIL \
           --member="user:DEVELOPER_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  2. Grant `roles/dataproc.worker` to the custom service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:WORKLOAD_SA_EMAIL" \
           --role="roles/dataproc.worker"
         

  3. Grant application data and staging access.

Grant data-level roles directly to the workload custom service account (see Common data and service roles) and grant `roles/storage.objectAdmin` on staging and temporary buckets.




#### Enable submitter custom service accounts (runtime 2.x)

Use a submitter custom service account when automated systems (such as Managed Service for Apache Airflow, Cloud Scheduler, or CI CD pipelines) submit workloads without an interactive human user.

  1. Grant `roles/dataproc.editor` to the submitter service account.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:SUBMITTER_SA_EMAIL" \
           --role="roles/dataproc.editor"
         

  2. Grant `roles/iam.serviceAccountUser` on the workload service account.
         
         gcloud iam service-accounts add-iam-policy-binding \
           WORKLOAD_SA_EMAIL \
           --member="serviceAccount:SUBMITTER_SA_EMAIL" \
           --role="roles/iam.serviceAccountUser"
         

  3. Configure the workload service account. Grant `roles/dataproc.worker` and dataset access to `WORKLOAD_SA_EMAIL`.




#### Spark administrator roles reference (runtime 2.x)

The following table summarizes the IAM roles to grant with runtime `2.x`.

Submitter | Workload identity | Grant to submitter | Grant to workload service account  
---|---|---|---  
End user (default) | Compute Engine default SA | `roles/dataproc.editor` \+ `roles/iam.serviceAccountUser` on default SA | `roles/dataproc.worker` \+ `roles/storage.objectAdmin` \+ data roles  
End user | Custom SA | `roles/dataproc.editor` \+ `roles/iam.serviceAccountUser` on custom SA | `roles/dataproc.worker` \+ `roles/storage.objectAdmin` \+ data roles  
Custom SA (automation) | Custom SA | `roles/dataproc.editor` \+ `roles/iam.serviceAccountUser` on custom SA | `roles/dataproc.worker` \+ `roles/storage.objectAdmin` \+ data roles  
  
### Viewer

### Spark viewer (runtime 2.x)

As a Spark viewer, you view batch workloads, interactive sessions, execution metrics, logs, and status dashboards without submitting or modifying workloads.

Ask your administrator to grant you `roles/dataproc.viewer`:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="user:VIEWER_EMAIL" \
      --role="roles/dataproc.viewer"
    

This role gives read-only access across Managed Service for Apache Spark resources, such as clusters, jobs, batches, sessions, and operations.

### Detailed permissions

### Detailed permissions (runtime 2.x)

This section lists the IAM permissions included in IAM roles associated with runtime `2.x`.

#### Editor role (`roles/dataproc.editor`)

This role provides control over runtime `2.x` serverless workloads and sessions, as well as Managed Service for Apache Spark clusters and jobs on Compute Engine.

Permission | Required for serverless | Description  
---|---|---  
`dataproc.batches.create` | **Yes** | Create and submit new batch workloads.  
`dataproc.batches.get` | **Yes** | Get batch workload status and details.  
`dataproc.batches.list` | **Yes** | List all batch workloads in a project or region.  
`dataproc.batches.delete` | **Yes** | Delete completed or terminated batches.  
`dataproc.batches.cancel` | **Yes** | Cancel a running batch workload.  
`dataproc.sessions.create` | **Yes** | Create interactive sessions.  
`dataproc.sessions.get` | **Yes** | Get session status and details.  
`dataproc.sessions.list` | **Yes** | List all sessions in a project or region.  
`dataproc.sessions.delete` | **Yes** | Delete terminated sessions.  
`dataproc.sessions.terminate` | **Yes** | Terminate a running interactive session.  
`dataproc.operations.get` | **Yes** | Poll asynchronous operation status (required by the `gcloud` CLI).  
`compute.networks.get` | **Yes** | View VPC network configuration.  
`compute.networks.list` | **Yes** | List available VPC networks and subnets.  
`dataproc.clusters.*` | No (clusters only) | Create, manage, and use Compute Engine-based Managed Service for Apache Spark clusters.  
`dataproc.jobs.*` | No (clusters only) | Submit and manage jobs on Compute Engine-based Managed Service for Apache Spark clusters.  
`dataproc.autoscalingPolicies.*` | No (clusters only) | Autoscaling policies for Compute Engine-based clusters.  
`dataproc.nodeGroups.*` | No (clusters only) | Custom node groups on Compute Engine-based clusters.  
`dataproc.workflowTemplates.*` | No (clusters only) | Template workflows for Compute Engine-based clusters.  
`compute.machineTypes.*` | No (clusters only) | Machine type metadata for Compute Engine-based clusters.  
  
#### Worker role (`roles/dataproc.worker`)

This role provides workload execution permissions for runtime `2.x`.

Permission | Description  
---|---  
`dataproc.agents.create` | Register the [VM agent](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job) on the VM.  
`dataproc.agents.get` | Read agent state.  
`dataproc.agents.update` | Update agent state.  
`dataproc.agents.delete` | Deregister the agent upon completion.  
`dataproc.tasks.lease` | Lease compute tasks for execution.  
`dataproc.tasks.reportStatus` | Report task execution status.  
`storage.objects.create` | Write staging data, temporary files, and logs.  
`storage.objects.delete` | Clean up temporary files.  
`storage.objects.get` | Read boot scripts and staged files.  
`storage.objects.list` | List staging and temporary bucket contents.  
  
#### Viewer role (`roles/dataproc.viewer`)

This role provides read-only access across all Managed Service for Apache Spark resources.

Permission | Required for serverless | Description  
---|---|---  
`dataproc.batches.get` | **Yes** | Read batch workload status and details.  
`dataproc.batches.list` | **Yes** | List all batch workloads in a project or region.  
`dataproc.sessions.get` | **Yes** | Read session status and details.  
`dataproc.sessions.list` | **Yes** | List all sessions in a project or region.  
`dataproc.operations.get` | **Yes** | Read asynchronous operation status.  
`dataproc.operations.list` | **Yes** | List operations in a project or region.  
`dataproc.clusters.get` | No (clusters only) | View cluster configuration and status.  
`dataproc.clusters.list` | No (clusters only) | List clusters in a project or region.  
`dataproc.jobs.get` | No (clusters only) | View job details and status on clusters.  
`dataproc.jobs.list` | No (clusters only) | List jobs on clusters.  
`dataproc.autoscalingPolicies.get` | No (clusters only) | View autoscaling policy details.  
`dataproc.autoscalingPolicies.list` | No (clusters only) | List autoscaling policies.  
`dataproc.workflowTemplates.get` | No (clusters only) | View workflow template details.  
`dataproc.workflowTemplates.list` | No (clusters only) | List workflow templates.  
  
#### Service account delegation role (`roles/iam.serviceAccountUser`)

Allows a user or automated system to attach and run workloads as the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or a custom service account. The workload executes with the permissions and resource access granted to that service account.

Permission | Description  
---|---  
`iam.serviceAccounts.actAs` | Allows the submitter to run workloads as the specified service account.  
  
## What's next

  * Read [Transform data and write to an Apache Iceberg table](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-to-iceberg) for an end-to-end tutorial using PySpark and serverless Spark permissions.
  * Understand the [Life of a Managed Service for Apache Spark serverless batch workload](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job).
  * Learn about [Managed Service for Apache Spark serverless network configuration](https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
