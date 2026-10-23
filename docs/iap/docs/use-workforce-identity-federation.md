---
url: https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation/
title: Configure IAP with Workforce Identity Federation \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:08.451421+00:00
---

# Configure IAP with Workforce Identity Federation  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/use-workforce-identity-federation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Configure IAP with Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure Identity-Aware Proxy (IAP) to use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

When you configure Workforce Identity Federation with IAP, you can use an external identity provider (IdP) to authenticate and authorize a workforce—a group of users, such as employees, partners, and contractors—using Identity and Access Management (IAM), so that the users can securely access services deployed on Google Cloud or on-premises.

Configuring IAP with Workforce Identity Federation lets you do the following with regards to your IAP-secured applications:

  * Redirect an end user to an external IdP, such as Okta, to sign in.
  * Configure a sign-in session between 15 minutes and 12 hours.
  * Allow only specific end users or end user sets in an IdP to access your application.
  * Specify the context under which an end user can access an application. For example, only allow access during a specific time of the day.

You can use IAP with Workforce Identity Federation on all existing resources and load balancers that IAP supports. 

## Configure IAP with Workforce Identity Federation for an application

Configuring IAP with Workforce Identity Federation comprises the following main tasks:

  1. Set up a workforce pool and provider.
  2. Create an OAuth client ID and secret.
  3. Enable IAP and configure it to use Workforce Identity Federation.



### Set up a workforce pool and provider

To set up a workforce pool and provider, follow the instructions for one of the following providers:

  * [Microsoft Entra ID](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id)
  * [Okta](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta)
  * [other OIDC or SAML 2.0 provider](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation)



