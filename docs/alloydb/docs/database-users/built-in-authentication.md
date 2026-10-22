---
url: https://docs.cloud.google.com/alloydb/docs/database-users/built-in-authentication/
title: AlloyDB for PostgreSQL built-in database authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:12.299895+00:00
---

# AlloyDB for PostgreSQL built-in database authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/database-users/built-in-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  AlloyDB for PostgreSQL built-in database authentication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how built-in authentication works on AlloyDB for PostgreSQL instances and how database administrators can set password policies for local database users.

Authentication is the process of verifying the identity of a user who is attempting to access data in the database. AlloyDB uses the following types of authentication for database users:

  * **PostgreSQL's native built-in authentication** uses a username and a password to authenticate local database users. The current page describes this type of authentication.

  * **IAM database authentication** uses IAM to authenticate a user. For more information, see [AlloyDB IAM database authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication).




Although IAM database authentication is more secure and reliable, you might prefer to use built-in authentication or a hybrid authentication model that includes both authentication types.

You might create and manage local database users locally within a database to allow specific persons or applications to access a database. Such database users own the objects they create in the database. AlloyDB offers strong built-in password enforcement. You can define and enable such enforcement through [password policies](https://docs.cloud.google.com/alloydb/docs/database-users/manage-password-policy).

## Password policies

You can set a password policy on the primary instance of a cluster. While this is an instance-level setting, it's best to think of it as a cluster-level policy, as users are defined for the entire cluster, and write operations like user creation can only be handled by the primary instance.

You can set a password policy when you create a primary instance, or you can add or modify a policy at a later time by updating the instance. This policy applies to all databases within the instance and can include the following options:

  * **Minimum length** : specify the minimum number of characters that the password must have.

  * **Password complexity** : check if the password is a combination of lowercase, uppercase, numeric, and non-alphanumeric characters.

  * **Disallow username** : prevent the use of the username in the password.

  * **Password expiration** : make sure that passwords are rotated periodically.




## AlloyDB built-in authentication for read replicas

Password policies for read replicas are inherited from the primary instance and can't be modified independently. This is because user management and authentication are write operations that can only be performed on the primary instance.

When you promote a read replica to become a primary instance, the password policy is not automatically carried over. You must explicitly enable the password policy on the newly promoted instance, including all the specific policy options you want to enforce.

## What's next

  * [Manage built-in authentication using password policies](https://docs.cloud.google.com/alloydb/docs/database-users/manage-password-policy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
