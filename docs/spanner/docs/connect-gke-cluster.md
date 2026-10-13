---
url: https://docs.cloud.google.com/spanner/docs/connect-gke-cluster/
title: Connect Spanner with a GKE cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:32.634626+00:00
---

# Connect Spanner with a GKE cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/connect-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Connect Spanner with a GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant your [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) cluster permissions to access your Spanner database.

GKE is a managed Kubernetes service that makes it easy to deploy and manage containerized applications. By using GKE and Spanner together, you can take advantage of scalability, reliability, security, and high availability in your application layer and in your database layer.

Your GKE cluster can access the Spanner API through [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity). Workload Identity Federation for GKE allows a Kubernetes service account in your cluster to act as an IAM service account. The IAM service account provides [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) for your pods, so that you don't need to configure each pod to use your personal user credential.

After you configure your applications to authenticate using Workload Identity Federation for GKE, you can use [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries) to query your Spanner databases. You can also [migrate your applications to your GKE node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).

To create a connection in a sample environment, try the [Connecting Spanner with GKE Autopilot codelab](https://codelabs.developers.google.com/codelabs/cloud-spanner-gke-autopilot).

## Enable Workload Identity Federation for GKE

If you haven't done so already, enable Workload Identity Federation for GKE for your GKE cluster. You can enable Workload Identity Federation for GKE on a new cluster by creating a [new node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable_on_cluster) or you can enable Workload Identity Federation for GKE on an [existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable-existing-cluster). [GKE autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) have Workload Identity Federation for GKE enabled by default. For more information, see [Enable Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable).

## Authenticate connection to Spanner with Workload Identity Federation for GKE

Configure your applications to authenticate to Google Cloud by using Workload Identity Federation for GKE.

  1. Ensure that your GKE Pod uses a Kubernetes `ServiceAccount` object, as described in [Configure authorization and principals](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#configure-authz-principals).

  2. Create an IAM allow policy that grants the necessary Spanner IAM roles to the Kubernetes `ServiceAccount` object. The following example grants the Spanner Database User (`roles/spanner.databaseUser`) role:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
               --member="principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/PROJECT_ID.svc.id.goog/subject/ns/NAMESPACE/sa/KSA_NAME \
               --role=roles/spanner.databaseUser \
               --condition=None
         

Replace the following:

     * `PROJECT_ID`: The project ID of the GKE cluster.
     * `PROJECT_NUMBER`: The numerical Google Cloud project number.
     * `NAMESPACE`: The Kubernetes namespace that contains the ServiceAccount.
     * `KSA_NAME`: The name of the ServiceAccount.



## Connect Spanner databases

After your application Pod is authenticated, you can use one of the [Spanner client libraries](https://docs.cloud.google.com/spanner/docs/reference/libraries) to query your Spanner database.

## What's next

  * Learn how to [deploy your application to the GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster).
  * Learn how to [deploy your application using GKE Autopilot and Spanner](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gke-spanner-integration).
  * Learn more about how to [migrate existing workloads to Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).
  * Learn more about [SQL best practices](https://docs.cloud.google.com/spanner/docs/sql-best-practices).
  * Integrate Spanner with other ORMs including [Hibernate ORM](https://docs.cloud.google.com/spanner/docs/use-hibernate), [gorm](https://docs.cloud.google.com/spanner/docs/use-gorm), and [Django ORM](https://docs.cloud.google.com/spanner/docs/django-orm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
