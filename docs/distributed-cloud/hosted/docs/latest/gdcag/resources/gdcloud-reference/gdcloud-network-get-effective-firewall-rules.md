---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-network-get-effective-firewall-rules/
title: gdcloud network get-effective-firewall-rules \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:33.883832+00:00
---

# gdcloud network get-effective-firewall-rules  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-network-get-effective-firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud network get-effective-firewall-rules Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud network get-effective-firewall-rules - Get the effective firewall rules for a workload.

## SYNOPSIS
    
    
    gdcloud network get-effective-firewall-rules [flags]
    

### EXAMPLES
    
    
    To get the effective firewall rules for a specific pod named 'my-pod' in shared cluster 'user-vm-1' and project 'project-1', run:
        gdcloud network get-effective-firewall-rules --project=project-1 --workload-name=pod/my-pod --cluster-name=user-vm-1
    
    To get the effective firewall rules for workloads with labels 'app=my-app' in project 'project-1', run:
        gdcloud network get-effective-firewall-rules --project=project-1 --workload-labels=app=my-app
    
    To get the effective firewall rules for workloads with labels 'app=my-app' in standard cluster 'standard-cluster-1' and project 'project-1', run:
        gdcloud network get-effective-firewall-rules --project=project-1 --workload-labels=app=my-app --cluster-name=standard-cluster-1 --standard --namespace=my-namespace
    

### OPTIONAL FLAGS
    
    
          --cluster-name string      Name of the cluster where the workload resides.
          --namespace string         Namespace where the workload resides. This is only required when --standard is specified.
          --standard                 Set the configuration for the cluster with the firewall rules as a standard cluster. If not specified, the shared cluster configuration is used.
          --workload-labels string   Comma-separated list of labels (key=value) of the workload to get the effective firewall rules for (for example, 'app=my-app,role=frontend').
          --workload-name string     Name of the workload to get the effective firewall rules for, in the 'kind/name' format (for example, 'pod/my-pod', 'deployment/my-deploy').
          --zone string              Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
