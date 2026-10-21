---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/
title: gcloud alpha container fleet \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:56:17.480680+00:00
---

# gcloud alpha container fleet  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container fleet Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container fleet - centrally manage features and services on all your Kubernetes clusters with fleet 
SYNOPSIS
    

`gcloud alpha container fleet` `GROUP` | `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The command group to register GKE or other Kubernetes clusters running in a variety of environments, including Google cloud, on premises in customer datacenters, or other third party clouds with fleet. Fleet provides a centralized control-plane to managed features and services on all registered clusters. 

A registered cluster is always associated with a Membership, a resource within fleet. 

EXAMPLES
     Manage memberships of all your GKE and other Kubernetes clusters with fleet: 
    
    
    [gcloud alpha container fleet memberships](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/memberships) --help

Manage Config Management feature on all memberships: 
    
    
    [gcloud alpha container fleet config-management](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management) --help

Manage Multi-cluster Ingress feature on all memberships: 
    
    
    [gcloud alpha container fleet ingress](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/ingress) --help

Manage Multi-cluster Services feature on all memberships: 
    
    
    [gcloud alpha container fleet multi-cluster-services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/multi-cluster-services) --help

Manage CloudRun feature on all memberships: 
    
    
    [gcloud alpha container fleet cloudrun](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/cloudrun) --help

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[cloudrun](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/cloudrun)`
     `(ALPHA)` Manage the CloudRun feature. 
`[clusterupgrade](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/clusterupgrade)`
     `(ALPHA)` Configure the Fleet clusterupgrade feature. 
`[config-management](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/config-management)`
     `(ALPHA)` Use the Config Management feature. 
`[dataplane-v2-encryption](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/dataplane-v2-encryption)`
     `(ALPHA)` Manage Dataplane V2 Encryption Feature. 
`[features](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/features)`
     `(ALPHA)` Manage Hub Feature resources. 
`[fleetobservability](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/fleetobservability)`
     `(ALPHA)` Manage Fleet Observability Feature. 
`[identity-service](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/identity-service)`
     `(ALPHA)` Manage Identity Service Feature. 
`[ingress](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/ingress)`
     `(ALPHA)` Manage Multi-cluster Ingress Feature. 
`[memberships](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/memberships)`
     `(ALPHA)` Manage memberships of all your GKE and other Kubernetes clusters with fleets. 
`[mesh](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/mesh)`
     `(ALPHA)` Manage Service Mesh Feature. 
`[multi-cluster-services](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/multi-cluster-services)`
     `(ALPHA)` Manage Multi-cluster Services Feature. 
`[namespaceactuation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/namespaceactuation)`
     `(ALPHA)` Manage Namespace Actuation Feature. 
`[operations](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/operations)`
     `(ALPHA)` Manage Anthos fleet long-running operations. 
`[packages](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/packages)`
     `(ALPHA)` Manage Fleet Packages resources. 
`[policycontroller](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/policycontroller)`
     `(ALPHA)` Manage Policy Controller Feature. 
`[rbacrolebindingactuation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/rbacrolebindingactuation)`
     `(ALPHA)` Manage RbacRoleBinding Actuation. 
`[rollouts](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/rollouts)`
     `(ALPHA)` Manage rollouts. 
`[rolloutsequences](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/rolloutsequences)`
     `(ALPHA)` Create and manage rollout sequences. 
`[scopes](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/scopes)`
     `(ALPHA)` Manage scopes of all your GKE fleets. 
`[service-directory](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/service-directory)`
     `(ALPHA)` Manage the Service Directory Feature. 
`[workload-identity](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/workload-identity)`
     `(ALPHA)` Manage Workload Identity Feature. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/create)`
     `(ALPHA)` Create a fleet. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/delete)`
     `(ALPHA)` Delete a fleet. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/describe)`
     `(ALPHA)` Show fleet info. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/list)`
     `(ALPHA)` List fleets visible to the user in an organization. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/fleet/update)`
     `(ALPHA)` Update a fleet. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud container fleet](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet)
    
    
    [gcloud beta container fleet](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/fleet)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