When setting the session duration time, refer to [Manage IAP with Workforce Identity Federation sessions](https://docs.cloud.google.com/iap/docs/manage-iap-wif-sessions).

If you want to map an email address from a third-party IdP to Google Cloud, you must add an attribute mapping in your workforce pool provider for `google.email`. Example: `google.email=assertion.email`.

### Create an OAuth client ID and secret

Important: The OAuth client ID and secret that you create in the following steps are created for the Workforce Identity Federation infrastructure. These are different than the client ID and secret that are required when using the [custom OAuth configuration to enable IAP](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration) with Google identities. 

  1. Follow the instructions to [create an OAuth client ID and secret](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app) under a project in the same organization as the workforce pool that you will be using for this configuration. The project does not have to be the same project that the IAP-secured resource is in. When creating the OAuth client ID and secret, do the following:

     1. Use a placeholder for the redirect URI when creating the client ID. After you create the client ID, run [`describe` an OAuth client](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#describe) to get the generated `clientID`.

     2. When you have the `clientID`, run [`update` an OAuth client](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#update) to update `allowed-redirect-uris` to the following: `https://iap.googleapis.com/v1/oauth/clientIds/$CLIENT_ID:handleRedirect`.

Where `CLIENT_ID` is the `clientID` retrieved in the previous step.

     3. After you create the client secret, run [`describe` an OAuth client credentials](https://docs.cloud.google.com/iam/docs/workforce-manage-oauth-app#describe-credential) to get the generated `clientSecret`.

Save the `clientId` and `clientSecret` because you will need them in later steps.




### Enable IAP to use Workforce Identity Federation

To enable IAP with Workforce Identity Federation, complete the following steps.

#### Enable IAP

Enable IAP on the resource.

###  console 

  1. In the Google Cloud console, open the IAP page.  
[ Go to the IAP page](https://console.cloud.google.com/security/iap)
  2. Select a project. The project must be in the same organization as the workforce pool that you created earlier. The project doesn't have to be the project that you created the OAuth client ID and secret in.
  3. Click the **Applications** tab, and then locate the application that you want to restrict access to using IAP.
  4. In the IAP column, toggle the switch to **On**.



###  gcloud 

To use the gcloud CLI to enable IAP, follow the procedures for the applicable service:

  * IAP for Cloud Run:

    * [Enable directly with Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run)

    * [Enable with a load balancer](https://docs.cloud.google.com/iap/docs/enabling-cloud-run)

  * [IAP for App Engine](https://docs.cloud.google.com/iap/docs/enabling-app-engine#enabling-iap-sdk)

  * [IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto#enabling_iap_sdk)




###  API 

  1. Create a `settings.json` file.
         
         cat << EOF > settings.json
         {
         "iap":
           {
             "enabled":true,
          }
         }
         EOF
         

  2. Enable IAP on App Engine.
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @settings.json \
         "https://appengine.googleapis.com/v1/apps/PROJECT_ID?updateMask=iap.enabled"
         

To enable IAP on Compute Engine, use the following URL: `https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/REGION/backendServices/BACKEND_SERVICE_NAME?updateMask=iap.enabled`. 




#### Update the IAP settings

To configure IAP to use Workforce Identity Federation, you must configure the following settings:

  * `WorkforceIdentitySettings`: The OAuth client ID and secret created earlier.
  * `IdentitySources`: The identity source.



For more information, see the [IAP APIs](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings).

###  gcloud 

  1. Using the following example as a reference, create an `iap_settings.yaml` file.
         
         CLIENT_ID=clientId
         CLIENT_SECRET=clientSecret
         WORKFORCE_POOL_NAME=locations/global/workforcePools/test-pool
         cat <<EOF > iap_settings.yaml
         access_settings:
           identity_sources: ["WORKFORCE_IDENTITY_FEDERATION"]
           workforce_identity_settings:
             workforce_pools: ["$WORKFORCE_POOL_NAME"]
             oauth2:
               client_id: "$CLIENT_ID"
               client_secret: "$CLIENT_SECRET"
         EOF
         

  2. Run the following command to update the IAP settings for your resource.
         
         gcloud iap settings set iap_settings.yaml --project=PROJECT --resource-type=RESOURCE_TYPE --service=SERVICE
         

Replace the following:

     * PROJECT: The project ID.
     * RESOURCE_TYPE: The IAP resource type. The resource type must be `cloud-run` [(Preview)](https://cloud.google.com/products#product-launch-stages), `app-engine`, `iap_web`, `compute`, `organization`, or `folder`. For the `cloud-run` resource type, use the `--region` flag to indicate the region where your Cloud Run service is deployed.
     * SERVICE: The service name. This is optional for both `app-engine` and `compute`.

For details on the command, see [gcloud iap settings set](https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings/set).




###  API 

  1. Using the following example as a reference, create an `iap_settings.json` settings file.
         
         CLIENT_ID=clientId
         CLIENT_SECRET=clientSecret
         WORKFORCE_POOL_NAME=locations/global/workforcePools/test-pool
         cat <<EOF > iap_settings.json
         {
            "access_settings": {
              "identity_sources": ["WORKFORCE_IDENTITY_FEDERATION"],
              "workforce_identity_settings": {
                "workforce_pools": ["$WORKFORCE_POOL_NAME"],
                "oauth2": {
                  "client_id": "$CLIENT_ID",
                  "client_secret": "$CLIENT_SECRET",
                }
             }
           }
         }
         EOF
         

  2. Use the gcloud CLI to get the name of the resource, and then copy the `RESOURCE_NAME` from the output because you will need it in the following step. 
         
         gcloud iap settings get \
             --project=PROJECT \
             --resource-type=RESOURCE_TYPE \
             --service=SERVICE
         

Replace the following:

     * PROJECT: The project ID.
     * RESOURCE_TYPE: The IAP resource type. The resource type must be `appengine`, `iap_web`, `compute`, `organization`, `folder`, or `cloud_run-$REGION` [(Preview)](https://cloud.google.com/products#product-launch-stages), where $REGION is the region in which your Cloud Run service is deployed.
     * SERVICE: The service name. This is optional for both `app-engine` and `compute`.
  3. Replace `RESOURCE_NAME` in the following command with the `RESOURCE_NAME` from the previous step.
         
         curl -X PATCH \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Accept: application/json" \
          -H "Content-Type: application/json" \
          -d @iap_settings.json \
         "https://iap.googleapis.com/v1/RESOURCE_NAME:iapSettings?updateMask=iapSettings.accessSettings.identitySources,iapSettings.accessSettings.workforceIdentitySettings.workforcePools,iapSettings.accessSettings.workforceIdentitySettings.oauth2.clientId,iapSettings.accessSettings.workforceIdentitySettings.oauth2.clientSecret"
         




#### Grant access to IAP-secured resources

To access an IAP-secured resource, end users must have the [IAP-Secured Web App User](https://docs.cloud.google.com/iap/docs/managing-access#roles) role on the resource. You can grant the IAP-Secured Web App User role to a single user (principal) or a set of users ([principal set](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users), which maps to a group, a specific attribute, or an entire pool of users).

**Important:** When providing the principals for Workforce Identity Federation, you must use a [principal identifier](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users). Don't use an email address.

Unrestricted access to IAP-secured resources is not supported.

###  console 

  1. In the Google Cloud console, open the IAP page.  
[ Go to the IAP page](https://console.cloud.google.com/security/iap)
  2. Select the resource you want to secure with IAP.
  3. Click **Add Principal** , and then add the [principal identifiers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users) of the groups or individuals to which you want to grant an IAM role for the resource.
  4. In **Assign roles** , select **IAP-Secured Web App User**.
  5. Click **Add**.



###  gcloud 

Run the following command.
    
    
    gcloud iap web add-iam-policy-binding \
        --member=PRINCIPAL_IDENTIFIER \
        --role='roles/iap.httpsResourceAccessor' \
        --project=PROJECT_ID \
        --resource-type=RESOURCE_TYPE \
        --service=SERVICE \
        --condition=CONDITION
    

Replace the following:

  * PRINCIPAL_IDENTIFIER: The [principal identifier](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#representing-workforce-users).
  * PROJECT_ID: The project ID. 
  * RESOURCE_TYPE: The IAP resource type, which can be `app-engine` or `backend-services`. 
  * SERVICE: (Optional) The service name.
  * CONDITION: (Optional) [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview). Following is an example condition configured with access levels:


    
    
    expression="accessPolicies/12345678/accessLevels/iap_test_access_level" in request.auth.access_levels,title=iap-test-access-level,description=only access on weekdays
    

###  API 

This method is not recommended because it touches the entire IAM policy of a resource. An error could remove the policy from a resource.

  1. Obtain the existing IAM policy bindings.
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           -H "Content-Type: application/json" \
           -d {} \
         "https://iap.googleapis.com/v1/RESOURCE_NAME:getIamPolicy" -o iam_policy_bindings.json
         

Replace the RESOURCE_NAME with the RESOURCE_NAME that you obtained in an earlier step.

  2. To the `iam_policy_bindings.json` file that you obtained from the previous step, remove the version and etag lines, and add the binding that you want to add for the principal identifier. For more information, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/policies).
         
         {
           "bindings": [
             {
               // existing bindings
             },
             {
               "role": "roles/iap.httpsResourceAccessor",
               "members": [
               "principal://iam.googleapis.com/locations/global/workforcePools/iap-test-pool/subject/iap-test-subject"
               ],
               "condition": {
                 "expression": "\"accessPolicies/12345678/accessLevels/iap_test_access_level\" in request.auth.access_levels",
                 "title": "iap-test-access-level",
                 "description": "only access on weekdays"
               }
             }
           ]
         }
         

  3. Update the IAM policy bindings.
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Accept: application/json" \
           -H "Content-Type: application/json" \
           -d "{"policy":$(cat iam_policy_bindings.json)}" \
         "https://iap.googleapis.com/v1/RESOURCE_NAME:setIamPolicy"
         

Replace the RESOURCE_NAME with the RESOURCE_NAME that you obtained in an earlier step.




See [GetIamPolicy](https://docs.cloud.google.com/iap/docs/reference/rest/v1/TopLevel/getIamPolicy) and [SetIamPolicy](https://docs.cloud.google.com/iap/docs/reference/rest/v1/TopLevel/setIamPolicy) for more information.

#### (Optional) Set up context-aware access

Optionally, you can set up context-aware access rules for advanced authorization.

To set up access levels, see [Creating and applying access levels](https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels). Access levels based on device information are not available when using Workforce Identity Federation. You can still use request-context-based access levels with conditions on IP address, and time and date.

### Programmatic authentication

IAP supports service account JWT authentication for applications configured with Workforce Identity Federation. For instructions, see [Authenticating with a service account JWT](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating-with-a-service-account-jwt).

### Limitations when working with workforce pools

* For each IAP-enabled application, only one workforce pool can be configured, and the workforce pool can contain only one provider. * The workforce pool, OAuth client ID and secret, and the IAP-enabled applications must all be in the same organization. * Access levels for device-related information are not supported. * Only the following IAP settings configurations are supported: * [CorsSettings](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#CorsSettings) * [CsmSettings](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#CsmSettings) * [AccessDeniedPageSettings.accessDeniedPageUri](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#AccessDeniedPageSettings) * [CookieDomain](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings#ApplicationSettings) * Programmatic access with Workforce Identity Federation is only supported for Google service accounts. 

### Troubleshooting

For troubleshooting information, see [Troubleshooting and frequently asked questions](https://docs.cloud.google.com/iap/docs/faq).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
