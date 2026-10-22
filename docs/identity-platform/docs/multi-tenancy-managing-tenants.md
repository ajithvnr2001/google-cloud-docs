---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants/
title: Managing Identity Platform tenants programmatically \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:06.653520+00:00
---

# Managing Identity Platform tenants programmatically  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Managing Identity Platform tenants programmatically 

This document explains how to use the Identity Platform Admin SDK to manage tenants and their users programmatically. Some activities you can perform as an administrator include:

  * **User management** : Create, update, delete, and list users for a specific tenant.

  * **Identity verification:** Identify users of an app to restrict access to resources on your own server.

  * **Import users:** Migrate users from an external authentication system or another Identity Platform project or tenant.

  * **Access control with custom claims:** Define custom attributes on user accounts for a specific tenant and implement various access control strategies, such as role-based access control.

  * **User session management:** Revoke a user's refresh tokens for a specific tenant.

  * **Email action links:** Generate customized email links for password reset, email link sign-in, and email verification for users of a specific tenant.

  * **Tenant management:** Create, list, get, update, delete tenants for a specific Identity Platform project.

  * **Manage OIDC and SAML providers on tenants:** Programmatically manage OIDC and SAML configurations on a specified tenant.




## Before you begin

  * [Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk) for Node.js, Java, Python, Go, or C#.

  * [Enable multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart) for your Google Cloud project.




## Supported features

The following table lists the features supported by each SDK in a multi-tenant environment:

Feature | Node.js | Java | Python | Go | C#  
---|---|---|---|---|---  
Custom token minting  |  |  |  |  |   
Verifying ID tokens  |  |  |  |  |   
Managing users  |  |  |  |  |   
Controlling access with custom claims  |  |  |  |  |   
Revoking refresh tokens  |  |  |  |  |   
Importing users  |  |  |  |  |   
Generating email action links  |  |  |  |  |   
Multi-factor authentication  |  |  |  |  |   
Managing SAML/OIDC provider configurations  |  |  |  |  |   
Session cookie management  |  |  |  |  |   
  
The following table shows what sign-in methods you can configure using the Admin SDK and the Google Cloud console in a tenant-specific context:

Feature | Google Cloud console | Admin SDK  
---|---|---  
Email  |  |   
OIDC  |  |   
SAML  |  |   
Social  |  |   
Phone  |  |   
Multi-factor authentication  |  |   
Anonymous  |  |   
  
## Tenant management

Using the Admin SDK, you can manage tenants programmatically from a secure server environment instead of using the Google Cloud console. This includes the ability to create, list, get, modify, or delete tenants.

Each tenant contains its own identity providers, settings, and sets of users. Tenant configuration management operations (CRUD) are available from the parent project instance using `admin.auth().tenantManager()`.

A tenant configuration provides information about a tenant, such as its display name, tenant identifier, and email authentication configuration.

All other settings (such as whitelisted domains and authenticated redirect URIs) of a tenant are inherited from the parent project. These must be managed using the Google Cloud console.

For operations such as tenant-specific user management, configuring OIDC/SAML providers, and email link generation, you'll need a `TenantAwareAuth` instance for the target tenant (identified by its unique `tenantId`).

###  Node.js 
    
    
    const tenantManager = admin.auth().tenantManager();
    const tenantAuth = tenantManager.authForTenant(tenantId);
    

###  Python 
    
    
    from firebase_admin import tenant_mgt
    
    tenant_client = tenant_mgt.auth_for_tenant(tenant_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L763-L765)

###  Java 
    
    
    FirebaseAuth auth = FirebaseAuth.getInstance();
    TenantManager tenantManager = auth.getTenantManager();
    TenantAwareFirebaseAuth tenantAuth = tenantManager.getAuthForTenant(tenantId);
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L828-L830)

All calls to the user management APIs, OIDC/SAML provider management APIs, and email link generation APIs will be inside the scope of this tenant (using its `TenantAwareAuth` instance).

### Getting an existing tenant

The Admin SDK provides the `getTenant()` method, which fetches information about a tenant based on its `tenantId` (a unique identifier for the tenant).

###  Node.js 
    
    
    admin.auth().tenantManager().getTenant(tenantId)
      .then((tenant) => {
        console.log(tenant.toJSON());
      })
      .catch((error) => {
        // Handle error.
      });
    

###  Python 
    
    
    tenant = tenant_mgt.get_tenant(tenant_id)
    
    print('Retrieved tenant:', tenant.tenant_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L771-L773)

###  Java 
    
    
    Tenant tenant = FirebaseAuth.getInstance().getTenantManager().getTenant(tenantId);
    System.out.println("Retrieved tenant: " + tenant.getTenantId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L838-L839)

This method returns a `Tenant` object corresponding to the `tenantId`. If the provided `tenantId` does not belong to an existing tenant, the returned promise rejects with an `auth/tenant-not-found` error.

