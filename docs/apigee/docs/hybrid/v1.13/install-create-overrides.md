---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-overrides/
title: Step 6: Create the overrides \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:49:49.644153+00:00
---

# Step 6: Create the overrides  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-overrides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 6: Create the overrides Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-create-overrides.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-create-overrides.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-create-overrides.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-overrides.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-create-overrides.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-create-overrides.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-create-overrides.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-overrides.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-create-overrides.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-create-overrides.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-create-overrides.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-create-overrides.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-create-overrides.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-create-overrides.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-create-overrides.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-create-overrides.html)



##  Specify configuration overrides 

The Apigee hybrid installer uses defaults for many settings. However, there are a few settings that do not have defaults. You must provide values for these settings, as explained next. 

### Before you begin

We recommend you review the following scenarios to determine if you want to configure your cluster for them. These configurations are optional. 

  * If you are planning on installing hybrid in multiple regions, read [Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-region) before continuing.
  * Apigee hybrid provides default passwords for the Cassandra users. Apigee recommends changing the default user passwords. See [Configuring TLS for Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-tls) for details. 
  * If you want to configure the storage and heap settings for Cassandra, see [ Configure storage and heap settings](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production). 
  * As described in [Part 1: Project and Org setup--Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-enableapi), For production installation scenarios, configure [persistent solid state disk (SSD)](https://docs.cloud.google.com/compute/docs/disks#pdspecs) storage for Cassandra. Apigee does not support using [local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) for Apigee hybrid. For details, see [Add SSD storage for production deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production#add-ssd-storage-for-production-deployments). 



### Configure the cluster

By convention, configuration overrides are written in a file named `overrides.yaml` typically stored in your `$APIGEE_HELM_CHARTS_HOME` directory. 

**Note:** The `overrides.yaml` file will be used during upgrades, expansions and anytime you need to alter the configuration of your hybrid runtime installation. Apigee recommends you store this file in a source control repository with version control. 

  1. Create a new file named **`overrides.yaml`** in your `$APIGEE_HELM_CHARTS_HOME` directory. 

The `overrides.yaml` provides the configuration for your unique Apigee hybrid installation. The overrides file in this step provides a basic configuration for a small-footprint hybrid runtime installation, suitable for your first installation. 

  2. In `overrides.yaml`, add the required property values, shown below. A detailed description of each property is provided below. 

Select the tab for your installation, production, **Production** or non-production (demo, evaluation, or proof-of-concept installations), **Non-prod** depending on your choice in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts).

For installations in production environments, look at the storage requirements for the Cassandra database in [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production).

If you are installing Apigee hybrid on GKE and you plan to use Workload Identity to authenticate hybrid components, select either the **Prod: Workload Identity** or **Non-prod: Workload Identity** tab to configure your `overrides.yaml` file. 

### Production

Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below.

