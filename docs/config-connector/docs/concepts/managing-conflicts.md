---
url: https://docs.cloud.google.com/config-connector/docs/concepts/managing-conflicts/
title: Managing conflicts with multiple Config Connector resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:44.540282+00:00
---

# Managing conflicts with multiple Config Connector resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/managing-conflicts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing conflicts with multiple Config Connector resources

This page describes how Config Connector handles conflicts. Conflicts can happen when the same resource is managed by multiple resources.

Config Connector [manages or acquires](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources) resources by mapping the combination of Kubernetes resource name, container annotation, and if applicable, region or location. In the simplest case, you organize your resources with Google Cloud [projects](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects).

Google Cloud supports additional levels of hierarchy beyond projects: folders, projects, and organizations. You can map resources to your [folders, projects, and organizations](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview) with an annotation. When you create a resource without an annotation using Config Connector, the resource is created in the project that shares the resource's namespace.

It is possible, but not recommended, to create two Config Connector resources in different namespaces that manage the same Google Cloud resource. Config Connector only manages the corresponding Google Cloud resource if it is able to obtain a lease on the Google Cloud resource and conflict prevention is enabled.

Leases are namespace-scoped. To obtain a namespace-scoped lease, Config Connector adds two labels to the resource:

  1. `cnrm-lease-holder-id`: Config Controller generates a unique ID for each namespace that manages a resource with conflict prevention enabled. This unique ID is what's used to set `cnrm-lease-holder-id`. To see the mapping of the namespace to the `cnrm-lease-holder-id` value, you can look at the `namespace-id` ConfigMap in the `cnrm-system` namespace.
  2. `cnrm-lease-expiration`: An expiration time in [Unix epoch time](https://en.wikipedia.org/wiki/Unix_time).



Config Connector is able to update these values if any of the following is true:

  * The value of `cnrm-lease-holder-id` matches the namespace's globally unique ID.
  * The value of `cnrm-lease-holder-id` is empty or non-existent.
  * The value of `cnrm-lease-expiration` is in the past.



When a Config Connector instance obtains a lease on a resource, the expiration time is set to 40 minutes in the future. The same instance of Config Connector retains management as long as the resource is in the namespace. Config Connector extends the expiration time by 40 minutes when less than 20 minutes remain.

If Config Connector is unable to obtain a lease on a given resource, the output of [`kubectl describe`](https://docs.cloud.google.com/config-connector/docs/how-to/get-resource-info#describing_a_resource) on the resource lists a Status of `ManagementConflict`.

## Modifying conflict prevention

You can control conflict prevention by adding the `cnrm.cloud.google.com/management-conflict-prevention-policy` annotation to the resource with one of the following values:

  * `resource`: management conflicts are prevented at the resource level by saving the appropriate lease labels into the resource as described in the preceding section.
  * `none`: management conflicts are not prevented.



The default value is `none`.

In the following example, a manifest for the default ComputeNetwork uses a management policy of `none`, which means that conflicts are not prevented:
    
    
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
     annotations:
       cnrm.cloud.google.com/management-conflict-prevention-policy: "none"
       cnrm.cloud.google.com/project-id: "PROJECT-ID"
       cnrm.cloud.google.com/deletion-policy: "abandon"
     name: default
    spec:
     description: Default network for the project
    

## Limitations

Conflict prevention has the following limitations:

  * Conflict prevention does not work for resources that don't support labels. Even if you change the value from `none` to `resource`, it still doesn't work.

  * If you are [Managing resources with the resourceID field](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids) you can create multiple resources with the same Google Cloud resource name, created under the same namespace. These resources create conflicts that Config Connector cannot manage.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
