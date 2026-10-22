---
url: https://docs.cloud.google.com/config-connector/docs/how-to/install-manually/
title: Install Config Connector manually \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:37.045184+00:00
---

# Install Config Connector manually  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/install-manually/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Install Config Connector manually

This page explains how to manually install Config Connector. Manual installation is a flexible option that gives you control over the installed version and upgrade schedule.

The instructions on this page are focused on installing Config Connector on Google Kubernetes Engine (GKE) clusters. For more information about the different installation options, see [Choosing an installation type](https://docs.cloud.google.com/config-connector/docs/concepts/installation-types).

For most use cases, you should manually install Config Connector in **namespaced mode**. The alternative is **cluster mode**. Namespaced mode is more scalable and offers better permission isolation, which makes it the recommended mode for multi-tenant clusters or for managing resources across multiple projects. In multi-tenant environments, avoid cluster mode. Cluster mode uses a single, shared Identity and Access Management (IAM) service account. Any user who can create Config Connector resources in any namespace can act with the full IAM permissions of that service account.

If you prefer a single, cluster-wide service account, instead follow the instructions for installing in **cluster mode**.

## Before you begin

Before you manually install the Config Connector operator, complete the following steps:

  * Create or identify a GKE cluster where Config Connector has not yet been installed and that has [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_new_cluster) and [Kubernetes Engine Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/installing) enabled.
  * [Configure `kubectl` to connect to your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl).



## Install the Config Connector operator

Config Connector uses a [Kubernetes operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) to keep its installation up to date. Installing the operator is required whether you're installing Config Connector in namespaced mode or cluster mode.

To install the Config Connector operator, complete the following steps:

  1. Download the latest Config Connector operator .tar file:
         
         gcloud storage cp gs://configconnector-operator/latest/release-bundle.tar.gz release-bundle.tar.gz
         

**Note:** Keep a copy of the installation bundle as you need this bundle to uninstall Config Connector.
  2. Extract the tar file:
         
         tar zxvf release-bundle.tar.gz
         

  3. Install the Config Connector operator on your cluster:

###  Autopilot 
         
         kubectl apply -f operator-system/autopilot-configconnector-operator.yaml
         

###  Standard 
         
         kubectl apply -f operator-system/configconnector-operator.yaml
         

  4. To configure the Config Connector operator to run in namespaced mode, complete the following steps:

     1. Create a manifest named `configconnector.yaml` with the following content:
            
            apiVersion: core.cnrm.cloud.google.com/v1beta1
            kind: ConfigConnector
            metadata:
              # the name is restricted to ensure that there is only ConfigConnector resource installed in your cluster
              name: configconnector.core.cnrm.cloud.google.com
            spec:
              mode: namespaced
              stateIntoSpec: Absent
            

     2. Apply the manifest to your cluster:
            
            kubectl apply -f configconnector.yaml
            




## Install Config Connector in namespaced mode

**Note:** You must perform these steps for every namespace that you want Config Connector to create resources from.

In the following sections, the project where you install Config Connector is the _host project_. The other projects where you can have Config Connector manage resources are _managed projects_. The host and managed project can be the same project, if you want Config Connector to only create resources in the same project as your cluster.

### Create a namespace

Create a new namespace by running the following command:
    
    
    kubectl create namespace NAMESPACE
    

Replace NAMESPACE with a name for the namespace.

### Create an identity

Create an IAM service account and create a binding between the IAM Service Account and the Config Connector Kubernetes service account by completing the following steps:

  1. Create an IAM service account. If you have an existing service account, you can use it instead of creating a new service account. Use `gcloud` to create the service account by running the following command:
         
         gcloud iam service-accounts create NAMESPACE_GSA --project HOST_PROJECT_ID
         

Replace the following:

     * NAMESPACE_GSA with the name of the Google service account (GSA) bound to your namespace.
     * HOST_PROJECT_ID with your host project's ID.

To learn more about creating service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

  2. Give the IAM service account elevated permissions on your _managed_ project:
         
         gcloud projects add-iam-policy-binding MANAGED_PROJECT_ID \
             --member="serviceAccount:NAMESPACE_GSA@HOST_PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/owner"
         

Replace MANAGED_PROJECT_ID with your managed project's ID.

**Note:** If you prefer to grant [editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) access to the project replace `roles/owner` with `roles/editor`. Granting the editor role allows most Config Connector functionality except Project or Organization wide configurations such as IAM modifications.
  3. Create an IAM policy binding between the IAM service account and the Config Connector Kubernetes service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
             NAMESPACE_GSA@HOST_PROJECT_ID.iam.gserviceaccount.com \
             --member="serviceAccount:HOST_PROJECT_ID.svc.id.goog[cnrm-system/cnrm-controller-manager-NAMESPACE]" \
             --role="roles/iam.workloadIdentityUser"
         

  4. Give the IAM service account permissions to publish Prometheus metrics to Google Cloud Observability on your _host_ project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member="serviceAccount:NAMESPACE_GSA@HOST_PROJECT_ID.iam.gserviceaccount.com" \
             --role="roles/monitoring.metricWriter"
         




### Create a ConfigConnectorContext

To create Google Cloud resources, configure Config Connector to watch your namespace by adding a `ConfigConnectorContext` object in that namespace.

To create a `ConfigConnectorContext`, complete the following steps:

  1. Create a manifest named `configconnectorcontext.yaml` with the following content:
         
         apiVersion: core.cnrm.cloud.google.com/v1beta1
         kind: ConfigConnectorContext
         metadata:
           # you need one ConfigConnectorContext per namespace
           name: configconnectorcontext.core.cnrm.cloud.google.com
           namespace: NAMESPACE
         spec:
           googleServiceAccount: "NAMESPACE_GSA@HOST_PROJECT_ID.iam.gserviceaccount.com"
           stateIntoSpec: Absent
         

  2. Apply the manifest to your cluster:
         
         kubectl apply -f configconnectorcontext.yaml
         

  3. Verify that the Config Connector operator created a Kubernetes service account for your namespace by running the following command:
         
         kubectl get serviceaccount/cnrm-controller-manager-NAMESPACE  -n cnrm-system
         

  4. Verify that the Config Connector controller Pod is running for your namespace:
         
         kubectl wait -n cnrm-system \
             --for=condition=Ready pod \
             -l cnrm.cloud.google.com/component=cnrm-controller-manager \
             -l cnrm.cloud.google.com/scoped-namespace=NAMESPACE
         

If the Config Connector controller is running, the output is similar to:
         
         cnrm-controller-manager-abcdefghijk-0 condition met.
         




### Stop managing resources in a namespace

If you want Config Connector to stop managing resources in a namespace, remove all Config Connector resources and the `ConfigConnectorContext` object in that namespace.

  1. To find all Config Connector resources in your namespace, for each Config Connector Custom Resource Definition, list all resources.
         
         kubectl get gcp -n NAMESPACE
         

The output of this command lists all Custom Resource Definitions (CRDs) that represent a resource managed by Config Connector in that namespace, including the name and Kubernetes kind of that resource.

  2. To remove all Config Connector resources, for each resource in the output of the previous step, run the following command:
         
         kubectl delete -n NAMESPACE KIND NAME
         

Replace the following:

     * `KIND`: the Kubernetes kind of the resource.
     * `NAME`: the name of the resource.
  3. Delete the `ConfigConnectorContext` object in your namespace.
         
         kubectl delete -n NAMESPACE ConfigConnectorContext configconnectorcontext.core.cnrm.cloud.google.com
         

**Important:** Don't delete the `ConfigConnectorContext` object until all Config Connector-managed resources are deleted.



### Uninstall Config Connector

To uninstall Config Connector, complete the following steps:

  1. To remove the Config Connector CRDs and controller components, run the following command:
         
         kubectl delete ConfigConnectorContext --all -A –wait=false
         
         kubectl delete ConfigConnector configconnector.core.cnrm.cloud.google.com \
             --wait=true
         

  2. To uninstall the Config Connector operator, run the following command:
         
         kubectl delete -f operator-system/configconnector-operator.yaml  --wait=true
         




## Install in cluster mode

You might prefer to install and manage Config Connector in cluster mode if you want to manage resources within a single project and don't require the permission separation that namespaced mode provides.

### Create an identity

Config Connector creates and manages Google Cloud resources by authenticating with an Identity and Access Management (IAM) service account and using Workload Identity Federation for GKE to bind IAM service accounts with Kubernetes service accounts.

**Note:** You need to perform these steps only once per cluster.

To create the identity, complete the following steps:

  1. Create an IAM service account. If you want to use an existing service account, you can use that account and skip this step:
         
         gcloud iam service-accounts create SERVICE_ACCOUNT_NAME
         

Replace SERVICE_ACCOUNT_NAME with a name for your service account.

To learn more about creating service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

  2. Give the IAM service account elevated permissions on your project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/editor"
         

Replace PROJECT_ID with your project ID.

**Note:** Granting the editor role allows most Config Connector functionality except project and organization wide configurations such as IAM modifications. In a production environment, we recommend that you set more granular permissions. For more information about IAM roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).
  3. Create an IAM policy binding between the IAM service account and the predefined Kubernetes service account that Config Connector runs:
         
         gcloud iam service-accounts add-iam-policy-binding \
         SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
           --member="serviceAccount:PROJECT_ID.svc.id.goog[cnrm-system/cnrm-controller-manager]" \
           --role="roles/iam.workloadIdentityUser"
         




