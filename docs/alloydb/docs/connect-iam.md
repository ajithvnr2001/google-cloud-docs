---
url: https://docs.cloud.google.com/alloydb/docs/connect-iam/
title: Connect using an IAM account \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:29.470048+00:00
---

# Connect using an IAM account  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect using an IAM account Stay organized with collections  Save and categorize content based on your preferences. 

To authenticate to an AlloyDB for PostgreSQL instance by using Identity and Access Management (IAM) credentials instead of built-in database passwords, you can sign in with an OAuth 2.0 access token or configure automatic IAM authentication. You can also perform an IAM-based sign-in by using the `psql` command-line client.

For an overview of connecting to AlloyDB instances, see [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).

## Before you begin

Your project, cluster, instances, and IAM user accounts all require preparation before you can sign in to an AlloyDB instance using IAM credentials.

**Caution:** There is a per-minute sign-in quota for each instance, which includes both successful and unsuccessful sign-ins. When the quota is exceeded, sign-ins are temporarily unavailable. We recommend that you avoid frequent sign-ins and restrict sign-ins using authorized networks.

For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).

## Authenticate with an OAuth 2.0 token

A user or an application can authenticate with an AlloyDB database by following these steps:

  1. If you haven't already done so, [authenticate for the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/authenticate) using the same user or service account that you want to sign in to your AlloyDB instance with.

  2. Request an OAuth 2.0 token from Google Cloud using [the `gcloud auth print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token):
         
         gcloud auth print-access-token

Google Cloud prints an OAuth 2.0 token as the output of this command.

For additional security, you can restrict the token for use with only AlloyDB authentication by following these alternative steps:

     1. Add the `alloydb.login` scope to your current environment's access credentials using [the `gcloud auth application-default login` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login), if you have not already done so:
            
            gcloud auth application-default login --scopes=https://www.googleapis.com/auth/alloydb.login,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/userinfo.email,openid

     2. Print a restricted OAuth 2.0 token using [the `gcloud auth application-default print-access-token` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token), scoping the token only to AlloyDB authentication:
            
            gcloud auth application-default print-access-token --scopes=https://www.googleapis.com/auth/alloydb.login

**Caution:** Treat your OAuth 2.0 token as sensitive information. Either store it securely, or don't store it at all after use.

The OAuth 2.0 token lets you—or anyone—make authenticated requests to Google Cloud on your behalf. Treat the token with the same level of security as a password. Either store the token securely, or avoid storing it at all. The example use of `psql` later on this page demonstrates a way to request, use, and discard an OAuth 2.0 token in a single action.

  3. Sign in to an AlloyDB instance with standard PostgreSQL techniques, using these credentials:

     * Present the access token you acquired in the previous step as your password.

     * For an IAM user account, the database username is the account's full email address.

     * For an IAM service account, the database username is the account's email address without the `.gserviceaccount.com` suffix.




The following `psql` command demonstrates one way to sign in to an IAM user on the command line. It assigns the output of `gcloud auth print-access-token` to the `PGPASSWORD` environment variable, which `psql` subsequently uses as a database login password.
    
    
    PGPASSWORD=$(gcloud auth print-access-token) psql \
      -h INSTANCE_ADDRESS \
      -U USERNAME \
      -d DATABASE

Replace the following:

  * `INSTANCE_ADDRESS`: The IP address of the AlloyDB instance to connect to.

  * `USERNAME`: An identifier for the IAM user to authenticate with the instance.

For an IAM user account, supply the user account's full email address. For example, `kai@example.com`.

For an IAM service account, supply the service account's address _without_ the `.gserviceaccount.com` suffix. For example, to specify the service account `my-service@my-project.iam.gserviceaccount.com`, you would use the value `my-service@my-project.iam` here.

  * `DATABASE`: The name of the database to connect to.




Note that `psql` truncates passwords entered on the command line that are longer than 100 characters. To use `psql` with an OAuth 2.0 token as a login password, you must set the `PGPASSWORD` environment variable as demonstrated in this example, rather than manually paste it when prompted.

## Authenticate automatically

To automatically authenticate an IAM-based AlloyDB user without the need for an OAuth 2.0 token, you have two options: [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect) and [AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors).

The IAM account that you use to run the proxy client or Language Connectors must be the same account that you added as a database user. For example, if you run your workload using the IAM user account `kai@example.com`, then you can use the proxy client or Language Connectors to automatically authenticate the `kai@example.com` database user without specifying an OAuth 2.0 token. In this example, automatic authentication does not work with any other database user except for `kai@example.com`.

###  Auth Proxy 

Using the Auth Proxy requires running the Auth Proxy client with the `--auto-iam-authn` flag enabled.

For more information about running the Auth Proxy, see [Connect using the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/connect).

###  Language Connectors 

Using Language Connectors requires enabling IAM authentication programmatically. For the AlloyDB Python Connector, automatic IAM authentication (`enable_iam_auth=True`) is supported with the `pg8000` and `asyncpg` drivers. There is a corresponding option for each language on [Configure the AlloyDB Language Connectors](https://docs.cloud.google.com/alloydb/docs/connect-language-connectors#configure-connectors).

## What's next

  * [Manage your IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth)
  * [Troubleshoot IAM authentication](https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-iam-auth)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
