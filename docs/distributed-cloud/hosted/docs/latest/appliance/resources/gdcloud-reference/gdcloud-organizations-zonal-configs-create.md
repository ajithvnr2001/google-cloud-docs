---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-organizations-zonal-configs-create/
title: gdcloud organizations zonal-configs create \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:43.267342+00:00
---

# gdcloud organizations zonal-configs create  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-organizations-zonal-configs-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud organizations zonal-configs create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud organizations zonal-configs create - Create an OrganizationZonalConfig custom resource YAML files for each zone.

## SYNOPSIS
    
    
    gdcloud organizations zonal-configs create [flags]
    

### EXAMPLES
    
    
    To create an OrganizationZonalConfig file with various fields preset, run:
    
      gdcloud organizations zonal-configs create --name testOrg \
          --zones={zone1,zone2}
          --version 1.9.2-gdch.153 \
          --server-quota \
              o1-highmem1-40-gdc-metal=1,\
              o1-standard1-64-gdc-metal=2,\
              o1-highmem1-96-gdc-metal=3,\
              o1-highmem1-104-gdc-metal=4,\
              o1-highmem1-448-gdc-metal=5,\
              o1-highgpu1-48-gdc-metal=6 \
          --storage-sku \
              block-standard=100Ti,\
              file-standard=100Ti,\
              object-nearline=100Ti,\
              object-standard=100Ti \
          --admin-server \
              o1-standard1-64-gdc-metal=3
      This command writes the YAML files to the HOME directory in the format [org name]-[zone].yaml
    

### OPTIONAL FLAGS
    
    
          --admin-server stringToString   Admin server type and the amount of org admin servers to allocate for that server type as a key-value pair. (default [])
          --name string                   Name of the referenced organization.
          --server-quota stringToString   Comma-separated list of key-value pairs for server types and their quotas for the worker machines. (default [])
          --storage-sku stringToString    Comma-separated list of key-value pairs for storage SKUs and their sizes for an organization. (default [])
          --version string                Version of the GDCH software.
          --zones stringArray             Comma-separated list of zone IDs to create a config for.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
