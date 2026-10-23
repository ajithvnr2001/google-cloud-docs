---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration/
title: Customize containerd configuration in GKE nodes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:01.321671+00:00
---

# Customize containerd configuration in GKE nodes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Customize containerd configuration in GKE nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to customize the configuration of the containerd container runtime on your Google Kubernetes Engine (GKE) nodes. Before reading this document, ensure that you're familiar with what a [container runtime](https://kubernetes.io/docs/reference/glossary/?all=true#term-container-runtime) is and why you'd want to customize it.

## About containerd configuration in GKE

You can manually configure a set of options in the containerd runtime on GKE nodes that run an operating system like Container-Optimized OS. Customizing the runtime lets you configure special requirements like access to private image registries. To set these options, you create a YAML file called a _runtime configuration file_ and pass the file to GKE when you create or update a cluster or a node pool.

This method of customizing containerd lets you avoid deploying privileged DaemonSets, which are a security risk. When you provide GKE with a runtime configuration file, GKE re-creates your nodes and updates the containerd `config.toml` file on every node with your configuration. The configuration persists through node termination, upgrades, and re-creations.

You can configure containerd settings at the cluster level or at the node pool level. A node pool-level configuration overrides a cluster-level configuration for those options. When you update a cluster-level containerd configuration option (such as `registryHosts` or `writableCgroups`), GKE updates and re-creates the nodes only in node pools that don't have their own node pool-level settings for those options. Node pools with their own node pool-level configurations for the option won't be updated or re-created and continue to use their own settings.

The runtime configuration file only lets you configure options in containerd. GKE also supports configuring specific kubelet options and low-level Linux kernel options by using a separate file called a node system configuration file. For more details, see [Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config).

### Limitations

You can't use a runtime configuration file to change containerd settings in Windows node images.

## Available containerd configuration options

The following sections describe the options that you can configure using a runtime configuration file.

**Note** : When setting containerd registries, we recommend using `registryHosts` configuration, which covers more registry fields, rather than `privateRegistryAccessConfig`. And `registryHosts` overrides any matching FQDNs in `privateRegistryAccessConfig`.

### `privateRegistryAccessConfig`

Access private image registries with private credentials that you store in Secret Manager.

This option is available with GKE versions 1.27.3-gke.1700 or later for Container-Optimized OS node images, and 1.33 or later for Ubuntu node images.

For instructions, see [Access private registries with private CA certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates).
    
    
    privateRegistryAccessConfig:
      enabled: true
      certificateAuthorityDomainConfig:
      - gcpSecretManagerCertificateConfig:
        secretURI: "SECRET_LOCATION"
      fqdns:
      - "FQDN1"
      - "FQDN2"

This configuration has the following fields:

  * `enabled`: a boolean to enable private registry configuration. If you set `enabled: false`, delete any other fields in the `privateRegistryAccessConfig` item.
  * `certificateAuthorityDomainConfig`: contains up to five certificate and FQDN definitions.
  * `gcpSecretManagerCertificateConfig`: contains a certificate stored in Secret Manager and an array of FQDNs.
  * `secretURI`: the location of the certificate in Secret Manager. `privateRegistryAccessConfig` supports global secrets only in `secretURI`.
  * `fqdns`: a list of fully-qualified domain names of private registries. You can also use IPv4 addresses, but we recommend using the FQDN.



### `registryHosts`

Configure advanced settings for containerd registries, such as capabilities, custom headers, and certificates. This corresponds to containerd's [hosts.toml](https://github.com/containerd/containerd/blob/main/docs/hosts.md).

This option is available for GKE versions 1.34.1-gke.2980000 or later.
    
    
    registryHosts:
    - server: "REGISTRY_SERVER_FQDN"
      hosts:
      - host: "MIRROR_FQDN"
        capabilities:
        - "HOST_CAPABILITY_PULL"
        - "HOST_CAPABILITY_RESOLVE"
        - "HOST_CAPABILITY_PUSH"
        overridePath: false
        dialTimeout: "30s"
        header:
        - key: "HEADER_KEY"
          value:
          - "HEADER_VALUE_1"
          - "HEADER_VALUE_2"
        ca:
        - gcpSecretManagerSecretUri: "projects/PROJECT_ID_OR_NUMBER/secrets/CA_SECRET/versions/VERSION"
        client:
        - cert:
            gcpSecretManagerSecretUri: "projects/PROJECT_ID_OR_NUMBER/secrets/CLIENT_CERT_SECRET/versions/VERSION"
          key:
            gcpSecretManagerSecretUri: "projects/PROJECT_ID_OR_NUMBER/secrets/CLIENT_KEY_SECRET/versions/VERSION"

