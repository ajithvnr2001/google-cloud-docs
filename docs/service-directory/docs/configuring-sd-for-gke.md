---
url: https://docs.cloud.google.com/service-directory/docs/configuring-sd-for-gke/
title: Configure Service Directory for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:08.035254+00:00
---

# Configure Service Directory for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/configuring-sd-for-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Configure Service Directory for GKE Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page provides information about how to configure Service Directory with Google Kubernetes Engine (GKE) and automatically register your GKE clusters with Service Directory. You can configure Service Directory for GKE with Autopilot GKE clusters or Standard GKE clusters. For information about the two modes, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

To learn more about Service Directory for GKE, see [Service Directory for GKE overview](https://docs.cloud.google.com/service-directory/docs/sd-gke-overview).

## Limitations

Service Directory for GKE has the following limitations:

  * You can only register services using the Service Directory-GKE integration. You must register ingresses, gateways, and other resources manually using the Service Directory API.
  * You must register your GKE clusters by using [Fleets](https://docs.cloud.google.com/anthos/multicluster-management/fleets) before you can sync services in those clusters to Service Directory. For details on how to register your GKE clusters, see [Registering a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).
  * All Service Directory resources are registered in the fleet project, not the project of the cluster.
  * You can not modify the Service Directory entities registered using this integration. You must make all changes to the GKE service resources themselves so that they propagate to Service Directory.



## Before you begin

  * Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 



  * You must register your GKE cluster to a fleet. To register your GKE cluster, follow the instructions in [Registering a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).



## Set up the GKE cluster

To set up the GKE cluster, follow these steps.

  * Enable the Service Directory GKE fleet feature.
  * Configure the Service Directory registration policy.
  * Deploy the GKE service.



### Enable the Service Directory GKE fleet feature

To enable the Service Directory GKE fleet feature, run the [`gcloud container hub`](https://docs.cloud.google.com/sdk/gcloud/reference/container/hub) command.

###  gcloud 
    
    
    gcloud alpha container hub service-directory enable
    

### Configure the Service Directory registration policy for the service

The registration policy defines what kinds of services within GKE are automatically imported by Service Directory. The following list shows the configurable options for this policy:

  * `resources`: the type of GKE resources that are imported. You can specify multiple resource types. Resources are identified by `Group` and `Kind`. By default, the `Group` is `core`. Only `Kind: service` is available.
  * `selector`: a GKE label selector which matches on key:value labels that are applied on the GKE resource. By default, no resources are selected.
  * `annotationsToSync`: the annotation keys on the resource that are synced to Service Directory. If this list is empty, then resources are synced to Service Directory without annotations.



Each namespace should define a single policy. This policy must have `name: "default"`. The Controller does not allow or reconcile other names.

#### Configure a `ServiceDirectoryRegistrationPolicy`.

The following manifest describes a `ServiceDirectoryRegistrationPolicy`:
    
    
    apiVersion: networking.gke.io/v1alpha1
    kind: ServiceDirectoryRegistrationPolicy
    metadata:
        # Only the name "default" is allowed.
        name: default
        # The ServiceDirectoryRegistrationPolicy is a namespaced resource
        namespace: NAMESPACE
    spec:
      resources:
        # Kind specifies the types of Kubernetes resources that can be synced into Service Directory.
        - kind: Service
          # Selector is a label selector for the resource types specified in Kind.
          selector:
            matchLabels:
              LABELS
          # annotationsToSync specifies the annotations that are matched and imported.
          # Any annotations that do not match this set of keys will not be imported into Service Directory.
          annotationsToSync:
          - ANNOTATIONS
          

Replace the following:

  * `NAMESPACE`: the name of the namespace. There can only be one `ServiceDirectoryRegistrationPolicy` in a namespace. If there are multiple policies in a single namespace, GKE chooses one policy to be the active policy and marks the others as inactive.
  * `LABELS`: the label selector, such as, `sd-import: "true"`. This value applies to resources specified in kind. By default, no resources are selected.
  * `ANNOTATIONS`: a list of annotations that are matched and imported, such as, `- cloud.google.com/load-balancer-type` If a selected GKE resource has one of the annotations in the list, the annotation and its values are synced to Service Directory with the resource. If this list is empty, then resources are synced to Service Directory without annotations.



Save the manifest as `registration_policy.yaml`.

#### Apply the manifest to your cluster

To apply the manifest to your cluster, run the `kubectl apply -f` command:
    
    
    kubectl apply -f registration_policy.yaml
    

### Deploy the GKE service

Deploy the GKE regional external passthrough Network Load Balancer service and application in your region's GKE cluster, for example, if your region is `us-central1`, deploy it in a GKE cluster `gke-us-central1`.

This imports your GKE service into Service Directory.

Create a YAML file and apply it like any other GKE resource. Here is a manifest for a service of type `LoadBalancer`:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: hello-app-service
      labels:
        sd-import: "true"
      annotations:
        cloud.google.com/load-balancer-type: "Internal"
    spec:
      type: LoadBalancer
      selector:
        app: hello
      ports:
      - name: tcp-port
        protocol: TCP
        port: 80
        targetPort: 8080
    

Here is a manifest for a `Deployment`:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        app: hello
      name: hello-app
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: hello
      template:
        metadata:
          labels:
            app: hello
        spec:
          containers:
          - image: gcr.io/google-samples/hello-app:1.0
            name: hello
            ports:
            - containerPort: 8080
              protocol: TCP
    

To verify, run the Service Directory query for your service by using the [`gcloud service-directory services resolve`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-directory/services/resolve) command:

###  gcloud 
    
    
    gcloud beta service-directory services resolve SERVICE_NAME \
      --location=LOCATION \
      --namespace=NAMESPACE
    

Replace the following:

  * `SERVICE_NAME`: the name or fully qualified identifier for the service, for example `hello-app-service`
  * `LOCATION`: the name of the region for the service, for example, `us-central1`
  * `NAMESPACE`: the name of the namespace for the service, for example, `default`



Your output shows your service and is similar to the following:
    
    
    service:
      endpoints:
      - address: 10.140.0.5
        metadata:
          cloud.google.com/load-balancer-type: "Internal"
        name: projects/my-project/locations/us-central1/namespaces/default/services/hello-app-service/endpoints/my-cluster-12345
        port: 80
        network: projects/123456789/locations/global/networks/default
      name: projects/my-project/locations/us-central1/namespaces/default/services/hello-app-service
    

## Billing

Service Directory does not charge for resources created by the GKE integration. However, there is a charge for the API calls. For pricing details, see [Service Directory pricing](https://cloud.google.com/service-directory/pricing).

## What's next

  * To get an overview of Service Directory, see the [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
