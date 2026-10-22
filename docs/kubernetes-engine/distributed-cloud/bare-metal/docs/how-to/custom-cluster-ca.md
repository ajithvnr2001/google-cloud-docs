---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/custom-cluster-ca/
title: Use custom cluster certificate authorities \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:53.442237+00:00
---

# Use custom cluster certificate authorities  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/custom-cluster-ca/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Use custom cluster certificate authorities Stay organized with collections  Save and categorize content based on your preferences. 

Cluster certificate authorities (CAs) issue and sign certificates to enable secure authentication and encryption between cluster components. By default, in Google Distributed Cloud, the Cluster API creates the cluster CAs when you create a new cluster. This document describes how you can use your own certificate authorities with Google Distributed Cloud. Using custom cluster CAs gives you more control over issuing and managing your cluster certificates. You can also control trust, encryption algorithm parameters, the depth of subordinate certificates, and their purpose.

To use custom CAs, you provide root CAs, consisting of a CA certificate file and its corresponding private key file. You provide a CA certificate and key file pair for each of the following required cluster CAs:

  * **etcd CA** : the certificate for the etcd CA certificate secures communication from the Kubernetes API server to the etcd replicas and also communication between etcd replicas.

  * **cluster CA** : the certificate for the cluster CA secures communication between the Kubernetes API server and all internal Kubernetes API clients. Clients include the kubelet, the controller manager, and the scheduler.

  * **front-proxy CA** : the certificate for the front-proxy CA secures communication with [aggregated APIs](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/apiserver-aggregation/).




You can provide a unique certificate-key pair for each CA or you can reuse a certificate-key pair for more than one of the CAs.

You apply the certificate-key pairs during [cluster creation (`bmctl` method only)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview) and [CA rotation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation). The Custom Cluster CA feature works with all cluster types: admin, user, hybrid, and standalone.

**Note:** When you create a user cluster with `bmctl`, you typically remove the credentials section of the cluster configuration file. To specify custom cluster CAs when you create a user cluster, specify only the custom cluster CA certificate and private key paths in the credentials section.

## Prerequisites

