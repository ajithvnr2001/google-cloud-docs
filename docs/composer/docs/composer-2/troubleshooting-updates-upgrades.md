---
url: https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-updates-upgrades/
title: Troubleshooting environment updates and upgrades \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:52.198143+00:00
---

# Troubleshooting environment updates and upgrades  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-updates-upgrades/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 2 Guides ](https://docs.cloud.google.com/composer/docs/composer-2/composer-overview)



Send feedback 

#  Troubleshooting environment updates and upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/troubleshooting-updates-upgrades "View this page for Managed Airflow \(Gen 3\)") | **Managed Airflow (Gen 2)** | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-updates-upgrades "View this page for Managed Airflow \(Legacy Gen 1\)")

This page provides troubleshooting information for problems that you might encounter while updating or upgrading Managed Service for Apache Airflow environments.

For troubleshooting information related to creating environments, see [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation).

When Managed Airflow environments are updated, the majority of issues happen because of the following reasons:

  * Service account permission problems
  * PyPI dependency issues
  * Size of the Airflow database



## Insufficient permissions to update or upgrade an environment

If Managed Airflow can't update or upgrade an environment because of insufficient permissions, it outputs the following error message:
    
    
    ERROR: (gcloud.composer.environments.update) PERMISSION_DENIED: The caller does not have permission
    

