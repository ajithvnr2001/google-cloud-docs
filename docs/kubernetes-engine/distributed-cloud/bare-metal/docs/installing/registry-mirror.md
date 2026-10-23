---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror/
title: Use a registry mirror for container images \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:24.288233+00:00
---

# Use a registry mirror for container images  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/registry-mirror/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Use a registry mirror for container images Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create and upgrade clusters using images pulled from a registry mirror, rather than from a public registry such as `gcr.io`. This feature can be enabled or disabled at any time in the cluster lifecycle.

This page is for Operators and Storage specialists who configure and manage storage performance, usage, and expense. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

A registry mirror is a local copy of a public registry that copies or mirrors the file structure of the public registry. For example, suppose that the path to your local registry mirror is `172.18.0.20:5000`. When `containerd` encounters a request to pull an image such as `gcr.io/kubernetes-e2e-test-images/nautilus:1.0`, `containerd` attempts to pull that image, not from `gcr.io`, but from your local registry at the following path: `172.18.0.20:5000/kubernetes-e2e-test-images/nautilus:1.0`. If the image isn't in this local registry path, the image is pulled automatically from the `gcr.io` public registry.

Using a registry mirror provides the following benefits:

  * Protects you from public registry outages.
  * Speeds up pod creation.
  * Lets you conduct your own vulnerability scanning.
  * Avoids limits imposed by public registries on how frequently you can issue commands to them.

**Note:** Image pulls for `gcr.io/anthos-baremetal-release/kindest/node` don't fall back to `gcr.io`. These images are pulled from the registry mirror only. If the registry mirror doesn't work, the pull fails.

## Before you begin

  * You must have a Artifact Registry server set up in your network.
  * If your registry server runs a private TLS certificate, you must have the certificate authority (CA) file.
  * If your registry server needs authentication, you must have the proper login credentials or Docker configuration file.
  * If you're using a Red Hat Quay registry, it might be necessary to create the directory structure of the local registry manually.
  * To use a registry mirror, you must set the container runtime to [containerd](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/runtime).
  * Make sure that you have enough disk space on your admin workstation for image uploads. The image upload command, `bmctl push images`, decompresses the downloaded images package file and then extracts all image files locally before uploading them. You need at least three times the size of the downloaded images package file in disk space for the image upload.

For example, the compressed `bmpackages_1.33.0-gke.799.tar.xz` file takes approximately 12 GB of disk space, so you should have at least 36 GB disk space free before you download the file.

If you're performing a [skip upgrade](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade#skip-upgrades) (upgrading two minor versions in a single operation), you need to upload images from images package files for both the target (`N+2`) version and the intermediate (`N+1`) version. Based on this example, you need approximately 72 GB of free disk space for the image upload. For more information about the intermediate version, see [Additional requirement for registry mirrors](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade#skip-registry).




## Download all required images for Google Distributed Cloud

Download the latest version of the `bmctl` tool and images package from the [Downloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/downloads) page.

