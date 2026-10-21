---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template/
title: Quickstart: Create a Managed Service for Apache Spark cluster by using a template \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:23.474084+00:00
---

# Quickstart: Create a Managed Service for Apache Spark cluster by using a template  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a cluster by using a template

This page shows you how to use an inline [Google APIs Explorer](https://developers.google.com/apis-explorer/#p/) template to create a Managed Service for Apache Spark cluster.

For other ways to create a cluster, see:

  * [Create a cluster by using the Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console#create_a_cluster)
  * [Create a cluster by using the Google Cloud CLI](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud#create_a_cluster)
  * [Create a cluster by using client libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries)



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. Verify that you have the permissions required to complete this guide. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. Verify that you have the permissions required to complete this guide. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Dataproc API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataproc.googleapis.com)




### Required roles

Certain IAM roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects,folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) IAM role to the Compute Engine default service account on the project. **Important:** You must grant this role to the Compute Engine default service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors. 

## Create a cluster

Before you can run Managed Service for Apache Spark jobs, you need to create a cluster of virtual machines to run them on. To create a Managed Service for Apache Spark cluster in your project, fill in and execute the Google APIs Explorer **Try this Method** template on this page (scroll or click **Try it!** to move to the template).

**Note:** The `region` and `clusterName` parameter values are filled in for you. Accept or replace these "seeded" parameter values.

  1. **Request parameters:**

     1. Insert your [**projectId**](https://console.cloud.google.com/).
     2. Specify the [**region**](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) where your cluster will be located (accept or replace "us-central1"). Since you are not specifying a zone within the region in this quickstart, [Managed Service for Apache Spark Auto Zone placement](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/auto-zone) will pick a zone within the region where it will create the cluster.
  2. **Request body:**

     1. Specify a [**clusterName**](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters#Cluster.FIELDS.cluster_name), (accept or replace "example-cluster"). You will use this name to interact with your cluster, for example when you [submit jobs](https://docs.cloud.google.com/managed-spark/docs/quickstarts/submit-spark-job-template) or [update the cluster](https://docs.cloud.google.com/managed-spark/docs/quickstarts/update-cluster-template).
  3. Click **EXECUTE**. The first time you run the API template, you may be asked to choose and sign into your Google account, then authorize the Google APIs Explorer to access your account. If the request is successful, the JSON response shows that cluster creation is pending.

  4. To confirm cluster creation, open the [Managed Service for Apache Spark Clusters](https://console.cloud.google.com/dataproc/clusters) page in the Google Cloud console. After cluster provisioning completes, the cluster's status will show as "Running".




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. If you don't need the cluster to explore the other quickstarts or to run other jobs, use the [APIs Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/quickstart-explorer-delete), the [Google Cloud console](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console#clean-up), the gcloud CLI [gcloud](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud#clean-up) command-line tool, or the [Cloud Client Libraries](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-client-libraries) to delete the cluster.



## What's next

  * Learn how to [submit a Spark job by using a template](https://docs.cloud.google.com/managed-spark/docs/quickstarts/submit-spark-job-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
