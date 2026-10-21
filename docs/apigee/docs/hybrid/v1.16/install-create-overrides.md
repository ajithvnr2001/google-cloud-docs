---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides/
title: Step 7: Create the overrides \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:34:07.525913+00:00
---

# Step 7: Create the overrides  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 7: Create the overrides Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

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

  * If you are planning on installing hybrid in multiple regions, read [Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region) before continuing.
  * Apigee hybrid provides default passwords for the Cassandra users. Apigee recommends changing the default user passwords. See [Configuring TLS for Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-tls) for details. 
  * If you want to configure the storage and heap settings for Cassandra, see [ Configure storage and heap settings](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production). 
  * As described in [Part 1: Project and Org setup--Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-enableapi), For production installation scenarios, configure [persistent solid state disk (SSD)](https://docs.cloud.google.com/compute/docs/disks#pdspecs) storage for Cassandra. Apigee does not support using [local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) for Apigee hybrid. For details, see [Add SSD storage for production deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production#add-ssd-storage-for-production-deployments). 



### Configure the cluster

By convention, configuration overrides are written in a file named `overrides.yaml` typically stored in your `$APIGEE_HELM_CHARTS_HOME` directory. 

**Note:** The `overrides.yaml` file will be used during upgrades, expansions and anytime you need to alter the configuration of your hybrid runtime installation. Apigee recommends you store this file in a source control repository with version control. 

  1. Create a new file named **`overrides.yaml`** in your `$APIGEE_HELM_CHARTS_HOME` directory. 

The `overrides.yaml` provides the configuration for your unique Apigee hybrid installation. The overrides file in this step provides a basic configuration for a small-footprint hybrid runtime installation, suitable for your first installation. 

  2. In `overrides.yaml`, add the required property values, shown below. A detailed description of each property is provided below. 

Make sure the `overrides.yaml` file has the following structure and syntax. 

Choose the relevant tab for the type of service account authentication you are using in your installation: [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). 

     * Service account keys in Kubernetes Secrets: **Kubernetes Secrets**
     * Service account JSON key files: **JSON files**
     * Service account keys in Vault: **Vault**
     * Workload Identity Federation for GKE: **WIF for GKE**
     * Workload Identity Federation: **WIF on other platforms**

For an overview of the different authentication options, see [Service account authentication methods in Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-authentication-methods).

Select the tab for your installation, production, **Production** or non-production (demo, evaluation, or proof-of-concept installations), **Non-prod** depending on your choice in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts).

For installations in production environments, look at the storage requirements for the Cassandra database in [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).

### Kubernetes Secrets

### Production

### Template
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretRefs:
        synchronizer: SYNCHRONIZER_SERVICE_ACCOUNT_SECRET
          # For example: "_apigee-synchronizer-svc-account_ "
        runtime: RUNTIME_SERVICE_ACCOUNT_SECRET
          # For example: "_apigee-runtime-svc-account_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
    
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
    
    guardrails:
      serviceAccountRef: GUARDRAILS_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-guardrails-svc-account_ "
    
    mart:
      serviceAccountRef: MART_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-mart-svc-account_ "
    
    connectAgent:
      serviceAccountRef: MART_SERVICE_ACCOUNT_SECRET
        # Use the same secret for mart and connectAgent
        # For example: "_apigee-mart-svc-account_ "
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
      serviceAccountRef: LOGGER_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-logger-svc-account_ "
    
    metrics:
      serviceAccountRef: METRICS_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-metrics-svc-account_ "
    
    watcher:
      serviceAccountRef: WATCHER_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-watcher-svc-account_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountRef: MINT_TASK_SCHEDULER_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-mint-task-scheduler-svc-account_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
SECRET | The name of the Kubernetes secret you for the service account key in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `apigee-cassandra-svc-account`
     * `apigee-guardrails-svc-account`
     * `apigee-logger-svc-account`
     * `apigee-mart-svc-account`
     * `apigee-metrics-svc-account`
     * `apigee-mint-task-scheduler-svc-account`
     * `apigee-runtime-svc-account`
     * `apigee-synchronizer-svc-account`
     * `apigee-watcher-svc-account`

### Non-prod

     * `apigee-non-prod-svc-account`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      serviceAccountSecretRefs:
        synchronizer: "apigee-synchronizer-svc-account"
        runtime: "apigee-runtime-svc-account"
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
    
    guardrails:
      serviceAccountRef: "apigee-guardrails-svc-account"
    
    mart:
      serviceAccountRef: "apigee-mart-svc-account"
    
    connectAgent:
      serviceAccountRef: "apigee-mart-svc-account"
    
    logger:
      enabled: true
      serviceAccountRef: "apigee-logger-svc-account"
    
    metrics:
      serviceAccountRef: "apigee-metrics-svc-account"
    
    watcher:
      serviceAccountRef: "apigee-watcher-svc-account"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountRef: apigee-mint-task-scheduler-svc-account
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
SECRET | The name of the Kubernetes secret you for the service account key in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `apigee-cassandra-svc-account`
     * `apigee-guardrails-svc-account`
     * `apigee-logger-svc-account`
     * `apigee-mart-svc-account`
     * `apigee-metrics-svc-account`
     * `apigee-mint-task-scheduler-svc-account`
     * `apigee-runtime-svc-account`
     * `apigee-synchronizer-svc-account`
     * `apigee-watcher-svc-account`

### Non-prod

     * `apigee-non-prod-svc-account`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### Non-prod

### Template
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretRefs:
        synchronizer: NON_PROD_SERVICE_ACCOUNT_SECRET
          # For example: "_apigee-non-prod-svc-account_ "
        runtime: NON_PROD_SERVICE_ACCOUNT_SECRET
          # For example: "_apigee-non-prod-svc-account_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    guardrails:
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-non-prod-svc-account_ "
    
    mart:
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-non-prod-svc-account_ "
    
    connectAgent:
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # Use the same secret for mart and connectAgent
        # For example: "_apigee-non-prod-svc-account_ "
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-non-prod-svc-account_ "
    
    metrics:
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-non-prod-svc-account_ "
    
    watcher:
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-non-prod-svc-account_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountRef: NON_PROD_SERVICE_ACCOUNT_SECRET
        # For example: "_apigee-non-prod-svc-account_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