### Configure Config Connector

To complete the installation, create a configuration file for the `ConfigConnector` [CustomResource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), then apply it using the `kubectl apply` command. The Config Connector Operator installs Google Cloud resource CRDs and Config Connector components in your cluster.

To configure the operator as cluster mode, complete the following steps: 

  1. Copy the following YAML file into a file named `configconnector.yaml`: 
         
         # configconnector.yaml
         apiVersion: core.cnrm.cloud.google.com/v1beta1
         kind: ConfigConnector
         metadata:
           # the name is restricted to ensure that there is only one
           # ConfigConnector resource installed in your cluster
           name: configconnector.core.cnrm.cloud.google.com
         spec:
           mode: cluster
           googleServiceAccount: "SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"
           # Setting `stateIntoSpec` to `Absent` is recommended. It means setting `cnrm.cloud.google.com/state-into-spec`
           # annotation to `absent` for all Config Connector resources created in the cluster in the future.
           # It prevents Config Connector from populating unspecified fields into the spec.
           stateIntoSpec: Absent

Replace the following: 
     * `SERVICE_ACCOUNT_NAME` with your service account's name.
     * `PROJECT_ID` with your project ID.
  2. Apply the configuration to your cluster with `kubectl apply`: 
         
         kubectl apply -f configconnector.yaml




