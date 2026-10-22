---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys/
title: Rotating service account keys \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:27.220960+00:00
---

# Rotating service account keys  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/rotating-service-account-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Rotating service account keys Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to rotate keys for the following service accounts:

  * [Component access](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account)
  * [Connect-register](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account)
  * [Logging-monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account)
  * [Audit logging](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account)

**Important:** The capabilities described in this document aren't fully supported for 1.31 or 1.32 clusters that have advanced clusters enabled. For details about what is or isn't supported for updating credentials for advanced clusters, see Advanced cluster differences for rotating service account keys. For a comprehensive list of Google Distributed Cloud for VMware features and capabilities that are or aren't supported for advanced clusters, see [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support).

To rotate your service account keys:

  1. Create a directory to store a backup of your current secrets:
         
         mkdir backup

  2. Note the following information for the relevant service account:

**Component access**

Cluster | Secret | Namespace  
---|---|---  
Admin | admin-cluster-creds | kube-system  
Admin | user-cluster-creds | CLUSTER_NAME-gke-onprem-mgmt  
Admin | private-registry-creds | kube-system  
User | private-registry-creds | kube-system  
     * If you aren't using a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-section), the `private-registry-creds` Secret holds the key for your component access service account.
     * If you are using a private registry, the `private-registry-creds` Secret holds the credentials for your private registry, **not** the component access service account key.

**Connect-register**

Cluster | Secret | Namespace  
---|---|---  
Admin | admin-cluster-creds | kube-system  
Admin | user-cluster-creds | CLUSTER_NAME-gke-onprem-mgmt  
  
**Logging-monitoring**

Cluster | Secret | Namespace  
---|---|---  
Admin | admin-cluster-creds | kube-system  
Admin | user-cluster-creds | CLUSTER_NAME-gke-onprem-mgmt  
User | google-cloud-credentials | kube-system  
User | stackdriver-service-account-key | knative-serving  
  
**Audit logging**

Cluster | Secret | Namespace  
---|---|---  
Admin | admin-cluster-creds | kube-system  
Admin | user-cluster-creds | CLUSTER_NAME-gke-onprem-mgmt  
Admin | kube-apiserver | CLUSTER_NAME  
  
**Stackdriver**

Cluster | Secret | Namespace  
---|---|---  
Admin | admin-cluster-creds | kube-system  
Admin | user-cluster-creds | CLUSTER_NAME-gke-onprem-mgmt  
User | google-cloud-credentials | kube-system  
User | stackdriver-service-account-key | knative-serving  
  3. Create a backup of each secret using the following command:
         
         kubectl get secret SECRET --namespace NAMESPACE \
             --kubeconfig KUBECONFIG -o json > backup/SECRET-NAMESPACE.json

Replace the following:

     * `NAMESPACE`: the namespace where the secret is located. For example, `kube-system`.
     * `KUBECONFIG`: the path to the kubeconfig file for the admin or user cluster.
     * `SECRET`: the name of the secret. For example, `admin-cluster-creds`.

For example, run the following commands for the audit logging service account:
    
    kubectl get secret admin-cluster-creds --namespace kube-system \
            --kubeconfig KUBECONFIG -o json > backup/admin-cluster-creds-kube-system.json
    
    kubectl get secret user-cluster-creds --namespace NAMESPACE \
            --kubeconfig KUBECONFIG -o json > backup/user-cluster-creds-NAMESPACE.json
    
    kubectl get secret kube-apiserver --namespace NAMESPACE \
            --kubeconfig KUBECONFIG -o json > backup/kube-apiserver-NAMESPACE.json

  4. To create a new service account key file, run the following command:
         
         gcloud iam service-accounts keys create NEW_KEY_FILE --iam-account IAM_ACCOUNT

