---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-compute-engine/
title: Securing Compute Engine apps and resources with IAP \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:21.519817+00:00
---

# Securing Compute Engine apps and resources with IAP  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)
  * [ Guides ](https://docs.cloud.google.com/chrome-enterprise-premium/docs/overview)



Send feedback 

#  Securing Compute Engine apps and resources with IAP Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to secure a Compute Engine instance with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview).

To secure resources not on Google Cloud, see [Securing on-premises apps and resources](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-on-premises).

## Before you begin

To enable IAP for Compute Engine, you need the following:

  * A Google Cloud console project with billing enabled.
  * A group of one or more Compute Engine instances, served by a load balancer. 
    * Learn about [Setting up an external HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https).
    * Learn about [setting up an internal HTTP load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal).
  * A domain name registered to the address of your load balancer.
  * Application code to verify that all requests have an identity. 
    * Learn about [Getting the user's identity](https://docs.cloud.google.com/iap/docs/identity-howto).



If you don't have your Compute Engine instance set up already, see [Setting up IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/tutorial-gce) for a complete walkthrough.

IAP uses a Google-managed OAuth client to authenticate users. Only users within the organization can access the IAP-enabled application. If you want to allow access to users outside of your organization, see [Enable IAP for external applications](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration).

You can enable IAP on a Compute Engine [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) or on a Compute Engine [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). When you enable IAP on a Compute Engine backend service, only that backend service is protected by IAP. When you enable IAP on a Compute Engine forwarding rule, all of the Compute Engine instances behind the forwarding rule are protected by IAP.

## Enable IAP on a forwarding rule

You can enable IAP on a forwarding rule by using the load balancer [authorization policies](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview) framework.

###  gcloud 

  1. Run the following command to prepare a `policy.yaml` file. The policy allows clients with an IP address range of `10.0.0.0/24` to enable IAP on a forwarding rule.


    
    
    $ cat << EOF > policy.yaml
    action: CUSTOM
    description: authz policy with Cloud IAP
    name: AUTHZ_POLICY_NAME
    httpRules:
      - from:
          sources:
          - ipBlocks:
            - prefix: "10.0.0.0"
              length: 24
    customProvider:
      cloudIap: {}
    target:
      loadBalancingScheme: EXTERNAL_MANAGED
      resources:
      - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_ID
    EOF
    

  1. Run the following command to enable IAP on a forwarding rule.


    
    
    gcloud network-security authz-policies import AUTHZ_POLICY_NAME \
    --source=policy.yaml \
    --location=LOCATION \
    --project=PROJECT_ID
    

Replace the following:

  * PROJECT_ID: The Google Cloud project ID.
  * LOCATION: The region that the resource is located in.
  * FORWARDING_RULE_ID: The ID of the forwarding rule resource.
  * AUTHZ_POLICY_NAME: The name of the authorization policy.



###  API 

  1. Run the following command to prepare a `policy.json` file. 
         
         cat << EOF > policy.json
         {
         "name": "AUTHZ_POLICY_NAME",
         "target": {
           "loadBalancingScheme": "INTERNAL_MANAGED",
           "resources": [
             "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_ID"
           ],
         },
         "action": "CUSTOM",
         "httpRules": [
           {
             "from": {
               "sources": {
                 "ipBlocks": [
                   {
                     "prefix": "10.0.0.0",
                     "length": 24
                   }
                 ]
               }
             }
           }
         ],
         "customProvider": {
           "cloudIap": {}
         }
         }
         EOF
         

  2. Run the following command to enable IAP on a forwarding rule. 
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @policy.json \
         "https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authzPolicies"
         

Replace the following:

     * PROJECT_ID: The Google Cloud project ID.
     * LOCATION: The region that the resource is located in.
     * FORWARDING_RULE_ID: The ID of the forwarding rule resource.
     * AUTHZ_POLICY_NAME: The name of the authorization policy.



After you enable IAP on a forwarding rule, you can [apply permissions to resources](https://docs.cloud.google.com/iap/docs/auth-policies#apply_permissions_to_resources).

## Enable IAP on a Compute Engine backend service

You can enable IAP on a Compute Engine backend service through that backend service.

### console

The Google-managed OAuth client is not available when enabling IAP using the Google Cloud console.

If you haven't configured your project's OAuth consent screen, you'll be prompted to do so. To configure your OAuth consent screen, see [Setting up your OAuth consent screen](https://support.google.com/cloud/answer/10311615).

If you are running GKE clusters version 1.24 or later, you can configure IAP and GKE by using the Kubernetes Gateway API. To do so, complete the following steps and then follow the instructions in [Configure IAP](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_iap). Do not configure `BackendConfig`.

### Setting up IAP access

  1. Go to the [Identity-Aware Proxy page](https://console.cloud.google.com/security/iap).   
[Go to the Identity-Aware Proxy page](https://console.cloud.google.com/security/iap)
  2. Select the project you want to secure with IAP.
  3. Select the checkbox next to the resource you want to grant access to.

If you don't see a resource, ensure that the resource is created and that the BackendConfig Compute Engine ingress controller is synced.

To verify that the backend service is available, run the following gcloud command:

`gcloud compute backend-services list`
  4. On the right side panel, click **Add principal**. 
  5. In the **Add principals** dialog that appears, enter the email addresses of groups or individuals who should have the **IAP-secured Web App User** role for the project. 

The following kinds of principals can have this role:

     * **Google Account** : user@gmail.com 
     * **Google Group** : admins@googlegroups.com 
     * **Service account** : server@example.gserviceaccount.com 
     * **Google Workspace domain** : example.com 

Make sure to add a Google Account that you have access to.

  6. Select **Cloud IAP > IAP-secured Web App User** from the **Roles** drop-down list. 
  7. Click **Save**. 



### Turning on IAP

  1. On the **Identity-Aware Proxy** page, under **APPLICATIONS** , find the load balancer that serves the instance group you want to restrict access to. To turn on IAP for a resource,  toggle the on/off switch in the **IAP** column.   
To enable IAP: 
     * At least one protocol in the load balancer frontend configuration must be HTTPS. Learn about [setting up a load balancer](https://docs.cloud.google.com/iap/docs/load-balancer-howto). 
     * You need the `compute.backendServices.update`, `clientauthconfig.clients.create`, `clientauthconfig.clients.update`, and `clientauthconfig.clients.getWithSecret` permissions. These permissions are granted by roles, such as the Project Editor role. To learn more, see [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access#turning_on_and_off). 
  2. In the **Turn on IAP** window that appears, click **Turn On** to confirm that you want IAP to secure your resource. After you turn on IAP, it requires login credentials for all connections to your load balancer. Only accounts with the **IAP-Secured Web App User** role on the project will be given access. 



### gcloud

Before you set up your project and IAP, you need an up-to-date version of the gcloud CLI. For instructions on how to install the gcloud CLI, see [Install the gcloud CLI](https://docs.cloud.google.com/sdk/downloads).

  1. To authenticate, use the Google Cloud CLI and run the following command. 
         
         gcloud auth login

  2. To sign in, follow the URL that appears.
  3. After you sign in, copy the verification code that appears and paste it in the command line. 
  4. Run the following command to specify the project that contains the resource that you want to protect with IAP. 
         
         gcloud config set project PROJECT_ID

  5. To enable IAP, run either the globally or regionally scoped command.   
  
Global scope 
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME --global --iap=enabled

Regional scope 
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME --region REGION_NAME --iap=enabled




After you enable IAP, you can use the gcloud CLI to modify the IAP access policy using the IAM role `roles/iap.httpsResourceAccessor`. Learn more about [managing roles and permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### API

  1. Run the following command to prepare a `settings.json` file. 
         
         cat << EOF > settings.json
         {
         "iap":
           {
             "enabled":true
           }
         }
         EOF
         

  2. Run the following command to enable IAP. 
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/REGION/backendServices/BACKEND_SERVICE_NAME"
         




After you enable IAP, you can use the Google Cloud CLI to modify the IAP access policy using the IAM role `roles/iap.httpsResourceAccessor`. Learn more about [managing roles and permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Next steps

  * Set richer context rules by [applying access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels).
  * See [Context-Aware Access logs in Cloud Audit Logs](https://docs.cloud.google.com/access-context-manager/docs/audit-logs).
  * Learn more about [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
