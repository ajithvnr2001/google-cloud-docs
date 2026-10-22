---
url: https://docs.cloud.google.com/identity/docs/how-to/setup-devices/
title: Set up the Devices API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:09.338219+00:00
---

# Set up the Devices API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/setup-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up the Devices API

This page explains how to set up the Cloud Identity Devices API. You can use the Devices API to programmatically provision resources—for example managing Google Groups—on behalf of an administrator.

## Enable the API and setting up credentials

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)




## Set up API access using a service account with domain-wide delegation

This section describes how to create and use a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to access Google Workspace resources. Authenticating directly to the Devices API using a service account isn't supported, so you must use this method.

### Create a service account and configure it for domain-wide delegation

To create a service account a download the service account key, do the following:

  1. To create a service account, do the following:

     1. In the Google Cloud console go to the IAM service accounts page:

[Go to service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

     2. Click add **Create service account**.

     3. Under **Service account details** , type a name, ID, and description for the service account, then click **Create and continue**.

     4. Optional: Under **Grant this service account access to project** , select the IAM roles to grant to the service account.

     5. Click **Continue**.

     6. Optional: Under **Grant users access to this service account** , add the users or groups that are allowed to use and manage the service account.

     7. Click **Done**.

  2. To let the service account access Devices API by using domain-wide delegation, follow the instructions in [Set up domain-wide delegation for the service account](https://support.google.com/a/answer/162106).

  3. To create and download a service account key, do the following.

**Important:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

     1. Click the email address for the service account you created.
     2. Click the **Keys** tab.
     3. In the **Add key** drop-down list, select **Create new key**.
     4. Click **Create**.

A JSON-formatted credential file, containing a new public and private key pair, is generated and downloaded to your machine. The file contains the only copy of the keys. You are responsible for storing it securely. If you lose the key pair, you must generate a new one.




### Review log entries

When reviewing log entries, note that audit logs will show any service account actions as having been initiated by the user. This is because domain-wide delegation works by allowing the service account to impersonate an administrator user.

### Initialize credentials

When you initialize the credential in your code, specify the email address on which the service account acts by calling `with_subject()` on the credential. For example:

###  Python 
    
    
    credentials = service_account.Credentials.from_service_account_file(
      'SERVICE_ACCOUNT_CREDENTIAL_FILE',
      scopes=SCOPES).with_subject(USER
    )
    

Replace the following:

  * `SERVICE_ACCOUNT_CREDENTIAL_FILE`: the service account key file that you created earlier in this document
  * `USER`: the user that the service account impersonates



#### Instantiating a client

The following example shows how to instantiate a client using service account credentials.

###  Python 
    
    
    from google.oauth2 import service_account
    import googleapiclient.discovery
    
    SCOPES = ['https://www.googleapis.com/auth/cloud-identity.devices']
    
    def create_service():
      credentials = service_account.Credentials.from_service_account_file(
        'SERVICE_ACCOUNT_CREDENTIAL_FILE',
        scopes=SCOPES
      )
    
      delegated_credentials = credentials.with_subject('USER')
    
      service_name = 'cloudidentity'
      api_version = 'v1'
      service = googleapiclient.discovery.build(
        service_name,
        api_version,
        credentials=delegated_credentials)
    
      return service
    

Replace the following:

  * `SERVICE_ACCOUNT_CREDENTIAL_FILE`: the service account key file that you created earlier in this document
  * `USER`: the user that the service account impersonates



You can now begin making calls to the Devices API.

To instead authenticate as an end-user, replace the `credential` object from the service account with the `credential` you can obtain in [Obtaining OAuth 2.0 tokens](https://developers.google.com/identity/protocols/oauth2/web-server#obtainingaccesstokens).

## Installing the Python client library

To install the Python client library, run the following command:
    
    
      pip install --upgrade google-api-python-client google-auth \
        google-auth-oauthlib google-auth-httplib2
    

For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
