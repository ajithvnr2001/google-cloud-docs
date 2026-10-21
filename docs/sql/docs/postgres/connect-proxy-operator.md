---
url: https://docs.cloud.google.com/sql/docs/postgres/connect-proxy-operator/
title: Connect using the Cloud SQL Proxy Operator \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:22.653758+00:00
---

# Connect using the Cloud SQL Proxy Operator  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/connect-proxy-operator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Connect using the Cloud SQL Proxy Operator Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/connect-proxy-operator "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/connect-proxy-operator "View this page for the SQL Server database engine")

This page describes how to connect to your Cloud SQL instance using the Cloud SQL Proxy Operator. For more information about how the Cloud SQL Proxy Operator works, see [About the Cloud SQL Proxy Operator](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy#proxy-operator).

## Overview

The Cloud SQL Proxy Operator configures applications deployed on Google Kubernetes Engine (GKE) to connect to Cloud SQL database instances using the Cloud SQL Auth Proxy. Using the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy) is the recommended method for connecting to a Cloud SQL instance. To learn more about the Cloud SQL Auth Proxy, see [About the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).

Applications running in [ GKE](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine#proxy) can connect using the Cloud SQL Auth Proxy.

## Before you begin

Before you can connect to a Cloud SQL instance, do the following:

  1. For a user or service account, make sure the account has the Cloud SQL Client role. This role contains the `cloudsql.instances.connect` permission, which authorizes a principal to connect to all Cloud SQL instances in a project. 

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

You can optionally include an [IAM condition](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#allow_users_to_connect_to_specific_instances) in the IAM policy binding that grants the account permission to connect only to one specific Cloud SQL instance.

  2. Enable the Cloud SQL Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=sqladmin)

  3. Install and initialize the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). 



## Install the Cloud SQL Proxy Operator

Use the following steps to install the Cloud SQL Proxy Operator.

  1. Confirm that `kubectl` can connect to your GKE cluster. 
         
         kubectl cluster-info

For more information about connecting Google Kubernetes Engine to Cloud SQL, see [Connect from Google Kubernetes Engine](https://docs.cloud.google.com/sql/docs/postgres/connect-kubernetes-engine). 
  2. Install `cert-manager` using helm. You will need to use the version and cli arguments specified here to use `cert-manager` on your GKE cluster. 
         
         helm repo add jetstack https://charts.jetstack.io
               helm repo update
               helm install \
                 cert-manager jetstack/cert-manager \
                 --namespace cert-manager \
                 --version "v1.9.1" \
                 --create-namespace \
                 --set global.leaderElection.namespace=cert-manager \
                 --set installCRDs=true
             

  3. Install the Cloud SQL Proxy Operator to your kubernetes cluster: 
         
         kubectl apply -f https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy-operator/v1.8.3/cloud-sql-proxy-operator.yaml
             

  4. Wait for the Cloud SQL Proxy Operator to start. 
         
         kubectl rollout status deployment -n cloud-sql-proxy-operator-system cloud-sql-proxy-operator-controller-manager --timeout=90s
             

  5. Confirm that the Cloud SQL Proxy Operator is installed and running: 
         
         kubectl get pods -n cloud-sql-proxy-operator-system
           




## What's next

  * Learn more about the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).
  * Learn more about [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview).
  * Learn more about [Service Accounts](https://docs.cloud.google.com/iam/docs/understanding-service-accounts).
  * Learn about the [two levels of access control](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control) for Cloud SQL instances.
  * Create [users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) and [databases](https://docs.cloud.google.com/sql/docs/postgres/create-manage-databases).
  * Learn about [ connecting to your instance from your application](https://docs.cloud.google.com/sql/docs/postgres/instance-access-control#instanceaccess).
  * Learn about [the psql Client](https://www.postgresql.org/docs/current/static/app-psql.html).
  * Learn about [options for support](https://docs.cloud.google.com/sql/docs/support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
