---
url: https://docs.cloud.google.com/alloydb/docs/connect-gcloud/
title: Connect using gcloud CLI \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:47.274182+00:00
---

# Connect using gcloud CLI  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/connect-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Connect using gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#0) of the Google Cloud Terms of Service. Pre-GA products might have limited support, and changes to pre-GA products might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The [`gcloud beta alloydb connect`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/alloydb/connect) command lets you establish an authorized, encrypted connection to an AlloyDB for PostgreSQL instance. It automates starting the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview) and running the `psql` client tool.

Use this command for manual database administration and development from environments like your local machine or Cloud Shell.

To learn more, see [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).

## Before you begin

  1. [Install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).
  2. [Install the `psql` client tool](https://docs.cloud.google.com/alloydb/docs/install-psql).
  3. Ensure your Identity and Access Management (IAM) principal has the AlloyDB Client (`roles/alloydb.client`) role. For more information, see [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).



## Connect to an instance

To connect to an instance using the default `postgres` user and database over private IP, run:
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID
    

**Note:** You must have a network path to your instance. For example, run the command from a Virtual Private Cloud (VPC) network that can reach your target instance.

### Connect over public IP

If your instance has a public IP address enabled, you can connect to it by adding the `--public-ip` flag:
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --public-ip
    

### Authenticate using IAM

The `gcloud beta alloydb connect` command supports automatic IAM authentication. Use the `--auto-iam-authn` flag to authenticate as the signed-in gcloud CLI user or a service account.
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --auto-iam-authn
    

For more information about IAM authentication, see [IAM database authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication).

### Connect over Private Service Connect

If you are using Private Service Connect, add the `--psc` flag:
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --psc
    

### Connect with a specific user and database

To connect as a specific database user to a specific database, use the `--user` and `--database` flags:
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --user=USER_NAME \
        --database=DATABASE_NAME
    

### Service account impersonation

You can use an impersonated service account to authorize the connection. When you use impersonation, the Auth Proxy uses the credentials of the specified service account to retrieve connection information.

To connect using an impersonated service account, add the `--impersonate-service-account` flag:
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --impersonate-service-account=SERVICE_ACCOUNT_EMAIL
    

The Auth Proxy uses the impersonated service account to retrieve connection information. However, it does not automatically authenticate to the database. To also authenticate to the database as the impersonated service account, add the `--auto-iam-authn` flag. The impersonated service account must be a user in your database.
    
    
    gcloud beta alloydb connect INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --impersonate-service-account=SERVICE_ACCOUNT_EMAIL \
        --auto-iam-authn
    

## What's next

  * Learn about [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview).
  * Learn about [Choose a connectivity option](https://docs.cloud.google.com/alloydb/docs/choose-alloydb-connectivity).
  * Learn more about the [AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
