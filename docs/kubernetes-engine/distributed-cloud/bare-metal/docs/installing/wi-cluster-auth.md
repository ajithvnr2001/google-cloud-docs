---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/wi-cluster-auth/
title: Workload Identity Cluster Authentication \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:05.306432+00:00
---

# Workload Identity Cluster Authentication  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/wi-cluster-auth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Workload Identity Cluster Authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up and use Workload Identity Cluster Authentication for Distributed Cloud software only for bare metal. Instead of service account keys, Workload Identity Cluster Authentication uses short-lived tokens and Workload Identity Federation to create and secure your clusters. The short-lived credentials for the service account are in the form of OAuth 2.0 access tokens. The access tokens expire after 1 hour by default. Likewise, image pull tokens also expire after 1 hour by default.

By contrast, _keyed mode_ , the standard method for creating and securing clusters, uses downloaded service account keys. When you create a self-managed (admin, hybrid, or standalone) cluster, you specify the path to the downloaded keys. The keys are then stored as Secrets in the cluster and any managed user clusters. By default, service account keys don't expire and are a security risk if not managed correctly. For information on setting an expiration time for your service account keys, see [Expiry times for user-managed keys](https://docs.cloud.google.com/iam/docs/service-account-creds#key-expiry).

Workload Identity Cluster Authentication provides two main benefits over using service account keys:

  * **Improved security** : Service account keys are a security risk if not managed correctly. OAuth 2.0 tokens and Workload Identity Federation are considered best practice alternatives to service account keys. For more information on service account tokens, see [Short-lived service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials). For more information about Workload Identity Federation, see [ Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).

  * **Reduced maintenance** : Service account keys require more maintenance. Regularly rotating and securing these keys can be a significant administrative burden.




