---
url: https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs/
title: Set up log ingestion for self-managed SAP systems \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:27.922607+00:00
---

# Set up log ingestion for self-managed SAP systems  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Set up log ingestion for self-managed SAP systems Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to ingest logs from your self-managed SAP systems and forward them to Google SecOps.

## Select your ingestion path

In a self-managed SAP environment, the ingestion path depends on the log layer. To achieve comprehensive log coverage across your infrastructure and application layers, follow both paths described in this document:

Log layer | Log type | Ingestion path  
---|---|---  
Infrastructure logs | ICM, Gateway, Web Dispatcher, and SAP HANA Audit logs | Bindplane agent and Bindplane server  
Application logs | Security Audit Logs and Change Documents | Application Telemetry Collector, Bindplane agent, and Bindplane server  
  
## Before you begin

Before you start the ingestion process, ensure that you've completed the following steps:

  * **Planning** : Review the ingestion paths and technical requirements in the [Plan for log ingestion](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion) guide.
  * **Foundation** : Provision your Google SecOps instance and complete the [onboarding process](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#onboarding-to-google-security-operations) in Google Cloud.
  * **Bindplane setup** : Install and configure the centralized Bindplane server as described in the [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#setup-bindplane-server) guide.
  * **Network access** : Ensure your network architecture allows the Bindplane server to receive incoming traffic on port `4317` (gRPC) from all agents, and the Bindplane agent to receive incoming traffic on the same port from the Application Telemetry Collector.
  * **SAP preparation** : Ensure your SAP system is prepared (service user, authorizations, and SNC) as described in the [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#prepare-for-application-layer-logs) guide.
  * **Google Cloud resources** : Ensure that you have configured the required Google Cloud resources, such as APIs, storage buckets, and IAM roles, as described in the [Prepare your environment for log ingestion](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-gcp-resources-app-logs) guide.



## Ingest infrastructure logs

Follow this path to ingest logs from the SAP operating system and database layers, including SAP HANA Audit, ICM, and Gateway logs.

Infrastructure log ingestion involves the following components:

  * **Bindplane agent** : A lightweight agent installed on each SAP application server. The agent tails local log files and forwards them to the Bindplane server.
  * **Bindplane server** : Receives the logs from Bindplane agents, batches the data, and forwards the data to the Google SecOps gateway.



### Install the Bindplane agents on SAP hosts

To forward infrastructure logs, install the Bindplane agent on each SAP host by running the command generated in the Bindplane UI. For detailed instructions, see the [Bindplane agent installation guide](https://docs.bindplane.com/readme/install-your-first-collector).

To verify the installation, go to the **Agents** tab in the **Bindplane UI** and confirm that the agent is visible with a **Connected** status.

### Configure the Bindplane pipeline

For optimized log delivery, we recommend a two-step ingestion pipeline:

  1. **SAP to Bindplane Gateway** : Ingest logs from the SAP host and send them to the central Bindplane server. For more information, see Configure SAP host log collection.
  2. **Bindplane Gateway to Google SecOps** : Forward the processed logs from the Bindplane server to your Google SecOps instance. For more information, see Configure the Google SecOps destination.



### Configure the SAP host log collection

A configuration defines the SAP log sources that you want to ingest, the processors for log normalization, and the Bindplane gateway destination, which is the Bindplane server. For more information, see [Build Your First Configuration](https://docs.bindplane.com/readme/build-your-first-configuration).

#### Create the log collection configuration

Define the basic settings for your log ingestion pipeline, including the agent type and platform.

  1. In the **Bindplane UI** , go to the **Configurations** tab.
  2. Click **Create Configuration**.
  3. Enter a **Name** , for example, `sap-infra-logs`.
  4. Select **BDOT 1.x (Stable)** as the **Agent Type**.
  5. Select **Linux** as the **Platform**.
  6. Click **Next**.



#### Add SAP log sources

Define the specific log sources on your SAP host that you want the Bindplane agent to monitor. You can add multiple sources to a single configuration.

##### For SAP ICM, SAP Gateway, and SAP Web Dispatcher

To ingest standard text-based logs, add a **File** source:

  1. In the **Add Sources** stage, select the **File** source type.
  2. Enter a **Short Description**.
  3. In the **File Path(s)** field, enter the path to your SAP log files. For more information about the supported log sources and their default locations, see [Review supported log sources](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources).
  4. In the **Log Type** field, enter the value that corresponds to the SAP log source that you are configuring, for example, `SAP_ICM`. For more information about the required values, see the mapping table in the **Add the Google SecOps Standardization processor** section.
  5. Click **Save**.



##### For SAP HANA Audit

To ingest HANA Audit logs sent through syslog, add a **Syslog** source:

  1. In the **Add Sources** stage, select the **Syslog** source type.
  2. Enter a **Short Description**.
  3. Set the **Listening IP Address** , for example, `0.0.0.0`.
  4. Set the **Listening Port** , for example, `5140`.
  5. Set the **Protocol** to `rfc3164`.
  6. Set the **Transport Protocol** to `tcp` or `udp`.
  7. In the **Log Type** field, enter `SAP_HANA_AUDIT`.
  8. Click **Save**.



#### Add destination

Configure the central Bindplane server as the primary destination for all ingested logs.

  1. In the **Add Destination** stage, select **Bindplane Gateway**.
  2. Enter the **Hostname** or IP address of your Bindplane server.
  3. Ensure the **Port** is set to `4317`, which is the default OTLP gRPC.
  4. Select `grpc` as the **Protocol**.
  5. Click **Save**.



#### Add the Google SecOps Standardization processor

Apply normalization rules to your logs to ensure that they are compatible with the Google SecOps Unified Data Model (UDM).

The **Google SecOps Standardization** processor maps your raw SAP logs to specific Google SecOps log types. Selecting the correct **Log Type** ensures that Bindplane correctly interprets and normalizes data from sources like SAP ICM, Gateway, Web Dispatcher, and SAP HANA Audit for ingestion.

  1. In the configuration diagram, click **Add Processor** on the link between the source and destination.
  2. Select **Google SecOps Standardization**.
  3. Click **Create New**.
  4. Click **Add Log Type**.
  5. In the **Log Type** field, enter the value that corresponds to the SAP log source that you're configuring. The following table shows the mapping between the SAP source and the required Google SecOps log type:

SAP log source | SecOps log type  
---|---  
[SAP ICM Logs](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources) | `SAP_ICM`  
[SAP Gateway Logs](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources) | `SAP_GATEWAY`  
[SAP Web Dispatcher Logs](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources) | `SAP_WEBDISP`  
[SAP HANA Audit Logs](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources) | `SAP_HANA_AUDIT`  
  6. Click **Save** and then click **Finish**.




#### Deploy the configuration to agents

Once the configuration is ready, assign the configuration to your installed Bindplane agents.

  1. In the **Bindplane UI** , go to the **Configurations** tab.
  2. Select your new configuration, for example, `sap-infra-logs`.
  3. Click **Add Agents**.
  4. Select the SAP host Bindplane agents and click **Apply**.



### Configure the Google SecOps destination

Once logs reach the central Bindplane server, configure a forwarder to send them to your Google SecOps instance. This involves creating a separate configuration for the Bindplane server that listens for incoming OTLP data from your SAP host agents.

#### Create the log forwarding configuration

Define the basic settings for the pipeline on your central Bindplane server.

  1. In the **Bindplane UI** , go to the **Configurations** tab.
  2. Click **Create Configuration**.
  3. Enter a **Name** , for example, `sap-forwarder-secops`.
  4. Select **BDOT 1.x (Stable)** as the **Agent Type**.
  5. Select **Linux** as the **Platform**.
  6. Click **Next**.



#### Add the Bindplane gateway source

Configure an OpenTelemetry (OTLP) listener on the Bindplane server to receive logs from the agents installed on your SAP hosts.

  1. In the **Add Sources** stage, select the **Bindplane Gateway** source type.
  2. Enter a **Short Description**.
  3. In the **Listen Address** field, enter `0.0.0.0`.
  4. Ensure the **Port** is set to `4317`.
  5. Click **Save**.



##### Add the Batch processor

To prevent overwhelming the Google SecOps API, batch your requests.

  1. Click **Add Processor** and select **Batch**.
  2. Use the recommended defaults, usually `8192` units or a `200ms` timeout.
  3. Click **Save**.



#### Obtain Google SecOps credentials

To securely forward logs to Google SecOps, obtain your ingestion authentication file and customer ID from the Google SecOps console.

##### Google SecOps ingestion authentication file

To download the ingestion authentication file, do the following:

  1. Open the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the Google SecOps ingestion authentication file. Your next step depends on your transfer method:

     * **gRPC** : Use the downloaded ingestion authentication file.
     * **HTTPS** : Create a service account in the Google Cloud project linked to Google SecOps and assign the **Chronicle Editor** role to the service account.



##### Google SecOps customer ID

To find the customer ID, do the following:

  1. Open the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy the customer ID from the **Organization Details** section.



For more information, see [Get Google SecOps customer ID](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install-collector).

#### Create the Google SecOps destination in Bindplane

Set up the final destination in Bindplane to securely forward your processed logs to Google SecOps.

  1. In the **Bindplane UI** , go to the **Destinations** tab and click **Create Destination**.
  2. Select **Google SecOps** as the destination type.
  3. Enter a **Name** , for example, `secops-destination`.
  4. In the **Customer ID** field, paste your Google SecOps customer ID.
  5. In the **Credentials** field, click **Upload** and select the ingestion authentication file you downloaded, or paste the file content directly.
  6. Click **Save**.



### Confirm your log ingestion

To verify the setup, do the following:

  1. **In the Bindplane UI** : 
     1. Go to the **Configurations** tab and select your configuration.
     2. Click the **Source** or **Destination** and select **Recent Logs** to see a livestream of data passing through the pipeline.
  2. **In Google SecOps** : 
     1. Go to **Search**.
     2. Enter a UDM query to filter by your log type, for example, `metadata.log_type = "SAP_ICM"`. For instructions on searching and filtering logs, see [Search and filter SAP logs](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats#search-and-filter-sap-logs).
     3. Confirm that logs are appearing and are correctly parsed into UDM fields.
     4. Open the **Event Viewer** to inspect the raw log and the normalized UDM fields. For example, verify that the **Log Type** in the UDM view matches your source, such as `SAP_ICM`, and that key fields like **Principal Host** (`principal.host.hostname`) and relevant network or file details are populated.



## Ingest application logs

Follow this path to ingest log types such as Security Audit Logs and Change Documents directly from the SAP application layer using the RFC protocol.

Application log ingestion involves the following components:

  * **Application Telemetry Collector** : A containerized Java application that connects to your SAP application servers using the RFC protocol to extract security logs.
  * **Bindplane server** : Receives the logs from the Application Telemetry Collector and forwards them to Google SecOps.



### Prepare the collector host and dependencies

Provision the infrastructure to run the collector and upload the necessary SAP libraries.

  * **Infrastructure Instance** : Provision a host to run the collector container. 
    * **Host options** : You can use Compute Engine, on-premises servers, or container orchestration platforms like GKE.
    * **Specifications** : Use a standard Linux distribution, such as Debian 11 or 12, with Docker Engine 20.10 or later.
    * **Network** : The host requires internal network access to the Bindplane server and outbound access to your SAP server and Cloud Storage.
    * **Continuity** : Ensure the host is "always-on" to prevent log gaps. Don't use serverless platforms like Cloud Run.
    * **Identity (Within Google Cloud)** : Attach the service account created in the [Configure Google Cloud resources](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-gcp-resources-app-logs) section to the VM. In the console, set **Access Scopes** to **Allow full access to all Cloud APIs**.
    * **Identity (Outside Google Cloud)** : Use [service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete) or [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * **SAP Java Connector (JCo) and SNC libraries** : Upload the SAP connector and cryptographic files to the `jco/` folder in your Cloud Storage bucket. You create the `jco/` folder as described in the [Configure Google Cloud resources](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#setup-storage-buckets-iam-roles) guide. 
    * **SAP JCo** : Download `sapjco3.jar` and `libsapjco3.so` from the [SAP Support Portal](https://support.sap.com/en/product/connectors/jco.html) and upload them to the `jco/` folder. Ensure you download the version matching your host architecture (ARM or x86).
    * **SNC Libraries** : If you use SNC, download `libslcryptokernel.so` and `libsapcrypto.so` from the SAP portal, and then upload them to the `jco/` folder. For instructions on how to download the `.SAR` file and extract the files by using the `sapcar` utility, see the [SAP documentation](https://help.sap.com/docs/SAP_HANA_CLIENT/8e208b44c0784f028b948958ef1d05e7/463d3ceeb7404eca8762dfe74e9cff62.html).



### Configure the collector

Create a `collector_config.json` file to define your SAP connections and the logs you want to ingest.

Once you have defined the configuration, upload the `collector_config.json` file to the `config/` folder in the Cloud Storage bucket you created in the [Configure Google Cloud resources](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-gcp-resources-app-logs) section.

#### Configuration example and field descriptions

Use the following JSON example to create your collector configuration file and refer to the field descriptions for detailed parameter information.
    
    
    {
      "systems": [
        {
          "system_id": "PRD-HANA",
          "connection": {
            "host": "sap-prd.internal.net",
            "client": "100",
            "system_number": "00",
            "language": "en"
          },
          "auth": {
            "basic": {
              "username_secret": "projects/my-project-123/secrets/sap-collector-user/versions/latest",
              "password_secret": "projects/my-project-123/secrets/sap-collector-pass/versions/latest"
            }
          },
          "log_sources": [
            {
              "log_type": "SAP_SECURITY_AUDIT",
              "interval": "60s"
            },
            {
              "log_type": "SAP_CHANGE_DOCUMENT",
              "interval": "300s",
              "change_document_object_classes": ["PFCG", "IDENTITY"]
            }
          ],
          "initial_lookback_window": "86400s",
          "sap_timezone": "UTC"
        },
        {
          "system_id": "DEV-HANA-SNC",
          "connection": {
            "host": "sap-dev.internal.net",
            "client": "200",
            "system_number": "01",
            "language": "en"
          },
          "auth": {
            "x509": {
              "snc_name": "p:CN=SAP-Collector,O=MyCompany,C=US",
              "snc_partner_name": "p:CN=SAP-Server-DEV,O=MyCompany,C=US",
              "snc_qop": "3",
              "x509_cert_secret": "projects/my-project-123/secrets/sap-x509-cert/versions/latest"
            }
          },
          "log_sources": [
            {
              "log_type": "SAP_SECURITY_AUDIT",
              "interval": "120s"
            }
          ],
          "initial_lookback_window": "3600s",
          "sap_timezone": "UTC"
        }
      ],
      "bindplane_host": "127.0.0.1",
      "bindplane_port": 4317,
      "heartbeat_enabled": true,
      "heartbeat_interval": "30s",
      "heartbeat_metric_name": "custom/sap/collector_heartbeat",
      "jco_pse_secret": "projects/my-project-123/secrets/sap-collector-pse/versions/latest",
      "jco_cred_secret": "projects/my-project-123/secrets/sap-collector-cred/versions/latest"
    }
    

The following table describes the fields in the `collector_config.json` file.

Section | Field | Description  
---|---|---  
**System Connection (`systems`)**  
List of systems to monitor. | `system_id` | A unique label for the system, for example, `PRD`. In the example, replace `PRD-HANA` with your specific label.  
`sap_timezone` | The timezone of the SAP application server, for example, `UTC`. This is critical for accurate log querying.  
`initial_lookback_window` | How far back the collector looks for logs on its first run, for example, `"86400s"` for 24 hours.  
`connection` | Contains the following RFC connection parameters: 

  * `host`: The FQDN or IP of your SAP server. Replace `sap-prd.internal.net` in the example.
  * `client`: The 3-digit SAP client, for example, `"100"`.
  * `system_number`: The 2-digit instance number, for example, `"00"`.
  * `language`: The logon language, defaults to `"en"`.

  
**Authentication (`auth`)**  
Choose one of the authentication methods. | `basic` | Username and password authentication. Provide the full Secret Manager paths for `username_secret` and `password_secret`. These secrets must contain the credentials of the [SAP service user](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#create-an-sap-service-user) created in the preparation guide. For more information, see [Basic authentication](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#auth-option-basic).  
`x509` (SNC) | Secure Network Communication authentication. For setup instructions, see [Secure Network Communication (SNC)](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#configure-snc-x509). Provide the following: 

  * `snc_name`: The SNC name.
  * `snc_partner_name`: The SNC identity of the SAP Application Server.
  * `snc_qop`: (Optional) The Quality of Protection level required by the SAP server, for example, `3` for end-to-end data privacy and payload encryption.
  * `x509_cert_secret`: (Optional) The full Secret Manager path to the secret containing the `collector_cert.crt` file. For more information, see [Store SNC artifacts in Secret Manager](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#store-snc-artifacts).

  
**Log Sources (`log_sources`)**  
Defines logs and frequency. | `log_type` | The type of log to ingest. Options include: 

  * `SAP_SECURITY_AUDIT`
  * `SAP_CHANGE_DOCUMENT`

For more information, see [Review supported log sources](https://docs.cloud.google.com/sap/docs/secops/plan-log-ingestion#review-supported-log-sources).   
`interval` | The polling frequency for this specific log source, for example, `"30s"`.  
`change_document_object_classes` | (Optional) Used only for `SAP_CHANGE_DOCUMENT`. A list of specific SAP object classes to track, for example, `["MATERIAL", "USER"]`.  
**Global Collector Settings**  
Applied to the entire instance. | `bindplane_host` | The hostname or IP address of your Bindplane agent, such as `localhost` or `10.0.0.5`. We recommend deploying Bindplane agent on the same host as Application Telemetry Collector. In this configuration, set the `bindplane_host` value to `localhost`.  
`bindplane_port` | The port number the Bindplane server listens on. Default is `4317`.  
`heartbeat_enabled` | A boolean, which is `true` or `false`, to toggle a "stay-alive" metric.  
`heartbeat_interval` | How often the heartbeat metric is sent to Monitoring through Bindplane. Must be a string followed by "s", for example, `"30s"`. Defaults to `60s`.  
`heartbeat_metric_name` | (Optional) The name that appears in your monitoring dashboard for this heartbeat, for example, `sap_collector_status`. Defaults to `sap_appl_telemetry_collector_heartbeat`.  
`jco_pse_secret` | The full Secret Manager path to the secret containing the PSE file (for example, `sapcrypto.pse`). For more information, see [Store SNC artifacts in Secret Manager](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#store-snc-artifacts).  
`jco_cred_secret` | The full Secret Manager path to the secret containing the `cred_v2` file. For more information, see [Store SNC artifacts in Secret Manager](https://docs.cloud.google.com/sap/docs/secops/prepare-environment-ingestion#store-snc-artifacts).  
  
### Deploy the collector

Run the Application Telemetry Collector as a Docker container on your host machine.

#### Prepare host directory and credentials (external hosts)

If your host machine is outside Google Cloud, such as on-premises or in another cloud, then prepare the configuration directory and credentials:

  1. **Create the directory** : Create the designated configuration directory:
         
         sudo mkdir -p /etc/sap-collector
         

  2. **Prepare credentials** : For hosts outside of Google Cloud, you can provide a service account key or configure Workload Identity Federation (WIF).

     * **Service account key** : [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete) and configure the key as [application default credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) on your host. Rename the downloaded JSON key to `creds.json` and move the key to the directory: `bash sudo mv /path/to/downloaded-key.json /etc/sap-collector/creds.json`
     * **Workload Identity Federation** : [Configure Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) to authenticate using an external identity provider.



#### Run the collector container

Choose the deployment command that matches your host environment:

###  Google Cloud 

Use this command if your host runs on Google Cloud and uses an attached Service Account for authentication.
    
    
    docker run -d \
        --name sap-telemetry-collector \
        --restart always \
        --network host \
        -e COLLECTOR_GCS_BUCKET=gs://YOUR_BUCKET_NAME \
        -e LOCK_LEASE_TIMEOUT_MINUTES=LEASE_TIMEOUT \
        -e LOCK_HEARTBEAT_INTERVAL_MINUTES=HEARTBEAT_INTERVAL \
        COLLECTOR_IMAGE_PATH
    

###  External host 

Use this command if your host is outside Google Cloud. This command uses the Docker volume mount (`-v`) to link your host's `/etc/sap-collector` directory to the container's `/tmp/keys` directory, and the `GOOGLE_APPLICATION_CREDENTIALS` environment variable (`-e`) to point the collector to your `creds.json` key.
    
    
    docker run -d \
        --name sap-telemetry-collector \
        --restart always \
        --network host \
        -v /etc/sap-collector:/tmp/keys:ro \
        -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/creds.json \
        -e COLLECTOR_GCS_BUCKET=gs://YOUR_BUCKET_NAME \
        -e LOCK_LEASE_TIMEOUT_MINUTES=LEASE_TIMEOUT \
        -e LOCK_HEARTBEAT_INTERVAL_MINUTES=HEARTBEAT_INTERVAL \
        COLLECTOR_IMAGE_PATH
    

Replace the following:

  * `YOUR_BUCKET_NAME`: The name of the Cloud Storage bucket where you uploaded the SAP JCo libraries and the `collector_config.json` file. Ensure the value follows the format `gs://BUCKET_NAME` without trailing slashes or subdirectories.
  * `LEASE_TIMEOUT`: (Optional) The duration, in minutes, that the collector instance holds a lease on the lock file. If an instance stops unexpectedly, then a new instance can acquire the lock after this period expires. Default value: `5`.
  * `HEARTBEAT_INTERVAL`: (Optional) The frequency, in minutes, at which the collector renews its lease on the Cloud Storage lock file. Default value: `1`.
  * `COLLECTOR_IMAGE_PATH`: The URI of the collector image. The collector is available to download from the following regional Artifact Registry paths:

    * `us-docker.pkg.dev/sap-core-eng-products/sap-application-telemetry/google-cloud-sap-application-telemetry:TAG`
    * `europe-docker.pkg.dev/sap-core-eng-products/sap-application-telemetry/google-cloud-sap-application-telemetry:TAG`
    * `asia-docker.pkg.dev/sap-core-eng-products/sap-application-telemetry/google-cloud-sap-application-telemetry:TAG`

Replace `TAG` with the version of the collector image that you want to download, for example, `latest`. For more information about how tags work, see [Artifact Registry container concepts](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags).




To ensure that only one collector instance pulls logs at a time, the Application Telemetry Collector uses a distributed lease-lock mechanism through Cloud Storage generation preconditions. This mechanism prevents duplicate log ingestion and supports containerized deployments across multiple hosts.

If an instance stops and you start a new instance, the new instance only begins log collection after the `LOCK_LEASE_TIMEOUT_MINUTES` period expires. To skip this waiting period and start log collection immediately, manually delete the `sap_app_telemetry_collector.lock` file from the root folder of your Cloud Storage bucket.

### Install the Bindplane agent on the Application Telemetry Collector host

To forward application logs, install the Bindplane agent on the Application Telemetry Collector host by running the command generated in the Bindplane UI. For detailed instructions, see the [Bindplane agent installation guide](https://docs.bindplane.com/readme/install-your-first-collector).

To verify the installation, go to the **Agents** tab in the **Bindplane UI** and confirm that the agent is visible with a **Connected** status.

#### Configure the Bindplane gateway

Configure a gateway in the Bindplane UI to receive logs from the Application Telemetry Collector and forward them to Google SecOps.

##### Create the log forwarding configuration

Define the basic settings for the pipeline on your central Bindplane server.

  1. In the **Bindplane UI** , go to the **Configurations** tab.
  2. Click **Create Configuration**.
  3. Enter a **Name** , for example, `sap-app-logs`.
  4. Select **BDOT 1.x (Stable)** as the **Agent Type**.
  5. Select **Linux** as the **Platform**.
  6. Click **Next**.



##### Add the Bindplane gateway source

Configure an OpenTelemetry (OTLP) listener on the Bindplane server to receive logs from the Application Telemetry Collector.

  1. In the **Add Sources** stage, select the **Bindplane Gateway** source type.
  2. Enter a **Short Description**.
  3. In the **Listen Address** field, enter `0.0.0.0`.
  4. Ensure the **Port** is set to `4317` (gRPC) and ensure that your host's firewall allows traffic on this port.
  5. Click **Save**.



##### Add the Batch processor

To prevent overwhelming the Google SecOps API, batch your requests.

  1. Click **Add Processor** and select **Batch**.
  2. Use the recommended defaults, usually `8192` units or a `200ms` timeout.
  3. Click **Save**.



##### Obtain Google SecOps credentials

To securely forward logs to Google SecOps, obtain your ingestion authentication file and customer ID from the Google SecOps console.

###### Google SecOps ingestion authentication file

To download the ingestion authentication file, do the following:

  1. Open the Google SecOps console.
  2. Go to **SIEM Settings** > **Collection Agent**.
  3. Download the Google SecOps ingestion authentication file. Your next step depends on your transfer method:

     * **gRPC** : Use the downloaded ingestion authentication file.
     * **HTTPS** : Create a service account in the Google Cloud project linked to Google SecOps and assign the **Chronicle Editor** role to the service account.



###### Google SecOps customer ID

To find the customer ID, do the following:

  1. Open the Google SecOps console.
  2. Go to **SIEM Settings** > **Profile**.
  3. Copy the customer ID from the **Organization Details** section.



##### Create the Google SecOps destination in Bindplane

Set up the final destination in Bindplane to securely forward your processed logs to Google SecOps.

  1. In the **Bindplane UI** , go to the **Destinations** tab and click **Create Destination**.
  2. Select **Google SecOps** as the destination type.
  3. Enter a **Name** , for example, `secops-destination`.
  4. In the **Customer ID** field, paste your Google SecOps customer ID.
  5. In the **Credentials** field, click **Upload** and select the ingestion authentication file you downloaded, or paste the file content directly.
  6. Click **Save**.



##### Add the Monitoring destination

To monitor the health of your collectors within Monitoring, ensure that heartbeat metrics are enabled and routed through the gateway.

  1. Click **Add Destination** and select **Google Cloud Monitoring**.
  2. In the **Project ID** field, enter your Google Cloud project ID.
  3. In the **Authentication** field, select **Auto** if your Bindplane server is running on a Google Cloud instance. Otherwise, provide your Service Account credentials.
  4. Click **Save**.



#### Deploy the configuration to agents

Once the configuration is ready, assign the configuration to your installed Bindplane agents.

  1. In the **Bindplane UI** , go to the **Configurations** tab.
  2. Select your new configuration, for example, `sap-app-logs`.
  3. Click **Add Agents**.
  4. Select the Bindplane agent on the Application Telemetry Collector host and click **Apply**.



### Confirm your log ingestion

To ensure the setup is working correctly, follow the verification steps in [Confirm your log ingestion](https://docs.cloud.google.com/sap/docs/secops/ingest-self-managed-sap-logs#confirm-ingestion-infra).

When verifying application-layer logs in Google SecOps, use a UDM query to filter by your specific log type, for example, `metadata.log_type = "SAP_CHANGE_DOCUMENT"`. For more information, see [Search and filter SAP logs](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats#search-and-filter-sap-logs).

## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

## What's next

  * [Detect and investigate threats in SAP logs](https://docs.cloud.google.com/sap/docs/secops/detect-sap-threats)
  * [SAP to UDM field mapping reference](https://docs.cloud.google.com/sap/docs/secops/udm-mapping-overview)
  * [Troubleshoot SAP log ingestion](https://docs.cloud.google.com/sap/docs/secops/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
