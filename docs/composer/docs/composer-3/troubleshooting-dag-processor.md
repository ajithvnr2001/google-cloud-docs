---
url: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dag-processor/
title: Troubleshooting DAG Processor issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:44.101834+00:00
---

# Troubleshooting DAG Processor issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dag-processor/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Troubleshooting DAG Processor issues Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dag-processor "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page refers only to issues related to [DAG File Processing](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/dagfile-processing.html), for issues scheduling tasks, see [Troubleshooting Airflow scheduler issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling).

## Troubleshooting Workflow

### Inspect DAG processor logs

If you have complex DAGs, then Airflow DAG processors might not parse all your DAGs. This might lead to many issues that have the following symptoms.

**Symptoms:**

  * If a DAG processor encounters problems when parsing your DAGs, then it might lead to a combination of the listed issues. If DAGs are generated dynamically, these issues might be more impactful compared to static DAGs.

    * DAGs are not visible in Airflow UI and DAG UI.
    * DAGs are not scheduled for execution.
    * There are errors in the DAG processor logs, for example:
    
    dag-processor-manager [2023-04-21 21:10:44,510] {manager.py:1144} ERROR -
    Processor for /home/airflow/gcs/dags/dag-example.py with PID 68311 started
    at 2023-04-21T21:09:53.772793+00:00 has timed out, killing it.
    

or
    
    dag-processor-manager [2023-04-26 06:18:34,860] {manager.py:948} ERROR -
    Processor for /home/airflow/gcs/dags/dag-example.py exited with return
    code 1.
    

  * Airflow tasks that are scheduled for execution are cancelled and DAG runs for DAGs that failed to be parsed might be marked as `failed`. For example:
        
        airflow-scheduler Failed to get task '<TaskInstance: dag-example.task1--1
        manual__2023-04-17T10:02:03.137439+00:00 [removed]>' for dag
        'dag-example'. Marking it as removed.
        




**Solution:**

  * Increase parameters related to DAG parsing:

    * Increase [`[core]dagbag_import_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dagbag-import-timeout) to at least 120 seconds (or more, if required).

    * Increase [`[core]dag_file_processor_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dag-file-processor-timeout) to at least 180 seconds (or more, if required). This value must be higher than `[core]dagbag_import_timeout`.

  * Correct or remove DAGs that cause problems to DAG processors.




### Inspecting DAG parse times

To verify if the issue happens at DAG parse time, follow these steps.

###  Console 

In Google Cloud console you can use the **Monitoring** page and the **Logs** tab to inspect DAG parse times.

Inspect DAG parse times with the Managed Service for Apache Airflow Monitoring page:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments][console-list-env]

  2. In the list of environments, click the name of your environment. The **Monitoring** page opens.

  3. In the **Monitoring** tab, select **DAG Statistics** and review the **Total parse time for all DAG files** chart to identify possible issues. We recommend to monitor this chart for some time to identify DAG parsing issues over several DAG parsing cycles. 

![The Total parse time for all DAG files is displayed on the Monitoring tab](https://docs.cloud.google.com/static/composer/docs/images/composer-dag-runs-section.png)




Inspect DAG parse times with the **Managed Service for Apache Airflow Logs** tab:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments][console-list-env]

  2. In the list of environments, click the name of your environment. The **Monitoring** page opens.

  3. Go to the **Logs** tab, and from the **All logs** navigation tree select the **DAG processor manager** section.

  4. Review `dag-processor-manager` logs and identify possible issues.