This configuration has the following fields:

  * `server`: The hostname of the registry server (for example, `example.com`). This is used to name the configuration file on the node. This should be fully-qualified domain name or IP address without scheme, port, or path.
  * `hosts`: A list of host-specific configurations for the `server`.
  * `host`: The hostname of a registry mirror (for example, `https://mirror.example.com:8000/1234`, `1.2.3.4:80`). This should be fully-qualified domain names or IP addresses. Scheme, port, and path are supported. Scheme can only be `http` or `https`.
  * `capabilities`: A list of capabilities specifying what operations a host is capable of performing. Supported values are any of the following: 
    * `HOST_CAPABILITY_PULL`: represents the capability to fetch manifests and blobs by digest.
    * `HOST_CAPABILITY_RESOLVE`: represents the capability to fetch manifests by name.
    * `HOST_CAPABILITY_PUSH`: represents the capability to push blobs and manifests.
If unspecified, all capabilities are enabled.
  * `overridePath`: A boolean. If `true`, indicates that the host's API root endpoint is defined in the URL path rather than by the API specification. This can be used with non-compliant OCI registries which are missing the `/v2` prefix. Defaults to `false`.
  * `dialTimeout`: A duration string (for example, `"30s"`) specifying the maximum duration allowed for a connection attempt to complete. Maximum allowed value is `"180s"`. If not set, containerd sets a default of `"30s"`. The value should be a decimal number of seconds with an `s` suffix.
  * `header`: A list of custom HTTP headers to send to the registry host. 
    * `key`: The header key.
    * `value`: A list of header values.
  * `ca`: A list of certificate configurations for the registry host's Certificate Authority (CA). To create secret for certificates and configure required permissions, see instructions in [Store your CA public keys in Secret Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates#store-keys-secret-manager). 
    * `gcpSecretManagerSecretUri`: The URI of a secret in Secret Manager containing the CA certificate. It supports both global secrets and regional secrets. The formats are the following, for the respective secret types: 
      * Global secret format: `projects/PROJECT_ID_OR_NUMBER/secrets/SECRET_NAME/versions/VERSION`.
      * Regional secret format: `projects/PROJECT_ID_OR_NUMBER/locations/REGION/secrets/SECRET_NAME/versions/VERSION`.
  * `client`: A list of client certificate and key pairs for authenticating to the registry host. To create secret for certificates and configure required permissions, see instructions in [Store your CA public keys in Secret Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-private-registries-private-certificates#store-keys-secret-manager). 
    * `cert`: The client certificate configuration.
      * `gcpSecretManagerSecretUri`: The URI of a secret in Secret Manager containing the client certificate. It supports both global secrets and regional secrets.
    * `key`: The client private key configuration.
      * `gcpSecretManagerSecretUri`: The URI of a secret in Secret Manager containing the client key. It supports both global secrets and regional secrets.



### `writableCgroups`

Mount the `/sys/fs/cgroup` file system in read-write mode so that workloads can manage the resources of their child processes.

This option is available for GKE versions 1.34.1-gke.2541000 or later.

For more information, see [Configure writable cgroups for containers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/writable-cgroups).
    
    
    writableCgroups:
      enabled: true

## Apply containerd configuration to new clusters

This section shows you how to apply a containerd configuration file when you create a new GKE cluster.

Run the following command to create Autopilot clusters:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=LOCATION \
        --scopes="cloud-platform" \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

**Note** : If your configuration file does not use secrets from Secret Manager, such as for the `privateRegistryAccessConfig` feature or when using `registryHosts` with certificates stored in Secret Manager, you can remove the `--scopes="cloud-platform"` flag.

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `LOCATION`: the Compute Engine location of your new cluster.
  * `PATH_TO_CONFIG_FILE`: the path to the configuration file that you created, like `~/containerd-configuration.yaml`.



You can enable the containerd configuration on new Standard clusters by running the `gcloud container clusters create` command with the same options. And unless you specify a different containerd configuration, new node pools that are created in the cluster inherit the cluster-level default containerd configuration.

### Apply containerd configuration to new node pools

You can apply the containerd configuration to a new GKE node pool with following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --scopes="cloud-platform" \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

**Note** : If your configuration file does not use secrets from Secret Manager, such as for the `privateRegistryAccessConfig` feature or when using `registryHosts` with certificates stored in Secret Manager, you can remove the `--scopes="cloud-platform"` flag.

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of the existing cluster.
  * `LOCATION`: the Compute Engine location of your new node pool.
  * `PATH_TO_CONFIG_FILE`: the path to the configuration file that you created, like `~/containerd-configuration.yaml`.



## Apply containerd configuration to existing clusters

This section shows you how to apply a containerd configuration to existing clusters and nodes.

Updating the cluster-level containerd configuration applies only to node pools that don't have their own settings defined at the node pool level (such as `registryHosts` or `writableCgroups`). GKE re-creates the nodes in these node pools to apply the new configuration. Node pools with node pool-level settings continue to use their own configuration and their nodes are not re-created. Updating a cluster or node pool with a containerd configuration re-creates the nodes to apply the configuration. This might cause temporary disruptions in running workloads. GKE only re-creates nodes if automatic upgrades are enabled. This re-creation respects any [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) that you set. In Standard clusters that don't have automatic upgrades enabled, you must manually re-create your nodes to apply the configuration.

### Check access scopes

If your configuration file uses secrets from Secret Manager, your cluster or node pool must have the `cloud-platform` access scope. This section shows you how to check your access scopes and update an existing cluster with a new or modified runtime configuration file.

For details about the default access scopes in new clusters, see [Access scopes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes#default_access_scopes).

#### Check Autopilot access scopes

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION \
        --flatten=nodeConfig \
        --format='csv[delimiter="\\n",no-heading](oauthScopes)'

If you are using secrets from Secret Manager and your cluster doesn't have the `https://www.googleapis.com/auth/cloud-platform` access scope, create a new cluster with this access scope.

#### Check Standard access scopes

To check your Standard cluster access scopes, check a node pool:
    
    
    gcloud container node-pools describe NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --format='value[delimiter="\\n"](config.oauthScopes)'

Replace `NODE_POOL_NAME` with the name of the node pool.

If you are using secrets from Secret Manager and your cluster doesn't have the `https://www.googleapis.com/auth/cloud-platform` access scope, create a new node pool with the `cloud-platform` access scope and delete your existing node pool.

### Update the cluster to use your configuration file

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

### Update a node pool to use a configuration file

To update the containerd configuration for a node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=LOCATION \
        --containerd-config-from-file="PATH_TO_CONFIG_FILE"

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool that you want to update.
  * `CLUSTER_NAME`: the name of the existing cluster.
  * `LOCATION`: the Compute Engine location of the cluster.
  * `PATH_TO_CONFIG_FILE`: the path to the configuration file that you created, like `~/containerd-configuration.yaml`.



### Re-create nodes in Standard clusters

If your Standard cluster doesn't use automatic upgrades, you must manually re-create your node pools to apply the new configuration. To trigger a manual node re-creation, upgrade your cluster to the same GKE version that it already uses.
    
    
    gcloud container clusters upgrade CLUSTER_NAME \
        --location=LOCATION \
        --cluster-version=VERSION

Replace `VERSION` with the same GKE patch version that the cluster already uses.

## Disable containerd configuration options

### Disable `privateRegistryAccessConfig`

  1. Update your configuration file to specify `enabled: false` in `privateRegistryAccessConfig` and delete any other fields in the item, like in the following example:
         
         privateRegistryAccessConfig:
           **enabled : false**

  2. Apply the updated configuration file to your cluster. For instructions, see [Apply containerd configuration to existing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration#containerd-configuration-existing-clusters).



### Disable `registryHosts`

  1. Update your configuration file to specify an empty array in the `registryHosts` item, like in the following example:
         
         registryHosts: []

  2. Apply the updated configuration file to your cluster. For instructions, see [Apply containerd configuration to existing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-containerd-configuration#containerd-configuration-existing-clusters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
