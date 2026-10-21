---
url: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console/
title: Quickstart: Create a cluster by using the Google Cloud console \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:22.606355+00:00
---

# Quickstart: Create a cluster by using the Google Cloud console  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-console/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a cluster by using the Google Cloud console

This page shows you how to use the Google Cloud console to create a Managed Service for Apache Spark cluster, run a basic [Apache Spark](http://spark.apache.org/) job in the cluster, and then modify the number of workers in the cluster.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=dataproc--quickstart-dataproc-console)

* * *

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

Certain Identity and Access Management (IAM) roles are required to run the examples on this page. Depending on organization policies, these roles may have already been granted. To check role grants, see [Do you need to grant roles?](https://docs.cloud.google.com/managed-spark/docs/concepts/iam#do_you_need_to_grant_roles).

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### User roles

To get the permissions that you need to create a Managed Service for Apache Spark cluster, ask your administrator to grant you the following IAM roles: 

  * [Dataproc Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`) on the project
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account



#### Service account role

To ensure that the Compute Engine default service account has the necessary permissions to create a Managed Service for Apache Spark cluster, ask your administrator to grant the following IAM roles to the Compute Engine default service account on the project: 

**Important:** You must grant these roles to the Compute Engine default service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * All: [Dataproc Worker ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`) 



## Create a cluster

  1. In the Google Cloud console, go to the Managed Service for Apache Spark **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/dataproc/clusters)

  2. Click **Create cluster**.

  3. In the **Create Dataproc cluster** dialog, click **Create** in the **Cluster on Compute Engine** row.

  4. In the **Cluster name** field, enter `example-cluster`.

  5. In the **Region** and **Zone** lists, select a region and zone.

Select a region (for example, `us-east1` or `europe-west1`) to isolate resources, such as virtual machine (VM) instances and Cloud Storage and metadata storage locations that are used by Managed Service for Apache Spark, in the region. For more information, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones#available) and [Cluster region](https://docs.cloud.google.com/managed-spark/docs/concepts/cluster-region)

  6. For all the other options, use the default settings.

  7. To create the cluster, click **Create**.

Your new cluster appears in a list on the **Clusters** page. The status is **Provisioning** until the cluster is ready to use, and then the status changes to **Running**. Provisioning the cluster might take a couple of minutes.




## Submit a Spark job

Submit a Spark job that estimates a value of Pi:

  1. In the Managed Service for Apache Spark navigation menu, click **Jobs**.
  2. On the **Jobs** page, click add_box **Submit job** , and then do the following:

     1. In the **Job ID** field, use the default setting, or provide an ID that is unique to your Google Cloud project.
     2. In the **Cluster** drop-down, select **`example-cluster`**.
     3. For **Job type** , select **Spark**.
     4. In the **Main class or jar** field, enter `org.apache.spark.examples.SparkPi`.
     5. In the **Jar files** field, enter `file:///usr/lib/spark/examples/jars/spark-examples.jar`. (This sample jar is pre-installed on the cluster. For custom jobs, specify a Cloud Storage path; see [Submit a job](https://docs.cloud.google.com/managed-spark/docs/guides/submit-job).)

**Caution:** Don't copy custom JAR files directly into cluster system directories such as `/usr/lib/spark/jars/`. Placing custom JARs in system directories pollutes the Managed Service for Apache Spark agent classpath and can cause job cancellation failures and orphaned YARN applications.
     6. In the **Arguments** field, enter `1000` to set the number of tasks.

**Note:** The Spark job estimates Pi by using the [Monte Carlo method](https://wikipedia.org/wiki/Monte_Carlo_method)

It generates _x_ and _y_ points on a coordinate plane that models a circle enclosed by a unit square. The input argument (`1000`) determines the number of x-y pairs to generate; the more pairs generated, the greater the accuracy of the estimation. This estimation uses Managed Service for Apache Spark worker nodes to parallelize the computation. For more information, see [Estimating Pi using the Monte Carlo Method](https://academo.org/demos/estimating-pi-monte-carlo/) and [JavaSparkPi.java on GitHub](https://github.com/apache/spark/blob/master/examples/src/main/java/org/apache/spark/examples/JavaSparkPi.java).

     7. Click **Submit**.

Your job is displayed on the **Job details** page. The job status is **Running** or **Starting** , and then it changes to **Succeeded** after it's submitted.

To avoid scrolling in the output, click **Line wrap: off**. The output is similar to the following:
            
            Pi is roughly 3.1416759514167594
            

To view job details, click the **Configuration** tab.




## Update a cluster

Update your cluster by changing the number of worker instances:

  1. In the Managed Service for Apache Spark navigation menu, click **Clusters**.
  2. In the list of clusters, click **`example-cluster`**.
  3. On the **Cluster details** page, click the **Configuration** tab.

Your cluster settings are displayed.

  4. Click mode_edit **Edit**.

  5. In the **Worker nodes** field, enter `5`.

  6. Click **Save**.




Your cluster is now updated. To decrease the number of worker nodes to the original value, follow the same procedure.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. To delete the cluster, on the **Cluster details** page for **`example-cluster`** , click delete **Delete**.
  2. To confirm that you want to delete the cluster, click **Delete**.



## What's next

  * Try this quickstart by using other tools:

    * [Use the API Explorer](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-template)

    * [Use the Google Cloud CLI](https://docs.cloud.google.com/managed-spark/docs/quickstarts/create-cluster-gcloud)

  * Learn how to [create robust firewall rules when you create a project](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network)

  * Learn how to [write and run a Spark Scala job](https://docs.cloud.google.com/managed-spark/docs/tutorials/spark-scala).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