There are differences between the different platforms for the Google Cloud project region and Kubernetes cluster region. Choose the platform where you are installing Apigee hybrid. 
         
         instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
         namespace: APIGEE_NAMESPACE # Usually "apigee"
         
         gcp:
           projectID: PROJECT_ID
           region: ANALYTICS_REGION
         
         k8sCluster:
           name: CLUSTER_NAME
           region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
         org: ORG_NAME
         
         # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
         contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
         
         # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
         newDataPipeline:
           debugSession: true
           analytics: true
         
         envs:
         - name: ENVIRONMENT_NAME
           serviceAccountPaths:
             # Provide the path relative to the apigee-env chart directory.
             synchronizer: SYNCHRONIZER_SERVICE_ACCOUNT_FILEPATH
             # For example: "PROJECT_ID _-apigee-synchronizer.json_ "
             runtime: RUNTIME_SERVICE_ACCOUNT_FILEPATH
             # For example: "PROJECT_ID _-apigee-runtime.json_ "
             udca: UDCA_SERVICE_ACCOUNT_FILEPATH
             # For example: "PROJECT_ID _-apigee-udca.json_ "
         
         cassandra:
           hostNetwork: false
             # Set to **_false_** for single region installations and multi-region installations
             # with connectivity between pods in different clusters, for example GKE installations.
             # Set to **_true_**  for multi-region installations with no communication between
             # pods in different clusters, for example Google Distributed Cloud on VMware or bare metal, GKE on AWS,
             # AKS, EKS, and OpenShift installations.
             # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-region#prerequisites)
           replicaCount: 3
             # Use multiples of 3 for production.
             # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production) for guidelines.
           storage:
             capacity: 500Gi
           resources:
             requests:
               cpu: 7
               memory: 15Gi
           maxHeapSize: 8192M
           heapNewSize: 1200M
             # Minimum storage requirements for a production environment.
             # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production).
         
         ingressGateways:
         - name: INGRESS_NAME # maximum 17 characters.
           replicaCountMin: 2
           replicaCountMax: 10
           svcAnnotations:  # optional. If you are on AKS, see [Known issue #260772383](https://docs.cloud.google.com/apigee/docs/release/known-issues#260772383)
             SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
         
         virtualhosts:
         - name: ENVIRONMENT_GROUP_NAME
           selector:
             app: apigee-ingressgateway
             ingress_name: INGRESS_NAME
           sslCertPath: PATH_TO_CERT_FILE
           sslKeyPath: PATH_TO_KEY_FILE
         
         mart:
           serviceAccountPath: MART_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-org chart directory.
             # For example: "PROJECT_ID _-apigee-mart.json_ "
         
         connectAgent:
           serviceAccountPath: MART_SERVICE_ACCOUNT_FILEPATH
             # **Use the same service account for mart and connectAgent**
             # Provide the path relative to the apigee-org chart directory.
             # For example: "PROJECT_ID _-apigee-mart.json_ "
         
         logger:
           enabled: true
             # enabled by default
             # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sa-about#recommended-sas).
           serviceAccountPath: LOGGER_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-telemetry chart directory.
             # For example: "PROJECT_ID _-apigee-logger.json_ "
         
         metrics:
           serviceAccountPath: METRICS_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-telemetry chart directory.
             # For example: "PROJECT_ID _-apigee-metrics.json_ "
         
         udca:
           serviceAccountPath: UDCA_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-org chart directory.
             # For example: "PROJECT_ID _-apigee-udca.json_ "
         
         watcher:
           serviceAccountPath: WATCHER_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-org chart directory.
             # For example: "PROJECT_ID _-apigee-watcher.json_ "
         

### Non-prod

Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below.

There are differences between the different platforms for the Google Cloud project region and Kubernetes cluster region. Choose the platform where you are installing Apigee hybrid. 
         
         instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
         namespace: APIGEE_NAMESPACE # Usually "apigee"
         
         gcp:
           projectID: PROJECT_ID
           region: ANALYTICS_REGION
         
         k8sCluster:
           name: CLUSTER_NAME
           region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
         org: ORG_NAME
         
         # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
         contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
         
         # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
         newDataPipeline:
           debugSession: true
           analytics: true
         
         envs:
         - name: ENVIRONMENT_NAME
           serviceAccountPaths:
             # Provide the path relative to the apigee-env chart directory.
             synchronizer: NON_PROD_SERVICE_ACCOUNT_FILEPATH
               # For example: "PROJECT_ID _-apigee-non-prod.json_ "
             runtime: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
             udca: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         
         cassandra:
           hostNetwork: false
             # Set to **_false_** for single region installations and multi-region installations
             # with connectivity between pods in different clusters, for example GKE installations.
             # Set to **_true_**  for multi-region installations with no communication between
             # pods in different clusters, for example Google Distributed Cloud on VMware or bare metal, GKE on AWS,
             # AKS, EKS, and OpenShift installations.
             # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-region#prerequisites)
           replicaCount: 1
             # Use 1 for non-prod or "demo" installations and multiples of 3 for production.
             # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production) for guidelines.
         
         ingressGateways:
         - name: INGRESS_NAME # maximum 17 characters.
           replicaCountMin: 2
           replicaCountMax: 10
           svcAnnotations:  # optional. If you are on AKS, see [Known issue #260772383](https://docs.cloud.google.com/apigee/docs/release/known-issues#260772383)
             SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
         
         virtualhosts:
         - name: ENVIRONMENT_GROUP_NAME
           selector:
             app: apigee-ingressgateway
             ingress_name: INGRESS_NAME
           sslCertPath: PATH_TO_CERT_FILE
           sslKeyPath: PATH_TO_KEY_FILE
         
         mart:
           serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
           # Provide the path relative to the chart directory.
           # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         
         connectAgent:
           serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-org chart directory.
             # **Use the same service account for mart and connectAgent**
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         
         logger:
           enabled: true
             # enabled by default
             # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sa-about#recommended-sas).
           serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-telemetry chart directory.
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         
         metrics:
           serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-telemetry chart directory.
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         
         udca:
           serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-org chart directory.
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         
         watcher:
           serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
             # Provide the path relative to the apigee-org chart directory.
             # For example: "PROJECT_ID _-apigee-non-prod.json_ "
         

