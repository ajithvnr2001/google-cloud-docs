---
url: https://docs.cloud.google.com/iap/docs/enabling-cloud-run/
title: Enable IAP for Cloud Run \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:13.171442+00:00
---

# Enable IAP for Cloud Run  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/enabling-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Enable IAP for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

You can enable Identity-Aware Proxy for your Cloud Run services by using one of the following methods: 

  1. **Recommended:** [Enable IAP **directly on a Cloud Run service**](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run), which has the following benefits:

     * Protects the `run.app` endpoint directly so that you don't have to provision load balancer resources.

     * Provides a simpler setup and avoids additional load balancer costs.

     * If you opt to place a load balancer in front of Cloud Run, the load balancer's endpoint is also protected.

  2. **Enable IAP on the backend service fronting the Cloud Run services:** If you're running Cloud Run in multiple regions attached to the same load balancer global backend service and you require central access management, follow the instructions on this page. Otherwise, we recommend that you [enable IAP directly on the Cloud Run service](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run). 

### Known limitations

     * IAP can't be used on both Cloud Run services and the load balancer. If you enable IAP on a load balancer, IAP secures traffic only through the load balancer and not with traffic that might reach the Cloud Run service through its `run.app` URL. To only allow IAP-authorized traffic, see Configuring Cloud Run to limit access.

     * IAP authenticates to Cloud Run using the [`X-Serverless-Authorization`](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#acquire-token) header. Cloud Run passes this header to your service after [stripping its signature](https://docs.cloud.google.com/run/docs/troubleshooting#signature-removed). If your service is designed to forward the request to another Cloud Run service that requires IAM authentication, update your service to remove this header first.

     * IAP is incompatible with Cloud CDN.

     * IAP increases latency. Enable IAP only for services that are not latency-sensitive.

## Before you begin

We recommend that you [enable IAP directly on Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run). 

If you choose to enable IAP for Cloud Run resources on the load balancer rather than directly on Cloud Run, you must have the following:

     * A Google Cloud console project with billing enabled.
     * A group of one or more Cloud Run services, served by a load balancer. 
       * Learn about [Setting up an external HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless).
       * Learn about [Setting up an internal HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless).
     * A domain name registered to the address of your load balancer.
     * Application code to verify that all requests have an identity.

       * Learn about [Getting the user's identity](https://docs.cloud.google.com/iap/docs/identity-howto). 

## Enabling IAP from a backend service or load balancer

Note: We recommend that you enable IAP directly on Cloud Run, as described in the [Cloud Run documentation](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run). 

To enable IAP on a backend service of a load balancer, use the following instructions. 

###  Console 

If you haven't configured your project's OAuth consent screen, you'll be prompted to do so. To configure your OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615). 

### Setting up IAP access

     1. Go to the [Identity-Aware Proxy page](https://console.cloud.google.com/security/iap).
     2. Select the project you want to secure with IAP.
     3. Under **APPLICATIONS** , select the checkbox next to the load balancer backend service to which you want to add members.
     4. On the right side panel, click **Add Principal**.
     5. In the **Add Principal** dialog, enter the accounts of groups or individuals who should have the **IAP-secured Web App User** role for the project. The following kinds of accounts can be members: 

        * **Google Account** : user@gmail.com - This can also be a Google Workspace account, such as user@google.com or some other Workspace domain.
        * **Google Group** : admins@googlegroups.com
        * **Service account** : server@example.iam.gserviceaccount.com
        * **Google Workspace domain** : example.com 
     6. Select **Cloud IAP > IAP-secured Web App User** from the **Roles** drop-down list.

     7. Click **Save**.

### Enabling access to users outside your organization

By default, when you enable IAP, it uses a Google-managed OAuth client to authenticate users. As a result, only users within the organization can access the IAP-enabled application.

To enable access to users outside your organization, or without an organization, update the OAuth client configuration to use a custom OAuth client as described in [Enable IAP for external applications](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration). 

### Turning on IAP

     1. On the [IAP page](https://console.cloud.google.com/security/iap), under **APPLICATIONS** , find the load balancer backend service to which you want to restrict access. To turn on IAP for a resource, click the **IAP** toggle. To enable IAP: 
        * At least one protocol in the load balancer frontend configuration must be HTTPS. Learn about [setting up a load balancer](https://docs.cloud.google.com/iap/docs/load-balancer-howto).
        * You need the `compute.backendServices.update`, `clientauthconfig.clients.create`, and `clientauthconfig.clients.getWithSecret` permissions. These permissions are granted by roles, such as the Project Editor role. To learn more, see [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access#turning_on_and_off). 
     2. In the **Turn on IAP** window that appears, click **Turn On** to confirm that you want IAP to secure your resource. After you turn on IAP, it requires login credentials for all connections to your load balancer. Only accounts with the **IAP-Secured Web App User** role on the project will be given access.
     3. Follow the instructions at [Access control with IAM](https://docs.cloud.google.com/run/docs/securing/managing-access#add-principals) to authorize IAP to send traffic to the backend Cloud Run service.

        * **Principal** : `service-[PROJECT-NUMBER]@gcp-sa-iap.iam.gserviceaccount.com`
        * **Role** : **Cloud Run Invoker**

The IAP service account is created when IAP is enabled. If the IAP service account is not in the list of principals, you can create it by running the following gcloud command:
    
    gcloud services identity create \
        --service=iap.googleapis.com \
        --project=PROJECT_ID
    

###  gcloud 

     1. If you have not previously done so in the project, create the IAP service agent by running the following command. If you previously created the service agent, running the command does not duplicate it. 
            
            gcloud services identity create --service=iap.googleapis.com --project=[PROJECT_ID]

     2. Grant the invoker permission to the service account, created in the previous step, by running the following command. 
            
            gcloud run services add-iam-policy-binding [SERVICE-NAME] \
            --member='serviceAccount:service-[PROJECT-NUMBER]@gcp-sa-iap.iam.gserviceaccount.com'  \
            --role='roles/run.invoker'
            

     3. Enable IAP by running either the globally or regionally scoped command, depending on whether your load balancer backend service is global or regional. Use the OAuth client ID and secret from the previous step.

Global scope 
            
            gcloud compute backend-services update BACKEND_SERVICE_NAME --global --iap=enabled
            

Regional scope 
            
            gcloud compute backend-services update BACKEND_SERVICE_NAME --region REGION_NAME --iap=enabled
            

Replace the following: 
        * BACKEND_SERVICE_NAME: the name of the backend service.
        * REGION_NAME: the region where you want to enable IAP. 

After you enable IAP, you can use the Google Cloud CLI to manipulate an IAP access policy using the Identity and Access Management role `roles/iap.httpsResourceAccessor`. See [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access) for more information.

###  Terraform 

     1. If you have not previously done so, in a project, create the IAP service agent by running the following command. If you previously created the service agent, running the command does not duplicate it. 
            
            resource "google_project_service" "project" {
              project = "your-project-id"
              service = "iap.googleapis.com"
            }
            

     2. Add the following to grant the `roles/run.invoker` role to the IAP service agent.
            
            resource "google_cloud_run_v2_service_iam_member" "iap_invoker" {
              project = google_cloud_run_v2_service.default.project
              location = google_cloud_run_v2_service.default.location
              name = google_cloud_run_v2_service.default.name
              role   = "roles/run.invoker"
              member = "serviceAccount:service-"PROJECT_NUMBER@gcp-sa-iap.iam.gserviceaccount.com"
            }
            

Replace PROJECT_NUMBER with your project number.

     3. Enable IAP by running either the global or the regional command depending on your load balancer. Use the OAuth client ID and secret from the previous step.

        * Global scope 
              
              resource "google_compute_backend_service" "default" {
                name                  = "tf-test-backend-service-external"
                protocol              = "HTTPS"
                load_balancing_scheme = "EXTERNAL_MANAGED"
                iap {
                  enabled              = true
                  oauth2_client_id     = "abc"
                  oauth2_client_secret = "xyz"
                }
              }
              

        * Regional scope 
              
              resource "google_compute_region_backend_service" "default" {
                name                  = "tf-test-backend-service-external"
                protocol              = "HTTPS"
                load_balancing_scheme = "EXTERNAL_MANAGED"
                iap {
                  enabled              = true
                  oauth2_client_id     = "abc"
                  oauth2_client_secret = "xyz"
                }
              }
              

## Configuring Cloud Run to limit access

To prevent traffic from routing through a Cloud Run service's default `run.app` URL, [Disable the default URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url). Otherwise, configure your ingress settings to [Restrict network ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress).

## Troubleshooting errors

### Permission denied accessing Cloud Run
    
    Your client does not have permission to get URL from this server 

     * IAP uses the IAP service account permissions to invoke your Cloud Run service. Be sure that you have granted the Cloud Run Invoker role to the following service account: `service-[PROJECT-NUMBER]@gcp-sa-iap.iam.gserviceaccount.com`.

     * If you have granted the Cloud Run Invoker role to the preceding service account and you are still facing this issue, redeploy your Cloud Run service.

### Service Agent failure causes set IAM error

Enabling IAP on a new project for the first time can cause the following error:
    
    Setting IAM permissions failed

This is because the Cloud Run Service Agent failed. To resolve the issue, either [enable IAP](https://docs.cloud.google.com/iap/docs/enabling-cloud-run#enable-from-iap) again or [set the IAM policy manually](https://docs.cloud.google.com/iap/docs/managing-access#managing_access_console).

### Can't set up IAP through the gcloud CLI
    
    The IAP service account is not provisioned 

If you are seeing this error, run the following command:

` gcloud services identity create --service=iap.googleapis.com --project=[PROJECT_ID] `

### IAP service account doesn't need `run.routes.invoke` permission

During the IAP with Cloud Run Preview, Cloud Run didn't perform the `run.routes.invoke` permission check for calls from IAP that use the Cloud Run Invoker role. With General Availability (GA), Cloud Run performs this permission check.

To avoid breaking changes, some customer projects that depended on this behavior during Preview were placed into an allowlist so that the permission wasn't checked. Contact [Cloud Run support](https://docs.cloud.google.com/run/docs/support) to remove such projects from the Preview-only allowlist.

## What's next

[Configure IAP for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