**Solution** : Assign roles to both to your account and to the service account of your environment as described in [Access control](https://docs.cloud.google.com/composer/docs/composer-2/access-control).

## The service account of the environment has insufficient permissions

When creating a Managed Airflow environment, you specify a service account that performs most of the environment's operations. If this service account doesn't have enough permissions for the requested operation, then Managed Airflow outputs an error:
    
    
        UPDATE operation on this environment failed 3 minutes ago with the
        following error message:
        Composer Backend timed out. Currently running tasks are [stage:
        CP_COMPOSER_AGENT_RUNNING
        description: "No agent response published."
        response_timestamp {
          seconds: 1618203503
          nanos: 291000000
        }
        ].
    

**Solution** : Assign roles to your Google Account and to the service account of your environment as described in [Access control](https://docs.cloud.google.com/composer/docs/composer-2/access-control).

## The size of the Airflow database is too big to perform the operation

An upgrade operation might not succeed because the size of the Airflow database is too large for upgrade operations to succeed.

If the size of the Airflow database is more than 16 GB, Managed Airflow outputs the following error:
    
    
    Airflow database uses more than 16 GB. Please clean the database before upgrading.
    

**Solution** : Perform the Airflow database cleanup, as described in [Clean up the Airflow database](https://docs.cloud.google.com/composer/docs/composer-2/cleanup-airflow-database).

## An upgrade to a new Managed Airflow version fails because of PyPI package conflicts

When you upgrade an environment with [installed custom PyPI packages](https://docs.cloud.google.com/composer/docs/composer-2/install-python-dependencies), you might encounter errors related to PyPI package conflicts. This might happen because the new Managed Service for Apache Airflow image contains later versions of preinstalled packages. This can cause dependency conflicts with PyPI packages that you installed in your environment.

**Solution** :

  * To get detailed information about package conflicts, run an [upgrade check](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments#upgrade-check).
  * Loosen version constraints for installed custom PyPI packages. For example, instead of specifying a version as `==1.0.1`, specify it as `>=1.0.1`.
  * For more information about changing version requirements to resolve conflicting dependencies, see [pip documentation](https://pip.pypa.io/en/stable/topics/dependency-resolution).



## It's not possible to upgrade an environment to a version that is still supported

Managed Airflow environments can be upgraded only to [several latest and previous versions](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments#select-version).

The version limitations for creating new environments and upgrading existing environments are different. The Managed Airflow version you choose when creating a new environment might not be available when upgrading existing environments.

You can perform the upgrade operation using Google Cloud CLI, API or Terraform. In Google Cloud console, only the latest versions are available as upgrade choices.

## Environment is not healthy (liveness check failed)

It is possible to upgrade an environment only if its status [is reported as healthy](https://docs.cloud.google.com/composer/docs/composer-2/use-monitoring-dashboard#metrics).

One of the most common causes for non-healthy status is when environment's components approach the configured resource limits and constantly operate at maximum load. Because some environment components can't report their status, the liveness check DAG reports the status of the environment as not healthy.

To solve this problem, we recommend to increase the resource limits. Although we recommend to keep your environment from approaching the limits at all times, you can also do so only for the period when your environment upgrades.

## Lack of connectivity to DNS can cause problems while performing upgrades or updates

Such connectivity problems might result in the log entries like this:

`WARNING - Compute Engine Metadata server unavailable attempt 1 of 5. Reason: [Errno -3] Temporary failure in name resolution Error`

It usually means that there is no route to DNS so make sure that metadata.google.internal DNS name can be resolved to IP address from within Cluster, Pods and Services networks. Check if you have Private Google Access turned on within VPC (in host or service project) where your environment is created.

  * [Configure VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc#connectivity-restricted)
  * [Private IP configuration](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip#connectivity-domains)



## Triggerer CPU exceeds the 1 vCPU limit

Managed Airflow versions 2.4.4 and later introduce a different triggerer resource allocation strategy to improve performance scaling. If you encounter an error related to triggerer CPU when performing an environment update, it means that your current triggerers are configured to use more than 1 vCPU per triggerer.

**Solution** :

  * [Adjust triggerer resource allocation](https://docs.cloud.google.com/composer/docs/composer-2/scale-environments#triggerer-parameters) to meet the 1 vCPU limit.
  * If you anticipate issues with DAGs that [use deferrable operators](https://docs.cloud.google.com/composer/docs/composer-2/use-deferrable-operators), then we recommend to also increase the number of triggerers.



## Inspect failed migration warnings

When upgrading Airflow to a later version, sometimes new constraints are applied to the Airflow database. If these constraints can't be applied, Airflow creates new tables to store the rows for which the constraints couldn't be applied. Airflow UI displays a warning message until the moved data tables are renamed or dropped.

**Solution** :

You can use the following two DAGs to inspect the moved data and rename the tables.

The `list_moved_tables_after_upgrade_dag` DAG lists rows that were moved from every table where constraints could not be applied. Inspect the data and decide whether you want to keep it. To keep it, you need to manually fix the data in the Airflow database. For example, by adding the rows back with the correct data.

If you don't need the data or if you already fixed it, then you can run the `rename_moved_tables_after_upgrade_dag` DAG. This DAG renames the moved tables. The tables and their data are not deleted, so you can review the data at a later point.
    
    
    """
    When upgrading Airflow to a newer version,
    it might happen that some data cannot be migrated,
    often because of constraint changes in the metadata base.
    This file contains 2 DAGs:
    
    1. 'list_moved_tables_after_upgrade_dag'
      Prints the rows which failed to be migrated.
    2. 'rename_moved_tables_after_upgrade_dag'
      Renames the table which contains the failed migrations. This will remove the
      warning message from airflow.
    """
    
    import datetime
    import logging
    
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from airflow.providers.postgres.hooks.postgres import PostgresHook
    from airflow.settings import AIRFLOW_MOVED_TABLE_PREFIX
    
    
    def get_moved_tables():
        hook = PostgresHook(postgres_conn_id="airflow_db")
        return hook.get_records(
            "SELECT schemaname, tablename FROM pg_catalog.pg_tables WHERE tablename"
            f" LIKE '{AIRFLOW_MOVED_TABLE_PREFIX}_%'"
        )
    
    
    def list_moved_records():
        tables = get_moved_tables()
        if not tables:
            logging.info("No moved tables found")
            return
    
        hook = PostgresHook(postgres_conn_id="airflow_db")
        for schema, table in tables:
            df = hook.get_pandas_df(f"SELECT * FROM {schema}.{table}")
            logging.info(df.to_markdown())
    
    
    def rename_moved_tables():
        tables = get_moved_tables()
        if not tables:
            return
    
        hook = PostgresHook(postgres_conn_id="airflow_db")
        for schema, table in tables:
            hook.run(f"ALTER TABLE {schema}.{table} RENAME TO _abandoned_{table}")
    
    
    with DAG(
        dag_id="list_moved_tables_after_upgrade_dag",
        start_date=datetime.datetime(2023, 1, 1),
        schedule_interval=None,
        catchup=False,
    ):
        t1 = PythonOperator(
            task_id="list_moved_records", python_callable=list_moved_records
        )
    
    with DAG(
        dag_id="rename_moved_tables_after_upgrade_dag",
        start_date=datetime.datetime(2023, 1, 1),
        schedule_interval=None,
        catchup=False,
    ) as dag:
        t1 = PythonOperator(
            task_id="rename_moved_tables", python_callable=rename_moved_tables
        )
    

## Environment operation stays in the failed state indefinitely

Managed Airflow (Gen 2) environments rely on Pub/Sub topics and subscriptions to communicate with resources located in the [tenant project](https://docs.cloud.google.com/composer/docs/composer-2/environment-architecture) of your environment during [environment operations](https://docs.cloud.google.com/composer/docs/composer-2/update-environments).

If the Pub/Sub API is disabled in your project, or if environment's topics or subscriptions are deleted, then an environment operation might fail and stay in the failed state indefinitely. Such an environment becomes irrevocably broken.

## What's next

  * [Updating environments](https://docs.cloud.google.com/composer/docs/composer-2/update-environments)
  * [Upgrading environments](https://docs.cloud.google.com/composer/docs/composer-2/upgrade-environments)
  * [Troubleshooting environment creation](https://docs.cloud.google.com/composer/docs/composer-2/troubleshooting-environment-creation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
