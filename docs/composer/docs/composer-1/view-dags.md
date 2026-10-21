---
url: https://docs.cloud.google.com/composer/docs/composer-1/view-dags/
title: View DAGs, DAG runs, and tasks \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:02.909200+00:00
---

# View DAGs, DAG runs, and tasks  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/view-dags/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  View DAGs, DAG runs, and tasks Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/view-dags "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/view-dags "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page explains how to get information about DAGs in your environment.

## Ways to view information about DAGs

Managed Airflow provides several ways to get detailed information about DAGs in your environment:

  * DAG UI is a section of Google Cloud console interface for Managed Airflow dedicated to viewing and monitoring DAGs, DAG runs, and individual tasks.
  * [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface) is the built-in web interface of Airflow.
  * [Airflow CLI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli) is the command-line interface of Airflow. You can get information about DAGs by running Airflow CLI commands with `gcloud`.



## About Managed Airflow DAG UI

DAG UI is a section of Google Cloud console interface for Managed Airflow dedicated to viewing and monitoring DAGs, DAG runs, and individual tasks.

In DAG UI, you can:

  * View a list of DAGs in your environment, including schedule intervals, DAG states, and descriptions.

  * Pause, unpause, and [trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-1/schedule-and-trigger-dags#manual).

  * View DAG run details, including successful, active, and failed runs, time since the last completed run. For each DAG, you can see the history of DAG runs and task instances associated with this particular DAG, including logs for executed tasks.

  * Filter DAG run details. For example, you can pick a time interval and create queries to select the information that you need.

  * View detailed information about individual DAGs and tasks. This includes visualized DAG diagrams, information about the tasks within a DAG, DAG source code, and extra information about DAGs.




## Before you begin

  * Make sure that your account has a role that can access DAG UI and view DAG details. For more information, see [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control).

  * DAG UI requires enabled [DAG serialization](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization).

  * DAG UI is supported in Managed Airflow 1.17.8 and later versions. 




## View the list of DAGs for your environment

###  Console 

The **DAGs** tab of your environment shows the list of DAGs along with DAG run details for each DAG.

To view the list of DAGs:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **DAG list** column, follow the **DAGs** link for your environment.




You can use filters to view the details only for certain DAGs or for certain conditions. For example:

  1. Select the **Filters** field.
  2. From the drop-down list, select the **DAG id** property.
  3. Specify the identifier of the DAG. The results show details only for the selected DAG.
  4. (Optional) To include more DAGs, add `OR` operators followed by DAG ids.
  5. (Optional) To filter on other conditions, add other properties in the **Filters** field. For example, you can filter for DAGs with failed runs by specifying `Failed runs:>0`.



###  Airflow UI 

To view the list of DAGs in the Airflow UI:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. Log in with the Google account that has the appropriate permissions.

  4. In the Airflow UI, on the **DAGs** page, a list of DAGs for your environment is displayed.




###  gcloud 

In Airflow 1.10.*, run the `list_dags` Airflow CLI command:
    
    
      gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        list_dags
    

In Airflow 2, run the `dags list` Airflow CLI command:
    
    
      gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        dags list -- -o plain
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



## View the history of DAG runs and tasks

###  Console 

The **Runs** tab on the **DAG details** page shows the history of DAG runs for an individual DAG.

To view the history of DAG runs:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **DAG list** column, follow the **DAGs** link for your environment.

  3. Select a DAG.

  4. On the **DAG details** page, go to the **Runs** tab.

  5. Select a DAG run from the list to view the DAG run details, such as the state of task instances for this DAG run, the number of tries and the execution duration. You can select individual tasks to view task instance logs.




###  Airflow UI 

To view the list of DAGs in the Airflow UI:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. Log in with the Google account that has the appropriate permissions.

  4. In the Airflow UI, in the menu, select **Browse** > **DAG Runs**. The **DAG Runs** page displays DAG runs for your environment. You can follow the link in the **Run ID** column to get additional information about tasks.




###  gcloud 

In Airflow 1.10.*, run the `list_dag_runs` Airflow CLI command:
    
    
      gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        list_dag_runs -- DAG_ID
    

In Airflow 2, run the `dags list-runs` Airflow CLI command:
    
    
      gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        dags list-runs -- -d DAG_ID
    
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `DAG_ID` with the name of the DAG.



You can get additional information about task instances by running `tasks state` and `tasks states-for-dag-run` Airflow CLI commands.

For more information, see [Access Airflow CLI](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-cli) and the Airflow CLI reference [for Airflow 1](https://airflow.apache.org/docs/apache-airflow/1.10.12/cli-ref.html) and [Airflow 2](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html).

## View DAG diagrams

###  Console 

The **Diagram** tab on the **DAG details** page show the visualisation of a DAG with task dependencies.

To view the diagram of a DAG:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **DAG list** column, follow the **DAGs** link for your environment.

  3. Select a DAG.

  4. On the **DAG details** page, go to the **Diagram** tab.

  5. (Optional) To see additional information about tasks, select individual tasks on the diagram.




###  Airflow UI 

To view the diagram of a DAGs in the Airflow web interface:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. Log in with the Google account that has the appropriate permissions.

  4. In the Airflow UI, on the **DAGs** page, a list of DAGs for your environment is displayed.

  5. For your DAG, in the **Links** column, follow the **Graph** link.




## View DAG source code and additional information about DAGs

###  Console 

You can view the source code of your DAGs and additional information such as DAG identifiers and links to DAG definition files in the environment's bucket.

**Note:** It is not possible to edit the source code of your DAGs on this tab.

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **DAG list** column, follow the **DAGs** link for your environment.

  3. Select a DAG.

  4. To view the DAG source code, go to the **Diagram** tab.

  5. To view additional information about the DAG, go to the **Source** tab.




###  Airflow UI 

To view the diagram of a DAGs in the Airflow web interface:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. Log in with the Google account that has the appropriate permissions.

  4. In the Airflow web interface, on the **DAGs** page, click on the name of your DAG.

  5. In the page with DAG details, navigate to available tabs to view additional information about the DAG.




## What's next

  * [Add and update DAGs](https://docs.cloud.google.com/composer/docs/composer-1/manage-dags)
  * [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-1/schedule-and-trigger-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