SECRET | The name of the Kubernetes secret you for the service account key in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `apigee-cassandra-svc-account`
     * `apigee-guardrails-svc-account`
     * `apigee-logger-svc-account`
     * `apigee-mart-svc-account`
     * `apigee-metrics-svc-account`
     * `apigee-mint-task-scheduler-svc-account`
     * `apigee-runtime-svc-account`
     * `apigee-synchronizer-svc-account`
     * `apigee-watcher-svc-account`

### Non-prod

     * `apigee-non-prod-svc-account`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
      serviceAccountSecretRefs:
        synchronizer: "apigee-non-prod-svc-account"
        runtime: "apigee-non-prod-svc-account"
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
    
    guardrails:
      serviceAccountRef: "apigee-non-prod-svc-account"
    
    mart:
      serviceAccountRef: "apigee-non-prod-svc-account"
    
    connectAgent:
      serviceAccountRef: "apigee-non-prod-svc-account"
    
    logger:
      enabled: true
      serviceAccountRef: "apigee-non-prod-svc-account"
    
    metrics:
      serviceAccountRef: "apigee-non-prod-svc-account"
    
    watcher:
      serviceAccountRef: "apigee-non-prod-svc-account"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountRef: apigee-non-prod-svc-account
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
SECRET | The name of the Kubernetes secret you for the service account key in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `apigee-cassandra-svc-account`
     * `apigee-guardrails-svc-account`
     * `apigee-logger-svc-account`
     * `apigee-mart-svc-account`
     * `apigee-metrics-svc-account`
     * `apigee-mint-task-scheduler-svc-account`
     * `apigee-runtime-svc-account`
     * `apigee-synchronizer-svc-account`
     * `apigee-watcher-svc-account`

### Non-prod

     * `apigee-non-prod-svc-account`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### JSON files

### Production

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountPaths:
        # Provide the path relative to the apigee-env chart directory.
        synchronizer: SYNCHRONIZER_SERVICE_ACCOUNT_FILEPATH
          # For example: "PROJECT_ID _-apigee-synchronizer.json_ "
        runtime: RUNTIME_SERVICE_ACCOUNT_FILEPATH
          # For example: "PROJECT_ID _-apigee-runtime.json_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
    
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
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
      serviceAccountPath: LOGGER_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-F chart directory.
        # For example: "PROJECT_ID _-apigee-logger.json_ "
    
    guardrails:
      serviceAccountPath: GUARDRAILS_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-operator chart directory.
        # For example: "PROJECT_ID _-apigee-guardrails.json_ "
    
    mart:
      serviceAccountPath: MART_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "PROJECT_ID _-apigee-mart.json_ "
    
    connectAgent:
      serviceAccountPath: MART_SERVICE_ACCOUNT_FILEPATH
        # Use the same service account for mart and connectAgent
        # Provide the path relative to the apigee-org chart directory.
        # For example: "PROJECT_ID _-apigee-mart.json_ "
    
    metrics:
      serviceAccountPath: METRICS_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "PROJECT_ID _-apigee-metrics.json_ "
    
    watcher:
      serviceAccountPath: WATCHER_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "PROJECT_ID _-apigee-watcher.json_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountPath: MINT_TASK_SCHEDULER_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "PROJECT_ID _-apigee-mint-task-scheduler.json_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
FILEPATH | The path and filename account of the service account JSON files in your corresponding chart directory. Provide the names with the path relative to the chart directory. For example: 
     * If the `my-project-apigee-synchronizer.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

For non-production environments, the name of the single service account is `PROJECT_ID-non-prod.json` by default. For production environments, the name of the service account key file that you generated with the `create-service-account` tool in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). You can see the service account files in each corresponding chart directory. The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`PROJECT_ID-apigee-cassandra.json` | `apigee-datastore/`  
`PROJECT_ID-apigee-guardrails.json` | `apigee-operator/`  
`PROJECT_ID-apigee-mart.json` | `apigee-org/`  
`PROJECT_ID-apigee-metrics.json` | `apigee-telemetry/`  
`PROJECT_ID-apigee-mint-task-scheduler.json` | `apigee-org/`  
`PROJECT_ID-apigee-runtime.json` | `apigee-env/`  
`PROJECT_ID-apigee-synchronizer.json` | `apigee-env/`  
`PROJECT_ID-apigee-watcher.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`PROJECT_ID-non-prod.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      serviceAccountPaths:
        synchronizer: "my-project-apigee-synchronizer.json"
        runtime: "my-project-apigee-runtime.json"
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
      enabled: true
      serviceAccountPath: "my-project-apigee-logger.json"
    
    guardrails:
      serviceAccountPath: "my-project-apigee-guardrails.json"
    
    mart:
      serviceAccountPath: "my-project-apigee-mart.json"
    
    connectAgent:
      serviceAccountPath: "my-project-apigee-mart.json"
    
    metrics:
      serviceAccountPath: "my-project-apigee-metrics.json"
    
    watcher:
      serviceAccountPath: "my-project-apigee-watcher.json"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountPath: my-project-apigee-mint-task-scheduler.json"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
FILEPATH | The path and filename account of the service account JSON files in your corresponding chart directory. Provide the names with the path relative to the chart directory. For example: 
     * If the `my-project-apigee-synchronizer.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

