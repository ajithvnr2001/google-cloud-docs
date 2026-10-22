---
url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install/
title: Install the Apigee Operator for Kubernetes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:58.250773+00:00
---

# Install the Apigee Operator for Kubernetes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Install the Apigee Operator for Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes the steps to install and configure the Apigee Operator for Kubernetes. To learn more about the benefits of using the Apigee Operator for Kubernetes, see [ Apigee Operator for Kubernetes overview](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-install).

## Before you begin

Before you install the Apigee Operator for Kubernetes, ensure that you have the required roles and permissions to complete the steps and that you have completed the prerequisite tasks described in [Apigee Operator for Kubernetes: Before you begin](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-before-you-begin).

### Required roles

To get the permissions that you need to install the Apigee Operator for Kubernetes, ask your administrator to grant you the following IAM roles on the organization: 

  * Create and manage the GKE cluster: [Container Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`) 
  * Create and manage service accounts: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) 
  * Create and manage service extensions: [Service Extensions Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.serviceExtensionsAdmin) (`roles/networkservices.serviceExtensionsAdmin`) 
  * Create and manage network endpoint groups (NEGs): [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`) 
  * Create and manage backend services: [Compute Load Balancer Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`) 
  * Create and manage Apigee resources: [Apigee Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Install and configure the Apigee Operator for Kubernetes

The following sections describe the steps to install and configure the Apigee Operator for Kubernetes: 

  1. Set environment variables.
  2. Enable the required APIs.
  3. Retrieve and configure credentials.
  4. Create a workload identity.
  5. Install the Apigee Operator for Kubernetes.
  6. Create an Apigee environment.
  7. Verify GKE Gateway setup.



### Set environment variables

In the Google Cloud project that contains your Apigee instance, use the following command to set environment variables: 
    
    
    export PROJECT_ID=PROJECT_ID
    export CLUSTER_NAME=CLUSTER_NAME
    export REGION=REGION
    export APIGEE_ORG=APIGEE_ORG

Where: 

  * `PROJECT_ID` is the ID of the project with your Apigee instance.
  * `CLUSTER_NAME` is the name of your GKE cluster.
  * `REGION` is the region of your GKE cluster.
  * `APIGEE_ORG` is set to the same value as `PROJECT_ID`.



To confirm that the environment variables are set correctly, run the following command: 
    
    
    echo $PROJECT_ID $CLUSTER_NAME $REGION $APIGEE_ORG

### Enable required APIs

Apigee Operator for Kubernetes requires access to the following APIs: 

Name | Title  
---|---  
`apigee.googleapis.com` | [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)  
`compute.googleapis.com` | [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest)  
`networkservices.googleapis.com` | [Network Services API](https://docs.cloud.google.com/service-extensions/docs/reference/rest)  
`container.googleapis.com` | [Kubernetes Engine API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest)  
  
Use the following command to confirm that the required APIs are enabled: 
    
    
    gcloud services list --project=$PROJECT_ID

If you don't see the required APIs listed in the command output, enable them: 
    
    
    gcloud services enable apigee.googleapis.com --project=$PROJECT_ID
    gcloud services enable compute.googleapis.com --project=$PROJECT_ID
    gcloud services enable networkservices.googleapis.com --project=$PROJECT_ID
    gcloud services enable container.googleapis.com --project=$PROJECT_ID

### Retrieve and configure credentials

Retrieve your cluster credentials and create a service account to connect to Google Cloud services: 

  1. Get cluster credentials using the following command: 
         
         gcloud container clusters get-credentials $CLUSTER_NAME --location=$REGION --project=$PROJECT_ID

These credentials communicate with the GKE cluster created in the prerequisite steps.

  2. Set up Service Account Credentials to connect to Google Cloud services: 
         
         gcloud iam service-accounts create apigee-apim-gsa

  3. Grant the required roles and permissions to the service account you created using the following commands: 
     * **Apigee Admin role** : Required to create and manage Apigee resources. 
           
           gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/apigee.admin"

     * **Service extension admin role** : Required to create and manage service extensions. 
           
           gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/networkservices.serviceExtensionsAdmin"

     * **Networking admin role** : Required to manage access to Apigee using service extensions. 
           
           gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/compute.networkAdmin"

     * **Load balancer admin role** : Required to manage access between network endpoint groups (NEGs) and backend services. 
           
           gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/compute.loadBalancerAdmin"
           
           gcloud projects add-iam-policy-binding $PROJECT_ID \
               --member "serviceAccount:apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com" \
               --role "roles/iam.workloadIdentityUser"




### Create a workload identity

The `helm` installation of the Apigee Operator for Kubernetes in the next step creates a required Kubernetes service account (KSA) named `apim-ksa` in the `apim` namespace. When created, the KSA contains the annotation required to associate with a workload identity used by the Apigee Operator for Kubernetes to access required Apigee and Service Networking resources.

To create the workload identity, use the following command: 
    
    
    gcloud iam service-accounts add-iam-policy-binding apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com --role roles/iam.workloadIdentityUser --member "serviceAccount:$PROJECT_ID.svc.id.goog[apim/apim-ksa]"

This command binds the KSA with the Google service account you created in Retrieve and configure credentials and assigns the `workloadIdentityUser` role.

It may take a few minutes, potentially 7 minutes or longer, for the workload identity changes to propagate through the system. You will verify this identity in a later step after the operator is installed.

### Install Custom Resource Definitions (CRDs) and Apigee Operator for Kubernetes

Install the [Kubernetes Custom Resource Definitions (CRDs)](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/#customresourcedefinitions) and Apigee Operator for Kubernetes: 

  1. Create a namespace for the Apigee Operator for Kubernetes: 
         
         kubectl create ns apim

  2. Install the Apigee Operator for Kubernetes CRDs: 
         
         helm install apigee-apim-crds -n apim \
           oci://us-docker.pkg.dev/apigee-release/apigee-k8s-tooling-helm-charts/apigee-apim-operator-crds \
           --version 1.1.1 \
           --atomic

  3. Install the Apigee Operator for Kubernetes: 
         
         helm install apigee-apim-operator -n apim \
           oci://us-docker.pkg.dev/apigee-release/apigee-k8s-tooling-helm-charts/apigee-apim-operator-helm \
           --version 1.1.1 \
           --set projectId=$PROJECT_ID \
           --set serviceAccount=apigee-apim-gsa@$PROJECT_ID.iam.gserviceaccount.com \
           --set apigeeOrg=$PROJECT_ID \
           --set generateEnv=ENV_GENERATION_MODE \
           --atomic

Replace `ENV_GENERATION_MODE` with `TRUE` if you want the operator to create a new Apigee environment when the Apigee Operator for Kubernetes is installed. Set `ENV_GENERATION_MODE` to `FALSE` if you want to create the environment manually after the operator is installed. See Create an Apigee environment for more information.

  4. Confirm that the installation completed successfully: 
         
         helm list -n apim

The output should look similar to the following: 
         
         NAME                  NAMESPACE REVISION  UPDATED                                 STATUS    CHART                           APP VERSION
         apigee-apim-crds      apim      1         2025-02-01 00:17:03.399810627 +0000 UTC deployed  apigee-apim-operator-crds-1.1.1 1.1.1
         apigee-apim-operator  apim      1         2025-02-01 00:15:00.362829981 +0000 UTC deployed  apigee-apim-operator-helm-1.1.1 1.1.1   

  5. Confirm that the KSA was created with the required annotation: 
         
         kubectl describe serviceaccounts apim-ksa -n apim

The output should look similar to the following: 
         
         Name:                apim-ksa
         Namespace:           apim
         ...
         Annotations:         iam.gke.io/gcp-service-account: apigee-apim-gsa@**my-project-id**.iam.gserviceaccount.com

  6. Confirm that the APIM operator is up and running in the cluster's pods: 
         
         kubectl get pods -n apim

The output should look similar to the following: 
         
         NAME                                    READY   STATUS    RESTARTS     AGE
         apigee-apim-operator-8559d4994b-h55fl   1/1     Running   0            8m34s
         

If the `STATUS` is not `Running`, or `READY` does not display `1/1`, see [Troubleshoot the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot) to troubleshoot the installation.

  7. To confirm that the workload identity is correctly configured, use the following commands: 
         
         gcloud config set project $PROJECT_ID
         
         kubectl run --rm -it --image google/cloud-sdk:slim \
           --namespace apim workload-identity-test \
           --overrides='{ "spec": { "serviceAccountName": "apim-ksa" } }'  \
           -- gcloud auth list

The output should look similar to the following: 
         
         Credentialed Accounts
           ACTIVE  ACCOUNT
           *       GSA@$PROJECT_ID.iam.gserviceaccount.com




### Create an Apigee environment

If you installed the Apigee Operator for Kubernetes using `generateEnv=TRUE` in the previous step, the operator creates a new Apigee environment when the [APIM Extension policy is created and applied](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-create#create-apim-policy). The new environment's name has the prefix: `apim-enabled-dep-env`.

If you installed the Apigee Operator for Kubernetes with `generateEnv=FALSE`, you must create a new Apigee environment: 

  1. Set the `TOKEN` required for the `curl` command: 
         
         export TOKEN=$(gcloud auth print-access-token)

  2. Create the environment using one of the following commands: 
     * For Subscription 2021 and 2024 organizations: 
           
           curl -i -X POST "https://apigee.googleapis.com/v1/organizations/$APIGEE_ORG/environments" -H \
             "Authorization: Bearer $TOKEN" -H "Content-Type:application/json" \
               -d '{
                 "name": "ENV_NAME",
                 "displayName": "ENV_NAME",
                 "state": "ACTIVE",
                 "deploymentType": "PROXY",
                 "apiProxyType": "PROGRAMMABLE",
                 "properties": {
                   "property": [
                     {
                       "name": "apigee-service-extension-enabled",
                       "value": "true"
                     }
                   ]
                 }
             }'

Where `ENV_NAME` is the name of the environment to create.

     * For Pay-as-you-go orgs: 
           
           curl -i -X POST -H "Authorization: Bearer $TOKEN"  "https://apigee.googleapis.com/v1/organizations/$APIGEE_ORG/environments" -H "Content-Type:application/json" -d '{
             "name": "ENV_NAME",
             "displayName": "ENV_NAME",
             "state": "ACTIVE",
             "deploymentType": "PROXY",
             "apiProxyType": "PROGRAMMABLE",
             "type" : "COMPREHENSIVE",
             "properties": {
               "property": [
                 {
                   "name": "apigee-service-extension-enabled",
                   "value": "true"
                 }
               ]
             }
           }'

Where: 

       * `ENV_NAME` is the name of the environment to create.
**Note** : The environment created in this step, or created by the Apigee Operator for Kubernetes, is either an [Intermediate or Comprehensive](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#environment-types) environment, to support the use of [Extensible proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types). This feature cannot be used with Base environments.

To check that the environment created successfully: 
    
    curl -i -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/$APIGEE_ORG/environments"

  3. Attach the environment to your Apigee instance: 
         
         curl -i -X POST -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/$APIGEE_ORG/instances/INSTANCE_NAME/attachments" \
           -H "Content-Type:application/json" -d '{"environment": "ENV_NAME"}'

Where: 

     * `INSTANCE_NAME` is the name of your Apigee instance.
     * `ENV_NAME` is the name of the environment you created in the previous step.

To check the status of the environment attachment operation: 
    
    curl -X GET -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/$APIGEE_ORG/operations/OPERATION_ID"

Where `OPERATION_ID` is the ID of the environment attachment operation.




## Troubleshoot

If you encounter issues when installing Apigee Operator for Kubernetes, see [Troubleshoot the Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-troubleshoot) for solutions to common errors.

## What's next

Create a traffic service extension using the `APIMExtensionPolicy` or the `ApigeeBackendService`: 

  * [Create an `APIMExtensionPolicy`](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apimextension)
  * [Create an `ApigeeBackendService`](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-apigeebackendservice)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
