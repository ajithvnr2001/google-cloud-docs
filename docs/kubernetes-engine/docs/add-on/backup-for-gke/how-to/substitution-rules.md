---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/substitution-rules/
title: Modify resources during restoration (deprecated) \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:23:06.525195+00:00
---

# Modify resources during restoration (deprecated)  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/substitution-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)



Send feedback 

#  Modify resources during restoration (deprecated) Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

**Deprecated:** You're viewing an obsolete version of resource modification.

This page describes how to make modifications to Kubernetes resources during the restoration process.

## Overview

There are several reasons why you might want to modify Kubernetes resources as part of the restore process. For example:

  * You may want to provision PVCs using a different storage provisioner (for example, move from the Kubernetes in-tree driver to the CSI driver).

  * You may want to restore a namespace under a different name.

  * You may want to change a replica count in a Deployment or StatefulSet.




Backup for GKE provides a mechanism for doing this called _substitution rules_ which you may optionally define as part of a [`RestorePlan`](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

A substitution rule is a set of matching criteria specified together with a replacement field value. You can use substitution rules in the restore process as follows:

  1. First, Backup for GKE computes the set of resources to restore, based on the scope parameters in the restore configuration (for example: namespaces, group/kinds, etc.)

  2. Backup for GKE evaluates each resource selected for restore against the ordered list of substitution rules. If a rule matches the resource, the resource is updated with the substituted field value. All resources are matched against all rules, and the same resource may potentially have multiple substitutions performed against it.

  3. After all the rules have been evaluated, Backup for GKE creates the resulting set of resources in the target cluster.




## Substitution rule parameters

To define a substitution rule, you provide the following parameters:

**Parameter** | **Required** | **Description**  
---|---|---  
**targetNamespaces** | optional |  This is a list of namespaces. For a resource to match this rule, it must be a namespaced resource and have one of the given namespaces:   


  * If nothing is provided for this parameter, then all resources will match (all namespaced and cluster-scoped resources). 
  * If an empty string ("") is provided, then it will match only cluster-scoped resources. In the Google Cloud console, you can check **Exclude namespaced resources** to set the list to a single empty string. 

  
**targetGroupKinds** | optional |  This is a list of Kubernetes resource group/kind tuples:   


  * If nothing is provided for this parameter, then all resources will match (no restrictions based on group/kind). 
  * If one or more group/kinds is supplied, then resources must match one of them in order to match the rule. 

  
**targetJsonPath** | required |  This is a [JSONPath](https://kubernetes.io/docs/reference/kubectl/jsonpath) expression that is matched against resources. Note that this rule not only matches the resource, it also matches a specific attribute in the resource.   
**originalValuePattern** | optional |  This is a [regular expression](https://en.wikipedia.org/wiki/Regular_expression) that is matched against the current value of the attribute. If not supplied, then the attribute will always match.   
**newValue** | required |  This is the new value to use for the matched attribute value.   
  
To learn more about defining substitution rules in the Google Cloud console, see [Plan a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

To define substitution rules using the gcloud CLI, create a file containing a YAML array of substitutionRules and include the `--substitution-rules-file=` parameter to the [`gcloud beta container backup-restore restore-plans create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-plans/create) command.

## Substitution rule examples

The following examples are provided in the YAML format used by the gcloud CLI.

### Change StorageClass

In this example, we change the StorageClass in all restored PersistentVolumeClaim resources from `standard` to `premium-rwo`:
    
    
    substitutionRules:
    - targetGroupKinds:
      - resourceGroup: ''
        resourceKind: PersistentVolumeClaim
      targetJsonPath: "{..storageClassName}"
      originalValuePattern: standard
      newValue: premium-rwo
    

### Clone Namespace

In this example, we clone a namespace from alpha to beta—creating a new namespace "beta" and restoring all of the resources from "alpha" into the new "beta" namespace. Note that this examples requires two substitution rules—one for the namespace itself, and one for the resources within the namespace.
    
    
    substitutionRules:
    - targetNamespaces:
      - ''
      targetGroupKinds:
      - resourceGroup: ''
        resourceKind: Namespace
      targetJsonPath: "{.metadata.name}"
      originalValuePattern: alpha
      newValue: beta
    - targetNamespaces:
      - alpha
      targetJsonPath: "{.metadata.namespace}"
      originalValuePattern: alpha
      newValue: beta
    

### Change StorageClass and replica count in a cloned namespace

In this example, we clone a namespace, and then apply a set of changes to the resources in the new namespace:

  * Change the StorageClass on PVCs from `standard` to `premium-rwo`

  * Change the replica count on Deployments from `7` to `3`



    
    
    substitutionRules:
    - targetNamespaces:
      - ''
      targetGroupKinds:
      - resourceGroup: ''
        resourceKind: Namespace
      targetJsonPath: "{.metadata.name}"
      originalValuePattern: alpha
      newValue: beta
    - targetNamespaces:
      - alpha
      targetJsonPath: "{.metadata.namespace}"
      originalValuePattern: alpha
      newValue: beta
    - targetNamespaces:
      - beta
      targetGroupKinds:
      - resourceGroup: ''
        resourceKind: PersistentVolumeClaim
      targetJsonPath: "{..storageClassName}"
      originalValuePattern: standard
      newValue: premium-rwo
    - targetNamespaces:
      - beta
      targetGroupKinds:
      - resourceGroup: apps
        resourceKind: Deployment
      targetJsonPath: "{$.spec.replicas}"
      originalValuePattern: '7'
      newValue: '3'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
