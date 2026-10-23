---
url: https://docs.cloud.google.com/alloydb/docs/use-secret-manager/
title: Use Secret Manager to handle secrets in AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:13.679420+00:00
---

# Use Secret Manager to handle secrets in AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/use-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use Secret Manager to handle secrets in AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use AlloyDB for PostgreSQL with Secret Manager to store sensitive access information.

Securely handling your sensitive information is an essential part of building a secure development workflow. For AlloyDB, we recommend that you store your sensitive information as secrets that you create in [Secret Manager](https://docs.cloud.google.com/secret-manager). Secrets include API keys, passwords, sensitive information, and credentials that you might use to access a confidential system.

## Overview

Secret Manager provides convenience and improves security. You can also apply versioning to your secrets and share them across your team. To learn more about how to share secrets with your team, see [Access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control).

## Usernames and passwords

Using Secret Manager to store the usernames and passwords of your AlloyDB user accounts as secrets is a safe and reliable way to manage your sensitive information.

First, create a user in AlloyDB. This requires you to supply a username and password. For more information about how to create a user in AlloyDB, see [Manage PostgreSQL users with built-in authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles).

After you create the user, create a secret in Secret Manager to store the username and password, which prevents the loss of your sensitive information. For more information about how to create and access secrets in Secret Manager, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

## Cross-region replica scenarios

If a primary AlloyDB cluster fails, then you might promote a secondary cluster. After the secondary cluster becomes the primary cluster, you must update the instance connection name to reflect this promotion. If the instance name is stored in a secret, then you must update the secret with the name of the new primary cluster. For more information, see [Edit a secret](https://docs.cloud.google.com/secret-manager/docs/edit-secrets).

One way to use Secret Manager for failovers is to store the name of your primary cluster in a secret, and then wrap the AlloyDB Auth Proxy invocation in a script that polls Secret Manager.

To detect when the value for the instance connection name is updated, use the AlloyDB Auth Proxy and then restart it with the new value, as follows:
    
    
    #!/bin/bash
    
    SECRET_ID="my-secret-id" # TODO(developer): replace this value
    REFRESH_INTERVAL=5
    PORT=5432                # TODO(developer): change this port as needed
    
    # Get the latest version of the secret and start the proxy
    INSTANCE=$(gcloud secrets versions access "latest" --secret="$SECRET_ID")
    alloydb-auth-proxy $INSTANCE --port=$PORT &
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
            alloydb-auth-proxy $INSTANCE --port=$PORT &
            PID=$!
        fi
    done
    

For more information on how to create and access a secret that contains the instance connection name of the primary replica, see [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart). For more information on using the AlloyDB Auth proxy, see [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).

## What's next

  * To learn how to integrate Secret Manager with your development environment, see the various samples available in the [All Secret Manager code samples](https://docs.cloud.google.com/secret-manager/docs/samples) page.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
