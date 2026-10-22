---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider/
title: Configuring the identity provider \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:39.607457+00:00
---

# Configuring the identity provider  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring the identity provider Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

For integrated portals, you can define identity providers to support the authentication types defined in the following table.

Authentication type | Description  
---|---  
Built-in | Requires users to pass their credentials (username and password) to the integrated portal for authentication. When you create a new portal, the built-in identity provider is configured and enabled.  To understand the sign-in experience from the user perspective, see [Signing in to the portal using user credentials (built-in provider)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#built-in).  
SAML (Preview) | Security assertion markup language (SAML) is a standard protocol for single sign-on (SSO) environment. SSO authentication using SAML enables users to log in to your Apigee integrated portals without having to create new accounts. Users log in using their centrally managed account credentials.  To understand the sign in experience from the user perspective, see [Signing in to the portal using SAML authentication (Preview)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#saml-auth).  
  
## Benefits of SAML authentication for integrated portals

Configuring SAML as an identity provider for an integrated portal offers the following benefits:

  * **Set up your developer program once and re-use it across multiple integrated portals.** Choose your developer program when creating your integrated portal. Easily update or change the developer program as requirements evolve.
  * **Take full control of user management** Connect your company SAML server to the integrated portal. When users leave your organization and are deprovisioned centrally, they will no longer be able to authenticate with your SSO service to use the integrated portal.



## Configuring the built-in identity provider

Configure the built-in identity provider, as described in the following sections.

### Accessing the Built-in Identity Provider page

To access the built-in identity provider:

  1. Open the Portals page.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.  
  
[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to view the identity provider.

  3. Click **Accounts**.

  4. Click the **Authentication** tab.

  5. In the **Identity providers** section, click the **Built-in** provider type.

  6. Configure the built-in identity provider, as described in the following sections:

     * Enabling the built-in identity provider
     * Restricting portal registration by email address or domain
     * Configuring email notifications



### Enabling the built-in identity provider

To enable the built-in identity provider:

  1. Access the Built-in Identity Provider page.
  2. Open the editor. Click edit **Edit**.

  3. Select the **Enabled** checkbox to enable the identity provider. To disable the built-in identity provider, clear the checkbox.

**Note:** At least one identity provider must be enabled to allow users to sign in.
  4. Click **Save**.




### Restricting portal registration by email address or domain

Restrict portal registration by identifying the individual email addresses (`developer@some-company.com`) or email domains (`some-company.com`, without the leading `@`) that can create accounts on your portal.

To match all nested subdomains, prepend the `*.` wildcard string to a domain or subdomain. For example, `*.example.com` will match `test@example.com`, `test@dev.example.com`, and so on.

If left blank, any email address can be used to register on the portal.

**Notes:**

  * When users create an account, as described in [Creating a user account on the integrated portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register), if the email address is allowed access, a confirmation email is sent with a link to complete the registration process. 
  * Users with existing accounts, created before the restriction was configured, will continue to be able to sign in to the portal (regardless of whether their email or email domain are given access). 
  * Email address and domain values are case-insensitive. 
  * See also [ Configuring manual activation of user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#manual-approval). 



To restrict portal registration by email address or domain:

  1. [Access the Built-in Identity Provider page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#access).
  2. Add one or more email addresses.

     1. Click edit **Edit**.
     2. Click **\+ Add email**.
     3. Enter an email address or email domain that you want to allow to register and sign in to the portal.
     4. Add additional entries, as required.
     5. To delete an entry, click delete **Delete** adjacent to the entry.
  3. Click **Save**.




### Configuring email notifications

**Note:** Apigee recommends that you configure the SMTP server for the email notifications originating from the portal. See [Configure an SMTP server](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-email#smtp).

For the built-in provider, you can enable and configure the following email notifications:

Email notification | Recipient | Trigger | Description  
---|---|---|---  
Account Notify| API provider| Portal user creates a new account| If you [configured your portal to require manual activation of user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#configure_manual_activation_of_user_accounts), you need to [manually activate the user account](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users#activate_user_account) before the portal user can sign in. **Notes:**

  * Ensure that you [configure notifications for new user account registration](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#configuring_notifications_for_new_user_account_registration).
  * For the Preview release, the portal user is given no indication that their account must be manually activated before they can sign in. It is recommended that if you configure manual activation, you expedite the activation of new user accounts.

  
Account Verify| Portal user| Portal user creates a new account| Provides a secure link to verify account creation. The link expires in 10 minutes.   
  
When configuring the email notifications:

  * Use HTML tags to format the text. Be sure to send a test email to validate the formatting appears as expected.
  * You can insert one or more of the following variables which will be substituted when the email notification is sent.

Variable | Description  
---|---  
`{``{firstName}``}` | First name  
`{``{lastName}``}` | Last name  
`{``{email}``}` | Email address  
`{``{siteurl}``}` | Link to the live portal  
`{``{verifylink}``}` | Link used for account verification  



To configure email notifications:

  1. Access the Built-in Identity Provider page.
  2. Configure email notifications.

Click edit **Edit**.

  3. Edit the **Subject** and **Body** fields.

  4. Click **Save**.




## Configuring the SAML identity provider (Preview)

**Note:** This is the **Preview release of the SAML identity provider**. 

Configure the SAML identity provider, as described in the following sections.

**Caution:** Identity provider-initiated sign-in flows carry a security risk (for example, risk of a login CSRF or DDOS attack) and are not supported. Apigee recommends using the integrated portal-initiated sign-in flow, where users click **Sign In** on the integrated portal to initiate authentication.

### Accessing the SAML Identity Provider page

To access the SAML identity provider:

  1. Open the Portals page.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.  
  
[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to view the identity provider.

  3. Click **Accounts**.

  4. Click the **Authentication** tab.

  5. In the **Identity providers** section, click the **SAML** provider type.

  6. Configure the SAML identity provider, as described in the following sections:

     * Enable the SAML identity provider
     * Configure SAML settings
     * Configure custom user attributes for the SAML identity provider
     * Upload a new certificate



### Enabling the SAML identity provider

To enable the SAML identity provider:

  1. [Access the SAML Identity Provider page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#access-saml).
  2. Open the editor. Click edit **Edit**.

  3. Select the **Enabled** checkbox to enable the identity provider.

To disable the SAML identity provider, clear the checkbox.

**Note:** At least one identity provider must be enabled to allow users to sign in. 
  4. Click **Save**.

  5. If you have configured a custom domain, see Using a custom domain with the SAML identity provider.




### Configuring SAML settings

To configure the SAML settings:

  1. [Access the SAML Identity Provider page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#access-saml).
  2. Open the editor. Click edit **Edit**.

  3. Click **Copy** adjacent to the **SP metadata URL**.

**Note:** The SAML identity provider must be enabled in order for the SP metadata URL to be populated.
  4. Configure your SAML identity provider using the information in the service provider (SP) metadata file.

For some SAML identity providers, you will be prompted only for the metadata URL. For others, you will need to extract specific information from the metadata file and enter it into a form.  
  
In the latter case, paste the URL into a browser to download the SP metadata file and extract the required information. For example, the entity ID or sign-in URL can be extracted from the following elements in the SP metadata file:

**Note:** In the SP metadata file, the sign-in URL is referred to as the `AssertionConsumerService` (ACS) URL. 
     * `<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" ID="diyyaumzqchrbui-a5vnmu1sp8qzekbd.apigee-saml-login" entityID="**diyyaumzqchrbui-a5vnmu1sp8qzekbd.apigee-saml-login** ">`
     * `<md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="**https://diyyaumzqchrbui-a5vnmu1sp8qzekbd.portal-login.apigee.com/saml/SSO/alias/diyyaumzqchrbui-a5vnmu1sp8qzekbd.apigee-saml-login** " index="0" isDefault="true"/>`
  5. Configure the SAML settings for the **identity provider**.

In the **SAML Settings** section, edit the following values _obtained from your SAML identity provider metadata file_ :

SAML setting| Description  
---|---  
Sign-in URL| URL to which users are redirected to sign-in to the SAML identity provider.  
For example: `https://dev-431871.oktapreview.com/app/googledev431871_devportalsaml_1/exkhgdyponHIp97po0h7/sso/saml`  
Sign-out URL| URL to which users are redirected to sign-out of the SAML identity provider.  
Leave this field **blank** if:
     * Your SAML identity provider does not provide a sign-out URL
     * You do not want users to be signed out of your SAML identity provider when they sign out of the integrated portal
     * You want to enable a custom domain (refer to the [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues#saml))
**Note:** This field is deprecated and will be removed in a future release.  
IDP entity ID| Unique ID for the SAML identity provider.  
For example: `http://www.okta.com/exkhgdyponHIp97po0h7`  
  6. Click **Save**.




### Configuring custom user attributes for the SAML identity provider

To ensure proper mapping between the SAML identity provider and [portal user accounts](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users), it is recommended that you create and configure the custom user attributes defined in the following table for your SAML identity provider. Set the value of each custom attribute to the corresponding user attribute defined by your SAML identity provider (for example, Okta).

**Note:** Custom attribute mapping is limited to the three attributes defined in the following table. Full support for custom attribute mapping is not available at this time.Custom attribute | Example (Okta)  
---|---  
`first_name` | `user.firstName`  
`last_name` | `user.lastName`  
`email` | `user.email`  
**Note:** In addition, ensure that the `NameID` attribute is mapped to the user's email address, which serves as the unique identifier of the portal user account.

The following shows how to configure custom user attributes and the `NameID` attribute using Okta as your third-party SAML identity provider.

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/okta-custom-attributes.png)

### Using a custom domain with the SAML identity provider

After you configure and enable the SAML identity provider, you can configure a custom domain (such as, `developers.example.com`), as described in [Customize your domain](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain).

It is important to keep the configuration settings in sync between the custom domain and SAML identity provider. If the configuration settings get out of sync, you may experience issues during authorization. For example, the authorization request sent to the SAML identity provider may have an `AssertionConsumerServiceURL` that is not defined using the custom domain.

To keep the configuration settings in sync between the custom domain and SAML identity provider:

  * If you configure or update the custom domain **after** you enable and configure the SAML identity provider, save the custom domain configuration and ensure it is enabled. Wait approximately 30 minutes for the cache to invalidate, then re-configure your SAML identity provider using the updated information in the service provider (SP) metadata file, as described in [Configure SAML settings](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#configure_saml_settings). You should see your custom domain in the SP Metadata.

  * If you configure a custom domain **before** you configure and enable the SAML identity provider, you need to reset the custom domain (described below) to ensure that the SAML identity provider is configured correctly.

  * If you need to reset (disable and re-enable) the SAML identity provider, as described in Enable the SAML identity provider, you must also Reset the custom domain (described below).




#### Resetting the custom domain

To reset (disable and enable) the custom domain:

  1. Open the Portals page.

In the Apigee in Cloud console, go to the **Distribution > Portals** page.  
  
[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click your portal.

  3. Click **Settings**.

  4. Click the **Domains** tab.

  5. Click **Disable** to disable the custom domain.

  6. Click **Enable** to enable the custom domain.




For more information, see [Customizing your domain](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain).

### Uploading a new certificate

To upload a new certificate:

  1. Download the certificate from your SAML identity provider. **Note:** The certificate must be in PEM or PKCSS format. If necessary, convert an x509 certificate to PEM format.

  2. Access the SAML Identity Provider page.

  3. Open the editor. Click edit **Edit**.

  4. Click **Browse** and navigate to the certificate in your local directory.

  5. Click **Open** to upload the new certificate. The Certificate information fields are updated to reflect the selected certificate.

  6. Verify that the certificate is valid and has not expired.

  7. Click **Save**.




### Converting an x509 certificate to PEM format

If you download an x509 certificate, you need to convert it to PEM format.

To convert an x509 certificate to PEM format:

  1. Copy the contents of the `ds:X509Certificate element` from the SAML identity provider metadata file and paste it into your favorite text editor.
  2. Add the following line at the top of the file: `-----BEGIN CERTIFICATE-----`
  3. Add the following line at the bottom of the file: `-----END CERTIFICATE-----`
  4. Save the file using a `.pem` extension.



The following provides an example of the PEM file contents:
    
    
    -----BEGIN CERTIFICATE-----
    MIICMzCCAZygAwIBAgIJALiPnVsvq8dsMA0GCSqGSIb3DQEBBQUAMFMxCzAJBgNV
    BAYTAlVTMQwwCgYDVQQIEwNmb28xDDAKBgNVBAcTA2ZvbzEMMAoGA1UEChMDZm9v
    MQwwCgYDVQQLEwNmb28xDDAKBgNVBAMTA2ZvbzAeFw0xMzAzMTkxNTQwMTlaFw0x
    ODAzMTgxNTQwMTlaMFMxCzAJBgNVBAYTAlVTMQwwCgYDVQQIEwNmb28xDDAKBgNV
    BAcTA2ZvbzEMMAoGA1UEChMDZm9vMQwwCgYDVQQLEwNmb28xDDAKBgNVBAMTA2Zv
    bzCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEAzdGfxi9CNbMf1UUcvDQh7MYB
    OveIHyc0E0KIbhjK5FkCBU4CiZrbfHagaW7ZEcN0tt3EvpbOMxxc/ZQU2WN/s/wP
    xph0pSfsfFsTKM4RhTWD2v4fgk+xZiKd1p0+L4hTtpwnEw0uXRVd0ki6muwV5y/P
    +5FHUeldq+pgTcgzuK8CAwEAAaMPMA0wCwYDVR0PBAQDAgLkMA0GCSqGSIb3DQEB
    BQUAA4GBAJiDAAtY0mQQeuxWdzLRzXmjvdSuL9GoyT3BF/jSnpxz5/58dba8pWen
    v3pj4P3w5DoOso0rzkZy2jEsEitlVM2mLSbQpMM+MUVQCQoiG6W9xuCFuxSrwPIS
    pAqEAuV4DNoxQKKWmhVv+J0ptMWD25Pnpxeq5sXzghfJnslJlQND
    -----END CERTIFICATE-----
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
