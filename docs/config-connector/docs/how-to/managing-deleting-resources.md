---
url: https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources/
title: Managing and deleting resources \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:53.703326+00:00
---

# Managing and deleting resources  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managing and deleting resources

This page explains how Config Connector manages an existing resource and handles deleting resources.

When you define a resource by using Config Connector, one of the following actions occur:

  * If the resource doesn't exist, Config Connector creates the resource. For an example of creating a new resource, see [Getting started](https://docs.cloud.google.com/config-connector/docs/how-to/getting-started#create_spanner-instanceyaml).
  * If a resource with the same name already exists, Config Connector acquires that resource and starts managing it. Config Connector checks for the name in either the [organization, project, or folder](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview). This page explains in detail how Config Connector acquires, manages, and handles deletion of resources.



You can alternatively manage resources using the `resourceID` field. Some resources can be acquired only by using the `resourceID` field. Some resources can only be created as new resources and not acquired. To learn more, see [Managing resources with the `resourceID` field](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids).

## Acquiring an existing resource

This section describes how you acquire an existing resource with Config Connector, using a BigQuery resource as an example.

### Before you begin

  1. [Enable the BigQuery API](https://console.cloud.google.com/apis/library/bigquery.googleapis.com?q=bigquery).
  2. Confirm you have access to the [`bq`](https://docs.cloud.google.com/bigquery/docs/bq-command-line-tool) command line tool. If you don't have `bq`, use [Cloud Shell](https://console.cloud.google.com/kubernetes/list?cloudshell=true) or install it with the [gcloud CLI](https://docs.cloud.google.com/sdk/install).



### Acquiring a BigQuery dataset

Config Connector acquires, or takes control of, resources when the values in the manifest and the resource name match. If a resource does not have a name (for example, a Project ID), the ID of the resource is used.

By creating an empty BigQuery dataset and then acquiring the dataset with Config Connector, you learn how Config Connector handles existing resources.

  1. Create a BigQuery dataset named `bigquerydatasetsample` with `bq`.
         
         bq --location=US mk \
         --dataset \
         --default_table_expiration 3600 \
         --description description \
         PROJECT_ID:bigquerydatasetsample

  2. Copy the following contents into a file named `bq-sample.yaml`.
         
         apiVersion: bigquery.cnrm.cloud.google.com/v1beta1
           kind: BigQueryDataset
           metadata:
             name: bigquerydatasetsample
           spec:
             defaultTableExpirationMs: 3600000
             description: "BigQuery Dataset Sample"
             friendlyName: bigquerydataset-sample
             location: US
         

  3. Apply the yaml to your cluster.
         
         kubectl apply --namespace CC_NAMESPACE -f bq-sample.yaml

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

  4. Use `kubectl describe` to see details on the dataset.
         
         kubectl describe --namespace CC_NAMESPACE bigquerydataset bigquerydatasetsample

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

The output from `kubectl describe` includes metadata on the resource's status and ownership.




### Deleting the dataset

By default, after Config Connector acquires and manages a resource, deleting the object from your cluster will delete the resource. If you prefer to keep the dataset, set the resource's `deletion-policy`.

For example, deleting the manifest that acquired `bigquerydataset-sample` will delete the dataset from BigQuery.

  1. You can delete the `bigquerydataset-sample` dataset with `kubectl delete`.
         
         kubectl delete --namespace CC_NAMESPACE -f bq-sample.yaml

Replace `CC_NAMESPACE` with the namespace Config Connector manages resources from.

The output of `kubectl` confirms the deletion:
         
         bigquerydataset.bigquery.cnrm.cloud.google.com "bigquerydatasetsample" deleted
         

  2. Use `bq` to confirm the dataset no longer exists.
         
         bq show PROJECT_ID:bigquerydatasetsample

The output of the command includes `Not Found`.




### Keeping resources after deletion

**Warning:** When deleting a Config Connector resource the associated Google Cloud resource is deleted by default. To keep the Google Cloud resource, add the following to the Config Connector resource YAML before deleting:
    
    
    ...
    metadata:
      annotations:
        cnrm.cloud.google.com/deletion-policy: abandon
    ...
    

For example, the YAML for the BigQuery dataset described earlier including the `abandon` deletion policy is below:
    
    
    apiVersion: bigquery.cnrm.cloud.google.com/v1beta1
    kind: BigQueryDataset
    metadata:
      name: bigquerydatasetsample
      annotations:
        cnrm.cloud.google.com/deletion-policy: abandon
    spec:
      defaultTableExpirationMs: 3600000
      description: "BigQuery Dataset Sample"
      friendlyName: bigquerydataset-sample
      location: US
    

## Resources with restrictions around acquisition

Some resources can't be acquired following the instructions in the preceding section. This section details the limitations around acquisition for some resources.

### Resources with a service-generated resource ID

You can only acquire Google Cloud resources which have a [service-generated resource ID](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids#types_of_resource_ids) by using the `resourceID` field.

The following Config Connector resources correspond to Google Cloud resources which have a service-generated resource ID:

  * `AccessContextManagerAccessPolicy`
  * `ApigeeOrganization`
  * `BigQueryDataTransferConfig`
  * `BillingBudgetsBudget`
  * `CloudIdentityGroup`
  * `CloudIdentityMembership`
  * `ComputeFirewallPolicy`
  * `DLPDeidentifyTemplate`
  * `DLPInspectTemplate`
  * `DLPJobTrigger`
  * `DLPStoredInfoType`
  * `DataCatalogPolicyTag`
  * `DataCatalogTaxonomy`
  * `EssentialContactsContact`
  * `Folder`
  * `IAPBrand`
  * `IAPIdentityAwareProxyClient`
  * `IdentityPlatformTenant`
  * `MonitoringAlertPolicy`
  * `MonitoringGroup`
  * `MonitoringNotificationChannel`
  * `MonitoringUptimeCheckConfig`
  * `RecaptchaEnterpriseKey`
  * `ResourceManagerLien`
  * `SQLSSLCert`
  * `SecretManagerSecretVersion`
  * `StorageNotification`
  * `StorageTransferJob`
  * `TagsTagBinding`
  * `TagsTagKey`
  * `TagsTagValue`
  * `VertexAIDataset`
  * `VertexAIIndex`

**Note:** `Folder` is a special case. You can set its `resourceID` to the folder ID of an existing folder to acquire that folder. However, if you leave `resourceID` unspecified, `Folder` acquires the folder with the given `displayName` in the given parent folder/organization. If none can be found, then a new folder is created.

To learn about how to use the `resourceID` field, see [Managing resources with the resourceID field](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids).

### Resources that cannot be acquired

The following Config Connector resources do not have support for acquiring existing Google Cloud resources:

  * `DataflowFlexTemplateJob`
  * `FirestoreIndex`
  * `IAMServiceAccountKey`



## What's next

  * Learn about how Config Connector models Google Cloud resources with [Kubernetes constructs](https://docs.cloud.google.com/config-connector/docs/concepts/resources).
  * See the Google Cloud [resources](https://docs.cloud.google.com/config-connector/docs/reference/resources) Config Connector can manage.
  * See additional examples of how to use Config Connector on the [GitHub repository](https://github.com/GoogleCloudPlatform/k8s-config-connector).
  * Learn how Kubernetes handles [declarative configuration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/declarative-config/) of objects.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
