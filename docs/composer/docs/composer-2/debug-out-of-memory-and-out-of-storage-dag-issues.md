---
url: https://docs.cloud.google.com/composer/docs/composer-2/debug-out-of-memory-and-out-of-storage-dag-issues/
title: Debug out of memory and out of storage DAG issues \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:07.511395+00:00
---

# Debug out of memory and out of storage DAG issues  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/debug-out-of-memory-and-out-of-storage-dag-issues/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Debug out of memory and out of storage DAG issues Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/debug-out-of-memory-and-out-of-storage-dag-issues "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | Managed Airflow (Legacy Gen 1)

This tutorial provides steps to debug a failed Airflow DAG in Managed Airflow and diagnose worker resource-related issues, such as lack of worker memory or storage space, with the help of logs and environment monitoring.

## Introduction

This tutorial focuses on resource-related issues to demonstrate ways to debug a DAG.

Lack of allocated worker resources causes DAG failures. If an Airflow task runs out of memory or storage, you might see an Airflow exception, such as:
    
    
    WARNING airflow.exceptions.AirflowException: Task received SIGTERM signal
    INFO - Marking task as FAILED.
    

or
    
    
    Task exited with return code Negsignal.SIGKILL
    

In such cases, the general recommendation is to increase the Airflow worker resources or reduce the number of tasks per worker. However, because Airflow exceptions can be generic, it might be challenging to identify the particular resource that is causing the problem.

This tutorial explains how you can diagnose the reason for a DAG failure and identify the type of resource that causes issues by debugging two example DAGs that fail because of a lack of worker memory and storage.

## Objectives

  * Run example DAGs that fail because of the following reasons:

    * Lack of worker memory
    * Lack of worker storage
  * Diagnose the reasons of the failure

  * Increase the allocated worker resources

  * Test the DAGs with new resource limits




## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Managed Airflow](https://docs.cloud.google.com/composer/pricing) (see [additional costs](https://docs.cloud.google.com/composer/pricing#additional-costs))
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring#pricing)



When you finish this tutorial, you can avoid continued billing by deleting the resources you created. For more details, see Clean up.

## Before you begin

This section describes actions that are required before you start the tutorial.

### Create and configure a project

For this tutorial, you need a Google Cloud [project](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). Configure the project in the following way:

  1. In the Google Cloud console, [select or create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects):