Replace the following:

     * `NEW_KEY_FILE`: the name for your new service account key file
     * `IAM_ACCOUNT`: the email address of the service account
  5. In the admin cluster configuration file, find the `componentAccessServiceAccountKeyPath` field, the `gkeConnect` section, the `stackdriver` section, and the `cloudAuditLogging` section. In those places, replace the paths to the service account key files.

  6. In the user cluster configuration file, find the `componentAccessServiceAccountKeyPath` field, the `gkeConnect` section, the `stackdriver` section, and the `cloudAudigLogging` section. In those places, replace the paths to the service account key files.

  7. Save the changes you made by running the following commands:

You can rotate the keys for one component at a time, or you can rotate all keys at once by setting the component to `sakeys`.
         
         gkectl update credentials COMPONENT \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG \
             --admin-cluster
         
         gkectl update credentials COMPONENT \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following;

     * `COMPONENT`: one of:

       * `componentaccess`
       * `register`
       * `cloudauditlogging`
       * `stackdriver`
       * `sakeys` (rotates all component keys)
     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the kubeconfig file for the admin cluster.

     * `ADMIN_CLUSTER_CONFIG`: the path to the admin cluster configuration file.

     * `USER_CLUSTER_CONFIG`: the path to the user cluster configuration file.




## Node re-creation

Some service account key rotations may take longer time because node re-creation is required:

**Service account** | **Nodes re-creation required**  
---|---  
Component access | If using Artifact Registry: Yes  
If using a private registry: No  
Audit logging | Admin cluster: Yes but only control-plane nodes  
User cluster using kubeception: No   
User cluster using Controlplane V2: Yes but only control plane nodes  
Logging-monitoring | No  
Connect-register | No  
  
For a key rotation that requires nodes to be re-created, the nodes are replaced in a rolling update process; that is, the nodes are re-created one by one.

The possible downtime during a key rotation is similar to the downtime for a cluster upgrade. For details, see [Downtime during upgrades](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/upgrading#downtime_upgrades).

## Restoring backups

If you need to restore the backups of the secrets you made earlier, run the following command:
    
    
    kubectl apply -f backup/
    

## Advanced cluster differences for rotating service account keys

The `gkectl update credentials` command is only partially supported for advanced clusters. The following table lists command variations that are and aren't supported:

Command | Description | Support  
---|---|---  
`gkectl update credentials certificate-authorities rotate` | Rotate certificate authorities. | Supported  
`gkectl update credentials certificate-authorities status` | ([Preview](https://cloud.google.com/products/#product-launch-stages)) View certificate authorities rotation status. | Supported  
`gkectl update credentials certificate-authorities update-kubeconfig` | Download a kubeconfig file with latest client certificate. | Supported  
`gkectl update credentials cloudauditlogging` | Update Cloud Audit Logs credentials. | Not Supported  
`gkectl update credentials componentaccess` | Update the component access service account key credentials for clusters created with Google Distributed Cloud for VMware. | Supported  
`gkectl update credentials f5bigip` | Update F5 BIG-IP load balancer credentials. | Not Needed  
`gkectl update credentials ksa-signing-key rotate` | Rotate the Kubernetes service account (KSA) token signing key. | Not Supported  
`gkectl update credentials ksa-signing-key status` | View the status of an ongoing KSA token signing key rotation. | Not Supported  
`gkectl update credentials` | Update cluster credentials. | Supported  
`gkectl update credentials privateregistry` | Update private registry credentials for a cluster. | Supported  
`gkectl update credentials register` | Update register service account key credentials. | Supported  
`gkectl update credentials sakeys` | Update service account keys credentials for a cluster. | Supported  
`gkectl update credentials stackdriver` | ([Preview](https://cloud.google.com/products/#product-launch-stages)) Update Google Cloud Observability credentials. | Supported  
`gkectl update credentials vsphere` | Update vSphere credentials for a cluster. | Supported  
  
For a comprehensive list of Google Distributed Cloud for VMware features and capabilities that are or aren't supported for advanced clusters, see [Differences when running advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters#adv-clusters-feature-support).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
