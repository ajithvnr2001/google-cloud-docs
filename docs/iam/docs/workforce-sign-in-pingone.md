---
url: https://docs.cloud.google.com/iam/docs/workforce-sign-in-pingone/
title: Configure Workforce Identity Federation with PingOne AIC \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:37.325126+00:00
---

# Configure Workforce Identity Federation with PingOne AIC  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-sign-in-pingone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Configure Workforce Identity Federation with PingOne AIC Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to configure Workforce Identity Federation with PingOne Advanced Identity Cloud (AIC) as an identity provider (IdP) and manage access to Google Cloud. After you configure the PingOne AIC IdP, federated users can access Google Cloud services that [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) by using the SAML 2.0 protocol.

## Before you begin

  1. Make sure that you set up a Google Cloud organization.
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. For sign-in, your IdP must provide signed authentication information: SAML IdP responses must be signed.
  4. To receive important information about changes to your organization or Google Cloud products, you must provide [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). For more information, see the [Workforce Identity Federation overview](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#essential-contacts).



## Costs

Workforce Identity Federation is available as a no-cost feature. However, Workforce Identity Federation detailed audit logging uses Cloud Logging. To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs). 

## Required roles

To get the permissions that you need to configure Workforce Identity Federation, ask your administrator to grant you the [IAM Workforce Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) (`roles/iam.workforcePoolAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

If you configure permissions in a development or test environment—but not in a production environment—you can grant the Identity and Access Management (IAM) Owner (`roles/owner`) basic role. This role also includes permissions for Workforce Identity Federation.

## Create a workforce identity pool

###  gcloud 

To create the workforce identity pool, run the following command:
    
    
    gcloud iam workforce-pools create WORKFORCE_POOL_ID \
        --organization=ORGANIZATION_ID \
        --display-name="DISPLAY_NAME" \
        --description="DESCRIPTION" \
        --session-duration=SESSION_DURATION \
        --location=global
    

Replace the following:

  * `WORKFORCE_POOL_ID`: an ID that you choose to represent your Google Cloud workforce pool. The pool ID must be globally unique across all workforce identity pools in Google Cloud. For information on formatting the ID, see the [Query parameters](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers/create#query-parameters) section in the API documentation.
  * `ORGANIZATION_ID`: the numeric organization ID of your Google Cloud organization for the workforce identity pool. Workforce identity pools are available across all projects and folders in the organization.
  * `DISPLAY_NAME`: Optional. A display name for your workforce identity pool.
  * `DESCRIPTION`: Optional. A workforce identity pool description.
  * `SESSION_DURATION`: Optional. The session duration, expressed as a number appended with `s`—for example, `3600s`. Session duration determines how long the Google Cloud access tokens, [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated) sign-in sessions, and gcloud CLI sign-in sessions from this workforce pool are valid. Session duration defaults to one hour (3600s). The session duration value must be between 15 minutes (900s) and 12 hours (43200s).

**Tip:** Run `gcloud iam workforce-pools create --help` to find other parameters you can customize for this command.

###  Console 

To create the workforce identity pool, do the following:

  1. In the Google Cloud console, go to the **Workforce Identity Pools** page:

[Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools?supportedpurview=organizationId)

  2. Select the organization for your workforce identity pool. Workforce identity pools are available across all projects and folders in an organization.

  3. Click **Create pool** and do the following:

     1. In the **Name** field, enter the display name of the pool. The pool ID is automatically derived from the name as you type, and it is displayed under the **Name** field. You can update the pool ID by clicking **Edit** next to the pool ID.

     2. Optional: In **Description** , enter a description of the pool.

     3. To create the workforce identity pool, click **Next**.




The workforce identity pool's session duration defaults to one hour (3600s). The session duration determines how long the Google Cloud access tokens, [console (federated)](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#console-federated), and gcloud CLI sign-in sessions from this workforce pool are valid. After you create the pool, you can [update the pool](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-pool) to set a custom session duration. The session duration must be from 15 minutes (900s) to 12 hours (43200s).

## Create a PingOne AIC application

This section shows you how to create a PingOne AIC _application integration_.

### Create a hosted IdP

  1. In **Native Consoles > Access Management**, go to **Realms > REALM_NAME > Dashboard**, and click **SAML Applications**.
  2. Click **Add Entity Provider > Hosted**.
  3. Enter an **Entity ID**. Record this value for later use.

**Note:** Advanced Identity Cloud truncates multiple spaces to a single space in values like entity IDs. For example, if **MyEntityID value** (one space) exists, adding a new entity named **My Entity ID** (multiple spaces) causes an error because Advanced Identity Cloud treats them as identical.
     1. Verify that the **Entity Provider Base URL** value is correct. Advanced Identity Cloud uses this value for all SAML 2.0 related endpoints.
     2. In the **Meta Aliases** section, provide a URL-friendly value in the **Identity Provider Meta Alias** property. This alias must be unique in the circle of trust.
     3. Click **Create**.
     4. On the **Assertion Processing** tab, in the **Attribute Mapper** section, map SAML attribute names to local attribute names. The SAML attribute names are the names that are used in an assertion.
     5. Click **Add** or **Update** for each mapping.
     6. Click **Save Changes**.



### Use attributes

This section describes how to use attributes from the SAML assertion.

In the following examples, attributes in the SAML assertion are mapped to local attributes:

SAML attribute | Local attribute  
---|---  
`IDPEmail` | `mail`  
`FirstName` | `givenName`  
`groups` | `groups`  
  
Set up the required attributes in the attribute mapping section. You will map these attributes when you create the workforce identity pool provider later in this guide.

### Export provider metadata

You can access the SAML 2.0 metadata for your hosted provider in one of the following ways:

  * **Over REST**

Run the following command:
        
        curl --output METADATA_XML \
            "https://TENANT_ENV_FQDN/am/ExportSamlMetadata?entityid=ENTITY_ID&realm=/REALM"
        

  * **In a browser**

Open your tenant environment's metadata URL in a browser to download the XML file: `https://TENANT_ENV_FQDN/am/ExportSamlMetadata?entityid=ENTITY_ID&realm=/REALM`



  1. Save the XML file to your local machine.



### Import Google as a remote SP

  1. Prepare the Google Cloud SP metadata XML. Use the following template, replacing the placeholder values:
         
         <?xml version="1.0" encoding="UTF-8"?>
         <md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" xmlns:ds="http://www.w3.org/2000/09/xmldsig#" entityID="https://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID">
            <md:SPSSODescriptor AuthnRequestsSigned="false" WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
               <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</md:NameIDFormat>
               <md:NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</md:NameIDFormat>
               <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://auth.cloud.google/signin-callback/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID" index="0" isDefault="true"/>
            </md:SPSSODescriptor>
         </md:EntityDescriptor>
         

  2. Import the metadata in one of the following ways:

     * **In the console**

       1. In the PingOne AIC admin console, navigate to **SAML Applications**.
       2. Click **Add Entity Provider > Remote**.
       3. Upload the Google Cloud SP metadata XML file you just created.
       4. Click **Create**.
     * **Over REST**

       1. Convert the XML metadata to a base64url-encoded string.
       2. [Get an access token](https://docs.pingidentity.com/pingoneaic/developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token).
       3. Run the following command:
              
              curl --request POST \
                  --header 'authorization: Bearer ACCESS_TOKEN' \
                  --header 'Content-Type: application/json' \
                  --header 'Accept-API-Version: resource=1.0' \
                  --data-raw '{"standardMetadata": "BASE64URL_ENCODED_METADATA"}' \
                  'https://TENANT_ENV_FQDN/am/json/realms/root/realms/alpha/realm-config/saml2/remote?_action=importEntity'
              




### Create a circle of trust (CoT)

  1. Navigate to **Realms > REALM_NAME > Applications > Federation > Circles of Trust**.
  2. Click **Add Circle of Trust**.
  3. Enter a name and click **Create**.
  4. On the **Circle of Trust** page, in the **Entity Providers** property, select your hosted IdP and the Google Cloud remote SP.
  5. Click **Save Changes**.



## Create the PingOne AIC workforce identity pool provider

This section describes how to create a [workforce identity pool provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-identity-pool-providers) to enable your IdP users to access Google Cloud. You can configure the provider to use the SAML protocol.

### Create a SAML workforce identity pool provider

  1. To create a SAML workforce identity pool provider, you want to ensure that your identity provider metadata includes at least the SAML entity ID, the single sign-on URL, and one signing public key. To do this, follow these steps:

### gcloud

     1. Save the SAML metadata from your PingOne AIC app.

     2. To create the SAML workforce identity pool provider, run the following command:
            
            gcloud iam workforce-pools providers create-saml WORKFORCE_PROVIDER_ID \
                --workforce-pool="WORKFORCE_POOL_ID" \
                --display-name="DISPLAY_NAME" \
                --description="DESCRIPTION" \
                --idp-metadata-path="XML_METADATA_PATH" \
                --attribute-mapping="ATTRIBUTE_MAPPING" \
                --attribute-condition="ATTRIBUTE_CONDITION" \
                --location=global
            

Replace the following:

        * `WORKFORCE_PROVIDER_ID`: a provider ID.
        * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
        * `DISPLAY_NAME`: a display name.
        * `DESCRIPTION`: a description.
        * `XML_METADATA_PATH`: the path to the XML-formatted metadata file you exported from PingOne AIC.
        * `ATTRIBUTE_MAPPING`: the [attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mappings); for example, `google.subject=assertion.subject,google.groups=assertion.attributes.groups,attribute.department=assertion.attributes.department[0]`.
        * `ATTRIBUTE_CONDITION`: an optional [attribute condition](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions); for example, to limit the `ipaddr` attribute to a certain IP range you can set the condition `assertion.ipaddr.startsWith('98.11.12.')`.

For more information, see [Attribute mapping](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-mapping).

This command assigns the `subject`, `groups`, and `department` in the SAML assertion to `google.subject`, `google.groups`, and `attribute.department` attributes, respectively. The attribute condition also ensures that only users within a certain IP range can sign in using this workforce provider.

### Console

To configure the SAML provider by using the Google Cloud console, do the following:

     1. In the Google Cloud console, go to the **Workforce Identity Pools** page: [Go to Workforce Identity Pools](https://console.cloud.google.com/iam-admin/workforce-identity-pools?supportedpurview=organizationId)
     2. In the **Workforce Identity Pools** table, select the pool for which you want to create the provider.
     3. In the **Providers** section, click **add Add Provider**.
     4. In the **Select a Provider vendor** list, select **Generic Identity Provider**.
     5. In **Select an authentication protocol** , select **SAML**.
     6. In the **Create a provider** section, do the following: 
        1. In **Name** , enter a name for the provider.
        2. Optional: In **Description** , enter a description for the provider.
        3. In **IDP metadata file (XML)** , select the metadata XML file you exported from PingOne AIC.
        4. To create a provider that is enabled, make sure **Enable provider** is on.
        5. Click **Continue**.
     7. In the **Share your provider information** section, click **Continue**.
     8. Optional: To turn on detailed audit logging, in the **Configure provider** section, in **Detailed logging** , click the **Enable attribute value audit logging** toggle. 

Workforce Identity Federation _detailed audit logging_ logs information received from your IdP to Logging. Detailed audit logging can help you troubleshoot your workforce identity pool provider configuration. To learn how to troubleshoot attribute mapping errors with detailed audit logging, see [General attribute mapping errors](https://docs.cloud.google.com/iam/docs/troubleshooting-workforce-identity-federation#general-attribute-mapping-errors). To learn about Logging pricing, see [Google Cloud Observability pricing](https://docs.cloud.google.com/stackdriver/pricing#logs-costs).

To disable detailed audit logging for a workforce identity pool provider, leave the **Enable attribute value audit logging** toggle off when you create the provider. To disable detailed audit logging, you can also [update the provider](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers#update-oidc-provider). 

     9. To create the provider, click **Submit**.

After the provider is created, you are redirected to the provider attributes page.

To configure attribute mappings and conditions, do the following:

     1. When prompted, sign in to your external IdP to validate the default attribute mappings.
     2. On the provider attributes page, view and edit the attribute mappings and conditions:

        1. To add or edit attribute mappings, do the following:

           1. Click **Add mapping** to add a new mapping, or edit the existing mappings.
           2. In the **Google _n_** field, where _n_ is a number, select a Google Cloud-supported key.
           3. In the corresponding **SAML _n_** field, enter the IdP attribute name or a CEL expression—for example:
                  
                  google.subject=assertion.subject,
                  google.groups=assertion.attributes['https://example.com/aliases'],
                  attribute.costcenter=assertion.attributes.costcenter[0]
                  

        2. To add an attribute condition, do the following: **Warning:** If your multi-tenant IdP has a single issuer URI, you must use [attribute conditions](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions) to ensure that access is restricted to the correct tenant. For more information, see [Use attribute conditions when federating with GitHub or other multi-tenant identity providers](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#use-attribute-conditions-multitenant). 

           1. Click **Add condition**.
           2. In the **Attribute Conditions** field, enter a condition in [CEL format](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#attribute-conditions)—for example, `assertion.attributes.ipaddr.startsWith('98.11.12.')`.
     3. To validate your mappings, click **Save and refetch token**.

     4. To complete the setup, click **Save and exit**.




## Manage access to Google Cloud resources

This section shows how to manage access to Google Cloud resources for PingOne AIC users.

The sample project used in this guide can be different from the project that you used to set up Workforce Identity Federation.

You can manage roles for single identities, a group of identities, or an entire pool. For more information, see [Workforce principal identifiers for allow policies](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation#representing-workforce-users).

### Use mapped department attributes

To grant the Storage Admin role (`roles/storage.admin`) to all identities within a specific department for the `TEST_PROJECT_ID` project, run the following command:
    
    
    gcloud projects add-iam-policy-binding TEST_PROJECT_ID \
        --role="roles/storage.admin" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/attribute.department/DEPARTMENT_VALUE"
    

Replace the following:

  * `TEST_PROJECT_ID`: the project ID.
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `DEPARTMENT_VALUE`: the mapped `attribute.department` value.



### Use mapped groups

To grant the Storage Admin role (`roles/storage.admin`) to all identities within the `GROUP_ID` group for the `TEST_PROJECT_ID` project, run the following command:
    
    
    gcloud projects add-iam-policy-binding TEST_PROJECT_ID \
        --role="roles/storage.admin" \
        --member="principalSet://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/group/GROUP_ID"
    

Replace the following:

  * `TEST_PROJECT_ID`: the project ID.
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `GROUP_ID`: a group in the mapped `google.groups` claim.



## Sign in and test access

In this section, you sign in as a workforce identity pool user and test your access.

### Sign in

###  console (federated) sign-in 

To sign in to the Google Cloud Workforce Identity Federation console, also known as the console (federated), do the following:

  1. Go to the console (federated) sign-in page.

[Go to console (federated)](https://auth.cloud.google/signin?continueUrl=https://console.cloud.google/)

  2. Enter the provider name, which is formatted as follows: 
         
         locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID

Enter your PingOne AIC credentials when prompted.


###  Google Cloud CLI browser-based sign-in 

To sign in to gcloud CLI using a browser-based sign-in flow:

Run the following command to create a login configuration file:

### Linux and macOS
    
    
    gcloud iam workforce-pools create-login-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --output-file=LOGIN_CONFIG_PATH

### Windows (PowerShell)
    
    
    gcloud iam workforce-pools create-login-config `
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID `
        --output-file=LOGIN_CONFIG_PATH

**Note:** You can optionally activate the login configuration file as the default for the gcloud CLI by adding the [ `--activate`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#--activate) flag. You can then run `gcloud auth login` to authorize the gcloud CLI without specifying the login configuration file path each time. 

Replace the following:

  * `WORKFORCE_POOL_ID`: The Workforce Identity Federation pool ID.
  * `WORKFORCE_PROVIDER_ID`: The Workforce Identity Federation provider ID.
  * `LOGIN_CONFIG_PATH`: The path to write the login configuration file to. For example, `login-config.json`. 



The login configuration file contains the endpoints used by the gcloud CLI to enable the browser-based authentication flow and set the audience to the IdP that was configured in the workforce identity pool provider. The file doesn't contain confidential information. 

The login configuration file content looks similar to the following:
    
    
    {
      "universe_domain": "googleapis.com",
      "universe_cloud_web_domain": "cloud.google",
      "type": "external_account_authorized_user_login_config",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "auth_url": "https://auth.cloud.google/authorize",
      "token_url": "https://sts.googleapis.com/v1/oauthtoken",
      "token_info_url": "https://sts.googleapis.com/v1/introspect"
    }

**Caution:** We recommend that you first ensure that the contents of this file are correct and then safeguard the file—for example, by making it read-only and restricting access with an ACL. The file isn't validated; a malicious actor with write access to this file can change the endpoints and intercept credentials. 

Point to the login configuration file with an environment variable, a property in the active gcloud CLI configuration, or use it directly with the `gcloud auth login` command: 

### Environment variable

To use the login configuration file with an environment variable, complete the following instructions: 

  1. Set the `CLOUDSDK_AUTH_LOGIN_CONFIG_FILE` environment variable to the path of the login configuration file. 
  2. Run the following command:
         
         gcloud auth login

  3. The gcloud CLI references the environment variable to find the login configuration file, and then starts the authentication process. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands. 



To stop using the login configuration file for `gcloud auth login` commands, clear the `CLOUDSDK_AUTH_LOGIN_CONFIG_FILE` environment variable. 

### gcloud CLI configuration

To use the login configuration file with a gcloud CLI configuration property, complete the following instructions: 

  1. Set the active gcloud CLI configuration's `auth/login_config_file` property to the login configuration file's path with the following command: 
         
         gcloud config set auth/login_config_file LOGIN_CONFIG_PATH

  2. Run the following command:
         
         gcloud auth login

  3. The gcloud CLI references the configuration property to find the login configuration file, and then starts the authentication process. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands. 



To stop using the login configuration file for `gcloud auth login` commands, unset the property with the following command: 
    
    
    gcloud config unset auth/login_config_file

### gcloud auth login

To use the login configuration file directly with the `gcloud auth login` command, complete the following instructions: 

  * If you used the `--activate` flag when you created the login configuration file, run the following command: 
        
        gcloud auth login

  * If you didn't use the `--activate` flag when you created the login configuration file, run the following command: 

### Linux and macOS
        
        gcloud auth login \
            --login-config=LOGIN_CONFIG_PATH

### Windows (PowerShell)
        
        gcloud auth login `
            --login-config=LOGIN_CONFIG_PATH

Replace LOGIN_CONFIG_PATH with the path of your login configuration file. 




The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 

###  gcloud CLI headless sign-in 

To sign in to PingOne AIC with the gcloud CLI using the SAML protocol, do the following:

  1. Sign in a user to your PingOne AIC application and get the SAML response.
  2. Save the SAML response returned by PingOne AIC in a secure location on your local machine. Store the path in an environment variable—for example: `SAML_ASSERTION_PATH=/tmp/saml_assertion.xml`.
  3. Generate a configuration file:
         
         gcloud iam workforce-pools create-cred-config \
             locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
             --subject-token-type=urn:ietf:params:oauth:token-type:saml2 \
             --credential-source-file=SAML_ASSERTION_PATH \
             --workforce-pool-user-project=PROJECT_ID \
             --output-file=config.json
         

Replace the following:

     * `SAML_ASSERTION_PATH`: the path of the SAML assertion file.
     * `PROJECT_ID`: the project ID.
  4. The configuration file that's generated looks similar to the following:
         
         {
           "type": "external_account",
           "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
           "subject_token_type": "urn:ietf:params:oauth:token-type:saml2",
           "token_url": "https://sts.googleapis.com/v1/token",
           "credential_source": {
             "file": "SAML_ASSERTION_PATH"
           },
           "workforce_pool_user_project": "PROJECT_ID"
         }
         

  5. To sign in to the gcloud CLI using token exchange, run the following command:
         
         gcloud auth login --cred-file=config.json
         

`gcloud` then transparently exchanges your PingOne AIC credentials for temporary Google Cloud access tokens, allowing you to make other `gcloud` calls to Google Cloud. The output is similar to the following:

`Authenticated with external account user credentials for: [principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/USER_ID].`

  6. To list the credentialed accounts and the active account, run the following command:
         
         gcloud auth list
         




### Test access

You can access the Google Cloud services that support Workforce Identity Federation that you're granted access to. Earlier in this guide, you granted the Storage Admin role to all identities within a specific department or group for project `TEST_PROJECT_ID`. You can test that you have access by listing Cloud Storage buckets.

###  console (federated) sign-in 

To verify your access in the console (federated), do the following:

  1. Go to the [Cloud Storage](https://console.cloud.google.com/storage) page.
  2. Verify that you can see the list of existing buckets for the project `TEST_PROJECT_ID`.



###  gcloud CLI 

To list Cloud Storage buckets and objects for the project that you have access to, run the following command:
    
    
    gcloud alpha storage ls --project="TEST_PROJECT_ID"
    

The principal must have the `serviceusage.services.use` permission on the project set in the gcloud CLI session: `PROJECT_ID`.

## What's next

  * [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data). 
  * [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 
  * Learn which Google Cloud products [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).
  * [Set up user access to console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
