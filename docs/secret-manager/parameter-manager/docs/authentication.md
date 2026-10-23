---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/authentication/
title: Authenticate to Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:43.684296+00:00
---

# Authenticate to Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)



Send feedback 

#  Authenticate to Secret Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to authenticate to Secret Manager programmatically. How you authenticate to Secret Manager depends on the interface you use to access the API and the environment where your code is running. 

For more information about Google Cloud authentication, see the [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

## API access

Secret Manager supports programmatic access. You can access the API in the following ways: 




## Set up authentication for Secret Manager

How you set up authentication depends on the environment where your code is running. 

The following options for setting up authentication are the most commonly used. For more options and information about authentication, see [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

Before you complete these instructions, you must complete the basic setup for Secret Manager, as described in [Enable the Parameter Manager API](https://docs.cloud.google.com/parameter-manager/docs/prepare-environment#enable_api). 

### For a local development environment

You can set up credentials for a local development environment in the following ways: 

  * User credentials for client libraries or third-party tools
  * Service account impersonation



#### Client libraries or third-party tools

Set up [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) in your local environment: 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




For more information about working with ADC in a local environment, see [Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 

#### Service account impersonation

In most cases, you can use your user credentials to authenticate from a local development environment. If that is not feasible, or if you need to test the permissions assigned to a service account, you can use service account impersonation. You must have the `iam.serviceAccounts.getAccessToken` permission, which is included in the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role. 

You can set up the gcloud CLI to use service account impersonation by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config): 
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL

For select languages, you can use service account impersonation to create a local ADC file for use by client libraries. This approach is supported only for the Go, Java, Node.js, and Python client libraries—it is not supported for the other languages. To set up a local ADC file with service account impersonation, use the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) with the [`gcloud auth application-default login` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login): 
    
    
    gcloud auth application-default login --impersonate-service-account=SERVICE_ACCT_EMAIL

For more information about service account impersonation, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). 

### On Google Cloud

To authenticate a workload running on Google Cloud, you use the credentials of the service account attached to the compute resource where your code is running, such as a [ Compute Engine virtual machine (VM) instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using). This approach is the preferred authentication method for code running on a Google Cloud compute resource. 

For most services, you must attach the service account when you create the resource that will run your code; you cannot add or replace the service account later. Compute Engine is an exception—it lets you attach a service account to a VM instance at any time. 

Use the gcloud CLI to create a service account and attach it to your resource: 

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. Set up authentication:

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. Create the service account: 
            
            gcloud iam service-accounts create SERVICE_ACCOUNT_NAME

Replace `SERVICE_ACCOUNT_NAME` with a name for the service account. 

     3. To provide access to your project and your resources, grant a role to the service account: 
            
            gcloud projects add-iam-policy-binding PROJECT_ID --member="serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com" --role=ROLE

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `ROLE`: the role to grant
**Note** : The `--role` flag affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
     4. To grant another role to the service account, run the command as you did in the previous step. 
     5. Grant the required role to the principal that will attach the service account to other resources. 
            
            gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com --member="user:USER_EMAIL" --role=roles/iam.serviceAccountUser

Replace the following: 

        * `SERVICE_ACCOUNT_NAME`: the name of the service account
        * `PROJECT_ID`: the project ID where you created the service account
        * `USER_EMAIL`: the email address for a Google Account
  3. Create the resource that will run your code, and attach the service account to that resource. For example, if you use Compute Engine: 

Create a Compute Engine instance. Configure the instance as follows: 
     * Replace `INSTANCE_NAME` with your preferred instance name. 
     * Set the `--zone` flag to the [zone](https://docs.cloud.google.com/compute/docs/zones#available) in which you want to create your instance. 
     * Set the `--service-account` flag to the email address for the service account that you created. 
    
    gcloud compute instances create INSTANCE_NAME --zone=ZONE --service-account=SERVICE_ACCOUNT_EMAIL




For more information about authenticating to Google APIs, see [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

### On-premises or on a different cloud provider

The preferred method to set up authentication from outside of Google Cloud is to use workload identity federation. For more information, see [Set up ADC for on-premises or another cloud provider](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises) in the authentication documentation. 

## Access control for Secret Manager

After you authenticate to Secret Manager, you must be authorized to access Google Cloud resources. Secret Manager uses Identity and Access Management (IAM) for authorization. 

For more information about the roles for Secret Manager, see [Access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control). For more information about IAM and authorization, see [IAM overview](https://docs.cloud.google.com/iam/docs/overview). 

## What's next

  * Learn about [Google Cloud authentication methods](https://docs.cloud.google.com/docs/authentication#auth-decision-tree). 
  * See a list of [authentication use cases](https://docs.cloud.google.com/docs/authentication/use-cases). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
