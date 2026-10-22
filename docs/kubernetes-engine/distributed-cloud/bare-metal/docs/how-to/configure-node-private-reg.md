---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-node-private-reg/
title: Configure nodes to authenticate to a private registry \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:48.931315+00:00
---

# Configure nodes to authenticate to a private registry  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/configure-node-private-reg/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure nodes to authenticate to a private registry Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your Google Distributed Cloud cluster so that its worker nodes can use private registries, including Artifact Registry. Node-level private registries are intended for use with your workloads to give you more control over image pulls and their related security. When you configure a cluster with the private registries as described in this document, Google Distributed Cloud updates the containerd configuration accordingly. Once your cluster is configured, all Pods on qualified nodes can use the registries without having to specify `imagePullSecrets` in the Pod spec.

This feature can be enabled or disabled at any time in the cluster lifecycle.

The following list shows the launch stage for this feature per version:

  * 1.30 and later: GA
  * 1.29: [Preview](https://cloud.google.com/products/#product-launch-stages)



## Prerequisites

###  1.30 and later 

To use this GA feature, your cluster must meet the following requirements:

  * The cluster version must be at 1.30 or later.
  * The node pool version must be at 1.29 or later (a 1.30 cluster can have node pools at version 1.28, but the feature only works for node pools at version 1.29 or later).
  * This feature is for user clusters and self-managing (hybrid and standalone) clusters with worker node pools, as shown in the following table:

Deployment model | Supported cluster types  
---|---  
Admin and user cluster deployment |  Admin cluster User cluster 1 User cluster 2  
Hybrid cluster deployment |  Hybrid cluster User cluster 1 User cluster 2  
Standalone cluster deployment |  Standalone cluster  



###  1.29 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To use this [Preview](https://cloud.google.com/products/#product-launch-stages) feature, your cluster must meet the following requirements:

  * The cluster version must be at 1.29.
  * The Node pool version must be at 1.29 (not all node pools need to be at version 1.29, but the feature only works for node pools at version 1.29).
  * The cluster must have the `preview.baremetal.cluster.gke.io/private-registry: "enable"` preview feature annotation.
  * This feature is for user clusters and self-managing (hybrid and standalone) clusters with worker node pools, as shown in the following table:

Deployment model | Supported cluster types  
---|---  
Admin and user cluster deployment |  Admin cluster User cluster 1 User cluster 2  
Hybrid cluster deployment |  Hybrid cluster User cluster 1 User cluster 2  
Standalone cluster deployment |  Standalone cluster  



## Configure a self-managing cluster for private registries

To configure a standalone or hybrid cluster to use node-level private registries:

  1. Edit the cluster configuration file to add the `privateRegistries` block in the credentials section:
         
         ---
         gcrKeyPath: baremetal/gcr.json
         sshPrivateKeyPath: .ssh/id_rsa
         ...
         privateRegistries:
           - host: REGISTRY_HOST
             caCertPath: CA_CERT_PATH
             pullCredentialConfigPath: CREDENTIALS_FILE_PATH
         ...
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-hybrid-basic
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: hybrid-basic
           namespace: cluster-hybrid-basic
           annotations:**    preview.baremetal.cluster.gke.io/private-registry: "enable" # Version 1.29 clusters only**
             ...
         spec:
           type: hybrid
           ...
         

Replace the following:

     * `REGISTRY_HOST`: the domain name or IP address of the private registry and the port. For example: `10.200.0.2:5007`.

     * `CA_CERT_PATH`: the path of the CA cert file (server root CA). For example: `/root/cert.pem`. If your private registry doesn't require a private TLS certificate, then you can omit this field.

     * `CREDENTIALS_FILE_PATH`: the path of the configuration file, `config.json` (for example, `$HOME/.docker/config.json`). To authenticate containerd to access your private registry, `config.json` must contain a base64-encoded version of your credentials in the `auths` section of the file.

For Artifact Registry, authenticate using a service account JSON key with the following values:

       * `username`: `_json_key`
       * `password`: the _entire contents_ of the service account JSON key file. Enclose the pasted JSON key content in single quotes (`'`) to prevent parsing errors.

For more information about how to generate this file, see [Configure authentication to Artifact Registry for Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#json-key) in the Artifact Registry documentation.

For other private registries, the base64-encoded `auth` string is typically formed from `USERNAME:PASSWORD`, using your specific registry credentials. If your private registry server doesn't require credentials for authentication, then you can omit the `pullCredentialConfigPath` field.

To protect sensitive data, you can use `chown` and `chmod` to restrict access to the configuration file.

  2. Apply the changes to your cluster:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=CLUSTER_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you want to update.

     * `CLUSTER_KUBECONFIG`: path of the self-managed (hybrid or standalone) cluster kubeconfig file.




## Configure a user cluster for private registries

With user clusters, the private registry configuration is specified in the user cluster resource spec, which is located in the admin cluster. Additionally, you need to store the private registry credentials in a Secret, which is also located in the admin cluster:

  1. Create a `kubernetes.io/dockerconfigjson` type Kubernetes Secret for the registry credentials:

If you want to scope the Secret to a specific namespace, add the `--namespace` flag to the following command to specify the name of the namespace. If the Secret isn't in the same namespace as the cluster, add the annotation `baremetal.cluster.gke.io/mark-source: "true"`, as shown in the example at the end of this step.
         
         kubectl create secret docker-registry CREDS_SECRET_NAME \
             --from-file=.dockerconfigjson=CREDENTIALS_FILE_PATH \
             --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CREDS_SECRET_NAME`: the name for your Secret.

     * `CREDENTIALS_FILE_PATH`: the path of the configuration file, `config.json` (for example, `$HOME/.docker/config.json`). To authenticate containerd to access your private registry, `config.json` must contain a base64-encoded version of your credentials in the `auths` section of the file.

For Artifact Registry, authenticate using a service account JSON key with the following values:

       * `username`: `_json_key`
       * `password`: the _entire contents_ of the service account JSON key file. Enclose the pasted JSON key content in single quotes (`'`) to prevent parsing errors.

For more information about how to generate this file, see [Configure authentication to Artifact Registry for Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#json-key) in the Artifact Registry documentation.

For other private registries, the base64-encoded `auth` string is typically formed from `USERNAME:PASSWORD`, using your specific registry credentials. If your private registry server doesn't require credentials for authentication, then you can omit the `pullCredentialSecretRef` field.

To protect sensitive data, you can use `chown` and `chmod` to restrict access to the configuration file.

Your Secret should look similar to the following example:
    
    apiVersion: v1
    data:
      .dockerconfigjson: ewoJImF1dGhzIjogewoJ...clpYSXdNak14IgoJCX0KCX0KfQ==
    kind: Secret
    metadata:
      creationTimestamp: "2024-04-28T22:06:06Z"
      name: private-registry-secret
      namespace: default
      resourceVersion: "5055821"
      ...
      annotations:
        ...**    baremetal.cluster.gke.io/mark-source: "true"**
    type: kubernetes.io/dockerconfigjson
    

  2. If applicable, store the CA cert for the registry in a Secret.

The Secret looks similar to the following:
         
         apiVersion: v1
         kind: Secret
         metadata:
           annotations:
             baremetal.cluster.gke.io/mark-source: "true"
           name: ca-9dd74fd308bac6df562c7a7b220590b5
           namespace: some-namespace
         type: Opaque
         data:
           ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUR2RENDQXFTZ0F3SUJBZ0lVQi
           3UGxjUzVFVk8vS0xuYjZiMHRhRFVleXJvd0RRWUpLb1pJaHZjTkFRRUwKQlFBd2ZqRUxNQWtHQ
           ...
           QnpPTkxTRFZJVk5LMm9YV1JvNEpJY0ZoNFZ4MWRMRHpqMldEaHhrUEljWEhLdGR3dk5iS2tocU
           LUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
           ```
         

  3. Edit the user cluster configuration file to enable and configure the private registry:

     1. For version 1.29 clusters only, add the [Preview](https://cloud.google.com/products/#product-launch-stages) feature annotation `preview.baremetal.cluster.gke.io/private-registry: "enable"` to enable the feature. For version 1.30 and later clusters, the private registry feature is enabled by default.
            
            apiVersion: baremetal.cluster.gke.io/v1
            kind: Cluster
            metadata:
              name: user-basic
              namespace: cluster-user-basic
              resourceVersion: "766027"
              annotations:
                ...**    preview.baremetal.cluster.gke.io/private-registry: "enable"**
            ...
            

     2. In the `nodeConfig` section of the user cluster configuration file, add the `privateRegistries` block:
            
            apiVersion: baremetal.cluster.gke.io/v1
            kind: Cluster
            metadata:
              name: user-basic
            ...
            spec:
              bypassPreflightCheck: false
            ...
              nodeConfig:
                containerRuntime: containerd
                podDensity:
                  maxPodsPerNode: 250**    privateRegistries:
                - caCertSecretRef:
                    name: CA_CERT_SECRET_NAME
                    namespace: CA_CERT_SECRET_NAMESPACE
                  host: REGISTRY_HOST
                  pullCredentialSecretRef:
                    name: CREDS_SECRET_NAME
                    namespace: CREDS_SECRET_NAMESPACE**
            

Replace the following:

     * `CA_CERT_SECRET_NAME`: the name of the Secret that you created to store the CA cert. If you didn't create this secret, remove the `caCertSecretRef` block. If multiple private registries reference CA certificate secrets with the same name across different namespaces (except the `anthos-creds` or cluster namespace), the system adds a prefix to the target secret name to make sure the CA certificate secret names are unique across namespaces. The system won't add a prefix to secrets in the cluster namespace or the source namespace in `anthos-creds`.

     * `CA_CERT_SECRET_NAMESPACE`: the name of the namespace for the CA cert Secret, if you created it.

     * `REGISTRY_HOST`: the domain name or IP address of the private registry and the port. For example: `10.200.0.2:5007`.

     * `CREDS_SECRET_NAME`: the name of the `kubernetes.io/dockerconfigjson` type Secret for the registry credentials.

     * `CREDS_SECRET_NAMESPACE`: the namespace name for the Secret for the registry credentials.

  4. Apply the changes to your cluster:
         
         bmctl update cluster -c USER_CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `USER_CLUSTER_NAME`: the name of the cluster you are updating.

     * `ADMIN_KUBECONFIG`: path of the admin cluster kubeconfig file.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
