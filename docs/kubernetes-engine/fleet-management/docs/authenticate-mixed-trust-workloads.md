---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/authenticate-mixed-trust-workloads/
title: Authenticate to Google Cloud APIs from mixed-trust fleet workloads \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:57.416646+00:00
---

# Authenticate to Google Cloud APIs from mixed-trust fleet workloads  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/authenticate-mixed-trust-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Authenticate to Google Cloud APIs from mixed-trust fleet workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure your applications to authenticate to Google Cloud APIs like the Compute Engine API or the AI Platform API from fleets that have a mixed trust model across the fleet. If your fleet has a shared trust model across the fleet, see [Authenticate to Google Cloud APIs from shared-trust fleet workloads](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity).

This page is for Platform admins and operators and for Security engineers who want to programmatically authenticate from fleet workloads to Google Cloud APIs. To learn more about the user roles and example tasks that we reference in Google Cloud documentation, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [About fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/about-fleet-workload-identity-federation)
  * [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
  * [Identity and Access Management (IAM) allow policies](https://docs.cloud.google.com/iam/docs/policies)
  * [Team scopes and fleet namespaces](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management)



## About fleet Workload Identity Federation for mixed-trust environments

Fleet Workload Identity Federation lets you grant IAM roles on Google Cloud APIs and resources to entities in your fleet, like workloads in a specific namespace. By default, your fleet host project uses a Google-managed workload identity pool to provision identities for entities across the fleet. However, in mixed-trust environments such as multi-tenant fleets or in fleet host projects that run standalone clusters, we recommend that you configure a separate _self-managed_ workload identity pool for a subset of your workloads and clusters.

Entities that use a self-managed workload identity pool have different identifiers in IAM policies than entities that use the Google-managed workload identity pool of the fleet host project. This ensures that granting access to principals in a specific fleet namespace doesn't unintentionally grant access to any other principals that match the identifier.

Self-managed workload identity pools require that you use _team scopes_. Team scopes let you control access to subsets of fleet resources on a per-team basis. You bind specific team scopes to specific fleet member clusters to allow that team to deploy workloads on those clusters. Within a team scope, team members can only deploy workloads to _fleet namespaces_.

Using self-managed workload identity pools to provide identities for team scope workloads has benefits like the following:

  * Ensure that access grants to entities in fleet namespaces don't unintentionally apply to entities in other namespaces or clusters.
  * Configure a set of fleet clusters to get identities from the self-managed pool by binding them to a team scope and setting up the self-managed pool as an identity provider in those clusters.
  * Configure a subset of a team scope's bound clusters to get identities from the self-managed pool by only setting up the self-managed pool as an identity provider in specific clusters.



### Identity sameness in mixed-trust environment example

Consider the following scenario:

  * You have two fleet member clusters: `frontend-cluster` and `finance-cluster`.
  * You haven't configured a self-managed workload identity pool.
  * You create a `finance-team` team scope and a `finance-ns` fleet namespace in the team scope.
  * You bind the `finance-cluster` cluster to the `finance-team` team scope.
  * You grant an IAM role to the `finance-sa` Kubernetes ServiceAccount in the `finance-ns` fleet namespace.



Any workloads that meet the following criteria share the same identity:

  * Run in the `finance-ns` fleet namespace.
  * Use the `finance-sa` ServiceAccount.



However, if someone in the `frontend-cluster` cluster creates a `finance-ns` Kubernetes namespace and a `finance-sa` ServiceAccount, they get the same identity as the workloads in the `finance-cluster` cluster. This is because the entire fleet uses the Google-managed workload identity pool of the fleet host project, and because the principal identifier doesn't specify a host cluster.

Consider the following changes to the preceding scenario:

  * You set up a self-managed workload identity pool in your fleet.
  * You configure the `finance-cluster` cluster to get identities from the self-managed pool instead of from the Google-managed pool.
  * You create an IAM role grant that specifies the self-managed pool in the principal identifier instead of the Google-managed pool.



The workloads that run in the `finance-ns` fleet namespace in `finance-cluster` now get an identity from the self-managed pool. However, entities in the `finance-ns` Kubernetes namespace in the `frontend-cluster` cluster continue to get identities from the Google-managed workload identity pool of the fleet host project.

These changes result in the following benefits:

  * You can explicitly grant roles to entities in the `finance-ns` fleet namespace.
  * Entities in the `frontend-cluster` cluster can't get the same access because the identities in the `frontend-cluster` cluster come from the Google-managed workload identity pool.



## Before you begin

  * Ensure that you have the following command line tools installed:

    * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which includes `gcloud`, the command line tool for interacting with Google Cloud.
    * [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl)

If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.




### Requirements

You must use fleet team management features like team scopes and fleet namespaces in your fleet. The instructions on this page show you how to configure an example team scope and fleet namespace.

## Prepare your clusters

Before applications in your fleet can receive a federated identity, the clusters that they run on must be [registered to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) and properly configured to use fleet Workload Identity Federation. The following sections describe how to set up fleet Workload Identity Federation for different types of clusters.

### GKE

For GKE clusters, you need to [register the cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke) to the fleet.

### Clusters outside Google Cloud

The following types of clusters automatically enable fleet Workload Identity Federation and are registered to your fleet during cluster creation:

  * Google Distributed Cloud (software only) on VMware
  * Google Distributed Cloud (software only) on bare metal
  * GKE on AWS
  * GKE on Azure



### Attached clusters

EKS and AKS attached clusters registered using the GKE Multi-Cloud API are registered with fleet Workload Identity Federation enabled by default. [Other attached clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/how-to/attach-kubernetes-clusters) can be registered with fleet Workload Identity Federation enabled if they meet the necessary [requirements](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/before-you-begin#fleet_workload_identity_requirements). Follow the instructions for your cluster type in [Registering a cluster](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/how-to/attach-kubernetes-clusters).

## Set up an IAM workload identity pool

In this section, you create a new IAM workload identity pool in the fleet host project and give the fleet service agent access to the new pool. This workload identity pool is the _self-managed_ pool.

  1. Create a workload identity pool:
         
         gcloud iam workload-identity-pools create POOL_NAME \
             --location=global \
             --project=POOL_HOST_PROJECT_ID \
             --mode=TRUST_DOMAIN
         

Replace the following:

     * `POOL_NAME`: the name of the new workload identity pool.
     * `POOL_HOST_PROJECT_ID`: the project ID of the project that you want to create the self-managed workload identity pool in. You can use any Google Cloud project, including your fleet host project.
  2. Grant the [IAM Workload Identity Pool Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`) on the new workload identity pool to the fleet service agent:
         
         gcloud iam workload-identity-pools add-iam-policy-binding POOL_NAME \
             --project=POOL_HOST_PROJECT_ID \
             --location=global \
             --member=serviceAccount:service-FLEET_HOST_PROJECT_NUMBER@gcp-sa-gkehub.iam.gserviceaccount.com \
             --role=roles/iam.workloadIdentityPoolAdmin \
             --condition=None
         

Replace `FLEET_HOST_PROJECT_NUMBER` with the project number of the fleet host project.

To follow the security best practice principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege), this command grants the IAM Workload Identity Pool Admin role for the specific workload identity pool that you are using for the fleet, and not for all workload identity pools in the project.




## Add the self-managed pool to your fleet configuration

In this section, you enable self-managed pools with fleet Workload Identity Federation and add the pool that you created to the fleet configuration. This section also provides instructions to create a new team scope and a fleet namespace. If your fleet already has team scopes and fleet namespaces configured, skip those steps.

  1. Enable fleet Workload Identity Federation at the fleet level:
         
         gcloud container fleet workload-identity enable \
           --project=FLEET_HOST_PROJECT_ID
         

Replace `FLEET_HOST_PROJECT_ID` with the project ID of your fleet host project.

  2. Add the self-managed workload identity pool to the fleet configuration:
         
         gcloud container fleet workload-identity scope-tenancy-pool set POOL_NAME
         

Replace POOL_NAME with the name of your self-managed workload identity pool. This value has the following syntax:
         
         POOL_NAME.global.POOL_HOST_PROJECT_NUMBER.workload.id.goog
         

  3. Create a new team scope. If you have an existing team scope and fleet namespace, skip to the Verify the workload identity pool configuration section.
         
         gcloud container fleet scopes create SCOPE_NAME
         

Replace `SCOPE_NAME` with the name of your new team scope.

  4. Create a new fleet namespace in the team scope:
         
         gcloud container fleet scopes namespaces create NAMESPACE_NAME \
             --scope=SCOPE_NAME
         

Replace `NAMESPACE_NAME` with the name of your new fleet namespace.

  5. Bind a cluster in your fleet to the team scope:
         
         gcloud container fleet memberships bindings create BINDING_NAME \
             --membership=FLEET_CLUSTER_NAME \
             --location=global \
             --scope=SCOPE_NAME
         

Replace the following:

     * `BINDING_NAME`: the name for your new membership binding.
     * `FLEET_CLUSTER_NAME`: the name of the existing fleet cluster to bind to the team scope.



## Verify the workload identity pool configuration

In this section, you ensure that your self-managed workload identity pool configuration was successful.

  1. Describe the fleet membership configuration:
         
         gcloud container fleet memberships describe FLEET_CLUSTER_NAME \
             --location=global
         

Replace `FLEET_CLUSTER_NAME` with the name of an existing fleet cluster that's bound to any team scope in your fleet.

The output is similar to the following:
         
         authority:
         ...
           **scopeTenancyIdentityProvider: https://gkehub.googleapis.com/projects/ FLEET_HOST_PROJECT_ID/locations/global/memberships/FLEET_CLUSTER_NAME
           scopeTenancyWorkloadIdentityPool: POOL_NAME.global.FLEET_HOST_PROJECT_NUMBER.workload.id.goog**
           workloadIdentityPool: FLEET_HOST_PROJECT_ID.svc.id.goog
         ...
         

This output should contain the following fields:

     * `scopeTenancyIdentityProvider`: the identity provider for workloads that run in fleet namespaces within team scopes. The value is a resource identifier for your cluster.
     * `scopeTenancyWorkloadIdentityPool`: the workload identity pool from which workloads in fleet namespaces within team scopes get identifiers. The value is your self-managed workload identity pool, with the format `POOL_NAME.global.FLEET_HOST_PROJECT_NUMBER.workload.id.goog`.
     * `workloadIdentityPool`: the name of the Google-managed workload identity pool of the fleet host project, from which all of the other workloads in the fleet get identities by default.
  2. Optional: Check whether your workload identity pool has a namespace that has the same name as your fleet namespace:
         
         gcloud iam workload-identity-pools namespaces list \
             --workload-identity-pool=POOL_NAME \
             --location=global
         

The output is similar to the following:
         
         ---
         description: Fleet namespace NAMESPACE_NAME
         name: projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_NAME/namespaces/NAMESPACE_NAME
         state: ACTIVE
         




Your fleet can now use the self-managed workload identity pool to get identities for workloads that run in fleet namespaces. To start using the self-managed pool, configure how specific clusters get identities, as described in the next section.

## Make workloads use self-managed pools for identities

To make workloads use the self-managed pool, you configure specific fleet namespaces in fleet member clusters by using a Kubernetes ConfigMap. This per-cluster, per-namespace configuration lets you further reduce the scope of access grants from entire fleet namespaces to workloads that run in specific fleet namespaces in specific clusters.

  1. Connect to your fleet member cluster:
         
         gcloud container clusters get-credentials FLEET_CLUSTER_NAME \
             --project=CLUSTER_PROJECT_ID \
             --location=CLUSTER_LOCATION
         

Replace the following:

     * `FLEET_CLUSTER_NAME`: the name of a fleet member cluster that's already bound to a team scope.
     * `CLUSTER_PROJECT_ID`: the project ID of the cluster project.
     * `CLUSTER_LOCATION`: the location of the cluster.
  2. Get the full name of the self-managed workload identity pool. You need it later.
         
         gcloud iam workload-identity-pools describe POOL_NAME --location=global
         

The output is similar to the following:
         
         POOL_NAME.global.FLEET_HOST_PROJECT_NUMBER.workload.id.goog
         

  3. Get the name of the identity provider for team scopes. You need it later.
         
         kubectl get membership membership -o json | jq -r ".spec.scope_tenancy_identity_provider"
         

The output is similar to the following:
         
         https://gkehub.googleapis.com/projects/FLEET_HOST_PROJECT_ID/locations/global/memberships/FLEET_CLUSTER_NAME
         

  4. In a text editor, save the following YAML manifest for a ConfigMap as `self-managed-pool.yaml`:
         
         kind: ConfigMap
         apiVersion: v1
         metadata:
           namespace: NAMESPACE_NAME
           name: google-application-credentials
         data:
           config: |
             {
               "type": "external_account",
               "audience": "identitynamespace:POOL_NAME:IDENTITY_PROVIDER",
               "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
               "token_url": "https://sts.googleapis.com/v1/token",
               "credential_source": {
                 "file": "/var/run/secrets/tokens/gcp-ksa/token"
               }
             }
         

Replace the following:

     * `NAMESPACE_NAME`: the name of the fleet namespace.
     * `POOL_NAME`: the full name of the self-managed workload identity pool from the output of the previous steps in this section. For example, `projects/1234567890/locations/global/workloadIdentityPools/example-pool`.
     * `IDENTITY_PROVIDER`: the identity provider name from the output of the previous steps in this section. For example, `https://gkehub.googleapis.com/projects/1234567890/locations/global/memberships/example-cluster.`
  5. Deploy the ConfigMap in your cluster:
         
         kubectl create -f self-managed-pool.yaml
         




Deploying the ConfigMap indicates to GKE that workloads in that namespace should use the self-managed workload identity pool to get identities.

## Grant IAM roles to principals

In this section, you create a Kubernetes ServiceAccount in a fleet namespace and grant an IAM role to the ServiceAccount. Pods that use this ServiceAccount can then access the Google Cloud resources on which you grant the role.

  1. Create a Kubernetes ServiceAccount in your fleet namespace:
         
         kubectl create serviceaccount SERVICEACCOUNT_NAME \
             --namespace=NAMESPACE_NAME
         

Replace the following:

     * `SERVICEACCOUNT_NAME`: the name of your new ServiceAccount.
     * `NAMESPACE_NAME`: the name of the fleet namespace.
  2. Grant an IAM role to the ServiceAccount. The following example command grants the [Storage Object Viewer role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) role on a bucket to the ServiceAccount:
         
         gcloud storage buckets add-iam-policy-binding gs://BUCKET_NAME \
             --member=principal://iam.googleapis.com/projects/FLEET_HOST_PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_NAME.global.FLEET_HOST_PROJECT_NUMBER.workload.id.goog/subject/ns/NAMESPACE_NAME/sa/SERVICEACCOUNT_NAME \
             --role=roles/storage.objectViewer \
             --condition=None
         




The `member` flag contains the principal identifier for the new ServiceAccount that you created. The requests that your workloads send to Google Cloud APIs use a [federated access token](https://docs.cloud.google.com/iam/docs/workload-identity-federation#access_management). This federated access token includes the principal identifier of the entity that sends the request. If the principal in an allow policy that grants a role on the target resource matches the principal in the federated access token, authentication and authorization can continue.

## Deploy workloads that use the self-managed pool

Kubernetes manifests that you apply in your fleet namespace must be configured to get identities from the self-managed pool. The workloads that you deploy that need to call Google Cloud APIs should include the following fields:

  * `metadata.namespace`: the name of the fleet namespace.
  * `spec.serviceAccountName`: the name of the Kubernetes ServiceAccount in the fleet namespace.
  * `spec.containers.env`: an environment variable named `GOOGLE_APPLICATION_CREDENTIALS` that indicates the path to the Application Default Credentials (ADC) file.
  * `spec.containers.volumeMounts`: a read-only volume that lets the container use the bearer token for the ServiceAccount.
  * `spec.volumes`: a projected volume that mounts a ServiceAccount token into the Pod. The token's audience is the self-managed workload identity pool. The ConfigMap that contains the fleet Workload Identity Federation configuration is a source for the volume.



For an example of a correctly-configured manifest file, see the Verify authentication from a workload section.

## Verify authentication from a workload

This section provides optional instructions to verify that you correctly configured the self-managed workload identity pool by listing the contents of an example Cloud Storage bucket. You create a bucket, grant a role on the bucket to a ServiceAccount in a fleet namespace, and deploy a Pod to try and access the bucket.

  1. Create a Cloud Storage bucket:
         
         gcloud storage buckets create gs://FLEET_HOST_PROJECT_ID-workload-id-bucket \
             --location=LOCATION \
             --project=FLEET_HOST_PROJECT_ID
         

  2. Grant the `roles/storage.objectViewer` role on the bucket to the ServiceAccount in the fleet namespace:
         
         gcloud storage buckets add-iam-policy-binding gs://FLEET_HOST_PROJECT_ID-workload-id-bucket \
             --condition=None \
             --role=roles/storage.objectViewer \
             --member=principal://iam.googleapis.com/projects/FLEET_PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_NAME.global.FLEET_HOST_PROJECT_NUMBER.workload.id.goog/subject/ns/NAMESPACE_NAME/sa/SERVICEACCOUNT_NAME
         

Replace the following:

     * `FLEET_HOST_PROJECT_NUMBER`: the project number of your fleet host project.
     * `POOL_NAME`: the name of your self-managed workload identity pool.
     * `NAMESPACE_NAME`: the name of the fleet namespace in which you want to run the Pod.
     * `SERVICEACCOUNT_NAME`: the name of the Kubernetes ServiceAccount that the Pod should use.
  3. Save the following manifest as `pod-bucket-access.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: bucket-access-pod
           namespace:  NAMESPACE_NAME
         spec:
           serviceAccountName: SERVICEACCOUNT_NAME
           containers:
           - name: sample-container
             image: google/cloud-sdk:slim
             command: ["sleep","infinity"]
             env:
             - name: GOOGLE_APPLICATION_CREDENTIALS
               value: /var/run/secrets/tokens/gcp-ksa/google-application-credentials.json
             volumeMounts:
             - name: gcp-ksa
               mountPath: /var/run/secrets/tokens/gcp-ksa
               readOnly: true
           volumes:
           - name: gcp-ksa
             projected:
               defaultMode: 420
               sources:
               - serviceAccountToken:
                   path: token
                   audience: POOL_NAME
                   expirationSeconds: 172800
               - configMap:
                   name: google-application-credentials
                   optional: false
                   items:
                   - key: "config"
                     path: "google-application-credentials.json"
         

Replace the following:

     * `NAMESPACE_NAME`: the name of the fleet namespace in which you want to run the Pod.
     * `SERVICEACCOUNT_NAME`: the name of the Kubernetes ServiceAccount that the Pod should use.
     * `POOL_NAME`: the name of your self-managed workload identity pool.
  4. Deploy the Pod in your cluster:
         
         kubectl apply -f pod-bucket-access.yaml
         

  5. Open a shell session in the Pod:
         
         kubectl exec -it bucket-access-pod -n NAMESPACE_NAME -- /bin/bash
         

  6. Try to list objects in the bucket:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             "https://storage.googleapis.com/storage/v1/b/FLEET_HOST_PROJECT_ID-workload-id-bucket/o"
         

The output is the following:
         
         {
           "kind": "storage#objects"
         }
         


**Success:** your fleet Workload Identity Federation configuration works as expected. Workloads in the fleet namespace use the self-managed pool to get identities.

You can optionally verify that a similar namespace and ServiceAccount in a different fleet member cluster won't be able to assert the same identity. In a cluster that uses fleet Workload Identity Federation but _doesn't_ have a fleet namespace or a self-managed pool configuration, do the following steps:

  1. Create a new Kubernetes namespace with the same name as the fleet namespace in which you set up the self-managed workload identity pool.
  2. Create a new Kubernetes ServiceAccount with the same name as the ServiceAccount to which you granted an IAM role in previous sections.
  3. Deploy a Pod that uses the same ServiceAccount and namespace, but for which the `spec.volumes.projected.sources.serviceAccountToken` field specifies the Google-managed workload identity pool. This pool has the following syntax:
         
         FLEET_HOST_PROJECT_ID.svc.id.goog
         

  4. Attempt to access the Cloud Storage bucket from a shell session in the Pod.




The output should be a `401: Unauthorized` error, because the principal identifier for the Pod that uses the Google-managed workload identity pool is different from the principal identifier for the Pod that uses the self-managed pool.

## What's next

  * [Manage fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features)
  * [Secure your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
