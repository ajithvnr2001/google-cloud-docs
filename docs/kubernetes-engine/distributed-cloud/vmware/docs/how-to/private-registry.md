---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry/
title: Configure a private container registry \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:40.676468+00:00
---

# Configure a private container registry  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/private-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure a private container registry Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure an existing container registry server for Google Distributed Cloud (software only) for VMware.

This page is for Admins, Architects, and Operators who set up, monitor, and manage the tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

By default during cluster creation or upgrade, Google Distributed Cloud pulls system images from `gcr.io/gke-on-prem-release` using the [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account). Optionally, you can provide your own container registry server so that system images are pulled from your private registry server instead.

Google Distributed Cloud doesn't support unsecured container registries. When you start your container registry server, you must provide a certificate and a key. The certificate can be signed by a public certificate authority (CA), or it can be self-signed.

## Create a container registry server

To learn how to create a container registry server, see [Run an externally-accessible registry](https://docs.docker.com/registry/deploying/#run-an-externally-accessible-registry) in the Docker documentation.

## Configure the registry

To use a private container registry, you can use either the `gkectl` command-line tool or Terraform.

### `gkectl`

  1. Add the [`privateRegistry`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section) section to the admin cluster configuration file before creating the cluster.

When this section is filled in:

     * When you run the `gkectl prepare` command before cluster creation or upgrade, the command extracts the images from the tar file that is specified in the [`bundlePath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#bundlepath-field) field in your admin cluster configuration file and pushes the images to your private registry server.

     * During cluster creation or upgrade, the system images are pulled from your private registry server.

  2. If your network is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#proxy-section) section.




### Terraform

  1. Follow the steps in the Terraform tab in [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) to fill in your admin cluster configuration file.



  1. Add the following to the admin cluster configuration file:
         
         private_registry_config {
           address = "ADDRESS"
           ca_cert = "CA_CERT"
         }
         

Replace the following:

     * `ADDRESS`: the IP address or FQDN (Fully Qualified Domain Name) of the machine that runs your private registry.

     * `CA_CERT`: the CA certificate data of the public key but with all the newlines replaced with the string `\n`.

     1. Run the following command to replace newlines with `\n`:
            
            awk 'ORS="\\n" {print}' PUBLIC_KEY_PATH
            

Replace `PUBLIC_KEY_PATH` with the path to the public key.

     2. Copy the output of the previous command and paste it into the `CA_CERT` placeholder variable.

  2. If your network is behind a proxy server, add the following:
         
         proxy {
           url: "PROXY_SERVER_ADDRESS"
           no_proxy: "BYPASS_LIST"
         }
         

Replace the following:

     * `PROXY_SERVER_ADDRESS`: the HTTP address of your proxy server. Include the port number even if it's the same as the scheme's default port.

     * `BYPASS_LIST`: a comma-separated list of IP addresses, IP address ranges, host names, and domain names that shouldn't go through the proxy server.

Example:
    
    url: "http://my-proxy.example.local:80"
    no_proxy: "192.0.2.0/24,my-host.example.local,198.51.100.0"
    

When Google Distributed Cloud sends a request to one of these addresses, hosts, or domains, the request bypasses the proxy server and is sent directly to the destination.



  1. Continue with the steps in the Terraform tab in [Create an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster) to verify the Terraform configuration file and plan and then create the bootstrap cluster.

  2. When you run the `gkectl register bootstrap` command, `gkectl` prompts you to enter the username and then the password for the private registry.




During cluster creation, the system images are pulled from your private registry server.

### Limitations with advanced clusters and the full bundle

There are two Google Distributed Cloud bundles available: full and regular. To determine which bundle is on your admin workstation, check the `bundlePath` field in your admin cluster configuration file. If the filename ends in `-full`, the full bundle is on your admin workstation. If the filename doesn't end in `-full`, the regular bundle is on your admin workstation.

If you created your admin workstation using the `gkeadm` command, the command creates the admin workstation VM with the full bundle on it, and configures the `bundlePath` field in the admin cluster configuration file.

If [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enable-advanced-cluster-field) is enabled, there are limitations with using the full bundle with a private registry, as follows:

  * Version 1.31: the full bundle isn't supported with a private registry. To use a private registry on an advanced cluster:

    1. [Download](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#bundle) the regular size bundle to your admin workstation.
    2. Update the filename in the `bundlePath` field in the admin cluster configuration file.
  * Version 1.32: using the full bundle is supported, but the `gkectl prepare` command pulls images from `gcr.io/gke-on-prem-release` instead of the tar file. The command does, however, push the images to your private registry so that the system images are pulled from your private registry during cluster creation or upgrade.




### Differences between normal clusters and advanced clusters

Advanced cluster introduces several key differences compared to standard clusters:

  * When you use a private registry, images appear to pull from `gcr.io`, not the hostname of your private registry. This change is expected, even though images actually pull from your private registry server.
  * Image pulls use credentials from the `/etc/containerd/config.toml` file in each machine that connects to the private registry, instead of from the `private-registry-creds` secret inside the cluster.
  * For all `gcr.io` images, the cluster first tries to pull from the private registry. If the image isn't in the private registry, the system pulls it from `gcr.io` over the internet. To stop this fallback, set up [`noProxy`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#proxy-noproxy-field) or use firewall rules to block `gcr.io` traffic.



To check that images pull from the correct source, see Verify images are pulled from your registry server.

## Verify images are pulled from your registry server

How you verify that images are being pulled from your registry server depends on whether advanced cluster is enabled.

  * If advanced cluster isn't enabled, run the following command:
        
        kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get pods \
            --all-namespaces -o jsonpath="{.items[*].spec['initContainers', 'containers'][*].image}"
        

Replace `ADMIN_CLUSTER_KUBECONFIG` with the path of the kubeconfig file for your admin cluster.

The output of this command displays all the images in your cluster. You can verify that all the Google Distributed Cloud images are from your own registry server.

  * If advanced cluster is enabled, do the following steps:

You can determine whether `containerd` is pulling images from your local registry by examining the contents of a file called `config.toml` as shown in the following steps:

    1. Log into a node and examine the contents of the file `/etc/containerd/config.toml`.
    2. Check the `plugins."io.containerd.grpc.v1.cri".registry.mirrors` field of the `config.toml` file to see whether your registry server is listed in the `endpoint` field.

The following is an excerpt from an example `config.toml` file.
           
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
           endpoint = ["http://privateregistry.io", "http://privateregistry2.io"]
           ...
           

    3. If your registry mirror appears in the `endpoint` field, then the node is pulling images from your registry mirror rather than from Artifact Registry.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
