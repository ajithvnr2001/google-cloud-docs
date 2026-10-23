---
url: https://docs.cloud.google.com/iap/docs/deprecations/migrate-oauth-client/
title: Migrate from the IAP OAuth Admin API \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:19.331525+00:00
---

# Migrate from the IAP OAuth Admin API  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/deprecations/migrate-oauth-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Resources ](https://docs.cloud.google.com/iap/docs/resources)



Send feedback 

#  Migrate from the IAP OAuth Admin API Stay organized with collections  Save and categorize content based on your preferences. 

The Identity-Aware Proxy (IAP) OAuth Admin API is now deprecated. This guide shows how you can optionally migrate existing OAuth clients to Google-managed OAuth clients. If you don't use the IAP OAuth Admin API, this change doesn't impact you.

To check if your project uses OAuth Admin APIs, see Check for OAuth Admin APIs usage. If your project is using OAuth Admin APIs, you must follow the migration instructions in this document, or you can use alternatives to the OAuth Admin API.

## What is changing

We are deprecating the IAP OAuth Admin API, which includes the following APIs and gcloud CLI command groups for manual OAuth client and brand management:

  * [OAuth Client APIs](https://docs.cloud.google.com/iap/docs/reference/rest#rest-resource:-v1.projects.brands.identityawareproxyclients)
  * [Brands APIs](https://docs.cloud.google.com/iap/docs/reference/rest#rest-resource:-v1.projects.brands)
  * [`gcloud iap oauth-brands`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-brands) (`create`, `describe`, and `list`), including the [`alpha`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/oauth-brands) and [`beta`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/oauth-brands) release tracks
  * [`gcloud iap oauth-clients`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/oauth-clients) (`create`, `delete`, `describe`, `list`, and `reset-secret`), including the [`alpha`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/iap/oauth-clients) and [`beta`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iap/oauth-clients) release tracks



You can no longer create or manage custom OAuth clients using the IAP OAuth Admin API. Instead of manually managing OAuth 2.0 clients, IAP uses a Google-managed OAuth client. This simplifies OAuth client management, reduces manual errors, and streamlines your deployment processes.

To continue to provide custom branding, we recommend that you [configure custom OAuth clients](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

## What is not changing

If you don't use the IAP OAuth Admin API, this change does not impact you.

This deprecation doesn't affect OAuth clients that you manually configure using the Compute Engine API, App Engine API, or Google Cloud console. It also doesn't affect other IAP APIs or gcloud CLI command groups (including their `alpha` and `beta` release tracks) that manage IAP access policies, settings, or TCP forwarding—such as [`gcloud iap web`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/web) (for example, `get-iam-policy` and `remove-iam-policy-binding`), [`gcloud iap settings`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings), and [`gcloud iap tcp`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/tcp)—because those commands use the `IdentityAwareProxyAdminService` API rather than the deprecated `IdentityAwareProxyOAuthService` API.

You can continue to create new OAuth brand and client configurations and manage them using the Google Cloud console. You are not required to migrate your existing OAuth clients; you can continue to use and manage them through the Google Cloud console instead of the IAP OAuth Admin API.

## Check for IAP OAuth Admin APIs usage

To check if your project is using IAP OAuth Admin APIs, do the following:

  1. In the Google Cloud console, go to the **IAP API Usage** page.

[Go to IAP API Usage](https://console.cloud.google.com/apis/api/iap.googleapis.com)

  2. Select the project that you want to check for IAP OAuth Admin API usage.

  3. In the **Select Graphs** list, select **Traffic by API method** , and then click **OK**.

  4. In the **Methods** section, look for any methods with the prefix `google.cloud.iap.v1.IdentityAwareProxyOAuthService`, which indicates that the project uses the IAP OAuth Admin API.




## Detailed description

As of January 22, 2025, the IAP OAuth 2.0 Admin API, which is used to create an IAP OAuth 2.0 client, is [deprecated](https://docs.cloud.google.com/iap/docs/deprecations). IAP now uses a Google-managed OAuth client for browser access by default or when no OAuth 2.0 client is configured explicitly. The Google-managed OAuth 2.0 client restricts access to IAP-enabled applications to users within the same organization when they access those applications through a browser.

With the deprecation of the Identity-Aware Proxy (IAP) OAuth 2.0 Admin API, you can no longer use this API to create or manage OAuth clients. OAuth clients created before this deprecation won't be invalidated. You can continue to use OAuth clients that you previously created and manage those clients using the Google Cloud console.

If you have applications configured with OAuth clients created using the IAP 2.0 Admin API or otherwise, those applications will continue to work. No changes are required to the applications. However, if your automation scripts or Infrastructure as Code (IaC) tools use the IAP OAuth 2.0 Admin API to configure new clients or fetch client secrets for existing clients, you must update the scripts so that they don't use the IAP OAuth 2.0 Admin API.

Whether you continue using your existing user-managed client or consider switching to the Google-managed option depends on your requirements for branding and external access. For a detailed breakdown of all functional differences, see [Google-managed and custom OAuth client comparison table](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#compare-google-managed-oauth-clients-and-custom-oauth-clients). If your application requires a custom Client ID for branding or external access, use the Google Cloud console to create the Client ID. For more information about custom OAuth clients, see [Customize an OAuth configuration to enable IAP](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

To learn how to configure Google-managed OAuth 2.0 clients for your applications, see [Programmatic access](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients#programmatic-access).

If you have a requirement that isn't met by the Google-managed OAuth 2.0 client, you can [share a single OAuth client with multiple IAP applications](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients), eliminating the need to manually create a client for every new application.

## Required actions

  * **Update automation scripts**

If you use Terraform, the gcloud CLI (`gcloud iap oauth-brands` or `gcloud iap oauth-clients`, including `alpha` and `beta`), or other tools to automate the configuration of IAP, and you use the IAP OAuth 2.0 Admin API, you must update the automation scripts to use a pre-created client or use the Google-managed OAuth client with IAP.

  * **Configure programmatic access for applications using the Google-Managed OAuth 2.0 clients**

If you already have some applications that are protected by IAP and you plan to migrate them using the Google-Managed OAuth 2.0 client, you can configure programmatic access for these applications by [allowlisting OAuth 2.0 clients](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating-with-an-oidc-token).




## Migrate IAP-enabled resources

To migrate your resources to use the Google-managed OAuth 2.0 client, follow the steps for the type of resource, such as a Compute Engine resource, that you want to migrate.

### Migrate IAP-enabled App Engine resources

Complete the steps in this section to migrate App Engine resources where IAP is enabled and an OAuth 2.0 client is configured.

### gcloud

Before you continue to the steps, ensure that you have an up-to-date version of the gcloud CLI. For instructions on how to install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads).

  1. Use the Google Cloud CLI to authenticate.
         
         gcloud auth login
         

  2. Click the URL that appears and sign in.

  3. After you sign in, copy the verification code that appears and paste it in the command line.

  4. Run the following command to specify the project that contains the applications that you want to continue to protect with IAP.
         
         gcloud config set project PROJECT_ID
         

  5. Run the following command to fetch the configured OAuth 2.0 client ID.
         
         gcloud app describe --format="value(iap.oauth2ClientId)"
         

Save the client ID from the previous command if you want to allow programmatic access.

  6. To allowlist the OAuth 2.0 client for programmatic access, perform a read-update-write operation on the IAP settings API.
         
         gcloud iap settings get --resource-type=app-engine --project=$PROJECT > settings.yaml
         

  7. Update the `settings.yaml` file and add the previously fetched OAuth 2.0 client ID under `programmaticClients` as shown in the following example.
         
         accessSettings:
           oauthSettings:
             programmaticClients:
             - CLIENT_ID
         

  8. Apply the new settings on the App Engine application
         
         gcloud iap settings set settings.yaml --resource-type=app-engine --project=PROJECT_ID
         

  9. To migrate your apps, run the following command.
         
         gcloud iap web enable --resource-type=app-engine
         




### API

  1. Run the following command to fetch the configured OAuth 2.0 Client ID.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         "https://appengine.googleapis.com/v1/apps/PROJECT_ID?fields=iap"
         

  2. Run the following command to fetch existing IAP settings into a `settings.json` file.
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/appengine-PROJECT_ID:iapSettings" > settings.json
         

  3. Update the `settings.json` file to add previously saved CLIENT_ID as a programmatic client.
         
         {
             "accessSettings": {
               "oauthSettings": {
                 "programmaticClients": [
                   "CLIENT_ID"
                 ]
               },
             },
         }
         

  4. Run the following command to update IAP settings.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d "@settings.json" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/appengine-PROJECT_ID:iapSettings"
         

  5. Run the following command to prepare a `settings.json` file.
         
         cat << EOF > settings.json
           {
           "iap":
               {
                 "enabled":true
               }
           }
           EOF
         

  6. Run the following command to migrate your apps.
         
         curl -X PATCH \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           -H "Content-Type: application/json" \
           -d @settings.json \
           "https://appengine.googleapis.com/v1/apps/PROJECT_ID?updateMask=iap"
         




### Migrate IAP-enabled Compute Engine resources

Complete the steps in this section to migrate Compute Engine resources where IAP is enabled and an OAuth 2.0 client is configured.

### gcloud

Before you continue to the steps, ensure that you have an up-to-date version of the gcloud CLI. For instructions on how to install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads).

  1. Use the Google Cloud CLI to authenticate.
         
         gcloud auth login
         

  2. Click the URL that appears and sign in.

  3. After you sign in, copy the verification code that appears and paste it in the command line.

  4. Run the following command to specify the project that contains the applications that you want to continue to protect with IAP.
         
         gcloud config set project PROJECT_ID
         

  5. Run the following command to fetch the configured OAuth 2.0 client ID.

### Global scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
         --global \
         --format="value(iap.oauth2ClientId)"
         

### Regional scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
         --region REGION_NAME \
         --format="value(iap.oauth2ClientId)"
         

Save the client ID from the previous command if you want to allow programmatic access.

  6. To give OAuth 2.0 client programmatic access, perform a read-update-write operation on the IAP settings API.

### Global scope
         
         gcloud iap settings get \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME > settings.yaml
         

### Regional scope
         
         gcloud iap settings get \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME \
             --region=REGION_NAME > settings.yaml
         

  7. Update the `settings.yaml` file and add the previously fetched OAuth 2.0 client ID under `programmaticClients` as shown in the following example:
         
         accessSettings:
           oauthSettings:
             programmaticClients:
             - CLIENT_ID
         

  8. Apply the new settings on the Compute Engine application:

### Global scope
         
         gcloud iap settings set settings.yaml \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME

### Regional scope
         
         gcloud iap settings set settings.yaml \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME \
             --region=REGION_NAME

  9. To migrate your applications, run the following command. To clear the OAuth client ID and OAuth secret, pass a quoted single space (`" "`) in the command. The backend service uses the Google-managed OAuth client.

### Global scope
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --global \
             --iap=enabled,oauth2-client-id=" ",oauth2-client-secret=" "
         

### Regional scope
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --region REGION_NAME \
             --iap=enabled,oauth2-client-id=" ",oauth2-client-secret=" "
         

  10. To confirm that you have removed the OAuth client ID and OAuth client secret and that backend service is using a Google-managed OAuth client, run [gcloud compute backend-services describe](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/describe). To clear these fields during migration, the `gcloud compute backend-services update` command uses a single space (`" "`), which the Compute Engine API interprets as an instruction to remove the `oauth2ClientId` and `oauth2ClientSecret` values.

### Global scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
             --global
         

### Regional scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
             --region REGION_NAME
         

After you run the `describe` command, examine the `iap` section of the output. A successful migration is indicated when the `oauth2ClientId` field shows a single space (`' '`), and the `oauth2ClientSecret` field contains the SHA256 hash (`36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068`) of a single space.




### API

  1. Run the following command to fetch the configured OAuth 2.0 Client ID.

### Global scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME?fields=iap.oauth2ClientId"
         

### Regional scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/backendServices/BACKEND_SERVICE_NAME?fields=iap.oauth2ClientId"
         

  2. Run the following command to fetch existing IAP settings into a `settings.json` file.

### Global scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute/services/BACKEND_SERVICE_NAME:iapSettings" > settings.json
         

### Regional scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute-REGION_NAME/services/BACKEND_SERVICE_NAME:iapSettings" > settings.json
         

  3. Update the `settings.json` file to add previously saved CLIENT_ID as a programmatic client.
         
         {
             "accessSettings": {
               "oauthSettings": {
                 "programmaticClients": [
                   "CLIENT_ID"
                 ]
               },
             },
         }
         

  4. Run the following command to update IAP settings.

### Global scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d "@settings.json" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute/services/BACKEND_SERVICE_NAME:iapSettings"
         

### Regional scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d "@settings.json" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute-REGION_NAME/services/BACKEND_SERVICE_NAME:iapSettings"
         

  5. Run the following command to prepare a `settings.json` file.
         
         cat << EOF > settings.json
         {
         "iap":
               {
                 "enabled":true,
                 "oauth2ClientId": " ",
                 "oauth2ClientSecret": " "
               }
         }
         EOF
         

  6. Run the following command to migrate your IAP resources.

### Global scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME"
         

### Regional scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/backendServices/BACKEND_SERVICE_NAME"
         

  7. To confirm that the OAuth client ID is not set, run the following global or regional scope command. After running the command, check the output to ensure that the OAuth client ID field is empty.

### Global scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME"
         

### Regional scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/backendServices/BACKEND_SERVICE_NAME"
         




### Terraform

If you are migrating existing IAP-enabled resources to use a Google-managed OAuth client, you must explicitly unset the `oauth2_client_id` and `oauth2_client_secret` fields. To unset the fields updating the values to a single whitespace character, as shown in the following example:
    
    
    resource "google_compute_backend_service" "default" {
      name                  = "tf-test-backend-service-external"
      protocol              = "HTTP"
      load_balancing_scheme = "EXTERNAL"
      iap {
        oauth2_client_id     = " "
        oauth2_client_secret = " "
      }
    }
    

The `oauth2_client_id` and `oauth2_client_secret` fields are optional, and if you are working with new IAP-enabled resources, you can ignore them.

For more information about using Terraform with Google Cloud, refer to the [Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_service#example-usage---backend-service-external-iap).

### Migrate IAP-enabled Cloud Run resources

Complete the steps in this section to migrate Cloud Run resources where IAP is enabled and an OAuth 2.0 client is configured.

### gcloud

Before continuing to the steps, ensure that you have an up-to-date version of the gcloud CLI. For instructions on how to install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads).

  1. To authenticate, use the Google Cloud CLI and run the following command.
         
         gcloud auth login
         

  2. Click the URL that appears and sign in.

  3. After you sign in, copy the verification code that appears and paste it in the command line.

  4. Run the following command to specify the project that contains the applications that you want to continue to protect with IAP.
         
         gcloud config set project PROJECT_ID
         

  5. Run the following command to fetch the configured OAuth 2.0 client ID.

### Global scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
             --global \
             --format="value(iap.oauth2ClientId)"
         

### Regional scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
           --region REGION_NAME \
           --format="value(iap.oauth2ClientId)"
         

Save the client ID from the previous command if you want to allow programmatic access.

  6. To allowlist OAuth 2.0 client for programmatic access, perform a read-update-write operation on IAP settings API.

### Global scope
         
         gcloud iap settings get \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME > settings.yaml
         

### Regional scope
         
         gcloud iap settings get \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME \
             --region=REGION_NAME > settings.yaml
         

  7. Update the `settings.yaml` file and add the previously fetched OAuth 2.0 client ID under `programmaticClients` as the example shown.
         
         accessSettings:
           oauthSettings:
             programmaticClients:
             - CLIENT_ID
         

  8. Apply the new settings on the Compute Engine application.

### Global scope
         
         gcloud iap settings set settings.yaml \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME
         

### Regional scope
         
         gcloud iap settings set settings.yaml \
             --resource-type=compute \
             --project=PROJECT_ID \
             --service=BACKEND_SERVICE_NAME \
             --region=REGION_NAME
         

  9. To migrate your resources, run either the globally or regionally scoped command.

### Global scope
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --global \
             --iap=enabled,oauth2-client-id=" ",oauth2-client-secret=" "
         

### Regional scope
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --region REGION_NAME \
             --iap=enabled,oauth2-client-id=" ",oauth2-client-secret=" "
         

  10. To confirm that the OAuth client ID is not set, run the following global or regional scope command. After running the command, check the output to ensure that the OAuth client ID field is empty.

### Global scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
             --global
         

### Regional scope
         
         gcloud compute backend-services describe BACKEND_SERVICE_NAME \
             --region REGION_NAME
         




### API

  1. Run the following command to fetch the configured OAuth 2.0 Client ID.

### Global scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME?fields=iap.oauth2ClientId"
         

### Regional scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/backendServices/BACKEND_SERVICE_NAME?fields=iap.oauth2ClientId"
         

  2. Run the following command to fetch existing IAP settings into a `settings.json` file.

### Global scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute/services/BACKEND_SERVICE_NAME:iapSettings" > settings.json
         

### Regional scope
         
         curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute-REGION_NAME/services/BACKEND_SERVICE_NAME:iapSettings" > settings.json
         

  3. Update the `settings.json` file to add previously saved CLIENT_ID as a programmatic client.
         
         {
             "accessSettings": {
               "oauthSettings": {
                 "programmaticClients": [
                   "CLIENT_ID"
                 ]
               },
             },
         }
         

  4. Run the following command to update IAP settings.

### Global scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d "@settings.json" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute/services/BACKEND_SERVICE_NAME:iapSettings"
         

### Regional scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d "@settings.json" \
         "https://iap.googleapis.com/v1/projects/PROJECT_ID/iap_web/compute-REGION_NAME/services/BACKEND_SERVICE_NAME:iapSettings"
         

  5. Run the following command to prepare a `settings.json` file.
         
         cat << EOF > settings.json
         {
         "iap":
               {
                 "enabled":true,
                 "oauth2ClientId": " ",
                 "oauth2ClientSecret": " "
               }
         }
         EOF
         

  6. Run the following command to migrate your resources.

### Global scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME"
         

### Regional scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/backendServices/BACKEND_SERVICE_NAME"
         

  7. To confirm that the OAuth client ID is not set, run the following global or regional scope command. After running the command, check the output to ensure that the OAuth client ID field is empty.

### Global scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_NAME"
         

### Regional scope
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_NAME/backendServices/BACKEND_SERVICE_NAME"
         




### Migrate IAP-enabled Google Kubernetes Engine resources

Add the following IAP block to the [BackendConfig](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto#kubernetes-configure) Custom Resource Definition (CRD). This enables IAP with the Google-managed OAuth 2.0 client.
    
    
    apiVersion: cloud.google.com/v1
    kind: BackendConfig
    metadata:
      name: config-default
      namespace: my-namespace
    spec:
      iap:
        enabled: true
    

## Use a service account JWT to authenticate to IAP

You can authenticate to IAP without having to use the deprecated OAuth Admin API by using a [service account JWT](https://docs.cloud.google.com/iap/docs/authentication-howto#service-account-jwt-auth).

## Get an OAuth client secret

When you create a custom OAuth client in the Google Cloud console, the client secret is displayed only at that time. You're responsible for securely storing this secret. Secret Manager is the recommended service to securely store OAuth client secrets.

If you use Secret Manager to store your OAuth client secret, see [Access a secret version](https://docs.cloud.google.com/secret-manager/docs/access-secret-version) for instructions on how to get the client secret.

## Verify if you are using the IAP OAuth Admin API

To check if your project uses IAP OAuth Admin APIs, see Check for OAuth Admin APIs usage.

## Alternatives to using the OAuth Admin API

If you need to obtain OAuth client credentials without using the OAuth API, you can use the following methods:

  * Google Cloud console: You can manually obtain OAuth credentials through the [**Credentials**](https://console.cloud.google.com/apis/credentials) page.

  * Secret Manager: You can store and retrieve the secret using Secret Manager. To learn how to use Secret Manager with Terraform, see [google_secret_manager_secret](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/secret_manager_secret.html).

  * Service account JWTs: Use service account JSON Web Tokens (JWTs) for authentication. With service account JWTs, you don't need to use OAuth clients.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
