---
url: https://docs.cloud.google.com/sql/docs/sqlserver/use-secret-manager/
title: Use Secret Manager to handle secrets in Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:53.536521+00:00
---

# Use Secret Manager to handle secrets in Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/use-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Use Secret Manager to handle secrets in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/use-secret-manager "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-secret-manager "View this page for the PostgreSQL database engine") | SQL Server

## Overview

Managing your sensitive information correctly is an essential part of creating a secure development workflow. For Cloud SQL, we recommend that you store your pieces of sensitive information as secrets that you create in [Secret Manager](https://docs.cloud.google.com/secret-manager). Secrets include API keys, passwords, sensitive information, or credentials that you might use to access a confidential system.

Secret Manager provides convenience and improves security. You can also apply versioning to your secrets and share them across your team. To learn more about how to share secrets with your team, see [Access control (IAM)](https://docs.cloud.google.com/secret-manager/docs/access-control).

This page describes four use cases for using Secret Manager to manage secrets with Cloud SQL:

  * Storing usernames and passwords
  * Connecting to Cloud SQL instances
  * Managing SSL/TLS certificates
  * Coordinating disaster recovery scenarios



## Before you begin

Before you begin using Secret Manager to handle secrets in Cloud SQL:

  * Familiarize yourself with both [Cloud SQL](https://docs.cloud.google.com/sql/docs) and [Secret Manager](https://docs.cloud.google.com/secret-manager/docs).
  * Get started with Cloud SQL by learning how to [connect to your first Cloud SQL instance from your local computer](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-local-computer).



## Usernames and passwords

Using Secret Manager to store the usernames and passwords of your Cloud SQL user accounts as secrets is a safe and reliable way to manage this sensitive information.

First, you have to create a user in Cloud SQL. As part of creating this user, you have to supply a username and password. For more information about creating a user in Cloud SQL, see [Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).

After the user is created, create a secret in Secret Manager to store the username and password. This ensures that this sensitive information won't be lost. For more information about creating and accessing secrets in Secret Manager, see [Creating and accessing secrets](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

## Cloud SQL instances

When connecting to your Cloud SQL instance, you can use Secret Manager to manage secrets to create a secure development workflow.

Start by connecting to your Cloud SQL instance from your local computer. After the instance is running, use environment variables to connect to it. Some values asociated with the variables are more sensitive, such as the instance connection name. For each value, you can create a secret in Secret Manager to store and manage this information. To learn more about using environment variables to connect to your Cloud SQL instance, see [Configure and run sample app](https://docs.cloud.google.com/sql/docs/mysql/connect-instance-local-computer#configure_and_run_sample_app).

You can retrieve the instance connection name that's stored as a secret directly from Secret Manager. This provides a flexible workflow that can help your team share this sensitive information across multiple applications and manage it from a centralized location. For more information on retrieving secrets from Secret Manager, see [Create a secret with Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret#create_and_access_a_secret_version).

An application requires the information in the secrets to start. This information includes the values associated with the environment variables that are used to connect to the application. Your application accesses the secrets when it starts, and then uses the secrets to configure a connection to Cloud SQL. If any relevant secrets are updated in Secret Manager, then you might have to restart the application.

## SSL/TLS certificates

If you connect to a Cloud SQL instance using a public or private IP address, then you should use a Transport Layer Security (TLS) certificate which secures data while it's transmitted. Each TLS certificate includes a public key certificate and a private key. For more information on configuring TLS certificates, see [Configure SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance).

You can save the TLS certificate, public key certificate, and private key as secrets to keep them safe and share them with your team. For more information on creating and accessing secrets, see [Create a secret with Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret). For more information on sharing secrets, see [Access control (IAM)](https://docs.cloud.google.com/secret-manager/docs/access-control).

## Disaster recovery scenarios

If a primary instance in Cloud SQL fails, then you might promote a read replica to the primary instance. After the read replica becomes the primary instance, you must update the instance connection name to reflect this promotion. If the instance connection name is stored in a secret, then you must update the secret with the name of the new primary instance. For more information, see [Edit a secret](https://docs.cloud.google.com/secret-manager/docs/edit-secrets).

One way to use Secret Manager for failovers is to store the name of your primary instance in a secret, and then configure your Cloud SQL connector to be updated whenever the secret is updated.

You can use the following bash wrapper script with the Cloud SQL Auth proxy to detect when the value for the instance connection name is updated, and then restart the proxy with the new value:
    
    
    #!/bin/bash
    
    SECRET_ID="my-secret-id" # TODO(developer): replace this value
    REFRESH_INTERVAL=5
    PORT=5432                # TODO(developer): change this port as needed
    
    # Get the latest version of the secret and start the proxy
    INSTANCE=$(gcloud secrets versions access "latest" --secret="$SECRET_ID")
    cloud_sql_proxy -instances="$INSTANCE"=tcp:"$PORT" &
    PID=$!
    
    # Every 5s, get the latest version of the secret. If it's changed, restart the
    # proxy with the new value.
    while true; do
        sleep $REFRESH_INTERVAL
        NEW=$(gcloud secrets versions access "latest" --secret="$SECRET_ID")
        if [ "$INSTANCE" != "$NEW" ]; then
            INSTANCE=$NEW
            kill $PID
            wait $PID
            cloud_sql_proxy -instances="$INSTANCE"=tcp:"$PORT" &
            PID=$!
        fi
    done

For more information on creating and accessing a secret that contains the instance connection name of the primary replica, see [Create a secret with Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret). For more information on using the Cloud SQL Auth proxy, see [Connect to Cloud SQL using the Cloud SQL Auth proxy](https://docs.cloud.google.com/sql/docs/sqlserver/connect-instance-auth-proxy).

## What's next

  * You can integrate Secret Manager with other Google Cloud products such as Cloud Run. 
    * For more information about how to secure your secrets in container environments, see [ Use secrets](https://docs.cloud.google.com/run/docs/configuring/secrets).
    * For a list of other Google Cloud products that integrate with Secret Manager, see [Using Secret Manager with other products](https://docs.cloud.google.com/secret-manager/docs/using-other-products).
  * To learn how to integrate Secret Manager with your development environment, see the various samples available in the [All Secret Manager code samples](https://docs.cloud.google.com/secret-manager/docs/samples) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