**Note:** Prior to minor version 1.29, the images package tar file format is compatible with Docker. For minor version 1.29 and later, the images package tar file is in [Open Container Initiative (OCI) image format](https://github.com/opencontainers/image-spec/blob/main/spec.md), which isn't compatible with Docker.

## Upload container images to your registry server

When you use `bmctl push images` to upload container images to your repository server, `bmctl` performs the following steps in order:

  1. Decompress a downloaded images package compressed tar file, such as `bmpackages_1.36.200-gke.118.tar.xz` into `bmpackages_1.36.200-gke.118.tar`.

  2. Extract all the images from the decompressed tar file into a directory named `bmpackages_1.36.200-gke.118`.

  3. Push each image file to the private registry specified.

`bmctl` uses `--username` and `--password` values for basic authentication to push the images into your private registry.




The following sections illustrate some common variations of the `bmctl push images` command to upload images to your repository server.

### Authenticate with your registry and share the TLS certificate

The following command includes `--username` and `--password` flags for user authentication with your registry server. The command also includes the `--cacert` flag for passing the CA transport layer security (TLS) certificate, which is used for secure registry server communication, including image pushes and pulls. These flags provide basic security for your registry server.

If your registry server requires authentication and you don't use the `--username` and `--password` flags, you should be prompted for credentials when you run `bmctl push images`. You can either type in your password or choose the docker config file that contains the credentials.

To upload images with authentication and a private CA certificate, use a command like the following:
    
    
    bmctl push images \
        --source IMAGES_TAR_FILE_PATH \
        --private-registry REGISTRY_IP:PORT \
        --username USERNAME \
        --password PASSWORD \
        --cacert CERT_PATH
    

Replace the following:

  * `IMAGES_TAR_FILE_PATH`: the path of the downloaded images package tar file, such as `bmpackages_1.36.200-gke.118.tar.xz`.

  * `REGISTRY_IP:PORT`: the IP address and port of the private registry server.

  * `USERNAME`: the username of a user with access permissions to upload images to the registry server.

  * `PASSWORD`: the user's password for authenticating with the registry server.

  * `CERT_PATH`: the path of the CA cert file, if your registry server uses a private TLS certificate.




For example:
    
    
    bmctl push images \
        --source bmpackages_1.36.200-gke.118.tar.xz \
        --private-registry 172.18.0.20:5000 \
        --username alex --password pa55w0rd \
        --cacert /etc/pki/tls/certs/ca-bundle.crt
    

### Upload images without user authentication or certificates

If your registry server doesn't require credentials, such as a username and password, then specify `--need-credential=false` in the `bmctl` command. If your registry server uses a public TLS certificate, then you don't need to use the `--cacert` flag. This type of upload command is best suited to testing environments, where security is less of a concern than in production.

To upload images without authentication or a private CA certificate, use a command like the following:
    
    
    bmctl push images \
        --source IMAGES_TAR_FILE_PATH \
        --private-registry REGISTRY_IP:PORT \
        --need-credential=false
    

For example:
    
    
    bmctl push images \
        --source bmpackages_1.36.200-gke.118.tar.xz \
        --private-registry 172.18.0.20:5000 \
        --need-credential=false.
    

### Adjust the number of threads

The image upload routine can be time consuming due to the size and quantity of container images in the images package tar file. Increasing the number of parallel threads makes the routine run faster. You can use the `--threads` flag to change the number of parallel threads that `bmctl push images` uses.

By default, the image upload routine uses 4 threads. If your image uploads take too long, increase this value. As a benchmark, in a Google test environment, uploading images from a workstation with 4 CPUs takes approximately 10 minutes with 8 parallel threads.
    
    
    bmctl push images \
        --source IMAGES_TAR_FILE_PATH \
        --private-registry REGISTRY_IP:PORT \
        --cacert CERT_PATH \
        --threads NUM_THREADS
    

Replace `NUM_THREADS` with the number of parallel threads used to process the image uploads. By default, `bmctl push images` uses four parallel threads.

The following command increases the number of threads for the upload from `4` to `8` to reduce upload time:
    
    
    bmctl push images \
        --source bmpackages_1.36.200-gke.118.tar.xz \
        --private-registry 172.18.0.20:5000 \
        --cacert ~/cert.pem \
        --threads **8**
    

### Upload through proxy

If you need a proxy to upload the images from your workstation to the registry server, you can add the proxy details ahead of the `bmctl` command:
    
    
    HTTPS_PROXY=http://PROXY_IP:PORT bmctl push images \
        --source=IMAGES_TAR_FILE_PATH \
        --private-registry=REGISTRY_IP:PORT \
        --cacert=CERT_PATH
    

Replace the following:

  * `PROXY_IP:PORT`: the IP address and port of the proxy.

  * `IMAGES_TAR_FILE_PATH`: the path of the downloaded images package tar file, such as `bmpackages_1.36.200-gke.118.tar.xz`.

  * `REGISTRY_IP:PORT`: the IP address and port of the private registry server.

  * `CERT_PATH`: the path of the CA cert file, if your registry server uses a private TLS certificate.




Enter your username and password when prompted or select a Docker configuration file.

The following command uploads images through a proxy:
    
    
    **HTTPS_PROXY =http://10.128.0.136:3128** bmctl push images \
        --source bmpackages_1.36.200-gke.118.tar.xz \
        --private-registry 172.18.0.20:5000 \
        --cacert ~/cert.pem
    

### Use your own namespace with `bmctl push images`

If you want to use your own namespace in your registry server instead of the root namespace, `containerd` can pull from this namespace if you provide the API endpoint for your private registry in the `registryMirrors.endpoint` field of your cluster configuration file. The endpoint is usually in the format of `<REGISTRY_IP:PORT>/v2/<NAMESPACE>`. Check your private registry user guide for specific details. For more information, see About the use of `v2` in the registry endpoint.
    
    
    bmctl push images \
        --source=IMAGES_TAR_FILE_PATH \
        --private-registry=REGISTRY_IP:PORT/NAMESPACE \
        --cacert=CERT_PATH
    

Replace `NAMESPACE` with the name of the namespace in the registry server into which you want to upload images.

For example, if you only have access to `198.51.20.1:5000/test-namespace/`, you can use a command like the following to upload all the images under the `test-namespace` namespace:
    
    
    bmctl push images \
        --source=./bmpackages_1.36.200-gke.118.tar.xz \
        --private-registry=198.51.20.1:5000/**test-namespace** \
        --username=alex \
        --password=pa55w0rd \
        --cacert /etc/pki/tls/certs/ca-bundle.crt
    

Then, in the cluster configuration file, you can add the following to make `containerd` pull from the `test-namespace` namespace:
    
    
    registryMirrors:
      - endpoint: https://198.51.20.1:5000/v2/test-namespace
    

For more information on the `bmctl push images` command, see the [`bmctl` command reference](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/bmctl#push_images).

## Configure clusters to use a registry mirror

You can configure a registry mirror for a cluster at cluster creation or whenever you update an existing cluster. The following two sections describe the two methods available for configuring registry mirrors.

### Use the header section in the cluster configuration file

Starting with version 1.35, you can configure or update registry mirrors and private registries for both admin and user clusters by defining them in the top-level header section of your cluster configuration file. The configuration persists across updates.

When executing `bmctl update`, any registry configuration in the header section automatically overrides the `spec.nodeConfig` section of the cluster configuration file.

**Important:** To completely remove a registry mirror or private registry from a live cluster during an update, you must remove the configuration fully from both the top-level header section and the `spec.nodeConfig` subsection inline. If either section contains a configuration, it won't be removed.

For 1.34 and earlier, you must use the `nodeConfig.registryMirrors` section to specify registry mirrors and private registries in user clusters, and not the header section, because the header section doesn't persist across updates.

The following sample cluster configuration file specifies that images are to be pulled from a local registry mirror whose endpoint is `https://198.51.20.1:5000`. Some of the fields appearing at the beginning of this configuration file are described in the following sections.
    
    
    # Sample cluster config with registry mirror:
    ---
    gcrKeyPath: /bmctl/bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-gcr.json
    sshPrivateKeyPath: /root/ssh-key/id_rsa** registryMirrors:
      - endpoint: https://198.51.20.1:5000
        caCertPath: /root/ca.crt
        pullCredentialConfigPath: /root/.docker/config.json
        hosts:
          - somehost.io
          - otherhost.io**
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: cluster-admin1
    ---
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: admin1
      namespace: cluster-admin1
    spec:
      nodeConfig:
        containerRuntime: containerd
    ...
    

### Use the `nodeConfig.registryMirrors` section in the Cluster spec

Because you can share the secrets created for the managing cluster with your user cluster, you can use the `nodeConfig.registryMirrors` from the managing admin or hybrid cluster to specify the registry mirror in the Cluster spec for the user cluster.

To configure a user cluster to use the same registry mirror as the admin cluster, follow these steps:

  1. Get the `nodeConfig.registryMirror` section, including secret references, from `nodeConfig.registryMirrors` of the admin cluster resource:
         
         kubectl get cluster CLUSTER_NAME -n CLUSTER_NAMESPACE \
             --kubeconfig ADMIN_KUBECONFIG \
             -o yaml
         

Replace the following:

     * `CLUSTER_NAME`: the name of the admin or hybrid cluster that manages the user cluster.

     * `CLUSTER_NAMESPACE`: the namespace name for the managing cluster.

     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file of the managing cluster.

  2. Add the `nodeConfig.registryMirrors` configuration from the admin cluster to the cluster configuration file of the user cluster.

The `registryMirrors` section in the user cluster configuration file should look similar to the following example:
         
         ---
         gcrKeyPath: /bmctl/bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-gcr.json
         sshPrivateKeyPath: /root/ssh-key/id_rsa
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-user1
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: user1
           namespace: cluster-user1
         spec:
           nodeConfig:
             containerRuntime: containerd**    registryMirrors:
             -   caCertSecretRef:
                 name: the-secret-created-for-the-admin-cluster
                 namespace: anthos-creds
               endpoint: https://172.18.0.20:5000
               hosts:
                 -   somehost.io
                 -   otherhost.io
               pullCredentialSecretRef:
                 name: the-image-pull-creds-created-for-the-admin-cluster
                 namespace: anthos-creds**
         ...
         




To make subsequent changes to the registry mirror configuration for your user cluster, edit the `nodeConfig.registryMirrors` in the user cluster configuration file and apply your changes with `bmctl update`.

### `hosts` field

`containerd` checks the `hosts` section of the cluster configuration file to discover which hosts are mirrored locally. These hosts are mapped to the registry mirror endpoint specified in the cluster configuration file (`registryMirror.endpoint`). In the example configuration file from the preceding section, the public registries listed in the `hosts` section are `somehost.io` and `otherhost.io`. Because these public registries appear in the `hosts` section, `containerd` checks the private registry mirror first when it encounters pull requests for images from `somehost.io` or `otherhost.io`.

For example, suppose `containerd` receives a pull command to `somehost.io/kubernetes-e2e-test-images/nautilus:1.0`. Because `somehost.io` is listed as one of the hosts in the `hosts` section of the cluster configuration file, `containerd` looks in the local registry mirror for the `kubernetes-e2e-test-images/nautilus:1.0` image. If `somehost.io` isn't listed in the `hosts` section, `containerd` doesn't know that a local mirror of `somehost.io` exists. In that case, `containerd` doesn't check the mirror for the image, and it pulls the image from the `somehost.io` public registry.

Note that by default, Google Distributed Cloud automatically mirrors images from `gcr.io` so you don't need to list `gcr.io` as a host in the `hosts` section.

The `hosts` values and the `endpoint` value shouldn't overlap. For example, the following configuration sample shows a host, `europe-docker.pkg.dev`, that matches the domain portion of the endpoint value. In this case, you don't need to specify a `hosts` value:
    
    
    ...
    registryMirrors:
      ...
      endpoint: https://**europe-docker.pkg.dev** :5000/v2/cloud-data-fusion-images
      hosts:
        - **europe-docker.pkg.dev**
        ...
    

### `gcrKeyPath` field

If you want Google Distributed Cloud to automatically use Artifact Registry (`gcr.io`) to pull images that don't appear in your local registry, you must specify the path to the Artifact Registry service account key. Google Distributed Cloud doesn't have a mechanism for providing keys for other public registries.

If you don't plan on using the feature in which images are pulled from `gcr.io` when they don't appear in your local registry, then you don't need to add a `gcrKeyPath` to the cluster configuration file.

### `caCertPath` field

If your registry requires a private transport layer security (TLS) certificate, this field takes the path to the server root CA certificate file. This certificate file should be on the admin workstation, the machine running `bmctl` commands. If your registry doesn't require a private TLS certificate, then you can leave the `caCertPath` field blank.

### `pullCredentialConfigPath` field

If your registry server doesn't require an authentication Docker configuration file, then you can leave the `pullCredentialConfigPath` field blank. Note that this is the path to the configuration file on the machine running `bmctl` commands.

## Use a registry mirror with user clusters

User clusters don't automatically pull images from a registry mirror if their admin cluster has been configured to do so. To have user clusters pull from a registry mirror, you need to configure them individually as described in Configure clusters to use a registry mirror.

## Update registry mirror endpoints, certificates, and pull credentials

To update registry mirror endpoints, certificates, or pull credentials:

  1. In the cluster configuration file, update the endpoint, CA certificate file, and path of the pull credential configuration file.

  2. Apply the changes by running:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * `CLUSTER_NAME` with the name of the cluster you want to update.

     * `ADMIN_KUBECONFIG` with the path of its admin cluster configuration file.




## Verify images are pulled from registry mirror

You can determine whether `containerd` is pulling images from your local registry by examining the contents of a `config.toml` file as shown in the following steps:

  1. Log into a node and examine the contents of the following file: `/etc/containerd/config.toml`

  2. Check the `plugins."io.containerd.grpc.v1.cri".registry.mirrors` section of the `config.toml` file to see whether your registry server is listed in the `endpoint` field. Here's an excerpt from an example `config.toml` file in which the `endpoint` field appears in bold:
         
         version = 2
         root = "/var/lib/containerd"
         state = "/run/containerd"
         ...
         [plugins."io.containerd.grpc.v1.cri".registry]
           [plugins."io.containerd.grpc.v1.cri".registry.configs]
             [plugins."io.containerd.grpc.v1.cri".registry.configs."gcr.io"]
               [plugins."io.containerd.grpc.v1.cri".registry.configs."privateregistry2.io".tls]
                 ca_file = '/etc/containerd/certs.d/privateregistry2.io/ca.crt'
           [plugins."io.containerd.grpc.v1.cri".registry.mirrors]
             [plugins."io.containerd.grpc.v1.cri".registry.mirrors."gcr.io"]
               **endpoint = ["http://privateregistry.io", "https://privateregistry2.io"]**
         ...
         

If your registry mirror appears in the `endpoint` field, then the node is pulling images from your registry mirror rather than from a public registry.




## Troubleshoot registry mirror settings

You can use `crictl`, the container runtime interface command-line tool, to test your registry settings by downloading individual image files. Each image file is tagged independently with a meaningful version string. For example, the cluster API controller image is tagged with the Google Distributed Cloud release version and the etcd image is tagged with the corresponding etcd version.

For the version 1.31.200-gke.59 release of Google Distributed Cloud for bare metal, the cluster API controller image, `cluster-api-controller`, and the etcd image, `etcd`, have the following tags:

  * `cluster-api-controller:**1.31.200-gke.59**`
  * `etcd:**v3.4.30-0-gke.1**`



### Pull an image from the registry mirror

If your registry mirror doesn't use namespaces, use the following command to pull an image:
    
    
    crictl pull REGISTRY_IP:PORT/IMAGE_PATH:IMAGE_TAG
    

### Pull an image from a registry mirror that uses namespaces

If your registry mirror uses namespaces, use the following command to pull an image:
    
    
    crictl pull REGISTRY_IP:PORT/NAMESPACE/IMAGE_PATH:IMAGE_TAG
    

### About the use of `v2` in the registry endpoint

When your registry uses custom namespaces, you must prepend the namespace in the registry endpoint (`registryMirror.endpoint`) in the cluster configuration file with `v2/`. If you aren't using namespaces, don't use `v2`. In either case, don't use `v2` in the `--private-registry` flag value or in image pull commands:

#### Without namespaces

  * Valid: 
    * `endpoint: https://172.18.0.20:5000`
    * `crictl pull 172.18.0.20:5000/anthos-baremetal-release/etcd:v3.4.30-0-gke.1`
  * Invalid: 
    * `endpoint: https://172.18.0.20:5000/v2`
    * `crictl pull 172.18.0.20:5000/v2/anthos-baremetal-release/etcd:v3.4.30-0-gke.1`



#### With namespaces

  * Valid: 
    * `endpoint: https://172.18.0.21:5000/v2/namespace`
    * `crictl 172.18.0.21:5000/namespace/anthos-baremetal-release/etcd:v3.4.30-0-gke.1`
  * Invalid: 
    * `endpoint: https://172.18.0.21:5000/namespace`
    * `crictl pull 172.18.0.21:5000/v2/namespace/anthos-baremetal-release/etcd:v3.4.30-0-gke.1`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
