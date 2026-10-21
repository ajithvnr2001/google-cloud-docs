---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-configure-cluster/
title: Step 6: Configure the cluster \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:13:58.639720+00:00
---

# Step 6: Configure the cluster  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-configure-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 6: Configure the cluster Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-configure-cluster.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-configure-cluster.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-configure-cluster.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-configure-cluster.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-configure-cluster.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-configure-cluster.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-configure-cluster.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-configure-cluster.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-configure-cluster.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-configure-cluster.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-configure-cluster.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-configure-cluster.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-configure-cluster.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-configure-cluster.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-configure-cluster.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-configure-cluster.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-configure-cluster.html)



##  Specify configuration overrides 

The Apigee hybrid installer uses defaults for many settings; however, there are a few settings that do not have defaults. You must provide values for these settings, as explained next. 

**Important:** Apigee hybrid v1.9.4 has been updated with one critical hotfix release. If you wish, you can apply the required configuration settings for the hotfix directly in the configuration overrides file described in this step. If you add the hotfix upgrade configurations now, you do not have to perform any further hotfix upgrades later. The configuration settings for the hotfix (v1.9.4-hotfix.1) are listed in the [upgrade guide](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/upgrade#install-hotfix). See also the release note for the hotfix release: 

  * [hybrid v1.9.4-hotfix.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v194-hotfix1)



### Before you begin

We recommend you review the following scenarios to determine if you want to configure your cluster for them. These configurations are optional. 

  * If you are planning on installing hybrid in multiple regions, read [Multi-region deployment](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-region) before continuing.
  * Apigee hybrid provides default passwords for the Cassandra users; however, we recommend that you change the default user passwords. See [Configuring TLS for Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-tls) for details. 
  * If you want to configure the storage and heap settings for Cassandra, see [ Configure storage and heap settings](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production). 
  * For production installation scenarios, configure [persistent solid state disk (SSD)](https://docs.cloud.google.com/compute/docs/disks#pdspecs) storage for Cassandra. We do not support using [local SSDs](https://docs.cloud.google.com/compute/docs/disks#localssds) for Apigee hybrid. For details, see [ Add SSD storage for production deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production#add-ssd-storage-for-production-deployments). 



### Configure the cluster

By convention, configuration overrides are written in a file named `overrides.yaml` in your `$HYBRID_FILES/overrides` directory. 

  1. Create a new file named **`overrides.yaml`** in your `$HYBRID_FILES/overrides` directory. For example: 
         
         vi $HYBRID_FILES/overrides/overrides.yaml

The `overrides.yaml` provides the configuration for your unique Apigee hybrid installation. The overrides file in this step provides a basic configuration for a small-footprint hybrid runtime installation, suitable for your first installation. 

  2. In `overrides.yaml`, add the required property values, shown below. A detailed description of each property is also provided below. 

If you are installing Apigee hybrid on GKE and you enabled Workload identity on your node pools in [Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-cluster), select the **GKE - Workload Identity** tab to configure your `overrides.yaml` file to use Workload identity. 

For all other installations, select the tab for either non-production, **Non-prod** or production, **Prod** environments, depending on your choice in [Step 4: Create service accounts and credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts).

For installations in production environments, look at the storage requirements for the Cassandra database in [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production).

### GKE - Workload Identity

Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. They are described in the table below.

If you are installing Apigee hybrid on **GKE** , you have an alternative to authenticate and make requests to Google APIs, **Workload Identity**. For overviews of Workload Identity, see:

     * [ Introducing Workload Identity: Better authentication for your GKE applications](https://cloud.google.com/blog/products/containers-kubernetes/introducing-workload-identity-better-authentication-for-your-gke-applications)
     * [Using Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

To use Workload Identity with Apigee hybrid on GKE, use this template and then follow the steps in [Step 8: Install hybrid runtime](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-hybrid-runtime) to create the Kubernetes service accounts and associate them with the Google service accounts you created in [Step 4: Create service accounts and credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts). 
    
    gcp:
      region: ANALYTICS_REGION
      projectID: GCP_PROJECT_ID
      **workloadIdentityEnabled: true**
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
    org: ORG_NAME
    
    instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
    
    cassandra:
      hostNetwork: false
        # **_false_** for all GKE installations.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-region#prerequisites)
      replicaCount: 3
        # Use 1 for demo installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production) for guidelines.
      backup:
        enabled: true
        # Set to true for initial installation.
        # This triggers apigeectl to create the apigee-cassandra-backup Kubernetes service account.
        # See [Cassandra backup overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-backup-overview) for instructions on using cassandra.backup.
    
    virtualhosts:
    - name: ENVIRONMENT_GROUP_NAME
      selector:
        app: apigee-ingressgateway
        ingress_name: INGRESS_NAME
      sslCertPath: ./certs/CERT_NAME.pem
      sslKeyPath: ./certs/KEY_NAME.key
    
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
    
    

### Non-prod

Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. They are described in the table below.

There are differences between the different platforms for the Google Cloud project region and Kubernetes cluster region. Choose the platform where you are installing Apigee hybrid.
    
    gcp:
      region: ANALYTICS_REGION
      projectID: GCP_PROJECT_ID
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
    org: ORG_NAME
    
    instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
    
    cassandra:
      replicaCount: 1
        # Use 1 for non-prod or "demo" installations and multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production) for guidelines.
      hostNetwork: false
        # Set to **_false_** for single region installations and multi-region installations
        # with connectivity between pods in different clusters, for example GKE installations.
        # Set to **_true_**  for multi-region installations with no communication between
        # pods in different clusters, for example GKE On-prem, GKE on AWS, Anthos on bare metal,
        # AKS, EKS, and OpenShift installations.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-region#prerequisites)
    
    virtualhosts:
    - name: ENVIRONMENT_GROUP_NAME
      selector:
        app: apigee-ingressgateway
        ingress_name: INGRESS_NAME
      sslCertPath: ./certs/CERT_NAME.pem
      sslKeyPath: ./certs/KEY_NAME.key
    
    ingressGateways:
    - name: INGRESS_NAME # maximum 17 characters.
      replicaCountMin: 2
      replicaCountMax: 10
      svcAnnotations:  # optional. If you are on AKS, see [Known issue #260772383](https://docs.cloud.google.com/apigee/docs/release/known-issues#260772383)
        SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
      svcLoadBalancerIP: SVC_LOAD_BALANCER_IP  # optional
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountPaths:
        synchronizer: NON_PROD_SERVICE_ACCOUNT_FILEPATH
          # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-non-prod.json"_
        udca: NON_PROD_SERVICE_ACCOUNT_FILEPATH
        runtime: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    
    mart:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    connectAgent:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    metrics:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    udca:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    watcher:
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    logger:
      enabled: false
            # Set to **_false_** to disable logger for GKE installations.
            # Set to **_true_** for all platforms other than GKE.
            # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-about#recommended-sas).
      serviceAccountPath: NON_PROD_SERVICE_ACCOUNT_FILEPATH
    
    

### Prod

Make sure the `overrides.yaml` file has the following structure and syntax. Values in red, bold italics are property values that you must provide. They are described in the table below.

There are differences between the different platforms for the Google Cloud project region and Kubernetes cluster region. Choose the platform where you are installing Apigee hybrid. 
    
    gcp:
      region: ANALYTICS_REGION
      projectID: GCP_PROJECT_ID
    
    k8sCluster:
      name: CLUSTER_NAME
      region: CLUSTER_LOCATION # Must be the closest Google Cloud region to your cluster.
    org: ORG_NAME
    
    instanceID: "UNIQUE_INSTANCE_IDENTIFIER"
    
    cassandra:
      hostNetwork: false
        # Set to **_false_** for single region installations and multi-region installations
        # with connectivity between pods in different clusters, for example GKE installations.
        # Set to **_true_**  for multi-region installations with no communication between
        # pods in different clusters, for example GKE On-prem, GKE on AWS, Anthos on bare metal,
        # AKS, EKS, and OpenShift installations.
        # See [Multi-region deployment: Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-region#prerequisites)
      replicaCount: 3
        # Use multiples of 3 for production.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production) for guidelines.
      storage:
        capacity: 500Gi
      resources:
        requests:
          cpu: 7
          memory: 15Gi
      maxHeapSize: 8192M
      heapNewSize: 1200M
        # Minimum storage requirements for a production environment.
        # See [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production).
    
    virtualhosts:
    - name: ENVIRONMENT_GROUP_NAME
      selector:
        app: apigee-ingressgateway
        ingress_name: INGRESS_NAME
      sslCertPath: ./certs/CERT_NAME.pem
      sslKeyPath: ./certs/KEY_NAME.key
    
    ingressGateways:
    - name: INGRESS_NAME # maximum 17 characters. See [Known issue 243167389](https://docs.cloud.google.com/apigee/docs/release/known-issues#243167389).
      replicaCountMin: 2
      replicaCountMax: 10
      svcAnnotations:  # optional. If you are on AKS, see [Known issue #260772383](https://docs.cloud.google.com/apigee/docs/release/known-issues#260772383)
        SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE
    
    envs:
    - name: ENVIRONMENT_NAME
      serviceAccountPaths:
        synchronizer: SYNCHRONIZER_SERVICE_ACCOUNT_FILEPATH
          # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-synchronizer.json_ "
        udca: UDCA_SERVICE_ACCOUNT_FILEPATH
          # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-udca.json_ "
        runtime: RUNTIME_SERVICE_ACCOUNT_FILEPATH
          # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-runtime.json_ "
    
    mart:
      serviceAccountPath: MART_SERVICE_ACCOUNT_FILEPATH
            # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-mart.json_ "
    
    connectAgent:
      serviceAccountPath: MART_SERVICE_ACCOUNT_FILEPATH
            # **Use the same service account for mart and connectAgent**
    
    metrics:
      serviceAccountPath: METRICS_SERVICE_ACCOUNT_FILEPATH
            # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-metrics.json_ "
    
    udca:
      serviceAccountPath: UDCA_SERVICE_ACCOUNT_FILEPATH
            # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-udca.json_ "
    
    watcher:
      serviceAccountPath: WATCHER_SERVICE_ACCOUNT_FILEPATH
            # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-watcher.json_ "
    
    logger:
      enabled: false
            # Set to **_false_** to disable logger for GKE installations.
            # Set to **_true_** for all platforms other than GKE.
            # See _apigee-logger_ in [Service accounts and roles used by hybrid components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/sa-about#recommended-sas).
      serviceAccountPath: LOGGER_SERVICE_ACCOUNT_FILEPATH
            # For example: "./service-accounts/GCP_PROJECT_ID _-apigee-logger.json_ "
    

### Example

The following example shows a completed overrides file with example property values added:
    
    gcp:
      region: us-central1
      projectID: hybrid-example
    
    k8sCluster:
      name: apigee-hybrid
      region: us-central1
    
    org: hybrid-example
    
    instanceID: "my_hybrid_example"
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
    
    virtualhosts:
    - name: example-env-group
      selector:
        app: apigee-ingressgateway
        ingress_name: my-ingress-1
      sslCertPath: ./certs/keystore.pem
      sslKeyPath: ./certs/keystore.key
    
    ingressGateways:
    - name: my-ingress-1
      replicaCountMin: 2
      replicaCountMax: 10
    
    envs:
    - name: test
      serviceAccountPaths:
        synchronizer: ./service-accounts/my-hybrid-project-apigee-non-prod.json
          # for production environments, my-hybrid-project-apigee-synchronizer.json
        udca: ./service-accounts/my-hybrid-project-apigee-non-prod.json
          # for production environments, my-hybrid-project-apigee-udca.json
        runtime: ./service-accounts/my-hybrid-project-apigee-non-prod.json
          # for production environments, my-hybrid-project-apigee-runtime.json
    
    mart:
      serviceAccountPath: ./service-accounts/my-hybrid-project-apigee-non-prod.json
        # for production environments, my-hybrid-project-apigee-mart.json
    
    connectAgent:
      serviceAccountPath: ./service-accounts/my-hybrid-project-apigee-non-prod.json
        # for production environments, example-hybrid-apigee-mart.json
    
    metrics:
      serviceAccountPath: ./service-accounts/my-hybrid-project-apigee-non-prod.json
        # for production environments, my-hybrid-project-apigee-metrics.json
    
    udca:
      serviceAccountPath: ./service-accounts/my-hybrid-project-apigee-non-prod.json
        # for production environments, my-hybrid-project-apigee-udca.json
    
    watcher:
      serviceAccountPath: ./service-accounts/my-hybrid-project-apigee-non-prod.json
        # for production environments, my-hybrid-project-apigee-watcher.json
    
    logger:
      enabled: false # Set to "false" for GKE. Set to "true" for all other Kubernetes platforms.
      serviceAccountPath: ./service-accounts/my-hybrid-project-apigee-non-prod.json
        # for production environments, LOGGER_SERVICE_ACCOUNT_NAME.json
    

  3. When you are finished, save the file.



The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref). 

Variable | Description  
---|---  
ANALYTICS_REGION | In GKE, You must set this value to the same region where the cluster is running. In all other platforms, select the closest analytics region to your cluster that has Analytics support (see the table in [Part 1, Step 2: Create an organization](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-provision). This is the value you assigned to the environment variable `ANALYTICS_REGION` previously.  
GCP_PROJECT_ID | Identifies the Google Cloud project where the `apigee-logger` and the `apigee-metrics` push their data. This is the value assigned to the environment variable `PROJECT_ID`.  
CLUSTER_NAME | Your Kubernetes cluster name. This is the value assigned to the environment variable `CLUSTER_NAME`.  
CLUSTER_LOCATION | The region where the cluster is running. This is the region where you created the cluster in [ Step 1: Create a cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-cluster). This is the value you assigned to the environment variable `CLUSTER_LOCATION` previously. If you are working with zonal clusters, you must specify the **region** in which your cluster was created. For example, if you created your cluster in the `us-central1-a` zone, specify `us-central1` for the CLUSTER_LOCATION.  
ORG_NAME | The ID of your Apigee hybrid organization. This is the value assigned to the environment variable `ORG_NAME`.  
UNIQUE_INSTANCE_IDENTIFIER | A unique string to identify this instance. This can be any combination of letters and numbers up to 63 characters in length. **Note:** You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster. For multi-region installations, each region requires its own cluster (individual clusters do not span regions).You can create multiple organizations in the same cluster, but the `instanceID` must be the same for all orgs in the same Kubernetes cluster.  
ENVIRONMENT_GROUP_NAME | The name of the environment group your environments are assigned to. This is the group you created in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-add-environment). This is the value assigned to the environment variable `ENV_GROUP`. **Note:** If you wish to place cluster instances in multiple regions, you must be careful about how you define your environments and virtual hosts. If you have one or more environments attached to an environment group, you must include that same environment group configuration in each cluster instance's overrides file.   
CERT_NAME  
KEY_NAME | Enter the name of the self-signed TLS key and certificate files that you generated previously in [ Step 5: Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-tls-certificates). These files must be located in the `base_directory/hybrid-files/certs` directory. For example: 
    
    
    sslCertPath: ./certs/keystore.pem
    sslKeyPath: ./certs/keystore.key  
  
INGRESS_NAME | The name of the Apigee ingress gateway for your deployment. This can be any name that meets the following requirements: 

  * Have a maximum length of 17 characters
  * Contain only lowercase alphanumeric characters, '-' or '.'
  * Start with an alphanumeric character
  * End with an alphanumeric character

See [`ingressGateways[].name`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/config-prop-ref#ingressgateways-name) in the Configuration property reference   
SVC_ANNOTATIONS_KEY: SVC_ANNOTATIONS_VALUE | (Optional). This is a key-value pair that provides annotations for your default ingress service. Annotations are used by your cloud platform to help configure your hybrid installation, for example setting the loadbalancer type to either internal or external. Annotations vary from platform to platform. Refer to your platform documentation for required and suggested annotations. **Note:** You do not need to set `svcAnnotations` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress). Comment out or delete this section if you are not using it.  
SVC_LOAD_BALANCER_IP | (Optional). An IP address you have reserved for your load balancer. On platforms that support specifying the load balancer IP address, the load balancer will be created with this IP address. On platforms that do not allow you to specify the load balancer IP, this property is ignored. **Note:** You do not need to set `LoadBalancerIP` if you are creating your own Kubernetes service for ingress deployment as documented in [Expose Apigee ingress gateway](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress). In production installations, it is recommended to create your own Kubernetes service. Comment out or delete this section if you are not using it.  
ENVIRONMENT_NAME | Use the same name that you used when you created an environment in the UI, as explained in [ Project and org setup - Step 3: Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-add-environment).   
***_SERVICE_ACCOUNT_FILEPATH** | The path and filename account of the service account JSON files in your `service-accounts/` directory. The names must include the path to the service account file. This can be a full path, or the path relative to your `hybrid-files/` directory. If you include a relative path, you must call `apigeectl`, the command to apply this configuration, from your `hybrid-files/` directory. For non-production environments, the name of the single service account is `GCP_PROJECT_ID-non-prod.json` by default. For production environments, the name of the service account key file that you generated with the `create-service-account` tool in [Hybrid runtime setup - Step 4: Create service accounts and credentials](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts). You can see the list of service account files in your `service-accounts/` directory. The default names of the production environment service accounts are:

  * **Cassandra:** GCP_PROJECT_ID-`apigee-cassandra.json`
  * **Logger:** GCP_PROJECT_ID-`apigee-logger.json`
  * **MART:** GCP_PROJECT_ID-`apigee-mart.json`
  * **Connect agent:** GCP_PROJECT_ID-`apigee-mart.json`
  * **Metrics:** GCP_PROJECT_ID-`apigee-metrics.json`
  * **Apigee runtime:** GCP_PROJECT_ID-````
  * **Synchronizer:** GCP_PROJECT_ID-`apigee-synchronizer.json`
  * **UDCA:** GCP_PROJECT_ID-`apigee-udca.json`
  * **Watcher:** GCP_PROJECT_ID-`apigee-watcher.json`

**Note:** Both `mart` and `connectAgent` use the `apigee-mart` service account.  
**Note:** If you want to create a security perimeter around your cluster and related Cloud services, you can configure one using Google Cloud [ Virtual Private Cloud (VPC) Service Controls](https://cloud.google.com/vpc-service-controls) with Apigee hybrid. See [ Using VPC Service Controls with Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) for instructions.

##  Summary 

The configuration file tells Kubernetes how to deploy the hybrid components to a cluster. Next, you will enable synchronizer access so the Apigee runtime and management planes will be able to communicate. 

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-cert-manager) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-apigeectl) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-configure-cluster) [(NEXT) Step 7: Enable Synchronizer access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-enable-synchronizer-access) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-hybrid-runtime) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-expose-apigee-ingress) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-deploy-proxy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
