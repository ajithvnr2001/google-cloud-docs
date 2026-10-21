---
url: https://docs.cloud.google.com/database-center/docs/assessments/
title: Create an assessment of a recommendation \u00a0|\u00a0 Database Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:40.043863+00:00
---

# Create an assessment of a recommendation  |  Database Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/assessments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs)
  * [ Guides ](https://docs.cloud.google.com/database-center/docs/overview)



Send feedback 

#  Create an assessment of a recommendation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Create an assessment of a recommendation**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use assessments in Database Center to assess and test the performance impact of database recommendations before you apply them to your production database fleet.

To assess recommendations, the assessments performs these operations:

  * Clones your database instance.

  * Runs benchmarking simulation tests on the clone.

  * Compares the baseline performance of the clone against the performance after you apply the recommended configuration changes.




## Supported products and recommendations

Database Center assessments are available only for [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres) instances.

You can assess the following types of recommendations:

  * **Compute resource expansion** : Evaluates the impact of resizing instances to machine types with more vCPUs or memory.

  * **Edition upgrade** : Assesses the performance impact of migrating from the Cloud SQL Enterprise edition to the Cloud SQL Enterprise Plus edition of Cloud SQL for PostgreSQL. For details, see [Upgrade an instance to Cloud SQL Enterprise Plus edition in place](https://docs.cloud.google.com/sql/docs/postgres/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).

  * **Data cache activation** : Analyzes the latency and throughput implications of enabling the [data cache](https://docs.cloud.google.com/sql/docs/postgres/data-cache).




## Before you begin

Ensure that you meet the following requirements before you run a recommendation assessment:

  * **API enablement** : Enable the following APIs:

    * [Cloud SQL Admin API](https://docs.cloud.google.com/sql/docs) (`sqladmin.googleapis.com`)
    * [Cloud Run Admin API](https://docs.cloud.google.com/run/docs) (`run.googleapis.com`)
    * [Cloud Logging API](https://docs.cloud.google.com/logging/docs) (`logging.googleapis.com`)
    * [Gemini Cloud Assist API](https://docs.cloud.google.com/gemini/docs/cloud-assist/overview) (`geminicloudassist.googleapis.com`)
    * [Secret Manager API](https://docs.cloud.google.com/secret-manager/docs) (`secretmanager.googleapis.com`)
    * [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/docs) (`monitoring.googleapis.com`)

See [Enabling and disabling APIs](https://docs.cloud.google.com/apis/docs/enable-disable-apis) to enable APIs.

  * **Database connection credentials** : You must provide the target database name and a database username.

  * **Secret Manager secret** : You must store the password for your database username in a global Secret Manager secret and know the name of the secret so you can search for it in the secret picker. You only need the full secret path if the secret doesn't appear in the list. For more information about creating secrets, see [Creating and accessing secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

  * **Service account** : Configure an Identity and Access Management (IAM) service account for the environment to benchmark and compare baseline performance against recommended changes. This service account requires permissions to read the database credentials secret from Secret Manager and to coordinate benchmarking tasks in Cloud Run. See [Creating a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) to configure service accounts.

  * **IAM permissions** : You must have the required IAM permissions to initiate and manage the testing process. For more information, see Required IAM permissions.




## Assess a recommendation

Follow these steps to assess and test a recommendation:

  1. Go to the **Database Center** page in the Google Cloud console.

[Go to Database Center](https://console.cloud.google.com/database-center)

  2. Click **Assessments** in the navigation menu.

  3. Locate a supported recommendation for a Cloud SQL for PostgreSQL instance.

  4. Click **Assess impact** in the **Implications** column for that recommendation.

If you haven't enabled the required APIs, follow the guidance in the panel to enable them.

  5. On the **Assessment details** page, enter the following connection details in the configuration panel:

     1. In **Database** , enter the name of the database. Valid options correspond to the databases listed on the **Databases** page of your Cloud SQL instance.

     2. In **Username** , enter the database username.

     3. In **Password secret** , select the Secret Manager secret containing the database user password.

If the secret doesn't appear in the list, enter the secret path manually in the format `projects/PROJECT_ID/secrets/SECRET_NAME`. Replace `PROJECT_ID` with your project ID and `SECRET_NAME` with the name of the secret. By default, Database Center uses the latest version of the secret. You can optionally specify a version by appending `/versions/VERSION` to the path, replacing `VERSION` with the version of the secret.

     4. In **Service account** , select the service account to use for running the benchmarking jobs.

  6. Click **Generate test plan**. Generating the plan takes a few minutes.

Database Center generates a test plan preview showing the sequence of steps to clone the database, run [pgbench](https://www.postgresql.org/docs/current/pgbench.html) workloads, apply the recommendation, and analyze performance.

Database Center lists the session on the **Assessments** page when it generates the plan. You can safely navigate away from the page and return to the session later.

  7. To refine the test plan, in the **Test instructions** field, enter instructions (for example, `Change the benchmark duration to 60 seconds`), and then click **Update test plan**.

  8. Click **Start assessment**. In the confirmation dialog, review the billing notice. Provisioning the cloned instance and running benchmark jobs are billable within your project.

The assessment session is available for 48 hours. Database Center automatically deletes the cloned instance after a successful assessment. If the assessment fails, the cloned instance isn't deleted automatically, and you must delete it manually.

  9. Click **Confirm** to start the evaluation. The assessment process takes some time to complete.

Database Center displays the assessment progress. You can safely leave the page while the session runs in the background.




## View assessment history and reports

Manage evaluations and review performance comparison reports by tracking assessment sessions. Database Center retains session reports and metadata for 48 hours and displays an expiration countdown for each session.

  1. In the Google Cloud console, go to the **Database Center** page.

[Go to Database Center](https://console.cloud.google.com/database-center)

  2. In the navigation menu, click **Assessments**.

  3. In the sessions list, click the **Session ID** of the session to view its details.

The following table describes the assessment session statuses, the information displayed for each status, and the available actions:

Status | Displayed information | Available actions  
---|---|---  
Planning phase |  Test plan details and preview.  |  Refine the test plan preview using the **Test instructions** field, or click **Start assessment** to begin the assessment.   
Assessment phase |  The assessment progress and the test plan used by the assessment.  |  Click **Cancel** to cancel the assessment.   
Completed |  A summary that compares database performance before and after applying the recommendation.  |  None   
Canceled |  The progress of the assessment before it was canceled.  |  None   
Generation failed |  Generation of the test plan failed. You can view test plan details and configuration fields, such as the database name and secret name, to retry generating the test plan.  |  Update the assessment configuration settings, such as database name and username, and retry the test plan generation.   
Assessment failed |  The assessment of the recommendation failed. You can view the error message and the progress of the assessment before it failed.  |  None   



## Cancel a session or clean up failed sessions

If you cancel an assessment session in progress or if the execution fails, verify that all temporary resources are removed. Because Database Center can't confirm whether cleanup succeeded after a failure or cancellation, check for and delete remaining database clone instances for all failed and canceled sessions.

  * **Cancel a session** : On the **Assessments** page, click the session ID of the assessment you want to cancel, then click **Cancel**. To cancel a session, its session ID must have a status of **Assessment phase**.

  * **Clean up cloned resources** :

To manually delete the cloned instance:

    1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

    2. In the instances list, locate the cloned instance. You can identify the clone using the resource link displayed on the session details page.

    3. Click **More actions** _more_vert_ next to the cloned instance, and then click **Delete**.

    4. In the confirmation dialog, enter the clone instance name and click **Delete**.


**Warning:** When you cancel a session or if a session fails, Database Center might not delete the temporary clone instance. To avoid ongoing database cloning charges, verify and manually delete any remaining database clone instances for all canceled or failed sessions. Cloud Run benchmarking resources stop automatically and don't require manual deletion.

## Required IAM permissions

You need specific permissions to initiate and manage the testing process. Obtain these permissions by assigning predefined roles or by creating custom roles with individual permissions.

See [Access control with IAM](https://docs.cloud.google.com/iam/docs/roles-permissions) to manage access and understand roles.

**Permissions for the end user**

The following table lists the permissions required for your user account and the predefined roles that contain them:

Required permissions | Predefined role  
---|---  
`cloudsql.instances.patch`  
`cloudsql.instances.clone`  
`cloudsql.instances.delete`  
`cloudsql.instances.get`  
`cloudsql.instances.createTestingAgentSession`  
`cloudsql.instances.getAgentSession`  
`cloudsql.instances.listAgentSessions`  
`cloudsql.instances.cancelAgentSession` |  [`roles/cloudsql.admin`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin)  
`run.jobs.create`  
`run.jobs.run` |  [`roles/run.developer`](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer)  
`logging.logEntries.list` |  [`roles/logging.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer)  
`secretmanager.secrets.list` |  [`roles/secretmanager.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer)  
`serviceusage.services.use` |  [`roles/serviceusage.serviceUsageConsumer`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer)  
`monitoring.monitoredResourceDescriptors.list` (optional)  |  [`roles/monitoring.viewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) or [`roles/viewer`](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic)  
  
To view charts data on the assessment results page, your user account must have the `monitoring.monitoredResourceDescriptors.list` permission. This permission is recommended, but it isn't required to run recommendation assessments.

The user initiating the assessment must also have the [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) role (`roles/iam.serviceAccountUser`) or the `iam.serviceAccounts.actAs` permission on the selected service account.

**Permissions for the Cloud Run service account**

The following table lists the permissions required for the service account used by the Cloud Run jobs and the predefined roles that contain them:

Required permissions | Predefined role  
---|---  
`cloudsql.instances.connect` |  [`roles/cloudsql.client`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.client)  
`cloudsql.instances.login` |  [`roles/cloudsql.instanceUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.instanceUser)  
`secretmanager.versions.access` |  [`roles/secretmanager.secretAccessor`](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor)  
  
## Limitations

Consider the following limitations when you use recommendation assessment:

  * **Informational report only** : The assessment doesn't apply modifications to your production databases. If you approve of the benchmarking results, apply the recommendations manually by using the Cloud SQL for PostgreSQL console or [Cloud SQL for PostgreSQL APIs](https://docs.cloud.google.com/sql/docs/postgres/apis).

  * **48-hour expiration** : Database Center retains session reports and metadata in the session store for only 48 hours, and then deletes them.

  * **Single user isolation** : Only the user who created a validation session can view it. Other principals in your project can't view your session history or results.

  * **Global secret location** : The Secret Manager secret containing the database password must be a global secret. Regional secrets aren't supported.




## Billing

A recommendation assessment incurs charges for the resources that you use during the evaluation. The system creates a clone of your database instance in your project, and you pay for this clone. Database Center automatically deletes the clone after a successful assessment. If an assessment fails or is canceled, you must manually delete the clone to avoid ongoing charges.

In addition, the database agent uses other Google Cloud infrastructure that might incur costs, including:

  * **Cloud SQL** : For the cloned instance. For details, see [Cloud SQL pricing](https://docs.cloud.google.com/sql/pricing).
  * **Cloud Run** : To run the assessment agent. For details, see [Cloud Run pricing](https://docs.cloud.google.com/run/pricing).
  * **Other services** : Minor charges for other services used to coordinate the assessment.



You pay only for the time that the assessment runs.

## What's next

  * Learn how to [view and filter health issues and recommendations](https://docs.cloud.google.com/database-center/docs/health-issues-recommendations).

  * Learn how to [analyze database fleet health using Gemini](https://docs.cloud.google.com/database-center/docs/analyze-database-using-gemini).

  * Learn how to [customize your database fleet view](https://docs.cloud.google.com/database-center/docs/customize-database-fleet-view).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