For non-production environments, the name of the single service account is `PROJECT_ID-non-prod.json` by default. For production environments, the name of the service account key file that you generated with the `create-service-account` tool in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). You can see the service account files in each corresponding chart directory. The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`PROJECT_ID-apigee-cassandra.json` | `apigee-datastore/`  
`PROJECT_ID-apigee-guardrails.json` | `apigee-operator/`  
`PROJECT_ID-apigee-mart.json` | `apigee-org/`  
`PROJECT_ID-apigee-metrics.json` | `apigee-telemetry/`  
`PROJECT_ID-apigee-mint-task-scheduler.json` | `apigee-org/`  
`PROJECT_ID-apigee-runtime.json` | `apigee-env/`  
`PROJECT_ID-apigee-synchronizer.json` | `apigee-env/`  
`PROJECT_ID-apigee-watcher.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`PROJECT_ID-non-prod.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Non-prod

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountPaths:
        # Provide the path relative to the apigee-env chart directory.
        synchronizer: NON_PROD_SERVICE_ACCOUNT_FILEPATH
          # For example: "PROJECT_ID _-apigee-non-prod.json_ "
        runtime: NON_PROD_SERVICE_ACCOUNT_FILEPATH
          # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    guardrails:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-operator chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    mart:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    connectAgent:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Use the same service account for mart and connectAgent
        # Provide the path relative to the apigee-org chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-F chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    metrics:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    watcher:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "PROJECT_ID _-apigee-non-prod.json_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
FILEPATH | The path and filename account of the service account JSON files in your corresponding chart directory. Provide the names with the path relative to the chart directory. For example: 
     * If the `my-project-apigee-synchronizer.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

For non-production environments, the name of the single service account is `PROJECT_ID-non-prod.json` by default. For production environments, the name of the service account key file that you generated with the `create-service-account` tool in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). You can see the service account files in each corresponding chart directory. The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`PROJECT_ID-apigee-cassandra.json` | `apigee-datastore/`  
`PROJECT_ID-apigee-guardrails.json` | `apigee-operator/`  
`PROJECT_ID-apigee-mart.json` | `apigee-org/`  
`PROJECT_ID-apigee-metrics.json` | `apigee-telemetry/`  
`PROJECT_ID-apigee-mint-task-scheduler.json` | `apigee-org/`  
`PROJECT_ID-apigee-runtime.json` | `apigee-env/`  
`PROJECT_ID-apigee-synchronizer.json` | `apigee-env/`  
`PROJECT_ID-apigee-watcher.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`PROJECT_ID-non-prod.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
      serviceAccountPaths:
        synchronizer: "hybrid-example-apigee-non-prod.json"
        runtime: "hybrid-example-apigee-non-prod.json"
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
    
    guardrails:
      serviceAccountPath: "my-project-apigee-non-prod.json"
    
    mart:
      serviceAccountPath: "my-project-apigee-non-prod.json"
    
    connectAgent:
      serviceAccountPath: "my-project-apigee-non-prod.json"
    
    logger:
      enabled: true
      serviceAccountPath: "my-project-apigee-non-prod.json"
    
    metrics:
      serviceAccountPath: "my-project-apigee-non-prod.json"
    
    watcher:
      serviceAccountPath: "my-project-apigee-non-prod.json"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountPath: my-project-apigee-non-prod.json"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
FILEPATH | The path and filename account of the service account JSON files in your corresponding chart directory. Provide the names with the path relative to the chart directory. For example: 
     * If the `my-project-apigee-synchronizer.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

For non-production environments, the name of the single service account is `PROJECT_ID-non-prod.json` by default. For production environments, the name of the service account key file that you generated with the `create-service-account` tool in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). You can see the service account files in each corresponding chart directory. The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`PROJECT_ID-apigee-cassandra.json` | `apigee-datastore/`  
`PROJECT_ID-apigee-guardrails.json` | `apigee-operator/`  
`PROJECT_ID-apigee-mart.json` | `apigee-org/`  
`PROJECT_ID-apigee-metrics.json` | `apigee-telemetry/`  
`PROJECT_ID-apigee-mint-task-scheduler.json` | `apigee-org/`  
`PROJECT_ID-apigee-runtime.json` | `apigee-env/`  
`PROJECT_ID-apigee-synchronizer.json` | `apigee-env/`  
`PROJECT_ID-apigee-watcher.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`PROJECT_ID-non-prod.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Vault

### Production

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretProviderClass: apigee-envsakeys-ENVIRONMENT_NAME-spc
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
    
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
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      serviceAccountSecretProviderClass: apigee-envsakeys-prod-env-spc
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
      enabled: true
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Non-prod

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretProviderClass: apigee-envsakeys-ENVIRONMENT_NAME-spc
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
      serviceAccountSecretProviderClass: apigee-envsakeys-test-env-spc
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
      enabled: true
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    # for message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### WIF for GKE

### Production

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: true
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      gsa:
        synchronizer: SYNCHRONIZER_SERVICE_ACCOUNT_EMAIL
          # For example: "_apigee-synchronizer@_ PROJECT_ID _.iam.gserviceaccount.com_ "
        runtime: RUNTIME_SERVICE_ACCOUNT_EMAIL
          # For example: "_apigee-runtime@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
      backup:
        enabled: true # Required to create the Cassandra Kubernetes service accounts
                      # for Workload Identity Federation for GKE
                      # See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-backup-overview).
    
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
    
    guardrails:
      gsa: GUARDRAILS_SERVICE_ACCOUNT_EMAIL
        # For example: "_apigee-guardrails@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    mart:
      gsa: MART_SERVICE_ACCOUNT_EMAIL
        # For example: "_apigee-mart@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    connectAgent:
      gsa: MART_SERVICE_ACCOUNT_EMAIL
        # Use the same service account email for mart and connectAgent
        # For example: "_apigee-mart@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
      gsa: LOGGER_SERVICE_ACCOUNT_EMAIL
        # For example: "_apigee-logger@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    metrics:
      gsa: METRICS_SERVICE_ACCOUNT_EMAIL
        # For example: "_apigee-metrics@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    watcher:
      gsa: WATCHER_SERVICE_ACCOUNT_EMAIL
        # For example: "_apigee-watcher@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      gsa: MINT_TASK_SCHEDULER_SERVICE_ACCOUNT_EMAIL
        # For example: "_apigee-mint-task-scheduler@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
