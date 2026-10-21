---
url: https://docs.cloud.google.com/iam/docs/configure-scim-okta/
title: Configure SCIM in Okta \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:09:59.106212+00:00
---

# Configure SCIM in Okta  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/configure-scim-okta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure SCIM in Okta Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** SCIM provisioning applies only to Gemini Enterprise and Looker ([Preview](https://cloud.google.com/products#product-launch-stages)).

This document describes how to configure a SCIM tenant in a workforce identity pool. To learn more about SCIM, see [SCIM provisioning for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim). 

Each workforce identity pool supports only one SCIM tenant. To configure a new SCIM tenant in a pool that already has one, you must first hard-delete the existing tenant. 

The `--claim-mapping` flag for a SCIM tenant can contain only specific Common Expression Language (CEL) expressions. To learn which expressions are supported, see Claim mapping. 

Ensure that your IdP provides unique, non-empty values for attributes mapped to `google.subject` and `google.group`. Syncing duplicate values fails with an HTTP `409 Conflict` error, and null or empty values fail with an HTTP `400 Bad Request` error. For more information, see [SCIM support](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim). 

To configure [System for Cross-domain Identity Management (SCIM)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim), do the following: 

  1. Configure a SCIM tenant and token in Google Cloud
  2. Configure SCIM in Okta
  3. Update the provider to enable SCIM
  4. Verify SCIM synchronization



## Configure a SCIM tenant and token in Google Cloud

To configure a SCIM tenant in Google Cloud, do the following: 

  1. Create a SCIM tenant. 
         
         gcloud iam workforce-pools providers scim-tenants create SCIM_TENANT_ID \
                 --workforce-pool="WORKFORCE_POOL_ID" \
                 --provider="PROVIDER_ID" \
                 --display-name="SCIM_TENANT_DISPLAY_NAME" \
                 --description="SCIM_TENANT_DESCRIPTION" \
                 --claim-mapping="CLAIM_MAPPING" \
                 --location="global"
             

Replace the following: 

     * `SCIM_TENANT_ID`: an ID for your SCIM tenant.
     * `WORKFORCE_POOL_ID`: the ID of the workforce pool that you created earlier in this document.
     * `PROVIDER_ID`: the ID of the workforce identity pool provider that you created earlier in this document.
     * `SCIM_TENANT_DISPLAY_NAME`: a display name for your SCIM tenant.
     * `SCIM_TENANT_DESCRIPTION`: a description for your SCIM tenant.
     * `CLAIM_MAPPING`: a comma-separated list of attribute mappings. For the extended list of mapping attributes, see Claim mapping. The following mapping is recommended for Gemini Enterprise: 
           
           google.subject=user.emails[0].value.lowerAscii(),google.group=group.displayName

The `google.subject` attribute that you map in the SCIM tenant must uniquely refer to the same identities that are mapped in the `google.subject` attribute in the workforce identity pool provider by using the `--attribute-mapping` flag. After the SCIM tenant is created, you can't update the claim mapping. To replace it, you can hard-delete the SCIM tenant and immediately create a new one. To learn more about considerations for using SCIM, see [SCIM support](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim).

  2. When the command completes, do the following: 

     1. In the `baseUri` field in the output, save the entire URI, which is formatted as `https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID`. You need to provide this URI to your IdP. 
     2. Additionally, from the URI, save only the `SCIM_TENANT_UID`. You need this UID to set an IAM allow policy on the SCIM tenant later in this document. 
  3. Create a SCIM token: 
         
         gcloud iam workforce-pools providers scim-tenants tokens create SCIM_TOKEN_ID \
                 --display-name DISPLAY_NAME \
                 --scim-tenant SCIM_TENANT_ID \
                 --workforce-pool WORKFORCE_POOL_ID \
                 --provider PROVIDER_ID \
                 --location global
             

Replace the following: 

     * `SCIM_TOKEN_ID`: an ID for the SCIM token
     * `DISPLAY_NAME`: the display name of the SCIM token
     * `WORKFORCE_POOL_ID`: the ID of the workforce pool
     * `SCIM_TENANT_ID`: the ID of the SCIM tenant
     * `PROVIDER_ID`: the ID of the workforce identity pool provider
  4. When the `gcloud iam workforce-pools providers scim-tenants tokens create` command completes, do the following: 

     1. In the output, save the value of `SCIM_TOKEN` in the `securityToken` field. You need to provide this security token to your IdP. The security token is displayed only in this output, and if it's lost, you must create a new SCIM token.

     2. To check if `SCIM_TOKEN` is rejected by your organization policy, run the following command:
            
            curl -v -H "Authorization: Bearer SCIM_TOKEN"  https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Users

