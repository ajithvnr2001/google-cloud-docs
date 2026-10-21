---
url: https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization/
title: Enabling and disabling DAG serialization \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:27:53.763468+00:00
---

# Enabling and disabling DAG serialization  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Enabling and disabling DAG serialization Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Composer 3 | Cloud Composer 2 | **Cloud Composer 1**

Follow the instructions on this page to enable or disable DAG serialization.

In a Cloud Composer environment, both the Airflow scheduler and the Airflow web server continuously process DAGs. You can improve the reliability and performance of the Airflow web server by enabling [DAG serialization](https://airflow.apache.org/docs/apache-airflow/stable/dag-serialization.html).

Enabling DAG serialization forces the scheduler to process DAG files before they are sent to the web server. The web server does not process DAGs. Instead, it reads the serialized DAGs from the Airflow database. Serializing DAGs in this way reduces the CPU and memory usage of the web server, especially when processing a large number of DAGs.

## Before you begin

**Note:** Starting from Cloud Composer version **1.15.0** , DAG serialization is enabled by default. You can enable and disable DAG serialization in new and existing environments by [overriding Airflow configuration options](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations), as described in the following sections.

DAG serialization affects the following Cloud Composer features:

  * DAG serialization cannot be enabled at the same time as [asynchronous DAG loading](https://docs.cloud.google.com/composer/docs/composer-2/access-airflow-web-interface#asynchronous-load).
  * Enabling DAG serialization disables all Airflow web server plugins for Cloud Composer. This does not impact scheduler or worker plugins, including Airflow operators, sensors, and so on.



## Enabling DAG serialization

You can enable DAG serialization for an existing environment or when creating a new environment.

**Note:** Do not apply these settings to environments running Airflow 2.x. The DAG serialization and storing DAG code in Airflow Metadata Database is by default turned on in Airflow 2.x and you cannot switch it on or off.

To enable DAG serialization, [override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value  
---|---|---  
`core` | `store_serialized_dags` | `True`  
`core` | `store_dag_code` | `True`  
`core` | `min_serialized_dag_update_interval` | `30`  
`scheduler` | `dag_dir_list_interval` | `30`  
  
The [`min_serialized_dag_update_interval`](https://airflow.apache.org/docs/stable/configurations-ref.html#min-serialized-dag-update-interval) Airflow configuration option controls how frequently serialized DAGs are updated in the database. The [`dag_dir_list_interval`](https://airflow.apache.org/docs/stable/configurations-ref.html#dag-dir-list-interval) option controls how frequently removed DAGs are deleted from the Airflow database. A high update frequency can negatively impact performance. We recommend setting `min_serialized_dag_update_interval` and `dag_dir_list_interval` to 30 seconds.

## Disabling DAG serialization

You can enable DAG serialization for an existing environment or when creating a new environment.

To disable DAG serialization, [override](https://docs.cloud.google.com/composer/docs/composer-2/override-airflow-configurations) the following Airflow configuration options:

Section | Key | Value  
---|---|---  
`core` | `store_serialized_dags` | `False`  
`core` | `store_dag_code` | `False`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
