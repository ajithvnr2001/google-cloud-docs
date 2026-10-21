---
url: https://docs.cloud.google.com/managed-spark/docs/tutorials/workflow-composer/
title: Workflow using Managed Airflow \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:36.122568+00:00
---

# Workflow using Managed Airflow  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/tutorials/workflow-composer/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Workflow using Managed Airflow Stay organized with collections  Save and categorize content based on your preferences. 

**Objective:**

  1. Create a Managed Service for Apache Spark workflow template that runs a [Spark PI job](https://spark.apache.org/examples.html)
  2. Create an Apache Airflow DAG that [Managed Airflow](https://docs.cloud.google.com/composer/docs) will use to start the workflow at a specific time.



In this document, you use the following billable components of Google Cloud: 

  * Managed Service for Apache Spark
  * Compute Engine
  * Managed Airflow



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Dataproc, Compute Engine, and Managed Airflow APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,composer.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Dataproc, Compute Engine, and Managed Airflow APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataproc,compute_component,composer.googleapis.com&redirect=https%3A//console.cloud.google.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init




## Create a Managed Service for Apache Spark workflow template

Copy and run the following commands in a local terminal window or in [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) to create and define a [workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows).

  1. Create the `sparkpi` workflow template. 
         
         gcloud dataproc workflow-templates create sparkpi \
             --region=us-central1
               

  2. Add the spark job to the `sparkpi` workflow template. The "compute" `step-id` flag identifies the SparkPi job. 
         
         gcloud dataproc workflow-templates add-job spark \
             --workflow-template=sparkpi \
             --step-id=compute \
             --class=org.apache.spark.examples.SparkPi \
             --jars=file:///usr/lib/spark/examples/jars/spark-examples.jar \
             --region=us-central1 \
             -- 1000
               

  3. Use a [managed](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview#managed_cluster), [single-node](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/single-node-clusters) cluster to run the workflow. Managed Service for Apache Spark will create the cluster, run the workflow on it, then delete the cluster when the workflow completes. 
         
         gcloud dataproc workflow-templates set-managed-cluster sparkpi \
             --cluster-name=sparkpi \
             --single-node \
             --region=us-central1
               

  4. Confirm workflow template creation. 

### Console 

Click the `sparkpi` name on the Managed Service for Apache Spark [**Workflows**](https://console.cloud.google.com/dataproc/workflows/templates) page in the Google Cloud console to open the **Workflow template details** page. Click the name of your workflow template to confirm the `sparkpi` template attributes.

![](https://docs.cloud.google.com/static/managed-spark/images/sparkpi-template.png)

### gcloud command 

Run the following command:
         
         gcloud dataproc workflow-templates describe sparkpi --region=us-central1
             




## Create and upload a DAG to Cloud Storage

  1. Create or use an existing [Managed Airflow environment](https://docs.cloud.google.com/composer/docs/how-to/managing/creating#creating_a_new_environment).
  2. Set environment variables. 

### Airflow UI

     1. In the toolbar, click **Admin > Variables**. ![](https://docs.cloud.google.com/static/managed-spark/images/airflow-toolbar.png)
     2. Click **Create**. ![](https://docs.cloud.google.com/static/managed-spark/images/airflow-variables.png)
     3. Enter the following information: 
        * Key:`project_id`
        * Val: PROJECT_ID — your Google Cloud project ID
     4. Click **Save**.

### gcloud command

Enter the following commands:

     * `ENVIRONMENT` is the name of the Managed Airflow environment
     * `LOCATION` is the region where the Managed Airflow environment is located
     * `PROJECT_ID` is the project ID for the project that contains the Managed Airflow environment
    
    gcloud composer environments run ENVIRONMENT --location LOCATION variables set -- project_id PROJECT_ID
        

  3. Copy the following DAG code locally into a file titled "composer-dataproc-dag.py", which uses the [DataprocInstantiateWorkflowTemplateOperator](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/operators/dataproc/index.html#airflow.providers.google.cloud.operators.dataproc.DataprocInstantiateWorkflowTemplateOperator).

### Airflow 2
         
         """Example Airflow DAG that kicks off a Cloud Dataproc Template that runs a
         Spark Pi Job.
         
         This DAG relies on an Airflow variable
         https://airflow.apache.org/docs/apache-airflow/stable/concepts/variables.html
         * project_id - Google Cloud Project ID to use for the Cloud Dataproc Template.
         """
         
         import datetime
         
         from airflow import models
         from airflow.providers.google.cloud.operators.dataproc import (
             DataprocInstantiateWorkflowTemplateOperator,
         )
         from airflow.utils.dates import days_ago
         
         project_id = "{{var.value.project_id}}"
         
         
         default_args = {
             # Tell airflow to start one day ago, so that it runs as soon as you upload it
             "start_date": days_ago(1),
             "project_id": project_id,
         }
         
         # Define a DAG (directed acyclic graph) of tasks.
         # Any task you create within the context manager is automatically added to the
         # DAG object.
         with models.DAG(
             # The id you will see in the DAG airflow page
             "dataproc_workflow_dag",
             default_args=default_args,
             # The interval with which to schedule the DAG
             schedule_interval=datetime.timedelta(days=1),  # Override to match your needs
         ) as dag:
             start_template_job = DataprocInstantiateWorkflowTemplateOperator(
                 # The task id of your job
                 task_id="dataproc_workflow_dag",
                 # The template id of your workflow
                 template_id="sparkpi",
                 project_id=project_id,
                 # The region for the template
                 region="us-central1",
             )
         

### Airflow 1
         
         """Example Airflow DAG that kicks off a Cloud Dataproc Template that runs a
         Spark Pi Job.
         
         This DAG relies on an Airflow variable
         https://airflow.apache.org/docs/apache-airflow/stable/concepts/variables.html
         * project_id - Google Cloud Project ID to use for the Cloud Dataproc Template.
         """
         
         import datetime
         
         from airflow import models
         from airflow.contrib.operators import dataproc_operator
         from airflow.utils.dates import days_ago
         
         project_id = "{{var.value.project_id}}"
         
         
         default_args = {
             # Tell airflow to start one day ago, so that it runs as soon as you upload it
             "start_date": days_ago(1),
             "project_id": project_id,
         }
         
         # Define a DAG (directed acyclic graph) of tasks.
         # Any task you create within the context manager is automatically added to the
         # DAG object.
         with models.DAG(
             # The id you will see in the DAG airflow page
             "dataproc_workflow_dag",
             default_args=default_args,
             # The interval with which to schedule the DAG
             schedule_interval=datetime.timedelta(days=1),  # Override to match your needs
         ) as dag:
             start_template_job = dataproc_operator.DataprocWorkflowTemplateInstantiateOperator(
                 # The task id of your job
                 task_id="dataproc_workflow_dag",
                 # The template id of your workflow
                 template_id="sparkpi",
                 project_id=project_id,
                 # The region for the template
                 # For more info on regions where Dataflow is available see:
                 # https://cloud.google.com/dataflow/docs/resources/locations
                 region="us-central1",
             )
         

  4. [Upload your DAG](https://docs.cloud.google.com/composer/docs/how-to/using/managing-dags) to your environment folder in Cloud Storage. After the upload has been completed successfully, click the **DAGs Folder** link on the Managed Airflow Environment's page.

![](https://docs.cloud.google.com/static/managed-spark/images/airflow-gcs.png)



### View a task's status

### Airflow UI

  1. Open the [Airflow web interface](https://docs.cloud.google.com/composer/docs/how-to/accessing/airflow-web-interface#accessing_the_web_interface).
  2. On the DAGs page, click the DAG name (for example, `dataproc_workflow_dag`).
  3. On the DAGs Details page, click **Graph View**.
  4. Check status: 
     * Failed: The task has a red box around it. You can also hold the pointer over task and look for **State: Failed**. ![the task has a red box around it, indicating it has failed](https://docs.cloud.google.com/static/managed-spark/images/airflow-dag-state-failed.png)
     * Success: The task has a green box around it. You can also hold the pointer over the task and check for **State: Success**. ![the task has a green box around it, indicating it has succeeded](https://docs.cloud.google.com/static/managed-spark/images/airflow-dag-state-success.png)



### Console

Click the Workflows tab to see workflow status.

![](https://docs.cloud.google.com/static/managed-spark/images/dataproc-workflow-view-dag.png)

### gcloud command
    
    
    gcloud dataproc operations list \
        --region=us-central1 \
        --filter="labels.goog-dataproc-workflow-template-id=sparkpi"
        

## Clean up

To avoid incurring charges to your Google Cloud account, you can delete the resources used in this tutorial:

  1. [Delete the Managed Airflow environment](https://console.cloud.google.com/composer/environments).

  2. [Delete the workflow template](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/using-workflows#deleting_a_workflow_template).




## What's next

  * See [Overview of Managed Service for Apache Spark workflow templates](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/overview).
  * See [Workflow scheduling solutions](https://docs.cloud.google.com/managed-spark/docs/concepts/workflows/workflow-schedule-solutions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
