---
url: https://docs.cloud.google.com/alloydb/docs/database-users/manage-password-policy/
title: Manage built-in authentication using password policies \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:13.319433+00:00
---

# Manage built-in authentication using password policies  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-users/manage-password-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage built-in authentication using password policies Stay organized with collections  Save and categorize content based on your preferences. 

You can set and manage password policies for database users of your AlloyDB for PostgreSQL instances.

For an overview of authentication methods available in AlloyDB, see [Authentication](https://docs.cloud.google.com/alloydb/docs/connection-overview#authn).

## About password policies

If your application's database users authenticate with your AlloyDB instances using the built-in, password-based method, then you can make authentication more secure by enforcing strong passwords. You can define and enable password enforcement by setting a password policy on your instances.

**Note:** As a secure and reliable alternative to password-based authentication, consider using authentication based on Identity and Access Management (IAM). For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/manage-iam-authn).

### Limitations of password policies

AlloyDB password policies have the following limitations:

  * Password policies apply to passwords created only after you set the policies. Existing user passwords aren't affected by a change in password policy.

  * Password policies apply to passwords entered only as plain text. Password policies don't apply to passwords entered as encrypted strings.




## Set an instance password policy

You can set a password policy on an instance by [configuring password flags on an instance](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags).

  * **Disallow username** : prevent the username from being used in the password.

  * **Password complexity** : check if the password contains the allowed number of lowercase, uppercase, numeric, and non-alphanumeric characters. Also check if the password length is valid.

  * **Password expiry** : make sure that passwords are rotated periodically.




For a list of the password policy flags that AlloyDB supports, see [Password policy flags](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags).

To comply with security standards and align with the security recommender's guidance, you must enable all three options together by configuring their primary enforcement flags to `ON`:

  * `password.enforce_password_does_not_contain_username`
  * `password.enforce_complexity`
  * `password.enforce_expiration`



If you set any of these three flags to `OFF` or omit them, the security recommender flags the instance as not having a password policy enabled.

### Enforce password complexity

To enforce a password-complexity policy, do the following:

  1. Set the [`password.enforce_complexity`](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags#enforce_complexity) flag to `ON`.
  2. Use [password policy flags](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags) to define your password policy.



For example, to enforce a password policy that states a password must contain at least one uppercase letter, one number, and be at least 10 characters long, you must set the following flags:

  * `password.enforce_complexity` to `ON`
  * `password.min_uppercase_letters` flag to `1`
  * `password.min_numerical_chars` flag to `1`
  * `password.min_pass_length` flag to `10`



After these flags are set, an attempt to set a database user password that doesn't comply with this password policy fails. For example, with this policy set, the following `psql` client command fails because the password `foo` is less than 10 characters and doesn't contain a number or an upper case character.
    
    
    CREATE USER USERNAME WITH PASSWORD 'foo';
    

### Enforce password expiration

To enforce the password expiration policy, do the following:

  1. Set the [`password.enforce_expiration`](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags#enforce_expiration) flag to `ON`.

  2. Set the [`password.expiration_in_days`](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags#expiration_in_days) flag to the number of days after a password is set that it expires.

  3. Set the [`password.notify_expiration_in_days`](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags#notify_expiration_in_days) flag to the number of days before a password expires that a user starts receiving password expiration notifications.




For example, to enforce a password policy that states passwords expire after 30 days and that users are notified 15 days before their password expires, you set the following:

  * `password.enforce_expiration` to `ON`
  * `password.expiration_in_days` flag to `30`
  * `password.notify_expiration_in_days` flag to `15`



If the password of a user expires, that user can't connect to the AlloyDB instance. To reset the password of a user, see [Change the password of a database user](https://docs.cloud.google.com/alloydb/docs/database-users/about#change-password).

### Don't allow usernames in passwords

To enforce the policy that prevents a password from containing a username, do the following:

  * Set the [`password.enforce_password_does_not_contain_username`](https://docs.cloud.google.com/alloydb/docs/reference/password-policy-flags#enforce-password-does-not-contain-username) to `ON`.



For example, to ensure that a password doesn't contain a username as a substring, you set the following:

  * `password.enforce_password_does_not_contain_username` to `ON`



If this flag is set, then the following operation fails because the password `alex-secret` contains the username `alex`:
    
    
    CREATE USER alex WITH PASSWORD 'alex-secret';
    

## What's next

  * [Manage AlloyDB user roles](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles)
  * [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