If the command fails with a permissions-related error, run `gcloud organizations add-iam-policy-binding`, described in a later step. If the command succeeds, you can skip that step.

  5. Set an IAM allow policy on the SCIM tenant and token. If the `curl` command in a previous step failed with a permissions-related error, you must run the following command: 
         
         gcloud organizations add-iam-policy-binding ORGANIZATION_ID \
                 --member=serviceAccount:SERVICE_AGENT_EMAIL \
                 --role roles/iam.scimSyncer
             

Replace the following: 

     * ORGANIZATION_ID: the ID of the organization.
     * SERVICE_AGENT_EMAIL: the email address of the service agent. The email address is in the following format: `o-ORGANIZATION_ID-SCIM_TENANT_UID@gcp-sa-iamscim.iam.gserviceaccount.com`. SCIM_TENANT_UID is returned when you create the SCIM tenant.



When you provision groups in your IdP, make sure that each group's display name, as provided in the `displayName` field, is unique within a SCIM tenant. To learn more about groups and SCIM in Microsoft Entra ID, see [Groups](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups#groups). 

## Configure SCIM in Okta

To configure SCIM in Okta, in your existing Okta application, do the following: 

  1. Sign in to the Okta Admin Console. 
  2. Go to **Applications** > **Applications**. 
  3. Select or create your application:

     * If you want to select an existing application, do the following:

       1. Click the name of the application you created using the Google Cloud Workforce Identity Federation template.
       2. In the **General** tab, do the following:

          1. In the **App Settings** pane, click **Edit**.
          2. In the **Tenant** field, enter the Tenant ID obtained from gcloud CLI.
          3. Click **Done**.
     * If you want to create a new application, do the following:

       1. Click **Browse App Catalog**.
       2. In the **Search** field, enter **Google Cloud Workforce Identity Federation** , and then select **Google Cloud Workforce Identity Federation** integration from the results.
       3. Click **Add Integration**.

          1. In the **Application** field, enter a name for your app.
          2. In the **Tenant** field, enter the Tenant ID obtained from gcloud CLI.
          3. Click **Done**.
  4. In the **Provisioning** tab, do the following:

     1. In the **Integration** pane, click **Edit**.

        1. In the **API Token** field, enter the SCIM token you obtained from Google Cloud.
        2. To confirm the validity of the API token, click **Test Credentials**.
        3. Select **Import Groups**.
        4. Click **Save**.
     2. In the **To App** pane, click **Edit**.

        1. Select **Create Users** , **Update User Attributes** , and **Deactivate users**.
        2. Click **Save**.



## Update the provider to enable SCIM

