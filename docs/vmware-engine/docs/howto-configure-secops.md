---
url: https://docs.cloud.google.com/vmware-engine/docs/howto-configure-secops/
title: Configure Google Security Operations with VMware Engine \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:04.321793+00:00
---

# Configure Google Security Operations with VMware Engine  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/howto-configure-secops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Google Security Operations with VMware Engine

This document describes how to configure [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) (Google SecOps) to improve the detection, investigation, and response to cybersecurity threats for virtual machines (VM) running on VMware Engine. Additionally, Google SecOps can analyze telemetry from your VMware infrastructure and other supported Google Cloud services.

## Overview

Google SecOps is a cloud service, built as a specialized layer on top of Google infrastructure, designed for enterprises to privately retain, analyze, and search the large amounts of security and network telemetry they generate. Google SecOps normalizes, indexes, correlates, and analyzes the data to provide instant analysis and context on risky or suspicious activity.

### Data ingestion mechanisms for Google SecOps

Google SecOps offers multiple pathways for data ingestion, as detailed in the [Google SecOps ingestion documentation](https://docs.cloud.google.com/chronicle/docs/secops/secops-ingestion). The configuration example in this guide focuses on the following key integration points within a representative architecture:

  * **VMs and workload system logs** : To capture logs originating from VMs and workloads, several architectural patterns exist. The configuration example in this guide uses an OpenTelemetry BindPlane agent deployed directly within these virtual machines. This method provides a flexible and standardized way to collect and forward system logs.

  * **Google Cloud Logs** : Beyond virtualized environments, most customer projects use a range of Google Cloud services (excluding VMware Engine in this specific context). To gain comprehensive visibility for threat detection, logs from these supported services can be channeled into Google SecOps. The configuration example that follows employs the direct ingestion mechanism, configuring Cloud Logging filters to selectively route relevant log data.




## Configure Google Security Operations with VMware Engine

To configure Google Security Operations with VMware Engine, complete the following steps:

  1. Forward Workload System Logs
  2. Create custom rules
  3. Forward Google Cloud cloud logs



### Forward workload system Logs

To forward workload system logs for VMs running within VMware Engine to Google SecOps, you can use an OpenTelemetry collection agent running within the workloads. The steps are as follows:

  1. Follow the Bindplane agent [before you begin](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#before-you-begin) instructions to install the agent and download the Google SecOps ingestion authentication file. You can download the Google SecOps authentication file from the [Google SecOps portal](https://pantheon.corp.google.com/security/chronicle).
  2. [Verify the firewall configuration](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#verify_the_firewall_configuration) to ensure relevant firewall ports are open.
  3. Install the Bindplane agent by following the instructions for your OS, either [Linux](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#linux) or [Windows](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#windows).
  4. Complete the steps to [configure the agent](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#configure_the_agent). Note the following details while completing these steps:

     * The **Receiver** section specifies which logs the agent should collect and sent to Google SecOps.
     * The **Exporter** section specifies the destination where the agents should send the logs.
     * This task uses the Google SecOps exporter, which sends the logs directly to theGoogle SecOps ingestion API.
  5. See [additional log collection configuration samples](https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent#additional_log_collection_configuration_samples) for sample configuration files you can use. The following is a specific example for collecting Windows Event Logs (Application, Security, and System) and sending them to Google SecOps. It uses the OpenTelemetry Collector configuration format: 
         
         receivers:
         windowseventlog/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _application:
             attributes:
                log_type: windows_event.application
             channel: application
             max_reads: 100
             poll_interval: 1s
             raw: true
             start_at: end
         windowseventlog/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _security:
             attributes:
                log_type: windows_event.security
             channel: security
             max_reads: 100
             poll_interval: 1s
             raw: true
             start_at: end
         windowseventlog/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _system:
             attributes:
                log_type: windows_event.system
             channel: system
             max_reads: 100
             poll_interval: 1s
             raw: true
             start_at: end
         processors:
         resourcedetection/source0_01HZ7NFAB5HZY6TPMGEYRN4XGZ:
             detectors:
                 -   system
             system:
                 hostname_sources:
                      -   os
         transform/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _processor0_ _logs:
             error_mode: ignore
             log_statements:
                 -   context: log
                   statements:
                       -   set(attributes["chronicle_log_type"], "WINEVTLOG") where true
         exporters:
         chronicle/NA-SDL:
             compression: none
             creds: '{  "type": "service_account",
                 "project_id": "malachite-previewamericassdl",
                 "private_key_id": "a9c8d8f0b081c09bcf92621804ba19fc6529ecce",
                 "private_key": "----BEGIN PRIVATE KEY-----abcdefg-----END PRIVATE KEY-----\n",
                 "client_email": "previewamericassdl-1710772997@malachite-previewamericassdl.iam.gserviceaccount.com",
                 "client_id": "114604545528934473681",
                 "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                 "token_uri": "https://oauth2.googleapis.com/token",
                 "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                 "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/previewamericassdl-1710772997%40malachite-previewamericassdl.iam.gserviceaccount.com",
                 "universe_domain": "googleapis.com" }'
             customer_id: a556547c-1cff-43ef-a2e4-cf5b12a865df
             endpoint: malachiteingestion-pa.googleapis.com
             ingestion_labels:
                 env: takeshi
             log_type: CATCH_ALL
             namespace: null
             raw_log_field: body
             retry_on_failure:
                 enabled: true
                 initial_interval: 5s
                 max_elapsed_time: 300s
                 max_interval: 30s
             sending_queue:
                 enabled: true
                 num_consumers: 10
                 queue_size: 5000
                 storage: file_storage/NA-SDL
         extensions:
         file_storage/NA-SDL:
             compaction:
                 directory: $OIQ_OTEL_COLLECTOR_HOME/storage
                 on_rebound: true
             directory: $OIQ_OTEL_COLLECTOR_HOME/storage
         service:
         extensions:
             -   file_storage/NA-SDL
         pipelines:
             logs/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _NA-SDL-0:
                 receivers:
                     -   windowseventlog/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _application
                     -   windowseventlog/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _security
                     -   windowseventlog/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _system
                 processors:
                     -   resourcedetection/source0_01HZ7NFAB5HZY6TPMGEYRN4XGZ
                     -   transform/source0 _01HZ7NFAB5HZY6TPMGEYRN4XGZ_ _processor0_ _logs
                 exporters:
                     -   chronicle/NA-SDL

  6. Restart the collector once the configuration is complete, and verify that logs are populated in the [Google SecOps dashboard](https://pantheon.corp.google.com/security/chronicle).




### Create custom rules for threat detection

Google SecOps provides default, curated rules and detection designed to identify cybersecurity threats effectively Beyond the default features, you can create custom rules to generate alerts tailored to a specific environment and its security concerns. For more sophisticated threat detection, Google SecOps enables the use of [multiple event rules](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview#multiple_event_rule). This allows tracking and correlating related security events over time, which which facilitates the identification of complex attack patterns that may not be apparent from isolated incidents.

### Forward Google Cloud cloud logs

To configure the ingestion of Google Cloud data into Google SecOps using direct ingestion, do the following:

  1. Follow the steps in [Ingest Google Cloud data to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs) to set up logs.
  2. Enable **ingest and analyze data** from Cloud Logging under the **Global Ingestion Settings** tab.
  3. Review the list of supported Google Cloud services for log ingestion to identify the Google Cloud services that are most important for your security monitoring needs. See [Export gcp_name logs](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs#export-logs).
  4. Modify the default export filter as needed under the **Export Filter Settings** tab to include the specific logs you require. The following example is a copy of the export filter used for this document: 
         
         log_id("dns.googleapis.com/dns_queries") OR log_id("cloudaudit.googleapis.com/activity") OR log_id("cloudaudit.googleapis.com/system_event") OR
         ( log_id("cloudaudit.googleapis.com/data_access")
         AND NOT protoPayload.methodName =~ "^storage.(buckets|objects).(get|list)$"
         AND NOT protoPayload.request.cmd = "select" ) OR
         log_id("cloudaudit.googleapis.com/policy") OR
         log_id("cloudaudit.googleapis.com/access_transparency") OR
         log_id("compute.googleapis.com/nat_flows") OR
         log_id("compute.googleapis.com/firewall") OR
         log_id("requests") OR
         logName =~ "^projects/[\w-]+/logs/syslog$" OR
         logName =~ "^projects/[\w-]+/logs/authlog$" OR
         log_id("securelog") OR
         log_id("sysmon.raw") OR
         logName =~ "^projects/[\w-]+/logs/windows_event_log$" OR
         log_id("windows_event_log") OR
         log_id("events") OR
         log_id("stdout") OR
         log_id("stderr") OR
         log_id("audit_log") OR
         log_id("recaptchaenterprise.googleapis.com/assessment") OR
         log_id("recaptchaenterprise.googleapis.com/annotation") OR
         log_id("cloudaudit.googleapis.com/activity")




## What's next

  * Learn how to [ingest Google Cloud data to Google SecOps](https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/ingest-gcp-logs).
  * Review [private cloud VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
