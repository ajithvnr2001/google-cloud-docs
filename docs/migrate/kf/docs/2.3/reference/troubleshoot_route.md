---
url: https://docs.cloud.google.com/migrate/kf/docs/2.3/reference/troubleshoot_route/
title: Troubleshoot Kf Routes \u00a0|\u00a0 Kf 2.3 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:23:57.097185+00:00
---

# Troubleshoot Kf Routes  |  Kf 2.3  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.3/reference/troubleshoot_route/

Version 2.3

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
  * [ 2.3 ](https://docs.cloud.google.com/migrate/kf/docs/2.3)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.3/reference)



Send feedback 

#  Troubleshoot Kf Routes Stay organized with collections  Save and categorize content based on your preferences. 

Use these steps to troubleshoot various issues that can occur when using Kf Routes.

## Object is stuck deleting.

Run the following command to get the resource information, then check for the causes listed below:
    
    
    kubectl get routes.kf.dev -n SPACE_NAME ROUTE_NAME -o yaml

The `kf` CLI can help check for some of the issues:
    
    
    kf doctor --space SPACE_NAME route/ROUTE_NAME

Possible Cause| Solution  
---|---  
Deletion timestamp is in the future.  |  With clock skew the `metadata.deletionTimestamp` may still be in the future. Wait a few minutes to see if the object is deleted.  
Finalizers exist on the object.  |  Finalizers are present on the object, they must be removed by the controller that set them before the object is deleted. If you want to force a deletion without waiting for the finalizers, edit the object to remove them from the `metadata.finalizers` array. Warning: Removing finalizers without allowing the controllers to complete may cause errors, security issues, data loss, or orphaned resources.  
Dependent objects may exist.  |  The object may be waiting on dependents to be deleted before it deleted. See the [Kubernetes garbage collection guide to learn more](https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/). Have an administrator check all objects in the namespace and cluster to see if one of them is blocking deletion. If you need to remove the object without waiting for dependents, use `kubectl delete` with the cascade flag set to: `--cascade=orphan`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
