---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/managed-service-prometheus/
title: Set up managed data collection with Managed Service for Prometheus \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:08.880204+00:00
---

# Set up managed data collection with Managed Service for Prometheus  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/managed-service-prometheus/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Set up managed data collection with Managed Service for Prometheus Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can set up managed data collection with [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) for GKE on AWS. This feature is available on AWS clusters running Kubernetes version 1.25 or later. It is also supported on Kubernetes clusters at version 1.24 for customers who had earlier signed up for a preview of this feature on that version.

With this feature, you can use a PodMonitoring resource to choose the metrics that you want to ingest into Cloud Monitoring. You can then view these metrics in the Google Cloud console.

## Limitations

  * This feature is not available on Kubernetes clusters earlier than version 1.24.


  * This feature requires a Linux workload.



## Set up managed data collection

To set up managed data collection with Managed Service for Prometheus, complete the following steps:

**Note:** Starting with Kubernetes version 1.28, manual policy binding to authorize service accounts for data collection is no longer necessary. The required permissions are now automatically granted to this service account. You can therefore disregard step 1 in this section.

  1. Authorize the `gmp-system/collector` and `gmp-system/rule-evaluator` service accounts to write your metrics:
         
         gcloud projects add-iam-policy-binding GOOGLE_PROJECT_ID \
               --member="serviceAccount:GOOGLE_PROJECT_ID.svc.id.goog[gmp-system/collector]" \
               --role=roles/monitoring.metricWriter
           gcloud projects add-iam-policy-binding GOOGLE_PROJECT_ID \
               --member="serviceAccount:GOOGLE_PROJECT_ID.svc.id.goog[gmp-system/rule-evaluator]" \
               --role=roles/monitoring.viewer
           gcloud projects add-iam-policy-binding GOOGLE_PROJECT_ID \
               --member="serviceAccount:GOOGLE_PROJECT_ID.svc.id.goog[gmp-system/rule-evaluator]" \
               --role=roles/monitoring.metricWriter
         

Replace `GOOGLE_PROJECT_ID` with your Google Cloud project ID.

Adding this IAM binding fails unless at least one cluster has been created in your Google Cloud project. This is because the workload identity pool it refers to (`GOOGLE_PROJECT_ID.svc.id.goog`) isn't provisioned until cluster creation. 

  2. Create a cluster with the standard `gcloud` [Create your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/create-cluster#create_your_cluster) command, but include the optional `--enable-managed-prometheus` flag. For example:
         
         gcloud container aws clusters create \
              ...
              --enable-managed-prometheus
         

  3. To configure which workload metrics you want to ingest, set up a [PodMonitoring](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.4.3-gke.0/doc/api.md#podmonitoring) resource. For an example, see [Configure a PodMonitoring resource](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-pod-monitoring) in the managed data collection with Managed Service for Prometheus documentation.




After you enable managed data collection with Managed Service for Prometheus, GKE on AWS creates the `gmp-system` namespace. Don't modify or deploy anything in this namespace. GKE on AWS also creates the `gmp-public` namespace. Managed Service for Prometheus uses the `gmp-public` namespace to deploy the [OperatorConfig](https://github.com/GoogleCloudPlatform/prometheus-engine/blob/v0.4.3-gke.0/doc/api.md#operatorconfig) resource.

## Update your Prometheus configuration

To disable or re-enable Prometheus data collection, use the standard `gcloud` [Update your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/update-cluster#update_your_cluster) command, but add a --disable-managed-prometheus or --enable-managed-prometheus optional parameter. For example: 
    
    
      gcloud container aws clusters update \
        ...
        --disable-managed-prometheus
           OR
        --enable-managed-prometheus
    

## What's next

  * Discover how to [Configure a query user interface](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query) in the managed data collection with Managed Service for Prometheus documentation.
  * Learn about [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed) in the Google Cloud Managed Service for Prometheus documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