EMAIL | The service account email addresses for the Google service accounts (GSA) you need to supply if you are using [Workload Identity Federation for GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke). These are the service accounts you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). You can find the email addresses for the service accounts with the following command: 
    
    gcloud iam service-accounts list \
      --project ${PROJECT_ID} \
      --filter "apigee"

See:
     * [`envs[].gsa.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-gsa-synchronizer). 
     * [`envs[].gsa.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-gsa-runtime). 
     * [`guardrails.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-gsa). 
     * [`logger.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-gsa). 
     * [`connectAgent.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-gsa). 
     * [`mart.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-gsa). 
     * [`metrics.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-gsa). 
     * [`mintTaskScheduler.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-gsa). 
     * [`watcher.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-gsa).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: true
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      gsa:
        synchronizer: "apigee-synchronizer@my-project.iam.gserviceaccount.com"
        runtime: "apigee-runtime@my-project.iam.gserviceaccount.com"
    
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
    
    guardrails:
      gsa: "apigee-guardrails@my-project.iam.gserviceaccount.com"
    
    mart:
      gsa: "apigee-mart@my-project.iam.gserviceaccount.com"
    
    connectAgent:
      gsa: "apigee-mart@my-project.iam.gserviceaccount.com"
    
    logger:
      enabled: true
      gsa: "apigee-logger@my-project.iam.gserviceaccount.com"
    
    metrics:
      gsa: "apigee-metrics@my-project.iam.gserviceaccount.com"
    
    watcher:
      gsa: "apigee-watcher@my-project.iam.gserviceaccount.com"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountPath: my-project-apigee-mint-task-scheduler.json"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
SERVICE_ACCOUNT_  
EMAIL | The service account email addresses for the Google service accounts (GSA) you need to supply if you are using [Workload Identity Federation for GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke). These are the service accounts you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). You can find the email addresses for the service accounts with the following command: 
    
    gcloud iam service-accounts list \
      --project ${PROJECT_ID} \
      --filter "apigee"

See:
     * [`envs[].gsa.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-gsa-synchronizer). 
     * [`envs[].gsa.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-gsa-runtime). 
     * [`guardrails.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-gsa). 
     * [`logger.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-gsa). 
     * [`connectAgent.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-gsa). 
     * [`mart.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-gsa). 
     * [`metrics.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-gsa). 
     * [`mintTaskScheduler.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-gsa). 
     * [`watcher.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-gsa).   
  
### Non-prod

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: true
        gsa: "NON_PROD_SERVICE_ACCOUNT_EMAIL"
        # For example: "_apigee-non-prod@_ PROJECT_ID _.iam.gserviceaccount.com_ "
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    logger:
      enabled: true
        # enabled by default
        # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/sa-about#recommended-sas).
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
NON_PROD_  
SERVICE_ACCOUNT_  
EMAIL | The service account email addresses for the non-prod Google service account (GSA). This is the `apigee-non-prod` service account you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). If you are using [Workload Identity Federation for GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) in a non-prod installation, specify the service account email address for the `gcp.workloadIdentity.gsa` property. You will not need to add the `gsa` property for any individual components. You can find the email addresses for the service accounts with the following command:
    
    gcloud iam service-accounts list \
      --project ${PROJECT_ID} \
      --filter "apigee"

