---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate/
title: Update vCenter CA certificate references \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:47.557912+00:00
---

# Update vCenter CA certificate references  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/update-vcenter-certificate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Update vCenter CA certificate references Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to update the reference to the vCenter CA certificate if it has changed, as your running admin cluster and user clusters must be informed of the change. This affects the `vCenter.caCertPath` field in the admin cluster configuration file and the user cluster configuration files for Google Distributed Cloud.

You can update the certificate references with the `gkectl update` command as described here.

## Update the referenced vCenter CA certificate in the cluster configuration files

To update the running admin and user clusters to use the new certificate:

  1. Retrieve the new vCenter CA certificate and extract it:
         
         curl -o certs.zip https://VCENTER_IP_ADDRESS_OR_FQDN/certs/download.zip
         unzip certs.zip
         

You can use the `-k` flag if you want to allow unknown certificates. This is to avoid any certificate issues you may have accessing vCenter.

  2. Determine which of the vCenter certificates is valid. Only one of the Linux certificate files in the extracted `..../certs/lin` folder is the valid vCenter certificate. To determine which file is the valid vCenter certificate, do the following:

     1. Set the following environment variables from the Admin Workstation where `govc` is already installed. If not already done, [download and install govc tool](https://github.com/vmware/govmomi/tree/main/govc#binaries): 
            
            export GOVC_URL=https://VCENTER_IP_ADDRESS_OR_FQDN
            export GOVC_USERNAME=VCENTER_USERNAME
            export GOVC_PASSWORD=VCENTER_PASSWORD
            export GOVC_TLS_CA_CERTS=FULL_PATH_OF_EXTRACTED_LIN_FILE
            export GOVC_INSECURE=false
            

Replace the following:

        * `VCENTER_IP_ADDRESS_OR_FQDN`: the IP address or FQDN of the vCenter Server.

        * `VCENTER_USERNAME`: the username of the vCenter Server.

        * `VCENTER_PASSWORD`: the password for the specified username.

        * `FULL_PATH_OF_EXTRACTED_LIN_FILE`: the full path to the Linux certificate file for which you are conducting a validity test.

     2. To verify that the vCenter certificate is valid, run the `govc about` command:
            
            govc about
            

If the vCenter certificate is valid, the `govc about` command prints details about the vCenter Server similar to the following:
            
            FullName: VMware Center Server 7.0.3 build-24322018
            Name: VMware Center Server
            Vendor: VMware, Inc.
            Version: 7.0.3
            Build: 24322018
            OS type: linux-x64
            API type: VirtualCenter
            API version: 7.0.3.0
            Product ID: vpx
            UUID: 475fa366-faa9-43f0-9417-e6dadc55514c
            

If the certificate is invalid, you should see an `x509` error. If you see an `x509` error, update the `FULL_PATH_OF_EXTRACTED_LIN_FILE` environment variable to point at a different Linux certificate file in the extracted `..../certs/lin` folder, and then run the `govc about` command again. Repeat steps a. and b. until you locate the valid certificate, or until you are done testing each of the Linux certificate files in the extracted `..../certs/lin` folder.

  3. To backup the old vCenter CA certificate file (which is at the path specified in the [`vCenter.caCertPath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-cacertpath-field) field of your admin cluster configuration file), rename it to `vcenter-ca-cert.pem.old`.

  4. Rename the new valid certificate file in the `..../certs/lin` folder to `vcenter-ca-cert.pem` and then move it to the path specified in the [`vCenter.caCertPath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#vcenter-cacertpath-field) field of your admin cluster configuration file.

  5. If you created your admin workstation with `gkeadm`, make sure that the [`vCenter.caCertPath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file#vcentercacertpath) in the admin workstation configuration file has the same path as the admin cluster configuration file.




If Controlplane V2 is enabled on your user clusters, which is required for version 1.32 and higher, update your user clusters first and then the admin cluster. For user clusters that don't have Controlplane V2 enabled (referred to as kubception), update the admin cluster first and then the user clusters.

### Controlplane V2

  1. In each of your user cluster configuration files, set [`vCenter.caCertPath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-cacertpath-field) to the path of your new `vcenter-ca-cert.pem` file.

  2. For each of your user clusters, run the `gkectl update` command:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace the following:

     * `USER_CLUSTER_CONFIG`: the path of your user cluster configuration file.
     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the admin cluster's kubeconfig file.

After the update command completes for a particular user cluster, the cluster will use the new certificate.

  3. Verify that the user cluster is healthy:
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --cluster-name USER_CLUSTER_NAME
         

For more information, see [Diagnose a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster).

  4. Update your admin cluster:
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_CONFIG`: the path of your admin cluster configuration file.

After the update command completes, the admin cluster will use the new certificate.

  5. Verify that the admin cluster is healthy:
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

For more information, see [Diagnose an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster).




### Kubception

  1. Update your admin cluster:
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace the following:

     * `ADMIN_CLUSTER_CONFIG`: the path of your admin cluster configuration file.

After the update command completes, the admin cluster will use the new certificate.

  2. Verify that the admin cluster is healthy:
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

For more information, see [Diagnose an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_admin_cluster).

  3. In each of your user cluster configuration files, set [`vCenter.caCertPath`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#vcenter-cacertpath-field) to the path of your new `vcenter-ca-cert.pem` file.

  4. For each of your user clusters, run the `gkectl update` command:
         
         gkectl update cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace the following:

     * `USER_CLUSTER_CONFIG`: the path of your user cluster configuration file.

After the update command completes for a particular user cluster, the cluster will use the new certificate.

  5. Verify that the user cluster is healthy:
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --cluster-name USER_CLUSTER_NAME
         

For more information, see [Diagnose a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose#diagnose_user_cluster).




**Note:** The `vCenter.caCertPath` field also appears in the admin workstation configuration file. If you want to create a new admin workstation, make sure that you edit the `vCenter.caCertPath` field to reference the current certificate.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
