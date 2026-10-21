---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/workload-identity/
title: Workload identity \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:22.850832+00:00
---

# Workload identity  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/overview)



Send feedback 

#  Workload identity Stay organized with collections  Save and categorize content based on your preferences. 

Workload Identity Federation for GKE (WIF) is a mechanism that lets your cluster's workloads access external cloud resources with Kubernetes service accounts. WIF is the recommended way for applications running within GKE attached clusters to access Google Cloud services. When you register your cluster, the GKE attached clusters API creates all the infrastructure required for WIF, with support for clusters that use either public or private OIDC issuers.

All GKE components that connect back to Google Cloud, such as Connect and telemetry agents, use Workload Identity Federation for GKE.

## Kubernetes service accounts and Workload Identity Federation for GKE

When a Pod runs, it uses a [Kubernetes service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/) to authorize its access to resources hosted within its cluster. By using WIF, the Pod can use the same Kubernetes service account (KSA) to obtain a short-lived token to access resources hosted outside the cluster.

WIF requires a trust relationship between the OIDC identity provider inside the cluster and the external resource provider, such as Google Cloud IAM. When you register an attached cluster, the registration process automatically creates this trust relationship by adding your cluster's OIDC service to the default workload identity pool bound to your Google Cloud project.

This workload identity pool is your Google Cloud project's pool of trusted identity providers and is named `PROJECT_ID.svc.id.goog`, where `PROJECT_ID` is the Google Cloud project ID associated with your attached cluster.

You can use regular IAM policies to control access by Kubernetes service accounts to Google Cloud services. Kubernetes service account principals are the representation of the KSA within the workload identity pool. They're formatted as follows:
    
    
    principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_NAME/subject/ns/KSA_NAMESPACE/sa/KSA_NAME
    

To grant a role to the Kubernetes service account, use the following command:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/KSA_NAMESPACE/sa/KSA_NAME" \
      --role=IAM_ROLE
    

Replace the following:

  * PROJECT_ID: your Google Cloud project ID
  * PROJECT_NUMBER: your Google Cloud project number
  * KSA_NAMESPACE: the cluster namespace that this service account resides in
  * KSA_NAME: the name of the Kubernetes service account you want to grant permissions to
  * IAM_ROLE: the IAM role you want to grant to this KSA



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