See [`gcp.workloadIdentity.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-workloadidentity-gsa).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: true
        gsa: "apigee-non-prod@my-project.iam.gserviceaccount.com"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
      enabled: true
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
NON_PROD_  
SERVICE_ACCOUNT_  
EMAIL | The service account email addresses for the non-prod Google service account (GSA). This is the `apigee-non-prod` service account you created in [Step 4: Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts). If you are using [Workload Identity Federation for GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enable-workload-identity-gke) in a non-prod installation, specify the service account email address for the `gcp.workloadIdentity.gsa` property. You will not need to add the `gsa` property for any individual components. You can find the email addresses for the service accounts with the following command:
    
    gcloud iam service-accounts list \
      --project ${PROJECT_ID} \
      --filter "apigee"

See [`gcp.workloadIdentity.gsa`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-workloadidentity-gsa).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### WIF on other platforms

### WIF: secrets

### Production

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: false # Must be set to **_false_** to use
          # Workload Identity Federation on other platforms.
      federatedWorkloadIdentity:
        enabled: true
        audience: "AUDIENCE"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretRefs:
        synchronizer: SYNCHRONIZER_WORKLOAD_IDENTITY_SECRET
          # For example: "_synchronizer-workload-identity-secret_ "
        runtime: RUNTIME_WORKLOAD_IDENTITY_SECRET
          # For example: "_runtime-workload-identity-secret_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
    
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
    
    guardrails:
      serviceAccountRef: GUARDRAILS_WORKLOAD_IDENTITY_SECRET
        # For example: "_guardrails-workload-identity-secret_ "
    
    mart:
      serviceAccountRef: MART_WORKLOAD_IDENTITY_SECRET
        # For example: "_mart-workload-identity-secret_ "
    
    connectAgent:
      serviceAccountRef: MART_WORKLOAD_IDENTITY_SECRET
        # Use the same secret for mart and connectAgent
        # For example: "_mart-workload-identity-secret_ "
    
    logger:
      enabled: false
        # apigee-logger does not support Workload Identity Federation.
        # See [Known issue #341099433](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).
        # If you want to enable the apigee-logger component, create a
        # Kubernetes secret for apigee-logger by following the steps
        # under Kubernetes secrets in
        # [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication#kubernetes-secrets).
        # Provide a reference to the secret with the
        # [logger.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref) property.
    
    metrics:
      serviceAccountRef: METRICS_WORKLOAD_IDENTITY_SECRET
        # For example: "_metrics-workload-identity-secret_ "
    
    watcher:
      serviceAccountRef: WATCHER_WORKLOAD_IDENTITY_SECRET
        # For example: "_watcher-workload-identity-secret_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountRef: MINT_TASK_SCHEDULER_WORKLOAD_IDENTITY_SECRET
        # For example: "_apigee-mint-task-scheduler-workload-identity-secret_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
WORKLOAD_IDENTITY_  
SECRET | The name of the Kubernetes secret you for the service account credential configuration in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `cassandra-workload-identity-secret`
     * `guardrails-workload-identity-secret`
     * `logger-workload-identity-secret`
     * `mart-workload-identity-secret`
     * `metrics-workload-identity-secret`
     * `mint-task-scheduler-workload-identity-secret`
     * `runtime-workload-identity-secret`
     * `synchronizer-workload-identity-secret`
     * `watcher-workload-identity-secret`

### Non-prod

     * `non-prod-workload-identity-secret`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      serviceAccountSecretRefs:
        synchronizer: "synchronizer-workload-identity-secret"
        runtime: "runtime-workload-identity-secret"
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
    
    guardrails:
      serviceAccountRef: "guardrails-workload-identity-secret"
    
    mart:
      serviceAccountRef: "mart-workload-identity-secret"
    
    connectAgent:
      serviceAccountRef: "mart-workload-identity-secret"
    
    logger:
      enabled: false
    
    metrics:
      serviceAccountRef: "metrics-workload-identity-secret"
    
    watcher:
      serviceAccountRef: "watcher-workload-identity-secret"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountRef: "apigee-mint-task-scheduler-workload-identity-secret"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
WORKLOAD_IDENTITY_  
SECRET | The name of the Kubernetes secret you for the service account credential configuration in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `cassandra-workload-identity-secret`
     * `guardrails-workload-identity-secret`
     * `logger-workload-identity-secret`
     * `mart-workload-identity-secret`
     * `metrics-workload-identity-secret`
     * `mint-task-scheduler-workload-identity-secret`
     * `runtime-workload-identity-secret`
     * `synchronizer-workload-identity-secret`
     * `watcher-workload-identity-secret`

### Non-prod

     * `non-prod-workload-identity-secret`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### Non-prod

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: false # Must be set to **_false_** to use
          # Workload Identity Federation on other platforms.
      federatedWorkloadIdentity:
        enabled: true
        audience: "AUDIENCE"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretRefs:
        synchronizer: NON_PROD_WORKLOAD_IDENTITY_SECRET
          # For example: "_non-prod-workload-identity-secret_ "
        runtime: NON_PROD_WORKLOAD_IDENTITY_SECRET
          # For example: "_non-prod-workload-identity-secret_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    guardrails:
      serviceAccountRef: NON_PROD_WORKLOAD_IDENTITY_SECRET
        # For example: "_non-prod-workload-identity-secret_ "
    
    mart:
      serviceAccountRef: NON_PROD_WORKLOAD_IDENTITY_SECRET
        # For example: "_non-prod-workload-identity-secret_ "
    
    connectAgent:
      serviceAccountRef: NON_PROD_WORKLOAD_IDENTITY_SECRET
        # Use the same secret for mart and connectAgent
        # For example: "_non-prod-workload-identity-secret_ "
    
    logger:
      enabled: false
        # apigee-logger does not support Workload Identity Federation.
        # See [Known issue #341099433](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).
        # If you want to enable the apigee-logger component, create a
        # Kubernetes secret for apigee-logger by following the steps
        # under Kubernetes secrets in
        # [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication#kubernetes-secrets).
        # Provide a reference to the secret with the
        # [logger.serviceAccountRef](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref) property.
    
    metrics:
      serviceAccountRef: NON_PROD_WORKLOAD_IDENTITY_SECRET
        # For example: "_non-prod-workload-identity-secret_ "
    
    watcher:
      serviceAccountRef: NON_PROD_WORKLOAD_IDENTITY_SECRET
        # For example: "_non-prod-workload-identity-secret_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountRef: NON_PROD_WORKLOAD_IDENTITY_SECRET
        # For example: "_non-prod-workload-identity-secret_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
WORKLOAD_IDENTITY_  
SECRET | The name of the Kubernetes secret you for the service account credential configuration in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `cassandra-workload-identity-secret`
     * `guardrails-workload-identity-secret`
     * `logger-workload-identity-secret`
     * `mart-workload-identity-secret`
     * `metrics-workload-identity-secret`
     * `mint-task-scheduler-workload-identity-secret`
     * `runtime-workload-identity-secret`
     * `synchronizer-workload-identity-secret`
     * `watcher-workload-identity-secret`

### Non-prod

     * `non-prod-workload-identity-secret`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
      serviceAccountSecretRefs:
        synchronizer: "non-prod-workload-identity-secret"
        runtime: "non-prod-workload-identity-secret"
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
    
    guardrails:
      serviceAccountRef: "non-prod-workload-identity-secret"
    
    mart:
      serviceAccountRef: "non-prod-workload-identity-secret"
    
    connectAgent:
      serviceAccountRef: "non-prod-workload-identity-secret"
    
    logger:
      enabled: false
    
    metrics:
      serviceAccountRef: "non-prod-workload-identity-secret"
    
    watcher:
      serviceAccountRef: "non-prod-workload-identity-secret"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountRef: "non-prod-workload-identity-secret"
    
    # for message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
WORKLOAD_IDENTITY_  
SECRET | The name of the Kubernetes secret you for the service account credential configuration in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). The default names of the secrets suggested in this guide are:

### Production

     * `cassandra-workload-identity-secret`
     * `guardrails-workload-identity-secret`
     * `logger-workload-identity-secret`
     * `mart-workload-identity-secret`
     * `metrics-workload-identity-secret`
     * `mint-task-scheduler-workload-identity-secret`
     * `runtime-workload-identity-secret`
     * `synchronizer-workload-identity-secret`
     * `watcher-workload-identity-secret`

### Non-prod

     * `non-prod-workload-identity-secret`
See:
     * [`envs[].serviceAccountSecretRefs.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-synchronizer). 
     * [`envs[].serviceAccountSecretRefs.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountsecretrefs-runtime). 
     * [`guardrails.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountref). 
     * [`logger.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountref). 
     * [`connectAgent.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountref). 
     * [`mart.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountref). 
     * [`metrics.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountref). 
     * [`mintTaskScheduler.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountref). 
     * [`watcher.serviceAccountRef`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountref).   
  
### WIF: files

### Production

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: false # Must be set to **_false_** to use
          # Workload Identity Federation on other platforms.
      federatedWorkloadIdentity:
        enabled: true
        audience: "AUDIENCE"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountPaths:
        # Provide the path relative to the apigee-env chart directory.
        synchronizer: SYNCHRONIZER_CREDENTIAL_CONFIGURATION_FILEPATH
          # For example: "_apigee-synchronizer-credential-configuration.json_ "
        runtime: RUNTIME_SERVICE_CREDENTIAL_CONFIGURATION_FILEPATH
          # For example: "_apigee-runtime-credential-configuration.json_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE installations.
        # Set to **_true_**  for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift
        # installations. See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
    
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
    
    guardrails:
      serviceAccountPath: GUARDRAILS_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-operator chart directory.
        # For example: "_apigee-guardrails-credential-configuration.json_ "
    
    mart:
      serviceAccountPath: MART_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "_apigee-mart-credential-configuration.json_ "
    
    connectAgent:
      serviceAccountPath: MART_CREDENTIAL_CONFIGURATION_FILEPATH
        # Use the same service account for mart and connectAgent
        # Provide the path relative to the apigee-org chart directory.
        # For example: "_apigee-mart-credential-configuration.json_ "
    
    logger:
      enabled: false
        # apigee-logger does not support Workload Identity Federation.
        # See [Known issue #341099433](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).
        # If you want to enable the apigee-logger component, provide
        # the path to the apigee-logger service account key file with
        # the [logger.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath) property.
    
    metrics:
      serviceAccountPath: METRICS_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "_apigee-metrics-credential-configuration.json_ "
    
    watcher:
      serviceAccountPath: WATCHER_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "_apigee-watcher-credential-configuration.json_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountPath: MINT_TASK_SCHEDULER_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "_apigee-mint-task-scheduler-credential-configuration.json_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
CREDENTIAL_  
CONFIGURATION_  
FILEPATH | The path and filename account of the credential configuration files you created in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). Provide the names with the path relative to the chart directory. For example:
     * If the `apigee-synchronizer-credential-configuration.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`apigee-cassandra-credential-configuration.json` | `apigee-datastore/`  
`apigee-guardrails-credential-configuration.json` | `apigee-operator/`  
`apigee-logger-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mart-credential-configuration.json` | `apigee-org/`  
`apigee-metrics-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mint-task-scheduler-credential-configuration.json` | `apigee-org/`  
`apigee-runtime-credential-configuration.json` | `apigee-env/`  
`apigee-synchronizer-credential-configuration.json` | `apigee-env/`  
`apigee-watcher-credential-configuration.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`apigee-non-prod-credential-configuration.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      serviceAccountPaths:
        synchronizer: "apigee-synchronizer-credential-configuration.json"
        runtime: "apigee-runtime-credential-configuration.json"
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
    
    guardrails:
      serviceAccountPath: "apigee-guardrails-credential-configuration.json"
    
    mart:
      serviceAccountPath: "apigee-mart-credential-configuration.json"
    
    connectAgent:
      serviceAccountPath: "apigee-mart-credential-configuration.json"
    
    logger:
      enabled: false
    
    metrics:
      serviceAccountPath: "apigee-metrics-credential-configuration.json"
    
    watcher:
      serviceAccountPath: "apigee-watcher-credential-configuration.json"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountPath: apigee-mint-task-scheduler-credential-configuration.json"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
CREDENTIAL_  
CONFIGURATION_  
FILEPATH | The path and filename account of the credential configuration files you created in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). Provide the names with the path relative to the chart directory. For example:
     * If the `apigee-synchronizer-credential-configuration.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`apigee-cassandra-credential-configuration.json` | `apigee-datastore/`  
`apigee-guardrails-credential-configuration.json` | `apigee-operator/`  
`apigee-logger-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mart-credential-configuration.json` | `apigee-org/`  
`apigee-metrics-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mint-task-scheduler-credential-configuration.json` | `apigee-org/`  
`apigee-runtime-credential-configuration.json` | `apigee-env/`  
`apigee-synchronizer-credential-configuration.json` | `apigee-env/`  
`apigee-watcher-credential-configuration.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`apigee-non-prod-credential-configuration.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Non-prod

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: false # Must be set to **_false_** to use
          # Workload Identity Federation on other platforms.
      federatedWorkloadIdentity:
        enabled: true
        audience: "AUDIENCE"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountPaths:
        # Provide the path relative to the apigee-env chart directory.
        synchronizer: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
          # For example: "_apigee-non-prod-credential-configuration.json_ "
        runtime: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
          # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    guardrails:
      serviceAccountPath: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-operator chart directory.
        # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    mart:
      serviceAccountPath: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    connectAgent:
      serviceAccountPath: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
        # Use the same service account for mart and connectAgent
        # Provide the path relative to the apigee-org chart directory.
        # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    logger:
      enabled: false
        # apigee-logger does not support Workload Identity Federation.
        # See [Known issue #341099433](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).
        # If you want to enable the apigee-logger component, provide
        # the path to the apigee-non-prod service account key file with
        # the [logger.serviceAccountPath](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath) property.
    
    metrics:
      serviceAccountPath: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    watcher:
      serviceAccountPath: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-telemetry chart directory.
        # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    mintTaskScheduler: # Required for Monetization for Apigee hybrid
      serviceAccountPath: NON_PROD_CREDENTIAL_CONFIGURATION_FILEPATH
        # Provide the path relative to the apigee-org chart directory.
        # For example: "_apigee-non-prod-credential-configuration.json_ "
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
CREDENTIAL_  
CONFIGURATION_  
FILEPATH | The path and filename account of the credential configuration files you created in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). Provide the names with the path relative to the chart directory. For example:
     * If the `apigee-synchronizer-credential-configuration.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`apigee-cassandra-credential-configuration.json` | `apigee-datastore/`  
