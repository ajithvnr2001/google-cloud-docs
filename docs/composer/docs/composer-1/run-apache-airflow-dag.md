---
url: https://docs.cloud.google.com/composer/docs/composer-1/run-apache-airflow-dag/
title: Quickstart: Run an Apache Airflow DAG in Managed Airflow\u00a0(Legacy Gen\u00a01) \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:51.924299+00:00
---

# Quickstart: Run an Apache Airflow DAG in Managed Airflow (Legacy Gen 1)  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/run-apache-airflow-dag/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run an Apache Airflow DAG in Managed Airflow (Legacy Gen 1)

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/run-apache-airflow-dag "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/run-apache-airflow-dag "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This quickstart guide shows you how to create a Managed Service for Apache Airflow environment and run an Apache Airflow DAG in Managed Airflow (Legacy Gen 1).

  * If you are **new to Airflow** , see the [Airflow concepts tutorial](https://airflow.apache.org/docs/stable/concepts.html) in Apache Airflow documentation for more information about Airflow concepts, objects, and their usage.

  * If you want to **use Google Cloud CLI instead** , see [Run an Apache Airflow DAG in Managed Service for Apache Airflow (Google Cloud CLI)](https://docs.cloud.google.com/composer/docs/composer-1/run-apache-airflow-dag-gcloud).

  * If you want to create an environment **using Terraform** , see [Create environments (Terraform)](https://docs.cloud.google.com/composer/docs/composer-1/terraform-create-environments).




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

  6. Enable the Managed Airflow API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=composer.googleapis.com)

  7. To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

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

  1. In the Google Cloud console, go to the **Create environment** page.

[Go to Create environment](https://console.cloud.google.com/composer/environments/create-composer-1)

  2. In the **Name** field, enter `example-environment`.

  3. In the **Location** drop-down list, select a region for the Managed Airflow environment. This guide uses `us-central1` region.

  4. For other environment configuration options, use the provided defaults.

  5. Click **Create** and wait until the environment is created.

**Note:** It takes approximately 25 minutes for Managed Airflow to create your environment.
  6. When done, a green check mark is displayed next to the environment name.




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

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment, `example-environment`. The **Environment details** page opens.

  3. Click **Open DAGs folder**. The **Bucket details** page opens.

  4. Click **Upload files** and then select your copy of `quickstart.py`.

  5. To upload the file, click **Open**.




## View the DAG

After you upload the DAG file, Airflow does the following:

  1. Parses the DAG file that you uploaded. It might take a few minutes for the DAG to become available to Airflow.
  2. Adds the DAG to the list of available DAGs.
  3. Executes the DAG according to the schedule you provided in the DAG file.



Check that your DAG is processed without errors and is available in Airflow by viewing it in DAG UI. DAG UI is Managed Airflow interface for viewing DAG information in Google Cloud console. Managed Airflow also provides access to [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface), which is a native Airflow web interface.

  1. Wait about five minutes to give Airflow time to process the DAG file that you uploaded previously, and to complete the first DAG run (explained later).

  2. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  3. In the list of environments, click the name of your environment, `example-environment`. The **Environment details** page opens.

  4. Go to the **DAGs** tab.

  5. Check that the `composer_quickstart` DAG is present in the list of DAGs.

[ ![The list of DAGs displays the composer_quickstart DAG with
    additional information such as state and schedule](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-dag-list.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-dag-list.png) **Figure 1.** The list of DAGs displays the composer_quickstart DAG (click to enlarge) **Note:** The `airflow_monitoring` DAG is used by Managed Airflow to monitor the health of your environment.



## View DAG run details

A single execution of a DAG is called a _DAG run_. Airflow immediately executes a DAG run for the example DAG because the start date in the DAG file is set to yesterday. In this way, Airflow catches up to the specified DAG's schedule.

The example DAG contains one task, `print_dag_run_conf`, which runs the `echo` command in the console. This command outputs meta information about the DAG (DAG run's numeric identifier).

  1. On the **DAGs** tab, click `composer_quickstart`. The **Runs** tab for the DAG opens.

  2. In the list of DAG runs, click the first entry.

[ ![The list of DAG runs shows the recent DAG run \(its execution date
    and status\)](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-dag-runs-list.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-dag-runs-list.png) **Figure 2.** The list of DAG runs for the composer_quickstart DAG (click to enlarge) 
  3. DAG run details are displayed, detailing the information about individual tasks of the example DAG.

[ ![The list of tasks with an entry print_dag_run_conf, its start
    time, end time, and duration](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-task-list.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-task-list.png) **Figure 3.** The list of tasks that were executed in the DAG run (click to enlarge) 
  4. The **Logs for DAG run** section lists logs for all tasks in the DAG run. You can see the output of the `echo` command in the logs.

[ ![Log entries of the task, one of them is Output and the other lists
    an identifier](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-task-logs.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-quickstart-task-logs.png) **Figure 4.** Logs of the print_dag_run_conf task (click to enlarge) 



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

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

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
