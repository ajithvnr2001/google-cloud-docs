---
url: https://docs.cloud.google.com/docs/terraform/authentication/
title: Authentication for Terraform \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:38.328035+00:00
---

# Authentication for Terraform  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Reference ](https://docs.cloud.google.com/docs/terraform/api)



Send feedback 

#  Authentication for Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to authenticate to Google Cloud when using Terraform.

Application Default Credentials (ADC) is the recommended way to authenticate to Google Cloud when using Terraform. ADC is a strategy used by the authentication libraries to automatically find credentials based on the application environment. When you use ADC, Terraform can run in either a development or production environment without changing how it authenticates to Google Cloud services and APIs. For information about where ADC looks for credentials and in what order, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

## Authenticate when using Terraform in a local development environment

When you're using Terraform in a local development environment, such as a development workstation, you can authenticate using the credentials associated with your [user account](https://docs.cloud.google.com/docs/authentication#user-accounts) or [service account](https://docs.cloud.google.com/iam/docs/service-account-overview).

### Authenticate using a user account

To configure ADC with a user account, you use the Google Cloud CLI:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




### Authenticate using service account impersonation

You can use service account impersonation to set up a local ADC file. Terraform uses those credentials automatically.

  1. Make sure you must have the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) IAM role on the service account you are impersonating. For more information, see [Required roles](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation#required-roles).

  2. Use service account impersonation to create a local ADC file by running the following command:
         
         gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL
         




If you want to allow users to use a shared primary authentication source and a variable service account per environment, set the [`impersonate_service_account`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference#impersonate_service_account) field in your Terraform configuration file:
    
    
    provider "google" {
      impersonate_service_account = "SERVICE_ACCT_EMAIL"
    }
    

## Authenticate when running Terraform on Google Cloud

When running Terraform on a Google Cloud cloud-based development environment such as Cloud Shell, the tool uses the credentials you provided when you signed in for authentication.

When using Terraform with Google Cloud services such as Compute Engine, App Engine, and Cloud Run functions, you can attach a [user-managed service account](https://docs.cloud.google.com/iam/docs/service-account-types#user-created) to resources. Generally, attaching a service account is supported when that service's resources can run or include application code. When you attach a service account to a resource, the code running on the resource can use that service account as its identity.

Attaching a user-managed service account is the preferred way to provide credentials to ADC for production code running on Google Cloud.

**Note:** Many of these Google Cloud services also provide a default service account. Using the default service account is not recommended, because by default the default service account is highly privileged, which violates the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

For help determining the roles that you need to provide to your service account, see [Choose predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

For information about which resources you can attach a service account to, and help with attaching the service account to the resource, see the [IAM documentation on attaching a service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-new-resource).

Set up authentication:

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



## Authenticate when running Terraform on-premises or on a different cloud provider

If you are running your application outside of Google Cloud, you need to provide credentials that are recognized by Google Cloud to use Google Cloud services.

### Authenticate using Workload Identity Federation

The preferred way to authenticate with Google Cloud using credentials from an external IdP is to use [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). You can create a credential configuration file and set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to point to it. This approach is more secure than creating a service account key. For instructions on setting up Workload Identity Federation for ADC, see [Workload Identity Federation with other clouds](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds).

## Authenticate using service account keys

When running Terraform in a local development environment, on premises, or a different cloud provider, you can create a service account, grant it the IAM roles that your application requires, and create a key for the service account.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To create a service account key and make it available to ADC:

  1. Create a service account with the roles your application needs, and a key for that service account, by following the instructions in [Creating a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating).




## Authenticate to Cloud Storage backends

Terraform lets you configure Cloud Storage as a backend to store Terraform state files. To authenticate to a [Cloud Storage backend](https://docs.cloud.google.com/docs/terraform/resource-management/store-state), use any of the methods described on this page. For information on configuration variables related to authentication for Cloud Storage backends, see the [Terraform backends page for Cloud Storage](https://developer.hashicorp.com/terraform/language/settings/backends/gcs#configuration-variables).

## What's next

  * Work through the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance)
  * Learn about the [basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