`apigee-guardrails-credential-configuration.json` | `apigee-operator/`  
`apigee-logger-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mart-credential-configuration.json` | `apigee-org/`  
`apigee-metrics-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mint-task-scheduler-credential-configuration.json` | `apigee-org/`  
`apigee-runtime-credential-configuration.json` | `apigee-env/`  
`apigee-synchronizer-credential-configuration.json` | `apigee-env/`  
`apigee-watcher-credential-configuration.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`apigee-non-prod-credential-configuration.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
      serviceAccountPaths:
        synchronizer: "apigee-non-prod-credential-configuration.json"
        runtime: "apigee-non-prod-credential-configuration.json"
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
    
    guardrails:
      serviceAccountPath: "apigee-non-prod-credential-configuration.json"
    
    mart:
      serviceAccountPath: "apigee-non-prod-credential-configuration.json"
    
    connectAgent:
      serviceAccountPath: "apigee-non-prod-credential-configuration.json"
    
    logger:
      enabled: false
    
    metrics:
      serviceAccountPath: "apigee-non-prod-credential-configuration.json"
    
    watcher:
      serviceAccountPath: "apigee-non-prod-credential-configuration.json"
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    mintTaskScheduler:
      serviceAccountPath: apigee-non-prod-credential-configuration.json"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
