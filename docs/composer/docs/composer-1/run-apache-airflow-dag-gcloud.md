---
url: https://docs.cloud.google.com/composer/docs/composer-1/run-apache-airflow-dag-gcloud/
title: Quickstart: Run an Apache Airflow DAG in Managed Airflow\u00a0(Legacy Gen\u00a01) (Google Cloud CLI) \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:24.240194+00:00
---

# Quickstart: Run an Apache Airflow DAG in Managed Airflow (Legacy Gen 1) (Google Cloud CLI)  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/run-apache-airflow-dag-gcloud/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run an Apache Airflow DAG in Managed Airflow (Legacy Gen 1) (Google Cloud CLI)

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/run-apache-airflow-dag-gcloud "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/run-apache-airflow-dag-gcloud "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This quickstart guide shows you how to create a Managed Service for Apache Airflow environment and run an Apache Airflow DAG in Managed Airflow (Legacy Gen 1).

  * If you are **new to Airflow** , see the [Airflow concepts tutorial](https://airflow.apache.org/docs/stable/concepts.html) in Apache Airflow documentation for more information about Airflow concepts, objects, and their usage.

  * If you want to **use Google Cloud console instead** , see [Run an Apache Airflow DAG in Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-1/run-apache-airflow-dag).

  * If you want to create an environment **using Terraform** , see [Create environments (Terraform)](https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments).




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
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

  7. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  8. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  10. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  11. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  12. Enable the Managed Airflow API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable composer.googleapis.com

  13. To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * To assign IAM roles and permissions: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
     * To create a service account for the Managed Airflow environment: [Create Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountCreator) (`roles/iam.serviceAccountCreator`) 
     * To view create and manage the Managed Airflow environment: 
       * [Environment and Storage Object Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.environmentAndStorageObjectAdmin) (`roles/composer.environmentAndStorageObjectAdmin`)
       * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
     * To view logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Create an environment's service account

When you create an environment, you specify a service account. This service account is called _environment's service account_. Your environment uses this service account to perform most of the operations.

The service account for your environment is not a user account. A service account is a special kind of account used by an application or a virtual machine (VM) instance, not a person.

To create a service account for your environment:

  1. [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating), as described in the Identity and Access Management documentation.

  2. [Grant a role to it](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role), as described in the Identity and Access Management documentation. The required role is **Composer Worker** (`composer.worker`).




## Create an environment

Create a new environment named `example-environment` in the `us-central1` region, with the latest Managed Airflow (Legacy Gen 1) [version](https://docs.cloud.google.com/composer/docs/composer-versions#images).
    
    
    gcloud composer environments create example-environment \
        --location us-central1 \
        --image-version composer-1.20.12-airflow-1.10.15 \
        --service-account ENVIRONMENT_SERVICE_ACCOUNT
    

Replace `ENVIRONMENT_SERVICE_ACCOUNT` with the service account for your environment that you have created eariler.

## Create a DAG file

An [Airflow DAG](https://airflow.apache.org/docs/stable/concepts.html) is a collection of organized tasks that you want to schedule and run. DAGs are defined in standard Python files.

This guide uses an example Airflow DAG defined in the `quickstart.py` file. Python code in this file does the following:

  1. Creates a DAG, `composer_sample_dag`. This DAG runs every day.
  2. Executes one task, `print_dag_run_conf`. The task prints the DAG run's configuration by using the bash operator.



Save a copy of the `quickstart.py` file on your local machine:
    
    
    import datetime
    
    from airflow import models
    from airflow.operators import bash
    
    # If you are running Airflow in more than one time zone
    # see https://airflow.apache.org/docs/apache-airflow/stable/timezone.html
    # for best practices
    YESTERDAY = datetime.datetime.now() - datetime.timedelta(days=1)
    
    default_args = {
        "owner": "Composer Example",
        "depends_on_past": False,
        "email": [""],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": datetime.timedelta(minutes=5),
        "start_date": YESTERDAY,
    }
    
    with models.DAG(
        "composer_quickstart",
        catchup=False,
        default_args=default_args,
        schedule_interval=datetime.timedelta(days=1),
    ) as dag:
        # Print the dag_run id from the Airflow logs
        print_dag_run_conf = bash.BashOperator(
            task_id="print_dag_run_conf", bash_command="echo {{ dag_run.id }}"
        )

## Upload the DAG file to your environment's bucket

Every Managed Airflow environment has a Cloud Storage bucket associated with it. Airflow in Managed Airflow schedules only DAGs that are located in the `/dags` folder in this bucket.

To schedule your DAG, upload `quickstart.py` from your local machine to your environment's `/dags` folder:

To upload `quickstart.py` with Google Cloud CLI, run the following command in the folder where the `quickstart.py` file is located:
    
    
    gcloud composer environments storage dags import \
    --environment example-environment --location us-central1 \
    --source quickstart.py
    

## View the DAG

After you upload the DAG file, Airflow does the following:

  1. Parses the DAG file that you uploaded. It might take a few minutes for the DAG to become available to Airflow.
  2. Adds the DAG to the list of available DAGs.
  3. Executes the DAG according to the schedule you provided in the DAG file.



Check that your DAG is processed without errors and is available in Airflow by viewing it in DAG UI. DAG UI is Managed Airflow interface for viewing DAG information in Google Cloud console. Managed Airflow also provides access to [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface), which is a native Airflow web interface.

  1. Wait about five minutes to give Airflow time to process the DAG file that you uploaded previously, and to complete the first DAG run (explained later).

  2. Run the following command in Google Cloud CLI. This command executes the `dags list` [Airflow CLI command](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli) that lists DAGs in your environment.
         
         gcloud composer environments run example-environment \
         --location us-central1 \
         dags list
         

  3. Check that the `composer_quickstart` DAG is listed in the command's output.

Example output:
         
         Executing the command: [ airflow dags list ]...
         Command has been started. execution_id=d49074c7-bbeb-4ee7-9b26-23124a5bafcb
         Use ctrl-c to interrupt the command
         dag_id              | filepath              | owner            | paused
         ====================+=======================+==================+=======
         airflow_monitoring  | airflow_monitoring.py | airflow          | False
         composer_quickstart | dag-quickstart-af2.py | Composer Example | False
         

**Note:** The `airflow_monitoring` DAG is used by Managed Airflow to monitor the health of your environment.



## View DAG run details

A single execution of a DAG is called a _DAG run_. Airflow immediately executes a DAG run for the example DAG because the start date in the DAG file is set to yesterday. In this way, Airflow catches up to the specified DAG's schedule.

The example DAG contains one task, `print_dag_run_conf`, which runs the `echo` command in the console. This command outputs meta information about the DAG (DAG run's numeric identifier).

Run the following command in Google Cloud CLI. This command lists DAG runs for the `composer_quickstart` DAG:
    
    
    gcloud composer environments run example-environment \
    --location us-central1 \
    dags list-runs -- --dag-id composer_quickstart
    

Example output:
    
    
    dag_id              | run_id                                      | state   | execution_date                   | start_date                       | end_date
    ====================+=============================================+=========+==================================+==================================+=================================
    composer_quickstart | scheduled__2024-02-17T15:38:38.969307+00:00 | success | 2024-02-17T15:38:38.969307+00:00 | 2024-02-18T15:38:39.526707+00:00 | 2024-02-18T15:38:42.020661+00:00
    

**Note:** You can use the `tasks states-for-dag-run` command to get the status of individual tasks.

Airflow CLI does not provide a command to view task logs. You can use other methods to [view Airflow task logs](https://docs.cloud.google.com/composer/docs/composer-1/view-logs): Managed Airflow DAG UI, Airflow UI, or Cloud Logging. This guide shows a way to query Cloud Logging for logs from a specific DAG run.

Run the following command in Google Cloud CLI. This command reads logs from Cloud Logging for a specific DAG run of the `composer_quickstart` DAG. The `--format` argument formats the output so that only the text of the log message is displayed.
    
    
    gcloud logging read \
    --format="value(textPayload)" \
    --order=asc \
    "resource.type=cloud_composer_environment \
    resource.labels.location=us-central1 \
    resource.labels.environment_name=example-environment \
    labels.workflow=composer_quickstart \
    (labels.\"execution-date\"=\"RUN_ID\")"
    

Replace:

  * `RUN_ID` with the `run_id` value from the output of the `tasks states-for-dag-run` command that you run previously. For example, `2024-02-17T15:38:38.969307+00:00`.



Example output:
    
    
    ...
    
    Starting attempt 1 of 2
    Executing <Task(BashOperator): print_dag_run_conf> on 2024-02-17
    15:38:38.969307+00:00
    Started process 22544 to run task
    
    ...
    
    Running command: ['/usr/bin/bash', '-c', 'echo 115746']
    Output:
    115746
    
    ...
    
    Command exited with return code 0
    Marking task as SUCCESS. dag_id=composer_quickstart,
    task_id=print_dag_run_conf, execution_date=20240217T153838,
    start_date=20240218T153841, end_date=20240218T153841
    Task exited with return code 0
    0 downstream tasks scheduled from follow-on schedule check
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

Delete the **resources** used in this tutorial:

  1. Delete the Managed Airflow environment:

     1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     2. Select `example-environment` and click **Delete**.

     3. Wait until the environment is deleted.

  2. Delete your environment's bucket. Deleting the Managed Airflow environment does not delete its bucket.

     1. In the Google Cloud console, go to the **Storage** > **Browser** page.

[Go to Storage > Browser](https://console.cloud.google.com/storage/browser)

     2. Select the environment's bucket and click **Delete**. For example, this bucket can be named `us-central1-example-environ-c1616fe8-bucket`.




## What's next

  * [Adding and updating DAGs](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags)
  * [Writing DAGs](https://docs.cloud.google.com/composer/docs/composer-1/write-dags)
  * [Overriding Airflow configurations](https://docs.cloud.google.com/composer/docs/composer-1/override-airflow-configurations)
  * [Accessing Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
