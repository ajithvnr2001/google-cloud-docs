---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys/
title: Rotating service account keys \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:04.109502+00:00
---

# Rotating service account keys  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/rotating-service-account-keys/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Rotating service account keys Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/rotating-service-account-keys)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/rotating-service-account-keys)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page describes how to rotate keys for the following service accounts:

  * [Component access](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#component_access_service_account)
  * [Connect-register](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#connect_register_service_account)
  * [Logging-monitoring](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#logging_monitoring_service_account)
  * [Audit logging](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#audit_logging_service_account)
  * [Usage metering](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/service-accounts#usage_metering_service_account)



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
     * If you are not using a [private registry](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/admin-cluster-configuration-file#privateregistry-section), the `private-registry-creds` Secret holds the key for your component access service account.
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
  
**Usage Metering**

Cluster | Secret | Namespace  
---|---|---  
Admin | user-cluster-creds | CLUSTER_NAME-gke-onprem-mgmt  
User | usage-metering-bigquery-service-account-key | kube-system  
  
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

  6. In the user cluster configuration file, find the `componentAccessServiceAccountKeyPath` field, the `gkeConnect` section, the `stackdriver` section, the `cloudAudigLogging` section, and the `usageMetering` section. In those places, replace the paths to the service account key files.

  7. Save the changes you made using the following commands:
         
         gkectl update credentials COMPONENT \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config ADMIN_CLUSTER_CONFIG \
             --admin-cluster
         
         gkectl update credentials COMPONENT \
             --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
             --config USER_CLUSTER_CONFIG
         

Replace the following;

     * `COMPONENT`: one of `componentaccess`, `register`, `cloudauditlogging`, `usagemetering`, or `stackdriver`.

     * `ADMIN_CLUSTER_KUBECONFIG`: the path to the kubeconfig file for the admin cluster.

     * `ADMIN_CLUSTER_CONFIG`: the path to the admin cluster configuration file.

     * `USER_CLUSTER_CONFIG`: the path to the user cluster configuration file.




## Node re-creation

Some service account key rotations may take longer time because node re-creation is required:

**Service account** | **Nodes re-creation required**  
---|---  
Component access | If using Container Registry: Yes  
If using a private registry: No  
Audit logging | Admin cluster: Yes  
User cluster with Contrlplane V2 enabled: Yes but only control plane nodes  
Logging-monitoring | No  
Connect-register | No  
Usage metering | No  
  
## Restoring backups

If you need to restore the backups of the secrets you made earlier, run the following command:
    
    
    kubectl apply -f backup/
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
