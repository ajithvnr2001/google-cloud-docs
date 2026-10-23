---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/use-telemetry-api/
title: Use the Telemetry API \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:56.321727+00:00
---

# Use the Telemetry API  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/use-telemetry-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Use the Telemetry API Stay organized with collections  Save and categorize content based on your preferences. 

You can configure the Ops Agent to use the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) to send logs, metrics, and traces to your Google Cloud project. The Telemetry API, `telemetry.googleapis.com`, is an implementation of the open-source [OpenTelemetry Protocol](https://opentelemetry.io/docs/specs/otlp). When you configure the Ops Agent to use this API, the Ops Agent sends telemetry by using the Telemetry API rather than the proprietary Cloud Monitoring API, Logging API, or Trace API.

If you adopt the use of the Telemetry API in the Ops Agent and have charts or alerting policies that monitor your API usage, then you must update these artifacts to monitor the `telemetry.googleapis.com` endpoint rather than the `monitoring.googleapis.com`, `logging.googleapis.com`, or `cloudtrace.googleapis.com` endpoints.

## Before you begin

To use the Telemetry API, do the following:

  1. Enable the Telemetry API in your Google Cloud project, if it is not already enabled. You can enable the API by running the following command:
         
         gcloud services enable telemetry.googleapis.com
         

  2. Adjust Telemetry API quotas, if the default values are not sufficient. The Telemetry API has quotas separate from those of the Cloud Monitoring API and Cloud Logging API. For information about the quotas and limits for the Telemetry API, see the following:

     * [Telemetry API quotas for metric ingestion](https://docs.cloud.google.com/stackdriver/quotas#telemetry-api-metric-limits)
     * [Telemetry API quotas for log ingestion](https://docs.cloud.google.com/stackdriver/quotas#telemetry-api-log-limits)
     * [Telemetry API quotas for trace ingestion](https://docs.cloud.google.com/stackdriver/quotas#telemetry-api-trace-limits)

You might need to adjust these quotas to accommodate the volume of telemetry data you ingest.

  3. If you are collecting traces, then grant the role [Cloud Telemetry Traces Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/telemetry#telemetry.tracesWriter) (`roles/telemetry.tracesWriter`) to the service account used by the Ops Agent. This role provides the permissions needed to write traces.




## Configure the Ops Agent to use the Telemetry API

The Ops Agent provides a configuration option to switch between sending telemetry by using the proprietary API—the default— and by using Telemetry API. To collect telemetry by using the Ops Agent and the Telemetry API, you must do the following, as described in the following sections:

  1. Install a version of the Ops Agent that supports the Telemetry API.
  2. Update the Ops Agent `config.yaml` file to set the configuration option.
  3. Restart the Ops Agent to pick up the change.



### Use Ops Agent version 2.71.0 or newer

To use the Telemetry API with the Ops Agent, you must install the Ops Agent version 2.71.0 or newer. For information about installing the Ops Agent, see [Install the Ops Agent of individual VMs](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation).

### Set the configuration option

Give the Ops Agent access to the Telemetry API by setting the `otlp_exporter` configuration option to `true` in the agent's `config.yaml` file:
    
    
    global:
       otlp_exporter: true
    

### Restart the Ops Agent

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
         




## Configure the Ops Agent to not use the Telemetry API

To stop the Ops Agent from collecting telemetry by using the Telemetry API and to resume collecting telemetry by using the Cloud Monitoring API, Logging API, and Trace API, do the following:

  1. Remove the `otlp_exporter` option from the `config.yaml` file. Alternatively, you can set the option to `false`.

  2. Restart the Ops Agent to pick up the change.




## What's next

  * To learn more about the Telemetry API, see [Telemetry (OTLP) API overview](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview).
  * For information about installing and configuring the Ops Agent, see the following documents: 
    * [Install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation)
    * [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
