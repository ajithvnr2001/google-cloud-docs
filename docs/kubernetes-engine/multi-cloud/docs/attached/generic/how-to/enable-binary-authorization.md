---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/enable-binary-authorization/
title: Enable Binary Authorization \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:57.643266+00:00
---

# Enable Binary Authorization  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/enable-binary-authorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/concepts/overview)



Send feedback 

#  Enable Binary Authorization Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Starting with Kubernetes version 1.28, manual policy binding to authorize the service account for Binary Authorization is no longer necessary. The required permissions are now automatically granted to this service account. You can therefore disregard step 2 in the following instructions.

To enable Binary Authorization for GKE attached clusters, perform the following steps:

  1. Enable the Binary Authorization API in your project:
         
         gcloud services enable binaryauthorization.googleapis.com \
           --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  2. Grant the `binaryauthorization.policyEvaluator` role to the Kubernetes service account associated with the Binary Authorization agent:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member=serviceAccount:PROJECT_ID.svc.id.goog[gke-system/binauthz-agent] \
           --role="roles/binaryauthorization.policyEvaluator"
         

  3. Enable Binary Authorization when registering or updating a cluster.

###  Register a cluster 

To enable Binary Authorization when registering a cluster, use the [`gcloud container attached clusters register` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register). Follow the instructions in [attach your CNCF conformant cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/attach-cluster), and include the optional argument `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE`:
         
         gcloud container attached clusters register CLUSTER_NAME \
           ...
           --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
         

Replace `CLUSTER_NAME` with the name of your cluster.

###  Update a cluster 

To enable Binary Authorization when updating a cluster, use the [`gcloud container attached clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update). Follow the instructions in [update your CNCF conformant cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/update-cluster), and include the optional argument `--binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE`:
         
         gcloud container attached clusters update CLUSTER_NAME \
           ...
           --binauthz-evaluation-mode=PROJECT_SINGLETON_POLICY_ENFORCE
         

Replace `CLUSTER_NAME` with the name of your cluster.




By following these steps, you ensure that only trusted and verified images are used to create Kubernetes containers in your GKE clusters. This helps to maintain a secure environment for your applications.

## Configure policies

Enabling Binary Authorization alone doesn't automatically protect your cluster. By default, it allows all container images to be deployed if no policy is configured. This means that to effectively secure your cluster, you need to define and enforce a policy that specifies which images are allowed. To learn how to configure a Binary Authorization policy, see [Configure a policy using the Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
