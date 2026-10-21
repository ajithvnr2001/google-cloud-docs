---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/
title: gcloud container hub \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:24:39.947810+00:00
---

# gcloud container hub  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container hub Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container hub - centrally manage features and services on all your Kubernetes clusters with fleet 
SYNOPSIS
    

`gcloud container hub` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     The command group to register GKE or other Kubernetes clusters running in a variety of environments, including Google cloud, on premises in customer datacenters, or other third party clouds with fleet. Fleet provides a centralized control-plane to managed features and services on all registered clusters. 

A registered cluster is always associated with a Membership, a resource within fleet. 

EXAMPLES
     Manage memberships of all your GKE and other Kubernetes clusters with fleet: 
    
    
    [gcloud container hub memberships](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/memberships) --help

Manage Config Management feature on all memberships: 
    
    
    [gcloud container hub config-management](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/config-management) --help

Manage Multi-cluster Ingress feature on all memberships: 
    
    
    [gcloud container hub ingress](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/ingress) --help

Manage Multi-cluster Services feature on all memberships: 
    
    
    [gcloud container hub multi-cluster-services](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/multi-cluster-services) --help

Manage CloudRun feature on all memberships: 
    
    
    [gcloud container hub cloudrun](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[cloudrun](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/cloudrun)`
     Manage the CloudRun feature. 
`[clusterupgrade](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade)`
     Configure the Fleet clusterupgrade feature. 
`[config-management](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/config-management)`
     Use the Config Management feature. 
`[dataplane-v2-encryption](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/dataplane-v2-encryption)`
     Manage Dataplane V2 Encryption Feature. 
`[features](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/features)`
     Manage Hub Feature resources. 
`[fleetobservability](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/fleetobservability)`
     Manage Fleet Observability Feature. 
`[identity-service](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/identity-service)`
     Manage Identity Service Feature. 
`[ingress](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/ingress)`
     Manage Multi-cluster Ingress Feature. 
`[memberships](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/memberships)`
     Manage memberships of all your GKE and other Kubernetes clusters with fleets. 
`[mesh](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/mesh)`
     Manage Service Mesh Feature. 
`[multi-cluster-services](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/multi-cluster-services)`
     Manage Multi-cluster Services Feature. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/operations)`
     Manage Anthos fleet long-running operations. 
`[packages](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/packages)`
     Manage Fleet Packages resources. 
`[policycontroller](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/policycontroller)`
     Manage Policy Controller Feature. 
`[rbacrolebindingactuation](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/rbacrolebindingactuation)`
     Manage RbacRoleBinding Actuation. 
`[rollouts](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/rollouts)`
     Manage rollouts. 
`[rolloutsequences](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/rolloutsequences)`
     Create and manage rollout sequences. 
`[scopes](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/scopes)`
     Manage scopes of all your GKE fleets. 
`[workload-identity](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/workload-identity)`
     Manage Workload Identity Feature. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/create)`
     Create a fleet. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/delete)`
     Delete a fleet. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/describe)`
     Show fleet info. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/list)`
     List fleets visible to the user in an organization. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub/update)`
     Update a fleet. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha container hub](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub)
    
    
    [gcloud beta container hub](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
