---
url: https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation/
title: Access environments with Workforce Identity Federation \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:10.542648+00:00
---

# Access environments with Workforce Identity Federation  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Access environments with Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/access-environments-with-workforce-identity-federation "View this page for Managed Airflow \(Gen 2\)") | Managed Airflow (Legacy Gen 1)

This page describes how to configure user access to your Managed Airflow environment with Workforce Identity Federation.

## About Workforce Identity Federation in Managed Airflow

Workforce Identity Federation lets you use an external identity provider (IdP) to authenticate and authorize a workforce—a group of _users_ , such as employees, partners, and contractors—using IAM, so that the users can access Google Cloud services. For more information about Workforce Identity Federation, see [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

If Workforce Identity Federation is configured in your project, you can access your environment in the following ways:

  * Managed Airflow page in Google Cloud console
  * Airflow UI
  * Google Cloud CLI, including running Airflow CLI commands
  * Cloud Composer API
  * Airflow REST API



## Before you begin

  * You don't need to configure your environment in any specific way to support Workforce Identity Federation. All Airflow builds in Managed Airflow (Gen 3) support Workforce Identity Federation. 

**Important:** Workforce Identity Federation support in Managed Airflow **doesn't automatically provide a new access path for external identities** to your environment. As long as you don't configure access through an external identity provider and grant access permissions to external identities, the external identities can't access your environment.
  * [Cloud Storage limitations for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#cloud-storage) apply to the environment's bucket. In particular, you must enable [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) on the environment's bucket to let external identities upload their DAGs and files to this bucket.

  * Emails sent from Airflow only include the Airflow UI URL for Google accounts. Because external identities can only access Airflow UI through the Airflow UI URL for external identities, the link must be adjusted (changed to the URL for external identities).

  * Managed Airflow doesn't support using third-party identities in ingress and egress rules to allow [Apache Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) operations. However, you can use the `ANY_IDENTITY` identity type in ingress and egress rules to allow access to all identities, including third-party identities. For more information about the `ANY_IDENTITY` identity type, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).




## Set up access to your environment with Workforce Identity Federation

This section describes steps to configure access for external identities to your Managed Airflow environment.

### Configure your identity provider

Configure Workforce Identity Federation for your identity provider by following the [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#configure_workforce_identity_federation) guide.

### Grant IAM roles to external identities

In Identity and Access Management, grant IAM roles to sets of external identities, so that they can access and interact with your environment:

  * For a list of roles specific to Managed Airflow, see [Grant roles to users](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account). For example, the **Environment User and Storage Object Viewer** (`composer.environmentAndStorageObjectViewer`) role allows a user to view environments, access the Airflow UI, view and trigger DAGs from the [DAG UI](https://docs.cloud.google.com/composer/docs/composer-3/view-dags), and view objects in environment buckets.

  * For instructions about assigning these roles to external users, see [Grant IAM roles to principals](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#grant_roles_to_principals).

  * For a format of representing external identities in IAM policies, see [Represent workforce pool users in IAM policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).




### Check that new users receive correct Airflow roles in Airflow UI Access Control

Managed Airflow handles Airflow users for external identities in the same way as for Google account users. Instead of an email address, a [principal identifier](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users) is used. When an external identity accesses Airflow UI for the first time, an Airflow user is automatically registered in the Airflow role-based access control system with the [default role](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac#registering-users).

Check that new users receive correct Airflow roles in [Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac). You have two options:

  * Let external identities receive the default role after they access Airflow UI for the first time. If required, Airflow admin users can then change this role to a different one.
  * [Preregister external identities](https://docs.cloud.google.com/composer/docs/composer-2/airflow-rbac#preregister-users) with a set of required roles by adding Airflow user records with the user name and email fields set to their principal identifiers. In this way, external identities get the role that you assigned to them, not the default role.

**Important:** Airflow UI Access Control supports only the [identifier format for single identities](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users). Groups and identities with a specific attribute are not supported.



## Access Managed Airflow page in Google Cloud console

[Google Cloud Workforce Identity Federation console](https://docs.cloud.google.com/iam/docs/workforce-console-learn-more) provides access to the Managed Airflow page.

From the **Composer** page in Google Cloud Workforce Identity Federation console, you can access the UI for managing environments, Managed Airflow logs, monitoring and DAG UI.

All links to Airflow UI in the federated console point to the Airflow UI access point for external identities.

## Access Airflow UI

**Note:** Make sure that external identities have [an IAM role](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account) with the `composer.environments.get` permission on their provider, groups, or individual identities. For more information about assigning IAM roles to external identities, see [Grant IAM roles to principals](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#grant_roles_to_principals).

Managed Airflow environments have two URLs for the Airflow UI: one for Google accounts and another for external identities. External identities must access Airflow UI through the URL for external identities.

  * The URL for external identities is `https://<UNIQUE_ID>.composer.byoid.googleusercontent.com`.

  * The URL for Google accounts is `https://<UNIQUE_ID>.composer.googleusercontent.com`.

**Note:** Service accounts (you can recognize them by identifiers that end in `.iam.gserviceaccount.com`) are considered Google accounts. Use the `.composer.googleusercontent.com` address if you want to work with Airflow using a Google service account. See [Access Airflow API using a service account](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api#long-service-account-email).



Only users that are authenticated with external identities can access the URL for external identities. If a user visits the URL for external identities while not logged in, they are first redirected to the authentication portal where they specify their workforce pool provider name, then they are redirected to their identity provider to sign in, and finally they are redirected to the Airflow UI of the environment.

## Access DAG UI in Google Cloud console

The [DAG UI](https://docs.cloud.google.com/composer/docs/composer-3/manage-dags) is available for external identity users as part of the federated console. You can control the access with [IAM policies](https://docs.cloud.google.com/composer/docs/composer-3/access-control#user-account).

The Airflow role-based access in the environments with full Workforce Identity Federation support is also taken into account and can be used to limit which DAGs are visible for individual users by setting up roles, as described in [Using Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac).

## Access Google Cloud CLI

**Note:** Make sure that external identities have IAM roles on their provider, groups, or individual identities that [permit them to run `gcloud` and Airflow CLI commands](https://docs.cloud.google.com/composer/docs/composer-3/access-control#cli). For more information about assigning IAM roles to external identities, see [Grant IAM roles to principals](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#grant_roles_to_principals).

To access your environment through Google Cloud CLI, external identities must do the following:

  1. Sign in with Google Cloud CLI using an external identity.
  2. Run [`gcloud composer environments`](https://docs.cloud.google.com/sdk/gcloud/reference/composer) commands.



## Access Cloud Composer API

Cloud Composer API can be used with external identities to manage all Managed Airflow environments with the supported authentication methods such as OAuth tokens.

## Access Airflow REST API

Airflow REST API is available at the endpoint for external identities with the supported authentication methods such as OAuth tokens.

To get the URL of the endpoint for external identities for your environment, run the following Google Cloud CLI command:
    
    
    gcloud composer environments describe ENVIRONMENT_NAME \
      --location LOCATION \
      --format="value(config.airflowByoidUri)"
    

Replace:

  * `ENVIRONMENT_NAME` with the name of the environment.
  * `LOCATION` with the region where the environment is located.



Example:
    
    
    gcloud composer environments describe example-environment \
      --location us-central1 \
      --format="value(config.airflowByoidUri)"
    

## What's next

  * [Access control with IAM](https://docs.cloud.google.com/composer/docs/composer-3/access-control)
  * [Using Airflow UI Access Control](https://docs.cloud.google.com/composer/docs/composer-3/airflow-rbac)
  * [Access Airflow CLI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-cli)
  * [Access Airflow REST API](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