![The DAG processor logs will show DAG parsing times](https://docs.cloud.google.com/static/composer/docs/images/airflow2-dag-parsing-times.png)




###  gcloud 

Use the `dags report` command to see the parse time for all your DAGs.
    
    
    gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        dags report
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



The output of the command looks similar to the following:
    
    
    file                  | duration       | dag_num | task_num | dags
    ======================+================+=========+==========+===================
    /manydagsbig.py       | 0:00:00.038334 | 2       | 10       | serial-0,serial-0
    /airflow_monitoring.py| 0:00:00.001620 | 1       | 1        | airflow_monitoring
    

Look for the **duration** value for each of the dags listed in the table. A large value might indicate that one of your DAGs is not implemented in an optimal way. From the output table, you can identify which DAGs have a long parsing time.

## Troubleshooting issues at DAG parse time

The following sections describe symptoms and potential fixes for some common issues at DAG parse time.

### Make the DAG processor ignore unnecessary files

You can improve performance of the Airflow DAG processor by skipping unnecessary files in the DAGs folder. Airflow DAG processor ignores files and folders specified in the `.airflowignore` file. 

To make the Airflow DAG processor ignore unnecessary files:

  1. Create an `.airflowignore` file.
  2. In this file, list files and folders that should be ignored.
  3. [Upload this file](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags#adding) to the `/dags` folder in your environment's bucket.



For more information about the `.airflowignore` file format, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#airflowignore).

### Airflow processes paused DAGs

You can pause DAGs to stop them from running. This saves resources of Airflow workers.

Airflow DAG processors continue parsing paused DAGs. If you want to improve the performance of DAG processors, use [`.airflowignore`](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#airflowignore) or delete paused DAGs from the DAGs folder.

## Common Issues

The following sections describe symptoms and potential fixes for some common parsing issues.

### DAG load import timeout

Symptom:

  * In the Airflow web interface, at the top of the DAGs list page, a red alert box shows `Broken DAG: [/path/to/dagfile] Timeout`.
  * In Cloud Monitoring: The `airflow-scheduler` logs contain entries similar to:

    * `ERROR - Process timed out`
    * `ERROR - Failed to import: /path/to/dagfile`
    * `AirflowTaskTimeout: Timeout`



Fix:

[Override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) the `dag_file_processor_timeout` Airflow configuration option and allow more time for DAG parsing:

Section | Key | Value  
---|---|---  
`core` | `dag_file_processor_timeout` | New timeout value  
  
### A DAG is not visible in Airflow UI or DAG UI and the scheduler does not schedule it

The DAG processor parses each DAG before it can be scheduled by the scheduler and before a DAG becomes visible in the [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) or [DAG UI](https://docs.cloud.google.com/composer/docs/composer-3/view-dags).

The following Airflow configuration options define timeouts for parsing DAGs:

  * [`[core]dagbag_import_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dagbag-import-timeout) defines how much time the DAG processor has to parse a single DAG.

  * [`[core]dag_file_processor_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dag-file-processor-timeout) defines the total amount of time the DAG processor can spend on parsing all DAGs.




If a DAG is not visible in the Airflow UI or DAG UI:

  * Check DAG processor logs if the DAG processor is able to correctly process your DAG. In case of problems, you might see the following log entries in the DAG processor or scheduler logs:
        
        [2020-12-03 03:06:45,672] {dag_processing.py:1334} ERROR - Processor for
        /usr/local/airflow/dags/example_dag.py with PID 21903 started at
        2020-12-03T03:05:55.442709+00:00 has timed out, killing it.
        

  * Check scheduler logs to see if the scheduler works correctly. In case of problems, you might see the following log entries in scheduler logs:
        
        DagFileProcessorManager (PID=732) last sent a heartbeat 240.09 seconds ago! Restarting it
        Process timed out, PID: 68496
        




**Solutions** :

  * Fix all DAG parsing errors. The DAG processor parses multiple DAGs, and in rare cases parsing errors of one DAG can negatively impact the parsing of other DAGs.

  * If the parsing of your DAG takes more than the amount of seconds defined in [`[core]dagbag_import_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dagbag-import-timeout), then increase this timeout.

  * If the parsing of all your DAGs takes more than the amount of seconds defined in [`[core]dag_file_processor_timeout`](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#dag-file-processor-timeout), then increase this timeout.

  * If your DAG takes a long time to parse, it can also mean that it is not implemented in an optimal way. For example, if it reads read many environment variables, or performs calls to external services or Airflow database. To the extent possible, avoid performing such operations in global sections of DAGs.

  * Increase CPU and memory resources for the DAG processor so it can work faster.

  * [Lower the frequency of DAG parsing](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#min-file-process-interval).

  * [Lower the load on the Airflow database](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling#database-overload-symptoms).




## What's next

  * [Troubleshooting file synchronization issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-cloud-storage)
  * [Troubleshooting Airflow scheduler issues](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
