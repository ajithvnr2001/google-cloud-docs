---
url: https://docs.cloud.google.com/composer/docs/composer-3/use-celery-kubernetes-executor/
title: Use CeleryKubernetesExecutor \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:05.383627+00:00
---

# Use CeleryKubernetesExecutor  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/use-celery-kubernetes-executor/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Use CeleryKubernetesExecutor Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | Managed Airflow (Gen 2) | Managed Airflow (Legacy Gen 1)

This page explains how to enable CeleryKubernetesExecutor in Managed Airflow and how to use KubernetesExecutor in your DAGs.

## About CeleryKubernetesExecutor

[CeleryKubernetesExecutor](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery_kubernetes.html) is a type of executor that can use CeleryExecutor and KubernetesExecutor at the same time. Airflow selects the executor based on the queue that you define for the task. In one DAG, you can run some tasks with CeleryExecutor, and other tasks with KubernetesExecutor:

  * CeleryExecutor is optimized for fast and scalable execution of tasks.
  * KubernetesExecutor is designed for execution of resource-intensive tasks and running tasks in isolation.



### CeleryKubernetesExecutor in Managed Airflow

CeleryKubernetesExecutor in Managed Airflow provides the ability to use KubernetesExecutor for your tasks. It is not possible to use KubernetesExecutor in Managed Airflow separately from CeleryKubernetesExecutor.

Managed Airflow runs tasks that you execute with KubernetesExecutor in your environment's cluster, in the same namespace with Airflow workers. Such tasks have the same [bindings](https://docs.cloud.google.com/composer/docs/composer-3/access-control#composer-sa) as Airflow workers and can access resources in your project.

