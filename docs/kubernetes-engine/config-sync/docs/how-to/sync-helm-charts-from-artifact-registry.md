---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-helm-charts-from-artifact-registry/
title: Sync Helm charts from Artifact Registry \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:06.456583+00:00
---

# Sync Helm charts from Artifact Registry  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-helm-charts-from-artifact-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Sync Helm charts from Artifact Registry Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to sync Helm charts from Artifact Registry by creating and pushing a Helm chart to a repository in Artifact Registry. It also contains a sample configuration to sync a chart from your Helm repository.

**Key Term:** **Helm** is a package manager for Kubernetes that helps you define, install, and upgrade applications. Config Sync can sync Helm charts directly from Artifact Registry by using the Helm API, or render Helm charts specified within Kustomize configurations.

You can configure Config Sync to sync from [Helm](https://helm.sh/) repositories. You can store Helm charts in [Artifact Registry](https://docs.cloud.google.com/artifact-registry), which is the recommended Helm repository for Google Cloud. To use this feature, you must enable the [RootSync and RepoSync APIs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields). Config Sync renders Helm charts by using [`helm template`](https://helm.sh/docs/helm/helm_template/) and therefore does not support full Helm lifecycle management.

[Bundled Helm and Kustomize versions](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#bundled_helm_and_kustomize_versions) lists the Kustomize and Helm versions bundled with the corresponding version of Config Sync.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE, Config Sync, Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com  anthosconfigmanagement.googleapis.com  artifactregistry.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the GKE, Config Sync, Artifact Registry APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com  anthosconfigmanagement.googleapis.com  artifactregistry.googleapis.com

  14. Create, or have access to, a cluster that meets the [requirements for Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/cluster-requirements) and is on the latest version of Config Sync.
  15. [Install the `nomos` CLI or upgrade it to the latest version.](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#installing)
  16. [Install Helm 3.8.0 or later](https://helm.sh/docs/intro/install/). In previous versions of Helm, support for charts in OCI format is an experimental feature.
  17. Enable [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable-existing-cluster) on your cluster.



## Limitations

  * You can't change any immutable field in a config by just changing the value in the source of truth. If you need to update an immutable field, first make the change in the source of truth, then manually delete the object in the cluster. Config Sync can then re-create the object with the new field value.

  * The following Helm charts include Jobs and aren't recommended for deployment by Config Sync:

    * [`secrets-store-csi-driver`](https://secrets-store-csi-driver.sigs.k8s.io/getting-started/installation)
    * [`cert-manager`](https://cert-manager.io/docs/installation/helm/)

To learn more about why Jobs aren't recommended for use with Config Sync, see [Avoid managing Jobs with Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices#avoid-jobs).




## Create an Artifact Registry repository

In this section, you create an Artifact Registry repository. To learn more about creating Artifact Registry repositories, see [Create repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).

  1. Enable the Artifact Registry API:
         
         gcloud services enable artifactregistry.googleapis.com --project=PROJECT_ID
         

  2. Create an Artifact Registry repository:
         
         gcloud artifacts repositories create AR_REPO_NAME \
            --repository-format=docker \
            --location=AR_REGION \
            --description="Config Sync Helm repo" \
            --project=PROJECT_ID
         




Replace the following:

  * `PROJECT_ID`: the organization's project ID.
  * `AR_REPO_NAME`: the ID of the repository.
  * `AR_REGION`: the regional or multi-regional location of the repository.



Variables used in the following sections:

  * `FLEET_HOST_PROJECT_NUMBER`: if you're using GKE Workload Identity Federation for GKE, this is the same as the project number for `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project number of the fleet that your cluster is registered to.
  * `FLEET_HOST_PROJECT_ID`: if you're using GKE Workload Identity Federation for GKE, this is the same as `PROJECT_ID`. If you're using fleet Workload Identity Federation for GKE, this is the project ID of the fleet that your cluster is registered to.
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount for the reconciler: 
    * For root repositories, if the `RootSync` name is `root-sync`, add `root-reconciler`. Otherwise, add `root-reconciler-ROOT_SYNC_NAME`.
    * For namespace repositories, if the `RepoSync` name is `repo-sync`, add `ns-reconciler-NAMESPACE`. Otherwise, add `ns-reconciler-NAMESPACE-REPO_SYNC_NAME-REPO_SYNC_NAME_LENGTH` where `REPO_SYNC_NAME_LENGTH` is the number of characters in `REPO_SYNC_NAME`.



## Grant reader permission

Grant the Artifact Registry Reader role (`roles/artifactregistry.reader`) on the repository to the Kubernetes ServiceAccount:
    
    
    gcloud artifacts repositories add-iam-policy-binding AR_REPO_NAME \
        --location=AR_REGION \
        --member="principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_HOST_PROJECT_ID.svc.id.goog/subject/ns/config-management-system/sa/KUBERNETES_SERVICEACCOUNT" \
        --role=roles/artifactregistry.reader \
        --project=PROJECT_ID \
        --condition=None
    

## Push a Helm chart to the Artifact Registry repository

In this section, you download a public Helm chart and push it to Artifact Registry.

  1. Retrieve the `mysql-9.3.1.tgz` package from the public Helm repository and download it locally:
         
         helm pull mysql --repo https://charts.bitnami.com/bitnami --version 9.3.1
         

  2. Authenticate with an access token:

### Linux / macOS
         
         gcloud auth print-access-token | helm registry login -u oauth2accesstoken \
         --password-stdin https://AR_REGION-docker.pkg.dev
         

### Windows
         
         gcloud auth print-access-token
         ya29.8QEQIfY_...
         
         helm registry login -u oauth2accesstoken -p "ya29.8QEQIfY_..." \
         https://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME
         

In this command, `oauth2accesstoken` is the username to use when authenticating with an access token and `gcloud auth print-access-token` is the command to obtain the access token. Your access token is the password for authentication. Authentication with an access token is the safest [authentication method](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication#methods).

  3. Push the Helm chart to Artifact Registry:
         
         helm push mysql-9.3.1.tgz oci://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME
         




## Configure Config Sync to sync from your Helm chart

In this section, you create a RootSync object and configure Config Sync to sync from the Helm chart.

If you want to override the Helm chart's default values, you can do this by either specifying values in the `spec.helm.values` field or by adding a reference to a [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/) by using the `spec.helm.valuesFileRefs` field. To learn more about the optional fields, see [Configuration for the Helm repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

**Tip:** if you want to use the chart's default values, you can use either example and omit the `spec.helm.values` or `spec.helm.valuesFileRefs` fields.

### values

  1. Create a RootSync object with a unique name:
         
         cat <<EOF>> ROOT_SYNC_NAME.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceFormat: unstructured
           sourceType: helm
           helm:
             repo: oci://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME
             chart: mysql
             version: 9.3.1
             releaseName: my-mysql
             namespace: test
             auth: k8sserviceaccount
             # Use the optional field spec.helm.values to override default values.
             # You can use the same format as the default values file to override
             # default values.
             values:
               image:
                 pullPolicy: Always
               primary:
                 resources:
                   limits:
                     cpu: 250m
                     memory: 256Mi
                   requests:
                     cpu: 250m
                     memory: 256Mi
         EOF
         

Replace `ROOT_SYNC_NAME` with the name of your RootSync object. The name should be unique in the cluster and have no more than 26 characters. If you [installed Config Sync using the Google Cloud console or Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync), choose a name other than `root-sync`.

In this example, the Helm chart is deployed in the `test` namespace because its resources contain `namespace: {{ .Release.Namespace }}` in its templates.

You can use `helm.values` to override the default values. To learn about the optional fields, see [Configuration for the Helm repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#configuration_for_the_helm_repository).

  2. Apply the RootSync object:
         
         kubectl apply -f ROOT_SYNC_NAME.yaml
         

  3. Verify that Config Sync is syncing from the image:
         
         nomos status --contexts=$(kubectl config current-context)
         

The output is similar to the following:
         
         Connecting to clusters...
         
         *cluster-name
           --------------------
           <root>:root-sync   oci://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME/mysql:9.3.1
           SYNCED             9.3.1
           Managed resources:
               NAMESPACE  NAME                       STATUS    SOURCEHASH
               default    configmap/my-mysql         Current   9.3.1
               default    secret/my-mysql            Current   9.3.1
               default    service/my-mysql           Current   9.3.1
               default    service/my-mysql-headless  Current   9.3.1
               default    serviceaccount/my-mysql    Current   9.3.1
               default    statefulset.apps/my-mysql  Current   9.3.1
         

You have now successfully synced the Helm chart to your cluster.




### valuesFileRefs

  1. Create a RootSync object with a unique name:
         
         cat <<EOF>> ROOT_SYNC_NAME.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceFormat: unstructured
           sourceType: helm
           helm:
             repo: oci://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME
             chart: mysql
             version: 9.3.1
             releaseName: my-mysql
             auth: k8sserviceaccount
             # use the optional field spec.helm.valuesFilesRefs to override default values
             # by referencing a ConfigMap
             valuesFileRefs:
             - name: CONFIGMAP_NAME
               dataKey: DATA_KEY
         
         EOF
         

Replace the following:

     * `ROOT_SYNC_NAME`: the name of your RootSync object. The name should be unique in the cluster and have no more than 26 characters. If you [installed Config Sync using the Google Cloud consoleor Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync), choose a name other than `root-sync`.
     * `CONFIGMAP_NAME`: the name of your ConfigMap. This can be any valid ConfigMap name accepted by Kubernetes that is unique in your cluster.
     * (optional) `DATA_KEY`: the data key in your ConfigMap that you would like to read the values from. The default is `values.yaml`.
  2. Create the ConfigMap object with your values:

**Note:** the ConfigMap is immutable and must be in the same namespace as the RootSync or RepoSync that references it.
         
         cat <<EOF>> CONFIGMAP_NAME.yaml
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: CONFIGMAP_NAME
           namespace: config-management-system
         immutable: true
         # You can use the same format as the default values file to override
         # default values.
         data:
           DATA_KEY: |-
             image:
               pullPolicy: Always
             primary:
               resources:
                 limits:
                   cpu: 250m
                   memory: 256Mi
                 requests:
                   cpu: 250m
                   memory: 256Mi
         
         EOF
         

If you didn't specify a value for `DATA_KEY` in the RootSync, it should be the default `values.yaml`.

  3. Apply the ConfigMap object:
         
         kubectl apply -f CONFIGMAP_NAME.yaml
         

  4. Apply the RootSync object:
         
         kubectl apply -f ROOT_SYNC_NAME.yaml
         

  5. Verify that Config Sync is syncing from the image:
         
         nomos status --contexts=$(kubectl config current-context)
         

The output is similar to the following:
         
         Connecting to clusters...
         
         *cluster-name
           --------------------
           <root>:root-sync   oci://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME/mysql:9.3.1
           SYNCED             9.3.1
           Managed resources:
               NAMESPACE  NAME                       STATUS    SOURCEHASH
               default    configmap/my-mysql         Current   9.3.1
               default    secret/my-mysql            Current   9.3.1
               default    service/my-mysql           Current   9.3.1
               default    service/my-mysql-headless  Current   9.3.1
               default    serviceaccount/my-mysql    Current   9.3.1
               default    statefulset.apps/my-mysql  Current   9.3.1
         

You have now successfully synced the Helm chart to your cluster.

You can also look at the `imagePullPolicy` in one of the synced resources in the cluster to verify that the values from the ConfigMap were used to render the chart:
         
         kubectl get statefulset -n test my-mysql -o yaml | grep imagePullPolicy
         

  6. Because the ConfigMap is immutable, to change the values, you must create a new ConfigMap and update `spec.helm.valuesFileRefs` in the RootSync or RepoSync spec to point to the new ConfigMap. Creating a new ConfigMap ensures changes to values cause the Helm chart to re-render, which is useful when multiple ConfigMaps referenced in `spec.helm.valuesFileRefs` need to be updated at the same time when re-rendering. To change the values that are used to render your chart, create a new ConfigMap with a different name:
         
         cat <<EOF>> CONFIGMAP_NAME-2.yaml
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: CONFIGMAP_NAME-2
           namespace: config-management-system
         immutable: true
         # You can use the same format as the default values file to override
         # default values.
         data:
           DATA_KEY: |-
             image:
               pullPolicy: Never
             primary:
               resources:
                 limits:
                   cpu: 100m
                   memory: 256Mi
                 requests:
                   cpu: 250m
                   memory: 200Mi
         
         EOF
         

  7. Update your RootSync object to reference the new ConfigMap:
         
         cat <<EOF>> ROOT_SYNC_NAME.yaml
         apiVersion: configsync.gke.io/v1beta1
         kind: RootSync
         metadata:
           name: ROOT_SYNC_NAME
           namespace: config-management-system
         spec:
           sourceFormat: unstructured
           sourceType: helm
           helm:
             repo: oci://AR_REGION-docker.pkg.dev/PROJECT_ID/AR_REPO_NAME
             chart: mysql
             version: 9.3.1
             releaseName: my-mysql
             namespace: test
             auth: k8sserviceaccount
             # use the optional field spec.helm.valuesFilesRefs to override default values
             # by referencing a ConfigMap
             valuesFileRefs:
             - name: CONFIGMAP_NAME-2
               dataKey: DATA_KEY
         
         EOF
         

  8. Apply the ConfigMap object:
         
         kubectl apply -f CONFIGMAP_NAME-2.yaml
         

  9. Apply the RootSync object:
         
         kubectl apply -f ROOT_SYNC_NAME.yaml
         

  10. Verify that Config Sync is syncing from the image:
         
         nomos status --contexts=$(kubectl config current-context)
         

You can also look at the `imagePullPolicy` in one of the synced resources in the cluster to verify that the new values from the updated ConfigMap were used to render the chart:

**Note:** it can take a few minutes for the resources to fully sync.
         
         kubectl get statefulset -n test my-mysql -o yaml | grep imagePullPolicy
         




## What's next

  * Learn more about [installing Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
