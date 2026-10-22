---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/enable-binary-authorization/
title: How to enable Binary Authorization \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:59.139623+00:00
---

# How to enable Binary Authorization  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/enable-binary-authorization/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  How to enable Binary Authorization Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting with GKE on AWS version 1.28, manual policy binding to authorize the service account for Binary Authorization is no longer necessary. The required permissions are now automatically granted to this service account. You can therefore disregard step 2 in the following instructions.

To enable Binary Authorization for GKE on AWS, perform the following steps:

  1. Enable the Binary Authorization API in your project:
         
         gcloud services enable binaryauthorization.googleapis.com \
           --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  2. Grant the `binaryauthorization.policyEvaluator` role to the Kubernetes service account associated with the Binary Authorization agent:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:PROJECT_ID.svc.id.goog[gke-system/binauthz-agent] \
           --role="roles/binaryauthorization.policyEvaluator"
         

  3. Enable Binary Authorization when creating or updating a cluster. Make sure to include the flag `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE` since this flag enables Binary Authorization:

###  Creating a cluster 
         
         gcloud container aws clusters create CLUSTER_NAME \
           --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
         

Replace `CLUSTER_NAME` with the name of your cluster.

###  Updating a cluster 
         
         gcloud container aws clusters update CLUSTER_NAME \
           --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
         

Replace `CLUSTER_NAME` with the name of your cluster.




By following these steps, you ensure that only trusted and verified images are used to create Kubernetes containers in your GKE clusters. This helps to maintain a secure environment for your applications.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