### Prod: Workload Identity

This template is for Production installations on GKE using Workload Identity. Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below.

If you are installing Apigee hybrid on **GKE** , you have an alternative to authenticate and make requests to Google APIs, **Workload Identity**. For overviews of Workload Identity, see:

     * [ Introducing Workload Identity: Better authentication for your GKE applications](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications)
     * [Using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

To use Workload Identity with Apigee hybrid on GKE, use this template and then follow the steps in [Step 10: Install Apigee hybrid using Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-helm-charts) to create the Kubernetes service accounts and associate them with the Google service accounts you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts). 

**Tip:** You can find the email address of your service accounts with the following command: 
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"
    
    instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: true
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
    org: ORG_NAME
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
    newDataPipeline:
      debugSession: true
      analytics: true
    
    envs:
    - name: ENVIRONMENT_NAME
      gsa:
        synchronizer: "SYNCHRONIZER_SERVICE_ACCOUNT_EMAIL"
          # For example: "apigee-synchronizer@PROJECT_ID.iam.gserviceaccount.com"
        runtime: "RUNTIME_SERVICE_ACCOUNT_EMAIL"
          # For example: "apigee-runtime@PROJECT_ID.iam.gserviceaccount.com"
        udca: "UDCA_SERVICE_ACCOUNT_EMAIL"
          # For example: "apigee-udca@PROJECT_ID.iam.gserviceaccount.com"
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and multi-region installations
        # with connectivity between pods in different clusters, for example GKE installations.
        # Set to **_true_**  for multi-region installations with no communication between
        # pods in different clusters, for example Google Distributed Cloud on VMware or bare metal, GKE on AWS,
        # AKS, EKS, and OpenShift installations.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production) for guidelines.
      storage:
        capacity: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production).
      backup:
        enabled: true
        # Set to true for initial installation.
        # This triggers the chart to create the apigee-cassandra-backup Kubernetes service account when you install it.
        # See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-backup-overview) for instructions on using cassandra.backup.
    
    ingressGateways:
    - name: INGRESS_NAME # maximum 17 characters.
      replicaCountMin: 2
      replicaCountMax: 10
      svcAnnotations:  # optional. If you are on AKS, see [Known issue #260772383](https://docs.cloud.google.com/apigee/docs/release/known-issues#260772383)
        SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
    
    virtualhosts:
    - name: ENVIRONMENT_GROUP_NAME
      selector:
        app: apigee-ingressgateway
        ingress_name: INGRESS_NAME
      sslCertPath: PATH_TO_CERT_FILE
      sslKeyPath: PATH_TO_KEY_FILE
    
    mart:
      gsa: "MART_SERVICE_ACCOUNT_EMAIL"
        # For example: "apigee-mart@PROJECT_ID.iam.gserviceaccount.com"
    
    connectAgent:
      gsa: "MART_SERVICE_ACCOUNT_EMAIL"
        # **Use the same service account for mart and connectAgent**
        # For example: "apigee-mart@PROJECT_ID.iam.gserviceaccount.com"
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/sa-about#recommended-sas).
       gsa: "LOGGER_SERVICE_ACCOUNT_EMAIL"
        # For example: "apigee-logger@PROJECT_ID.iam.gserviceaccount.com"
    metrics:
      gsa: "METRICS_SERVICE_ACCOUNT_EMAIL"
        # For example: "apigee-metrics@PROJECT_ID.iam.gserviceaccount.com"
    
    udca:
      gsa: "UDCA_SERVICE_ACCOUNT_EMAIL"
        # For example: "apigee-udca@PROJECT_ID.iam.gserviceaccount.com"
    
    watcher:
      gsa: "WATCHER_SERVICE_ACCOUNT_EMAIL"
        # For example: "apigee-watcher@PROJECT_ID.iam.gserviceaccount.com"
    

