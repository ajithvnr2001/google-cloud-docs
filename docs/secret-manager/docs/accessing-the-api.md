---
url: https://docs.cloud.google.com/secret-manager/docs/accessing-the-api/
title: Access the Secret Manager API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:44.350488+00:00
---

# Access the Secret Manager API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/accessing-the-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Access the Secret Manager API Stay organized with collections  Save and categorize content based on your preferences. 

We recommend that you access Secret Manager API using the following tools:

  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/secrets), which provides a command-line interface for managing secrets.

  * Convenient, idiomatic [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries), which lets you access and manage secrets from within your application source code. Client libraries are available in many languages including C#(.NET), Go, Java, Node.js, PHP, Python, and Ruby.




## Before you begin

  1. [Enable the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/configuring-secret-manager).

  2. Requests to the Secret Manager API require authentication. For information, see [Set up authentication for Secret Manager](https://docs.cloud.google.com/secret-manager/docs/authentication#authn-how-to).




## Use Secret Manager with Compute Engine and Google Kubernetes Engine

To use Secret Manager with workloads running on Compute Engine or GKE, the underlying instance or node must have the `cloud-platform` OAuth scope. If you receive an error with the following message, it means the instance or node was not provisioned with the correct OAuth scopes.
    
    
    Request had insufficient authentication scopes
    

The required OAuth scope to use Secret Manager is:
    
    
    https://www.googleapis.com/auth/cloud-platform
    

When creating a new instance, instance group, or node pool, [specify the `cloud-platform` scope](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using):

###  gcloud 
    
    
    gcloud compute instances create "INSTANCE_ID" \
        --scopes "https://www.googleapis.com/auth/cloud-platform"

For an existing instance, instance group, or node pool, [update the access scopes](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes):

###  gcloud 
    
    
    gcloud compute instances set-service-account "INSTANCE_ID" \
        --service-account "SERVICE_ACCOUNT_EMAIL" \
        --scopes "https://www.googleapis.com/auth/cloud-platform"

See the [Compute Engine service account permissions](https://docs.cloud.google.com/compute/docs/access/service-accounts#service_account_permissions) for more information.

## Use Secret Manager with App Engine

To use Secret Manager with workloads running on App Engine, you must grant any [required permissions](https://docs.cloud.google.com/secret-manager/docs/access-control#roles) to the App Engine service.

## What's next

  * Learn more about [managing access to Secret Manager resources with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control).
  * Learn how to [create a secret and access a secret version](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