To enable SCIM for a provider, set the `--scim-usage` flag based on your product target: 

  * **Enabled for groups (`enabled-for-groups`)**: Used for Gemini Enterprise. Uses SCIM-synced groups for IAM authorization and policy evaluation. User attributes continue to be sourced from IdP login tokens. 
  * **Enabled for users and groups (`enabled-for-users-groups`)**: Used for Looker ([Preview](https://cloud.google.com/products#product-launch-stages)). Uses SCIM-synced user and group data as the primary source of claims for IAM authorization and OAuth sign-in workflows. 



### Enable SCIM for groups (Gemini Enterprise)

#### OIDC
    
    
          gcloud iam workforce-pools providers update-oidc PROVIDER_ID \
              --workforce-pool=WORKFORCE_POOL_ID \
              --location=LOCATION \
              --scim-usage=enabled-for-groups
        

Replace the following: 

  * `PROVIDER_ID`: the ID of the workforce identity pool provider
  * `WORKFORCE_POOL_ID`: the ID of the workforce pool
  * `LOCATION`: the location of the workforce pool



#### SAML
    
    
          gcloud iam workforce-pools providers update-saml PROVIDER_ID \
              --workforce-pool=WORKFORCE_POOL_ID \
              --location=LOCATION \
              --scim-usage=enabled-for-groups
        

Replace the following: 

  * `PROVIDER_ID`: the ID of the workforce identity pool provider
  * `WORKFORCE_POOL_ID`: the ID of the workforce pool
  * `LOCATION`: the location of the workforce pool



### Enable SCIM for users and groups (Looker) ([Preview](https://cloud.google.com/products#product-launch-stages))

#### OIDC
    
    
          gcloud iam workforce-pools providers update-oidc PROVIDER_ID \
              --workforce-pool=WORKFORCE_POOL_ID \
              --location=LOCATION \
              --scim-usage=enabled-for-users-groups
        

Replace the following: 

  * `PROVIDER_ID`: the ID of the workforce identity pool provider
  * `WORKFORCE_POOL_ID`: the ID of the workforce pool
  * `LOCATION`: the location of the workforce pool



#### SAML
    
    
          gcloud iam workforce-pools providers update-saml PROVIDER_ID \
              --workforce-pool=WORKFORCE_POOL_ID \
              --location=LOCATION \
              --scim-usage=enabled-for-users-groups
        

Replace the following: 

  * `PROVIDER_ID`: the ID of the workforce identity pool provider
  * `WORKFORCE_POOL_ID`: the ID of the workforce pool
  * `LOCATION`: the location of the workforce pool



To verify SCIM synchronization, see Verify SCIM synchronization.

## Claim mapping

When you configure SCIM, you define claim mappings (`--claim-mapping`) in the SCIM tenant to map SCIM user and group attributes to Google attributes. 

### Supported Google Cloud attributes for claim mapping

The following table lists the Google Cloud attributes that you can map in your SCIM tenant (`--claim-mapping`) using Common Expression Language (CEL): 

Google Cloud attribute | Requirement | Description | Supported expressions and limits  
---|---|---|---  
`google.subject` | Mandatory |  Unique identifier for the authenticating user. The underlying IdP attribute used to populate `google.subject` must be identical across both the provider mapping (`--attribute-mapping`) and the SCIM tenant (`--claim-mapping`). If these mappings are inconsistent, users might be able to sign in but won't be recognized as members of SCIM-provisioned groups. | Restricted to the following base expressions (or with `.lowerAscii()`): 

  * `user.externalId`
  * `user.userName`
  * `user.emails[0].value`

Maximum length: 127 bytes. **Note:** This mapping is immutable once the SCIM tenant is created; to update it, you must hard-delete and recreate the SCIM tenant.  
`google.group` | Mandatory for SCIM groups | Unique identifier for group membership synced using SCIM. | Restricted to the following base expressions (or with `.lowerAscii()`): 

  * `group.externalId`
  * `group.displayName`

**Note:** This mapping is immutable once the SCIM tenant is created; to update it, you must hard-delete and recreate the SCIM tenant.  
`google.display_name` | Optional | An attribute that sets the name of the signed-in user in the Google Cloud console. It can't be used in IAM allow policies. | Maps to a string attribute (such as `user.displayName` or `user.name.formatted`). Maximum length: 100 bytes.  
`google.profile_photo` | Optional | A URL of the user's thumbnail photo that is visible as their profile picture in the Google Cloud console. It can't be used in IAM allow policies. | Must evaluate to a valid URL string (such as `user.photos.filter(p, p.type == 'thumbnail')[0].value` or `user.photos[0].value`).  
`google.email` | Optional | An attribute used to map email addresses from the IdP to products integrated by using Workforce Identity Federation OAuth client integration. It can't be used in IAM allow policies. | Maps to an email attribute (such as `user.emails.filter(e, e.type == 'work')[0].value` or `user.emails[0].value`).  
`google.posix_username` | Optional | A unique POSIX-compliant username string used for SSH-in-browser and OS Login with Workforce Identity Federation. This attribute can't be used in IAM allow policies. | The maximum length is 32 characters.  
`attribute.KEY` | Optional |  Custom attributes from your IdP that you can use to define your authorization strategy in an IAM allow policy. Replace KEY with the attribute name you want to use. For example, you can define a custom attribute such as `costcenter = "1234"` and refer to it by using `principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workforcePools/WORKFORCE_POOL_ID/attribute.costcenter/1234`. Granting access to this principal identifier gives access to all identities configured in the IdP with that cost center. | Up to 50 custom attribute mapping rules. Maximum size per rule: 256 characters.  
  
### Example mappings for subject consistency

As described in Supported attributes for claim mapping, the underlying IdP attribute used to populate `google.subject` must be identical across both the provider mapping (`--attribute-mapping`) and the SCIM tenant (`--claim-mapping`). The following table shows reference examples for Okta: 

Google attribute | Workforce identity pool provider mapping | SCIM tenant mapping  
---|---|---  
`google.subject` | `assertion.sub` | `user.externalId`  
`google.subject` | `assertion.subject` | `user.userName`  
`google.subject` | `assertion.subject.lowerAscii()` | `user.userName.lowerAscii()`  
`google.subject` | `assertion.preferred_username` | `user.userName`  
`google.subject` | `assertion.preferred_username.lowerAscii()` | `user.userName.lowerAscii()`  
`google.subject` | `assertion.email` | `user.emails[0].value`  
`google.subject` | `assertion.email.lowerAscii()` | `user.emails[0].value.lowerAscii()`  
  
## Verify SCIM synchronization

**Important:** Because SCIM is push-based from your IdP, Google Cloud doesn't actively pull data or check connection health. If the connection between your IdP and Google Cloud breaks silently, identity data can become stale. 

In extended session length (ESL) workflows lasting up to 90 days, a deactivated user might retain access until the next successful sync or session expiration. To prevent unauthorized access, continuously monitor and audit your SCIM synchronization health. 

After configuring SCIM, you can use `curl` to query the IAM SCIM service endpoint (`iamscim.googleapis.com`) and verify that users and groups are syncing to Google Cloud. These commands require a valid SCIM token and your SCIM tenant UID. The `iamscim.googleapis.com` service implements the [SCIM 2.0 protocol (RFC 7644)](https://datatracker.ietf.org/doc/html/rfc7644). For details about supported endpoints, query filters, and limitations, see [Supported and unsupported endpoints](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim#endpoints) and [Protocol feature limitations](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim#protocol-limitations). 

### Verify user sync

To verify that a user synced correctly, search for the user's `userName` by using the following filter:
    
    
    curl -H "Authorization: Bearer SCIM_TOKEN" \
      "https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Users?filter=userName%20eq%20%22USER_NAME%22"

Example response:
    
    
    {
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
      "totalResults": 1,
      "Resources": [
        {
          "id": "USER_ID",
          "userName": "USER_NAME",
          ...
        }
      ]
    }
    

### Verify group sync

To verify that a group synced correctly, search for the group's `displayName` by using the following filter:
    
    
    curl -H "Authorization: Bearer SCIM_TOKEN" \
      "https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Groups?filter=displayName%20eq%20%22GROUP_NAME%22"

Example response:
    
    
    {
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
      "totalResults": 1,
      "Resources": [
        {
          "id": "GROUP_ID",
          "displayName": "GROUP_NAME",
          ...
        }
      ]
    }
    

### Verify group membership

To verify if a specific user is a member of a group, use a filter that specifies both the group ID and the user ID.
    
    
    curl -H "Authorization: Bearer SCIM_TOKEN" \
      "https://iamscim.googleapis.com/v1alpha1/tenants/SCIM_TENANT_UID/Groups?filter=id%20eq%20%22GROUP_ID%22%20and%20members%20eq%20%22USER_ID%22"

Example response if the user is a member:
    
    
    {
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
      "totalResults": 1,
      "Resources": [
        {
          "id": "GROUP_ID",
          "displayName": "GROUP_NAME",
          ...
        }
      ]
    }
    

Example response if the user is not a member:
    
    
    {
      "schemas": ["urn:ietf:params:scim:api:messages:2.0:ListResponse"],
      "totalResults": 0,
      "Resources": []
    }
    

**Note:** To obtain the `GROUP_ID` and `USER_ID`, first find the group and user using the `displayName` and `userName` filters. The IDs are returned in the `id` field of the response. Replace `SCIM_TOKEN`, `SCIM_TENANT_UID`, `USER_NAME`, `GROUP_NAME`, `GROUP_ID`, and `USER_ID` with your actual values. 

## Force delete a SCIM tenant

To force delete a SCIM tenant, do the following:

  1. If `--scim-usage=enabled-for-groups` or `--scim-usage=enabled-for-users-groups` is set for your provider, disable it from the provider configuration:

### OIDC
         
         gcloud iam workforce-pools providers update-oidc PROVIDER_ID \
             --workforce-pool=WORKFORCE_POOL_ID \
             --location=LOCATION \
             --scim-usage=SCIM_USAGE_UNSPECIFIED
         

Replace the following: 

     * `PROVIDER_ID`: the ID of the workforce identity pool provider
     * `WORKFORCE_POOL_ID`: the ID of the workforce pool
     * `LOCATION`: the location of the workforce pool

### SAML
    
    gcloud iam workforce-pools providers update-saml PROVIDER_ID \
        --workforce-pool=WORKFORCE_POOL_ID \
        --location=LOCATION \
        --scim-usage=SCIM_USAGE_UNSPECIFIED
    

Replace the following: 

     * `PROVIDER_ID`: the ID of the workforce identity pool provider
     * `WORKFORCE_POOL_ID`: the ID of the workforce pool
     * `LOCATION`: the location of the workforce pool
  2. Delete the SCIM tenant: 
         
         gcloud iam workforce-pools providers scim-tenants delete SCIM_TENANT_ID \
             --workforce-pool=WORKFORCE_POOL_ID \
             --provider=PROVIDER_ID \
             --hard-delete \
             --location=global
         

Replace the following: 

     * `SCIM_TENANT_ID`: the ID of the SCIM tenant to delete
     * `WORKFORCE_POOL_ID`: the ID of the workforce pool
     * `PROVIDER_ID`: the ID of the workforce identity pool provider
To learn more about SCIM, including deleting SCIM tenants, see [SCIM support](https://docs.cloud.google.com/iam/docs/workforce-identity-federation-scim). 



## What's next

  * [Troubleshoot SCIM provisioning](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#scim-provisioning-errors)
  * [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data)
  * [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions)
  * Learn which Google Cloud products [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services)
  * [Set up user access to console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
