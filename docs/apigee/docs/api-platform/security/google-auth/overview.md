---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview/
title: Using Google authentication \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:57.176041+00:00
---

# Using Google authentication  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/google-auth/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using Google authentication Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This topic explains how to set up and deploy an API proxy that is configured to use Google authentication. 

**Apigee hybrid users:** If you are using Apigee hybrid, note that this feature is only supported for Apigee hybrid v1.6.x and later versions.

##  Introduction 

Apigee supports using [Google OAuth tokens](https://developers.google.com/identity/protocols/oauth2) or [OpenID Connect tokens](https://developers.google.com/identity/protocols/oauth2/openid-connect) to authenticate with Google services such as [Cloud Logging](https://cloud.google.com/logging) and [Secret Manager](https://cloud.google.com/secret-manager), and custom services running on certain Google Cloud products such as [Cloud Functions](https://cloud.google.com/functions) and [Cloud Run](https://cloud.google.com/run). 

To use this feature, you must configure the `<Authentication>` XML element in one of the following contexts: 

  * AssignMessage policies
  * ServiceCallout policies
  * ExternalCallout policies
  * TargetEndpoint configurations



After you complete some basic setup steps (as described in this topic), Apigee performs the token generation and makes secure calls to targeted Google services or custom hosted services for you, without the need to manually set authentication headers or otherwise modify a service request. From the perspective of an API developer, the process of calling Google services from within a properly configured API proxy is handled seamlessly. 

##  API proxy configuration options 

This section explains where you can use the `<Authentication>` XML element to enable Google OAuth Token or OpenID Connect authentication: 

Configuration option | Description  
---|---  
AssignMessage policy | The [ AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) allows you to add the headers required for Google authentication and token injection. For usage details and examples, see [ AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy).  
ServiceCallout policy | The [ ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) lets you call other internal or external services from an API proxy. For example, ServiceCallout can call external Google services or custom hosted services. For usage details and examples, see [ ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy).  
ExternalCallout policy | The [ ExternalCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy) enables you to send [gRPC](https://grpc.io/) requests to your gRPC server to implement custom behavior that isn't supported by Apigee policies. For usage details and examples, see [ ExternalCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy).  
TargetEndpoint | Specify a Google service or custom hosted service as an API proxy target endpoint. For usage details and examples, see [API Proxy configuration reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference).  
  
##  Google Auth Token supported contexts 

The `<Authentication>` element has two sub-element configurations: `<GoogleAccessToken>` or `<GoogleIDToken>`. The following table shows the contexts in which these elements are supported: 

Used in | GoogleAccessToken | GoogleIDToken  
---|---|---  
[ AssignMessage policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) | Supported | Supported  
[ ServiceCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy) | Supported | Supported  
[ ExternalCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy) | Not supported | Supported  
[TargetEndpoint](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#authentication-element-usage) | Supported | Supported  
**Note:** The ExternalCallout policy cannot call Google APIs, so Google access tokens are not supported by the policy. However, OpenID Connect tokens are supported, so if the target service is hosted in, for example, Cloud Run, the policy can seamlessly connect to it. **Caution:** Avoid using non-SSL dynamic targets. For example, avoid overriding the [target.url](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#target) flow variable to point to a non-SSL target endpoint. If you use a non-SSL dynamic target, the Google Auth Token will still be generated; however, the authentication token will be exposed in plain text.

##  Deployment steps 

This section explains how to deploy an API proxy that uses Google authentication to call targeted Google services or custom hosted services. We explain the deployment steps for Apigee and Apigee hybrid separately. 

**Note:** [Shared flow deployments](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows) also support use of the `Authentication` tag in the supported policies and TargetEndpoint configuration. See also the [Shared flow deployment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.sharedflows.revisions.deployments/deploy) documentation. 

###  Deploy on Apigee 

The following steps explain how to deploy an API proxy on Apigee, where the proxy is configured to make authenticated calls to Google services or custom hosted services. The steps assume that you have already created the proxy, and that it includes an `<Authentication>` element in one of the listed supported contexts. 

  1. Create a Google service account in the same Google Cloud project where your Apigee organization was created. You can create the service account in the Google Cloud console or with the Google Cloud CLI. See [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts). 

You must provide this service account's name when you deploy an API proxy that is configured to use Google authentication, and the OAuth tokens that are generated will represent the service account.

  2. Give the user who will do the deployment (the deployer) the `iam.serviceAccounts.actAs` permission on the service account. See About service account permissions and [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access). **Caution:** Users granted the Service Account User role on a service account can use it to indirectly access all the resources to which the service account has access. For details, see [Service Account User role](https://cloud.google.com/iam/docs/service-account-permissions#user-role). We recommend configuring the service account for [least privilege](https://cloud.google.com/iam/docs/using-iam-securely#least_privilege) to minimize the impact of user role assignments.**Note:** This step may be optional if the deployer already has sufficient permission, for example, when deploying through the UI and the Google Cloud user has the Owner role on the project.
         
         gcloud iam service-accounts add-iam-policy-binding \
                 SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
                 --member="MEMBER" \
                 --role="roles/iam.serviceAccountUser"
         

With:

     * **SA_NAME** : The name that you provided when you created the service account.
     * **PROJECT_ID** : The project ID. The ID is the same as your organization name.
     * **MEMBER** : The member to add the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`.
  3. Ensure that the Apigee service account has the ability to impersonate the proxy service account. To provide this ability, grant the Apigee service account the `iam.serviceAccountTokenCreator` role on the proxy service account. See also About service account permissions. 

To configure your service account with this role using the gcloud CLI:
         
         gcloud iam service-accounts add-iam-policy-binding SERVICE_ACCOUNT_EMAIL \
                 --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com" \
                 --role="roles/iam.serviceAccountTokenCreator"

With:

     * **SERVICE_ACCOUNT_EMAIL** : The email for your service account.
     * **PROJECT_NUMBER** : Your Google Cloud project number.

See [ Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

  4. Give the service account permissions needed to talk to your targeted Google services. For example, if you want to call the Google Logging service, this service account must include the required permissions to talk to that service. See also [Understanding roles](https://cloud.google.com/iam/docs/understanding-roles).
  5. Before deploying an API proxy that is configured to use Google authentication, you need: 
     * The name of the service account you created previously. For example: `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`
     * As the user performing the deployment (the deployer), you must already have or be granted the `iam.serviceAccounts.actAs` permission on the service account, as noted in Step 2. 
  6. Deploy the API proxy containing the Google authentication configuration you implemented. You can use the Apigee UI or API to deploy the proxy. To learn more, see [Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new). 
     * If using the UI, you are asked to provide a service account name. Use the name of the **proxy** service account you created in Step 1. For example: `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`. 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/proxy-deploy-service-account.png)

     * When deploying the proxy using the [Apigee deployment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy), here's an example cURL command that you can use. Notice that the command includes a service account name as a query parameter. This is the name of the service account you created in Step 1: 
           
           curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG_NAME/environments/ENV_NAME/apis/apiproxy/revisions/2/deployments?serviceAccount=SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
           -H "Content-Type: application/json" -X POST

Where: 

       * `TOKEN`: An OAuth token that you must obtain in exchange for your Google credentials. For details, see [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).
       * `ORG_NAME`: Your Apigee organization name.
       * `ENV_NAME`: The name of the environment to deploy the API proxy to.
       * `SA_NAME`: The name that you provided when you created the service account.
       * `PROJECT_ID`: Your Google Cloud project ID (same as the organization name).
  7. When the deployment completes, test your API proxy to make sure the Google service returns the expected response.



###  Deploy on Apigee hybrid 

The following steps explain how to deploy to Apigee hybrid an API proxy that is configured to make authenticated calls to Google services. The steps assume that you have already created the proxy, and that it includes an `<Authentication>` element in one of the listed supported contexts. 

**Note:** Steps 1-3 below are required, but are one-time setup steps. 

Before you begin, we recommend confirming that all required APIs are enabled, as described in [Step 1: Enable APIs](https://docs.cloud.google.com/apigee/docs/hybrid/latest/precog-enableapi).

  1. Create a service account and key for the Apigee hybrid **runtime** component by using one of the following methods: **Note:** If you already created an `apigee-runtime` service account when you installed Apigee hybrid, then you can skip this step.
     * Use the `create-service-account` tool supplied with Apigee hybrid to create an `apigee-runtime` service account. The tool creates the service account and returns a service account key. See [create-service-account](https://docs.cloud.google.com/apigee/docs/hybrid/latest/create-service-account) for details.
     * Create the service account in the Google Cloud console or with the gcloud CLI. See [Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts). To fetch the service account key, see [Creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys).
**Note:** You can create the runtime service account in any Google Cloud project where you have permission to do so. It does not have to be created in the same project used for your Apigee organization.
  2. Open your `overrides.yaml` file and specify the path to the service account key file for each environment that requires Google authentication capability: 
         
         envs:
           - name: "ENVIRONMENT_NAME"
             serviceAccountPaths:
               runtime: "KEY_FILE_PATH"

**Note:** If you have multiple environments that require Google Authentication capability, each can have its own service account, or they can all share the same one. See also About service account permissions. 

For example:
         
         envs:
           - name: "test"
             serviceAccountPaths:
               runtime: "./service_accounts/my_runtime_sa.json"

  3. Apply the overrides file to your cluster using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference): 
         
         helm upgrade ENV_NAME apigee-env/ \
           --namespace APIGEE_NAMESPACE \
           --set env=ENV_NAME \
           --atomic \
           -f overrides.yaml

  4. Create a second service account, which we call the **proxy** service account. This service account must be in the same Google Cloud project you used to create your Apigee organization. You must provide this service account's email address when you deploy an API proxy that is configured to use Google authentication, and the OAuth tokens that are generated will represent the service account. 
  5. Give the user who will do the deployment (the deployer) the `iam.serviceAccounts.actAs` permission on the service account. See also About service account permissions. **Caution:** Users granted the Service Account User role on a service account can use it to indirectly access all the resources to which the service account has access. For details, see [Service Account User role](https://cloud.google.com/iam/docs/service-account-permissions#user-role). We recommend configuring the service account for [least privilege](https://cloud.google.com/iam/docs/using-iam-securely#least_privilege) to minimize the impact of user role assignments.**Note:** This step may be optional if the deployer already has sufficient permission, for example, when deploying through the UI and the Google Cloud user has the Owner role on the project.
         
         gcloud iam service-accounts add-iam-policy-binding \
         SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
         --member="MEMBER" \
           --role="roles/iam.serviceAccountUser"
         

Where:

     * **PROJECT_ID** : The project ID. The ID is the same as your organization name. 
     * **SA_NAME** : The name you provided when you created the service account. 
     * **MEMBER** : The member to add the binding for. Should be of the form `user|group|serviceAccount:email` or `domain:domain`.
  6. Give the **proxy** service account permissions needed to talk to your targeted Google services. For example, if you want to call the Google Logging service, this service account must include the required permissions to talk to that service. See also [Understanding roles](https://cloud.google.com/iam/docs/understanding-roles).
  7. Ensure that the runtime has the ability to impersonate the proxy service account. To provide this ability, grant the **runtime** service account the `iam.serviceAccountTokenCreator` role on the proxy service account. See also About service account permissions. For example: 
         
         gcloud iam service-accounts add-iam-policy-binding \
         PROXY_SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
         --member=serviceAccount:RUNTIME_SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
         --role=roles/iam.serviceAccountTokenCreator
         

Where:

     * **PROJECT_ID** : The project ID. The ID is the same as your organization name. Note that you did not have to use the project associated with your organization to create the runtime service account. Just be sure you use the correct project IDs in this command.
     * **PROXY_SA_NAME** : The ID for the **proxy** service account.
     * **RUNTIME_SA_NAME** : The ID for the **runtime** service account.
  8. Before deploying an API proxy that is configured to use Google authentication, you need: 
     * The name of the **proxy** service account you created previously. For example: `PROXY_SA_NAME@PROJECT_ID.iam.gserviceaccount.com`
     * As the user performing the deployment, you must already have or be granted the `iam.serviceAccounts.actAs` permission in the Google Cloud project where the Apigee organization is provisioned. See [ Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access). 
  9. Deploy the API proxy containing the Google authentication configuration you implemented. You can use the Apigee UI or API to deploy the proxy. To learn more, see [Deploying an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-new). 
     * If using the UI, you are asked to provide a service account name. Use the name of the **proxy** service account you created previously. For example: `PROXY_SA_NAME@PROJECT_ID.iam.gserviceaccount.com`. 

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/proxy-deploy-service-account.png)

     * If you prefer to deploy the proxy using the [Apigee deployment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.deployments/deploy), here's an example cURL command that you can use. Notice that the command includes a service account name as a query parameter. This is the name of the **proxy** service account: 
           
           curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/ORG_NAME/environments/ENV_NAME/apis/apiproxy/revisions/2/deployments?serviceAccount=PROXY_SA_NAME@PROJECT_ID.iam.gserviceaccount.com" \
           -H "Content-Type: application/json" -X POST

Where: 

       * `TOKEN`: An OAuth token that you must obtain in exchange for your Google credentials. For details, see [Obtaining an OAuth 2.0 access token](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/api-get-started#oauth20).
       * `ORG_NAME`: Your Apigee organization name.
       * `ENV_NAME`: The name of the environment to deploy the API proxy to.
       * `PROXY_SA_NAME`: The name of the **proxy** service account.
       * `PROJECT_ID`: Your Google Cloud project ID (same as the organization name).
  10. When the deployment completes, test your API proxy to make sure the Google service returns the expected response.



## About service account permissions

To configure an API proxy to use Google authentication, you must create a service account as described in the following table. See also [ Creating and managing service accounts](https://cloud.google.com/iam/docs/creating-managing-service-accounts). 

Service account | Required for | Description  
---|---|---  
Proxy | Apigee and Apigee hybrid | Has permissions needed for an API proxy to make authenticated calls to targeted Google services.

  * Must be created in the same Google Cloud project as your Apigee organization.
  * The user performing the deployment (the deployer), must have or be granted the `iam.serviceAccounts.actAs` permission on the proxy service account.
  * Must include permissions needed to talk to specific target Google services. For example, if you want to call the Google Logging service, this service account must include the required permissions to talk to that service. See also [Understanding roles](https://cloud.google.com/iam/docs/understanding-roles).
  * The name of the service account must be provided when you deploy the proxy that uses Google authentication.

  
Runtime | Apigee hybrid only | Allows the Apigee runtime to generate tokens to authenticate on Google services requested by an API proxy. This service account "impersonates" the proxy-specific service account to make authenticated calls on its behalf.

  * To be able to impersonate the **proxy** service account and create tokens, the **runtime** service account must be granted the role `roles/iam.serviceAccountTokenCreator` on the **proxy** service account. See [Manage access to service accounts](https://cloud.google.com/iam/docs/manage-access-service-accounts).

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
