---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/vault/
title: Hashicorp Vault \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:05.788927+00:00
---

# Hashicorp Vault  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Hashicorp Vault Stay organized with collections  Save and categorize content based on your preferences. 

Vault is an identity-based secrets and encryption management system. This integration collects Vault's audit logs. The integration also collects token, memory, and storage metrics.

For more information about Vault, see the [Hashicorp Vault documentation](https://www.vaultproject.io/).

## Prerequisites

To collect Vault telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index):

  * For metrics, install version 2.18.2 or higher.
  * For logs, install version 2.18.1 or higher.



This integration supports Vault version 1.6+.

## Configure your Vault instance

To collect telemetry from your Vault instance, you must set the `prometheus_retention_time` field to a non-zero value in your HCL or JSON Vault configuration file.
    
    
    Full configuration options can be found at https://www.vaultproject.io/docs/configuration
    telemetry {
      prometheus_retention_time = "10m"
      disable_hostname = false
    }
    

Additionally, a root user is required to enable audit-log collection and to create a prometheus-metrics ACL policy. A root token is used to add a policy that has read capabilities to the `/sys/metrics` endpoint. This policy is used to create a Vault token with sufficient permission to collect Vault metrics.

If you are initializing Vault for the first time, then you can use the following script to generate a root token. Otherwise, see [Generate Root Tokens Using Unseal Keys](https://developer.hashicorp.com/vault/tutorials/operations/generate-root) for information about generating a root token.
    
    
    export VAULT_ADDR=http://localhost:8200
    # Create simple Vault initialization with 1 key share and a key threshold of 1.
    vault operator init -key-shares=1 -key-threshold=1 | head -n3 | cat > .vault-init
    VAULT_KEY=$(grep 'Unseal Key 1'  .vault-init | awk '{print $NF}')
    VAULT_TOKEN=$(grep 'Initial Root Token:' .vault-init | awk '{print $NF}')
    export VAULT_TOKEN
    vault operator unseal $VAULT_KEY
    
    # Enable audit logs.
    vault audit enable file file_path=/var/log/vault_audit.log
    
    # Create Prometheus ACL policy to access metrics endpoint.
    vault policy write prometheus-metrics - << EOF
    path "/sys/metrics" {
      capabilities = ["read"]
    }
    EOF
    
    # Create an example token with the prometheus-metrics policy to access Vault metrics.
    # This token is used as `$VAULT_TOKEN` in your Ops Agent configuration for Vault.
    vault token create -field=token -policy prometheus-metrics > prometheus-token
    

## Configure the Ops Agent for Vault

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from Vault instances, and [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Vault:
    
    
    # Configures Ops Agent to collect telemetry from the app. You must restart the agent for the configuration to take effect.
    
    set -e
    
    # Check if the file exists
    if [ ! -f /etc/google-cloud-ops-agent/config.yaml ]; then
      # Create the file if it doesn't exist.
      sudo mkdir -p /etc/google-cloud-ops-agent
      sudo touch /etc/google-cloud-ops-agent/config.yaml
    fi
    
    # Create a back up of the existing file so existing configurations are not lost.
    sudo cp /etc/google-cloud-ops-agent/config.yaml /etc/google-cloud-ops-agent/config.yaml.bak
    
    # Create a Vault token that has read capabilities to /sys/metrics policy.
    # For more information see: https://developer.hashicorp.com/vault/tutorials/monitoring/monitor-telemetry-grafana-prometheus?in=vault%2Fmonitoring#define-prometheus-acl-policy
    VAULT_TOKEN=$(cat prometheus-token)
    
    
    sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
    metrics:
      receivers:
        vault:
          type: vault
          token: $VAULT_TOKEN
          endpoint: 127.0.0.1:8200
      service:
        pipelines:
          vault:
            receivers:
              - vault
    logging:
      receivers:
        vault_audit:
          type: vault_audit
          include_paths: [/var/log/vault_audit.log]
      service:
        pipelines:
          vault:
            receivers:
              - vault_audit
    EOF
    

For these changes to take effect, you must restart the Ops Agent:

### Linux

  1. To restart the agent, run the following command on your instance: 
         
         sudo systemctl restart google-cloud-ops-agent
         

  2. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         sudo systemctl status "google-cloud-ops-agent*"
         




### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows. 
  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**
  3. To restart the agent, run the following PowerShell command: 
         
         Restart-Service google-cloud-ops-agent -Force
         

  4. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         Get-Service google-cloud-ops-agent*
         




### Configure logs collection

To ingest logs from Vault, you must create a receiver for the logs that Vault produces and then create a pipeline for the new receiver.

To configure a receiver for your `vault_audit` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` |  | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | The value must be `vault_audit`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `vault_audit` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.auth` | struct |   
`jsonPayload.auth.accessor` | string | This is an HMAC of the client token accessor.  
`jsonPayload.auth.client_token` | string | This is an HMAC of the client's token ID.  
`jsonPayload.auth.display_name` | string | This is the display name set by the auth method role or explicitly at secret creation time.  
`jsonPayload.auth.entity_id` | string | This is a token entity identifier.  
`jsonPayload.auth.metadata` | object | This will contain a list of metadata key/value pairs associated with the client_token.  
`jsonPayload.auth.policies` | object | This will contain a list of policies associated with the client_token.  
`jsonPayload.auth.token_type` | string |   
`jsonPayload.error` | string | If an error occurred with the request, the error message is included in this field's value.  
`jsonPayload.request` | struct |   
`jsonPayload.request.client_token` | string | This is an HMAC of the client's token ID.  
`jsonPayload.request.client_token_accessor` | string | This is an HMAC of the client token accessor.  
`jsonPayload.request.data` | object | The data object will contain secret data in key/value pairs.  
`jsonPayload.request.headers` | object | Additional HTTP headers specified by the client as part of the request.  
`jsonPayload.request.id` | string | This is the unique request identifier.  
`jsonPayload.request.namespace.id` | string |   
`jsonPayload.request.operation` | string | This is the type of operation which corresponds to path capabilities and is expected to be one of: `create`, `read`, `update`, `delete`, or `list`.  
`jsonPayload.request.path` | string | The requested Vault path for operation.  
`jsonPayload.request.policy_override` | boolean | This is `true` when a soft-mandatory policy override was requested.  
`jsonPayload.request.remote_address` | string | The IP address of the client making the request.  
`jsonPayload.request.wrap_ttl` | string | If the token is wrapped, this displays configured wrapped TTL value as numeric string.  
`jsonPayload.response` | struct |   
`jsonPayload.response.data.accessor` | string | This is an HMAC of the client token accessor.  
`jsonPayload.response.data.creation_time` | string | RFC 3339 format timestamp of the token's creation.  
`jsonPayload.response.data.creation_ttl` | string | Token creation TTL in seconds.  
`jsonPayload.response.data.display_name` | string | This is the display name set by the auth method role or explicitly at secret creation time.  
`jsonPayload.response.data.entity_id` | string | This is a token entity identifier.  
`jsonPayload.response.data.expire_time` | string | RFC 3339 format timestamp representing the moment this token will expire.  
`jsonPayload.response.data.explicit_max_ttl` | string | Explicit token maximum TTL value as seconds ("0" when not set).  
`jsonPayload.response.data.id` | string | This is the unique response identifier.  
`jsonPayload.response.data.issue_time` | string | RFC 3339 format timestamp.  
`jsonPayload.response.data.num_uses` | number | If the token is limited to a number of uses, that value will be represented here.  
`jsonPayload.response.data.orphan` | boolean | Boolean value representing whether the token is an orphan.  
`jsonPayload.response.data.path` | string | The requested Vault path for operation.  
`jsonPayload.response.data.policies` | object | This will contain a list of policies associated with the client_token.  
`jsonPayload.response.data.renewable` | boolean | Boolean value representing whether the token is an orphan.  
`jsonPayload.type` | string | The type of audit log.  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Vault, you must create a receiver for the metrics that Vault produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `vault` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`ca_file` |  | Path to the CA certificate. As a client, this verifies the server certificate. If empty, the receiver uses the system root CA.  
`cert_file` |  | Path to the TLS certificate to use for mTLS-required connections.  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `localhost:8200` | The 'hostname:port' used by Vault.  
`insecure` | `true` | Sets whether or not to use a secure TLS connection. If set to `false`, then TLS is enabled.  
`insecure_skip_verify` | `false` | Sets whether or not to skip verifying the certificate. If `insecure` is set to `true`, then the `insecure_skip_verify` value is not used.  
`key_file` |  | Path to the TLS key to use for mTLS-required connections.  
`metrics_path` | `/v1/sys/metrics` | The path for metrics collection.  
`token` | `localhost:8200` | Token used for authentication.  
`type` |  | This value must be `vault`.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Vault instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/vault.audit.request.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.audit.response.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.core.leader.duration`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/vault.core.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `cluster`  
`workload.googleapis.com/vault.memory.usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/vault.storage.operation.delete.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.delete.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.get.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.get.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.list.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.list.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.put.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.storage.operation.put.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `storage`  
`workload.googleapis.com/vault.token.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `cluster`  
`namespace`  
`workload.googleapis.com/vault.token.lease.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.token.renew.time`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/vault.token.revoke.time`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
## Verify the configuration

This section describes how to verify that you correctly configured the Vault receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Vault logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("vault_audit")
         




To verify that Vault metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/vault.memory.usage", monitored_resource="gce_instance"}
         




## View dashboard

To view your Vault metrics, you must have a chart or dashboard configured. The Vault integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

You can also view static previews of dashboards without installing the integration.

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab, and then choose the **Integrations** category.
  3. Click the name of the dashboard you want to view. 



If you have configured an integration but the dashboard has not been installed, then check that the Ops Agent is running. When there is no metric data for a chart in the dashboard, installation of the dashboard fails. After the Ops Agent begins collecting metrics, the dashboard is installed for you.

To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Compute Engine** deployment-platform filter.
  3. Locate the entry for Vault and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Vault integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Vault and click **View Details**. 
  3. Select the **Alerts** tab. This tab provides descriptions of available alerting policies and provides an interface for installing them.
  4. Install alerting policies. Alerting policies need to know where to send notifications that the alert has been triggered, so they require information from you for installation. To install alerting policies, do the following: 
     1. From the list of available alerting policies, select those that you want to install.
     2. In the **Configure notifications** section, select one or more notification channels. You have the option to disable the use of notification channels, but if you do, then your alerting policies fire silently. You can check their status in Monitoring, but you receive no notifications.

For more information about notification channels, see [Manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

     3. Click **Create Policies**.



For more information about alerting policies in Cloud Monitoring, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## What's next

For a walkthrough on how to use Ansible to install the Ops Agent, configure a third-party application, and install a sample dashboard, see the [ Install the Ops Agent to troubleshoot third-party applications](https://www.youtube.com/watch?v=GQgNygd-XJU&t=7s) video.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