### Non-prod: Workload Identity

This template is for Non-Production installations on GKE using Workload Identity. Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below.

If you are installing Apigee hybrid on **GKE** , you have an alternative to authenticate and make requests to Google APIs, **Workload Identity**. For overviews of Workload Identity, see:

     * [ Introducing Workload Identity: Better authentication for your GKE applications](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications)
     * [Using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

To use Workload Identity with Apigee hybrid on GKE, use this template and then follow the steps in [Step 10: Install Apigee hybrid using Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-helm-charts) to create the Kubernetes service accounts and associate them with the Google service accounts you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts). 

**Tip:** You can find the email address of your `apigee-non-prod` service account with the following command: 
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee-non-prod"
    
    instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: true
        gsa: "NON_PROD_SERVICE_ACCOUNT_EMAIL"
        # For example: "apigee-non-prod@PROJECT_ID.iam.gserviceaccount.com"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
    org: ORG_NAME
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
    newDataPipeline:
      debugSession: true
      analytics: true
    
    instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
    
    cassandra:
      hostNetwork: false
        # **_false_** for all GKE installations.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod or "demo" installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-production) for guidelines.
      backup:
        enabled: true
        # Set to true for initial installation.
        # This triggers the chart to create the apigee-cassandra-backup Kubernetes service account when you install it.
        # See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-backup-overview) for instructions on using cassandra.backup.
    
    virtualhosts:
    - name: ENVIRONMENT_GROUP_NAME
      selector:
        app: apigee-ingressgateway
        ingress_name: INGRESS_NAME
      sslCertPath: PATH_TO_CERT_FILE
      sslKeyPath: PATH_TO_KEY_FILE
    
    ingressGateways:
    - name: INGRESS_NAME # maximum 17 characters.
      replicaCountMin: 2
      replicaCountMax: 10
      svcAnnotations:  # optional. If you are on AKS, see [Known issue #260772383](https://docs.cloud.google.com/apigee/docs/release/known-issues#260772383)
        SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
      svcLoadBalancerIP: SVC_LOAD_BALANCER_IP  # optional
    
    envs:
    - name: ENVIRONMENT_NAME
    
    logger:
      enabled: false # Set to **_false_** for all GKE installations.
    

### Example

The following example shows a completed overrides file with example property values added:
    
    instanceID: "my_hybrid_example"
    namespace: apigee
    
    gcp:
      projectID: hybrid-example
      region: us-central1
    
    k8sCluster:
      name: apigee-hybrid
      region: us-central1
    
    org: hybrid-example
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/using-data-residency-with-apigee-hybrid):
    newDataPipeline:
      debugSession: true
      analytics: true
    
    envs:
    - name: test
      serviceAccountPaths:
        synchronizer:my-hybrid-project-apigee-synchronizer.json
        runtime: my-hybrid-project-apigee-runtime.json
        udca: my-hybrid-project-apigee-udca.json
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
    
    ingressGateways:
    - name: my-ingress-1
      replicaCountMin: 2
      replicaCountMax: 10
    
    virtualhosts:
    - name: example-env-group
      selector:
        app: apigee-ingressgateway
        ingress_name: my-ingress-1
        sslCertPath: certs/keystore.pem
        sslKeyPath: certs/keystore.key
    
    logger:
      enabled: true # Set to "false" for GKE. Set to "true" for all other Kubernetes platforms.
      serviceAccountPath: my-hybrid-project-apigee-logger.json
    
    mart:
      serviceAccountPath: my-hybrid-project-apigee-mart.json
    
    connectAgent:
      serviceAccountPath: my-hybrid-project-apigee-mart.json
    
    metrics:
      serviceAccountPath: my-hybrid-project-apigee-metrics.json
    
    udca:
      serviceAccountPath: my-hybrid-project-apigee-udca.json
    
    watcher:
      serviceAccountPath: my-hybrid-project-apigee-watcher.json
    

  3. When you are finished, save the file.



