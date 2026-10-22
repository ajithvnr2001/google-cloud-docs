---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-logging-targets-create/
title: gdcloud logging targets create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:42.886476+00:00
---

# gdcloud logging targets create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-logging-targets-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud logging targets create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud logging targets create - Create a logging target in the given namespace.

## SYNOPSIS
    
    
    gdcloud logging targets create LOGGING_TARGET_NAME [flags]
    

### EXAMPLES
    
    
    To create a logging target, run:
    
        gdcloud logging targets create logging-target-name \
            --namespace=sample_namespace  \
            --match-clusters=cluster1,cluster2 \
            --match-pod-name-prefixes=pod-prefix1,pod-prefix2 \
            --match-container-name-prefixes=container-prefix1,container-prefix2 \
            --parser=json \
            --log-access-level=pa \
            --service-name=sample_service_name \
            --additional-fields={\"fieldName\": \"field-value\"}
    

### REQUIRED FLAGS
    
    
          --namespace string      Namespace of the operational logs to collect.
          --service-name string   Service name to apply as a label. For user workloads, this could be also considered as a workload name.
    

### OPTIONAL FLAGS
    
    
          --additional-fields string               Additional static fields to apply to log entries. Field name must not contain '-' character.
          --log-access-level string                Access level for log entries. Available options are: [ao, pa, io]. (default "ao")
          --match-clusters string                  Comma-separated list of cluster names to consider for the log collection job.
          --match-container-name-prefixes string   Comma-separated list of container name prefixes where logs are collected.
          --match-pod-name-prefixes string         Comma-separated list of pod name prefixes where logs are collected.
          --parser string                          Predefined parser for log entries. Available options are: [klog_text, klog_json, klogr, gdch_json, json].
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