[Go to Project Selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your project. [Learn how to check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Make sure that your Google Cloud project user has the following [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to create the necessary resources:

     * **Environment and Storage Object Administrator** (`roles/composer.environmentAndStorageObjectAdmin`)
     * **Compute Admin** (`roles/compute.admin`)
     * **Monitoring Editor** (`roles/monitoring.editor`)



### Enable APIs for your project

Enable the Managed Airflow API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=composer.googleapis.com)

### Create your Managed Airflow environment

[Create a Managed Airflow (Gen 2) environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#basic-setup).

**Important:** Make sure that you use the **Small environment preset** in order to reproduce the errors when using the examples provided further in this tutorial. This is the default preset when creating an environment through Google Cloud console.

[As a part of creating the environment](https://docs.cloud.google.com/composer/docs/composer-2/create-environments#grant-permissions), you grant the **Cloud Composer v2 API Service Agent Extension** (`roles/composer.ServiceAgentV2Ext`) role to the Composer Service Agent account. Managed Airflow uses this account to perform operations in your Google Cloud project.

### Check worker resource limits

Check the Airflow worker resource limits in your environment:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Go to **Resources** > **Workloads configuration** > Worker.

  5. Check that the values are 0.5 vCPUs, 1.875 GB memory, and 1 GB storage. These are the Airflow worker resource limits that you work with in the next steps of this tutorial.




## Example: Diagnose out-of-memory issues

[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the following sample DAG to the environment that you created in the previous steps. In this tutorial, this DAG is named `create_list_with_many_strings`.

This DAG contains one task that executes the following steps:

  1. Creates an empty list `s`.
  2. Runs a cycle to append the `More` string to the list.
  3. Prints how much memory the list consumes and waits 1 second in each 1 minute iteration.

**Warning:** This DAG **simulates an out-of-memory issue** , which can potentially disrupt operations in your environment.
    
    
    import time
    
    import airflow
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    import sys
    from datetime import timedelta
    
    default_args = {
        'start_date': airflow.utils.dates.days_ago(0),
        'retries': 0,
        'retry_delay': timedelta(minutes=10)
    }
    
    dag = DAG(
        'create_list_with_many_strings',
        default_args=default_args,
        schedule=None)
    
    
    def consume():
        s = []
        for i in range(120):
            for j in range(1000000):
                s.append("More")
            print(f"i={i}; size={sys.getsizeof(s) / (1000**3)}GB")
            time.sleep(1)
    
    
    t1 = PythonOperator(
        task_id='task0',
        python_callable=consume,
        dag=dag,
        depends_on_past=False,
        retries=0
    )
    

### Trigger the sample DAG

Trigger the sample DAG, `create_list_with_many_strings`:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. In the Airflow UI, on the **DAGs** page, click the **Trigger DAG** button for your DAG.

  4. Click **Trigger**.

  5. On the **DAGs** page, click the task you triggered and review the output logs to make sure your DAG started running.




While the task is running, the output logs will print the memory size in GB that the DAG is using.

After several minutes, the task will fail because it exceeds the Airflow worker memory limit of 1.875 GB.

**Note:** If you trigger the DAG that exceeds the memory limit simultaneously with any other sample DAG, you will see that, if one of the tasks exceeds the memory limit and fails, other running tasks will fail, too, even if they don't consume memory.

### Diagnose the failed DAG

If you were running multiple tasks at the time of the failure, consider running only one task and diagnosing resource pressure during that time to identify which tasks cause resource pressure and which resources you need to increase.

#### Review the Airflow task logs

Observe that the task from the `create_list_with_many_strings` DAG has a `Failed` state.

Review the task's logs. You will see the following log entry:
    
    
    ```none
    {local_task_job.py:102} INFO - Task exited with return code
    Negsignal.SIGKILL
    ```
    
    `Netsignal.SIGKILL` might be an indication of your task using more memory
    than the Airflow worker is allocated. The system sends
    the `Negsignal.SIGKILL` signal to avoid further memory consumption.
    

#### Review workloads

Review workloads to check that your task's load does not cause the node where the Pod runs to exceed the memory consumption limit:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. In **Resources** > **GKE cluster** > **Workloads** , click **view cluster workloads**.

  5. Check if some of the workload pods have statuses similar to the following:
         
         Error with exit code 137 and 1 more issue.
         ContainerStatusUnknown with exit code 137 and 1 more issue
         

`Exit code 137` means a container or Pod is trying to use more memory than allowed. The process gets terminated to prevent memory usage.




#### Review the environment health and resource consumption monitoring

Review the environment health and resource consumption monitoring:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Monitoring** tab and select **Overview**.

  4. On the **Environment overview** panel, locate the **Environment Health (Airflow Monitoring DAG)** graph. It contains a red area, which corresponds to the time when logs started printing errors.

  5. Select **Workers** , and find the **Total workers memory usage** graph. Observe that the **Memory usage** line has a spike at the time when the task was running.


[ ![The Memory usage line has a spike at the time when the
    task was running](https://docs.cloud.google.com/static/composer/docs/images/composer-workers-memory-usage.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-workers-memory-usage.png) **Figure 1.** Total workers memory usage graph (click to enlarge) 

Even though the memory usage line on the graph does not reach the limit, when diagnosing the reasons for failure, you need to take into account memory usage by individual workers. Each worker uses a portion of its memory to run other containers that perform actions necessary for worker's operation, such as syncing its DAG files with the environment's bucket. The actual amount of memory available to a worker to execute Airflow tasks is less than its memory limit. If a worker reaches the limit of the actual memory available to it, the executed task can fail due to insufficient worker memory. In such cases, you can observe task failures even though the line on the total workers memory usage graph doesn't reach the memory limit.

**Note:** If the memory consumption level is growing too fast, the memory usage line might not capture the real resource consumption level properly. The `airflow_monitoring` DAG is a per-environment liveness health check that is used to populate the [`environment/healthy` monitoring metric](https://docs.cloud.google.com/composer/docs/composer-2/monitor-environments). This DAG lets you to use Cloud Monitoring features such as metric graphs, or setting alerts when your environment becomes unhealthy. It runs every 5 minutes and collects the metrics, which means it might not capture the resource usage between the runs.

### Increase the worker memory limit

**Note:** changing the worker's CPU or memory restarts workers, which might affect running tasks. We recommend doing it when no DAGs are running.

Allocate additional worker memory in order for the sample DAG to succeed:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Find the **Resources** > **Workloads** configuration and click **Edit**.

  5. In the **Worker** section, in the **Memory** field, specify the new memory limit for Airflow workers. In this tutorial, use 3 GB.

  6. Save the changes and allow several minutes for your Airflow workers to restart.




### Test your DAG with the new memory limit

Trigger the `create_list_with_many_strings` DAG again and wait until it finishes running.

  1. In the output logs of your DAG run, you will see `Marking task as SUCCESS`, and the task's state will indicate **Success**.

  2. Review the **Environment overview** section in the **Monitoring** tab and make sure that there are no red areas.

  3. Click the **Workers** section and find the **Total workers memory usage** graph. You will see that the **Memory limit** line reflects the change in the memory limit, and the **Memory usage** line is far below the actual allocatable memory limit.




## Example: Diagnose out-of-storage issues

In this step, you upload two DAGs that create large files. The first DAG creates a large file. The second DAG creates a large file and imitates a long-running operation.

The size of the file in both DAGs exceeds the default Airflow worker storage limit of 1 GB but the second DAG has an additional wait task to extend its duration artificially.

You will investigate the differences in the behavior of both DAGs in the next steps.

**Note:** DAGs in this tutorial create local files. In a production setting, avoid storing any file or config in the local file system because the next task will likely run on a different Airflow worker without access to the file.

### Upload a DAG that creates a large file

[Upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the following sample DAG to the environment that you created in the previous steps. In this tutorial, this DAG is named `create_large_txt_file_print_logs`.

This DAG contains one task that executes the following steps:

  1. Writes a 1.5 GB `localfile.txt` file to the Airflow worker storage.
  2. Prints the size of the created file by using the Python `os` module.
  3. Prints the duration of the DAG run every 1 minute.

**Warning:** This DAG **simulates an out-of-storage issue** , which can potentially disrupt operations in your environment.
    
    
    import airflow
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    import os
    from datetime import timedelta
    import time
    
    default_args = {
        'start_date': airflow.utils.dates.days_ago(0),
        'retries': 0,
        'retry_delay': timedelta(minutes=10)
    }
    
    dag = DAG(
        'create_large_txt_file_print_logs',
        default_args=default_args,
        schedule=None)
    
    
    def consume():
        size = 1000**2  # bytes in 1 MB
        amount = 100
    
        def create_file():
            print(f"Start creating a huge file")
            with open("localfile.txt", "ab") as f:
                for j in range(15):
                    f.write(os.urandom(amount) * size)
            print("localfile.txt size:", os.stat("localfile.txt").st_size / (1000**3), "GB")
    
        create_file()
        print("Success!")
    
    
    t1 = PythonOperator(
        task_id='create_huge_file',
        python_callable=consume,
        dag=dag,
        depends_on_past=False,
        retries=0)
    

### Upload a DAG that creates a large file in a long-running operation

To imitate a long-running DAG and investigate the impact of the task duration on the end state, [upload](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags#adding) the second sample DAG to your environment. In this tutorial, this DAG is named `long_running_create_large_txt_file_print_logs`.

This DAG contains one task that executes the following steps:

  1. Writes a 1.5 GB `localfile.txt` file to the Airflow worker storage.
  2. Prints the size of the created file by using the Python `os` module.
  3. Waits 1 hour 15 minutes to imitate some time needed for operations with the file, for example, reading from the file.
  4. Prints the duration of the DAG run every 1 minute.

**Warning:** This DAG **simulates an out-of-storage issue** , which can potentially disrupt operations in your environment.
    
    
    import airflow
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    import os
    from datetime import timedelta
    import time
    
    default_args = {
        'start_date': airflow.utils.dates.days_ago(0),
        'retries': 0,
        'retry_delay': timedelta(minutes=10)
    }
    
    dag = DAG(
        'long_running_create_large_txt_file_print_logs',
        default_args=default_args,
        schedule=None)
    
    
    def consume():
        size = 1000**2  # bytes in 1 MB
        amount = 100
    
        def create_file():
            print(f"Start creating a huge file")
            with open("localfile.txt", "ab") as f:
                for j in range(15):
                    f.write(os.urandom(amount) * size)
            print("localfile.txt size:", os.stat("localfile.txt").st_size / (1000**3), "GB")
    
        create_file()
        for k in range(75):
            time.sleep(60)
            print(f"{k+1} minute")
    
        print("Success!")
    
    
    t1 = PythonOperator(
        task_id='create_huge_file',
        python_callable=consume,
        dag=dag,
        depends_on_past=False,
        retries=0)
    

### Trigger sample DAGs

Trigger the first DAG, `create_large_txt_file_print_logs`:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. In the Airflow UI, on the **DAGs** page, click the **Trigger DAG** button for your DAG.

  4. Click **Trigger**.

  5. On the **DAGs** page, click the task you triggered and review the output logs to make sure your DAG started running.

  6. Wait until the task you created with the `create_large_txt_file_print_logs` DAG completes. This might take several minutes.

**Note:** You might notice that the used Airflow worker storage was reset to zero after the task was completed. Managed Airflow relies on [Google Kubernetes Engine Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) which provides necessary resources. [Autoscaling](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments) in Managed Airflow is metric-based and controls resource allocation through GKE Pods management within a given quota.
  7. On the **DAGs** page, click the DAG run. You will see your task has a `Success` state, even though the storage limit was exceeded.




Review the task Airflow logs:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

     1. In the list of environments, click the name of your environment. The **Environment details** page opens.

     2. Go to the **Logs** tab, then go to **All logs** > **Airflow logs** > **Workers** > **View in Logs Explorer**.

     3. Filter the logs by type: show only **Error** messages.




In the logs, you will see messages similar to the following:
    
    
    Worker: warm shutdown (Main Process)
    

or
    
    
    A worker pod was evicted at 2023-12-01T12:30:05Z with message: Pod ephemeral
    local storage usage exceeds the total limit of containers 1023Mi.
    

These logs indicate the pod started the "warm shutdown" process because the used storage exceeded the limit and was evicted in 1 hour. However, the DAG run did not fail because it was completed within the Kubernetes termination grace period, which is explained further in this tutorial.

To illustrate the concept of the termination grace period, review the outcome of the second sample DAG, `long_running_create_large_txt_file_print_logs`.

Trigger the second DAG, `long_running_create_large_txt_file_print_logs`:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the **Airflow webserver** column, follow the **Airflow** link for your environment.

  3. In the Airflow UI, on the **DAGs** page, click the **Trigger DAG** button for your DAG.

  4. Click **Trigger**.

  5. On the **DAGs** page, click the task you triggered and review the output logs to make sure your DAG started running.

  6. Wait until the `long_running_create_large_txt_file_print_logs` DAG run fails. **This will take about one hour**.




Review the DAG run results:

  1. On the **DAGs** page, click the `long_running_create_large_txt_file_print_logs` DAG run. You will see that the task has a `Failed` state, and that the duration of the run was exactly 1 hour 5 minutes, which is less than the task's waiting period of 1 hour 15 minutes.

  2. Review the task's logs. Once the DAG created the `localfile.txt` file in the Airflow worker's container, the log prints that the DAG started waiting, and the run duration is printed in the task logs every 1 minute. In this example, the DAG prints the `localfile.txt size:` log and the size of the `localfile.txt` file will be 1.5 GB.




Once the file written to the Airflow worker's container exceeds the storage limit, the DAG run is supposed to fail. However, the task does not fail immediately and keeps running until its duration reaches 1 hour and 5 minutes. This happens because Kubernetes does not kill the task immediately and keeps running to allow 1 hour of time-to-recovery, known as the "termination grace period". Once a node runs out of resources, Kubernetes does not terminate the Pod immediately to handle termination gracefully, so that there is minimal impact on the end user.

The termination grace period helps users to recover files after task failures, however, it can lead to confusion when diagnosing DAGs. When the Airflow worker storage limit is exceeded, the end task state depends on the duration of the DAG run:

  * If the DAG run exceeds the worker storage limit but completes in less than 1 hour, the task completes with a `Success` status because it was completed within the termination grace period. However, Kubernetes terminates the Pod and the written file is deleted from the container immediately.

  * If the DAG exceeds the worker storage limit and runs for more than 1 hour, the DAG keeps running for 1 hour and can exceed the storage limit by thousands of percent before Kubernetes eliminates the Pod and Airflow marks the task as `Failed`.


**Note:** If you trigger one of the sample DAGs that exceed the storage limit simultaneously with any other sample DAG, you will see that, if one of the tasks exceeds the storage limit and fails, any other running tasks will fail, too, even if they don't require storage space.

### Diagnose the failed DAG

If you were running multiple tasks at the time of the failure, consider running only one task and diagnosing resource pressure during that time to identify which tasks cause resource pressure and which resources you need to increase.

Review the task logs of the second DAG, `long_running_create_large_txt_file_print_logs`:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Logs** tab, then go to **All logs** > **Airflow logs** > **Workers** > **View in Logs Explorer**.

  4. Filter the logs by type: show only **Error** messages.




In the logs, you will see messages similar to the following:
    
    
    Container storage usage of worker reached 155.7% of the limit.
    
    This likely means that the total size of local files generated by your DAGs is
    close to the storage limit of worker.
    
    You may need to decrease the storage usage or increase the worker storage limit
    in your Cloud Composer environment configuration.
    

or
    
    
    Pod storage usage of worker reached 140.2% of the limit.
    A worker pod was evicted at 2023-12-01T12:30:05Z with message: Pod ephemeral
    local storage usage exceeds the total limit of containers 1023Mi.
    
    This eviction likely means that the total size of dags and plugins folders plus
    local files generated by your DAGs exceeds the storage limit of worker.
    
    Please decrease the storage usage or increase the worker storage limit in your
    Cloud Composer environment configuration.
    

These messages indicate that, as the task progressed, Airflow logs started printing errors when the size of the files generated by your DAG exceeded the worker storage limit, and the termination grace period started. During the termination grace period, storage consumption did not return to the limit, which led to Pod eviction after the termination grace period ended.

Review the environment health and resource consumption monitoring:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Monitoring** tab and select **Overview**.

  4. On the **Environment overview** panel, locate the **Environment Health (Airflow Monitoring DAG)** graph. It contains a red area, which corresponds to the time when logs started printing errors.

  5. Select **Workers** , and find the **Total workers disk usage** graph. Observe that the **Disk usage** line has a spike and exceeds the **Disk limit** line at the time when your task was running.


[ ![The Disk usage line has a spike and exceeds the Disk limit
    line at the time when your task was running](https://docs.cloud.google.com/static/composer/docs/images/composer-workers-disk-usage.png)](https://docs.cloud.google.com/static/composer/docs/images/composer-workers-disk-usage.png) **Figure 2.** Total workers disk usage graph (click to enlarge) 

### Increase the worker storage limit

**Note:** Changing worker storage restarts Airflow workers, which might affect running tasks. We recommend doing it when no DAGs are running.

Allocate additional Airflow worker storage in order for the sample DAG to succeed:

  1. In the Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Environment configuration** tab.

  4. Find the **Resources** > **Workloads** configuration and click **Edit**.

  5. In the **Worker** section, in the **Storage** field, specify the new storage limit for Airflow workers. In this tutorial, set it to 2 GB.

  6. Save the changes and allow several minutes for your Airflow workers to restart.




### Test your DAG with the new storage limit

Trigger the `long_running_create_large_txt_file_print_logs` DAG again and wait for 1 hour and 15 minutes until it finishes running.

  1. In the output logs of your DAG run, you will see `Marking task as SUCCESS`, and the task's state will indicate **Success** , with a duration of 1 hour and 15 minutes which is equal to the waiting time set in the DAG code.

  2. Review the **Environment overview** section in the **Monitoring** tab and make sure that there are no red areas.

  3. Click the **Workers** section and find the **Total workers disk usage** graph. You will see that the **Disk limit** line reflects the change in the storage limit, and the **Disk usage** line is within the allowed range.




## Summary

In this tutorial, you diagnosed the reason for a DAG failure and identified the type of resource that causes pressure by debugging two example DAGs that fail due to a lack of worker memory and storage. You then ran the DAGs successfully after allocating more memory and storage to your workers. However, it is recommended to [optimize your DAGs (workflows)](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) to reduce worker resource consumption in the first place, because it is not possible to increase the resources beyond a certain threshold.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

[Delete the Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/delete-environments). You also delete the environment's bucket during this procedure.

## What's next

  * [Scale environments](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
