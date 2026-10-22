---
url: https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally/
title: Manage fields externally \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:51.720142+00:00
---

# Manage fields externally  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage fields externally

**Caution:** For CustomResourceDefinitions (CRDs) added in [version 1.114.0 and later](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/master/config/crds/resources), externally managed fields aren't populated by default.

When Config Connector creates a resource on Google Cloud, fields left unspecified in the `spec` field take on values from the API unless they aren't readable, such as fields that aren't available with an HTTP GET request.

In this case, the field is considered _externally managed_ because Kubernetes isn't the source of truth for this value.

## Behavior with server-side apply

If [server-side apply](https://kubernetes.io/docs/reference/using-api/api-concepts/#server-side-apply) is enabled for the resource, the values of externally managed fields in the object are updated continuously to match the underlying Google Cloud resource.

If a field in the `spec` section of the applied configuration has a value, the field isn't externally managed.

If the field is removed, the field is externally managed.

**Note:** For list fields, this behavior doesn't apply. Instead, list fields follow the Behavior without server-side apply.

## Behavior without server-side apply

If server-side apply isn't enabled and the resource uses the `Merge` populating behavior, Config Connector populates unspecified fields in the resource `spec` field with the value read from the Google Cloud API and enforces those initially populated values.

For example, suppose you apply a resource configuration without setting a value for the `field2` field in the `spec` section:
    
    
    spec:
        field1: "value-1"
    

If the value of the `field2` field is `"api-value-1"` in the Google Cloud API, the resource in the [API server](https://kubernetes.io/docs/concepts/overview/components/#kube-apiserver) is populated with that value:
    
    
    # object in the api-server
    spec:
        field1: "value-1"
        field2: "api-value-1"  # populated by first reconciliation
    

If the Google Cloud resource is modified directly so that the `field2` field is now `"api-value-2"`, Config Connector reverts the Google Cloud resource to the value that was initially populated in the resource `spec` field (`"api-value-1"`):
    
    
    # object in the api-server
    spec:
        field1: "value-1"
        # still the originally populated value; overrides the external value
        field2: "api-value-1"
    

## Behavior for list fields in resource spec

Due to a technical limitation in Config Connector, list fields in your resource configuration can't be managed externally by default when the resource uses the `Merge` populating behavior. Because of this limitation, Config Connector takes ownership of list fields in the resource `spec` field, even when you don't specify the field in your original resource configuration.

When you apply a resource `spec` field, Config Connector reads the value of list fields from the Google Cloud API and treats this initial value as the source of truth and target state. If the value in that list field changes outside of Config Connector, Config Connector tries to revert the change, which might not be intended.

To bypass this limitation and let list fields be managed externally, use the `cnrm.cloud.google.com/state-into-spec: absent` annotation to [ignore unspecified fields](https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields). The value of this annotation is set to `absent` by default for newly created resources in Config Connector version 1.123.1 and later. To see if your resource supports the annotation, check the corresponding [resource reference page](https://docs.cloud.google.com/config-connector/docs/reference/resources).

To configure this behavior, add the following annotation to your resource manifest:
    
    
    metadata:
      annotations:
        cnrm.cloud.google.com/state-into-spec: absent
    

When you set the value of the `state-into-spec` annotation to `absent`, Config Connector ignores list fields that aren't specified in your resource configuration so that they can be managed externally.

## Caveats

Fields that are managed by Config Connector and automatically updated by external services can trigger endless updates or reconciliation errors on the underlying API. These issues can occur when the underlying Google Cloud API has autoscaling or automatically updated fields and your resource uses the `cnrm.cloud.google.com/state-into-spec: merge` annotation without server-side apply.

For example, if a SQLInstance resource uses the `cnrm.cloud.google.com/state-into-spec: merge` annotation, Config Connector populates the instance's initial `spec.maintenanceVersion` field into the Kubernetes resource `spec` field. When Cloud SQL later performs an automatic maintenance update on the underlying instance, Config Connector attempts to revert the instance to the older `spec.maintenanceVersion` value stored in the `spec` field. Because Cloud SQL rejects maintenance version downgrades, reconciliation fails repeatedly with an `UpdateFailed` error.

To let external services manage automatically updated fields, do the following:

  * Omit the automatically updated field from your YAML configuration file when you apply it.
  * Configure the resource to ignore unspecified fields by doing one of the following: 
    * Set the `cnrm.cloud.google.com/state-into-spec: absent` annotation on the resource, or [migrate the existing resource from the `Merge` behavior to the `Absent` behavior](https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields#migrate-from-merge-to-absent).
    * Enable server-side apply for the resource.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