Workload Identity Cluster Authentication was introduced for [Preview](https://cloud.google.com/products/#product-launch-stages) with release 1.30 and it's in GA for release 1.33 and higher. Workload Identity Cluster Authentication can be enabled only when creating new clusters. You can't configure an existing cluster to use Workload Identity Cluster Authentication during an update or upgrade. For additional restrictions, see Limitations.

This page is for Admins and architects and Operators who set up, monitor, and manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Before you begin

In the following sections, you create service accounts and grant roles needed for Workload Identity Cluster Authentication. The setup instructions in this document aren't a replacement for the instructions in [Set up Google Cloud resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa), they are required in addition to the standard Distributed Cloud software only installation prerequisites. The service accounts required for Workload Identity Cluster Authentication are similar to the service accounts described in [Set up Google Cloud resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa), but they are uniquely named, so they don't interfere with clusters that use the default service account keys.

The service accounts required for Workload Identity Cluster Authentication differ for the [Preview](https://cloud.google.com/products#product-launch-stages) and GA offerings as described in the following table:

###  1.33 and later 

Service account | Purpose | Roles  
---|---|---  
`admin-sa` |  You use this service account to generate tokens. Each token has the privileges associated with the service account roles.  |  `roles/gkehub.admin`  
`roles/iam.serviceAccountAdmin`  
`roles/iam.serviceAccountTokenCreator`  
`roles/iam.workloadIdentityPoolAdmin`*  
`roles/logging.admin`  
`roles/monitoring.admin`  
`roles/resourcemanager.projectIamAdmin`  
`baremetal-gcr` |  Google Distributed Cloud uses this service account to download container images from Artifact Registry.  | None  
  
*The `roles/iam.workloadIdentityPoolAdmin` IAM role is required for version 1.34 and later only.

###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Service account | Purpose | Roles  
---|---|---  
`admin-sa` |  You use this service account to generate tokens. Each token has the privileges associated with the service account roles.  |  `roles/gkehub.admin`  
`roles/iam.serviceAccountAdmin`  
`roles/iam.serviceAccountTokenCreator`  
`roles/logging.admin`  
`roles/monitoring.admin`  
`baremetal-controller` |  [Connect Agent](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/connect-agent) uses this service account to maintain a connection between your cluster and Google Cloud and to register your clusters with [ a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts). This service account also refreshes tokens for the `baremetal-gcr` service account.  |  `roles/gkehub.admin`  
`roles/monitoring.dashboardEditor`  
`roles/serviceusage.serviceUsageViewer`  
`baremetal-cloud-ops` |  Stackdriver Agent uses this service account to export logs and metrics from clusters to [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). You can't disable Cloud Logging and Cloud Monitoring for your clusters. This service account and all of the roles listed for this service account are required. |  `roles/kubernetesmetadata.publisher`  
`roles/logging.logWriter`  
`roles/monitoring.dashboardEditor`  
`roles/monitoring.metricWriter`  
`roles/monitoring.viewer`  
`roles/opsconfigmonitoring.resourceMetadata.writer`  
`roles/serviceusage.serviceUsageViewer`  
`roles/stackdriver.resourceMetadata.writer`  
`baremetal-gcr` |  Google Distributed Cloud uses this service account to download container images from Artifact Registry.  | None  
  
## Set up service accounts

The following sections contain instructions to create the required service accounts and grant them the necessary roles for Workload Identity Cluster Authentication. For a list of the service accounts and their required roles, see the table in the preceding section.

### Create service accounts

To create the service accounts for Workload Identity Cluster Authentication, use the following steps:

  1. On your admin workstation, log in to Google Cloud CLI:
         
         gcloud auth login
         

  2. Create the required service accounts for Workload Identity Cluster Authentication:

The `admin-sa` service account name is arbitrary. You can change the name if it causes a conflict in your project. The other service accounts for Workload Identity Cluster Authentication have predetermined names that can be customized, if you want.

###  1.33 and later 
         
         gcloud iam service-accounts create admin-sa \
             --project=PROJECT_ID
         
         gcloud iam service-accounts create baremetal-gcr \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

```sh gcloud iam service-accounts create admin-sa   
\--project=PROJECT_ID

gcloud iam service-accounts create baremetal-controller   
\--project=PROJECT_ID

gcloud iam service-accounts create baremetal-cloud-ops   
\--project=PROJECT_ID

gcloud iam service-accounts create baremetal-gcr   
\--project=PROJECT_ID ```

Replace `PROJECT_ID` with the ID of your Google Cloud project.




### Add Identity and Access Management policy bindings for service accounts

Use the following steps to apply the required Identity and Access Management policy bindings to the new service accounts:

###  1.33 and later 

  1. Add IAM policy bindings for required roles for the `admin-sa` service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/gkehub.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountAdmin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/logging.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/monitoring.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/resourcemanager.projectIamAdmin
         




###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Add IAM policy bindings for required roles for the `admin-sa` service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/gkehub.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountAdmin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/logging.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/monitoring.admin
         

  2. Add IAM policy bindings for required roles for the `baremetal-controller` service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-controller@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/gkehub.admin
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-controller@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/monitoring.dashboardEditor
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-controller@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/serviceusage.serviceUsageViewer
         

  3. Add IAM policy bindings for required roles for the `baremetal-cloud-ops` service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/kubernetesmetadata.publisher
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/logging.logWriter
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/monitoring.dashboardEditor
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/monitoring.metricWriter
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/monitoring.viewer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/opsconfigmonitoring.resourceMetadata.writer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/serviceusage.serviceUsageViewer
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member=serviceAccount:baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/stackdriver.resourceMetadata.writer
         

  4. Grant the `baremetal-controller` service account the ability to generate access tokens on behalf of the `baremetal-gcr` service account:
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-gcr@PROJECT_ID.iam.gserviceaccount.com \
             --member=serviceAccount:baremetal-controller@PROJECT_ID.iam.gserviceaccount.com \
             --role=roles/iam.serviceAccountTokenCreator
         




### Set up authentication

The following steps set up the authentication flow that uses a short-lived token for authenticating cluster operations:

  1. On your admin workstation, log in to Google Cloud CLI:
         
         gcloud auth login
         

  2. On your admin workstation, create and download a key for the `admin-sa` service account:

This key is needed for authorizing access for the `admin-sa` service account.
         
         gcloud iam service-accounts keys create TMP_KEY_FILE_PATH \
             --iam-account=admin-sa@PROJECT_ID.iam.gserviceaccount.com
         

Replace `TMP_KEY_FILE_PATH` with the path, including the filename, of the downloaded key file.

  3. On your admin workstation, create a `GOOGLE_APPLICATION_CREDENTIALS` environment variable with the value of downloaded service account key:
         
         export GOOGLE_APPLICATION_CREDENTIALS=TMP_KEY_FILE_PATH
         

  4. On your admin workstation, create a `GCP_ACCESS_TOKEN` environment variable with the value of an access token created by the `admin-sa` service account:
         
         export GCP_ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
         

By default, the access token has a lifetime of 1 hour.

  5. Verify that the token is generated by the `admin-sa` service account with the correct expiration:
         
         curl "https://oauth2.googleapis.com/tokeninfo?access_token=$GCP_ACCESS_TOKEN"
         

The response should include lines that look similar to the following:
         
         ...
         "exp": "1759512810",**"expires_in": "3589",**
         ...
         

The expiration value is in seconds and should be less than `3600`, indicating that the token expires in less than an hour.




## Configure Workload Identity Federation for your clusters

To provide Google Cloud access with Workload Identity Federation for GKE, you create an IAM allow policy that grants access on a specific Google Cloud resource to a principal that corresponds to your application's identity. In this case, Workload Identity Federation grants access to specific operators in the cluster. For more information on Workload Identity Federation for GKE, see [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) in the IAM documentation.

###  1.33 and later 

For cluster versions where Workload Identity Cluster Authentication is in GA, you use the `bmctl configure projects` command to configure Workload Identity Federation for your clusters. This command is incorporated into the steps for creating an admin cluster and creating a user cluster.

To prevent containerd instability when you're using a registry mirror to pull container images for your cluster, you must add the `baremetal.cluster.gke.io/enable-gcr-image-credential-refresh: "false"` cluster annotation. This annotation is available for versions 1.33.200-gke.70 and later:
    
    
    ---
    ...
    registryMirrors:
      - endpoint: https://198.51.20.1:5000
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
      annotations:**    baremetal.cluster.gke.io/enable-gcr-image-credential-refresh: "false"**
    spec:
      type: admin
      anthosBareMetalVersion: 1.33.200-gke.70
      ...
    

###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For cluster versions where Workload Identity Cluster Authentication is in [Preview](https://cloud.google.com/products#product-launch-stages), you must configure Workload Identity Federation for your clusters manually as described in the following sections.

### Add IAM policy bindings for the cluster operator

The following commands grant the `anthos-cluster-operator` Kubernetes service account the ability to impersonate the `baremetal-controller` service account and interact with Google Cloud resources on behalf of the cluster:

  1. For each cluster configured for Workload Identity Cluster Authentication (or planned to use Workload Identity Cluster Authentication), including the bootstrap cluster, grant `anthos-cluster-operator` in the cluster the ability to impersonate the `baremetal-controller` service account:

In the following command, the `principalSet` consists of the workload identity pool and a Kubernetes service account, `anthos-cluster-operator`, in the `kube-system` namespace.
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-controller@PROJECT_ID.iam.gserviceaccount.com \
             --member=principalSet://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/attribute.fleetclusteridentity/projects/PROJECT_ID/locations/REGION/memberships/CLUSTER_NAME/ns/kube-system/sa/anthos-cluster-operator \
             --role=roles/iam.workloadIdentityUser \
             --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_NUM`: the automatically generated [unique identifier for your project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `REGION`: the fleet membership location for your cluster, which is `global`, by default. For more information, see [Fleet membership location](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#fleet_membership_location).

     * `CLUSTER_NAME`: the name of the cluster. By default, the bootstrap cluster name is `bmctl-MACHINE_NAME`.

  2. Verify the policy bindings for the `baremetal-controller` service account:
         
         gcloud iam service-accounts get-iam-policy \
             baremetal-controller@PROJECT_ID.iam.gserviceaccount.com
         

The response should look similar to the following:
         
         bindings:
         - members:
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/bmctl-admin-ws/kube-system/anthos-cluster-operator
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/admin-cluster/kube-system/anthos-cluster-operator
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/user-cluster/kube-system/anthos-cluster-operator
           role: roles/iam.workloadIdentityUser
         etag: BwYoN3QLig0=
         version: 1
         




### Add IAM policy bindings for the Google Cloud Observability operators

The following commands grant the following Google Cloud Observability Kubernetes service accounts the ability to impersonate the `baremetal-cloud-ops` service account and interact with Google Cloud resources on behalf of the cluster:

  * `cloud-audit-logging`
  * `gke-metrics-agent`
  * `kubestore-collector`
  * `metadata-agent`
  * `stackdriver-log-forwarder`


  1. For each cluster configured for Workload Identity Cluster Authentication (or planned to use Workload Identity Cluster Authentication), including the bootstrap cluster, grant the Google Cloud Observability operators in the cluster the ability to impersonate the `baremetal-cloud-ops` service account:

In each of the following commands, the `principalSet` consists of the workload identity pool and a Kubernetes service account, such as `cloud-audit-logging`, in the `kube-system` namespace.
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --member=principalSet://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/attribute.fleetclusteridentity/projects/PROJECT_ID/locations/REGION/memberships/CLUSTER_NAME/ns/kube-system/sa/cloud-audit-logging \
             --role=roles/iam.workloadIdentityUser \
             --project=PROJECT_ID
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --member=principalSet://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/attribute.fleetclusteridentity/projects/PROJECT_ID/locations/REGION/memberships/CLUSTER_NAME/ns/kube-system/sa/gke-metrics-agent \
             --role=roles/iam.workloadIdentityUser \
             --project=PROJECT_ID
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --member=principalSet://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/attribute.fleetclusteridentity/projects/PROJECT_ID/locations/REGION/memberships/CLUSTER_NAME/ns/kube-system/sa/kubestore-collector \
             --role=roles/iam.workloadIdentityUser \
             --project=PROJECT_ID
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --member=principalSet://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/attribute.fleetclusteridentity/projects/PROJECT_ID/locations/REGION/memberships/CLUSTER_NAME/ns/kube-system/sa/metadata-agent \
             --role=roles/iam.workloadIdentityUser \
             --project=PROJECT_ID
         
         gcloud iam service-accounts add-iam-policy-binding \
             baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com \
             --member=principalSet://iam.googleapis.com/projects/PROJECT_NUM/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/attribute.fleetclusteridentity/projects/PROJECT_ID/locations/REGION/memberships/CLUSTER_NAME/ns/kube-system/sa/stackdriver-log-forwarder \
             --role=roles/iam.workloadIdentityUser \
             --project=PROJECT_ID
         

  2. Verify the policy bindings for the `baremetal-cloud-ops` service account:
         
         gcloud iam service-accounts get-iam-policy \
             baremetal-cloud-ops@PROJECT_ID.iam.gserviceaccount.com
         

The response should look similar to the following:
         
         bindings:
         - members:
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/bmctl-admin-ws/kube-system/cloud-audit-logging
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/bmctl-admin-ws/kube-system/gke-metrics-agent
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/bmctl-admin-ws/kube-system/kubestore-collector
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/bmctl-admin-ws/kube-system/metadata-agent
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/bmctl-admin-ws/kube-system/stackdriver-log-forwarder
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/admin-cluster/kube-system/cloud-audit-logging
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/admin-cluster/kube-system/gke-metrics-agent
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/admin-cluster/kube-system/kubestore-collector
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/admin-cluster/kube-system/metadata-agent
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/admin-cluster/kube-system/stackdriver-log-forwarder
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/user-cluster/kube-system/cloud-audit-logging
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/user-cluster/kube-system/gke-metrics-agent
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/user-cluster/kube-system/kubestore-collector
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/user-cluster/kube-system/metadata-agent
           - principalSet://iam.googleapis.com/projects/112233445566/locations/global/workloadIdentityPools/my-project.svc.id.goog/attribute.fleetclusteridentity/user-cluster/kube-system/stackdriver-log-forwarder
           role: roles/iam.workloadIdentityUser
         etag: BwYhT4gL-dY=
         version: 1
         




## Create an admin cluster

The steps for creating an admin cluster differ slightly for the [Preview](https://cloud.google.com/products#product-launch-stages) (versions 1.30-1.32) and GA (versions 1.33 and higher) offerings. The GA steps use the `bmctl configure projects` command to configure Workload Identity Federation for your clusters.

###  1.33 and later 

The most obvious cluster configuration difference for clusters that use Workload Identity Cluster Authentication is that you don't specify paths to downloaded service account keys.

  1. When you fill in your cluster settings in the configuration file, leave the service account key paths in the credential section blank as shown in the following example:
         
         gcrKeyPath:
         sshPrivateKeyPath: /home/USERNAME/.ssh/id_rsa
         gkeConnectAgentServiceAccountKeyPath:
         gkeConnectRegisterServiceAccountKeyPath:
         cloudOperationsServiceAccountKeyPath:
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-ADMIN_CLUSTER_NAME
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: ADMIN_CLUSTER_NAME
           namespace: cluster-ADMIN_CLUSTER_NAME
         spec:
           type: admin
           profile: default
           anthosBareMetalVersion: 1.33.0-gke.799
           ...
         

  2. Add the `baremetal.cluster.gke.io/enable-workload-identity-cluster-authentication: "true"` annotation to the cluster configuration file:
         
         gcrKeyPath:
         sshPrivateKeyPath: /home/USERNAME/.ssh/id_rsa
         gkeConnectAgentServiceAccountKeyPath:
         gkeConnectRegisterServiceAccountKeyPath:
         cloudOperationsServiceAccountKeyPath:
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-ADMIN_CLUSTER_NAME
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: ADMIN_CLUSTER_NAME
           namespace: cluster-ADMIN_CLUSTER_NAME**  annotations:
             baremetal.cluster.gke.io/enable-workload-identity-cluster-authentication: "true"**
         spec:
           type: admin
           profile: default
           anthosBareMetalVersion: 1.33.0-gke.799
           ...
         

  3. On your admin workstation, update the `GCP_ACCESS_TOKEN` environment variable with a newly retrieved access token:
         
         export GCP_ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
         

By default, the access token has a lifetime of 3600 seconds (1 hour). When you are using Workload Identity Cluster Authentication, `bmctl` checks the token expiration time. If the token expiry is within 1800 seconds (30 minutes), `bmctl` reports an error and exits.

  4. Configure Workload Identity Federation for cluster you're creating:
         
         bmctl configure projects --project-id=PROJECT_ID \
             --admin-cluster=ADMIN_CLUSTER_NAME
         

  5. Run the `bmctl create cluster` command to create your admin cluster.




###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The most obvious cluster configuration difference for clusters that use Workload Identity Cluster Authentication is that you don't specify paths to downloaded service account keys.

  1. When you fill in your cluster settings in the configuration file, leave the service account key paths in the credential section blank as shown in the following example:
         
         gcrKeyPath:
         sshPrivateKeyPath: /home/USERNAME/.ssh/id_rsa
         gkeConnectAgentServiceAccountKeyPath:
         gkeConnectRegisterServiceAccountKeyPath:
         cloudOperationsServiceAccountKeyPath:
         ---
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-ADMIN_CLUSTER_NAME
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: ADMIN_CLUSTER_NAME
           namespace: cluster-ADMIN_CLUSTER_NAME
         spec:
           type: admin
           profile: default
           anthosBareMetalVersion: 1.33.0-gke.799
           ...
         

  2. On your admin workstation, create and download a key for the `admin-sa` service account:

This key is needed for authorizing access for the `admin-sa` service account and you delete it immediately after the service account is authorized.
         
         gcloud iam service-accounts keys create TMP_KEY_FILE_PATH \
             --iam-account=admin-sa@PROJECT_ID.iam.gserviceaccount.com
         

Replace `TMP_KEY_FILE_PATH` with the path, including the filename, of the downloaded key file.

  3. Authorize access to Google Cloud with the `admin-sa` service account:
         
         gcloud auth activate-service-account admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --key-file=TMP_KEY_FILE_PATH
         

  4. Delete the downloaded JSON key file:
         
         rm TMP_KEY_FILE_PATH
         

The access token is short lived, so you typically need to regenerate it before you run `bmctl` commands for cluster operations, such as creating, upgrading, or resetting a cluster.

  5. On your admin workstation, create a `GCP_ACCESS_TOKEN` environment variable with the value of an access token created by the `admin-sa` service account:
         
         export GCP_ACCESS_TOKEN=$(gcloud auth print-access-token \
             --impersonate-service-account=admin-sa@PROJECT_ID.iam.gserviceaccount.com)
         

By default, the access token has a lifetime of 3600 seconds (1 hour).

  6. Run the `bmctl create cluster` command to create your admin cluster.




## Create a user cluster

The steps for creating an admin cluster differ slightly for the [Preview](https://cloud.google.com/products#product-launch-stages) (versions 1.30-1.32) and GA (versions 1.33 and higher) offerings. The GA steps use the `bmctl configure projects` command to configure Workload Identity Federation for your clusters.

###  1.33 and later 

  1. Add the `baremetal.cluster.gke.io/enable-workload-identity-cluster-authentication: "true"` annotation to the cluster configuration file:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: cluster-USER_CLUSTER_NAME
         ---
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: USER_CLUSTER_NAME
           namespace: cluster-USER_CLUSTER_NAME**  annotations:
             baremetal.cluster.gke.io/enable-workload-identity-cluster-authentication: "true"**
         spec:
           type: admin
           profile: default
           anthosBareMetalVersion: 1.33.0-gke.799
           ...
         

The access token is short lived, so you typically need to regenerate it before you run `bmctl` commands for cluster operations, such as creating, upgrading, or resetting a cluster.

  2. On your admin workstation, update the `GCP_ACCESS_TOKEN` environment variable with a newly retrieved access token:
         
         export GCP_ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
         

By default, the access token has a lifetime of 3600 seconds (1 hour).

  3. Configure Workload Identity Federation for cluster you're creating:
         
         bmctl configure projects --project-id=PROJECT_ID \
             --user-clusters=USER_CLUSTER_NAME
         

  4. Use `kubectl` to deploy the user cluster manifest:
         
         kubectl apply -f USER_CLUSTER_CONFIG \
             --kubeconfig ADMIN_KUBECONFIG
         




Replace the following:

  * `USER_CLUSTER_CONFIG`: the path of the user cluster configuration file.

  * `ADMIN_KUBECONFIG`: the path of the admin cluster's kubeconfig file.




###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. On your admin workstation, create and download a key for the `admin-sa` service account:

This key is needed for authorizing access for the `admin-sa` service account and you delete it immediately after the service account is authorized.
         
         gcloud iam service-accounts keys create TMP_KEY_FILE_PATH \
             --iam-account=admin-sa@PROJECT_ID.iam.gserviceaccount.com
         

Replace `TMP_KEY_FILE_PATH` with the path, including the filename, of the downloaded key file.

  2. Authorize access to Google Cloud with the `admin-sa` service account:
         
         gcloud auth activate-service-account admin-sa@PROJECT_ID.iam.gserviceaccount.com \
             --key-file=TMP_KEY_FILE_PATH
         

  3. Delete the downloaded JSON key file:
         
         rm TMP_KEY_FILE_PATH
         

The access token is short lived, so you typically need to regenerate it before you run `bmctl` commands for cluster operations, such as creating, upgrading, or resetting a cluster.

  4. On your admin workstation, create a `GCP_ACCESS_TOKEN` environment variable with the value of an access token created by the `admin-sa` service account:
         
         export GCP_ACCESS_TOKEN=$(gcloud auth print-access-token \
             --impersonate-service-account=admin-sa@PROJECT_ID.iam.gserviceaccount.com)
         

By default, the access token has a lifetime of 3600 seconds (1 hour).

  5. Run the `bmctl create cluster` command to create your user cluster.




## Other cluster operations

For clusters that use Workload Identity Cluster Authentication, the following `bmctl` commands require you to set the `GCP_ACCESS_TOKEN` environment variable to a valid, active access token:

  * `bmctl configure projects`
  * `bmctl create cluster`
  * `bmctl register bootstrap`
  * `bmctl reset cluster`
  * `bmctl upgrade cluster`



The `bmctl register bootstrap` supports using the `GCP_ACCESS_TOKEN` environment variable for Workload Identity Cluster Authentication only for Google Distributed Cloud version 1.34.0 and later. For versions before 1.34.0, you must use service account key files to authenticate `bmctl register bootstrap`.

If `bmctl` detects that the `GCP_ACCESS_TOKEN` environment variable has been set, it performs token validation:

  * If the token is valid, `bmctl` uses it for cluster operations.

  * If the token isn't valid, retrieve a new one:

The access token is short lived, so you typically need to regenerate it before you run `bmctl` commands for cluster operations, such as creating, upgrading, or resetting a cluster. On your admin workstation, update the `GCP_ACCESS_TOKEN` environment variable with a newly retrieved access token:

###  1.33 and later 
        
        export GCP_ACCESS_TOKEN=$(gcloud auth application-default print-access-token)
        

###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

`sh export GCP_ACCESS_TOKEN=$(gcloud auth print-access-token \ --impersonate-service-account=admin-sa@PROJECT_ID.iam.gserviceaccount.com)`

By default, the access token has a lifetime of 3600 seconds (1 hour). When you are using Workload Identity Cluster Authentication, `bmctl` checks the token expiration time. If the token expiry is within 1800 seconds (30 minutes), `bmctl` reports an error and exits.




## Customization

You can use service accounts with unique names for Workload Identity Cluster Authentication as long as they have bindings for the required roles.

###  1.33 and later 

By default, Workload Identity Cluster Authentication for version 1.33 and later clusters uses the `baremetal-gcr` service account only. Therefore, this is the only service account that can be customized.

  1. Ensure that the service account that you want to use has the roles identified in the table in Before you begin.

  2. Annotate the cluster configuration file to specify the custom name for the Workload Identity Cluster Authentication service account:
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: my-cluster
           namespace: cluster-my-cluster
           annotations:
             ...**    baremetal.cluster.gke.io/gcr-service-account: "CUSTOM_AR_GSA"**
         spec:
           type: admin
           profile: default
           anthosBareMetalVersion: 1.33.0-gke.799
           ...
         




Replace `CUSTOM_AR_GSA` with the email name of the service account used by Google Distributed Cloud to download container images from Artifact Registry.

###  1.30-1.32 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Ensure that the service accounts that you want to use have the roles identified in the table in Before you begin.

  2. Annotate the cluster configuration file to specify the custom names for the Workload Identity Cluster Authentication service accounts:

Specifying custom names lets you use existing service accounts. Make sure that the custom service account names you specify are distinct from each other. We don't support using a single service account to replace two or more of the default service accounts.
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: my-cluster
           namespace: cluster-my-cluster
           annotations:
             ...**    baremetal.cluster.gke.io/controller-service-account: "CUSTOM_CONTROLLER_GSA"
             baremetal.cluster.gke.io/cloud-ops-service-account: "CUSTOM_CLOUD_OPS_GSA"
             baremetal.cluster.gke.io/gcr-service-account: "CUSTOM_AR_GSA"**
         spec:
           type: admin
           profile: default
           anthosBareMetalVersion: 1.30.0-gke.1930
           ...
         




Replace the following:

  * `CUSTOM_CONTROLLER_GSA`: the email name of the service account used by Connect Agent to maintain a connection between your cluster and Google Cloud, and to register your clusters.

  * `CUSTOM_CLOUD_OPS_GSA`: the email name of the service account used by Stackdriver Agent to export logs and metrics from clusters to Cloud Logging and Cloud Monitoring.

  * `CUSTOM_AR_GSA`: the email name of the service account used by Google Distributed Cloud to download container images from Artifact Registry.




## Limitations

The following features and capabilities aren't supported when you use Workload Identity Cluster Authentication for Distributed Cloud software only for bare metal:

  * Using a proxy server
  * VPC Service Controls
  * Update existing _keyed mode_ clusters to use Workload Identity Cluster Authentication
  * Cluster lifecycle management using GKE On-Prem API clients, such as Google Cloud CLI, Terraform, or the Google Cloud console



## What's next

  * [Deploy an application](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/deploy-app)
  * [Create a Service and an Ingress](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
