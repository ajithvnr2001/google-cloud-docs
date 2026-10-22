---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-connector-authentication/
title: Authenticate connector repositories to upstream sources \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:21.734680+00:00
---

# Authenticate connector repositories to upstream sources  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/configure-connector-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Authenticate connector repositories to upstream sources Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Configuring upstream authentication for Artifact Registry connector repositories lets you connect to private external registries using your account credentials. You can store a personal access token in Secret Manager and attach it to your connector repository to authenticate requests to upstream sources.

To complete these steps, you need an Artifact Registry [connector repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-repo) and an account with the external source. For more information about connector repositories, see the [Connector repositories overview](https://docs.cloud.google.com/artifact-registry/docs/repositories/connector-overview).

## Required roles

To get the permissions that you need to configure authentication to upstream sources for connector repositories, ask your administrator to grant you the following IAM roles on the project: 

  * [Artifact Registry Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`)
  * [Secret Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## User-defined upstream sources

To configure authentication for user-defined upstream sources, complete the following steps.

### Save your access token in a secret

  1. Create an access token in the private registry.
  2. [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets) in Secret Manager.
  3. Save your personal access token as a [secret version](https://docs.cloud.google.com/secret-manager/docs/add-secret-version).



### Grant the Artifact Registry service account access to your secret

The Artifact Registry service agent acts on behalf of Artifact Registry when interacting with Google Cloud services. To allow the service agent to use secrets stored in Secret Manager, you must grant the service agent permission to view your secret version.

The service agent identifier is:

`service-PROJECT-NUMBER@gcp-sa-artifactregistry.iam.gserviceaccount.com`

PROJECT-NUMBER is the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Artifact Registry is running.

To grant the Artifact Registry service agent the **Secret Manager Secret Accessor** role:

### Console

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to the Secret Manager page](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the checkbox next to the name of the secret.

  3. If it is not already open, click **Show Info Panel** to open the panel.

  4. In the info panel, click **Add Principal**.

  5. In the **New principals** text area, enter the email address(es) of the members to add.

  6. In the **Select a role** dropdown, choose **Secret Manager** and then **Secret Manager Secret Accessor**.




### gcloud
    
    
    $ gcloud secrets add-iam-policy-binding secret-id \
        --member="member" \
        --role="roles/secretmanager.secretAccessor"
    

Where member is an [IAM member](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity), such as a user, group, or service account.

### API

Note: Unlike the other examples, this replaces the entire IAM policy.
    
    
    $ curl "https://secretmanager.googleapis.com/v1/projects/project-id/secrets/secret-id:setIamPolicy" \
        --request "POST" \
        --header "authorization: Bearer $(gcloud auth print-access-token)" \
        --header "content-type: application/json" \
        --data "{\"policy\": {\"bindings\": [{\"members\": [\"member\"], \"role\": \"roles/secretmanager.secretAccessor\"}]}}"
    

For more information on granting or revoking access to secrets, see [Manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).

### Add upstream credentials to your connector repository

To update your connector repository with your upstream source credentials:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the repository and click **Edit Repository**.

  3. In the **Connector repository authentication mode** section, update or add your upstream source username and the secret containing your access token.




###  gcloud CLI 

To update your connector repository with your upstream source credentials, run the following command:
    
    
    gcloud artifacts repositories update REPOSITORY \
        --project=PROJECT_ID \
        --location=LOCATION \
        --remote-username=USERNAME \
        --remote-password-secret-version=projects/SECRET_PROJECT_ID/secrets/SECRET_ID/versions/SECRET_VERSION
    

Replace the following:

  * `REPOSITORY`: the name of your Artifact Registry connector repository.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
  * `USERNAME`: your upstream source username.
  * `SECRET_PROJECT_ID`: the project ID of the project in which you created your secret.
  * `SECRET_ID`: the name you gave your secret.
  * `SECRET_VERSION`: the secret version you saved your access token in.



Your credentials are used the next time the connector repository sends a request for an artifact from the upstream source.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