_< component>__  
CREDENTIAL_  
CONFIGURATION_  
FILEPATH | The path and filename account of the credential configuration files you created in [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication). Provide the names with the path relative to the chart directory. For example:
     * If the `apigee-synchronizer-credential-configuration.json` file resides in the `apigee-env/` chart directory, you only need to provide the file name, such as: 
           
           synchronizer:  "FILE_NAME.json"

     * If the file resides in a `apigee-env/service-accounts/` directory, you would specify a relative path: 
           
           synchronizer:  "service-accounts/FILE_NAME.json"

The default names of the and corresponding chart directories for the service accounts are:

### Production

| Service account file name | Chart directory  
---|---  
`apigee-cassandra-credential-configuration.json` | `apigee-datastore/`  
`apigee-guardrails-credential-configuration.json` | `apigee-operator/`  
`apigee-logger-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mart-credential-configuration.json` | `apigee-org/`  
`apigee-metrics-credential-configuration.json` | `apigee-telemetry/`  
`apigee-mint-task-scheduler-credential-configuration.json` | `apigee-org/`  
`apigee-runtime-credential-configuration.json` | `apigee-env/`  
`apigee-synchronizer-credential-configuration.json` | `apigee-env/`  
`apigee-watcher-credential-configuration.json` | `apigee-org/`  
  
### Non-prod

Service account file name | Chart directory  
---|---  
`apigee-non-prod-credential-configuration.json` | `apigee-datastore/`  
`apigee-operator/`  
`apigee-org/`  
`apigee-telemetry/`  
**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.

