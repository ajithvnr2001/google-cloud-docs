---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/nginx/
title: nginx \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:04.823938+00:00
---

# nginx  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/nginx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  nginx Stay organized with collections  Save and categorize content based on your preferences. 

The nginx integration collects connection metrics and access logs. Connection metrics capture the current state of the connection: active, reading, or waiting. Access logs are parsed for their connection details, which include fields mapped to request, client, server, and message.

For more information about nginx, see the [nginx documentation](https://nginx.org/).

## Prerequisites

To collect nginx telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics, install version 2.1.0 or higher.
  * For logs, install version 2.1.0 or higher.



This integration supports nginx versions 1.18 and 1.20.

## Configure your nginx instance

You must enable the `stub_status` module in the nginx configuration file to set up a locally reachable URL, for example, `http://www.example.com/nginx_status` for the status page. To enable the `stub_status` module, complete the following steps:

  1. Edit the `status.conf` file, or create the file if it doesn't exist. You can find this file in the nginx configuration directory, typically found at `/etc/nginx/conf.d`.

  2. Add the following lines to the `server` section:
         
         location /nginx_status {
             stub_status on;
             access_log off;
             allow 127.0.0.1;
             deny all;
         }
         

Your configuration file might look like the following example:
         
         server {
            listen 80;
            server_name 127.0.0.1;
            location /nginx_status {
                stub_status on;
                access_log off;
                allow 127.0.0.1;
                deny all;
            }
            location / {
                root /dev/null;
            }
         }
         

  3. Reload the nginx configuration.
         
         sudo service nginx reload
         




You can run the following command to automate the previous steps. It creates a `status.conf` file if it doesn't exist or overwrites the existing one if it does exist. The command turns on `stub_status`, reloads nginx, and verifies that the expected information is exposed through the endpoint.
    
    
    sudo tee /etc/nginx/conf.d/status.conf > /dev/null << EOF
    server {
        listen 80;
        server_name 127.0.0.1;
        location /nginx_status {
            stub_status on;
            access_log off;
            allow 127.0.0.1;
            deny all;
        }
        location / {
           root /dev/null;
        }
    }
    EOF
    sudo service nginx reload
    curl http://127.0.0.1:80/nginx_status
    

The sample output is:
    
    
    Active connections: 1
    server accepts handled requests
     23 23 74
    Reading: 0 Writing: 1 Waiting: 0
    

**Note:** `127.0.0.1` can be replaced with the real server name, for example, `server_name mynginx.domain.com`. The curl command to verify would be `curl http://mynginx.domain.com:80/nginx_status`.

Alternately, instead of using a separate `status.conf` file, you can also directly embed the lines to the main `nginx.conf` file, which is typically located in one of the following directories: `/etc/nginx`, `/usr/local/nginx/conf`, or `/usr/local/etc/nginx`.

## Configure the Ops Agent for nginx

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from nginx instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for nginx:
    
    
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
    
    # Configure the Ops Agent.
    sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
    metrics:
      receivers:
        nginx:
          type: nginx
          stub_status_url: http://127.0.0.1:80/nginx_status
      service:
        pipelines:
          nginx:
            receivers:
              - nginx
    logging:
      receivers:
        nginx_access:
          type: nginx_access
        nginx_error:
          type: nginx_error
      service:
        pipelines:
          nginx:
            receivers:
              - nginx_access
              - nginx_error
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

To ingest logs from nginx, you must create a receiver for the logs that nginx produces and then create a pipeline for the new receiver.

To configure a receiver for your `nginx_access` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/nginx/access.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `nginx_access`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
To configure a receiver for your `nginx_error` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/nginx/error.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `nginx_error`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `nginx_access` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`httpRequest` | object | See [`HttpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest)  
`jsonPayload.host` | string | Contents of the Host header (usually not reported by nginx)  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.user` | string | Authenticated username for the request  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `nginx_error` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.client` | string | Client IP address (optional)  
`jsonPayload.connection` | number | Connection ID  
`jsonPayload.host` | string | Host header (optional)  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message  
`jsonPayload.pid` | number | The process ID issuing the log  
`jsonPayload.referer` | string | Referer header (optional)  
`jsonPayload.request` | string | Original HTTP request (optional)  
`jsonPayload.server` | string | Nginx server name (optional)  
`jsonPayload.subrequest` | string | Nginx subrequest (optional)  
`jsonPayload.tid` | number | Thread ID where the log originated  
`jsonPayload.upstream` | string | Upstream request URI (optional)  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from nginx, you must create a receiver for the metrics that nginx produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `nginx` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`server_status_url` | `http://localhost/status` | The URL exposed by the nginx stub status module.  
`type` |  | This value must be `nginx`.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the nginx instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/nginx.connections_accepted`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/nginx.connections_current`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/nginx.connections_handled`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/nginx.requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
  
## Verify the configuration

This section describes how to verify that you correctly configured the nginx receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that nginx logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("nginx_access") OR log_id("nginx_error"))
         




To verify that nginx metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/nginx.requests", monitored_resource="gce_instance"}
         




## View dashboard

To view your nginx metrics, you must have a chart or dashboard configured. The nginx integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for nginx and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The nginx integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for nginx and click **View Details**. 
  3. Select the **Alerts** tab. This tab provides descriptions of available alerting policies and provides an interface for installing them.
  4. Install alerting policies. Alerting policies need to know where to send notifications that the alert has been triggered, so they require information from you for installation. To install alerting policies, do the following: 
     1. From the list of available alerting policies, select those that you want to install.
     2. In the **Configure notifications** section, select one or more notification channels. You have the option to disable the use of notification channels, but if you do, then your alerting policies fire silently. You can check their status in Monitoring, but you receive no notifications.

For more information about notification channels, see [Manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

     3. Click **Create Policies**.



For more information about alerting policies in Cloud Monitoring, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Troubleshooting

On most distributions, nginx comes with `ngx_http_stub_status_module` enabled. You can check if the module is enabled by running the following command:
    
    
    sudo nginx -V 2>&1 | grep -o with-http_stub_status_module
    

The expected output is `with-http_stub_status_module`, which means the module is enabled. In rare cases, if the command returns no output, you must compile nginx from source with the `-with-http_stub_status_module` following the nginx public documentation.

## What's next

For a walkthrough on how to use Ansible to install the Ops Agent, configure a third-party application, and install a sample dashboard, see the [ Install the Ops Agent to troubleshoot third-party applications](https://www.youtube.com/watch?v=GQgNygd-XJU&t=7s) video.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
