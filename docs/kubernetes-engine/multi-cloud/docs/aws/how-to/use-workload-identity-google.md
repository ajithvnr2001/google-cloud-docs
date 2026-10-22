---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-google/
title: Use workload identity with Google Cloud \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:26.191084+00:00
---

# Use workload identity with Google Cloud  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/use-workload-identity-google/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Use workload identity with Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

_Workload identity_ enables you to assign distinct, fine-grained identities and authorization for each application in your cluster. Workload identity is the recommended way for applications running within GKE on AWS to access Google Cloud services. For more information, see [Workload identity](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/workload-identity).

This topic describes how to use workload identity to connect to Google Cloud services from your workloads.

## Configure IAM permissions

In this section, you give a Kubernetes ServiceAccount permissions to access Google Cloud services by granting it IAM roles.

### Get your workload identity pool and provider

To configure workload identity, you must have the values for your cluster's identity provider URI and [workload identity pools](https://docs.cloud.google.com/iam/docs/workload-identity-federation#pools).

  1. Determine the workload identity pool for your cluster:

All GKE clusters have an identity provider created in the workload identity pool `PROJECT_ID.svc.id.goog`. To get your cluster's identity pool name, use the Google Cloud CLI:
         
         gcloud container aws clusters describe CLUSTER_NAME \
             --location=GOOGLE_CLOUD_LOCATION \
             --format='value(workloadIdentityConfig.workloadPool)'
         

Replace the following:

     * `CLUSTER_NAME` with the name of your cluster.
     * `GOOGLE_CLOUD_LOCATION` with the name of the Google Cloud location that manages your cluster

The output includes the name of your cluster's identity pool. Save this value. You'll need it later.

  2. Determine the identity provider for your cluster.

To find your cluster's identity provider name, use the Google Cloud CLI:
         
         gcloud container aws clusters describe CLUSTER_NAME \
             --location=GOOGLE_CLOUD_LOCATION \
             --format='value(workloadIdentityConfig.identityProvider)'
         

Replace the following:

     * `CLUSTER_NAME`
     * `GOOGLE_CLOUD_LOCATION`

The output includes the name of your cluster's identity provider. Save this value. You'll need it later.




### Grant IAM roles to your Kubernetes ServiceAccount

Grant the IAM role on the project to the Kubernetes ServiceAccount:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT" \
        --role=IAM_ROLE \
        --condition=None
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `PROJECT_NUMBER`: your Google Cloud project number
  * `NAMESPACE`: the Kubernetes namespace for the application
  * `KUBERNETES_SERVICEACCOUNT`: the Kubernetes ServiceAccount to use for the application
  * `IAM_ROLE`: the IAM role to grant to the Kubernetes ServiceAccount



In this example, we will use the role `roles/compute.viewer`, which allows read-only access to compute services:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT" \
        --role=roles/compute.viewer \
        --condition=None
    

## Deploy a sample application

In this section, you deploy a sample application that accesses the Compute Engine API. To use this sample, your Kubernetes ServiceAccount must have the `roles/compute.viewer` IAM role granted to it. To deploy the sample application, follow these steps:

  1. Copy the following manifest into a file named `workload-identity-sample.yaml`:
         
         apiVersion: v1
         kind: Namespace
         metadata:
           name: NAMESPACE
         ---
         apiVersion: v1
         kind: ServiceAccount
         metadata:
           name: KUBERNETES_SERVICEACCOUNT
           namespace: NAMESPACE
         automountServiceAccountToken: false
         ---
         apiVersion: v1
         kind: ConfigMap
         metadata:
           name: cloud-sdk-config
           namespace: NAMESPACE
         data:
           config: |
             {
               "type": "external_account",
               "audience": "identitynamespace:PROJECT_ID.svc.id.goog:IDENTITY_PROVIDER",
               "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
               "token_url": "https://sts.googleapis.com/v1/token",
               "credential_source": {
                 "file": "/var/run/secrets/tokens/gcp-ksa/token"
               }
             }
         ---
         apiVersion: v1
         kind: Pod
         metadata:
           name: cloud-sdk-example
           namespace: NAMESPACE
         spec:
           serviceAccount: KUBERNETES_SERVICEACCOUNT
           containers:
           - name: cloud-sdk
             image: gcr.io/google.com/cloudsdktool/cloud-sdk:latest
             command:
             - /bin/bash
             - -c
             - 'set -eu -o pipefail; while true; do gcloud compute zones list --filter="name ~ us-central1-*"; sleep 5; done'
             env:
             - name: CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE
               value: /var/run/secrets/tokens/gcp-ksa/google-application-credentials.json
             - name: CLOUDSDK_CORE_PROJECT
               value: PROJECT_ID
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
                   audience: PROJECT_ID.svc.id.goog
                   expirationSeconds: 86400
                   path: token
               - configMap:
                   name: cloud-sdk-config
                   optional: false
                   items:
                   - key: config
                     path: google-application-credentials.json
         

Replace the following:

     * `PROJECT_ID`
     * `NAMESPACE`
     * `KUBERNETES_SERVICEACCOUNT`
     * `IDENTITY_PROVIDER` with the name of the identity provider for your cluster.
**Note:** If you are using an application other than Google Cloud CLI, you should set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, rather than `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE`.
  2. Apply the manifest to your cluster
         
         kubectl apply -f workload-identity-sample.yaml
         

  3. Verify the sample application is working, check the Pod's logs:
         
         kubectl logs -f cloud-sdk-example -n NAMESPACE
         

Replace the following:

     * `NAMESPACE`

If the Pod is successful in accessing the Google Cloud compute API, you will see output that looks similar to this:
    
    NAME           REGION       STATUS  NEXT_MAINTENANCE  TURNDOWN_DATE
    us-central1-c  us-central1  UP
    us-central1-a  us-central1  UP
    us-central1-f  us-central1  UP
    us-central1-b  us-central1  UP
    




## Cleaning up

  1. Delete the sample application
         
         kubectl delete -f manifest.yaml
         

  2. Remove the IAM policy binding from the project
         
         gcloud projects remove-iam-policy-binding PROJECT_ID \
             --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KUBERNETES_SERVICEACCOUNT" \
             --role=roles/compute.viewer \
             --condition=None
         

Replace the following:

     * `PROJECT_ID`
     * `PROJECT_NUMBER`
     * `NAMESPACE`
     * `KUBERNETES_SERVICEACCOUNT`



## What's next

  * [Fleet workload identity](https://cloud.google.com/anthos/multicluster-management/fleets/workload-identity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
