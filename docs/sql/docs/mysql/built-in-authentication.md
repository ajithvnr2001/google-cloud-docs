---
url: https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication/
title: Cloud SQL built-in database authentication \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:40.965203+00:00
---

# Cloud SQL built-in database authentication  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/built-in-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Cloud SQL built-in database authentication Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/built-in-authentication "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/built-in-authentication "View this page for the SQL Server database engine")

This page describes how built-in authentication works on Cloud SQL instances and how database administrators can set password policies for local database users.

## Introduction

Authentication is the process of verifying the identity of a user who is attempting to access an instance. Cloud SQL uses the following types of authentication for database users:

  * The database's built-in authentication uses a username and a password to authenticate local database users. The current page describes this type of authentication.
  * IAM database authentication uses IAM to authenticate a user. For more information, see [Overview of Cloud SQL IAM database authentication](https://docs.cloud.google.com/sql/docs/mysql/authentication).



Although IAM database authentication is more secure and reliable, you might prefer to use built-in authentication or a hybrid authentication model that includes both authentication types.

You might create and manage local database users locally within a database to allow specific persons or applications to access a database. Such database users own the objects they create in the database. Cloud SQL offers strong built-in password enforcement. You can define and enable such enforcement through password policies.

**Note:** Password policies don't apply to hashed passwords.

## Instance password policies

You can set a password policy at the instance level when you [create an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance).

A password policy for an instance can include the following options: 

  * **Minimum length** : specify the minimum number of characters that the password must have.
  * **Password complexity** : check if the password is a combination of lowercase, uppercase, numeric, and non-alphanumeric characters.
  * **Restrict password reuse** : specify the number of previous passwords that you can't reuse. 

Supported only on Cloud SQL for MySQL 8.0 and later. 

  * **Disallow username** : prevent the use of the username in the password.

You need to explicitly enable a password policy at the instance level. You can modify it later by [editing the instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance). Note: When you enable a password policy, due to password policy verification, statements that create users or change user passwords cause additional latency usually spanning less than 150ms. 

## User password policies

While [creating a user](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating), you can set the following password usage restrictions:

  * **Set password to expire** : specify the number of days after which the password expires and you need to create a new one.
  * **Lock after failed attempts** : specify the number of times that you can try the password incorrectly before the account is locked.
  * **Require current password when password is changed** : require you to enter your existing password when attempting to change it.

**Note:** User password policy options are supported on Cloud SQL for MySQL 8.0 and later. The **Set password to expire** option is also supported on Cloud SQL for MySQL 5.7.

You can also modify user password policies.

The status of a user, indicating whether their password has expired or they're locked out, is visible when you [list the users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#list_users) of the instance. You can unlock users and change the password from the Users page.

## Cloud SQL built-in authentication for read replicas

You manage password policies for replicas on the primary instance. You can't separately modify password policies for read replicas.

When you promote an instance, you need to re-enable the instance password policy, along with the policy options.

## What's next

  * [Create an instance and set the password policy](https://docs.cloud.google.com/sql/docs/mysql/create-instance).
  * [Create users with built-in authentication](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
