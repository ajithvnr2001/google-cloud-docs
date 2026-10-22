---
url: https://docs.cloud.google.com/identity/docs/how-to/setup-policies/
title: Setting up the Policy API \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:20.971405+00:00
---

# Setting up the Policy API  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/setup-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Setting up the Policy API

This page explains how to set up the Cloud Identity Policy API before [listing and getting policies](https://docs.cloud.google.com/identity/docs/how-to/list-get-policies).

## Install the Python client library

To install the Python client library, run the following command:
    
    
      pip install --upgrade google-api-python-client google-auth \
        google-auth-oauthlib google-auth-httplib2 absl-py
    

For more on setting up your Python development environment, refer to the [Python Development Environment Setup Guide](https://docs.cloud.google.com/python/docs/setup).

## Enable the API and set up service account credentials

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

  5. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Service Account Token Creator** role to the service account. 

To grant the role, find the **Select a role** list, then select **Service Account Token Creator**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. In the **Service account users role** field, enter the identifier for the principal that will attach the service account to other resources, such as Compute Engine instances. 

This is typically the email address for a Google Account.

     9. Click **Done** to finish creating the service account. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Identity API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudidentity.googleapis.com)

  9. Create a service account: 

     1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
     2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
     3. Select your project. 
     4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

     5. Click **Create and continue**. 
     6. Grant the **Service Account Token Creator** role to the service account. 

To grant the role, find the **Select a role** list, then select **Service Account Token Creator**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. 
     7. Click **Continue**. 
     8. In the **Service account users role** field, enter the identifier for the principal that will attach the service account to other resources, such as Compute Engine instances. 

This is typically the email address for a Google Account.

     9. Click **Done** to finish creating the service account. 




## Authenticate as a service account with domain-wide delegation

If you're an administrator managing identity policies, or if you want to provide an account with domain-wide privileges so that it can manage Google policies on behalf of administrators, you should authenticate as a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) and then grant domain-wide privileges to the service account.

**Note:** Because domain-wide delegation lets the service account impersonate an administrator user, service account actions are logged as having been done by the user.

For details about setting up domain-wide delegation, see [Control API access with domain-wide delegation](https://support.google.com/a/answer/162106). Review the [best practices](https://support.google.com/a/answer/14437356) to mitigate the security risks associated with using domain-wide delegation.

After setting up domain wide delegation, [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) can be used for authentication. When you use ADC, your code can run in either a development or production environment without changing how your application authenticates to Google Cloud services and APIs. When initializing the credentials in your code, specify the email address that the service account acts on by using the `subject()` parameter on the credential. Make sure that the email address is granted the `Service Account User` role on the service account (as described above). For example:

> **Important:** The OAuth scopes specified in your application code used to create delegated credentials must be present in the authorized scopes list for domain-wide delegation in the Google Admin Console. A broader or more permissive scope won't work. If a scope requested by the application to create delegated credentials is not authorized in domain-wide delegation, the application receives an `unauthorized_client` error.

###  Python 
    
    
    AUTH_SCOPES = ['https://www.googleapis.com/auth/iam']
    # The read and write scope of the API. Note that you must authorize the
    # exact same scope for domain-wide delegation in the Google Admin Console.
    POLICY_SCOPES = ['https://www.googleapis.com/auth/cloud-identity.policies']
    TOKEN_URI = "https://accounts.google.com/o/oauth2/token"
    
    _ADMIN_EMAIL = flags.DEFINE_string(
        name='admin_email',
        default=None,
        help='Administrator email to call as',
        required=True,
    )
    
    # Fetch application default credentials (ADC)
    credentials, _ = google.auth.default(scopes=AUTH_SCOPES)
    
    # Populate account information
    request = requests.Request()
    credentials.refresh(request)
    
    # Create an IAM signer
    signer = iam.Signer(request, credentials,
                        credentials.service_account_email)
    
    # Create domain-wide delegated (DWD) credentials
    delegated_credentials = service_account.Credentials(
        signer=signer,
        service_account_email=credentials.service_account_email,
        token_uri=TOKEN_URI,
        scopes=POLICY_SCOPES,
        subject=_ADMIN_EMAIL.value
    )
    

In order to impersonate a service account when using Application default credentials, use the `impersonate-service-account` flag.

###  Shell 
    
    
    gcloud auth application-default login --impersonate-service-account=<service_account_email>
    --scopes=https://www.googleapis.com/auth/iam,https://www.googleapis.com/auth/cloud-identity.policies
    

Detailed sample code to call Policy API, including the code for authentication, are provided in [Listing and getting policies](https://docs.cloud.google.com/identity/docs/how-to/list-get-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
