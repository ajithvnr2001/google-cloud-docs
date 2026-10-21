---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/function-identity/
title: Function identity (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:41.229748+00:00
---

# Function identity (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/function-identity/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Function identity (1st gen)

For security most interactions between entities in Google Cloud require that each entity have a verifiable identity, secured by some kind of secret, like a password or a key. Just as other entities need an identity to access Cloud Run functions, functions themselves often need access to other resources in Google Cloud to do their work. Every function is associated with a service account that serves as its identity when the function accesses other resources. The service account a function uses as its identity is also known as its _runtime service account_.

For production use, Google recommends that you give each function a dedicated identity by assigning it a user-managed service account. User-managed service accounts allow you to control access by granting a minimal set of permissions [using Identity and Access Management](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

## Runtime service account

Unless you specify a different runtime service account when deploying a function, Cloud Run functions uses a default service account as its identity for function execution:

  * Cloud Run functions uses the [App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/python/service-account), `PROJECT_ID@appspot.gserviceaccount.com`.

Note that the project number is distinct from the project ID and project name. You can find your project number on the Google Cloud console [Dashboard page](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).




These default service accounts have the **Editor** role, which allows them broad access to many Google Cloud services. While this is the fastest way to develop functions, Google recommends using the default service account for testing and development only. For production, you should grant the runtime service account only the [minimum set of permissions required to achieve its goal](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges).

To secure your functions in production:

  * Change permissions on the default runtime service account, or
  * Create individual service accounts for your functions



### Changing permissions on the default runtime service account

**Warning:** Changing permissions on the App Engine default service account or default compute service account affects _all_ resources linked to those service accounts, potentially including other Cloud Run functions, App Engine services, and Compute Engine resources.

### Console

  1. Go to the IAM page in the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/iam-admin/iam)

  2. Select the _App Engine default service account_ or _Default compute service account_ from the table.

  3. Click the pencil icon on the right side of the row to show the **Edit permissions** tab.

  4. Add or remove roles in the **Role** dropdown to provide least privilege access.

  5. Click **Save**.




### gcloud

Remove the **Editor** role, then use the `gcloud projects add-iam-policy-binding` command to add a new role:
    
    
    # Remove the Editor role
    gcloud projects remove-iam-policy-binding PROJECT_ID \
    --member="SERVICE_ACCOUNT_EMAIL" \
    --role="roles/editor"
    
    # Add the desired role
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member="SERVICE_ACCOUNT_EMAIL" \
    --role="ROLE"

Where `PROJECT_ID` is the project ID of the project you're using, `SERVICE_ACCOUNT_EMAIL` is the email address of the default runtime service account as shown earlier in Runtime service account, and `ROLE` is the new role to assign to the default runtime service account.

### Using individual service accounts for your functions

To give you greater flexibility in controlling access for your functions, you can give them each their own user-managed service account.

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) your service account. Make a note of its name.
  2. [Grant it](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) the [appropriate roles](https://docs.cloud.google.com/iam/docs/roles-permissions), based on what resources the function needs to access to do its work.
  3. If the service account and the function are in **different projects** , from the project where the service account is located:

     1. [Configure the service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-different-project) to work across projects.
     2. Grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to the Cloud Run functions Service Agent (`service-PROJECT_NUMBER@gcf-admin-robot.iam.gserviceaccount.com`), where `PROJECT` refers to the project in which the function resides. Cloud Run functions Service Agent manages cross-project access for your service account.

     3. Grant the `iam.serviceaccounts.actAs` permission to the Cloud Run functions service agent on the service account from the different project.

  4. Grant the service account access to the resource. The method for doing this depends on the resource type.

  5. Connect the service account with your function. You can do this either at deployment time or by updating a previously deployed function.


**Note:** In order to deploy a function with a user-managed service account, the deployer must have the `iam.serviceAccounts.actAs` permission on the service account being deployed. If you created the service account, you are automatically granted this permission. If not, someone who has the correct permissions must grant you this permission on the service account.

#### Adding a user-managed service account at deployment

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/add)

  2. Specify and configure the function however you would like.

  3. Click **Runtime, build...** to display additional settings.

  4. Select the **Runtime** tab.

  5. Click the **Service account** dropdown and select the desired service account.

  6. Click **Next** and **Deploy**.




### gcloud

When deploying a function using `gcloud functions deploy`, add the `--service-account` flag. For example:
    
    
    gcloud functions deploy --no-gen2 FUNCTION_NAME --service-account SERVICE_ACCOUNT_EMAIL

where `FUNCTION_NAME` is your function name, and `SERVICE_ACCOUNT_EMAIL` is the service account email.

#### Updating the service account of an existing function

You can update the runtime service account of an existing function.

### Console

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/functions/list)

  2. Click the name of the desired function to go to its detail page.

  3. Click the **Edit** pencil at the top of the detail page to edit the function.

  4. Click **Runtime, build...** to display additional settings.

  5. Select the **Runtime** tab.

  6. Click the **Service account** dropdown and select the desired service account.

  7. Click **Next** and **Deploy**.




### gcloud

When deploying a function using `gcloud functions deploy`, add the `--service-account` flag:
    
    
    gcloud functions deploy FUNCTION_NAME --service-account SERVICE_ACCOUNT_EMAIL

where `FUNCTION_NAME` is your function name, and `SERVICE_ACCOUNT_EMAIL` is the service account.

The redeployed function now uses the new runtime service account.

## Using the Metadata Server to acquire tokens

While IAM-defined service accounts are the preferred method for managing access in Google Cloud, some services might require other modes, such as an [API key, OAuth 2.0 client, or service account key](https://docs.cloud.google.com/docs/authentication#strategies). Access to an external resource might also require alternate methods.

If your target service requires that you present an [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect) ID token or an [Oauth 2.0](https://developers.google.com/identity/protocols/oauth2/cross-client-identity) access token, you might be able to use the [Compute Metadata Server](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) to fetch these tokens rather than setting up a full OAuth client.

**Note:** You cannot query the metadata server directly from your local computer.

### Identity tokens

You can use the Compute Metadata Server to [fetch ID tokens](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity#request_signature) with a specific audience as follows:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=AUDIENCE" \
      -H "Metadata-Flavor: Google"

Where `AUDIENCE` is the requested target, for example: the URL of a service you're invoking, such as `https://service.domain.com`, or the OAuth Client ID of an IAP protected resource, such as `1234567890.apps.googleusercontent.com`.

### Access tokens

OAuth 2.0 access tokens use _scopes_ to define access permissions. By default, within Google Cloud access tokens have the `cloud-platform` scope. To access other Google or Google Cloud APIs, you must fetch an access token with the appropriate scope.

You can use the Compute Metadata Server to [fetch access tokens](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#applications).

If you need an access token with a specific scope, you can generate one as follows:
    
    
    curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token?scopes=SCOPES" \
      -H "Metadata-Flavor: Google"

Where `SCOPES` is a comma separated list of OAuth scopes requested, for example: `https://www.googleapis.com/auth/drive,https://www.googleapis.com/auth/spreadsheets`.

Consult the full list of [Google OAuth scopes](https://developers.google.com/identity/protocols/googlescopes) to find which scopes you need.

**Note:** the `?scopes=` query parameter is only available on App Engine and Cloud Run functions.

## Next steps

Learn how to [authorize access](https://docs.cloud.google.com/functions/1stgendocs/securing/managing-access-iam) to your functions or to authenticate [developers and other functions](https://docs.cloud.google.com/functions/1stgendocs/securing/authenticating) so that they can invoke your functions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
