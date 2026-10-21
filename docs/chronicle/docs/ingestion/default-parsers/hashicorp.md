---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hashicorp/
title: Collect HashiCorp Vault audit logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:28:56.883766+00:00
---

# Collect HashiCorp Vault audit logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hashicorp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect HashiCorp Vault audit logs

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document explains how you can ingest HashiCorp Vault audit logs to Google Security Operations using Bindplane.

HashiCorp Vault is a secrets management and data protection platform that provides secure storage, dynamic secrets generation, data encryption, and identity-based access control. Vault produces audit logs that record all requests and responses to Vault, including authentication, secret access, and policy changes. These audit logs can be forwarded using syslog to a SIEM for security monitoring and compliance.

## Before you begin

Make sure you have the following prerequisites:

  * A Google SecOps instance.
  * Windows Server 2016 or later, or Linux host with `systemd`.
  * Network connectivity between the Bindplane agent and the HashiCorp Vault server.
  * If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements.
  * Privileged access to the HashiCorp Vault server (root token or sufficient policy permissions to enable audit devices).



## Get Google SecOps credentials for the Bindplane agent

To authenticate the Bindplane agent to Google SecOps, choose one of the following methods:

  * **New deployments** : Use the Chronicle API (Option 1).
  * **Legacy deployments** : Continue using the ingestion authentication file (Option 2) until the Ingestion API is discontinued on July 20, 2027.