Be careful not to confuse a `Tenant` instance with a `TenantAwareAuth` object. `authInstance.tenantManager().authForTenant()` returns a `TenantAwareAuth` instance that extends [`BaseAuth`](https://firebase.google.com/docs/reference/admin/node/admin.auth.BaseAuth.html). The [`Auth`](https://firebase.google.com/docs/reference/admin/node/admin.auth) class also extends [`BaseAuth`](https://firebase.google.com/docs/reference/admin/node/admin.auth.BaseAuth.html). `BaseAuth` provides APIs to manage users, configure OIDC/SAML providers in different contexts. For `Auth`, the context is at the parent project level. For `TenantAwareAuth`, the context is at the tenant level (the tenant is determined by the tenant ID). The `getTenant()` method will resolve with basic tenant information (like tenant ID, display name, and email provider settings), but to call APIs on that tenant, you need to use `authForTenant(tenantFromGetTenant.tenantId)`.

### Creating a tenant

Use the `createTenant()` method to to create a new tenant configuration:

###  Node.js 
    
    
    admin.auth().tenantManager().createTenant({
      displayName: 'myTenant1',
      emailSignInConfig: {
        enabled: true,
        passwordRequired: false, // Email link sign-in enabled.
      },
      // TODO: Remove if you don't want to enable multi-factor authentication.
      multiFactorConfig: {
        state: 'ENABLED',
        factorIds: ['phone']
      },
      // TODO: Remove if you don't want to register test phone numbers for use
      // with multi-factor authentication.
      testPhoneNumbers: {
        '+16505551234': '145678',
        '+16505550000': '123456'
      },
    })
    .then((createdTenant) => {
      console.log(createdTenant.toJSON());
    })
    .catch((error) => {
      // Handle error.
    });
    

###  Python 
    
    
    tenant = tenant_mgt.create_tenant(
        display_name='myTenant1',
        enable_email_link_sign_in=True,
        allow_password_sign_up=True)
    
    print('Created tenant:', tenant.tenant_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L778-L783)

###  Java 
    
    
    Tenant.CreateRequest request = new Tenant.CreateRequest()
        .setDisplayName("myTenant1")
        .setEmailLinkSignInEnabled(true)
        .setPasswordSignInAllowed(true);
    Tenant tenant = FirebaseAuth.getInstance().getTenantManager().createTenant(request);
    System.out.println("Created tenant: " + tenant.getTenantId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L845-L850)

You can provide any combination of these properties:

Property | Type | Description  
---|---|---  
`displayName` | 
    
    
    string
        

|  The tenant display name. This must be 4-20 characters, consisting of letters, digits, and hyphens, and must begin with a letter.   
`emailSignInConfig` | 
    
    
    {
      enable: boolean,
      passwordRequired: boolean
    }
        

|  The email sign in provider configuration. This includes whether email provider is enabled, and whether password is required for email sign-in. When not required, email sign-in can be performed with password or using email link sign-in.   
`multiFactorConfig` | 
    
    
    {
      state: 'DISABLED' | 'ENABLED',
      factorIds: string[]
    }
        

|  Whether [multi-factor authentication](https://docs.cloud.google.com/identity-platform/docs/web/mfa) is enabled for the tenant, and what factor types are allowed. Currently, the only supported factor ID is `phone`.   
`testPhoneNumbers` | 
    
    
    {
      string: string
    }
      

|  A map of phone numbers and their associated multi-factor authentication codes to register for [test purposes](https://docs.cloud.google.com/identity-platform/docs/test-phone-numbers). A maximum of 10 entries are allowed. To remove all test phone numbers, set this field to `null`.   
  
The method returns a `Tenant` object for the newly created tenant.

### Updating a tenant

Use the `updateTenant()` method to modify an existing tenant's data. You'll need to specify the `tenantId`, along with the properties to update for that tenant.

###  Node.js 
    
    
    admin.auth().tenantManager().updateTenant(tenantId, {
      displayName: 'updatedName',
      emailSignInConfig: {
        enabled: false, // Disable email provider.
      },
      // Enable multi-factor authentication.
      multiFactorConfig: {
        state: 'ENABLED',
        factorIds: ['phone']
      },
      // Register phone numbers for testing.
      testPhoneNumbers: {
        '+16505551234': '145678',
        '+16505550000': '123456'
      },
    })
    .then((updatedTenant) => {
      console.log(updatedTenant.toJSON());
    })
    .catch((error) => {
      // Handle error.
    });
    

###  Python 
    
    
    tenant = tenant_mgt.update_tenant(
        tenant_id,
        display_name='updatedName',
        allow_password_sign_up=False) # Disable email provider
    
    print('Updated tenant:', tenant.tenant_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L788-L793)

###  Java 
    
    
    Tenant.UpdateRequest request = new Tenant.UpdateRequest(tenantId)
        .setDisplayName("updatedName")
        .setPasswordSignInAllowed(false);
    Tenant tenant = FirebaseAuth.getInstance().getTenantManager().updateTenant(request);
    System.out.println("Updated tenant: " + tenant.getTenantId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L856-L860)

`updateTenant()` accepts the same properties as `createTenant()`. All properties are optional. If a property is not specified, the existing value will not be modified.

The method returns an updated `Tenant` object upon completion. If the provided `tenantId` does not belong to an existing tenant, the returned promise rejects with an `auth/tenant-not-found` error.

### Deleting a tenant

You can delete a tenant using its `tenantId`:

###  Node.js 
    
    
    admin.auth().tenantManager().deleteTenant(tenantId)
      .then(() => {
        // Tenant deleted.
      })
      .catch((error) => {
        // Handle error.
      });
    

###  Python 
    
    
    tenant_mgt.delete_tenant(tenant_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L798-L798)

###  Java 
    
    
    FirebaseAuth.getInstance().getTenantManager().deleteTenant(tenantId);
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L866-L866)

The method returns an empty result when the deletion completes successfully. If the provided `tenantId` does not belong to an existing tenant, the returned promise rejects with an `auth/tenant-not-found` error.

### Listing tenants

Use the `listTenants()` method to list existing tenants:

###  Node.js 
    
    
    function listAllTenants(nextPageToken) {
      return admin.auth().tenantManager().listTenants(100, nextPageToken)
        .then((result) => {
          result.tenants.forEach((tenant) => {
            console.log(tenant.toJSON());
          });
          if (result.pageToken) {
            return listAllTenants(result.pageToken);
          }
        });
    }
    
    listAllTenants();
    

###  Python 
    
    
    for tenant in tenant_mgt.list_tenants().iterate_all():
        print('Retrieved tenant:', tenant.tenant_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L803-L804)

###  Java 
    
    
    ListTenantsPage page = FirebaseAuth.getInstance().getTenantManager().listTenants(null);
    for (Tenant tenant : page.iterateAll()) {
      System.out.println("Retrieved tenant: " + tenant.getTenantId());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L872-L875)

Each batch of results contains a list of tenants, plus a next page token to list the next batch of tenant. When all the tenants have already been listed, no `pageToken` is returned.

If no `maxResults` field is specified, the default is 1000 tenants per batch. This is also the maximum number of tenants allowed to be listed at a time. Any value greater than the maximum will throw an argument error. If no `pageToken` is specified, the method will list tenants from the beginning.

## Managing SAML and OIDC providers programmatically

The Admin SDK provides APIs for managing Security Assertion Markup Language (SAML) 2.0 and OpenID Connect (OIDC) provider configurations programmatically from a secure server environment.

With the Admin SDK, you can manage these providers for a specific tenant. This is similar to [managing project-level OIDC and SAML providers](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically).

**Note:** The default supported identity providers (such as Google, Facebook, Twitter, and Microsoft) cannot be configured using the Admin SDK; configure them manually using the Google Cloud console. Be aware that when configuring these providers, their tenants will inherit the whitelisted domains and authenticated redirect URIs of their parent project.

To manage providers for a tenant, first create a `TenantAwareAuth` instance:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

You can then perform common operations, such as creating, modifying, or deleting providers for a tenant.

### Creating a provider

The following code shows how to create a SAML provider for a tenant:

###  Node.js 
    
    
    const newConfig = {
      displayName: 'SAML provider name',
      enabled: true,
      providerId: 'saml.myProvider',
      idpEntityId: 'IDP_ENTITY_ID',
      ssoURL: 'https://example.com/saml/sso/1234/',
      x509Certificates: [
        '-----BEGIN CERTIFICATE-----\nCERT1...\n-----END CERTIFICATE-----',
        '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----'
      ],
      rpEntityId: 'RP_ENTITY_ID',
      // Using the default callback URL.
      callbackURL: 'https://project-id.firebaseapp.com/__/auth/handler'
    };
    
    tenantAuth.createProviderConfig(newConfig).then(() => {
      // Successful creation.
    }).catch((error) => {
      // Handle error.
    });
    

###  Python 
    
    
    saml = tenant_client.create_saml_provider_config(
        display_name='SAML provider name',
        enabled=True,
        provider_id='saml.myProvider',
        idp_entity_id='IDP_ENTITY_ID',
        sso_url='https://example.com/saml/sso/1234/',
        x509_certificates=[
            '-----BEGIN CERTIFICATE-----\nCERT1...\n-----END CERTIFICATE-----',
            '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----',
        ],
        rp_entity_id='P_ENTITY_ID',
        callback_url='https://project-id.firebaseapp.com/__/auth/handler')
    
    print('Created new SAML provider:', saml.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L813-L826)

###  Java 
    
    
    SamlProviderConfig.CreateRequest request = new SamlProviderConfig.CreateRequest()
        .setDisplayName("SAML provider name")
        .setEnabled(true)
        .setProviderId("saml.myProvider")
        .setIdpEntityId("IDP_ENTITY_ID")
        .setSsoUrl("https://example.com/saml/sso/1234/")
        .addX509Certificate("-----BEGIN CERTIFICATE-----\nCERT1...\n-----END CERTIFICATE-----")
        .addX509Certificate("-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----")
        .setRpEntityId("RP_ENTITY_ID")
        .setCallbackUrl("https://project-id.firebaseapp.com/__/auth/handler");
    SamlProviderConfig saml = tenantAuth.createSamlProviderConfig(request);
    System.out.println("Created new SAML provider: " + saml.getProviderId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L886-L897)

### Modifying a provider

The following code shows how to modify a provider:

###  Node.js 
    
    
    const updatedConfig = {
      x509Certificates: [
        '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----',
        '-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----',
      ],
    };
    tenantAuth.updateProviderConfig('saml.myProvider', updatedConfig).then(() => {
      // Successful update.
    }).catch((error) => {
      // Handle error.
    });
    

###  Python 
    
    
    saml = tenant_client.update_saml_provider_config(
        'saml.myProvider',
        x509_certificates=[
            '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----',
            '-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----',
        ])
    
    print('Updated SAML provider:', saml.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L831-L838)

###  Java 
    
    
    SamlProviderConfig.UpdateRequest request =
        new SamlProviderConfig.UpdateRequest("saml.myProvider")
          .addX509Certificate("-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----")
          .addX509Certificate("-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----");
    SamlProviderConfig saml = tenantAuth.updateSamlProviderConfig(request);
    System.out.println("Updated SAML provider: " + saml.getProviderId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L904-L909)

### Getting a provider

The following code shows how to retrieve the provider configuration for a specific tenant using their provider ID:

###  Node.js 
    
    
    tenantAuth.getProviderConfig('saml.myProvider').then((config) => {
      // Get display name and whether it is enabled.
      console.log(config.displayName, config.enabled);
    }).catch((error) => {
      // Handle error. Common error is that config is not found.
    });
    

###  Python 
    
    
    saml = tennat_client.get_saml_provider_config('saml.myProvider')
    print(saml.display_name, saml.enabled)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L843-L844)

###  Java 
    
    
    SamlProviderConfig saml = tenantAuth.getSamlProviderConfig("saml.myProvider");
    
    // Get display name and whether it is enabled.
    System.out.println(saml.getDisplayName() + " " + saml.isEnabled());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L915-L918)

