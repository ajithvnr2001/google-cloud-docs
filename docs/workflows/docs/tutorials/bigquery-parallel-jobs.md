---
url: https://docs.cloud.google.com/workflows/docs/tutorials/bigquery-parallel-jobs/
title: Run multiple BigQuery jobs in parallel \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:26.359522+00:00
---

# Run multiple BigQuery jobs in parallel  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/tutorials/bigquery-parallel-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Run multiple BigQuery jobs in parallel Stay organized with collections  Save and categorize content based on your preferences. 

BigQuery hosts a number of [public datasets](https://docs.cloud.google.com/bigquery/public-data) that are available to the general public to query. In this tutorial, you create a workflow that runs multiple BigQuery query jobs in parallel, demonstrating an improvement in performance when compared to running the jobs serially, one after the other.

**Note:** When initiating a BigQuery job using the [BigQuery connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview), your workflow might not automatically wait for the job's completion. If subsequent steps depend on the job's success, you should [implement a polling mechanism](https://docs.cloud.google.com/workflows/docs/poll-bigquery-job).

## Objectives

In this tutorial you will: 

  1. Run a query against a [Wikipedia public dataset](https://console.cloud.google.com/bigquery?p=bigquery-samples&d=wikipedia_pageviews&page=dataset) to determine the most viewed titles in a specific month.
  2. Deploy and execute a workflow that runs multiple BigQuery query jobs serially, one after the other.
  3. Deploy and execute a workflow that runs the BigQuery jobs using [parallel iteration](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps#parallel-iteration), and where ordinary `for` loops are executed in parallel.



You can run the following commands in the Google Cloud console, or by using the Google Cloud CLI in either your terminal or Cloud Shell.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [BigQuery](https://docs.cloud.google.com/bigquery)
  * [Workflows](https://docs.cloud.google.com/workflows)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

### Console

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com)

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **BigQuery > BigQuery Job User, Logging > Logs Writer**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Workflows API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=workflows.googleapis.com)

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the following roles to the service account: **BigQuery > BigQuery Job User, Logging > Logs Writer**. 

To grant a role, find the **Select a role** list, then select the role. 

To grant additional roles, click add **Add another role** and add each additional role. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. Click **Done** to finish creating the service account. 




### gcloud

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Workflows API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable workflows.googleapis.com

  8. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/bigquery.jobUser, roles/logging.logWriter`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Workflows API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable workflows.googleapis.com

  15. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. Grant roles to the service account. Run the following command once for each of the following IAM roles: `roles/bigquery.jobUser, roles/logging.logWriter`: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 




## Run a BigQuery query job

In BigQuery, you can run an interactive (on-demand) query job. For more information, see [Running interactive and batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries).

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. Enter the following BigQuery SQL query in the **Query editor** text area:
         
         SELECT TITLE, SUM(views)
         FROM `bigquery-samples.wikipedia_pageviews.201207h`
         GROUP BY TITLE
         ORDER BY SUM(views) DESC
         LIMIT 100
         

  3. Click **Run**.




### bq

In your terminal, enter the following `bq query` command to run an interactive query using standard SQL syntax:
    
    
    bq query \
    --use_legacy_sql=false \
    'SELECT
      TITLE, SUM(views)
    FROM
      `bigquery-samples.wikipedia_pageviews.201207h`
    GROUP BY
      TITLE
    ORDER BY
      SUM(views) DESC
    LIMIT 100'
    

This runs a query that returns the top 100 Wikipedia titles with the most views in a specific month and writes the output to a temporary table.

Note how long the query takes to run.

## Deploy a workflow that runs multiple queries serially

A workflow definition is made up of a series of steps described using the [Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax). After creating a workflow, you deploy it to make it available for execution. The deploy step also validates that the source file can be executed.

The following workflow defines a list of five tables to run a query against using the Workflows [BigQuery connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/Overview). The queries are run serially, one after the other, and the most viewed titles from each table are saved to a results map.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click **Create**.

  3. Enter a name for the new workflow, such as `workflow-serial-bqjobs`.

  4. Choose an appropriate region; for example, **us-central1**.

  5. Select the **service account** you previously created.

You should have already granted both the **BigQuery > BigQuery Job User** and **Logging > Logs Writer** IAM roles to the service account.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
             steps:
             - init:
                 assign:
                     - results : {} # result from each iteration keyed by table name
                     - tables:
                         - 201201h
                         - 201202h
                         - 201203h
                         - 201204h
                         - 201205h
             - runQueries:
                 for:
                     value: table
                     in: ${tables}
                     steps:
                     - logTable:
                         call: sys.log
                         args:
                             text: ${"Running query for table " + table}
                     - runQuery:
                         call: googleapis.bigquery.v2.jobs.query
                         args:
                             projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                             body:
                                 useLegacySql: false
                                 useQueryCache: false
                                 timeoutMs: 30000
                                 # Find top 100 titles with most views on Wikipedia
                                 query: ${
                                     "SELECT TITLE, SUM(views)
                                     FROM `bigquery-samples.wikipedia_pageviews." + table + "`
                                     WHERE LENGTH(TITLE) > 10
                                     GROUP BY TITLE
                                     ORDER BY SUM(VIEWS) DESC
                                     LIMIT 100"
                                     }
                         result: queryResult
                     - returnResult:
                         assign:
                             # Return the top title from each table
                             - results[table]: {}
                             - results[table].title: ${queryResult.rows[0].f[0].v}
                             - results[table].views: ${queryResult.rows[0].f[1].v}
             - returnResults:
                 return: ${results}

  8. Click **Deploy**.




### gcloud

  1. Open a terminal and create a source code file for your workflow:
         
         touch workflow-serial-bqjobs.yaml

  2. Copy the following workflow to your source code file:
         
         main:
             steps:
             - init:
                 assign:
                     - results : {} # result from each iteration keyed by table name
                     - tables:
                         - 201201h
                         - 201202h
                         - 201203h
                         - 201204h
                         - 201205h
             - runQueries:
                 for:
                     value: table
                     in: ${tables}
                     steps:
                     - logTable:
                         call: sys.log
                         args:
                             text: ${"Running query for table " + table}
                     - runQuery:
                         call: googleapis.bigquery.v2.jobs.query
                         args:
                             projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                             body:
                                 useLegacySql: false
                                 useQueryCache: false
                                 timeoutMs: 30000
                                 # Find top 100 titles with most views on Wikipedia
                                 query: ${
                                     "SELECT TITLE, SUM(views)
                                     FROM `bigquery-samples.wikipedia_pageviews." + table + "`
                                     WHERE LENGTH(TITLE) > 10
                                     GROUP BY TITLE
                                     ORDER BY SUM(VIEWS) DESC
                                     LIMIT 100"
                                     }
                         result: queryResult
                     - returnResult:
                         assign:
                             # Return the top title from each table
                             - results[table]: {}
                             - results[table].title: ${queryResult.rows[0].f[0].v}
                             - results[table].views: ${queryResult.rows[0].f[1].v}
             - returnResults:
                 return: ${results}

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy workflow-serial-bqjobs \
            --source=workflow-serial-bqjobs.yaml \
            --service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.iam.gserviceaccount.com

Replace `MY_SERVICE_ACCOUNT@MY_PROJECT.iam.gserviceaccount.com` with the email of the service account you previously created.

You should have already granted both the `roles/bigquery.jobUser` and `roles/logging.logWriter` IAM roles to the service account.




## Execute the workflow and run multiple queries serially

Executing a workflow runs the current workflow definition associated with the workflow.

### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. On the **Workflows** page, select the **workflow-serial-bqjobs** workflow to go to its details page.

  3. On the **Workflow Details** page, click _play_arrow_ **Execute**.

  4. Click **Execute** again.

  5. View the results of the workflow in the **Output** pane.




### gcloud

  1. Open a terminal.

  2. Execute the workflow:
         
         gcloud workflows run workflow-serial-bqjob




The workflow execution should take approximately a minute or five times the previous running time. The result will include each table and look similar to the following:
    
    
    {
      "201201h": {
        "title": "Special:Search",
        "views": "14591339"
      },
      "201202h": {
        "title": "Special:Search",
        "views": "132765420"
      },
      "201203h": {
        "title": "Special:Search",
        "views": "123316818"
      },
      "201204h": {
        "title": "Special:Search",
        "views": "116830614"
      },
      "201205h": {
        "title": "Special:Search",
        "views": "131357063"
      }
    }
    

## Deploy and execute a workflow that runs multiple queries in parallel

Instead of running five queries sequentially, you can run the queries in parallel by making a few changes:
    
    
     - runQueries:
        parallel:
            shared: [results]
            for:
                value: table
                in: ${tables}
    

  * A `parallel` step allows each iteration of the `for` loop to run in parallel.
  * The `results` variable is declared as `shared` which allows it to be writable by a branch, and the result of each branch can be appended to it.




### Console

  1. In the Google Cloud console, go to the **Workflows** page:

[Go to Workflows](https://console.cloud.google.com/workflows)

  2. Click **Create**.

  3. Enter a name for the new workflow, such as `workflow-parallel-bqjobs`.

  4. Choose an appropriate region; for example, **us-central1**.

  5. Select the **service account** you previously created.

  6. Click **Next**.

  7. In the workflow editor, enter the following definition for your workflow:
         
         main:
             steps:
             - init:
                 assign:
                     - results : {} # result from each iteration keyed by table name
                     - tables:
                         - 201201h
                         - 201202h
                         - 201203h
                         - 201204h
                         - 201205h
             - runQueries:
                 parallel:
                     shared: [results]
                     for:
                         value: table
                         in: ${tables}
                         steps:
                         - logTable:
                             call: sys.log
                             args:
                                 text: ${"Running query for table " + table}
                         - runQuery:
                             call: googleapis.bigquery.v2.jobs.query
                             args:
                                 projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                                 body:
                                     useLegacySql: false
                                     useQueryCache: false
                                     timeoutMs: 30000
                                     # Find top 100 titles with most views on Wikipedia
                                     query: ${
                                         "SELECT TITLE, SUM(views)
                                         FROM `bigquery-samples.wikipedia_pageviews." + table + "`
                                         WHERE LENGTH(TITLE) > 10
                                         GROUP BY TITLE
                                         ORDER BY SUM(VIEWS) DESC
                                         LIMIT 100"
                                         }
                             result: queryResult
                         - returnResult:
                             assign:
                                 # Return the top title from each table
                                 - results[table]: {}
                                 - results[table].title: ${queryResult.rows[0].f[0].v}
                                 - results[table].views: ${queryResult.rows[0].f[1].v}
             - returnResults:
                 return: ${results}

  8. Click **Deploy**.

  9. On the **Workflow Details** page, click _play_arrow_ **Execute**.

  10. Click **Execute** again.

  11. View the results of the workflow in the **Output** pane.




### gcloud

  1. Open a terminal and create a source code file for your workflow:
         
         touch workflow-parallel-bqjobs.yaml

  2. Copy the following workflow to your source code file:
         
         main:
             steps:
             - init:
                 assign:
                     - results : {} # result from each iteration keyed by table name
                     - tables:
                         - 201201h
                         - 201202h
                         - 201203h
                         - 201204h
                         - 201205h
             - runQueries:
                 parallel:
                     shared: [results]
                     for:
                         value: table
                         in: ${tables}
                         steps:
                         - logTable:
                             call: sys.log
                             args:
                                 text: ${"Running query for table " + table}
                         - runQuery:
                             call: googleapis.bigquery.v2.jobs.query
                             args:
                                 projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
                                 body:
                                     useLegacySql: false
                                     useQueryCache: false
                                     timeoutMs: 30000
                                     # Find top 100 titles with most views on Wikipedia
                                     query: ${
                                         "SELECT TITLE, SUM(views)
                                         FROM `bigquery-samples.wikipedia_pageviews." + table + "`
                                         WHERE LENGTH(TITLE) > 10
                                         GROUP BY TITLE
                                         ORDER BY SUM(VIEWS) DESC
                                         LIMIT 100"
                                         }
                             result: queryResult
                         - returnResult:
                             assign:
                                 # Return the top title from each table
                                 - results[table]: {}
                                 - results[table].title: ${queryResult.rows[0].f[0].v}
                                 - results[table].views: ${queryResult.rows[0].f[1].v}
             - returnResults:
                 return: ${results}

  3. Deploy the workflow by entering the following command:
         
         gcloud workflows deploy workflow-parallell-bqjobs \
            --source=workflow-parallel-bqjobs.yaml \
            --service-account=MY_SERVICE_ACCOUNT@MY_PROJECT.iam.gserviceaccount.com

Replace `MY_SERVICE_ACCOUNT@MY_PROJECT.iam.gserviceaccount.com` with the email of the service account you previously created.

  4. Execute the workflow:
         
         gcloud workflows run workflow-parallel-bqjobs




The result will be similar to the previous output but the workflow execution should take approximately twenty seconds or less!

## Clean up

If you created a new project for this tutorial, delete the project. If you used an existing project and wish to keep it without the changes added in this tutorial, delete resources created for the tutorial.

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



### Delete tutorial resources

Delete the workflows created in this tutorial:
    
    
    gcloud workflows delete WORKFLOW_NAME

## What's next

  * To learn more about parallel steps, see [Execute parallel steps](https://docs.cloud.google.com/workflows/docs/execute-parallel-steps).
  * To learn more about Workflows connectors, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).
  * To learn more about Workflows, see the [Workflows overview](https://docs.cloud.google.com/workflows/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