Tasks that you execute with KubernetesExecutor use the [Managed Airflow pricing model](https://docs.cloud.google.com/composer/pricing), since pods with these tasks run in your environment's cluster. Managed Airflow Compute SKUs (for CPU, Memory, and Storage) apply to these pods.

We recommend to run tasks with the CeleryExecutor when:

  * Task start-up time is important.
  * Tasks do not require runtime isolation and are not resource-intensive.



We recommend to run tasks with the KubernetesExecutor when:

  * Tasks require runtime isolation. For example, so that tasks do not compete for memory and CPU, since they run in their own pods.
  * Tasks are resource-intensive and you want to control the available CPU and memory resources.



### KubernetesExecutor compared to KubernetesPodOperator

Running tasks with KubernetesExecutor is similar to [running tasks using KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator). Tasks are executed in pods, thus providing pod-level task isolation and better resource management.

However, there are some key differences:

  * KubernetesExecutor runs tasks only in the versioned Managed Airflow namespace of your environment. It is not possible to change this namespace in Managed Airflow. You can specify a namespace where KubernetesPodOperator runs pod tasks.
  * KubernetesExecutor can use any built-in Airflow operator. KubernetesPodOperator executes only a provided script defined by the entrypoint of the container.
  * KubernetesExecutor uses the default Managed Airflow Docker image with the same Python, Airflow configuration option overrides, environment variables, and PyPI packages that are defined in your Managed Airflow environment. 



### About Docker images

By default, KubernetesExecutor launches tasks using the same Docker image that Managed Airflow uses for Celery workers. This is the [Managed Airflow image](https://docs.cloud.google.com/composer/docs/composer-versions) for your environment, with all changes that you specified for your environment, such as custom PyPI packages or environment variables.

**Warning:** Managed Airflow **does not support using custom images** with KubernetesExecutor.

## Before you begin

  * You can use CeleryKubernetesExecutor in Managed Airflow (Gen 3). 

  * It is not possible to use any executor other than CeleryKubernetesExecutor in Managed Airflow (Gen 3). This means you can run tasks using CeleryExecutor, KubernetesExecutor or both in one DAG, but it's not possible to configure your environment to only use KubernetesExecutor or CeleryExecutor.




## Configure CeleryKubernetesExecutor

You might want to [override](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations) existing Airflow configuration options that are related to KubernetesExecutor:

  * `[kubernetes]worker_pods_creation_batch_size`

This option defines the number of Kubernetes Worker Pod creation calls per scheduler loop. The default value is `1`, so only a single pod is launched per scheduler heartbeat. If you use KubernetesExecutor heavily, we recommended to increase this value.

  * `[kubernetes]worker_pods_pending_timeout`

This option defines, in seconds, how long a worker can stay in the `Pending` state (Pod is being created) before it is considered failed. The default value is 5 minutes.




## Run tasks with KubernetesExecutor or CeleryExecutor

You can run tasks using CeleryExecutor, KubernetesExecutor, or both in one DAG:

###  Airflow 3 

  * To run a task with KubernetesExecutor, specify: the `KubernetesExecutor` value in the `executor` parameter of a task.
  * To run a task with CeleryExecutor, omit the `executor` parameter.



###  Airflow 2 

  * To run a task with KubernetesExecutor, specify: the `kubernetes` value in the `queue` parameter of a task.
  * To run a task with CeleryExecutor, omit the `queue` parameter.

**Note:** The default value for the `[celery_kubernetes_executor]kubernetes_queue` Airflow configuration option is `kubernetes`. You do not need to override this value.

The following example runs the `task-kubernetes` task using KubernetesExecutor and the `task-celery` task using CeleryExecutor:

###  Airflow 3 
    
    
    import datetime
    import airflow
    from airflow.providers.standard.operators.python import PythonOperator
    
    with airflow.DAG(
      "composer_sample_celery_kubernetes",
      start_date=datetime.datetime(2026, 1, 1),
      schedule=None) as dag:
    
      def kubernetes_example():
          print("This task runs using KubernetesExecutor")
    
      def celery_example():
          print("This task runs using CeleryExecutor")
    
      # To run with KubernetesExecutor, set queue to kubernetes
      task_kubernetes = PythonOperator(
        task_id='task-kubernetes',
        python_callable=kubernetes_example,
        dag=dag,
        executor='KubernetesExecutor')
    
      # To run with CeleryExecutor, omit the queue argument
      task_celery = PythonOperator(
        task_id='task-celery',
        python_callable=celery_example,
        dag=dag)
    
      task_kubernetes >> task_celery
    

###  Airflow 2 
    
    
    import datetime
    import airflow
    from airflow.operators.python_operator import PythonOperator
    
    with airflow.DAG(
      "composer_sample_celery_kubernetes",
      start_date=datetime.datetime(2026, 1, 1),
      schedule=None) as dag:
    
      def kubernetes_example():
          print("This task runs using KubernetesExecutor")
    
      def celery_example():
          print("This task runs using CeleryExecutor")
    
      # To run with KubernetesExecutor, set queue to kubernetes
      task_kubernetes = PythonOperator(
        task_id='task-kubernetes',
        python_callable=kubernetes_example,
        dag=dag,
        queue='kubernetes')
    
      # To run with CeleryExecutor, omit the queue argument
      task_celery = PythonOperator(
        task_id='task-celery',
        python_callable=celery_example,
        dag=dag)
    
      task_kubernetes >> task_celery
    

## Run Airflow CLI commands related to KubernetesExecutor

You can run several [Airflow CLI commands related to KubernetesExecutor](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#kubernetes) using `gcloud`.

### Customize worker pod spec

You can customize worker pod spec by passing it in the `executor_config` parameter of a task. You can use this to define custom CPU and memory requirements.

You can override the entire worker pod spec that is used to run a task. To retrieve the pod spec of a task used by KubernetesExecutor, you can run the `kubernetes generate-dag-yaml` Airflow CLI command.

For more information about customizing worker pod spec, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/executor/kubernetes.html#pod-override).

**Caution:** Always use `base` as the name of the container in the overridden pod spec.

Managed Airflow (Gen 3) supports the following values for resource requirements:

Resource | Minimum | Maximum | Step  
---|---|---|---  
CPU | 0.25 | 32 | Step values: 0.25, 0.5, 1, 2, 4, 6, 8, 10, ..., 32. Requested values are rounded up to the closest supported step value (for example, 5 to 6).  
Memory | 2G (GB) | 128G (GB) | Step values: 2, 3, 4, 5, ..., 128. Requested values are rounded up to the closest supported step value (for example, 3.5G to 4G).  
Storage | - | 100G (GB) | Any value. If more than 100 GB are requested, only 100 GB are provided.  
  
For more information about resource units in Kubernetes, see [Resource units in Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes).

The following example demonstrates a task that uses custom worker pod spec:
    
    
    PythonOperator(
        task_id='custom-spec-example',
        python_callable=f,
        dag=dag,
        queue='kubernetes',
        executor_config={
            'pod_override': k8s.V1Pod(
                spec=k8s.V1PodSpec(
                    containers=[
                        k8s.V1Container(
                            name='base',
                            resources=k8s.V1ResourceRequirements(requests={
                                'cpu': '0.5',
                                'memory': '2G',
                            })
                        ),
                    ],
                ),
            )
        },
    )
    

## View task logs

Logs of tasks executed by KubernetesExecutor are available in the **Logs** tab, together with logs of tasks run by CeleryExecutor:

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Go to the **Logs** tab.

  4. Navigate to **All logs** > **Airflow logs** > **Workers**.

  5. Workers named `airflow-k8s-worker` execute KubernetesExecutor tasks. To look for logs of a specific task, you can use a DAG id or a task id as a keyword in the search.




## What's next

  * [Troubleshooting KubernetesExecutor](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-kubernetes-executor)
  * [Using KubernetesPodOperator](https://docs.cloud.google.com/composer/docs/composer-3/use-kubernetes-pod-operator)
  * [Using GKE operators](https://docs.cloud.google.com/composer/docs/composer-3/use-gke-operator)
  * [Overriding Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-3/override-airflow-configurations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