### Listing providers

The following code shows how to list provider configurations for a given tenant:

###  Node.js 
    
    
    // Returns 10 SAML provider configs starting from the specified nextPageToken offset.
    tenantAuth.listProviderConfigs({type: 'saml', maxResults: 10, pageToken: 'nextPageToken'}).then((results) => {
      results.providerConfigs.forEach((config) => {
        console.log(config.providerId);
      });
      // To list the next 10:
      // return tenantAuth.listProviderConfigs(
      //     {type: 'saml', maxResults: 10, pageToken: results.pageToken});
    }).catch((error) => {
      // Handle error.
    });
    

###  Python 
    
    
    for saml in tenant_client.list_saml_provider_configs('nextPageToken').iterate_all():
        print(saml.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L849-L850)

###  Java 
    
    
    ListProviderConfigsPage<SamlProviderConfig> page = tenantAuth.listSamlProviderConfigs(
        "nextPageToken");
    for (SamlProviderConfig saml : page.iterateAll()) {
      System.out.println(saml.getProviderId());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L924-L928)

### Deleting a provider

The following code shows how to delete a provider:

###  Node.js 
    
    
    tenantAuth.deleteProviderConfig('saml.myProvider').then(() => {
      // Successful deletion.
    }).catch((error) => {
      // Handle error.
    });
    

