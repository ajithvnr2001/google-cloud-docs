---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate/
title: Update vCenter CA certificate references \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:15.121738+00:00
---

# Update vCenter CA certificate references  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/update-vcenter-certificate/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Update vCenter CA certificate references Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/update-vcenter-certificate)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/update-vcenter-certificate)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes how to update the reference to the vCenter CA certificate if it has changed, as your running admin cluster and user clusters must be informed of the change. This affects the `vCenter.caCertPath` field in the admin cluster configuration file and the user cluster configuration files for Google Distributed Cloud.

You can update the certificate references with the `gkectl update` command as described here.

## Update the referenced vCenter CA certificate in the cluster configuration files

To update the running admin and user clusters to use the new certificate:

  1. Retrieve the new vCenter CA certificate and unzip it:
         
         curl -o certs.zip https://VCENTER_IP_ADDRESS/certs/download.zip
         unzip certs.zip
         

You can use the `-k` flag if you want to allow unknown certificates. This is to avoid any certificate issues you may have accessing vCenter.

  2. Save the Linux certificate to a file named `vcenter-ca.pem`.

  3. In your admin cluster configuration file, set [`vCenter.caCertPath`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#vcenter-cacertpath-field) to the path of your new `vcenter-ca.pem` file.

  4. Update your admin cluster:
         
         gkectl update admin --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

Replace:

     * ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.

After the update command completes, the admin cluster will use the new certificate.

  5. Verify that the admin cluster is healthy:
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         

For more information, see [Diagnose an admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#diagnose_admin_cluster).

  6. In each of your user cluster configuration files, set [`vCenter.caCertPath`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#vcenter-cacertpath-field) to the path of your new `vcenter-ca.pem` file.

  7. For each of your user clusters, run the `gkectl update` command: 
         
         gkectl update cluster --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG

Replace:

     * USER_CLUSTER_CONFIG with the path of your user cluster configuration file.

After the update command completes for a particular user cluster, the cluster will use the new certificate.

  8. Verify that the user cluster is healthy:
         
         gkectl diagnose cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --cluster-name USER_CLUSTER_NAME
         

For more information, see [Diagnose a user cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/diagnose#diagnose_user_cluster).


**Note:** The `vCenter.caCertPath` field also appears in the admin workstation configuration file. If you want to create a new admin workstation, make sure that you edit the `vCenter.caCertPath` field to reference the current certificate. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
