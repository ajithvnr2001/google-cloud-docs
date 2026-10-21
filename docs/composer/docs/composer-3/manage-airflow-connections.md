---
url: https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections/
title: Manage Airflow connections \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:15.780951+00:00
---

# Manage Airflow connections  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/manage-airflow-connections/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Manage Airflow connections Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/manage-airflow-connections "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/manage-airflow-connections "View this page for Managed Airflow \(Legacy Gen 1\)")

This page describes how to manage [Airflow connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html) in your environment and access them from your DAGs.

## About Airflow connections

Aiflow connections store credentials and other connection information, such as user names, connections strings, and passwords. Your DAGs use connections to communicate and access resources in Google Cloud and other services from your DAGs.

Airflow operators in your DAGs either use a default connection for the operator, or you specify a custom connection name.

### About connection security

Most Airflow operators do not accept credentials directly. Instead, they use Airflow connections.

When you create a new environment, Managed Airflow generates a unique, permanent fernet key for the environment and secures connection extras by default. You can view the `fernet_key` in the **Configuration** page in [Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface).

For more information about how connections and passwords are secured in Airflow, see [Securing Connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#securing-connections) and [Masking sensitive data](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/mask-sensitive-values.html) in the Airflow documentations.

**Important:** In Managed Airflow, we recommend to **store your connections in Secret Manager** instead of storing them in Airflow or directly in your DAGs.

### About connection types

Airflow uses connections of different types to connect to specific services. For example, the [Google Cloud connection type](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/connections/gcp.html) connects to other services in Google Cloud. As another example, S3 connection type connects to an Amazon S3 bucket.

To add a connection type to Airflow, [install a PyPI package](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies) with that connection type. Some packages are preinstalled in your environment. For example, you can use connection from the `apache-airflow-providers-google` package without installing custom PyPI packages.

### Preconfigured connections

Managed Airflow configures the following default connections in your environment. You can use these connections to access resources in your project without configuring them.

  * `google_cloud_default`
  * `bigquery_default`
  * `google_cloud_datastore_default`
  * `google_cloud_storage_default`



## Add a connection in Secret Manager

You can store a connection in Secret Manager, without adding it to Airflow. We recommend to use this approach when storing credentials and other sensitive information.

**Important:** Your DAGs prioritize connections stored in Secret Manager over connections stored in Airflow.

To add a connection in Secret Manager:

  1. [Configure Secret Manager for your environment](https://docs.cloud.google.com/composer/docs/composer-3/configure-secret-manager).

  2. [Add a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) with the name that matches the pattern for connections.

For example: `airflow-connections-example_connection`. In your DAGs, use the connection name without the prefix: `example_connection`.

  3. Add parameters for the connection:

###  JSON format 

Add the JSON representation of your connection as the value of the secret. For example:
         
         {
           "conn_type": "mysql",
           "host": "example.com",
           "login": "login",
           "password": "password",
           "port": "9000"
         }
         

For more information about the JSON connection format, see [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html).

###  URI format 

Add the URI representation of your connection as the value of the secret:

     * The secret must store a [URI representation](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-connection-uri) of the connection. For example, `mysql://login:password@example.com:9000`.

     * The URI must be URL-encoded. For example, a password that has a space symbol in it must be URL-encoded as follows: `mysql://login:secret%20password@example.com:9000`.

Airflow has a [convenience method](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#generating-connection-uri) for generating connection URIs. An example of how to encode a complex URL with JSON extras is available in the [Airflow documentation](https://airflow.apache.org/docs/apache-airflow-providers-mysql/stable/connections/mysql.html).

  4. Check that all connection parameters are correctly read from Secret Manager.




### Add a connection in Airflow

As an alternative to storing your connections in Secret Manager, you can store them in Airflow.

To add a connection in Airflow:

###  Airflow CLI 

Run the [`connections add`](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#connections) Airflow CLI command with Google Cloud CLI. For example:
    
    
    gcloud composer environments run ENVIRONMENT_NAME \
      --location LOCATION \
      connections add -- \
        --conn-type "mysql" \
        --conn-host "example.com" \
        --conn-port "9000" \
        --conn-login "login" \
        --conn-password "password" \
        example_connection
    

You can also use the `--conn-uri` argument:
    
    
    gcloud composer environments run ENVIRONMENT_NAME \
      --location LOCATION \
      connections add -- \
        --conn-uri "mysql://login:password@example.com:9000" \
        example_connection
    

Replace the following:

  * `ENVIRONMENT_NAME`: the name of your environment.
  * `LOCATION`: the region where the environment is located.



###  Airflow UI 

Follow the [Airflow documentation on creating connections](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html#creating-a-connection-with-the-ui).

## Check that Airflow correctly reads a connection

You can run the `connections get` Airflow CLI command through Google Cloud CLI to check that a connection is read correctly. For example, if you store a connection in Secret Manager, this provides a way to check if all parameters of a connection are read by Airflow from a secret.

**Warning:** **Airflow prints connection passwords in the command's output**. This happens both for connections stored in Airflow and in Secret Manager.
    
    
    gcloud composer environments run ENVIRONMENT_NAME \
        --location LOCATION \
        connections get \
        -- CONNECTION_NAME
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.
  * `CONNECTION_NAME` with the name of the connection. If your connection is stored in Secret Manager, use the connection name without the connection prefix. For example, specify `example_connection` instead of `airflow-connections-example_connection_json`.



Example:
    
    
    gcloud composer environments run example-environment \
        --location us-central1 \
        connections get \
        -- example_connection -o json
    

## Use Airflow connections in your DAGs

This section shows how to access your connection from a DAG.

### Use a Secret Manager connection

Use the name of the connection without the prefix. For example, if your secret is named `airflow-connections-aws_s3`, specify `aws_s3`.
    
    
    transfer_dir_from_s3 = S3ToGCSOperator(
        task_id='transfer_dir_from_s3',
        aws_conn_id='aws_s3',
        prefix='data-for-gcs',
        bucket='example-s3-bucket-transfer-operators',
        dest_gcs='gs://us-central1-example-environ-361f4221-bucket/data/from-s3/')
    

If you store a default connection in Secret Manager you can omit the connection name. See Airflow documentation for a specific operator to get the default connection name used by an operator. For example, the `S3ToGCSOperator` Airflow operator uses the `aws_default` connection by default. You can store this default connection in a secret named `airflow-connections-aws_default`.

### Use a connection stored in Airflow

Use the name of the connection, as it is defined in Airflow:
    
    
    transfer_dir_from_s3 = S3ToGCSOperator(
        task_id='transfer_dir_from_s3',
        aws_conn_id='aws_s3',
        prefix='data-for-gcs',
        bucket='example-s3-bucket-transfer-operators',
        dest_gcs='gs://us-central1-example-environ-361f4221-bucket/data/from-s3/')
    

To use the default connection for an operator, omit the connection name. See Airflow documentation for a specific operator to get the default connection name used by an operator. For example, the `S3ToGCSOperator` Airflow operator uses the `aws_default` connection by default.

## Troubleshooting

If your environment cannot access the secret stored in Secret Manager:

  1. Make sure that Secret Manager is configured in your environment.

  2. Check that connection's name in Secret Manager corresponds to the connection used by Airflow. For example, for a connection named `example_connection`, the secret name is `airflow-connections-example_connection`.

  3. Check that Airflow correctly reads a connection.




## What's next

  * [Configure Secret Manager](https://docs.cloud.google.com/composer/docs/composer-3/configure-secret-manager)
  * [Configure email notifications](https://docs.cloud.google.com/composer/docs/composer-3/configure-email)
  * [Write DAGs](https://docs.cloud.google.com/composer/docs/composer-3/write-dags)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