###  Python 
    
    
    tenant_client.delete_saml_provider_config('saml.myProvider')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L855-L855)

###  Java 
    
    
    tenantAuth.deleteSamlProviderConfig("saml.myProvider");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L935-L935)

OIDC providers are managed similarly to project-level OIDC providers, except they can be managed from the corresponding `TenantAwareAuth` instance, rather than an `Auth` project-level instance.

To learn more, refer to [Managing SAML and OIDC providers programmatically](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically).

## Managing tenant specific users

You can use the Admin SDK to to create, retrieve, update, delete, and list all users for a specific tenant.

To start, you need a `TenantAwareAuth` instance for the corresponding tenant:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

### Getting a user

You can retrieve a tenant-specific user with a `uid` identifier:

###  Node.js 
    
    
    tenantAuth.getUser(uid)
      .then((userRecord) => {
        // See the UserRecord reference documentation to learn more.
        console.log('Successfully fetched user data:', userRecord.toJSON());
        // Tenant ID will be reflected in userRecord.tenantId.
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });
    

###  Python 
    
    
    	# Get an auth.Client from tenant_mgt.auth_for_tenant()
        user = tenant_client.get_user(uid)
        print('Successfully fetched user data:', user.uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L862-L864)

###  Java 
    
    
    // Get an auth client from the firebase.App
    UserRecord user = tenantAuth.getUser(uid);
    System.out.println("Successfully fetched user data: " + user.getDisplayName());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L942-L944)

You can also identify a user by their email:

###  Node.js 
    
    
    tenantAuth.getUserByEmail(email)
      .then((userRecord) => {
        // See the UserRecord reference documentation to learn more.
        console.log('Successfully fetched user data:', userRecord.toJSON());
        // Tenant ID will be reflected in userRecord.tenantId.
      })
      .catch((error) => {
        console.log('Error fetching user data:', error);
      });
    

###  Python 
    
    
    user = tenant_client.get_user_by_email(email)
    print('Successfully fetched user data:', user.uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L870-L871)

###  Java 
    
    
    // Get an auth client from the firebase.App
    UserRecord user = tenantAuth.getUserByEmail(email);
    System.out.println("Successfully fetched user data: " + user.getDisplayName());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L951-L953)

### Creating a user

Use the `createUser()` method to create new users for a specific tenant. When creating a new user, providing a `uid` is optional; if not specified, Identity Platform will provision a unique one.

###  Node.js 
    
    
    tenantAuth.createUser({
      email: 'user@example.com',
      emailVerified: false,
      phoneNumber: '+11234567890',
      password: 'secretPassword',
      displayName: 'John Doe',
      photoURL: 'http://www.example.com/12345678/photo.png',
      disabled: false
    })
    .then((userRecord) => {
      // See the UserRecord reference documentation to learn more.
      console.log('Successfully created new user:', userRecord.uid);
      // Tenant ID will be reflected in userRecord.tenantId.
    })
    .catch((error) => {
      console.log('Error creating new user:', error);
    });
    

###  Python 
    
    
    user = tenant_client.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False)
    print('Sucessfully created new user:', user.uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L876-L884)

###  Java 
    
    
    UserRecord.CreateRequest request = new UserRecord.CreateRequest()
        .setEmail("user@example.com")
        .setEmailVerified(false)
        .setPhoneNumber("+15555550100")
        .setPassword("secretPassword")
        .setDisplayName("John Doe")
        .setPhotoUrl("http://www.example.com/12345678/photo.png")
        .setDisabled(false);
    UserRecord user = tenantAuth.createUser(request);
    System.out.println("Successfully created user: " + user.getDisplayName());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L959-L968)

### Modifying a user

You can modify existing users by specifying their `uid` to the `updateUser()` method:

###  Node.js 
    
    
    tenantAuth.updateUser(uid, {
      email: 'modifiedUser@example.com',
      phoneNumber: '+11234567890',
      emailVerified: true,
      password: 'newPassword',
      displayName: 'Jane Doe',
      photoURL: 'http://www.example.com/12345678/photo.png',
      disabled: true
    })
    .then((userRecord) => {
      // See the UserRecord reference documentation to learn more.
      console.log('Successfully updated user', userRecord.toJSON());
    })
    .catch((error) => {
      console.log('Error updating user:', error);
    });
    

###  Python 
    
    
    user = tenant_client.update_user(
        uid,
        email='user@example.com',
        phone_number='+15555550100',
        email_verified=True,
        password='newPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=True)
    print('Sucessfully updated user:', user.uid)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L889-L898)

###  Java 
    
    
    UserRecord.UpdateRequest request = new UserRecord.UpdateRequest(uid)
        .setEmail("user@example.com")
        .setEmailVerified(true)
        .setPhoneNumber("+15555550100")
        .setPassword("newPassword")
        .setDisplayName("John Doe")
        .setPhotoUrl("http://www.example.com/12345678/photo.png")
        .setDisabled(true);
    UserRecord user = tenantAuth.updateUser(request);
    System.out.println("Successfully updated user: " + user.getDisplayName());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L975-L984)

### Deleting a user

The following example shows how to delete a user based on their `uid`:

###  Node.js 
    
    
    tenantAuth.deleteUser(uid)
      .then(() => {
        console.log('Successfully deleted user');
      })
      .catch((error) => {
        console.log('Error deleting user:', error);
      });
    

###  Python 
    
    
    tenant_client.delete_user(uid)
    print('Successfully deleted user')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L903-L904)

###  Java 
    
    
    tenantAuth.deleteUser(uid);
    
    System.out.println("Successfully deleted user: " + uid);
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L991-L993)

### Listing users

To retrieve an entire list of users for a specific tenant in batches, use the `listUsers()` method. Each batch will contain a list of user records, plus a next page token if additional users remain.

