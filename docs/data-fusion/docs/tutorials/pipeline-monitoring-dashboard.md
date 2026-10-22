---
url: https://docs.cloud.google.com/data-fusion/docs/tutorials/pipeline-monitoring-dashboard/
title: Create a pipeline monitoring dashboard using Cloud Monitoring \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:43.295801+00:00
---

# Create a pipeline monitoring dashboard using Cloud Monitoring  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/tutorials/pipeline-monitoring-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a pipeline monitoring dashboard using Cloud Monitoring

Learn how to use Cloud Monitoring to create a dashboard to monitor pipelines.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=data-fusion--pipeline-monitoring-dashboard)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Cloud Data Fusion, BigQuery, Cloud Storage, and Dataproc APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=datafusion.googleapis.com,bigquery.googleapis.com,storage.googleapis.com,dataproc.googleapis.com)

  7. To create custom dashboards, you must be granted the [Monitoring Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on the service account.

For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Create a Cloud Data Fusion instance with Cloud Logging enabled

To use Cloud Logging with your Cloud Data Fusion pipeline, create a Cloud Data Fusion instance with Cloud Logging enabled:

  1. Go to the Cloud Data Fusion **Instances** page and click **Create instance**.

[Create an instance](https://console.cloud.google.com/data-fusion/instance-create)

  2. In the **Instance name** field, enter a name for your new instance.

  3. From the **Region** drop-down, select the Google Cloud region in which you want to create the instance.

  4. From the **Version** drop-down, select a Cloud Data Fusion version.

  5. Select an **Edition**.

  6. Expand **Advanced options**.

  7. In the **Logging and monitoring** section, select **Enable Stackdriver logging service**.

  8. Click **Create**.


After you create an instance, you can't enable Cloud Logging in the Google Cloud console. 

## Create a log-based metric

  1. Go to the Cloud Logging **Log-based metrics** page:

[Go to Log-based metrics](https://console.cloud.google.com/logs/metrics)

  2. Click **Create metric**.

  3. On the **Create a metric** page, do the following:

     1. For **Metric type** , select **Counter**.
     2. In the **Log-based metric name** field, enter `pipeline_logs`.
     3. In the **Units** field, enter `1`.
     4. In the **Build filter** field, enter the following:
            
            resource.type="cloud_dataproc_cluster"
            log_name=~"projects/.*/logs/datafusion-pipeline-logs"
            

     5. In the **Labels** section, click **Add label** and create the following labels. After entering each label, click **Done** , and click **Add label** again to create the next label.

Label name | Label type | Field name  
---|---|---  
`Project` | `STRING` | `resource.labels.project_id`  
`Message` | `STRING` | `jsonPayload.message`  
`LoggerName` | `STRING` | `labels.loggerName`  
`ClusterName` | `STRING` | `resource.labels.cluster_name`  
`SparkPhase` | `STRING` | `labels.".workflowSparkId"`  
`Region` | `STRING` | `resource.labels.region`  
`Pipeline` | `STRING` | `labels.".applicationId"`  
`RunId` | `STRING` | `labels.".runId"`  
`Namespace` | `STRING` | `labels.".namespaceId"`  
`LogLevel` | `STRING` | `labels.levelName`  
     6. Click **Create metric**.

The newly created metric appears in the user-defined metrics table. If the metric isn't immediately visible, refresh the page.

The dashboard contains the following charts:

        * All pipelines
        * Completed pipelines
        * Failed pipelines
        * All pipeline runs
        * Completed pipeline runs
        * Failed pipeline runs
        * Managed Service for Apache Spark clusters for runs

After a metric is created, it might take up to 24 hours to start displaying the time series data.




## Install the dashboard

  1. [Download the JSON file](https://docs.cloud.google.com/static/data-fusion/docs/tutorials/sample_datasets/datafusion-pipelines-overview.json) to your local machine.

  2. Go to the Cloud Monitoring **Dashboards** page:

[Go to Monitoring dashboards](https://console.cloud.google.com/monitoring/dashboards)

  3. Click **Create dashboard**.

  4. Click settings **Dashboard settings** **> JSON > JSON editor**.

  5. In a text editor, open the JSON file that you downloaded.

  6. Copy the content of the downloaded JSON file and paste it into the JSON editor, replacing the content that the JSON editor contains by default.

  7. Click **Apply changes**.

This refreshes the dashboard. The Cloud Data Fusion pipelines run after the metric was created, appear in the dashboard. If no pipelines were run after the metric was created, the dashboard will be empty.

  8. Autosave is enabled by default. If autosave is disabled, click **Save** to save the dashboard.

  9. Click **Close editor**.

Your new dashboard appears in the list of dashboards on the **Monitoring overview** page.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the Cloud Data Fusion instance

Follow these instructions to [ delete your Cloud Data Fusion instance](https://docs.cloud.google.com/data-fusion/docs/how-to/delete-instance).

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
