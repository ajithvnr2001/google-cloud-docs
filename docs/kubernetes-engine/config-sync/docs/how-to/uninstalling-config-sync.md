---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/uninstalling-config-sync/
title: Uninstall Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:11.572470+00:00
---

# Uninstall Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/uninstalling-config-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Uninstall Config Sync Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to uninstall Config Sync from your cluster, disable the Config Management fleet feature on your fleet, and uninstall the ConfigManagement Operator.

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

The Config Management fleet feature manages Config Sync using the ConfigManagement Operator. Because of this architecture, the uninstall steps must be completed in the following order:

  1. Uninstall Config Sync from your cluster
  2. Disable the Config Management feature on your fleet
  3. Uninstall the ConfigManagement Operator from your cluster

**Note:** If you use Config Controller to install and manage Config Sync, don't use the instructions on this page. Instead, follow the instructions in [Delete your Config Controller instance](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/setup#delete) to uninstall Config Controller.

## Uninstall Config Sync from your cluster

**Note:** Uninstalling Config Sync will delete all `RootSync` and `RepoSync` objects on the cluster. Before you continue, you should check the deletion propagation policies on your `RootSync` and `RepoSync` objects. For more information, see [Bulk delete objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects#bulk_delete_objects).

### Console

You can't uninstall Config Sync with only the Google Cloud console. Use Google Cloud CLI instead.

### gcloud

  1. Open the [applySpec manifest](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields) that you created during installation with the Google Cloud CLI. 

  2. In the applySpec manifest, set `spec.configSync.enabled` to `false`:
         
         applySpecVersion: 1
         spec:
           configSync:
             **enabled : false**
         ...
         

  3. Apply the changes:
         
         gcloud beta container fleet config-management apply \
               --membership=MEMBERSHIP_NAME \
               --config=CONFIG_YAML \
               --project=PROJECT_ID
         

Replace the following:

     * MEMBERSHIP_NAME: add the registered cluster that you want to apply this configuration to. If you registered the cluster in the Google Cloud console, the membership name is the same as the name of your cluster.

     * CONFIG_YAML: add the path to your `apply-spec.yaml` file.

     * PROJECT_ID: add your project ID.




### Terraform

If you used [Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html) to install Config Sync using a [gke_hub_feature_membership](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_membership) resource from the [Google Cloud Platform Provider](https://www.terraform.io/docs/providers/google/index.html), then update that resource to uninstall Config Sync. Don't use the `terraform destroy` command. The `terraform destroy` command doesn't fully uninstall Config Sync. Some components remain.

  1. Identify the `gke_hub_feature_membership` resource in your Terraform configuration files that has a `configmanagement` argument populated.

  2. Update the `gke_hub_feature_membership` resource to remove the `config_sync` argument from the `configmanagement`.

For example:
         
         resource "google_gke_hub_feature_membership" "feature_member" {
           location = "global"
           feature = google_gke_hub_feature.feature.name
           membership = google_gke_hub_membership.membership.membership_id
           membership_location = google_gke_hub_membership.membership.location
           configmanagement {
             version = "1.24.0"
           }
         }
         

  3. Apply the Terraform configuration:
         
         terraform apply
         

Confirm you want to apply the actions described by entering `yes`.




### Config Connector

If you used [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to install Config Sync using a [GKEHubFeatureMembership](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeaturemembership) resource, then update that resource to uninstall Config Sync.

  1. Identify the `GKEHubFeatureMembership` resource object on your cluster that has a `.spec.configmanagement.configSync` field populated.

  2. Patch the `GKEHubFeatureMembership` resource object to remove the `.spec.configmanagement.configSync` field by setting it to null:
         
         kubectl patch GKEHubFeatureMembership FEATURE_MEMBERSHIP_OBJECT_NAME \
             --namespace FEATURE_MEMBERSHIP_OBJECT_NAMESPACE \
             -p '{"spec":{"configmanagement":{"configSync": null}}}'
         

Replace the following:

     * FEATURE_MEMBERSHIP_OBJECT_NAME: add the name of the `GKEHubFeatureMembership` resource object that you previously created.

     * FEATURE_MEMBERSHIP_OBJECT_NAMESPACE: add the namespace that contains the `GKEHubFeatureMembership` resource object that you previously created.




## Disable Config Management on your fleet

**Note:** If you still want to use Config Management on other clusters in the Fleet, you can skip this step, but you won't be able to uninstall the ConfigManagement Operator until after the Config Management feature is disabled on the fleet or the cluster is removed from the fleet.

### Console

  1. In the Google Cloud console, go to the **Feature Manager** page. 

[Go to Feature Manager](https://console.cloud.google.com/kubernetes/features)

  2. In the **Config Management** row of the **Features** table, click **Details**. The **Status summary** page appears.

  3. Click **Disable Config Management**. A confirmation page appears.

  4. On the confirmation page, click **Disable Config Management**.




### gcloud

  1. To disable Config Management on all clusters in the fleet, run the following command:
         
         gcloud beta container fleet config-management disable
         

**Note:** The preceding commands don't stop status reporting. If you want to stop status reporting, you need to [unregister your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster).



### Terraform

If you used [Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html) to enable the Config Management feature on your fleet using a [google_gke_hub_feature](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_membership) resource from the from the [Google Cloud Platform Provider](https://www.terraform.io/docs/providers/google/index.html), then update that resource to disable Config Management on all clusters in the fleet.

  1. Update the HCL file that contains your `google_gke_hub_feature` resource to remove the `google_gke_hub_feature` resource.

  2. If you still have a `gke_hub_feature_membership` resource defined with a `feature` field that references the removed `google_gke_hub_feature`, remove that `gke_hub_feature_membership` resource too.

  3. Apply the Terraform configuration:
         
         terraform apply
         

Confirm you want to apply the actions described by entering `yes`.




### Config Connector

If you used [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to enable the Config Management feature on your fleet using a [GKEHubFeature](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeature) resource, then update that resource to disable Config Management on all clusters in the fleet.

  1. Identify the `GKEHubFeature` resource object on your cluster that has a `.spec.resourceID` value of `configmanagement`.

  2. If you still have a `GKEHubFeatureMembership` resource object defined with a `.spec.featureRef` field that references that `GKEHubFeature` resource object, delete it:
         
         kubectl delete GKEHubFeatureMembership FEATURE_MEMBERSHIP_OBJECT_NAME \
             --namespace FEATURE_MEMBERSHIP_OBJECT_NAMESPACE
         

Replace the following:

     * FEATURE_MEMBERSHIP_OBJECT_NAME: add the name of the `GKEHubFeatureMembership` resource object that you previously created.

     * FEATURE_MEMBERSHIP_OBJECT_NAMESPACE: add the namespace that contains the `GKEHubFeatureMembership` resource object that you previously created.

  3. Delete the `GKEHubFeature` resource from your cluster:
         
         kubectl delete GKEHubFeature FEATURE_OBJECT_NAME \
             --namespace FEATURE_OBJECT_NAMESPACE
         

Replace the following:

     * FEATURE_OBJECT_NAME: add the name of the `GKEHubFeature` resource object that you previously created.

     * FEATURE_OBJECT_NAMESPACE: add the namespace that contains the `GKEHubFeature` resource object that you previously created.




**Note:** Disabling the Config Management feature on your fleet does not automatically uninstall the ConfigManagement Operator from the clusters in the fleet. Proceed to the next section to uninstall the ConfigManagement Operator on each cluster.

## Uninstall the ConfigManagement Operator

Use `kubectl` to delete the ConfigManagement Operator after you disable Config Management feature on the fleet or [unregister your cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster) from the fleet.

To remove the ConfigManagement Operator, run the following commands:

  1. Delete the ConfigManagement object from the cluster:
         
         kubectl delete configmanagement --all
         

After you run this command, the following things happen:

     * Any ClusterRoles and ClusterRoleBindings created in the cluster by ConfigManagement Operator are deleted from the cluster.
     * Any admission controller configurations installed by ConfigManagement Operator are deleted.
     * The contents of the `config-management-system` namespace are deleted, with the exception of the [`git-creds` Secret](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#git-creds-secret), and for versions of Config Sync beginning in 1.9.0, the `config-management-operator` Deployment, and the `config-management-operator` Pod. ConfigManagement Operator cannot function without the `config-management-system` namespace. Any CustomResourceDefinitions (CRDs) created or modified by ConfigManagement Operator controller are removed from the clusters where they were created or modified. The CRD required to run ConfigManagement Operator still exists because from the point of view of Kubernetes, they were added by the user who installed ConfigManagement Operator. Information about removing these components is covered in the next step.
  2. If you need to retain the `git-creds` Secret, do that now:
         
         kubectl -n config-management-system get secret git-creds -o yaml
         

  3. Delete the `config-management-system` namespace:
         
         kubectl delete ns config-management-system
         

  4. Delete the `config-management-monitoring` namespace:
         
         kubectl delete ns config-management-monitoring
         

  5. Delete the ConfigManagement CustomResourceDefinition:
         
         kubectl delete crd configmanagements.configmanagement.gke.io
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