###  Node.js 
    
    
    function listAllUsers(nextPageToken) {
      // List batch of users, 1000 at a time.
      tenantAuth.listUsers(1000, nextPageToken)
        .then((listUsersResult) => {
          listUsersResult.users.forEach((userRecord) => {
            console.log('user', userRecord.toJSON());
            // Tenant ID will be reflected in userRecord.tenantId.
          });
          if (listUsersResult.pageToken) {
            // List next batch of users.
            listAllUsers(listUsersResult.pageToken);
          }
        })
        .catch((error) => {
          console.log('Error listing users:', error);
        });
    }
    // Start listing users from the beginning, 1000 at a time.
    listAllUsers();
    

###  Python 
    
    
    	# Note, behind the scenes, the iterator will retrive 1000 users at a time through the API
        for user in tenant_client.list_users().iterate_all():
            print('User: ' + user.uid)
    
    	# Iterating by pages of 1000 users at a time.
        page = tenant_client.list_users()
        while page:
            for user in page.users:
                print('User: ' + user.uid)
            # Get next batch of users.
            page = page.get_next_page()
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L909-L919)

###  Java 
    
    
    // Note, behind the scenes, the ListUsersPage retrieves 1000 Users at a time
    // through the API
    ListUsersPage  page = tenantAuth.listUsers(null);
    for (ExportedUserRecord user : page.iterateAll()) {
      System.out.println("User: " + user.getUid());
    }
    
    // Iterating by pages 100 users at a time.
    page = tenantAuth.listUsers(null, 100);
    while (page != null) {
      for (ExportedUserRecord user : page.getValues()) {
        System.out.println("User: " + user.getUid());
      }
    
      page = page.getNextPage();
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L999-L1014)

See the Admin SDK documentation on [managing users](https://firebase.google.com/docs/auth/admin/manage-users) to learn more.

## Importing users

You can use the Admin SDK to import users in bulk to a specific tenant with elevated privileges. This offers numerous benefits, such as the ability to [migrate users](https://docs.cloud.google.com/identity-platform/docs/migrate-users-between-projects-tenants) from another Identity Platform product, from another tenant, or from an an external authentication system using a different hashing algorithm. You can also import users with federated providers (such as SAML and OIDC) and custom claims directly in bulk.

To start, get a `TenantAwareAuth` instance for the corresponding tenant:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

You can import up to 1000 users at a time using a specific hashing algorithm.

###  Node.js 
    
    
    tenantAuth.importUsers([{
      uid: 'uid1',
      email: 'user1@example.com',
      // Must be provided in a byte buffer.
      passwordHash: Buffer.from('password-hash-1'),
      // Must be provided in a byte buffer.
      passwordSalt: Buffer.from('salt1')
    },
    {
      uid: 'uid2',
      email: 'user2@example.com',
      // Must be provided in a byte buffer.
      passwordHash: Buffer.from('password-hash-2'),
      // Must be provided in a byte buffer.
      passwordSalt: Buffer.from('salt2')
    
    }], {
      hash: {
        algorithm: 'HMAC_SHA256',
        // Must be provided in a byte buffer.
        key: Buffer.from('secret')
      }
    })
    .then((results) => {
      results.errors.forEach(function(indexedError) {
      console.log('Error importing user ' + indexedError.index);
      });
    })
    .catch((error) => {
      console.log('Error importing users:', error);
    });
    

###  Python 
    
    
    users = [
        auth.ImportUserRecord(
            uid='uid1',
            email='user1@example.com',
            password_hash=b'password_hash_1',
            password_salt=b'salt1'
        ),
        auth.ImportUserRecord(
            uid='uid2',
            email='user2@example.com',
            password_hash=b'password_hash_2',
            password_salt=b'salt2'
        ),
    ]
    
    hash_alg = auth.UserImportHash.hmac_sha256(key=b'secret')
    try:
        result = tenant_client.import_users(users, hash_alg=hash_alg)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L924-L945)

###  Java 
    
    
    List<ImportUserRecord> users = new ArrayList<>();
    users.add(ImportUserRecord.builder()
        .setUid("uid1")
        .setEmail("user1@example.com")
        .setPasswordHash("password-hash-1".getBytes())
        .setPasswordSalt("salt1".getBytes())
        .build());
    users.add(ImportUserRecord.builder()
        .setUid("uid2")
        .setEmail("user2@example.com")
        .setPasswordHash("password-hash-2".getBytes())
        .setPasswordSalt("salt2".getBytes())
        .build());
    UserImportHash hmacSha256 = HmacSha256.builder()
        .setKey("secret".getBytes())
        .build();
    UserImportResult result = tenantAuth.importUsers(users, UserImportOptions.withHash(hmacSha256));
    
    for (ErrorInfo error : result.getErrors()) {
      System.out.println("Failed to import user: " + error.getReason());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1021-L1041)

All imported users will have their `tenantId` set to the `tenantAuth.tenantId`.

Users without passwords can also be imported to a specific tenant. These users can be imported with federated providers and custom claims.

###  Node,js 
    
    
    tenantAuth.importUsers([{
      uid: 'some-uid',
      displayName: 'John Doe',
      email: 'johndoe@acme.com',
      photoURL: 'http://www.example.com/12345678/photo.png',
      emailVerified: true,
      phoneNumber: '+11234567890',
      // Set this user as admin.
      customClaims: {admin: true},
      // User with SAML provider.
      providerData: [{
        uid: 'saml-uid',
        email: 'johndoe@acme.com',
        displayName: 'John Doe',
        photoURL: 'http://www.example.com/12345678/photo.png',
        providerId: 'saml.acme'
      }]
    }])
    .then(function(results) {
      results.errors.forEach(function(indexedError) {
      console.log('Error importing user ' + indexedError.index);
      });
    })
    .catch(function(error) {
      console.log('Error importing users:', error);
    });
    

###  Python 
    
    
    users = [
        auth.ImportUserRecord(
            uid='some-uid',
            display_name='John Doe',
            email='johndoe@gmail.com',
            photo_url='http://www.example.com/12345678/photo.png',
            email_verified=True,
            phone_number='+11234567890',
            custom_claims={'admin': True}, # set this user as admin
            provider_data=[ # user with SAML provider
                auth.UserProvider(
                    uid='saml-uid',
                    email='johndoe@gmail.com',
                    display_name='John Doe',
                    photo_url='http://www.example.com/12345678/photo.png',
                    provider_id='saml.acme'
                )
            ],
        ),
    ]
    try:
        result = tenant_client.import_users(users)
        for err in result.errors:
            print('Failed to import user:', err.reason)
    except exceptions.FirebaseError as error:
        print('Error importing users:', error)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L950-L975)

