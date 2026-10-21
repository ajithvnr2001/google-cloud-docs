---
url: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-kubernetes-executor/
title: Troubleshooting KubernetesExecutor tasks \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:39.603115+00:00
---

# Troubleshooting KubernetesExecutor tasks  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-kubernetes-executor/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Troubleshooting KubernetesExecutor tasks Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)

This page describes how to troubleshoot issues with [tasks run by KubernetesExecutor](https://docs.cloud.google.com/composer/docs/composer-3/use-celery-kubernetes-executor) and provides solutions for common issues.

## General approach to troubleshooting KubernetesExecutor

To troubleshoot issues with a task executed with KubernetesExecutor, do the following actions in the listed order:

  1. Check logs of the task in the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-3/view-dags#runs-history) or [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).

  2. Check scheduler logs in Google Cloud console:

     1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     2. In the list of environments, click the name of your environment. The **Environment details** page opens.

     3. Go to the **Logs** tab and check the **Airflow logs** > **Scheduler** section.

     4. For a given time range, inspect the KubernetesExecutor worker pod that was running the task. If the pod no longer exists, skip this step. The pod has the `airflow-k8s-worker` prefix and a DAG or a task name in its name. Look for any reported issues such as a failed task or the task being unschedulable.




## Common troubleshooting scenarios for KubernetesExecutor

This section lists common troublehooting scenarions that you might encounter with KubernetesExecutor.

### The task gets to the `Running` state, then fails during the execution.

Symptoms:

  * There are logs for the task in Airflow UI and on the **Logs** tab in the **Workers** section.



Solution: The task logs indicate the problem.

### Task instance gets to the `queued` state, then it is marked as `UP_FOR_RETRY` or `FAILED` after some time.

Symptoms:

  * There are no logs for task in Airflow UI and on the **Logs** tab in the **Workers** section.
  * There are logs on the **Logs** tab in the **Scheduler** section with a message that the task is marked as `UP_FOR_RETRY` or `FAILED`.



Solution:

  * Inspect scheduler logs for any details of the issue.



Possible causes:

  * If the scheduler logs contain the `Adopted tasks were still pending after...` message followed by the printed task instance, check that CeleryKubernetesExecutor is enabled in your environment.



### The task instance gets to the `Queued` state and is immediately marked as `UP_FOR_RETRY` or `FAILED`

Symptoms:

  * There are no logs for the task in Airflow UI and on the **Logs** tab in the **Workers** section.
  * The scheduler logs on the **Logs** tab in the **Scheduler** section has the `Pod creation failed with reason ... Failing task` message, and the message that the task is marked as `UP_FOR_RETRY` or `FAILED`.



Solution:

  * Check scheduler logs for the exact response and failure reason.



Possible reason:

If the error message is `quantities must match the regular expression ...`, then the issue is most-likely caused by a custom values set for k8s resources (requests/limits) of task worker pods.

### KubernetesExecutor tasks fail without logs when a large number of tasks is executed

When your environment executes a large number of tasks [with KubernetesExecutor](https://docs.cloud.google.com/composer/docs/composer-3/use-celery-kubernetes-executor) or [KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator) at the same time, Managed Airflow (Gen 3) doesn't accept new tasks until some of the existing tasks are finished. Extra tasks are marked as failed, and Airflow retries them later, if you define retries for the tasks (Airflow does this by default).

**Symptom:** Tasks executed with KubernetesExecutor or KubernetesPodOperator fail without task logs in Airflow UI or DAG UI. In the [scheduler's logs](https://docs.cloud.google.com/composer/docs/composer-3/view-logs#streaming), you can see error messages similar to the following:
    
    
    pods \"airflow-k8s-worker-*\" is forbidden: exceeded quota: k8s-resources-quota,
    requested: pods=1, used: pods=*, limited: pods=*","reason":"Forbidden"
    

**Possible solutions:**

  * Adjust the DAG run schedule so that tasks are distributed more evenly over time.
  * Reduce the number of tasks by consolidating small tasks.



**Workaround:**

If you prefer tasks to stay in the scheduled state until your environment can execute them, you can define an [Airflow pool](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/pools.html) with the limited number of slots in the Airflow UI and then associate all container-based tasks with this pool. We recommend to set the number of slots in the pool to 50 or less. Extra tasks will stay in the scheduled state until the Airflow pool has a free slot to execute them. If you use this workaround without applying possible solutions, you can still experience a large queue of tasks in the Airflow pool.

## What's next

  * [Use CeleryKubernetesExecutor](https://docs.cloud.google.com/composer/docs/composer-3/use-celery-kubernetes-executor)
  * [Use KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator)
  * [Troubleshooting scheduling](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-scheduling)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
