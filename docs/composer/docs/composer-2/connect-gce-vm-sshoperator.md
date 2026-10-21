---
url: https://docs.cloud.google.com/composer/docs/composer-2/connect-gce-vm-sshoperator/
title: Connect to a Compute Engine VM with SSHOperator \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:47.394784+00:00
---

# Connect to a Compute Engine VM with SSHOperator  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/connect-gce-vm-sshoperator/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Connect to a Compute Engine VM with SSHOperator Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/connect-gce-vm-sshoperator "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/connect-gce-vm-sshoperator "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to connect to a Compute Engine VM from a DAG.

## Create a DAG that connects to a Compute Engine VM instance

In the `ssh_hook` parameter of `SSHOperator`, use [`ComputeEngineSSHHook`](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/_api/airflow/providers/google/cloud/hooks/compute_ssh/index.html) with parameters that point to the Compute Engine VM.

The following example demonstrates how to use [`SSHOperator`](https://airflow.apache.org/docs/apache-airflow-providers-ssh/stable/_api/airflow/providers/ssh/operators/ssh/index.html) to run a command on a Compute Engine VM instance.

Replace the values:

  * `GCE_INSTANCE` with the name of the VM instance.
  * `GCE_ZONE` with the [Compute Engine zone](https://docs.cloud.google.com/compute/docs/regions-zones/regions-zones) where the VM is located.
  * `GCP_PROJECT_ID` with the [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of a project where the VM and the environment that runs the DAG is located.



    
    
    import datetime
    
    import airflow
    from airflow.providers.ssh.operators.ssh import SSHOperator
    from airflow.providers.google.cloud.hooks.compute_ssh import ComputeEngineSSHHook
    
    GCE_INSTANCE = 'example-compute-instance'
    GCE_ZONE = 'us-central1-a'
    GCP_PROJECT_ID = 'example-project'
    
    with airflow.DAG(
            'composer_compute_ssh_dag',
            start_date=datetime.datetime(2025, 1, 1)
            ) as dag:
    
      ssh_task = SSHOperator(
          task_id='composer_compute_ssh_task',
          ssh_hook=ComputeEngineSSHHook(
              instance_name=GCE_INSTANCE,
              zone=GCE_ZONE,
              project_id=GCP_PROJECT_ID,
              use_oslogin=True,
              use_iap_tunnel=False,
              use_internal_ip=True),
          command='echo This command is executed from a DAG',
          dag=dag)
    

## What's next

  * [Add and update DAGs](https://docs.cloud.google.com/composer/docs/composer-2/manage-dags)
  * [Schedule and trigger DAGs](https://docs.cloud.google.com/composer/docs/composer-2/schedule-and-trigger-dags)
  * [Troubleshooting DAGs](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