###  Java 
    
    
    List<ImportUserRecord> users = new ArrayList<>();
    users.add(ImportUserRecord.builder()
        .setUid("some-uid")
        .setDisplayName("John Doe")
        .setEmail("johndoe@acme.com")
        .setPhotoUrl("https://www.example.com/12345678/photo.png")
        .setEmailVerified(true)
        .setPhoneNumber("+11234567890")
        // Set this user as admin.
        .putCustomClaim("admin", true)
        // User with SAML provider.
        .addUserProvider(UserProvider.builder()
            .setUid("saml-uid")
            .setEmail("johndoe@acme.com")
            .setDisplayName("John Doe")
            .setPhotoUrl("https://www.example.com/12345678/photo.png")
            .setProviderId("saml.acme")
            .build())
        .build());
    
    UserImportResult result = tenantAuth.importUsers(users);
    
    for (ErrorInfo error : result.getErrors()) {
      System.out.println("Failed to import user: " + error.getReason());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1048-L1072)

See [Import users](https://firebase.google.com/docs/auth/admin/import-users) in the Admin SDK documentation to learn more.

## Identity verification

When an Identity Platform client app communicates with a custom backend server, the current signed in user needs to be identified on that server. This can be done securely by sending the user's ID token after successful sign-in using a secure connection to your server. The server can then verify the integrity and authenticity of the ID token.

The Admin SDK has a built-in method for verifying and decoding ID tokens for a specific tenant.

After successfully signing in a user to a specific tenant from the client, retrieve the user's ID token using the Client SDK:
    
    
    auth.tenantId = 'TENANT-ID';
    auth.signInWithEmailAndPassword('user@example.com', 'password')
      .then((userCredential) => {
        return userCredential.user.getIdToken();
      })
      .then((idToken) => {
        // Send the ID token to server for verification. ID token should be scoped to TENANT-ID.
      });
    

Create a `TenantAwareAuth` instance on the server:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

You can then verify the ID token for that specific tenant:

###  Node.js 
    
    
    // idToken comes from the client app
    tenantAuth.verifyIdToken(idToken)
      .then((decodedToken) => {
        let uid = decodedToken.uid;
        // This should be set to TENANT-ID. Otherwise auth/mismatching-tenant-id error thrown.
        console.log(decodedToken.firebase.tenant);
        // ...
      }).catch((error) => {
        // Handle error
      });
    

A server side resource might be accessible by multiple tenants with different levels of access. Since the tenant ID might not be known ahead of time in this case, the ID token can be verified at the project level first.
    
    
    admin.auth().verifyIdToken(idToken)
      .then((decodedToken) => {
        if (decodedToken.firebase.tenant === 'TENANT-ID1') {
          // Allow appropriate level of access for TENANT-ID1.
        } else if (decodedToken.firebase.tenant === 'TENANT-ID2') {
          // Allow appropriate level of access for TENANT-ID2.
        } else {
          // Block access for all other tenants.
          throw new Error('Access not allowed.');
        }
      }).catch((error) => {
        // Handle error
      });
    

###  Python 
    
    
    	# id_token comes from the client app
        try:
            decoded_token = tenant_client.verify_id_token(id_token)
    
            # This should be set to TENANT-ID. Otherwise TenantIdMismatchError error raised.
            print('Verified ID token from tenant:', decoded_token['firebase']['tenant'])
        except tenant_mgt.TenantIdMismatchError:
            # Token revoked, inform the user to reauthenticate or signOut().
            pass
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L980-L988)

###  Java 
    
    
    try {
      // idToken comes from the client app
      FirebaseToken token = tenantAuth.verifyIdToken(idToken);
      // TenantId on the FirebaseToken should be set to TENANT-ID.
      // Otherwise "tenant-id-mismatch" error thrown.
      System.out.println("Verified ID token from tenant: " + token.getTenantId());
    } catch (FirebaseAuthException e) {
      System.out.println("error verifying ID token: " + e.getMessage());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1078-L1086)

See the Admin SDK documentation on [verifying ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) to learn more.

## Managing user sessions

Identity Platform sessions are long lived. Every time a user signs in, the user's credentials are verified on the Identity Platform server, then exchanged for a short lived ID token and a long lived refresh token. An ID tokens last for an hour. Refresh tokens never expire, except when a user is disabled, deleted or undergoes a large account change (like an email or password update).

In some cases, a user's refresh token may need to be revoked for security reasons, such as the user reporting a lost or stolen device, discovery of a general vulnerability within an app, or a wide-scale leak of active tokens. The Admin SDK provides an API to revoke all issued refresh tokens for a specified user of a specific tenant.

To begin, you need a `TenantAwareAuth` instance:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

The refresh tokens can then be revoked by specifying the `uid` of that user:

###  Node.js 
    
    
    // Revoke all refresh tokens for a specified user in a specified tenant for whatever reason.
    // Retrieve the timestamp of the revocation, in seconds since the epoch.
    tenantAuth.revokeRefreshTokens(uid)
      .then(() => {
        return tenantAuth.getUser(uid);
      })
      .then((userRecord) => {
        return new Date(userRecord.tokensValidAfterTime).getTime() / 1000;
      })
      .then((timestamp) => {
        console.log('Tokens revoked at: ', timestamp);
      });
    