### Specifying where to create your resources

Config Connector can organize resources by project, folder, or organization, which is the same way you would organize resources with Google Cloud.

Before creating resources with Config Connector, you must configure where to create your resources. To determine where to create the resource, Config Connector uses an annotation on either the resource configuration or an existing Namespace. For more information, see [Organizing resources](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/overview).

If you do not have a Namespace for this purpose, create one with `kubectl`. 
    
    
    kubectl create namespace NAMESPACE

Replace `NAMESPACE` with your namespace name. For example `config-connector`.

Select a tab to choose where you want Config Connector to create resources.

### Project

To [create resources in a certain project](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/project-scoped-resources), run the following command:
    
    
        kubectl annotate namespace \
        NAMESPACE cnrm.cloud.google.com/project-id=PROJECT_ID

Replace the following: 

  * `NAMESPACE` with your namespace name.
  * `PROJECT_ID` with your Google Cloud project ID.



### Folder

To [create resources in a certain folder](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/folder-scoped-resources), run the following command:
    
    
        kubectl annotate namespace \
        NAMESPACE cnrm.cloud.google.com/folder-id=FOLDER_ID

Replace the following: 

  * `NAMESPACE` with your namespace name.
  * `FOLDER_ID` with your Google Cloud folder ID.



### Organization

To [create resources in a certain organization](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/organization-scoped-resources), run the following command:
    
    
        kubectl annotate namespace \
        NAMESPACE cnrm.cloud.google.com/organization-id=ORGANIZATION_ID

Replace the following: 

  * `NAMESPACE` with your namespace name.
  * `ORGANIZATION_ID` with your Google Cloud organization ID.



