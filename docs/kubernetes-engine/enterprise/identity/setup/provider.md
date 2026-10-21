---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider/
title: Configure OIDC providers to authenticate to clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:27:47.462722+00:00
---

# Configure OIDC providers to authenticate to clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/provider/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Configure OIDC providers to authenticate to clusters Stay organized with collections  Save and categorize content based on your preferences. 

This document is for **platform administrators** , or whoever manages identity setup in your organization. It explains how to configure your chosen [OpenID Connect (OIDC)](https://openid.net/connect/) identity provider for authentication to Kubernetes clusters that aren't on Google Cloud.

## Register a client application with your provider

During the authentication flow for users, the cluster uses a _client ID_ and _secret_ to connect to your identity provider. You can get a client ID and a secret from your identity provider by configuring a client application for Kubernetes. The procedure to set up a client application depends on your provider. You can find some specific registration details for popular providers in the next section.

For redirect URLs, specify the following values:

  * `https://console.cloud.google.com/kubernetes/oidc` is the redirect URL for the Google Cloud console.
  * `http://localhost:PORT/callback` is the redirect URL for the gcloud CLI. You can specify any port number that is higher than 1024.
  * `APISERVER_URL:11001/finish-login` is the redirect URL if you choose to [authenticate using FQDN access](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access#alternativeuserloginaccess). Replace `APISERVER_URL` with the FQDN of the cluster's Kubernetes API server. For example, if the `APISERVER_URL` is `https://apiserver.company.com`, then the `redirect_uri` should be `https://apiserver.company.com:11001/finish-login`.



Save the client ID and secret you get from the registration step. Share these details with cluster administrators who need to set up their clusters.

### Identity provider setup information

This section provides steps for registering a client application with Microsoft Active Directory Federation Services (AD FS) or with Microsoft Entra ID.

### Microsoft AD FS

Use a set of AD FS management wizards to configure your AD FS server and AD user database.

  1. Open the AD FS management pane.

  2. Select **Application Groups** > **Actions** > **Add an Application Group**.

  3. Select **Server Application**. Enter a name and description of your choice. Click **Next**.

  4. Enter your two redirect URLs, as specified above. You are given a client ID. AD FS identifies the cluster by using this client ID. Save the client ID for later.

  5. Select **Generate a shared secret**. The Kubernetes authentication mechanism uses this secret to authenticate to the AD FS server. Save the secret for later.




#### Configuring security groups (optional)

  1. In AD FS management, select **Relying party trusts** > **Add a new relying party trust**.

  2. Select **Claims aware** , and click **Start**.

  3. Select **Enter data about relying party manually**.

  4. Enter a display name.

  5. Skip the next two steps.

  6. Enter a Relying party trust identifier. Suggestion: `token-groups-claim`.

  7. For **Access control policy** , select **Permit everyone**. This means that all users share their security group information with the gcloud CLI and Google Cloud console.

  8. Click **Finish**.




#### Mapping LDAP attributes to claim names

  1. In AD FS management, select **Relying party trusts** > **Edit claim issuance policy**.

  2. Select **Send LDAP Attributes as Claims** , and click **Next**.

  3. For **Claim rule name** , enter `groups`.

  4. For **Attribute store** , select **Active Directory**.

  5. In the table, for **LDAP Attribute** , select:

     * AD FS version 5.0 and later: **Token-Groups Qualified by Domain name**
     * AD FS versions before 5.0: **Token Groups - Qualified Names**
  6. For **Outgoing Claim Type** , select:

     * AD FS version 5.0 and later: **Group**
     * AD FS versions before 5.0: **groups**
  7. Click **Finish** , and click **Apply**.




#### Registering the Kubernetes client application with AD FS

Open a PowerShell window in Administrator mode, and enter this command:
    
    
    Grant-AD FSApplicationPermission `
      -ClientRoleIdentifier "[CLIENT_ID]" `
     -ServerRoleIdentifier [SERVER_ROLE_IDENTIFIER] `
      -ScopeName "allatclaims", "openid"
    

Replace the following:

  * [CLIENT_ID] is the client ID that you obtained previously.

  * [SERVER_ROLE_IDENTIFIER] is the claim identifier you entered previously. Recall that the suggested identifier was `token-groups-claim`.




### Microsoft Entra ID

To register an OAuth client with Microsoft Entra ID, complete the steps at the following links:

  1. If you haven't done so already, [Set up a Microsoft Entra tenant](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-create-new-tenant).

  2. [Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

  3. In the Microsoft Entra admin center, open the **App registrations** page and select your application. The application overview page opens.

  4. Create a client secret:

     1. In the navigation menu, click **Certificates & Secrets**.
     2. Click the **Client secrets** tab.
     3. Click **New client secret**. Name your secret and click **Add**.
     4. Save the **Value** of the secret in a secure location. You will not be able to retrieve it after you close or refresh the page.

For more information, see [Add and manage application credentials in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials).

  5. Add redirect URIs:

     1. In the navigation menu, click **Authentication**.
     2. In the **Platform configurations** section, click **Add a platform**. The **Configure platforms** pane opens.
     3. Click **Web**.
     4. In the **Redirect URIs** field, enter `http://localhost:PORT/callback` for the gcloud CLI login flow. Pick a PORT greater than 1024.
     5. Click **Configure**.
     6. Click **Add URI** to add another URI.
     7. Enter `https://console.cloud.google.com/kubernetes/oidc` for the Google Cloud console login flow.
     8. Save your configuration.

For more information, see [How to add a redirect URI to your application](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-redirect-uri).




Now your client registration is complete. You should have the following info to share with your cluster administrator:

  * **Issuer URI** : `https://login.microsoftonline.com/TENANT_ID/v2.0`. The tenant ID is displayed as the `Directory (tenant) ID` in the application overview page in the Microsoft Entra admin center.

  * **Client ID** : The client ID is displayed as the `Application (client) ID` in the application overview page in the Microsoft Entra admin center.

  * **Client Secret** : The value of the client secret that you created when you registered the client application. If you don't have access to this value, generate a new secret.




### Advanced setup for Microsoft Entra ID

Consider using this advanced setup only when you want to set up clusters with Microsoft Entra ID group-based authorization policies where users of the clusters belong to more than 200 Microsoft Entra ID groups. The advanced setup for Microsoft Entra ID supports the following platforms:

  * On-premises Google Distributed Cloud (both VMware and bare metal): From version 1.14
  * GKE on AWS: From version 1.14 (Kubernetes version of 1.25 or later)
  * GKE on Azure: From version 1.14 (Kubernetes version of 1.25 or later)



Before you begin, make sure that each user has an associated email address configured as their identifier in Microsoft Entra ID. This email address is used to assert the user's identity and authenticate the request.

You need to ensure that the client you 'registered in the previous section has delegated permissions to get user and group information from the Microsoft Graph API. These permissions let the Kubernetes authentication mechanism access the Microsoft Graph API endpoints from which group information is fetched. Without this step, the cluster can't get group information for the user, which causes RBAC authorization policies based on groups to not work as expected.

You need to have global admin or organization admin permissions to perform this setup step.

  1. Sign in to the Microsoft Entra admin center.
  2. Select the Microsoft Entra tenant that has your client application.
  3. Select **App registrations** , and then select your client application.
  4. Select **API permissions - Add a permission - Microsoft Graph - Delegated permissions**.
  5. Under the **Group** tab, check **Group.Read.All**. Under the **User** tab, check **User.Read.All**.
  6. Click **Add permissions** to complete the process.
  7. Grant consent on behalf of all users by clicking **Grant admin consent for...**. For more information, see [More on API permissions and admin consent](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#more-on-api-permissions-and-admin-consent).



## Share the identity provider details

Share the following provider information with your cluster administrator for cluster setup:

  * The provider's issuer URI
  * The client secret
  * The client ID
  * The redirect URI and port you specified for the gcloud CLI
  * The user name field (claim) that your provider uses to identify users in its tokens (the assumed default when configuring clusters is `sub`)
  * The group name field (claim) that your provider uses to return security groups, if any.
  * Any additional scopes or parameters that are specific to your provider, as described in the previous section. For example, if your authorization server prompts for consent for authentication with Microsoft Entra ID and Okta, the cluster admin needs to specify `prompt=consent` as a parameter. If you have configured AD FS to provide security group information, the relevant additional parameter is `resource=token-groups-claim` (or whatever you chose as your relying party trust identifier).
  * (Optional) If your provider is not using a certificate signed by a public certificate authority (for example if you are using self-signed certificates), then you will need a certificate (or certificate chain) of the identity provider. The certificate (or certificate chain) needs to contain the root certificate at a minimum (partial chains are accepted, as long as the chain is contiguous back to the root certificate). When providing this value in ClientConfig, it needs to be formatted as a base64 encoded string. To create the string, concatenate the complete PEM-encoded certificate(s) into a single string and then base64 encode it.



For more information about the configuration parameters for clusters, see [Configure clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure_clusters).

## What's next

  * [Configure authentication for individual clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster)
  * [Configure authentication for your fleet](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
