---
url: https://docs.cloud.google.com/migrate/kf/docs/2.10/reference/troubleshoot_serviceinstance/
title: Troubleshoot Kf ServiceInstances \u00a0|\u00a0 Kf 2.10 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:16.328378+00:00
---

# Troubleshoot Kf ServiceInstances  |  Kf 2.10  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.10/reference/troubleshoot_serviceinstance/

Version 2.10

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.10 ](https://docs.cloud.google.com/migrate/kf/docs/2.10)



Send feedback 

#  Troubleshoot Kf ServiceInstances Stay organized with collections  Save and categorize content based on your preferences. 

Use these steps to troubleshoot various issues that can occur when using Kf ServiceInstances.

## Object is stuck deleting.

Run the following command to get the resource information, then check for the causes listed below:
    
    
    kubectl get serviceinstances.kf.dev -n SPACE_NAME SERVICEINSTANCE_NAME -o yaml

The `kf` CLI can help check for some of the issues:
    
    
    kf doctor --space SPACE_NAME serviceinstance/SERVICEINSTANCE_NAME

Possible Cause| Solution  
---|---  
Deletion timestamp is in the future.  |  With clock skew the `metadata.deletionTimestamp` may still be in the future. Wait a few minutes to see if the object is deleted.  
Finalizers exist on the object.  |  Finalizers are present on the object, they must be removed by the controller that set them before the object is deleted. If you want to force a deletion without waiting for the finalizers, edit the object to remove them from the `metadata.finalizers` array. To remove the finalizer from an object, use the `kubectl edit RESOURCE_TYPE RESOURCE_NAME -n my-space` command. See [using finalizers to control deletion](https://kubernetes.io/blog/2021/05/14/using-finalizers-to-control-deletion/) to learn more. Warning: Removing finalizers without allowing the controllers to complete may cause errors, security issues, data loss, or orphaned resources.  
Dependent objects may exist.  |  The object may be waiting on dependents to be deleted before it is deleted. See the [Kubernetes garbage collection guide to learn more](https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/). Have an administrator check all objects in the namespace and cluster to see if one of them is blocking deletion. If you need to remove the object without waiting for dependents, use `kubectl delete` with the cascade flag set to: `--cascade=orphan`.  
  
## Object generation state drift.

Run the following command to get the resource information, then check for the causes listed below:
    
    
    kubectl get serviceinstances.kf.dev -n SPACE_NAME SERVICEINSTANCE_NAME -o yaml

The `kf` CLI can help check for some of the issues:
    
    
    kf doctor --space SPACE_NAME serviceinstance/SERVICEINSTANCE_NAME

Possible Cause| Solution  
---|---  
Object has generation version drift.  |  This error usually occurs Kf controller did not read the latest version of the object, this error is usually self-recovered once Kubernetes replicas reach eventual consistency, and it usually does not require action from users.  
  
## Object reconciliation failed.

Run the following command to get the resource information, then check for the causes listed below:
    
    
    kubectl get serviceinstances.kf.dev -n SPACE_NAME SERVICEINSTANCE_NAME -o yaml

The `kf` CLI can help check for some of the issues:
    
    
    kf doctor --space SPACE_NAME serviceinstance/SERVICEINSTANCE_NAME

Possible Cause| Solution  
---|---  
Object has TemplateError  |  This error usually occurs if user has entered an invalid property in the custom resource Spec, or the configuration on the Space/Cluster is bad. To understand the root cause, user can read the longer error message in the object’s `status.conditions` using the command:`kubectl describe RESOURCE_TYPE RESOURCE_NAME -n space`. For example: `kubectl describe serviceinstance my-service -n my-space`.  
Object has ChildNotOwned error (Name conflicts)  |  This error usually means that the object(s) the controller is trying to create already exists. This happens if the user created a K8s resource that has the same name as what the controller is trying to create; but more often it happens if user deletes a resource then Kf controller tries to re-create it. If a child resource is still hanging around, its owner will be the old resource that no longer exists. To recover from the error, it is recommended that user deletes the impacted resource and then recreates it. To delete the object, use a Kf deletion command or use the `kubectl delete RESOURCE_TYPE RESOURCE_NAME -n SPACE`command. For example, `kf delete-space my-space` or `kubectl delete space my-space`. To recreate a resource, use a Kf command. For example: `kf create-space my-space`.  
Object has ReconciliationError  |  This error usually means that something has gone wrong with the HTTP call made (by Kf controller) to the Kubernetes API servier to create/update resource. To understand the root cause, user can read the longer error message in the object’s `status.conditions` using the command:`kubectl describe RESOURCE_TYPE RESOURCE_NAME -n space`. For example: `kubectl describe serviceinstance my-service -n my-space`.  
  
## Backing resource reconciliation failed.

Run the following command to get the resource information, then check for the causes listed below:
    
    
    kubectl get serviceinstances.kf.dev -n SPACE_NAME SERVICEINSTANCE_NAME -o yaml

The `kf` CLI can help check for some of the issues:
    
    
    kf doctor --space SPACE_NAME serviceinstance/SERVICEINSTANCE_NAME

Possible Cause| Solution  
---|---  
Backing resource DeprovisionFailed error.  |  This error usually occurs when backing resources (MySQL database hosted at an external OSB server) fails to be deprovisioned. Kf can not safely determine if the dependent resource is deprovisioned. To recover from the error, it is recommended that user reads the detail error message in the object’s `status.conditions` using the command:`kubectl describe RESOURCE_TYPE RESOURCE_NAME -n space`. For example: `kubectl describe servipropogatesceinstance my-service -n my-space`. Once the error message is confirmed, have an administrator check the backing resource and clean it up manually. Once the backing resource is determined to be safely released, the impacted Kf resource can be reconciled successfully by manually removing the `Finalizer` from the object spec, use the `kubectl edit serviceinstance my-service -n my-space` command.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
