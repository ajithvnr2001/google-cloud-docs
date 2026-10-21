---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/
title: gcloud beta container hub \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:48:48.415268+00:00
---

# gcloud beta container hub  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container hub Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container hub - centrally manage features and services on all your Kubernetes clusters with fleet 
SYNOPSIS
    

`gcloud beta container hub` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` The command group to register GKE or other Kubernetes clusters running in a variety of environments, including Google cloud, on premises in customer datacenters, or other third party clouds with fleet. Fleet provides a centralized control-plane to managed features and services on all registered clusters. 

A registered cluster is always associated with a Membership, a resource within fleet. 

EXAMPLES
     Manage memberships of all your GKE and other Kubernetes clusters with fleet: 
    
    
    [gcloud beta container hub memberships](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships) --help

Manage Config Management feature on all memberships: 
    
    
    [gcloud beta container hub config-management](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management) --help

Manage Multi-cluster Ingress feature on all memberships: 
    
    
    [gcloud beta container hub ingress](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/ingress) --help

Manage Multi-cluster Services feature on all memberships: 
    
    
    [gcloud beta container hub multi-cluster-services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/multi-cluster-services) --help

Manage CloudRun feature on all memberships: 
    
    
    [gcloud beta container hub cloudrun](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/cloudrun) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[cloudrun](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/cloudrun)`
     `(BETA)` Manage the CloudRun feature. 
`[clusterupgrade](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/clusterupgrade)`
     `(BETA)` Configure the Fleet clusterupgrade feature. 
`[config-management](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/config-management)`
     `(BETA)` Use the Config Management feature. 
`[dataplane-v2-encryption](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/dataplane-v2-encryption)`
     `(BETA)` Manage Dataplane V2 Encryption Feature. 
`[features](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/features)`
     `(BETA)` Manage Hub Feature resources. 
`[fleetobservability](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/fleetobservability)`
     `(BETA)` Manage Fleet Observability Feature. 
`[identity-service](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/identity-service)`
     `(BETA)` Manage Identity Service Feature. 
`[ingress](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/ingress)`
     `(BETA)` Manage Multi-cluster Ingress Feature. 
`[memberships](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/memberships)`
     `(BETA)` Manage memberships of all your GKE and other Kubernetes clusters with fleets. 
`[mesh](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/mesh)`
     `(BETA)` Manage Service Mesh Feature. 
`[multi-cluster-services](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/multi-cluster-services)`
     `(BETA)` Manage Multi-cluster Services Feature. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/operations)`
     `(BETA)` Manage Anthos fleet long-running operations. 
`[packages](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/packages)`
     `(BETA)` Manage Fleet Packages resources. 
`[policycontroller](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/policycontroller)`
     `(BETA)` Manage Policy Controller Feature. 
`[rbacrolebindingactuation](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/rbacrolebindingactuation)`
     `(BETA)` Manage RbacRoleBinding Actuation. 
`[rollouts](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/rollouts)`
     `(BETA)` Manage rollouts. 
`[rolloutsequences](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/rolloutsequences)`
     `(BETA)` Create and manage rollout sequences. 
`[scopes](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/scopes)`
     `(BETA)` Manage scopes of all your GKE fleets. 
`[workload-identity](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/workload-identity)`
     `(BETA)` Manage Workload Identity Feature. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/create)`
     `(BETA)` Create a fleet. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/delete)`
     `(BETA)` Delete a fleet. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/describe)`
     `(BETA)` Show fleet info. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/list)`
     `(BETA)` List fleets visible to the user in an organization. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/hub/update)`
     `(BETA)` Update a fleet. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud container hub](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub)
    
    
    [gcloud alpha container hub](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/hub)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