The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster.  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`.  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-provision). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously.  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`.  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`.  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`.  
CONTROL_PLANE_LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.devsite.corp.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-provision).  
ENVIRONMENT_GROUP_NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file.   
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 5: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key  
  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 

  * Have a maximum length of 17 characters
  * Contain only lowercase alphanumeric characters, '-' or '.'
  * Start with an alphanumeric character
  * End with an alphanumeric character

See [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref#ingressgateways-name) in the Configuration property reference   
SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-expose-apigee-ingress). Comment out or delete this section if you are not using it.  
SVC_LOAD_BALANCER_IP | (Optional). An IP address you have reserved for your load balancer. On platforms that support specifying the load balancer IP address, the load balancer will be created with this IP address. On platforms that do not allow you to specify the load balancer IP, this property is ignored. **Note:** You do not need to set `LoadBalancerIP` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-expose-apigee-ingress). In production installations, it is recommended to create your own Kubernetes service. Comment out or delete this section if you are not using it.  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-add-environment).   
***_SERVICE_ACCOUNT_FILEPATH** | The path and filename account of the service account JSON files in your corresponding chart directory. Provide the names with the path relative to the chart directory. For example: 

  * If the `my-hybrid-project-apigee-synchronizer.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
        
        synchronizer:  "my-hybrid-project-apigee-synchronizer.json"

  * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
        
        synchronizer:  "service-accounts/my-hybrid-project-apigee-synchronizer.json"


For non-production environments, the name of the single service account is `PROJECT_ID-non-prod.json` by default. For production environments, the name of the service account key file that you generated with the `create-service-account` tool in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts). You can see the service account files in each corresponding chart directory. The default names of the and corresponding chart directories for the service accounts are: | Service account | file name | Chart directory  
---|---|---  
Storage Object Admin | `PROJECT_ID-apigee-cassandra.json` | `apigee-datastore/`  
Logs Writer | `PROJECT_ID-apigee-logger.json` | `apigee-telemetry/`  
Apigee Connect Agent | `PROJECT_ID-apigee-mart.json` | `apigee-org/`  
Monitoring Metric Writer | `PROJECT_ID-apigee-metrics.json` | `apigee-telemetry/`  
No role required | `PROJECT_ID-apigee-runtime.json` | `apigee-env/`  
Apigee Synchronizer Manager | `PROJECT_ID-apigee-synchronizer.json` | `apigee-env/`  
Apigee Analytics Agent | `PROJECT_ID-apigee-udca.json` | `apigee-org/`  
Apigee Runtime Agent | `PROJECT_ID-apigee-watcher.json` | `apigee-org/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.  
***_SERVICE_ACCOUNT_EMAIL** | The service account email addresses for the Google service accounts (GSA) you need to supply if you are using [Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/enable-workload-identity-gke). These are the service accounts you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts). You can find the email addresses for the service accounts with the following command: 
    
    
    gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee"  
  
**Note:** If you want to create a security perimeter around your cluster and related Cloud services, you can configure one using Google Cloud [ Virtual Private Cloud (VPC) Service Controls](https://cloud.google.com/vpc-service-controls) with Apigee hybrid. See [ Using VPC Service Controls with Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) for instructions.

##  Summary 

The configuration file tells Kubernetes how to deploy the hybrid components to a cluster. Next, you will enable synchronizer access so the Apigee runtime and management planes will be able to communicate. 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-overrides) [(NEXT) Step 7: Enable Synchronizer access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-helm-charts) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
