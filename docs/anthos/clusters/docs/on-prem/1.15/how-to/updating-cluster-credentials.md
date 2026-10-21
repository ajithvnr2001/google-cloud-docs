---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials/
title: Updating cluster credentials \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:04.530298+00:00
---

# Updating cluster credentials  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/updating-cluster-credentials/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Updating cluster credentials Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/updating-cluster-credentials)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/updating-cluster-credentials)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page shows how to update the vCenter and F5 BIG-IP credentials for the admin cluster or a user cluster for Google Distributed Cloud.

## Update vSphere credentials

The vCenter credentials that you want to add to a cluster must already exist. [Learn about vCenter roles and user privileges](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.security.doc/GUID-18071E9A-EED1-4968-8D51-E0B4F526FDA3.html).

The admin cluster and each user cluster are initially configured to use the [vCenter username and password](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) that you used to create those clusters. The [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#vcenter-credentials-fileref-path-field) contains a reference to a credentials file, as does each [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file#vcenter-credentials-fileref-path-field). These references can be different for each cluster.

Use the following steps to update the vCenter credentials on a cluster:

  1. In the admin workstation, open your [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file) in an editor.

Update the `username` and `password` attributes in the credentials configuration file.

  2. Run the `gkectl update credentials vsphere` command to deploy the changes to a cluster:
         
         gkectl update credentials vsphere \
           --config CLUSTER_CONFIG \
           --kubeconfig CLUSTER_KUBECONFIG \
           --admin-cluster

Replace the following:

     * CLUSTER_CONFIG: Specifies the [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file) or the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/user-cluster-configuration-file), depending on which cluster you are updating.That cluster configuration file includes a reference to the vCenter credentials that you want to deploy to your cluster. 
     * ADMIN_CLUSTER_KUBECONFIG: Specifies the [`kubeconfig`](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-admin-cluster#create-admin-cluster) file of the admin cluster. Example: `kubeconfig`

For updating credentials for the admin cluster, you must also include the `--admin-cluster` flag.

     * `--admin-cluster`: Required flag if you are deploying changes to the admin cluster. Exclude this flag when deploying changes to a user cluster.

Result: The changed vCenter credentials are immediately validated against the server and a confirmation is output to the terminal: "`vsphere credentials updated successfully`". If the new credentials fail to log in to the vCenter server, you can edit the `username` and `password` in the credentials file and redeploy your changes.

**Examples:**

     * User cluster example:
           
           gkectl update credentials vsphere \
           --config USER_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG

If successful, the result output indicates that the vSphere credentials have updated successfully.

     * Admin cluster example:
           
           gkectl update credentials vsphere \
           --config ADMIN_CLUSTER_CONFIG --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
           --admin-cluster

Result:
           
           validating new credentials against vcenter
           restarted "deployment/clusterapi-controllers" in namespace "kube-system"
           vsphere credentials updated successfully.




## Update F5 BIG-IP credentials for an admin cluster or a user cluster

Update the F5 BIG-IP credentials in the F5 web interface.

On your admin workstation, use the following steps to update the F5 BIG-IP credentials for an admin cluster or a user cluster.

  1. Edit your F5 credentials file to change the credentials.

  2. Update the F5 BIG-IP credentials for your cluster:
         
         gkectl update credentials f5bigip --config CLUSTER_CONFIG \
            --kubeconfig ADMIN_CLUSTER_KUBECONFIG --admin-cluster
         


**Note:** The user cluster configuration file and the admin cluster configuration file reference the path to this credentials file. If you want to change the path of the credentials, update the corresponding cluster configuration file to change the file reference. Run the appropriate `gkectl update admin` or `gkectl update cluster` command to update this reference.

## Update private registry credentials for an admin cluster or a user cluster (_Preview_)

You can update the private registry credentials and certificate (server update is **not** supported) for a cluster. As you do the update, both the current and new credentials must be able to connect to the private registry.

**Note:** If your cluster is currently using Container Registry, you cannot update the cluster to use a private registry.

On your admin workstation, use the following steps to update the private registry credentials for an admin cluster or a user cluster.

  1. Update your private registry credentials in the [credentials configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/credentials-configuration-file).

  2. Update the cluster to use the new private registry credentials:

Admin cluster:
         
         gkectl update credentials privateregistry --config CLUSTER_CONFIG \
            --kubeconfig ADMIN_CLUSTER_KUBECONFIG --admin-cluster
         

User cluster:
         
         gkectl update credentials privateregistry --config CLUSTER_CONFIG \
            --kubeconfig ADMIN_CLUSTER_KUBECONFIG
         




## Update other credentials

To update keys for your Identity and Access Management [service accounts](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts), see [Rotate service account keys](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
