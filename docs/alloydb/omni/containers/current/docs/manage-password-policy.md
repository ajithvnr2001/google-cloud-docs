---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage-password-policy/
title: Manage built-in authentication using password policies \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:38:59.092338+00:00
---

# Manage built-in authentication using password policies  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage-password-policy/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Manage built-in authentication using password policies Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage-password-policy)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/manage-password-policy)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/manage-password-policy)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/manage-password-policy)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/manage-password-policy)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/manage-password-policy)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/manage-password-policy)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/manage-password-policy)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage-password-policy)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/manage-password-policy)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/manage-password-policy)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/manage-password-policy)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/manage-password-policy)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage-password-policy)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/manage-password-policy)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/manage-password-policy)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/manage-password-policy)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/manage-password-policy)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/manage-password-policy)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/manage-password-policy)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/manage-password-policy)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/manage-password-policy)

This page describes how you can set and manage password policies for AlloyDB Omni. 

## About password policies

If your application's database users authenticate with AlloyDB Omni using the built-in, password-based method, then you can make authentication more secure by enforcing strong passwords. You can define and enable password enforcement by setting an AlloyDB Omni password policy.

### Limitations of password policies

AlloyDB Omni password policies have the following limitations:

  * Password policies apply to passwords created only after you set the policies. Existing user passwords aren't affected by a change in password policy.

  * Password policies apply to passwords entered only as plain text. Password policies don't apply to passwords entered as encrypted strings.




## Set an AlloyDB Omni password policy

You set a password policy by updating Grand Unified Configuration (GUC) password parameters in your `postgresql.conf` configuration file. To learn how to set a GUC parameter, see [Configure AlloyDB Omni database flags](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/configure-database-flags).

A password policy for AlloyDB Omni can include the following options:

  * **Disallow username** : prevent the username from being used in the password.

  * **Password complexity** : check if the password contains the allowed number of lowercase, uppercase, numeric, and non-alphanumeric characters. Also check if the password length is valid.

  * **Password expiry** : make sure that passwords are rotated periodically.




For a list of the password policy flags that AlloyDB Omni supports, see [Password policy flags](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags).

To comply with security standards and align with the security recommender's guidance, you must enable all three options together by configuring their primary enforcement flags to `ON`:

  * `password.enforce_password_does_not_contain_username`
  * `password.enforce_complexity`
  * `password.enforce_expiration`



If you set any of these three flags to `OFF` or omit them, the security recommender flags the instance as not having a password policy enabled.

### Preload the password validation library

For password a policy to take effect in AlloyDB Omni, the `alloydb_password_validation` library must be loaded. To load this library, do the following:

  1. Locate the `postgresql.conf` configuration file for your installation of AlloyDB Omni and open it in a text editor.

  2. Locate the `shared_preload_libraries` line and check if it includes `alloydb_password_validation`. If it doesn't, then you need to add it. When finished, your `shared_preload_libraries` line looks similar to the following:
         
         shared_preload_libraries='google_columnar_engine,google_job_scheduler,google_storage,alloydb_password_validation'
         




### Enforce password complexity

To enforce a password-complexity policy, do the following:

  1. Verify the your `postgresql.conf` file preloads password validation library.

  2. Set the [`password.enforce_complexity`](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags#enforce-complexity) flag to `ON`.

  3. Use [password policy flags](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags) to define your password policy.




For example, to enforce a password policy that states a password must contain at least one uppercase letter, one number, and be at least 10 characters long, you set the following in your `postgresql.conf` file:

  * `password.enforce_complexity = ON`
  * `password.min_uppercase_letters = 1`
  * `password.min_numerical_chars = 1`
  * `password.min_pass_length = 10`



After these flags are set, an attempt to set a database user password that doesn't comply with this password policy fails. For example, with this policy set, the following `psql` client command fails because the password `foo` is less than 10 characters and doesn't contain a number or an upper case character.
    
    
    CREATE USER USERNAME WITH PASSWORD foo;
    

### Enforce password expiration

To enforce the password expiration policy, do the following:

  1. Verify the your `postgresql.conf` file preloads password validation library.

  2. Set the [`password.enforce_expiration`](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags#enforce_expiration) flag to `ON`.

  3. Set the [`password.expiration_in_days`](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags#expiration_in_days) flag to the number of days after a password is set that it expires.

  4. Set the [`password.notify_expiration_in_days`](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags#notify_expiration_in_days) flag to the number of days before a password expires that a user starts receiving password expiration notifications.




For example, to enforce a password policy that states passwords expire after 30 days and that users are notified 15 days before their password expires, you must set the following in your `postgresql.conf` file:

  * `password.enforce_expiration = ON`
  * `password.expiration_in_days = 30`
  * `password.notify_expiration_in_days = 15`



If the password of a user expires, that user can't connect to AlloyDB Omni. To reset the password of a user, do the following:

  1. Connect to AlloyDB Omni using `psql`. For example, if you installed AlloyDB Omni using Docker, run the following command:

`sh docker exec -it CONTAINER-NAME psql -h localhost -U postgres`

  2. At the `postgres=#` prompt, run the following command:
         
         ALTER USER USERNAME WITH 'NEW-PASSWORD';
         




For more information about changing a user's password, see [`ALTER ROLE`](https://www.postgresql.org/docs/current/sql-alterrole.html) in PostgreSQL documentation. 

### Don't allow usernames in passwords

To enforce the policy that prevents a password from containing a username, do the following:

  1. Verify the your `postgresql.conf` file preloads password validation library.

  2. Set the [`password.enforce_password_does_not_contain_username`](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/password-policy-flags#enforce-password-does-not-contain-username) to `ON`.




For example, to ensure that a password doesn't contain a username as a substring, you set the following in your `postgresql.conf` file:

  * `password.enforce_password_does_not_contain_username = ON`



If this flag is set, then the following operation fails because the password `alex-secret` contains the username `alex`:
    
    
    CREATE USER alex WITH PASSWORD 'alex-secret';
    

## What's next

  * Learn how to [backup and restore AlloyDB AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/backup-overview)
  * [Create a read-only replica](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/set-up-read-replica)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