See:

     * [`envs[].serviceAccountPaths.synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-synchronizer). 
     * [`envs[].serviceAccountPaths.runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-serviceaccountpaths-runtime). 
     * [`guardrails.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#guardrails-serviceaccountpath). 
     * [`logger.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#logger-serviceaccountpath). 
     * [`connectAgent.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#connectagent-serviceaccountpath). 
     * [`mart.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#mart-serviceaccountpath). 
     * [`metrics.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#metrics-serviceaccountpath). 
     * [`mintTaskScheduler.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#minttaskscheduler-serviceaccountpath). 
     * [`watcher.serviceAccountPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#watcher-serviceaccountpath).   
  
### WIF: Vault

### Production

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: false # Must be set to **_false_** to use
          # Workload Identity Federation on other platforms.
      federatedWorkloadIdentity:
        enabled: true
        audience: "AUDIENCE"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretProviderClass: apigee-envsakeys-ENVIRONMENT_NAME-spc
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production).
    
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
    
    logger:
      enabled: false
        # apigee-logger does not support Workload Identity Federation.
        # See [Known issue #341099433](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).
        # If you want to enable the apigee-logger component, add
        # a "logger" : "value" entry in the _orgsakeys_ vault secret
        # using the contents of the apigee-logger key file for the
        # value. See [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication).
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: prod-env
      serviceAccountSecretProviderClass: apigee-envsakeys-prod-env-spc
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageSize: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
    
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
      enabled: false
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    # For message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Non-prod

### Template

Values in red, bold italics are property values that you must provide. You can edit their values on this page. They are described in the table below. 
    
    instanceID: UNIQUE_INSTANCE_IDENTIFIER
    namespace: APIGEE_NAMESPACE # Usually "apigee"
    
    gcp:
      projectID: PROJECT_ID
      region: ANALYTICS_REGION
      workloadIdentity:
        enabled: false # Must be set to **_false_** to use
          # Workload Identity Federation on other platforms.
      federatedWorkloadIdentity:
        enabled: true
        audience: "AUDIENCE"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Closest Google Cloud region to your cluster.
    
    org: ORG_NAME
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    # Required for [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/enhanced-proxy-limits):
    enhanceProxyLimits: true
    
    # Required if using [data residency with hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/using-data-residency-with-apigee-hybrid):
    contractProvider: https://CONTROL_PLANE_LOCATION-apigee.googleapis.com
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountSecretProviderClass: apigee-envsakeys-ENVIRONMENT_NAME-spc
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and  for multi-region
        # installations with connectivity between pods in different clusters,
        # like GKE.
        # Set to **_true_** for multi-region installations with no communication
        # between pods in different clusters, for example Google Distributed
        # Cloud on VMware or bare metal, AKS, EKS, and OpenShift.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-region#prerequisites)
      replicaCount: 1
        # Use 1 for non-prod installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-production) for guidelines.
    
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
    
    logger:
      enabled: false
        # apigee-logger does not support Workload Identity Federation.
        # See [Known issue #341099433](https://docs.cloud.google.com/apigee/docs/release/known-issues#hybrid-apigee-logger-wif).
        # If you want to enable the apigee-logger component, add
        # a "logger" : "value" entry in the _orgsakeys_ vault secret
        # using the contents of the apigee-non-prod key file for the
        # value. See [Step 5: Set up service account authentication](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication).
    
    # Required if using [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) ([v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later)
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11" # Must be 1.15.1 or higher.
    
    # If using message payloads larger than 10MB.
    # See [configure large message payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-large-payload-support):
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
  
### Example
    
    instanceID: "my_hybrid_example"
    namespace: "apigee"
    
    gcp:
      projectID: my-project
      region: us-central1
      workloadIdentity:
        enabled: false
      federatedWorkloadIdentity:
        enabled: true
        audience: "//iam.googleapis.com/projects/123123123123/locations/global/workloadIdentityPools/my-wi-pool/providers/my-wi-provider"
        credentialSourceFile: "/var/run/service-account/token"
    
    k8sCluster:
      name: hybrid-env
      region: us-central1
    
    org: my-project
    
    serviceAccountSecretProviderClass: apigee-orgsakeys-spc
    
    enhanceProxyLimits: true
    
    contractProvider: https://us-apigee.googleapis.com
    
    envs:
    - name: test
      serviceAccountSecretProviderClass: apigee-envsakeys-test-env-spc
    
    cassandra:
      hostNetwork: false
      replicaCount: 1
    
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
      enabled: false
    
    # Monetization for Apigee hybrid
    runtime:
      image:
        url: "gcr.io/apigee-release/hybrid/apigee-runtime"
        tag: "1.16.11"
    
    # for message payloads larger than 10MB:
    runtime:
      cwcAppend:
        bin_setenv_max_mem: 4096m   # Increase max heap size to 4 gigs
      resources:
        requests:
          memory: 4Gi
        limits:
          memory: 6Gi
    

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref). 

Variable | Description  
---|---  
UNIQUE_INSTANCE_  
IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. See [`instanceID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#instanceid).  
APIGEE_NAMESPACE | The Kubernetes namespace for your Apigee hybrid components. The default value is `apigee`. See [`namespace`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#namespace).  
PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`. See [`gcp.projectID`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-projectid).  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision)). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously. See [`gcp.region`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-region).  
AUDIENCE | The allowed audience of the Workload Identity Provider. You can find the value by searching any of the credential configuration files for the term `audience: `. The audience value is the same in each credential configuration file. For example, in the following sample `apigee-runtime-credential-configuration.json` file:
    
    {
      "universe_domain": "googleapis.com",
      "type": "external_account:,"
      "audience": "AUDIENCE",
      "subject_token_type": "TOKEN_TYPE",
      "token_url": "TOKEN_URL",
      "service
      "impersonation_url": "IMPERSONATION_URL",
      "credential_source": {
        "file": "FILE_PATH",
        "format": {
          "type": "text"
        }
      }
    }

The audience value will look something like the following (without line breaks):
    
    "//iam.googleapis.com/projects/123456789012/
    locations/global/workloadIdentityPools/
    POOL_ID/providers/WORKLOAD_PROVIDER_ID"
              

**Tip:** You can delete the credential configuration files after you copy the audience value. See [`gcp.federatedWorkloadIdentity.audience`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#gcp-federatedworkloadidentity-audience).  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`. See [`k8sCluster.name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-name).  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.See [`k8sCluster.location`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#k8scluster-location).  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`. See [`org`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#org).  
CONTROL_PLANE_  
LOCATION | Required if you are using Data residency with your Apigee hybrid installation. This is the location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). It is the value assigned to the `CONTROL_PLANE_LOCATION` environment variable in [Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision). See [`contractProvider`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#contractprovider).  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). See [`envs[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#envs-name).  
ENVIRONMENT_GROUP_  
NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file. See [`virtualhosts[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-name).  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 
     * Have a maximum length of 17 characters
     * Contain only lowercase alphanumeric characters, '-' or '.'
     * Start with an alphanumeric character
     * End with an alphanumeric character
See:
     * [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-name). 
     * [`virtualhosts[].selector`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-selector)  
PATH_TO_CERT_FILE  
PATH_TO_KEY_FILE | Enter the path and filename of the self-signed TLS key and certificate files that you generated previously in [ Step 6: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates). These files must be located in the `APIGEE_HELM_CHARTS_HOME/apigee-virtualhosts/certs` directory. For example: 
    
    sslCertPath: certs/keystore.crt
    sslKeyPath: certs/keystore.key

See:
     * [`virtualhosts[].sslCertPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslcertpath). 
     * [`virtualhosts[].sslKeyPath`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#virtualhosts-sslkeypath)  
SVC_ANNOTATIONS_  
KEY: SVC_ANNOTATIONS_  
VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Your cloud platform uses annotations to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-expose-apigee-ingress). Comment out or delete this section if you are not using it. See [`ingressGateways[].svcAnnotations`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/config-prop-ref#ingressgateways-svcannotations).  
**Note:** If you want to create a security perimeter around your cluster and related Cloud services, you can configure one using Google Cloud [ Virtual Private Cloud (VPC) Service Controls](https://cloud.google.com/vpc-service-controls) with Apigee hybrid. See [ Using VPC Service Controls with Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) for instructions.

##  Summary 

The configuration file tells Kubernetes how to deploy the hybrid components to a cluster. Next, you will enable synchronizer access so the Apigee runtime and management planes will be able to communicate. 

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides) [(NEXT) Step 8: Enable Control Plane access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-enable-control-plane-access) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-cert-manager) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-crds) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-helm-charts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
