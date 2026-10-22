---
url: https://docs.cloud.google.com/composer/docs/composer-3/lineage-integration/
title: Data lineage with Knowledge Catalog \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:31.486765+00:00
---

# Data lineage with Knowledge Catalog  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/lineage-integration/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Data lineage with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/lineage-integration "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page explains how to enable data lineage integration in Managed Airflow.

## About data lineage integration

[Data lineage](https://docs.cloud.google.com/dataplex/docs/about-data-lineage) is a [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) feature that tracks how data moves through your systems: where it comes from, where it is passed to, and what transformations are applied to it.

Managed Airflow uses the `apache-airflow-providers-openlineage` package to generate the lineage events that are sent to the Data Lineage API.

This package already installed in Managed Airflow environments. If you [install another version](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies) of this package, the list of supported operators might change. We recommend to do so only if necessary and keep the preinstalled version of the package otherwise.

  * Data lineage is available for environments in the same regions as Knowledge Catalog regions [that support data lineage](https://docs.cloud.google.com/dataplex/docs/locations).

  * If data lineage is enabled in your Managed Service for Apache Airflow environment, Managed Service for Apache Airflow reports lineage information to the Data Lineage API for DAGs that utilize any of the supported operators. You can also send custom lineage events if you want to report lineage for an operator that isn't supported.

  * You can access lineage information with:

    * [Data Lineage API](https://docs.cloud.google.com/dataplex/docs/reference/data-lineage/rest)
    * Lineage graphs for supported entries in Knowledge Catalog. For more information, see [Lineage graphs](https://docs.cloud.google.com/dataplex/docs/about-data-lineage#lineage-feature-graph) in the Knowledge Catalog documentation.



When you create an environment, data lineage integration is **automatically enabled** if the following conditions are met:

  * Data Lineage API is enabled in your project. For more information, see [Enabling Data Lineage API](https://docs.cloud.google.com/dataplex/docs/use-lineage) in Knowledge Catalog documentation.

**Caution:** After you enable Data Lineage API, Knowledge Catalog **automatically starts ingesting data** for BigQuery, Cloud Data Fusion, Managed Service for Apache Spark. This happens even if you don't create a Managed Airflow environment with data lineage integration.   
You can [configure the ingestion of data lineage](https://docs.cloud.google.com/dataplex/docs/use-lineage#control-ingestion) to enable or deactivate automatic data lineage ingestion for BigQuery, Managed Service for Apache Spark and Managed Service for Apache Airflow.
  * A custom [Lineage Backend](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/lineage.html#lineage-backend) isn't configured in Airflow.




You can disable data lineage integration when you create an environment.

For an existing environment, you can enable or disable data lineage integration at any time.

### Feature considerations in Managed Service for Apache Airflow

Managed Airflow makes an RPC call to create lineage events in the following cases:

  * When an Airflow task starts or finishes
  * When a DAG run starts or finishes



For details on these entities, see [lineage information model](https://docs.cloud.google.com/dataplex/docs/about-data-lineage#information-model) and [Lineage API reference](https://docs.cloud.google.com/dataplex/docs/reference/data-lineage/rest) in the Knowledge Catalog documentation.

Emitted lineage traffic is subject to [quotas in Data Lineage API](https://docs.cloud.google.com/dataplex/docs/quotas). Managed Airflow consumes Write quota.

Pricing associated with handling lineage data is subject to lineage pricing. See [data lineage considerations](https://docs.cloud.google.com/dataplex/docs/lineage-considerations#billing-impact).

### Performance considerations in Managed Service for Apache Airflow

Data lineage is reported at the end of Airflow task execution. On average, the data lineage reporting takes about 1-2 seconds.

This does not affect the performance of the task itself: Airflow tasks do not fail if lineage is not successfully reported to the Lineage API. There is no impact on the main operator logic, but the whole task instance does execute a bit longer to account for reporting lineage data.

An environment that reports data lineage will have a minor increase in associated costs, because of extra time needed to report data lineage.

### Compliance

Data lineage offers different support levels for features such as VPC Service Controls. Review [data lineage considerations](https://docs.cloud.google.com/dataplex/docs/lineage-considerations) to make sure that support levels match your environment requirements.

## Before you begin

  * This feature provides **varying compliance support**. Make sure to first review both feature considerations specific to Managed Service for Apache Airflow, and [data lineage feature considerations](https://docs.cloud.google.com/dataplex/docs/lineage-considerations).

  * All required IAM permissions for data lineage are already included in the Composer Worker (`roles/composer.worker`) role. This role is the required [role for environment's service accounts](https://docs.cloud.google.com/composer/docs/composer-3/access-control#service-account).

For more information about data lineage permissions, see [lineage roles and permissions](https://docs.cloud.google.com/dataplex/docs/iam-roles#lineage-roles) in the Knowledge Catalog documentation.




## Check if an operator is supported

Data lineage support is provided by the provider package where the operator is located:

  1. Check the changelogs of the provider package where the operator is located for entries that add OpenLineage support.

For example, BigQueryToBigQueryOperator supports OpenLineage starting from `apache-airflow-providers-google` [version 11.0.0](https://airflow.apache.org/docs/apache-airflow-providers-google/11.0.0/commits.html).

  2. Check the version of the provider package used by your environment. To do so, see the [list of preinstalled packages](https://docs.cloud.google.com/composer/docs/composer-versions) for Airflow build used in your environment. You can also [install a different version](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies) of the package in your environment.




In addition, the [Supported classes](https://airflow.apache.org/docs/apache-airflow-providers-openlineage/stable/supported_classes.html) page in the `apache-airflow-providers-openlineage` documentation lists latest supported operators.

## Configure data lineage integration

Data lineage integration for Managed Service for Apache Airflow is managed on a per-environment basis. This means that enabling the feature requires two steps:

  1. Enable the Data Lineage API in your project.
  2. Enable data lineage integration in a specific Managed Service for Apache Airflow environment.



### Enable data lineage in Managed Service for Apache Airflow

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Select the **Environment configuration** tab.

  4. In the **Knowledge Catalog Lineage integration** section, click **Edit**.

  5. In the **Knowledge Catalog Lineage integration** panel, select **Enable integration with Knowledge Catalog Lineage**.

  6. Click **Save**.




###  gcloud 

Use the `--enable-cloud-data-lineage-integration` argument.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --enable-cloud-data-lineage-integration
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --enable-cloud-data-lineage-integration
    

### Disable data lineage in Managed Service for Apache Airflow

Disabling lineage integration in a Managed Service for Apache Airflow environment doesn't disable the Data Lineage API. If you want to completely disable lineage reporting for your project, also disable the Data Lineage API. See [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).

###  Console 

  1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

  2. In the list of environments, click the name of your environment. The **Environment details** page opens.

  3. Select the **Environment configuration** tab.

  4. In the **Knowledge Catalog Lineage integration** section, click **Edit**.

  5. In the **Knowledge Catalog Lineage integration** panel, select **Disable integration with Knowledge Catalog Lineage**.

  6. Click **Save**.




###  gcloud 

Use the `--disable-cloud-data-lineage-integration` argument.
    
    
    gcloud composer environments update ENVIRONMENT_NAME \
        --location LOCATION \
        --disable-cloud-data-lineage-integration
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



Example:
    
    
    gcloud composer environments update example-environment \
        --location us-central1 \
        --disable-cloud-data-lineage-integration
    

## Send lineage events in supported operators

If data lineage is enabled, supported operators send lineage events automatically. You don't need to change your DAG code.

For example, running the following task:
    
    
    task = BigQueryInsertJobOperator(
        task_id='snapshot_task',
        dag=dag,
        location='<dataset-location>',
        configuration={
            'query': {
                'query': 'SELECT * FROM dataset.tableA',
                'useLegacySql': False,
                'destinationTable': {
                    'project_id': 'example-project',
                    'dataset_id': 'dataset',
                    'table_id': 'tableB',
                },
            }
        },
    )
    

Results in creating the following lineage graph in the Knowledge Catalog UI:

![Example lineage graph in Knowledge Catalog UI.](https://docs.cloud.google.com/static/composer/docs/images/lineage-auto-sample.png)**Figure 1.** Example lineage graph for a BigQuery table in Knowledge Catalog UI. 

## Send custom lineage events

You can send custom lineage events if you want to report lineage for an operator that isn't supported for automated lineage reporting.

For example, to send custom events with:

  * BashOperator: modify the `inlets` or `outlets` parameter in the task definition.
  * PythonOperator: modify the `task.inlets` or `task.outlets` parameter in the task definition.
  * You can use `AUTO` for the `inlets` parameter. This sets its value equal to the `outlets` of its upstream task.



The following example demonstrates the usage of inlets and outlets:
    
    
    from airflow.composer.data_lineage.entities import BigQueryTable
    from airflow.lineage import AUTO
    
    ...
    
    bash_task = BashOperator(
        task_id="bash_task",
        dag=dag,
        bash_command="sleep 0",
        inlets=[
            BigQueryTable(
                project_id="example-project",
                dataset_id="dataset",
                table_id="table1",
            )
        ],
        outlets=[
            BigQueryTable(
                project_id="example-project",
                dataset_id="dataset",
                table_id="table2",
            )
        ],
    )
    
    
    def _python_task(task):
        print("Python task")
    
    
    python_task = PythonOperator(
        task_id="python_task",
        dag=dag,
        python_callable=_python_task,
        inlets=[
            AUTO,
            BigQueryTable(
                project_id="example-project",
                dataset_id="dataset",
                table_id="table3",
            ),
        ],
        outlets=[
            BigQueryTable(
                project_id="example-project",
                dataset_id="dataset",
                table_id="table4",
            )
        ],
    )
    
    bash_task >> python_task
    

As a result, the following lineage graph is created in Knowledge Catalog UI:

![Example lineage graph for custom events in Knowledge Catalog UI.](https://docs.cloud.google.com/static/composer/docs/images/lineage-custom-sample.png)**Figure 2.** Example lineage graph for multiple BigQuery tables in Knowledge Catalog UI. 

## View lineage logs in Managed Service for Apache Airflow

You can inspect logs related to data lineage using the link on the **Environment configuration** page in the **Knowledge Catalog Lineage integration** section.

## Troubleshooting

If lineage data is not reported to the Lineage API, or you can't see it in Knowledge Catalog, try the following troubleshooting steps:

  * Make sure Data Lineage API is enabled in the project of your Managed Service for Apache Airflow environment.
  * Check if data lineage integration is enabled in the Managed Service for Apache Airflow environment.
  * Check if the operator that you use is included in the automated lineage reporting support. For more information, see Supported Airflow operators.
  * Check lineage logs in Managed Service for Apache Airflow for possible issues.



## What's next

  * [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-3/access-control)
  * [Create a Managed Airflow environment](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
