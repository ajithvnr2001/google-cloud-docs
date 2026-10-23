---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/jvm/
title: JVM \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:19.878801+00:00
---

# JVM  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/jvm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  JVM Stay organized with collections  Save and categorize content based on your preferences. 

The JVM integration collects JVM metrics exposed through [Java Management Extensions (JMX)](https://www.oracle.com/java/technologies/javase/javamanagement.html). The integration primarily collects metrics on memory and garbage collection. Additional runtime metrics, such as thread count and classes loaded, are also available.

For more information about JVM, see the [JVM documentation](https://docs.oracle.com/javase/specs/index.html).

## Prerequisites

To collect JVM telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index):

  * For metrics, install version 2.2.0 or higher.

**Note:** The `PATH` variable that includes the JVM executable must be available to the `google-cloud-ops-agent-opentelemetry-collector` service. If you didn't install the JDK by using a package manager, or if you installed it into a non-standard location, then you can modify the systemd environment to include the path by using the `systemctl set-environment` command. 

This integration supports JVM versions Java 16 and Java 11.

## Configure your JVM instance

To expose a JMX endpoint, you must set the `com.sun.management.jmxremote.port` system property when starting the JVM. We also recommend setting the `com.sun.management.jmxremote.rmi.port` system property to the same port.

To expose a JMX endpoint remotely, you must also set the `java.rmi.server.hostname` system property.

To set system properties by using command-line arguments, prepend the property name with `-D` when starting the JVM.

For example, to set `com.sun.management.jmxremote.port` to port `9999`, specify the following when starting the JVM:
    
    
    -Dcom.sun.management.jmxremote.port=9999
    

## Configure the Ops Agent for JVM

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from JVM instances, and [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for JVM:
    
    
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
        jvm:
          type: jvm
          endpoint: service:jmx:rmi:///jndi/rmi://127.0.0.1:9010/jmxrmi
      service:
        pipelines:
          jvm:
            receivers:
              - jvm
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
         




### Configure metrics collection

To ingest metrics from JVM, you must create a receiver for the metrics that JVM produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `jvm` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `localhost:9999` | The [JMX Service URL](https://docs.oracle.com/javase/8/docs/api/javax/management/remote/JMXServiceURL.html) or host and port used to construct the service URL. This value must be in the form of `service:jmx:<protocol>:<sap>` or `host:port`. Values in `host:port` form are used to create a service URL of `service:jmx:rmi:///jndi/rmi://<host>:<port>/jmxrmi`.  
`password` |  | The configured password if JMX is configured to require authentication.  
`type` |  | This value must be `jvm`.  
`username` |  | The configured username if JMX is configured to require authentication.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the JVM instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/jvm.classes.loaded`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.gc.collections.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.gc.collections.elapsed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.heap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.heap.init`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.heap.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.heap.used`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.init`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.nonheap.used`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/jvm.memory.pool.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.pool.init`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.pool.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.memory.pool.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/jvm.threads.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
## Verify the configuration

This section describes how to verify that you correctly configured the JVM receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that JVM metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/jvm.memory.heap.used", monitored_resource="gce_instance"}
         




## View dashboard

To view your JVM metrics, you must have a chart or dashboard configured. The JVM integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for JVM and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The JVM integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for JVM and click **View Details**. 
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
