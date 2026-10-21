---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/scalability/
title: Troubleshooting scalability in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:51:43.553247+00:00
---

# Troubleshooting scalability in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/scalability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting scalability in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

High usage of the etcd database can cause cluster instability and resource shortages that prevent your Google Kubernetes Engine (GKE) clusters from scaling effectively.

Use this document to learn how to identify clusters where etcd usage is approaching its limit and find recommendations to free up space, helping to ensure that your cluster remains stable.

This information is important for Platform admins and operators responsible for maintaining the health and scalability of GKE clusters. For more information about the common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This document covers troubleshooting cluster stability related to high etcd usage. If you experience a different scalability problem, one of the following documents might help:

  * **Cluster autoscaler issues** :

    * For troubleshooting why new nodes aren't being added, see [Troubleshoot cluster autoscaler not scaling up](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-up).
    * For troubleshooting why underutilized nodes aren't being removed, see [Troubleshoot cluster autoscaler not scaling down](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/cluster-autoscaler-scale-down).
  * **Horizontal Pod Autoscaler issues** : for troubleshooting why your Horizontal Pod Autoscaler isn't working, see [Troubleshoot horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/horizontal-pod-autoscaling).

  * **Autopilot scaling issues** : for more information about Autopilot-specific issues, including those related to scaling, see [Troubleshoot Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/autopilot-clusters).




## Identify clusters where etcd usage is approaching the limit

GKE provides insights and recommendations for the scenario where etcd usage is approaching the limit. You can find these insights and recommendations in the following ways:

  * Use the Google Cloud console. Go to the [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list) page. In the **Notifications** column for specific clusters, check for the **Free up space to reduce risk of cluster instability** recommendation.
  * Use the gcloud CLI or Recommender API by specifying the `ETCD_DB_USAGE_APPROACHING_LIMIT` recommender subtype.

To query for this recommendation, run the following command:
        
        gcloud recommender recommendations list \
            --recommender=google.container.DiagnosisRecommender \
            --location=LOCATION \
            --project=PROJECT_ID \
            --format=yaml \
            --filter="recommenderSubtype:ETCD_DB_USAGE_APPROACHING_LIMIT"
        


**Note:** This recommendation might take up to 24 hours to appear. For detailed instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation, remove any unnecessary data from etcd to free up space. This might involve deleting old resources or moving large objects out of etcd. For more information, see [Plan for large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters).

## Identify clusters where storage usage per object type is approaching the limit

GKE provides insights and recommendations for the scenario where total size of etcd objects per type is approaching the [limit](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters). You can find these insights and recommendations in the following ways:

  * Use the Google Cloud console. Go to the [Kubernetes clusters](https://console.cloud.google.com/kubernetes/list) page. In the **Notifications** column for specific clusters, check for the **Reduce the size of resource type(s)** recommendation.
  * Use the gcloud CLI or Recommender API by specifying the `APISERVER_RESOURCE_TYPE_SIZE_EXCEEDS_LIMIT` recommender subtype.

To query for this recommendation, run the following command:
        
        gcloud recommender recommendations list \
            --recommender=google.container.DiagnosisRecommender \
            --location=LOCATION \
            --project=PROJECT_ID \
            --format=yaml \
            --filter="recommenderSubtype:APISERVER_RESOURCE_TYPE_SIZE_EXCEEDS_LIMIT"
        

To decide which objects to remove, you can use kubectl to list them. For example, if ConfigMaps are nearing the storage limit, the following command will output all ConfigMaps across all namespaces, helping you identify candidates for deletion:
        
        kubectl get configmaps --all-namespaces > new_file.txt
        


**Note:** This recommendation might take up to five hours to appear. For detailed instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation and free up space, remove any unnecessary objects of the specified types from storage. This process might involve deleting old resources or moving large objects out of storage. For more information, see [Plan for large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#limits-best-practices-large-scale-clusters).

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
