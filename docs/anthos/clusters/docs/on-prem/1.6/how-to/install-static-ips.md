---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-static-ips/
title: Creating an admin cluster \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:31.136571+00:00
---

# Creating an admin cluster  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-static-ips/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  Creating an admin cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create an admin cluster for Google Distributed Cloud.

The instructions here are complete. For a shorter introduction to creating an admin cluster, see [Create an admin cluster (quickstart)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-quickstart).

## Before you begin

[Create an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-admin-workstation).

## Get an SSH connection to your admin workstation

[Get an SSH connection](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-admin-workstation#getting_an_ssh_connection_to_your_admin_workstation) to your admin workstation.

Recall that `gkeadm` activated your component access service account on the admin workstation.

Do all the remaining steps in this topic on your admin workstation in the home directory.

## Credentials configuration file

When you used `gkeadm` to create your admin workstation, you filled in a credentials configuration file named `credential.yaml`. This file holds the username and password for your vCenter server.

## Admin cluster configuration file

When `gkeadm` created your admin workstation, it generated a configuration file named `admin-cluster.yaml`. This configuration file is for creating your admin cluster.

## Filling in your configuration file

### `bundlePath`

This field is already filled in for you.

### `vCenter`

Most of the fields in this are already filled in with values that you entered when you created your admin workstation. The exception is the [`dataDisk` field](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#vcenter-datadisk-field), which you must fill in now.

### `network`

Decide how you want your cluster nodes to get their IP addresses. The options are:

  * From a DHCP server. Set `network.ipMode.type` to `"dhcp"`.

  * From a list of static IP addresses that you provide. Set `network.ipMode.type` to `"static"`, and create an [IP block file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/ip-block-file) that provides the static IP addresses.




Provide values for the remaining fields in the [`network`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#network-section) section.

Regardless of whether you rely on a DHCP server or specify a list of static IP addresses, you need enough IP addresses to satisfy the following:

  * Three nodes in the admin cluster to run the admin cluster control plane and add-ons.

  * An additional node in the admin cluster to be used temporarily during upgrades.

  * For each user cluster that you intend to create, one or three nodes in the admin cluster to run the control-plane components for the user cluster. If you want the control plane for a user cluster to be highly available (HA), then you need three nodes in the admin cluster for the user cluster control plane. Otherwise, you need only one node in the admin cluster for the user cluster control plane.




For example, suppose you intend to create two user clusters: one with an HA control plane and one with a non-HA control plane. Then you would need eight IP addresses for the following nodes in the admin cluster:

  * Three nodes for the admin cluster control plane and add-ons
  * One temporary node
  * Three nodes for the HA user-cluster control plane
  * One node for the non-HA user-cluster control plane



As mentioned previously, if you want to use static IP addresses, then you need to provide an IP block file. Here is an example of an IP block file with eight hosts:
    
    
    blocks:
      - netmask: 255.255.252.0
        gateway: 172.16.23.254
        ips:
        - ip: 172.16.20.10
          hostname: admin-host1
        - ip: 172.16.20.11
          hostname: admin-host2
        - ip: 172.16.20.12
          hostname: admin-host3
        - ip: 172.16.20.13
          hostname: admin-host4
        - ip: 172.16.20.14
          hostname: admin-host5
        - ip: 172.16.20.15
          hostname: admin-host6
        - ip: 172.16.20.16
          hostname: admin-host7
        - ip: 172.16.20.17
          hostname: admin-host8

### `loadBalancer`

Set aside a VIP for the Kubernetes API server of your admin cluster. Set aside another VIP for the add-ons server. Provide your VIPs as values for [`loadBalancer.vips.controlPlaneVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#loadbalancer-controlplanevip-field) and [`loadBalancer.vips.addonsVIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#loadbalancer-addonsvip-field).

Decide what type of load balancing you want to use. The options are:

  * Seesaw bundled load balancing. Set `loadBalancer.kind` to `"Seesaw"`, and fill in the [`loadBalancer.seesaw`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#loadbalancer-seesaw-section) section.

  * Integrated load balancing with F5 BIG-IP. Set `loadBalancer.kind` to `"F5BigIP"`, and fill in the [`f5BigIP`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#loadbalancer-f5bigip-section) section.

  * Manual load balancing. Set `loadBalancer.kind` to `"ManualLB"`, and fill in the [`manualLB`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#loadbalancer-manuallb-section) section.




### `antiAffinityGroups`

Set [`antiAffinityGroups.enabled`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#antiaffinitygroups-enabled-field) to `true` or `false` according to your preference.

### `proxy`

If the network that will have your admin cluster nodes is behind a proxy server, fill in the [`proxy`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#proxy-section) section.

### `privateRegistry`

Decide where you want to keep container images for the Google Distributed Cloud components. The options are:

  * gcr.io. Do not fill in the `privateRegistry` section.

  * Your own private Docker registry. Fill in the [`privateRegistry`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#privateregistry-section) section.




## `gcrKeyPath`

Set `gcrKeyPath` to the path of the JSON key file for your [component access service account](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/service-accounts#component_access_service_account).

### `stackdriver`

Fill in the [`stackdriver`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#stackdriver-section) section.

### `cloudAuditLogging`

If you want Kubernetes audit logs to be integrated with Cloud Audit Logs, fill in the [`cloudAuditLogging`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#cloudauditlogging-section) section.

### `autoRepair`

If you want to enable [node auto repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/node-auto-repair), set `autoRepair.enabled` to `true`. Otherwise, set it to `false`.

### `adminMaster`

If you want to manually configure the CPUs and memory for the admin control-plane node, fill in the [`adminMaster`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-cluster-configuration-file#adminmaster-section) section.

## Validating your configuration file

After you've filled in your admin cluster configuration file, run `gkectl check-config` to verify that the file is valid:
    
    
    gkectl check-config --config [CONFIG_PATH]
    

where [CONFIG_PATH] is the path of your admin cluster configuration file.

If the command returns any failure messages, fix the issues and validate the file again.

If you want to skip the more time-consuming validations, pass the `--fast` flag. To skip individual validations, use the `--skip-validation-xxx` flags. To learn more about the `check-config` command, see [Running preflight checks](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/preflight-checks).

## Running `gkectl prepare`

Run `gkectl prepare` to initialize your vSphere environment:
    
    
    gkectl prepare --config [CONFIG_PATH]

The `gkectl prepare` command performs the following preparatory tasks:

  * Imports the OS images to vSphere and marks them as VM templates.

  * If you are using a private Docker registry, this command pushes the Docker container images to your registry.

  * Optionally, this command validates the container images' build attestations, thereby verifying the images were built and signed by Google and are ready for deployment.


**Note:** If you're using internal DNS names, or your workstation cannot access Google public DNS addresses (8.8.8.8 or 8.8.4.4), you must specify your internal nameserver in [`/etc/resolv.conf`](https://help.ubuntu.com/lts/serverguide/network-configuration.html.en#name-resolution).

## Creating a Seesaw load balancer for your admin cluster

If you have chosen to use the bundled Seesaw load balancer, do the step in this section. Otherwise, you can skip this section.

Create and configure the VMs for your [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/load-balance-basic#creating_ipblock_files):
    
    
    gkectl create loadbalancer --config [CONFIG_PATH]
    

## Creating the admin cluster

Create the admin cluster:
    
    
    gkectl create admin --config [CONFIG_PATH]

where [CONFIG_PATH] is the path of your admin cluster configuration file.

The `gkectl create admin` command creates a kubeconfig file named `kubeconfig` in the current directory. You will need this kubeconfig file later to interact with your admin cluster.

## Verifying that your admin cluster is running

Verify that your admin cluster is running:
    
    
    kubectl get nodes --kubeconfig [ADMIN_CLUSTER_KUBECONFIG]
    

where [ADMIN_CLUSTER_KUBECONFIG] is the path of your kubeconfig file.

The output shows the admin cluster nodes.

## Troubleshooting

### Diagnosing cluster issues using `gkectl`

Use `gkectl diagnose`commands to identify cluster issues and share cluster information with Google. See [Diagnosing cluster issues](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/diagnose). 

### Default logging behavior

For `gkectl` and `gkeadm` it is sufficient to use the default logging settings:

  * By default, log entries are saved as follows:

    * For `gkectl`, the default log file is `/home/ubuntu/.config/gke-on-prem/logs/gkectl-$(date).log`, and the file is symlinked with the `logs/gkectl-$(date).log` file in the local directory where you run `gkectl`. 
    * For `gkeadm`, the default log file is `logs/gkeadm-$(date).log` in the local directory where you run `gkeadm`. 
  * All log entries are saved in the log file, even if they are not printed in the terminal (when `--alsologtostderr` is `false`).
  * The `-v5` verbosity level (default) covers all the log entries needed by the support team.
  * The log file also contains the command executed and the failure message.



We recommend that you send the log file to the support team when you need help.

### Specifying a non-default location for the log file

To specify a non-default location for the `gkectl` log file, use the `--log_file` flag. The log file that you specify will not be symlinked with the local directory.

To specify a non-default location for the `gkeadm` log file, use the `--log_file` flag.

### Locating Cluster API logs in the admin cluster

If a VM fails to start after the admin control plane has started, you can try debugging this by inspecting the Cluster API controllers' logs in the admin cluster:

  1. Find the name of the Cluster API controllers Pod in the `kube-system` namespace, where [ADMIN_CLUSTER_KUBECONFIG] is the path to the admin cluster's kubeconfig file:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] -n kube-system get pods | grep clusterapi-controllers

  2. Open the Pod's logs, where [POD_NAME] is the name of the Pod. Optionally, use `grep` or a similar tool to search for errors:
         
         kubectl --kubeconfig [ADMIN_CLUSTER_KUBECONFIG] -n kube-system logs [POD_NAME] vsphere-controller-manager




### Debugging F5 BIG-IP issues using the admin cluster control plane node's kubeconfig

After an installation, Google Distributed Cloud generates a kubeconfig file in the home directory of your admin workstation named `internal-cluster-kubeconfig-debug`. This kubeconfig file is identical to your admin cluster's kubeconfig, except that it points directly at the admin cluster's control plane node, where the admin control plane runs. You can use the `internal-cluster-kubeconfig-debug` file to debug F5 BIG-IP issues.

### `gkectl check-config` validation fails: can't find F5 BIG-IP partitions

Symptoms
    

Validation fails because F5 BIG-IP partitions can't be found, even though they exist.

Potential causes
    

An issue with the F5 BIG-IP API can cause validation to fail.

Resolution
    

Try running `gkectl check-config` again.

### `gkectl prepare --validate-attestations` fails: could not validate build attestation

Symptoms
    

Running `gkectl prepare` with the optional `--validate-attestations` flag returns the following error:
    
    
    could not validate build attestation for gcr.io/gke-on-prem-release/.../...: VIOLATES_POLICY

Potential causes
    

An attestation might not exist for the affected image(s).

Resolution
    

Try downloading and deploying the admin workstation OVA again, as instructed in [Creating an admin workstation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation). If the issue persists, reach out to Google for assistance.

### Debugging using the bootstrap cluster's logs

During installation, Google Distributed Cloud creates a temporary bootstrap cluster. After a successful installation, Google Distributed Cloud deletes the bootstrap cluster, leaving you with your admin cluster and user cluster. Generally, you should have no reason to interact with this cluster.

If something goes wrong during an installation, and you did pass `--cleanup-external-cluster=false` to `gkectl create cluster`, you might find it useful to debug using the bootstrap cluster's logs. You can find the Pod, and then get its logs:
    
    
    kubectl --kubeconfig /home/ubuntu/.kube/kind-config-gkectl get pods -n kube-system
    
    
    kubectl --kubeconfig /home/ubuntu/.kube/kind-config-gkectl -n kube-system get logs [POD_NAME]

For more information, refer to [Troubleshooting](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/troubleshooting).

## What's next

[Creating a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/create-user-cluster)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