###  Python 
    
    
    	# Revoke all refresh tokens for a specified user in a specified tenant for whatever reason.
    	# Retrieve the timestamp of the revocation, in seconds since the epoch.
        tenant_client.revoke_refresh_tokens(uid)
    
        user = tenant_client.get_user(uid)
        # Convert to seconds as the auth_time in the token claims is in seconds.
        revocation_second = user.tokens_valid_after_timestamp / 1000
        print(f'Tokens revoked at: {revocation_second}')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L1009-L1016)

###  Java 
    
    
    // Revoke all refresh tokens for a specified user in a specified tenant for whatever reason.
    // Retrieve the timestamp of the revocation, in seconds since the epoch.
    tenantAuth.revokeRefreshTokens(uid);
    
    // accessing the user's TokenValidAfter
    UserRecord user = tenantAuth.getUser(uid);
    
    
    long timestamp = user.getTokensValidAfterTimestamp() / 1000;
    System.out.println("the refresh tokens were revoked at: " + timestamp + " (UTC seconds)");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1111-L1120)

After refresh tokens are revoked, no new ID tokens can be issued for that user until they re-authenticate. However, existing ID tokens will remain active until their natural expiration time (one hour).

You can verify that an unexpired valid ID token is not revoked by specifying the optional `checkRevoked` parameter; this checks if a token is revoked after its integrity and authenticity is verified.

###  Node.js 
    
    
    // Verify the ID token for a specific tenant while checking if the token is revoked by passing
    // checkRevoked true.
    let checkRevoked = true;
    tenantAuth.verifyIdToken(idToken, checkRevoked)
      .then(payload => {
        // Token is valid.
      })
      .catch(error => {
        if (error.code == 'auth/id-token-revoked') {
          // Token has been revoked. Inform the user to re-authenticate or
          // signOut() the user.
        } else {
          // Token is invalid.
        }
      });
    

###  Python 
    
    
    	# Verify the ID token for a specific tenant while checking if the token is revoked.
        try:
            # Verify the ID token while checking if the token is revoked by
            # passing check_revoked=True.
            decoded_token = tenant_client.verify_id_token(id_token, check_revoked=True)
            # Token is valid and not revoked.
            uid = decoded_token['uid']
        except tenant_mgt.TenantIdMismatchError:
            # Token belongs to a different tenant.
            pass
        except auth.RevokedIdTokenError:
            # Token revoked, inform the user to reauthenticate or signOut().
            pass
        except auth.UserDisabledError:
            # Token belongs to a disabled user record.
            pass
        except auth.InvalidIdTokenError:
            # Token is invalid
            pass
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L1021-L1039)

###  Java 
    
    
    // Verify the ID token for a specific tenant while checking if the token is revoked.
    boolean checkRevoked = true;
    try {
      FirebaseToken token = tenantAuth.verifyIdToken(idToken, checkRevoked);
      System.out.println("Verified ID token for: " + token.getUid());
    } catch (FirebaseAuthException e) {
      if ("id-token-revoked".equals(e.getErrorCode())) {
        // Token is revoked. Inform the user to re-authenticate or signOut() the user.
      } else {
        // Token is invalid
      }
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1127-L1138)

See the Admin SDK documentation on [managing sessions](https://firebase.google.com/docs/auth/admin/manage-sessions) to learn more.

## Controlling access with custom claims

The Admin SDK supports defining custom attributes on user accounts for a specific tenant. These attributes allow you to implement different access control strategies, such as role-based access control. The attributes can be used to give users different levels of access enforced by the application's security rules.

To begin, get a `TenantAwareAuth` instance for the corresponding tenant:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

Custom claims can contain sensitive data, so they should only be set from a privileged server environment using the Admin SDK.

###  Node.js 
    
    
    // Set admin privilege on the user corresponding to uid for a specific tenant.
    tenantAuth.setCustomUserClaims(uid, {admin: true}).then(() => {
      // The new custom claims will propagate to the user's ID token the
      // next time a new one is issued.
    });
    

###  Python 
    
    
    # Set admin privilege on the user corresponding to uid.
    tenant_client.set_custom_user_claims(uid, {'admin': True})
    # The new custom claims will propagate to the user's ID token the
    # next time a new one is issued.
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L1044-L1047)

###  Java 
    
    
    // Set admin privilege on the user corresponding to uid in a specific tenant.
    Map<String, Object> claims = new HashMap<>();
    claims.put("admin", true);
    tenantAuth.setCustomUserClaims(uid, claims);
    // The new custom claims will propagate to the user's ID token the
    // next time a new one is issued.
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1156-L1161)

Newly-set custom attributes will appear on the top-level attributes of the token payload the next time the user signs in or refreshes their ID tokens on an existing session. In the previous example, the ID token contains an additional claim: `{admin: true}`.

After verifying the ID token and decoding its payload, the additional custom claims can then be checked to enforce access control.

###  Node.js 
    
    
    // Verify the ID token first.
    tenantAuth.verifyIdToken(idToken).then((claims) => {
      if (claims.admin === true) {
        // Allow access to requested admin resource.
      }
    });
    

###  Python 
    
    
    # Verify the ID token first.
    claims = tenant_client.verify_id_token(id_token)
    if claims['admin'] is True:
        # Allow access to requested admin resource.
        pass
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L1052-L1056)

###  Java 
    
    
    // Verify the ID token first.
    FirebaseToken token = tenantAuth.verifyIdToken(idToken);
    if (Boolean.TRUE.equals(token.getClaims().get("admin"))) {
      //Allow access to requested admin resource.
    }
    // Verify the ID token first.
    FirebaseToken decoded = tenantAuth.verifyIdToken(idToken);
    if (Boolean.TRUE.equals(decoded.getClaims().get("admin"))) {
      // Allow access to requested admin resource.
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1166-L1170)

Custom claims for an existing user for a specific tenant are also available as a property on the user record.

###  Node.js
    
    
    // Lookup the user associated with the specified uid.
    tenantAuth.getUser(uid).then((userRecord) => {
      // The claims can be accessed on the user record.
      console.log(userRecord.customClaims.admin);
    });
    

###  Python 
    
    
    	# Lookup the user associated with the specified uid.
        user = tenant_client.get_user(uid)
    
    	# The claims can be accessed on the user record.
        print(user.custom_claims.get('admin'))
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L1061-L1065)