### Option 1: Create a service account for the Chronicle API (recommended)

  1. Sign in to the [Google Cloud console](https://console.cloud.google.com/) and select the Google Cloud project that is linked to your Google SecOps instance.
  2. Go to **IAM & Admin > Service Accounts**.
  3. Click **Create service account**.
  4. Provide the following configuration details: 
     * **Service account name** : Enter a name for the account (for example, `bindplane-ingest`).
     * **Service account description** : Enter a description (for example, `Bindplane agent log ingestion`).
  5. Click **Create and continue**.
  6. In the **Grant this service account access to project** section, click **Select a role** and select **Chronicle Editor**.
  7. Click **Continue** , and then click **Done**.
  8. Click the service account you created, and then go to the **Keys** tab.
  9. Click **Add key > Create new key**.
  10. Select **JSON** and click **Create**. The key file is downloaded to your computer.
  11. Save the key file as `ingestion-auth.json` in the Bindplane collector directory (`/opt/observiq-otel-collector/ingestion-auth.json` on Linux or `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json` on Windows), or update `creds_file_path` in `config.yaml` to match the path where you save it.
  12. Go to **IAM & Admin > Settings** and copy the **Project number**. You'll need it for the exporter configuration.

**Note:** The JSON key is a credential. Restrict access to the file on the Bindplane host and rotate the key according to your organization's policy.

### Option 2: Download the ingestion authentication file (legacy)

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Collection Agents**.
  3. Download the **ingestion authentication file**.
  4. Save the file securely on the system where the Bindplane agent will be installed.

**Note:** This file authenticates the agent to the legacy Ingestion API (`malachiteingestion-pa.googleapis.com`), which Google has scheduled for end of life on July 20, 2027. Plan to move to Option 1 before that date.

## Get Google SecOps customer ID

  1. Sign in to the Google SecOps console.
  2. Go to **SIEM Settings > Profile**.
  3. Copy and save the **Customer ID** from the **Organization Details** section.



## Install the Bindplane agent

Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.

### Windows installation

  1. Open **Command Prompt** or **PowerShell** as an administrator.
  2. Run the following command:
         
         msiexec /i "[https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi](https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi)" /quiet
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sc query observiq-otel-collector
         




The service should show as **RUNNING**.

### Linux installation

  1. Open a terminal with root or sudo privileges.
  2. Run the following command:
         
         sudo sh -c "$(curl -fsSlL [https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh](https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh))" install_unix.sh
         

  3. Wait for the installation to complete.

  4. Verify the installation by running:
         
         sudo systemctl status observiq-otel-collector
         




The service should show as **active (running)**.

### Additional installation resources

For additional installation options and troubleshooting, see the [Bindplane agent installation guide](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#install_the_bindplane_agent).

**Note:** The Chronicle API exporter configuration requires Bindplane collector v1.106.0 or later. The previous commands install the latest release. If you're updating an existing installation, upgrade the collector before changing the configuration.

## Configure the Bindplane agent to ingest syslog and send to Google SecOps

### Locate the configuration file

  * **Linux:**
        
        sudo nano /opt/observiq-otel-collector/config.yaml
        

  * **Windows:**
        
        notepad "C:\Program Files\observIQ OpenTelemetry Collector\config.yaml"
        




### Edit the configuration file

  * Replace the entire contents of `config.yaml` with the following configuration:
        
        receivers:
          tcplog:
            listen_address: "0.0.0.0:1514"
        
        exporters:
          chronicle/vault:
            protocol: https
            # Region of your instance, for example us, europe, asia-southeast1
            location: <LOCATION>
            # Project number of the Google Cloud project linked to the instance
            project: '<PROJECT_NUMBER>'
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: chronicle.googleapis.com
            log_type: HASHICORP
            raw_log_field: body
            ingestion_labels:
              env: production
        
        service:
          pipelines:
            logs/vault_to_chronicle:
              receivers:
                - tcplog
              exporters:
                - chronicle/vault
        




### Configuration parameters

Replace the following placeholders:

  * **Receiver configuration:**

    * `listen_address`: IP address and port to listen on. Use `0.0.0.0` to listen on all interfaces. Port `1514` is recommended to avoid requiring root privileges on Linux.
  * **Exporter configuration:**

    * `creds_file_path`: Full path to the service account JSON key file (Option 1): 
      * **Linux** : `/opt/observiq-otel-collector/ingestion-auth.json`
      * **Windows** : `C:\Program Files\observIQ OpenTelemetry Collector\ingestion-auth.json`
    * `customer_id`: Your Google SecOps customer ID.
    * `location`: Replace `<LOCATION>` with the region of your Google SecOps instance (for example, `us`, `europe`, or `asia-southeast1`). The exporter prefixes `chronicle.googleapis.com` with this value. See [Regional Endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=us#regional-service-endpoint) for the complete list.
    * `project`: Replace `<PROJECT_NUMBER>` with the project number from **IAM & Admin > Settings**.
    * `endpoint`: Keep set to `chronicle.googleapis.com`.
    * `ingestion_labels`: Optional labels in YAML format (for example, `env: production`).



### Legacy ingestion API exporter

  * If you use the ingestion authentication file from Option 2, replace the `exporters` block with the following. Set `creds_file_path` to the path to the ingestion authentication file, and if your instance is outside the US, replace `malachiteingestion-pa.googleapis.com` with your [regional endpoint](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api#regional-endpoints) (for example, `europe-malachiteingestion-pa.googleapis.com`).
        
        exporters:
          chronicle/vault:
            compression: gzip
            creds_file_path: '/opt/observiq-otel-collector/ingestion-auth.json'
            customer_id: 'your-customer-id-here'
            endpoint: malachiteingestion-pa.googleapis.com
            log_type: HASHICORP
            raw_log_field: body
            ingestion_labels:
              env: production
        


**Note:** This exporter will stop working when the Ingestion API is discontinued on July 20, 2027.

### Save the configuration file

After editing, save the file:

  * **Linux** : Press `Ctrl+O`, then `Enter`, then `Ctrl+X`
  * **Windows** : Click **File > Save**



## Restart the Bindplane agent to apply the changes

To restart the Bindplane agent in Linux: 

  1. Run the following command:
         
         sudo systemctl restart observiq-otel-collector
         

  2. Verify the service is running:
         
         sudo systemctl status observiq-otel-collector
         

  3. Check logs for errors:
         
         sudo journalctl -u observiq-otel-collector -f
         




To restart the Bindplane agent in Windows:

  1. Choose one of the following options:

     * Command Prompt or PowerShell as administrator:
    
    net stop observiq-otel-collector && net start observiq-otel-collector
    

     * Services console: 
       1. Press `Win+R`, type `services.msc`, and press Enter.
       2. Locate **observIQ OpenTelemetry Collector**.
       3. Right-click and select **Restart**.
  2. Verify the service is running:
         
         sc query observiq-otel-collector
         

  3. Check logs for errors:
         
         type "C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log"
         




## Configure HashiCorp Vault audit log forwarding via syslog

Vault audit devices log all requests and responses. You can enable a syslog audit device to forward audit logs to the Bindplane agent.

### Enable syslog audit device

  1. Open a terminal with access to the Vault CLI and a valid Vault token.
  2. Run the following command to enable the syslog audit device:
         
         vault audit enable syslog tag="vault" facility="AUTH"
         

**Note:** The `tag` parameter sets the syslog tag for all Vault audit log messages. The `facility` parameter specifies the syslog facility (for example, `AUTH`, `LOCAL0` through `LOCAL7`).
  3. Verify the audit device is enabled:
         
         vault audit list
         




The output should show the syslog audit device as **enabled**.

### Configure syslog forwarding to Bindplane agent

After enabling the Vault syslog audit device, configure the system syslog daemon (rsyslog or syslog-ng) to forward Vault audit logs to the Bindplane agent.

#### Option - rsyslog configuration

  1. Create a new rsyslog configuration file:
         
         sudo nano /etc/rsyslog.d/50-vault-forward.conf
         

  2. Add the following configuration:
         
         # Forward Vault audit logs to Bindplane agent
         if $programname == 'vault' then @@BINDPLANE_IP:1514
         

Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.

**Note:** `@@` specifies TCP transport. Use `@` for UDP transport.
  3. Restart rsyslog:
         
         sudo systemctl restart rsyslog
         




#### Option - syslog-ng configuration

  1. Edit the syslog-ng configuration file:
         
         sudo nano /etc/syslog-ng/conf.d/vault-forward.conf
         

  2. Add the following configuration:
         
         destination d_bindplane {
             network("BINDPLANE_IP" port(1514) transport("tcp"));
         };
         
         filter f_vault {
             program("vault");
         };
         
         log {
             source(s_src);
             filter(f_vault);
             destination(d_bindplane);
         };
         

Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.

  3. Restart syslog-ng:
         
         sudo systemctl restart syslog-ng
         




### Alternative - file-based audit with log forwarder

If syslog audit is not preferred, you can enable a file audit device and forward the file contents:

  1. Enable file audit device:
         
         vault audit enable file file_path=/var/log/vault/audit.log
         

  2. Configure rsyslog to monitor and forward the file:
         
         sudo nano /etc/rsyslog.d/50-vault-file-forward.conf
         
         
         module(load="imfile")
         input(type="imfile"
             File="/var/log/vault/audit.log"
             Tag="vault-audit"
             Severity="info"
             Facility="auth")
         
         if $syslogtag == 'vault-audit' then @@BINDPLANE_IP:1514
         

Replace `BINDPLANE_IP` with the IP address of the Bindplane agent host.

  3. Restart rsyslog:
         
         sudo systemctl restart rsyslog
         




### Verify log forwarding

  1. Perform a Vault operation (for example, login or read a secret):
         
         vault login token=<YOUR_TOKEN>
         

  2. Check the Bindplane agent logs to confirm logs are being received.




For more information, see the [HashiCorp Vault audit devices documentation](https://developer.hashicorp.com/vault/docs/audit).

## UDM mapping table

Log Field | UDM Mapping | Logic  
---|---|---  
`auth.client_token` | `network.session_id` | Value taken from `auth.client_token` (hashed).  
`auth.display_name` | `principal.user.user_display_name` | Value taken from `auth.display_name`.  
`auth.metadata.role_name` | `principal.user.attribute.roles.name` | Value taken from `auth.metadata.role_name`.  
`auth.policies` | `principal.user.attribute.permissions.name` | Values taken from `auth.policies` array.  
`auth.token_type` | `additional.fields` | Value taken from `auth.token_type` and added with key `token_type`.  
`request.id` | `metadata.product_log_id` | Value taken from `request.id`.  
`request.operation` | `metadata.product_event_type` | Value taken from `request.operation`.  
`request.path` | `target.resource.name` | Value taken from `request.path`.  
`request.remote_address` | `principal.ip` | Value taken from `request.remote_address`.  
`request.namespace.id` | `target.namespace` | Value taken from `request.namespace.id`.  
`response.auth.client_token` | `network.session_id` | Value taken from response `client_token` (hashed).  
`type` | `metadata.product_event_type` | Appended to operation (for example, `request` or `response`).  
`time` | `metadata.event_timestamp` | Parsed as RFC 3339 timestamp.  
`error` | `security_result.description` | Value taken from `error` if present.  
| `metadata.vendor_name` | Set to **HashiCorp**.  
| `metadata.product_name` | Set to **Vault**.  
| `metadata.event_type` | Set to **USER_RESOURCE_ACCESS** for secret operations, **USER_LOGIN** for auth operations, **GENERIC_EVENT** otherwise.  
`response.auth.metadata.username` | `event.idm.read_only_udm.target.user.userid` | Mapped from changelog  
`appname` | `event.idm.read_only_udm.target.application` | Mapped from changelog  
`priority` | `event.idm.read_only_udm.security_result.priority_details` | Mapped from changelog  
`proc_id` | `event.idm.read_only_udm.observer.process.pid` | Mapped from changelog  
`auth.policies` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`auth.token_policies` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request.policy_override` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.admin_password` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.admin_token` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.admin_user` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.certificate` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.check_url` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.keystore` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.keystore_password` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`response.data.private_key` | `event.idm.read_only_udm.target.resource.attribute.labels` | Mapped from changelog  
`type` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`auth.identity_policies` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`request.data` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`facility` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`task` | `event.idm.read_only_udm.additional.fields` | Mapped from changelog  
`jsonPayload.auth.policy_results.granting_policies.type", "jsonPayload.auth.policy_results.granting_policies.name", and "jsonPayload.auth.policy_results.granting_policies.namespace_id` | `additional.fields` | Mapped from changelog  
`jsonPayload.request.namespace.id` | `target.namespace` | Mapped from changelog  
`jsonPayload.cos.googleapis.com/container_id", "jsonPayload.cos.googleapis.com/container_name", "jsonPayload.cos.googleapis.com/stream` | `additional.fields` | Mapped from changelog  
`resource.labels.instance_id` | `principal.resource.product_object_id` | Mapped from changelog  
`principal.resource.attribute.cloud.availability_zone` | `resource.labels.zone` | Mapped from changelog  
`logName` | `security_result.category_details` | Mapped from changelog  
`resource.labels.namespace_name` | `target.namespace` | Mapped from changelog  
`resource.labels.pod_name", "resource.labels.container_name` | `additional.fields` | Mapped from changelog  
`resource.labels.project_id` | `target.cloud.project.name` | Mapped from changelog  
`resource.labels.location` | `target.location.name` | Mapped from changelog  
`insertId` | `metadata.product_log_id` | Mapped from changelog  
`labels.k8s-pod/app_kubernetes_io/instance", "labels.k8s-pod/app_kubernetes_io/name", "labels.k8s-pod/component", "labels.k8s-pod/helm_sh/chart", "labels.k8s-pod/controller-revision-hash", "labels.k8s-pod/vault-initialized", "labels.k8s-pod/vault-version", "labels.k8s-pod/vault-sealed", "labels.k8s-pod/vault-perf-standby", and "labels.k8s-pod/vault-active` | `target.resource.attribute.labels` | Mapped from changelog  
`labels.compute.googleapis.com/resource_name` | `target.resource.name` | Mapped from changelog  
`status` | `network.http.response_code` | Mapped from changelog  
`runner` | `principal.user.userid` | Mapped from changelog  
`job_id", "job_status` | `additional.fields` | Mapped from changelog  
`host` | `observer.hostname` | Mapped from changelog  
`cluster` | `observer.resource.name` | Mapped from changelog  
`cluster` | `observer.resource.resource_type` | Mapped from changelog  
  
## Change Log

[View the Change Log for this parser](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hashicorp-changelog)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
