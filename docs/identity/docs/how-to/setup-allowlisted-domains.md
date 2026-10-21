---
url: https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/
title: Set up the Allowlisted Domains API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:17:01.471934+00:00
---

# Set up the Allowlisted Domains API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/setup-allowlisted-domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up the Allowlisted Domains API

This page explains how to set up the Allowlisted Domains API before [adding](https://docs.cloud.google.com/identity/docs/how-to/create-allowlisted-domains), [listing and getting](https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains), or [deleting](https://docs.cloud.google.com/identity/docs/how-to/delete-allowlisted-domains) allowlisted domains.

## Before you begin

Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. For instructions, see [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin).

## Install the Python client library

To install the Python client library, run the following command:
    
    
      pip install --upgrade google-api-python-client google-auth \
        google-auth-oauthlib google-auth-httplib2
    

For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup).

## Enable the API and set up credentials

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

  8. Create a service account: 
     * Ensure that you have the **Create Service Accounts** IAM role (`roles/iam.serviceAccountCreator`) and the **Project IAM Admin** role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
     * In the Google Cloud console, go to the [**Create service account**](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project) page.
     * Select your project.
     * In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name.
     * In the **Service account description** field, enter a description. For example, `Service account for quickstart`.
     * Click **Create and continue**.
     * Grant the **Project > Owner** role to the service account. To grant the role, find the **Select a role** list, then select **Project > Owner**.
     * Click **Continue**.
     * Click **Done** to finish creating the service account. Don't close your browser window. You will use it in the next step.
  9. Create a service account key: 
     * In the Google Cloud console, click the email address for the service account that you created.
     * Click **Keys**.
     * Click **Add key** , and then click **Create new key**.
     * Click **Create**. A JSON key file is downloaded to your computer.
     * Click **Close**.



### Create an API key

  1. In the Google Cloud console, go to the [Credentials](https://console.cloud.google.com/apis/credentials) page.
  2. Click **Create Credentials** and select **API key**.
  3. The **API key created** dialog displays your newly created API key. Copy this key for use in your script as the `API_KEY` constant.



## Authenticate as a service account with domain-wide delegation

If you're an administrator managing allowlisted domains, or if you want to provide an account with domain-wide privileges so that it can manage allowlisted domains on behalf of administrators, you should authenticate as a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) and then grant domain-wide privileges to the service account.

**Note:** Because domain-wide delegation lets the service account impersonate an administrator user, service account actions are logged as having been done by the user.

For details about setting up domain-wide delegation, see [Control API access with domain-wide delegation](https://support.google.com/a/answer/162106). Review the [best practices](https://support.google.com/a/answer/14437356) to mitigate the security risks associated with using domain-wide delegation.

Provide the following scopes to authorize the service account:

  * **For read and write operations** (`create`, `delete`, `list`, `get`): `https://www.googleapis.com/auth/cloud-identity.allowlisteddomains`

  * **For read-only operations** (`list`, `get`): `https://www.googleapis.com/auth/cloud-identity.allowlisteddomains.readonly`




### Initialize credentials and instantiate a client

When you initialize the credential in your code, specify the email address on which the service account acts by calling `with_subject()` on the credential.

The following example shows how to instantiate a client using service account credentials to interact with the Allowlisted Domains API:

###  Python 
    
    
    from google.oauth2 import service_account
    import googleapiclient.discovery
    
    SCOPES = [
        'https://www.googleapis.com/auth/cloud-identity.allowlisteddomains.readonly',
        'https://www.googleapis.com/auth/cloud-identity.allowlisteddomains',
    ]
    SERVICE_ACCOUNT_FILE = 'SERVICE_ACCOUNT_CREDENTIAL_FILE'
    PROD_DISCOVERY_URL_BASE = (
        'https://cloudidentity.googleapis.com/$discovery/rest'
    )
    API_KEY = 'YOUR_API_KEY'
    
    def create_service(version, delegated_email):
      """Instantiates a client using service account credentials."""
      credentials = service_account.Credentials.from_service_account_file(
          SERVICE_ACCOUNT_FILE, scopes=SCOPES
      )
      delegated_credentials = credentials.with_subject(delegated_email)
      url = f'{PROD_DISCOVERY_URL_BASE}?version={version}&key={API_KEY}'
    
      service = googleapiclient.discovery.build(
          serviceName=None,
          version=None,
          credentials=delegated_credentials,
          discoveryServiceUrl=url,
          static_discovery=False,
      )
      return service
    

Replace the following:

  * `SERVICE_ACCOUNT_CREDENTIAL_FILE`: the service account key file that you created earlier in this document
  * `YOUR_API_KEY`: the API key copied from your Google Cloud console Credentials page



Detailed sample code to call the Allowlisted Domains API operations are provided in [Listing and getting allowlisted domains](https://docs.cloud.google.com/identity/docs/how-to/list-get-allowlisted-domains).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
