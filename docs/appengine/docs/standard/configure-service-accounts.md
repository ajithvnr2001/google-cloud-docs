---
url: https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts/
title: Configure App Engine service accounts \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:14.086979+00:00
---

# Configure App Engine service accounts  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Configure App Engine service accounts Stay organized with collections  Save and categorize content based on your preferences. 

App Engine applications require a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to access other Google Cloud services and execute tasks.

There are two types of service accounts in App Engine and any service account in your Cloud project can be assigned to act as either the app-level default or per-version service account:

  * **App-level default service account** \- This service account is used for all of your deployed services when you don't configure a "per-version service account". You can choose to assign a service account that you created or use the [auto-created default service account](https://docs.cloud.google.com/iam/docs/service-account-types#default) that gets created when you initially deploy a service to your Cloud project. For example, the _App Engine default service account_ (_`PROJECT_ID @appspot.gserviceaccount.com`_).

  * **Per-version service account** \- A service account configured as the identity for a specific version of your deployed service. When deploying an existing version or a new version, you can specify a service account to act as that version's identity. For example, if a version requires permissions that differ from the app-level default service account, you can assign a service account that is specific to that version.




## View your configured service accounts

To view the current app-level default service account, run the `gcloud app describe` command.

To view the service account used by a deployed version:

### gcloud

Run the `gcloud app versions describe` command:
    
    
      gcloud app versions describe VERSION_ID --service=SERVICE_NAME
    

Replace:

  * `VERSION_ID` with the ID of the version.
  * `SERVICE_NAME` with the name of the service that you created.



### Console

  1. Go to the App Engine **Versions** tab in the console. [Go to Versions](https://console.cloud.google.com/appengine/versions)
  2. Locate the email address of your App Engine version-specific service account. Example: `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`



## Assign an app-level default service account

By default, the app-level default service account is the auto-created _`PROJECT_ID @appspot.gserviceaccount.com`_ service account. You can assign another service account to act as the app-level default service account using Google Cloud CLI, Google Cloud console, or Admin API.

### Specify an app-level default service account during app creation

During the initial App Engine application creation process, you can choose to assign a service account that you [created](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) or use the auto-created _`PROJECT_ID @appspot.gserviceaccount.com`_ service account to act as the default.

To create a your App Engine application and assign an app-level default service account, you can use one of the following:

### gcloud

Run the `gcloud app create` command:
    
    
    gcloud app create --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
    

Replace:

  * `SERVICE_ACCOUNT_NAME` with the name of the service account that you created.
  * `PROJECT_ID` with ID of the Google Cloud project in which you want to assign the service account.



### Console

  1. Go to the App Engine page:

[Go to App Engine](https://console.cloud.google.com/projectselector/appengine/create?st=true)

  2. Create a Google Cloud project.

  3. In the **Create App** section, select a service account from **Identity and API access**.




### Update the app-level default service account for your app

To update the app-level default service account for your application, you can use one of the following to assign a new service account:

**Important:** Only versions deployed after the update will use the new app-level default service account. All previously deployed versions will not use the new app-level default service account until you re-deploy that version.

### gcloud

Run the `gcloud app update` command.
    
    
        gcloud app update --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
    
    

Replace:

  * `SERVICE_ACCOUNT_NAME` with the name of the service account that you created.
  * `PROJECT_ID` with ID of the Google Cloud project in which you want to assign the service account.



Each new version that you deploy hereafter uses the new app-level default service account unless you explicitly assign a version-specific service account.

### Console

  1. Go to the App Engine **Application Settings** tab in the console and click **Edit Application Settings**.

[Go to Application Settings](https://console.cloud.google.com/appengine/settings)

  2. Choose an app-level default service account from **Select a Service account** and click **Save**.

You will be redirected to the **Application Settings** tab where you can view the email address of your updated app-level default service account. Example: `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.

Each new version that you deploy hereafter uses the new app-level default service account unless you explicitly assign a version-specific service account.




## Deploy with a version-specific service account

You can set a version-specific service account only during the deployment of new versions. Using a version-specific service account lets you grant different privileges to each application version, based on the specific tasks it performs, and avoid granting more privileges than necessary.

You must have an [existing](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) service account before deploying your application. Your version-specific service account must be in the same project where you deploy your application.

**Note:** If a version-specific service account is specified in both the `app.yaml` file and in the `gcloud` CLI, the `gcloud` setting takes precedence.

After May 15, 2024, Artifact Registry hosts images for the `gcr.io` domain in Google Cloud projects without previous Container Registry usage. If you deploy an existing application in a new project created after this date, the service account might not have the required permissions to deploy the app. To grant the required permissions, see [Deploying to App Engine](https://docs.cloud.google.com/artifact-registry/docs/integrate-app-engine#permissions).

### Set a version-specific service account

### gcloud

Run the `gcloud app deploy` command:
    
    
      gcloud app deploy --service-account=SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
    
    

Replace:

  * `SERVICE_ACCOUNT_NAME` with the name of the service account that you created.
  * `PROJECT_ID` with ID of the Google Cloud project in which you want to assign the service account. Your version-specific service account must be in the same project where you deploy your application.



### app.yaml

In your [`app.yaml`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml) file, specify your service account by adding the [`service_account`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#service-account) element:
    
    
    service_account: SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com
    

Replace:

  * `SERVICE_ACCOUNT_NAME` with the name of the service account that you created.
  * `PROJECT_ID` with ID of the Google Cloud project in which you want to assign the service account. Your version-specific service account must be in the same project where you deploy your application.



### appengine-web.xml

If you use the Java runtimes and include the App Engine legacy bundled services, specify your service account by adding the [`<service-account>`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml#service-account) element in your [`appengine-web.xml`](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/config/appref-xml) file:
    
    
    <service-account>SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com</service-account>
    

Replace:

  * `SERVICE_ACCOUNT_NAME` with the name of the service account that you created.
  * `PROJECT_ID` with ID of the Google Cloud project in which you want to assign the service account. Your version-specific service account must be in the same project where you deploy your application.



## App Engine default service account

The default App Engine service account is automatically created when you use App Engine.

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

To learn how to grant roles to service accounts and other principals, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).

After May 15, 2024, Artifact Registry hosts images for the `gcr.io` domain in Google Cloud projects without previous Container Registry usage. If you deploy an existing application in a new project created after this date, the service account might not have the required permissions to deploy the app. To grant the required permissions, see [Deploying to App Engine](https://docs.cloud.google.com/artifact-registry/docs/integrate-app-engine#permissions).

For modifying permissions, deleting, and restoring your service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
