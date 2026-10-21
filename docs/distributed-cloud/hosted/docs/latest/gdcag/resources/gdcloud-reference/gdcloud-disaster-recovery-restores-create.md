---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-disaster-recovery-restores-create/
title: gdcloud disaster-recovery restores create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:37:54.019305+00:00
---

# gdcloud disaster-recovery restores create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-disaster-recovery-restores-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud disaster-recovery restores create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud disaster-recovery restores create - Create a disaster recovery restore.

## SYNOPSIS
    
    
    gdcloud disaster-recovery restores create [flags]
    

### REQUIRED FLAGS
    
    
          --backup string                Name of the backup used for the disaster recovery restoration.
          --cluster string               Name of the cluster where the restore is located.
          --name string                  Name of the disaster recovery restore.
          --restore-scope restoreScope   Scope of the disaster recovery restore, must be one of [gitlab, hwdr, controlplane, custom].
    

### OPTIONAL FLAGS
    
    
          --all-namespaces                     Whether to restore resources in all namespaces, the flag only works in the custom scope.
          --cluster-resources stringArray      A list of allowed cluster resources to be restored for the custom scope, the resources are provided by <group>/<kind> format, e.g. rbac.authorization.k8s.io/ClusterRole.
          --dry-run                            Whether to dry run the command.
          --namespaced-resources stringArray   A list of allowed namespaced resources to be restored for the custom scope, the resources are provided by <group>/<kind> format, e.g. apps/Deployment.
          --namespaces stringArray             A list of namespaces of the resources to restore, the list only works in the custom scope.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
