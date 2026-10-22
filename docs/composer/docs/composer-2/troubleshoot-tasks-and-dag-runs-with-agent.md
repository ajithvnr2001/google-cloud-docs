---
url: https://docs.cloud.google.com/composer/docs/composer-2/troubleshoot-tasks-and-dag-runs-with-agent/
title: Troubleshoot Airflow tasks and DAG runs with Managed Airflow Agent \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:32.020790+00:00
---

# Troubleshoot Airflow tasks and DAG runs with Managed Airflow Agent  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/troubleshoot-tasks-and-dag-runs-with-agent/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Troubleshoot Airflow tasks and DAG runs with Managed Airflow Agent Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/troubleshoot-tasks-and-dag-runs-with-agent "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

Managed Airflow Agent can help you understand, diagnose, and resolve issues with failed Airflow tasks and DAG runs.

## Before you begin

  * Conversational Analytics API that runs Managed Airflow Agent has its [own data residency policy](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency). Your conversation might be handled in a region different from your environment's location.



## Investigate failed Airflow tasks or DAG runs

To investigate a failed Airflow task or DAG run:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. Select an environment to view its details.

  3. On the **Environment details** page, go to the **DAGs** tab.

  4. Click the name of a DAG.

  5. On the **DAG details** page, go to the **Run history** tab.

  6. Locate a failed DAG run. You can investigate a whole DAG run or a specific failed task:

     * To investigate a DAG run:

       1. Click auto_awesome **Investigate** next to the failed DAG run name.

       2. In the **Investigate DAG run failure** dialog, click **Investigate**.

     * To investigate an Airflow task:

       1. Click the name of the failed DAG run to display a list of tasks.

       2. In the **State** column of the failed Airflow task, click auto_awesome **Investigate**.

       3. In the **Investigate task failure** dialog, click **Investigate**.

  7. The **Ask agent** panel opens and Managed Airflow Agent starts invesitgating the DAG run failure. Wait until the agent finishes the analysis and then review the diagnostic report, which consists of several sections:

     * **Problem** describes the root cause of the issue.
     * **Evidence** points at specific artifacts that support the agent's conclusions.
     * **Recommendation** provides specific steps for addressing the issue.



## Example investigation

This example shows a process of analyzing a failing task.

  1. On the **Monitoring** > **DAG Statistics** dashboard, observe failing DAG runs:

[ ![The Completed DAG runs graph on the Monitoring dashboard shows
    several failed DAG runs](https://docs.cloud.google.com/static/composer/docs/images/composer-investigation-monitoring-failing-dag-runs.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-investigation-monitoring-failing-dag-runs.png) **Figure 1.** Completed DAG runs graph (click to enlarge) 
  2. Navigate to the **DAGs** tab. The **Failed runs (1h)** column shows that the `create_large_txt_file_print_logs` DAG had several failed runs in the past hour. Click the name of the DAG.

[ ![The list of DAGs shows failed DAG runs for the
    create_large_txt_file_print_logs DAG](https://docs.cloud.google.com/static/composer/docs/images/composer-investigation-dags-list-failed-runs.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-investigation-dags-list-failed-runs.png) **Figure 2.** List of DAGs with DAG run statistics (click to enlarge) 
  3. Click one of the failed DAG runs, then click auto_awesome **Investigate** next to the failed Airflow task entry.

[ ![The list of tasks in a DAG shows a failed Airflow task with an
    investigate button next to it](https://docs.cloud.google.com/static/composer/docs/images/composer-investigation-failing-task-investigate.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-investigation-failing-task-investigate.png) **Figure 3.** List of tasks in the failing DAGs (click to enlarge) 
  4. Wait until the agent completes its report.

  5. Review the diagnostic report. In this particular example, the task failed without generating logs, but Managed Airflow Agent was able to find the cause of the failure in the Airflow scheduler logs, where the task was terminated as a zombie:
         
         ### **1. Problem**
         
         The task `create_huge_file` in DAG `dag_simulation` failed because the
         Airflow worker executing it ran out of memory (OOM). This caused the task
         container or process to be abruptly terminated, preventing it from sending
         heartbeats to the scheduler. As a result, the scheduler detected it as a
         zombie task and marked it as failed.
         
         ### **2. Evidence**
         
         *  **Scheduler Log (Zombie Detection)**:
            Detected a task instance without a heartbeat:
            filepath='dag-simulation.py'
            bundle_name='dags-folder' bundle_version=None msg="{'DAG Id':
            'dag_simulation', 'Task Id': 'create_huge_file', 'Run Id':
            'manual__2026-11-25T12:42:50.190250+00:00', 'Hostname':
            'airflow-worker-2lxm2', 'External Executor Id':
            'cfc98619-0de6-4699-96e6-7ba8a5a581aa'}"
         
         *  ...
         

  6. Finally, check the proposed recommendations. Managed Airflow Agent summarizes the evidence and provides recommendations for fixing the issue. In this example, the task failed because an Airflow worker didn't have enough resources to process it. This is supported by evidence of the worker Pod being restarted multiple times with an OOM error, and the task being subsequently terminated by the scheduler as a zombie task.
         
         ### **3. Recommendation**
         To resolve this issue, you must prevent the task from consuming unbound
         memory. Depending on your workflow:
         
         *  **Fix Code Logic (Highly Recommended)**: Avoid loading large datasets
            completely into worker memory. Implement chunk-based processing or
            streaming, or set up explicit safety limits. For example, if you need to
            limit memory allocation or process in bounded batches, do not keep
            references to old chunks in memory: ...
         
         *  **Scale Worker Memory**: If processing massive datasets in memory is
            unavoidable, consider upgrading the resource limits (RAM/CPU) of your
            Airflow worker pools or offloading the heavy processing step to external
            services.
         




## What's next

  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)
  * [Troubleshooting scheduling](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-scheduling)
  * [Troubleshooting PyPI package installation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-package-installation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
