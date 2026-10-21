---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-organizations-config-create/
title: gdcloud organizations config create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:10:43.062212+00:00
---

# gdcloud organizations config create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-organizations-config-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud organizations config create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud organizations config create - Create an Organization custom resource YAML file.

## SYNOPSIS
    
    
    gdcloud organizations config create [flags]
    

### EXAMPLES
    
    
    To create an Organization YAML file with various fields preset, run:
    
      gdcloud organizations config create --name org-1 \
        --log-retention-policy \
        paAuditLogsRetentionTime=400,\
        ioAuditLogsRetentionTime=2000,\
        operationalLogsRetentionTime=90,\
        metricsRetentionTime=90 \
        --kms-root-key-type ctm-root
    

### OPTIONAL FLAGS
    
    
          --kms-root-key-type string              The KMS root key type for an organization. This can be either 'local-root' or 'ctm-root'. (default "ctm-root")
          --labels stringToString                 Propagates labels to the admin and system clusters as a key-value pair. Key must start with 'lcm.private.gdc.goog/' to propagate. (default [])
          --log-retention-policy stringToString   Comma-separated list of log retention times for an organization in days. (default [metricsRetentionTime=90,paAuditLogsRetentionTime=400,ioAuditLogsRetentionTime=2000,operationalLogsRetentionTime=90])
          --name string                           Name for the organization to create. (default "org-1")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
