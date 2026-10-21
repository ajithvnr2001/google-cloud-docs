---
url: https://docs.cloud.google.com/config-connector/docs/concepts/reconciliation/
title: Reconciliation strategy \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:18.030112+00:00
---

# Reconciliation strategy  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/reconciliation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reconciliation strategy

With declarative configuration, you define the desired state of the system. The system then works constantly to remain as close as possible to this state. See [Declarative management of Kubernetes objects using configuration files](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/) for more information.

With Config Connector, you can create and update resources in any order, regardless of dependency relationships. GKE moves your declared configuration towards [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency) with the desired state.

For example, if you create a `PubSubSubscription` before the corresponding `PubSubTopic`, Config Connector waits until the topic is created before creating the associated subscription.

The duration your Config Connector installation remains inconsistent depends on the number and types of resources it manages. Changes to a GKE cluster are typically executed in seconds. However, the time to create Google Cloud resources can vary based on the type of resource. For example, a single `PubSubTopic` takes seconds to create. Google Cloud resources do not reach consistency until they are created. For example, when creating an `SQLInstance` and an `SQLDatabase`, the system is inconsistent for a period of minutes while the database is created.

GKE and Config Connector reconcile each resource with every update or after a jitter period with an average based on the preconfigured default interval. You can find the default interval in "Config Connector Default Average Reconcile Interval In Seconds" from each resource's reference page. For links to each resource, see the [Resource overview](https://docs.cloud.google.com/config-connector/docs/reference/overview). When there is an error in reconciling, Config Connector retries with exponential backoff where maximum backoff is two minutes. You can view any errors in the [Events](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-your-resources#viewing_events) of a given resource.

## Configuring the reconciliation interval

Starting from Config Connector [1.102](https://docs.cloud.google.com/config-connector/docs/release-notes#March_30_2023), you can configure the average reconcile interval for resources managed by Config Connector with the `cnrm.cloud.google.com/reconcile-interval-in-seconds` annotation. The value of the annotation overwrites the default value of "Config Connector Default Average Reconcile Interval In Seconds" from the [resource reference](https://docs.cloud.google.com/config-connector/docs/reference/overview) page. The value of the annotation should be a non-negative integer representing time in seconds. If the value is set to 0, Config Connector stops initiating reconciliations for the resource once it reaches the [UpToDate](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-your-resources#-specific_events) status.

For example, if you want Config Connector to reconcile a resource less frequently to avoid hitting underlying Google Cloud [API quota issues](https://docs.cloud.google.com/config-connector/docs/best-practices#quota-limits), you can set the average reconciliation interval value to 1 hour.
    
    
    cnrm.cloud.google.com/reconcile-interval-in-seconds: "3600"
    

If you want Config Connector to reconcile a resource more frequently to correct drifts sooner, you can set the annotation with a small value.

You can annotate all resources of a particular type that shares the same Group Version Kind (GVK) with the following script:

**Note:** If you are using a GitOps-style workflow, for example with [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview), the following script may not be applicable. Instead, you must update the YAML files with the annotation set in your source of truth.
    
    
    #!/bin/bash
    
    KIND=RESOURCE_KIND
    NAMESPACE=RESOURCE_NAMESPACE
    ANNOTATION_KEY="cnrm.cloud.google.com/reconcile-interval-in-seconds"
    ANNOTATION_VALUE=RECONCILE_INTERVAL
    
    kubectl annotate --overwrite --all ${KIND} ${ANNOTATION_KEY}=${ANNOTATION_VALUE} -n ${NAMESPACE}
    echo "Annotation added to all ${KIND} RESOURCE"
    

Replace the following:

  * `RESOURCE_KIND`: the resource kind that you want to annotate.
  * `RESOURCE_NAMESPACE`: the namespace that contains the resources that you want to annotate.
  * `RECONCILE_INTERVAL`: the reconcile interval in seconds.



You can set the reconciliation interval to 0 to disable drift correction for a resource, but it does not disable resource actuation. If you make changes to the resource [`Spec`](https://docs.cloud.google.com/config-connector/docs/concepts/resources#spec_and_status), the resource will be reconciled again.

Setting the reconciliation interval to 0 is irreversible. This means changing the value back to a non-zero number does not make Config Connector reconcile the resource again.

If you want to revert the 0 reconciliation interval, you have the following options:

  * Modify the resource spec with the reconciliation interval value to enable new reconciliations.
  * Abandon the resource by setting the annotation `cnrm.cloud.google.com/deletion-policy: "abandon"` and recreate the resource with a reconciliation interval value other than 0.



## Mutable but unreadable fields are actuated on change only

Some APIs expose fields that are not readable, but are mutable (for example, the password for a SQL user). Due to the inability to see if these fields have been modified, mutable but unreadable fields are updated only when the custom resource is modified.

## Resources are not recreated when modifying immutable fields

Some fields in a resource are immutable, and can't be reconciled without deleting, then re-creating the target resource.

In these situations, Config Connector emits an "UpdatedFailed" Kubernetes event for the resource rather than perform this re-creation. You must then delete and re-create the resource.

Example event:
    
    
    Warning  UpdateFailed  37m (x643 over 15d)    computeinstance-controller  Update call failed: the desired mutation for the following field(s) is invalid: [bootDisk.0.InitializeParams.0.Image networkInterface.0.NetworkIp]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
