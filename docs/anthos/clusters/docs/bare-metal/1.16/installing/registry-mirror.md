---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/registry-mirror/
title: Use a registry mirror to create clusters \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:13.199954+00:00
---

# Use a registry mirror to create clusters  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/registry-mirror/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Use a registry mirror to create clusters Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/installing/registry-mirror)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/registry-mirror)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page explains how to create clusters using images pulled from a registry mirror rather than from a public registry, such as `gcr.io`.

A registry mirror is a local copy of a public registry that copies or mirrors the file structure of the public registry. For example, let's say that the path to your local registry mirror is `172.18.0.20:5000`. When `containerd` encounters a request to pull an image such as `gcr.io/kubernetes-e2e-test-images/nautilus:1.0`, `containerd` attempts to pull that image, not from `gcr.io`, but from your local registry at the following path: `172.18.0.20:5000/kubernetes-e2e-test-images/nautilus:1.0`. If the image isn't in this local registry path, the image is pulled automatically from the public registry `gcr.io`.

Using a registry mirror provides the following benefits:

  * Protects you from public registry outages.
  * Speeds up pod creation.
  * Allows you to conduct your own vulnerability scanning.
  * Avoids limits imposed by public registries on how frequently you can issue commands to them.



## Before you begin

  * You must have a container registry server set up in your network.
  * If your registry server runs a private TLS certificate, you must have the certificate authority (CA) file.
  * If your registry server needs authentication, you must have the proper login credentials or Docker configuration file.
  * To use a registry mirror, you must set the container runtime to [containerd](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/installing/runtime).



## Download all required images for Google Distributed Cloud

Download the latest version of the `bmctl` tool and images package from the [Downloads](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads) page.

## Upload container images to your registry server