When you annotate your namespace, Config Connector creates resources in the corresponding project, folder or organization. To learn more about how Config Connector uses Kubernetes namespaces, see [Kubernetes Namespaces and Google Cloud projects](https://docs.cloud.google.com/config-connector/docs/concepts/namespaces-and-projects). 

### Verify your installation

Config Connector runs all of its components in a namespace named `cnrm-system`. You can verify the Pods are ready by running the following command: 
    
    
    kubectl wait -n cnrm-system \
          --for=condition=Ready pod --all
    

If Config Connector is installed correctly, the output is similar to the following: 
    
    
    pod/cnrm-controller-manager-0 condition met

Note: The controller Pod can take several minutes to start. 

### Uninstall Config Connector

To uninstall Config Connector, complete the following steps:

  1. To remove the Config Connector CRDs and controller components, run the following command:
         
         kubectl delete ConfigConnector configconnector.core.cnrm.cloud.google.com \
             --wait=true
         

  2. To uninstall the Config Connector operator, run the following command:
         
         kubectl delete -f operator-system/configconnector-operator.yaml  --wait=true
         




## Upgrade Config Connector

To download and install the latest version of Config Connector operator, run the following command:
    
    
    gcloud storage cp gs://configconnector-operator/latest/release-bundle.tar.gz release-bundle.tar.gz
    tar zxvf release-bundle.tar.gz
    kubectl apply -f operator-system/configconnector-operator.yaml
    

## Downgrade Config Connector

Fully downgrading Config Connector is not supported. To downgrade both the Config Connector operator and CRDs, you must uninstall, reinstall Config Connector, and then re-apply your resources.

In Config Connector version 1.123.1 and later, you can roll back the operator version for installations that use [namespaced mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced). In each namespace that has an operator you want to roll back, set the `spec.version` field in the `ConfigConnectorContext` object to the previous Config Connector version.

You can roll back the Config Connector controller by a maximum of 3 minor versions. You must always roll back to the latest patch version for a given minor version.

## Upgrade from non-operator installations

Config Connector version 1.33.0 and higher only supports installation with the [GKE add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall), or the operator.

To upgrade to the operator (and retain all Config Connector resources), you must remove all Config Connector system components except the CRDs, and then install the operator.

  1. Run the following commands to remove Config Connector system non-CRD components:
         
         kubectl delete sts,deploy,po,svc,roles,clusterroles,clusterrolebindings --all-namespaces -l cnrm.cloud.google.com/system=true --wait=true
         kubectl delete validatingwebhookconfiguration abandon-on-uninstall.cnrm.cloud.google.com --ignore-not-found --wait=true
         kubectl delete validatingwebhookconfiguration validating-webhook.cnrm.cloud.google.com --ignore-not-found --wait=true
         kubectl delete mutatingwebhookconfiguration mutating-webhook.cnrm.cloud.google.com --ignore-not-found --wait=true
         

  2. Install Config Connector with the [GKE add-on](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall), or the [operator](https://docs.cloud.google.com/config-connector/docs/how-to/advanced-install#manual).




## Switch from the add-on to a manual installation

When installed as an add-on, the version of Config Connector is directly tied to the GKE version that is installed.

The manual installation allows for faster updates at the cost of manual upgrades.

To switch installation methods and safely retain your resources, complete the following steps:

  1. Disable the addon _without_ deleting any `ConfigConnector` or `ConfigConnectorContext` objects:
         
         gcloud container clusters update CLUSTER_NAME --update-addons ConfigConnector=DISABLED
         

Replace `CLUSTER_NAME` with the name of the cluster that you installed Config Connector on.

  2. [Install the manual operator of the chosen version](https://docs.cloud.google.com/config-connector/docs/how-to/advanced-install#installing_the_operator).

To prevent potential CRD validation errors (for example, `KNV2009: Invalid value: "v1beta1": must appear in spec.versions`), the chosen version of the manual operator must be the same or later than the version you were using for the add-on. Downgrading the manual operator version can cause errors (for example, KNV2009) because the GKE add-on might have already upgraded certain CRDs to a later Config Connector version.


**Note:** Because the `namespace-id` `ConfigMap` in the `configconnector-operator-system` namespace is deleted as part of disabling the add-on, old `cnrm-controller-manager` `StatefulSets` are recreated.

## What's next

  * [Get started](https://docs.cloud.google.com/config-connector/docs/how-to/getting-started) with Config Connector.
  * [Learn about best practices](https://docs.cloud.google.com/config-connector/docs/best-practices) for Config Connector.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