You're responsible for preparing your own root CAs according to the following rules:

  * Custom CAs are root CAs, each consisting of a self-signed certificate file and a private key file.

  * For your certificate, we recommend that you use the Distinguished Encoding Rules (DER) format (see [recommendation X.690 for ASN.1 encoding rules](https://www.itu.int/rec/T-REC-X.690/)). Your certificate file should contain base64-encoded data preceded by `‑‑‑‑‑BEGIN CERTIFICATE‑‑‑‑‑` and followed by `‑‑‑‑END CERTIFICATE‑‑‑‑‑`.

  * For the private key, we recommend that you use the [Public-Key Cryptography Standards (PKCS) #1](https://datatracker.ietf.org/doc/html/rfc8017) format. Your key file should contain base64-encoded data preceded by `‑‑‑‑BEGIN RSA PRIVATE KEY‑‑‑‑` and followed by `‑‑‑‑END RSA PRIVATE KEY‑‑‑‑`.

  * To minimize potential cluster disruption, custom CAs shouldn't expire sooner than five years. We recommend a longer expiration period, such as 10 to 30 years.

  * Make sure the certificate and key files are on the admin workstation where you run `bmctl` commands.

  * The user who runs `bmctl` commands must have access to the directory in which you store the files. We recommend that you put the files in an existing directory used for certificates and keys. For example, you can store the files in `~/baremetal/bmctl-workspace/.sa-keys` along with your service account keys.

  * The user who runs `bmctl` commands must have read access to the files.




## Use a custom CA during cluster creation

When you [create a cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview) with `bmctl`, you first update the cluster configuration file to describe your cluster features and settings. To use the Custom Cluster CA feature during cluster creation, you have two options for specifying the custom cluster CAs in the cluster configuration file:

  * Specify the paths for both the CA certificate files and the private key files
  * Specify the paths for the private key files only



When you specify the private keys only, `bmctl` looks for the corresponding CA certificate files in the same directory. Certificate files must have the same name as the corresponding private key files and the `.crt` file extension. For example, if the private key path is `/custom-ca/cluster_ca.key`, then `bmctl` expects the certificate path to be `/custom-ca/cluster_ca.crt`.

In either case, the paths are specified in the credentials section of the configuration file as shown in the following examples.

Example 1: Specify certificate and key paths

The following excerpt from a cluster configuration file shows how to specify the paths to both the certificate and key files for each cluster CA. In this example, the CA certificate and key files are in the same directory as the service account JSON key files.

**Note:** For a user cluster, you remove the service account and SSH key paths from the credentials section.
    
    
    gcrKeyPath: bmctl-workspace/.sa-keys/myproject-anthos-baremetal-gcr.json
    ...
    cloudOperationsServiceAccountKeyPath: bmctl-workspace/.sa-keys/myproject-anthos-baremetal-cloud-ops.json** clusterCACertPath: bmctl-workspace/.sa-keys/cluster_ca_cert.pem
    clusterCAPrivateKeyPath: bmctl-workspace/.sa-keys/cluster_ca_key.pem
    etcdCACertPath: bmctl-workspace/.sa-keys/etcd_ca_cert.pem
    etcdCAPrivateKeyPath: bmctl-workspace/.sa-keys/etcd_ca_key.pem
    frontProxyCACertPath: bmctl-workspace/.sa-keys/front_proxy_ca_cert.pem
    frontProxyCAPrivateKeyPath: bmctl-workspace/.sa-keys/front_proxy_ca_key.pem**
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin-test
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    ...
    

Example 2: Specify private key paths only

The following excerpt from a cluster configuration file shows how to specify the paths to key files only. In this example, the CA private key files are in the same directory as the service account JSON key files. The corresponding CA certificate files must be in the `/.sa-keys` directory, too. Certificate files have the same filename as the key files, but with a `.crt` extension. So, the etcd CA certificate file has the name `etcd_ca.crt`.

**Note:** For a user cluster, you remove the service account and SSH key paths from the credentials section.
    
    
    gcrKeyPath: bmctl-workspace/.sa-keys/myproject-anthos-baremetal-gcr.json
    ...
    cloudOperationsServiceAccountKeyPath: bmctl-workspace/.sa-keys/myproject-anthos-baremetal-cloud-ops.json** clusterCAPrivateKeyPath: bmctl-workspace/.sa-keys/cluster_ca_key.pem
    etcdCAPrivateKeyPath: bmctl-workspace/.sa-keys/etcd_ca_key.pem
    frontProxyCAPrivateKeyPath: bmctl-workspace/.sa-keys/front_proxy_ca_key.pem**
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin-test
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    ...
    

Example 3: Reuse a single pair of CA certificate and key files

The following excerpt from a cluster configuration file shows how to specify the paths to key files only. In this example, a single certificate-key pair is used for all cluster CAs. The CA certificate and private key files are both in the `/custom-ca` directory. Following the naming convention, the CA certificate filename is `custom_ca.crt`.

**Note:** For a user cluster, you remove the service account and SSH key paths from the credentials section.
    
    
    gcrKeyPath: bmctl-workspace/.sa-keys/myproject-anthos-baremetal-gcr.json
    ...
    cloudOperationsServiceAccountKeyPath: bmctl-workspace/.sa-keys/myproject-anthos-baremetal-cloud-ops.json** clusterCAPrivateKeyPath: /custom-ca/custom_ca.key
    etcdCAPrivateKeyPath: /custom-ca/custom_ca.key
    frontProxyCAPrivateKeyPath: /custom-ca/custom_ca.key**
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin-test
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    ...
    

## Use a custom CA during CA rotation

When you [rotate CAs](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/ca-rotation), you can specify the paths for your custom cluster CA certificate and private key files. The options you have are similar to the options for specifying custom cluster CAs during cluster creation. When you run the `bmctl update credentials certificate-authorities rotate` command, you have the following options:

  * Specify the paths for both the custom CA certificate files and the private key files.
  * Specify the paths for the custom CA private key files only. The corresponding CA certificate file must be in the same directory, have the same name as the key file, and have a `.crt` file extension.
  * Reuse a CA certificate-key pair by specifying the same certificate and key paths for more than one cluster CA.
  * Omit the arguments for the custom CA paths. If you don't specify custom CA paths when you rotate CAs, Google Distributed Cloud creates and uses the standard cluster CA.



Example 1: Specify CA certificate and private key paths
    
    
    bmctl update credentials certificate-authorities rotate \
        --cluster CLUSTER_NAME \
        --kubeconfig ADMIN_KUBECONFIG \
        --cluster-ca-cert-path=CLUSTER_CA_CERT_PATH \
        --cluster-ca-private-key-path=CLUSTER_CA_KEY_PATH \
        --etcd-ca-cert-path=ETCD_CA_CERT_PATH \
        --etcd-ca-private-key-path=ETCD_CA_KEY_PATH \
        --front-proxy-ca-cert-path=FRONT_PROXY_CA_CERT_PATH \
        --front-proxy-ca-private-key-path=FRONT_PROXY_CA_KEY_PATH
    

Replace the following:

  * CLUSTER_NAME: the name of the cluster for which you want to rotate CAs.
  * ADMIN_KUBECONFIG: the path to the admin cluster kubeconfig file. For self-managing clusters, this file is the cluster's kubeconfig file.
  * CLUSTER_CA_CERT_PATH: the path of the cluster CA certificate file.
  * CLUSTER_CA_KEY_PATH: the path of the cluster CA private key file.
  * ETCD_CA_CERT_PATH: the path of the etcd CA certificate file.
  * ETCD_CA_KEY_PATH: the path of the etcd CA private key file.
  * FRONT_PROXY_CA_CERT_PATH: the path of the front-proxy certificate file.
  * FRONT_PROXY_CA_KEY_PATH: the path of the front-proxy private key file.



Example 2: Specify private key paths only
    
    
    bmctl update credentials certificate-authorities rotate \
        --cluster CLUSTER_NAME \
        --kubeconfig ADMIN_KUBECONFIG \
        --cluster-ca-private-key-path=CLUSTER_CA_KEY_PATH \
        --etcd-ca-private-key-path=ETCD_CA_KEY_PATH \
        --front-proxy-ca-private-key-path=FRONT_PROXY_CA_KEY_PATH
    

Replace the following:

  * CLUSTER_NAME: the name of the cluster for which you want to rotate CAs.
  * ADMIN_KUBECONFIG: the path to the admin cluster kubeconfig file. For self-managing clusters, this file is the cluster's kubeconfig file.
  * CLUSTER_CA_KEY_PATH: the path of the cluster CA private key file.
  * ETCD_CA_KEY_PATH: the path of the etcd CA private key file.
  * FRONT_PROXY_CA_KEY_PATH: the path of the front-proxy private key file.



## Intermediate CAs

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Version 1.29 clusters support the use of intermediate CAs as a [Preview](https://cloud.google.com/products/#product-launch-stages) capability. This capability isn't at the same launch stage for all supported product versions:

  * 1.29: [Preview](https://cloud.google.com/products/#product-launch-stages)
  * 1.28: Not available
  * 1.16: Not available



Similar to the root CA requirement for custom CAs, to use intermediate CAs you must prepare three sets of CAs. Each CA consists of a CA certificate file and its corresponding private key file. You provide a CA certificate and key file pair for each of the following required cluster CAs:

  * etcd CA
  * cluster CA
  * front-proxy CA



As with root CAs, you can provide a unique certificate-key pair for each CA or you can reuse a certificate-key pair for more than one of the CAs by specifying the same file paths in the CA configuration.

When you use intermediate CAs, the CA certificate file should contain the whole certificate chain, which includes certificates from the intermediate CAs up to the root CA. The certificates are listed in reverse order of how they were signed, with the last intermediate CA certificate at the top and the root CA certificate at the bottom.

In the following example (starting with the root CA at the bottom), the order indicates the following:

  * Root CA signed the Intermediate-A CA certificate
  * Intermediate-A CA signed the Intermediate-B CA certificate
  * The chain continues up to the final Intermediate-Y CA certificate, which was signed by the Intermediate-X CA


    
    
    -----BEGIN CERTIFICATE-----
    <Intermediate-Y CA CERT CONTENT>
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    <Intermediate-X CA CERT CONTENT>
    -----END CERTIFICATE-----
    ...
    -----BEGIN CERTIFICATE-----
    <Intermediate-B CA CERT CONTENT>
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    <Intermediate-A CA CERT CONTENT>
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    <ROOT CA CERT CONTENT>
    -----END CERTIFICATE----- 
    

To continue with this example, the private key associated with the Intermediate-Y CA certificate should be passed along with the CA certificate chains in the same way as in a custom CA.
    
    
    -----BEGIN RSA PRIVATE KEY-----
    <Intermediate-Y PRIVATE KEY CONTENT>
    -----END RSA PRIVATE KEY-----
    

To check if the cluster is using the intermediate CA, inspect the certificate count in the cluster's CA secret:
    
    
    kubectl get secret CLUSTER_NAME-ca \
        --kubeconfig ADMIN_KUBECONFIG
        -n cluster-CLUSTER_NAME \
        -o jsonpath='{.data.tls\.crt}' | base64 --decode | grep "BEGIN CERTIFICATE" | wc -l
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
