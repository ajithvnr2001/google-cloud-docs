---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity/
title: Authenticate to Google Cloud APIs from shared-trust fleet workloads \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:14.740057+00:00
---

# Authenticate to Google Cloud APIs from shared-trust fleet workloads  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Authenticate to Google Cloud APIs from shared-trust fleet workloads Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure your applications to authenticate to Google Cloud APIs like the Compute Engine API or the AI Platform API from fleets that have a shared trust model across the fleet. If your fleet has a mixed trust model across the fleet, see [Authenticate to Google Cloud APIs from mixed-trust fleet workloads](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/authenticate-mixed-trust-workloads).

This page is for Platform admins and operators and for Security engineers who want to programmatically authenticate from fleet workloads to Google Cloud APIs. To learn more about the user roles and example tasks that we reference in Google Cloud documentation, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the following concepts:

  * [About fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/about-fleet-workload-identity-federation)
  * [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)
  * [Identity and Access Management (IAM) allow policies](https://docs.cloud.google.com/iam/docs/policies)



## About fleet Workload Identity Federation for shared-trust environments

Fleet Workload Identity Federation lets you authenticate from fleet workloads to Google Cloud APIs by using built-in Google Cloud and Kubernetes authentication mechanisms. Fleet Workload Identity Federation eliminates the need to use less secure methods like mounting access tokens in Pods or storing long-lived credentials.

By default, your fleet host project uses a Google-managed workload identity pool to provision identities for entities across the fleet. Any entity in the fleet or in the fleet host project that has the same IAM identifier is considered to be the same thing by IAM. This _implicit identity sameness_ is useful when granting access at scale in shared-trust environments, such as single-tenant fleets, where it doesn't matter if other entities unintentionally get similar permissions on resources.

## Before you start

  * Ensure that you have the following command line tools installed:

    * The latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), which includes `gcloud`, the command line tool for interacting with Google Cloud.
    * [`kubectl`](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin#install-kubectl)

If you are using Cloud Shell as your shell environment for interacting with Google Cloud, these tools are installed for you.

  * Ensure that you have [initialized](https://docs.cloud.google.com/sdk/docs/install-sdk#initializing_the) the gcloud CLI for use with your project.




## Prepare your clusters

Before applications in your fleet can receive a federated identity, the clusters that they run on must be [registered to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) and properly configured to use fleet Workload Identity Federation. The following sections describe how to set up fleet Workload Identity Federation for different types of clusters.

### GKE

For GKE clusters, do the following:

  1. [Enable Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) on your Google Kubernetes Engine cluster, if it is not already enabled.
  2. [Register the cluster](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke) to the fleet.



You can also enable Workload Identity Federation for GKE during the cluster creation and fleet registration process.

### Clusters outside Google Cloud

The following types of clusters automatically enable fleet Workload Identity Federation and are registered to your fleet during cluster creation:

  * Google Distributed Cloud (software only) on VMware
  * Google Distributed Cloud (software only) on bare metal
  * GKE on AWS
  * GKE on Azure



### Attached clusters

EKS and AKS attached clusters registered using the GKE Multi-Cloud API are registered with fleet Workload Identity Federation enabled by default. [Other attached clusters](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/how-to/attach-kubernetes-clusters) can be registered with fleet Workload Identity Federation enabled if they meet the necessary [requirements](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/before-you-begin#fleet_workload_identity_requirements). Follow the instructions for your cluster type in [Registering a cluster](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/previous-generation/how-to/attach-kubernetes-clusters).

## Use fleet Workload Identity Federation in applications

The following steps show you how to configure a workload in a registered cluster to use fleet Workload Identity Federation:

  1. Find the name of your cluster workload identity pool and identity provider:
         
         gcloud container fleet memberships describe MEMBERSHIP_ID \
             --project=FLEET_PROJECT_ID \
             --format="table(authority.identityProvider,authority.workloadIdentityPool,name)"
         

Replace the following:

     * `MEMBERSHIP_ID`: the cluster [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership). This is often the name of your cluster.
     * `FLEET_PROJECT_ID`: the project ID of the fleet host project.

The output is similar to the following:
    
    IDENTITY_PROVIDER: IDENTITY_PROVIDER
    WORKLOAD_IDENTITY_POOL: WORKLOAD_IDENTITY_POOL
    NAME: projects/FLEET_PROJECT_ID/locations/MEMBERSHIP_LOCATION/memberships/MEMBERSHIP_ID
    

This output contains the following information:

     * `IDENTITY_PROVIDER`: the identity provider for the cluster.
     * `MEMBERSHIP_LOCATION`: the location of the fleet membership. This is usually the same as your cluster location.
     * `WORKLOAD_IDENTITY_POOL`: the name of the [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) associated with your fleet. This value has the syntax `FLEET_PROJECT_ID.svc.id.goog`.
  2. Create a Kubernetes namespace. You can also use any existing namespace, including the `default` namespace.
         
         kubectl create namespace NAMESPACE
         

Replace `NAMESPACE` with the name of the namespace.

  3. Create a new Kubernetes ServiceAccount in the namespace. You can also use any existing ServiceAccount, including the `default` ServiceAccount in the namespace.
         
         kubectl create serviceaccount KUBERNETES_SERVICEACCOUNT \
             --namespace=NAMESPACE
         

Replace `KUBERNETES_SERVICEACCOUNT` with the name of the ServiceAccount.

  4. Save the following manifest as `adc-config-map.yaml`. This ConfigMap contains the ADC configuration for workloads.
         
         kind: ConfigMap
         apiVersion: v1
         metadata:
           namespace: NAMESPACE
           name: my-cloudsdk-config
         data:
           config: |
             {
               "type": "external_account",
               "audience": "identitynamespace:WORKLOAD_IDENTITY_POOL:IDENTITY_PROVIDER",
               "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
               "token_url": "https://sts.googleapis.com/v1/token",
               "credential_source": {
                 "file": "/var/run/secrets/tokens/gcp-ksa/token"
               }
             }
         

  5. Deploy the ConfigMap:
         
         kubectl create -f adc-config-map.yaml
         

  6. Save the following manifest as `workload-config.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-pod
           namespace:  NAMESPACE
         spec:
           serviceAccountName: KUBERNETES_SERVICEACCOUNT
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
                   audience: WORKLOAD_IDENTITY_POOL
                   expirationSeconds: 172800
               - configMap:
                   name: my-cloudsdk-config
                   optional: false
                   items:
                   - key: "config"
                     path: "google-application-credentials.json"
         

When you deploy this workload, the `gcp-ksa` volume in the Pod contains the following data:

     * The data in the ConfigMap that you deployed as a file named `google-application-credentials.json`. This file is an [ADC credential configuration file](https://docs.cloud.google.com/docs/authentication/application-default-credentials#GAC).
     * The Kubernetes ServiceAccount token as `token`. Kubernetes mounts a signed JWT for the ServiceAccount as a [projected ServiceAccount token file](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection).

The container in the Pod mounts the `gcp-ksa` volume to the `/var/run/secrets/tokens/gcp-ksa` path and configures ADC to look for the credential configuration JSON file in that path.

  7. Deploy the workload:
         
         kubectl apply -f workload-config.yaml
         




### Alternative: Impersonate an IAM service account

Alternatively, you can configure Kubernetes ServiceAccounts in your clusters to impersonate IAM service accounts and perform any authorized actions that the IAM service accounts can perform. This approach might increase maintenance overhead, because you have to manage pairings of service accounts in both IAM and Kubernetes.

In most scenarios, we recommend that you directly reference Kubernetes principals in IAM allow policies to grant access to Google Cloud resources by following the instructions in Use fleet Workload Identity Federation in applications.

  1. Find the name of your cluster workload identity pool and identity provider:
         
         gcloud container fleet memberships describe MEMBERSHIP_ID \
             --project=FLEET_PROJECT_ID \
             --format="table(authority.identityProvider,authority.workloadIdentityPool,name)"
         

Replace the following:

     * `MEMBERSHIP_ID`: the cluster [membership name](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership). This is often the name of your cluster.
     * `FLEET_PROJECT_ID`: the project ID of the fleet host project.

The output is similar to the following:
    
    IDENTITY_PROVIDER: IDENTITY_PROVIDER
    WORKLOAD_IDENTITY_POOL: WORKLOAD_IDENTITY_POOL
    NAME: projects/FLEET_PROJECT_ID/locations/MEMBERSHIP_LOCATION/memberships/MEMBERSHIP_ID
    

This output contains the following information:

     * `IDENTITY_PROVIDER`: the identity provider for the cluster.
     * `MEMBERSHIP_LOCATION`: the location of the membership. This is usually the same as your cluster location.
     * `WORKLOAD_IDENTITY_POOL`: the name of the [workload identity pool](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools) associated with your fleet. This value has the syntax `FLEET_PROJECT_ID.svc.id.goog`.
  2. Create an IAM service account that your application can impersonate. You can also use any existing IAM service account.
         
         gcloud iam service-accounts create IAM_SA_NAME \
             --project=IAM_SA_PROJECT_ID
         

Replace the following:

     * `IAM_SA_NAME`: the name for your IAM service account.
     * `IAM_SA_PROJECT_ID`: the project ID of the project that contains your IAM service account. This can be different than your fleet host project.
  3. Grant the IAM service account any permissions that it needs to access Google Cloud APIs by adding the necessary IAM allow policies. You can do this by using [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) or [another method](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You can find out which permissions are required to use Google Cloud APIs in each service's documentation, and see a complete list of predefined roles with the necessary permissions in [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  4. Create a Kubernetes ServiceAccount in a namespace. You can also use an existing Kubernetes ServiceAccount and any namespace, including the `default` ServiceAccount and the `default` namespace.
         
         kubectl create serviceaccount KUBERNETES_SERVICEACCOUNT \
             --namespace=NAMESPACE
         

Replace the following:

     * `KUBERNETES_SERVICEACCOUNT`: the name of the ServiceAccount.
     * `NAMESPACE`: the name of the namespace.
  5. Create an IAM allow policy that lets a Kubernetes ServiceAccount in a specific namespace in your cluster impersonate the IAM service account:
         
         gcloud iam service-accounts add-iam-policy-binding IAM_SA_NAME@IAM_SA_PROJECT_ID.iam.gserviceaccount.com \
             --project=IAM_SA_PROJECT_ID \
             --role=roles/iam.workloadIdentityUser \
             --member="serviceAccount:WORKLOAD_IDENTITY_POOL[NAMESPACE/KUBERNETES_SERVICEACCOUNT]"
         

Replace `WORKLOAD_IDENTITY_POOL` with the name of the workload identity pool.

  6. Save the following manifest as `adc-config-map.yaml`. This ConfigMap contains the ADC configuration for workloads.
         
         kind: ConfigMap
         apiVersion: v1
         metadata:
           namespace: NAMESPACE
           name: my-cloudsdk-config
         data:
           config: |
             {
               "type": "external_account",
               "audience": "identitynamespace:WORKLOAD_IDENTITY_POOL:IDENTITY_PROVIDER",
               "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/IAM_SA_NAME@IAM_SA_PROJECT_ID.iam.gserviceaccount.com:generateAccessToken",
               "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
               "token_url": "https://sts.googleapis.com/v1/token",
               "credential_source": {
                 "file": "/var/run/secrets/tokens/gcp-ksa/token"
               }
             }
         

Replace the following:

     * `IAM_SA_NAME`: the name of the IAM service account to impersonate.
     * `IAM_SA_PROJECT_ID`: the project ID of the IAM service account.
  7. Save the following manifest as `workload-config.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: my-pod
           namespace:  NAMESPACE
         spec:
           serviceAccountName: KUBERNETES_SERVICEACCOUNT
           containers:
           - name: my-container
             image: my-image
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
                   audience: WORKLOAD_IDENTITY_POOL
                   expirationSeconds: 172800
               - configMap:
                   name: my-cloudsdk-config
                   optional: false
                   items:
                     - key: "config"
                       path: "google-application-credentials.json"
         
         

When you deploy this workload, the `gcp-ksa` volume in the Pod contains the following data:

     * The data in the ConfigMap that you deployed as a file named `google-application-credentials.json`. This file is an [ADC credential configuration file](https://docs.cloud.google.com/docs/authentication/application-default-credentials#GAC).
     * The Kubernetes ServiceAccount token as `token`. Kubernetes mounts a signed JWT for the ServiceAccount as a [projected ServiceAccount token file](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#service-account-token-volume-projection).

The container in the Pod mounts the `gcp-ksa` volume to the `/var/run/secrets/tokens/gcp-ksa` path and configures ADC to look for the credential configuration JSON file in that path.

  8. Deploy the workload:
         
         kubectl apply -f workload-config.yaml
         




## Verify the fleet Workload Identity Federation setup

In this section, you create a Cloud Storage bucket and access it from a Pod that uses fleet Workload Identity Federation. Before you perform these steps, ensure that you configured Workload Identity Federation by following the instructions in the Use fleet Workload Identity Federation in applications section.

This section doesn't show you how to verify Workload Identity Federation using the IAM service account impersonation method.

  1. Find your numerical project number:
         
         gcloud projects describe FLEET_PROJECT_ID \
             --format="value(projectNumber)"
         

The output is similar to the following:
         
         1234567890
         

  2. Create a Cloud Storage bucket:
         
         gcloud storage buckets create gs://FLEET_PROJECT_ID-test-bucket \
             --location=LOCATION
         

Replace `LOCATION` with a Google Cloud location.

  3. Create an IAM allow policy that grants access on the bucket to the service account that you created:
         
         gcloud storage buckets add-iam-policy-binding gs://FLEET_PROJECT_ID-test-bucket \
             --condition=None \
             --role=roles/storage.objectViewer \
             --member=principal://iam.googleapis.com/projects/FLEET_PROJECT_NUMBER/locations/global/workloadIdentityPools/FLEET_PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT
         

Replace the following:

     * `FLEET_PROJECT_NUMBER`: your numerical project number.
     * `FLEET_PROJECT_ID`: your project ID.
     * `NAMESPACE`: the name of the Kubernetes namespace that runs your Pod from the previous section.
     * `KUBERNETES_SERVICEACCOUNT`: the name of the Kubernetes ServiceAccount that your Pod from the previous section uses.
**Best practice:** Create IAM allow policies that give the least amount of permissions on the specific resource that the workload needs to access. 
  4. Create a shell session in your Pod:
         
         kubectl exec -it pods/my-pod --namespace=NAMESPACE -- /bin/bash
         

  5. Try to list the objects in the bucket:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/FLEET_PROJECT_ID-test-bucket/o"
         

The output is the following:
         
         {
           "kind": "storage#objects"
         }
         




## Authenticate from your code

When you use [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained), authentication libraries automatically use ADC to look for credentials to authenticate to Google Cloud services. You must use Cloud Client Libraries that support Workload Identity Federation. The following shows the minimum required Cloud Client Libraries versions, as well as instructions for how to check your current version:

### C++

Most of the [Google Cloud Client Libraries for C++](https://github.com/googleapis/google-cloud-cpp) support identity federation by using a `ChannelCredentials` object, which is created by calling `grpc::GoogleDefaultCredentials()`. To initialize this credential, you must build the client libraries with version 1.36.0 or later of [gRPC](https://github.com/grpc/grpc).

The Cloud Storage Client Library for C++ uses the REST API, not gRPC, so it does not support identity federation.

### Go

Client libraries for Go support identity federation if they use version v0.0.0-20210218202405-ba52d332ba99 or later of the `golang.org/x/oauth2` module.

To check which version of this module your client library uses, run the following commands:
    
    
    cd $GOPATH/src/cloud.google.com/go
    go list -m golang.org/x/oauth2
    

### Java

Client libraries for Java support identity federation if they use version 0.24.0 or later of the [`com.google.auth:google-auth-library-oauth2-http` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).

To check which version of this artifact your client library uses, run the following Maven command in your application directory:
    
    
    mvn dependency:list -DincludeArtifactIds=google-auth-library-oauth2-http
    

### Node.js

Client libraries for Node.js support identity federation if they use version 7.0.2 or later of the [`google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs).

To check which version of this package your client library uses, run the following command in your application directory:
    
    
    npm list google-auth-library
    

When you create a `GoogleAuth` object, you can specify a project ID, or you can allow `GoogleAuth` to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [`README` for the `google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs#using-external-identities).

### Python

Client libraries for Python support identity federation if they use version 1.27.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).

To check which version of this package your client library uses, run the following command in the environment where the package is installed:
    
    
    pip show google-auth
    

To specify a project ID for the authentication client, you can set the `GOOGLE_CLOUD_PROJECT` environment variable, or you can allow the client to find the project ID automatically. To find the project ID automatically, the service account in the configuration file must have the Browser role (`roles/browser`), or a role with equivalent permissions, on your project. For details, see the [user guide for the `google-auth` package](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-auth/docs/user-guide.rst#using-external-identities).

## What's next?

Learn [best practices](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/best-practices-workload-identity) for organizing your fleets when using fleet Workload Identity Federation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