Upload the images from the images package to your registry server by running:
    
    
    [HTTPS_PROXY=http://PROXY_IP:PORT] ./bmctl push images \
        --source=./bmpackages_VERSION.tar.xz \
        --private-registry=REGISTRY_IP:PORT \
        [--cacert=CERT_PATH] \
        [--need-credential=false]
    

Replace the following:

  * `PROXY_IP:PORT` with the IP address and port of the proxy if you need a proxy to upload the images from your workstation to the registry server.
  * `VERSION` with the version of the images package you downloaded from the [Downloads](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/downloads) page.
  * `REGISTRY_IP:PORT` with the IP address and port of the private registry server.
  * `CERT_PATH` with the path of the CA cert file if your registry server uses a private TLS certificate.



Enter your username and password when prompted or select a Docker configuration file. If your registry server doesn't require credentials, then specify `--need-credential=false`.

For more information on the `bmctl push images` command, run:
    
    
    bmctl push images --help
    

### Use your own namespace

If you want to use your own namespace in your registry server instead of the root namespace, `containerd` can pull from this namespace if you provide the API endpoint for your private registry in `registryMirrors.endpoint`. The endpoint is usually in the format of `<REGISTRY_IP:PORT>/v2/<NAMESPACE>`. Check your private registry's user guide for specific details.

For example, if you only have access to `172.18.0.20:5000/test-namespace/`, you can use the following command to upload all the images under namespace `test-namespace`:
    
    
    ./bmctl push images \
        --source=./bmpackages_VERSION.tar.xz \
        --private-registry=172.18.0.20:5000/test-namespace
        --username=<USERNAME>
        --password=<PASSWORD>
        --cacert <path/to/cert.crt>
    

Then in the cluster configuration file, you can add the following to make `containerd` pull from the namespace:
    
    
    registryMirrors:
      - endpoint: https://172.18.0.20:5000/v2/test-namespace
    

## Create clusters from the registry mirror

The following sample cluster configuration file specifies that images are to be pulled from a local registry mirror whose endpoint is `https://172.18.0.20:5000`. Some of the fields appearing at the beginning of this configuration file are described in the following sections.
    
    
    # Sample cluster config with registry mirror:
    ---
    gcrKeyPath: /bmctl/bmctl-workspace/.sa-keys/my-gcp-project-anthos-baremetal-gcr.json
    sshPrivateKeyPath: /root/ssh-key/id_rsa
    registryMirrors:
      - endpoint: https://172.18.0.20:5000
        caCertPath: /root/ca.crt
        pullCredentialConfigPath: /root/.docker/config.json
        hosts:
          - somehost.io
          - otherhost.io
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
    

### `hosts` field

`containerd` checks the `hosts` section of the cluster configuration file to discover which hosts are mirrored locally. In the example configuration file, the public registries listed in the `hosts` section are `somehost.io` and `otherhost.io`. Because these public registries appear in the `hosts` section, `containerd` checks the private registry mirror first when it encounters pull requests for images from `somehost.io` or `otherhost.io`.

For example, let's say `containerd` receives a pull command to `somehost.io/kubernetes-e2e-test-images/nautilus:1.0`. Because `somehost.io` is listed as one of the hosts in the `hosts` section of the cluster configuration file, `containerd` looks in the local registry mirror for the `kubernetes-e2e-test-images/nautilus:1.0` image. If `somehost.io` isn't listed in the `hosts` section, `containerd` doesn't know that a local mirror of `somehost.io` exists. In that case, `containerd` doesn't check the mirror for the image, and it simply pulls the image from the `somehost.io` public registry.

Note that by default, Google Distributed Cloud automatically mirrors images from `gcr.io` so you don't need to list `gcr.io` as a host in the `hosts` section.

### `gcrKeyPath` field

If you want Google Distributed Cloud to automatically use Container Registry (`gcr.io`) to pull images that don't appear in your local registry, you must specify the path to the Container Registry service account key. Google Distributed Cloud doesn't have a mechanism for providing keys for other public registries.

If you don't plan on using the feature in which images are pulled from `gcr.io` when they don't appear in your local registry, then you don't need to add a `gcrKeyPath` to the cluster configuration file.

### `caCertPath` field

If your registry requires a private transport layer security (TLS) certificate, this field takes the path to the server root CA certificate file. This certificate file should be on the admin workstation, the machine running `bmctl` commands. If your registry doesn't require a private TLS certificate, then you can leave the `caCertPath` field blank.

### `pullCredentialConfigPath` field

If your registry server doesn't require an authentication Docker configuration file, then you can leave the `pullCredentialConfigPath` field blank. Note that this is the path to the configuration file on the machine running `bmctl` commands.

## Create user cluster from the registry mirror

User clusters don't automatically pull images from a registry mirror if their admin cluster has been configured to do so. To have user clusters pull from a registry mirror, you need to configure them individually as described in Create clusters from the registry mirror.

## Update registry mirror endpoints, certificates, and pull credentials

To update registry mirror endpoints, certificates, or pull credentials:

  1. In the cluster configuration file, update the endpoint, CA certificate file, and pull credential configuration file path.

  2. Apply the changes by running:
         
         bmctl update cluster -c CLUSTER_NAME --kubeconfig=ADMIN_KUBECONFIG
         

Replace the following:

     * CLUSTER_NAME with the name of the cluster you want to update.
     * ADMIN_KUBECONFIG with the path of its admin cluster's configuration file.



## Verify images are pulled from registry mirror

This section describes two methods you can use to verify whether `containerd` is pulling images from your local registry mirror rather than from a public registry.

### Method #1: compare repository digests

This method involves comparing repository digests to determine whether an image has been pulled from your registry mirror.

Keep in mind that a registry has a unique identifier called the repository digest, and an image has a unique identifier called the container image digest. Two images that are identical have the same container image digest, even if the images come from different registries. However, if images come from different registries, they have different repository digests.

  1. Log into a cluster node using SSH.

  2. Choose an image whose origin you want to verify.

  3. Pull the image from the public registry you use by running the following command:
         
         crictl pull PUBLIC_ENDPOINT
         

Replace `PUBLIC_ENDPOINT` with the image's path in the public registry. For example: `gcr.io/anthos-baremetal-release/kube-rbac-proxy:v0.6.0-gke.0`.

  4. Pull the same image from your registry mirror by running the following command:
         
         crictl pull MIRROR_ENDPOINT
         

Replace `MIRROR_ENDPOINT` with the image's path in your registry mirror. For example: `10.168.15.224:5007/test-namespace/anthos-baremetal-release/kube-rbac-proxy:v0.6.0-gke.0`.

  5. Run the following command to display the repository digests of the two images you pulled in the previous steps:
         
         crictl inspecti PUBLIC_OR_MIRROR_ENDPOINT | grep -A 3 repoDigests
         

Replace `PUBLIC_OR_MIRROR_ENDPOINT` with either the image's public endpoint or the image's registry mirror endpoint. Either one is fine because the `crictl inspecti` command looks at the container image digest of the argument you pass to it. Since the image from the public registry is identical to the image from the registry mirror, they both have the same container image digest.

Output from the command might look like this:
         
         "repoDigests": [
            "gcr.io/anthos-baremetal-release/kube-rbac-proxy@sha256:**27be66fb9140d83c4af8794a234b998c90e844e3414108ce72db603f4f6ea0b3"** ,
            "10.168.15.224:5007/test-namespace/anthos-baremetal-release/kube-rbac-proxy@sha256:**27be66fb9140d83c4af8794a234b998c90e844e3414108ce72db603f4f6ea0b3** "
          ],
         

  6. Compare the repository digests that appear in bold in the output from the preceding step. If the digests are identical, then the nodes in your cluster are pulling from your registry mirror. Otherwise, your cluster nodes are pulling images from a public registry.




### Method #2: examine `config.toml` file

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
          **endpoint = ["http://privateregistry.io", "http://privateregistry2.io"]**
    ...
    

If your registry mirror appears in the `endpoint` field, then the node is pulling images from your registry mirror rather than from a public registry.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