###  Java 
    
    
    // Lookup the user associated with the specified uid in a specific tenant.
    UserRecord user = tenantAuth.getUser(uid);
    System.out.println(user.getCustomClaims().get("admin"));
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1174-L1176)

See the Admin SDK documentation on [Custom claims](https://firebase.google.com/docs/auth/admin/custom-claims) to learn more.

## Generating email action links

Using the Identity Platform Client SDKs, you can send users of a specific tenant emails containing links they can use for password resets, email address verification, and email-based sign-in. These emails are sent by Google and have limited customizability.

With the Admin SDK, you can generate these links programmatically within the scope of a specific tenant.

To begin, get a `TenantAwareAuth` instance for the corresponding tenant:

###  Node.js 
    
    
    const tenantAuth = admin.auth().tenantManager().authForTenant('TENANT-ID');
    

###  Python 
    
    
    tenant_client = tenant_mgt.auth_for_tenant('TENANT-ID')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L809-L809)

###  Java 
    
    
    TenantAwareFirebaseAuth tenantAuth = FirebaseAuth.getInstance().getTenantManager()
        .getAuthForTenant("TENANT-ID");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L881-L882)

The following example shows how to generate a link to verify a user's email for a specified tenant:

###  Node.js 
    
    
    const actionCodeSettings = {
      // URL you want to redirect back to. The domain (www.example.com) for
      // this URL must be whitelisted in the Cloud console.
      url: 'https://www.example.com/checkout?cartId=1234',
      // This must be true for email link sign-in.
      handleCodeInApp: true,
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      // FDL custom domain.
      dynamicLinkDomain: 'coolapp.page.link'
    };
    
    // Admin SDK API to generate the email verification link.
    const userEmail = 'user@example.com';
    tenantAuth.generateEmailVerificationLink(userEmail, actionCodeSettings)
      .then((link) => {
        // Construct email verification template, embed the link and send
        // using custom SMTP server.
        return sendCustomVerificationEmail(userEmail, displayName, link);
      })
      .catch((error) => {
        // Some error occurred.
      });
    

###  Python 
    
    
    action_code_settings = auth.ActionCodeSettings(
        url='https://www.example.com/checkout?cartId=1234',
        handle_code_in_app=True,
        ios_bundle_id='com.example.ios',
        android_package_name='com.example.android',
        android_install_app=True,
        android_minimum_version='12',
        # FDL custom domain.
        dynamic_link_domain='coolapp.page.link',
    )
    
    email = 'user@example.com'
    link = tenant_client.generate_email_verification_link(email, action_code_settings)
    # Construct email from a template embedding the link, and send
    # using a custom SMTP server.
    send_custom_email(email, link)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/ae0a284127609272957c594af7c8a6179d87d1d4/snippets/auth/index.py#L1070-L1085)

###  Java 
    
    
    ActionCodeSettings actionCodeSettings = ActionCodeSettings.builder()
        // URL you want to redirect back to. The domain (www.example.com) for
        // this URL must be whitelisted in the GCP Console.
        .setUrl("https://www.example.com/checkout?cartId=1234")
        // This must be true for email link sign-in.
        .setHandleCodeInApp(true)
        .setIosBundleId("com.example.ios")
        .setAndroidPackageName("com.example.android")
        .setAndroidInstallApp(true)
        .setAndroidMinimumVersion("12")
        // FDL custom domain.
        .setDynamicLinkDomain("coolapp.page.link")
        .build();
    
    String link = tenantAuth.generateEmailVerificationLink(email, actionCodeSettings);
    
    // Construct email verification template, embed the link and send
    // using custom SMTP server.
    sendCustomEmail(email, displayName, link);
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2d89465e59689e6256b0965cf50197cf3ddaf823/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L1185-L1203)

Similar mechanisms are available for generating password reset and email-based sign-in links. Note that when generating an email action link in a tenant context, the tenant ID has to be parsed from the link and set on the client `Auth` instance before the code can be applied.
    
    
    const actionCodeUrl = firebase.auth.ActionCodeURL.parseLink(window.location.href);
    // A one-time code, used to identify and verify a request.
    const code = actionCodeUrl.code;
    // The tenant ID being used to trigger the email action.
    const tenantId = actionCodeUrl.tenantId;
    auth.tenantId = tenantId;
    
    // Apply the action code.
    auth.applyActionCode(actionCode)
      .then(() => {
        // User's email is now verified.
      })
      .catch((error) => {
        // Handle error.
      });
    

See [Email action links](https://firebase.google.com/docs/auth/admin/email-action-links) in the Admin SDK documentation to learn more.

## Error messages

The following table lists common error messages you may encounter.

Error code | Description and Resolution Steps  
---|---  
`auth/billing-not-enabled` | This feature requires billing to be enabled.  
`auth/invalid-display-name` | The displayName field must be a valid string.  
`auth/invalid-name` | The resource name provided is invalid.  
`auth/invalid-page-token` | The page token must be a valid non-empty string.  
`auth/invalid-project-id` |  Invalid parent project. Either the parent project doesn't, or didn't enable multi-tenancy.   
`auth/invalid-tenant-id` | The tenant ID must be a valid non-empty string.  
`auth/mismatching-tenant-id` |  User tenant ID does not match with the current `TenantAwareAuth` tenant ID.   
`auth/missing-display-name` |  The resource being created or edited is missing a valid display name.   
`auth/insufficient-permission` |  The user has insufficient permission to access the requested resource or to run the specific tenant operation.   
`auth/quota-exceeded` | The project quota for the specified operation has been exceeded.  
`auth/tenant-not-found` | There is no tenant corresponding to the provided identifier.  
`auth/unsupported-tenant-operation` | This operation is not supported in a multi-tenant context.  
`auth/invalid-testing-phone-number` | An invalid testing phone number or invalid test code was provided.  
`auth/test-phone-number-limit-exceeded` |  The maximum number of allowed test phone number and code pairs has been exceeded.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
