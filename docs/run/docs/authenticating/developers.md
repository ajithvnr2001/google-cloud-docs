---
url: https://docs.cloud.google.com/run/docs/authenticating/developers/
title: Authenticate developers \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:28.767270+00:00
---

# Authenticate developers  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/authenticating/developers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Authenticate developers Stay organized with collections  Save and categorize content based on your preferences. 

In addition to administrative actions such as creating, updating, and deleting services, developers often want to test services privately before releasing them. This option is for Cloud Run services and not Cloud Run jobs.

## Before you start

Make sure you grant permissions to access the services you are authenticating to. You must grant the Cloud Run Invoker role to the developer or group of developers:

### Console UI

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/run/)

  2. Select the service, but don't click it.

  3. Click the **Permissions** tab in the right side panel. (You might need to first click **Show Info Panel** in the top right corner.)

  4. Click **Add Principal**.

  5. In the **New principals** field, enter the developer account email.

  6. Select the `Cloud Run Invoker` role from the **Select a role** drop-down menu.

  7. Click **Save**.




###  gcloud 

Use the `gcloud run services add-iam-policy-binding` command:
    
    
    gcloud run services add-iam-policy-binding SERVICE \
      --member='USER:EMAIL' \
      --role='roles/run.invoker'

where

  * SERVICE is the name of the service.
  * USER is the value `user` or `group` depending on whether you are authorizing a single developer or a group.
  * EMAIL is the email account.

For example:
        
        gcloud run services add-iam-policy-binding myservice \
        --member='user:test-user@gmail.com' \
        --role='roles/run.invoker'




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service_iam_binding" "binding" {
      project = "PROJECT"
      location = "LOCATION"
      name = "SERVICE"
      role = "roles/run.invoker"
      members = [
          "user:EMAIL",
      ]
    }
    

Replace:

  * PROJECT with the project ID the service belongs to.
  * LOCATION with the location of the Cloud Run service.
  * SERVICE with the name of the Cloud Run service to bind the IAM policy to.
  * EMAIL with the user's email account you are granting permissions for.



## Test your private service

You can use the Cloud Run proxy or `curl` to test your private service.

### Use the Cloud Run proxy in Google Cloud CLI

The easiest way for you to test private services is to use the [Cloud Run proxy in Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/proxy). This proxies the private service to `http://localhost:8080` (or to the port specified with `--port`), providing the token of the active account or another token you specify. This lets you use a web browser or a tool like `curl`. This is the recommended way to test privately a website or API in your browser.

You can proxy a service locally using the following command line in a Linux, macOS, [WSL (preferred)](https://docs.microsoft.com/en-us/windows/wsl/install-win10), or [cygwin](https://cygwin.com/install.html) environment:
    
    
    gcloud run services proxy SERVICE --project PROJECT-ID

### Use `curl`

Alternatively, you can test private services without the proxy by using a tool like `curl` and by passing an auth token in the `Authorization` header:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" SERVICE_URL

For the `curl` command to work, you must pass a valid ID token for a user with the `run.routes.invoke` permission, such as the _Cloud Run Admin_ or _Cloud Run Invoker_. See [Cloud Run IAM Roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) for the full list of roles and their associated permissions.

**Note:** To use the `curl` command on Microsoft Windows, you might need the [WSL (preferred)](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or [cygwin](https://cygwin.com/install.html) command line.

To get a valid ID token for the identity logged into the gcloud CLI, use the [`gcloud auth print-identity-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-identity-token) command. You can use tokens created by the gcloud CLI to invoke HTTP requests in any project, as long as your account has the `run.routes.invoke` permission on the service.

For development purposes, use gcloud CLI-generated ID tokens. However, note that such tokens lack an audience claim, which makes them susceptible to replay attacks. In production environments, use ID tokens issued for a service account with the appropriate audience specified. This approach enhances security by restricting token usage to the intended service only. For non-user accounts, use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) to invoke your Cloud Run service so you don't have to download a service account key.

When this document uses the term _user account_ , it refers to a Google Account, or a user account managed by your identity provider and federated with [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 

You use the credentials provided by your user account to sign in to the tool.

We recommend that you allocate the [minimum set of permissions](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges) required to develop and use your services. Make sure that IAM policies on your services are limited to the minimum number of users and service accounts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
