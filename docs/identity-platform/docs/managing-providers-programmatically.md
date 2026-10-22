---
url: https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically/
title: Managing SAML and OIDC providers programmatically \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:14.358154+00:00
---

# Managing SAML and OIDC providers programmatically  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Managing SAML and OIDC providers programmatically 

This document shows you how to use the Identity Platform Admin SDK to manage Security Assertion Markup Language (SAML) 2.0 and OpenID Connect (OIDC) provider configurations programmatically.

Using the Admin SDK, you can automatically configure providers, perform basic CRUD operations, rotate certificates, and more. This is useful when you have a large number of providers that would be cumbersome to manage manually using the Google Cloud console.

## Before you begin

  * [Enable Identity Platform](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email).
  * [Install the Admin SDK](https://docs.cloud.google.com/identity-platform/docs/install-admin-sdk).



## Working with SAML providers

### Creating a SAML provider configuration

You'll need to supply the following parameters when creating a SAML provider configuration. You may need to consult your identity provider's documentation for details on how to obtain some of the values.

Display name
     A user-friendly display name for the configuration. This name is also the provider label in the Google Cloud console. 
Enabled
     Whether the current provider configuration is enabled or disabled. Users cannot sign in with disabled providers. 
Provider ID
     The provider's unique identifier, beginning with `saml.`. 
Identity provider entity ID
     The entity ID for the provider. 
SSO URL
     The SAML SSO URL for the provider. The URL must be valid. 
X.509 certificates
    

A list of SAML provider X.509 certificates, including the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE----` strings. These are used for token-signing on the identity provider. 

When Identity Platform receives a SAML response, it will verify its signature using a certificate on record. If verification fails, the response will be rejected. You will need to update these certificates as keys are rotated. Consider uploading multiple certificates to prevent outages during rotations. 

Relaying party entity ID
     The SAML relying party (RP/SP) entity ID. This is commonly the URL of the app. On the SAML identity provider, this is referred to as the audience. 
Callback URL
    

The URL to return to when authentication completes. SAML providers commonly refer to this as the Assertion Consumer Service (ACS) URL. You'll need to register this URL with the SAML provider. It should look something like `https://PROJECT-ID.firebaseapp.com/__/auth/handler`, similar to the URLs displayed in the Google Cloud console. To learn more, see [Signing in users with SAML](https://docs.cloud.google.com/identity-platform/docs/web/saml). 

Using the default callback URL will decrease the complexity of validating SAML responses. However, you can also choose to show a [custom domain](https://docs.cloud.google.com/identity-platform/docs/show-custom-domain). In this case, make sure the Identity Platform callback URL for your project is properly correctly configured with your SAML identity provider. Typically, this looks something like `https://AUTH-DOMAIN/__/auth/handler`. 

The following example demonstrates how to create a SAML provider configuration:

###  Node.js 
    
    
    const newConfig = {
      displayName: 'SAML provider name',
      enabled: true,
      providerId: 'saml.myProvider',
      idpEntityId: 'IDP_ENTITY_ID',
      ssoURL: 'https://example.com/saml/sso/1234/'
      x509Certificates: [
        '-----BEGIN CERTIFICATE-----\nCERT1...\n-----END CERTIFICATE-----',
        '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----',
      ],
      rpEntityId: 'RP_ENTITY_ID',
      // Using the default callback URL.
      callbackURL: 'https://project-id.firebaseapp.com/__/auth/handler',
    };
    admin.auth().createProviderConfig(newConfig).then(() => {
      // Successful creation.
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    newConfig := (&auth.SAMLProviderConfigToCreate{}).
    	DisplayName("SAML provider name").
    	Enabled(true).
    	ID("saml.myProvider").
    	IDPEntityID("IDP_ENTITY_ID").
    	SSOURL("https://example.com/saml/sso/1234/").
    	X509Certificates([]string{
    		"-----BEGIN CERTIFICATE-----\nCERT1...\n-----END CERTIFICATE-----",
    		"-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----",
    	}).
    	RPEntityID("RP_ENTITY_ID").
    	CallbackURL("https://project-id.firebaseapp.com/__/auth/handler")
    saml, err := client.CreateSAMLProviderConfig(ctx, newConfig)
    if err != nil {
    	log.Fatalf("error creating SAML provider: %v\n", err)
    }
    
    log.Printf("Created new SAML provider: %s", saml.ID)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L897-L914)

###  Python 
    
    
    saml = auth.create_saml_provider_config(
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
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L676-L689)

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
    SamlProviderConfig saml = FirebaseAuth.getInstance().createSamlProviderConfig(request);
    System.out.println("Created new SAML provider: " + saml.getProviderId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L724-L735)

On completion, the method returns a [`SAMLAuthProviderConfig`](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs) object for the newly created configuration.

### Updating a SAML provider configuration

The following example demonstrates how to modify a SAML provider configuration. You can update any field, except for the provider ID.

###  Node.js 
    
    
    const updatedConfig = {
      x509Certificates: [
        '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----',
        '-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----',
      ],
    };
    admin.auth().updateProviderConfig('saml.myProvider', updatedConfig).then(() => {
      // Successful update.
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    updatedConfig := (&auth.SAMLProviderConfigToUpdate{}).
    	X509Certificates([]string{
    		"-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----",
    		"-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----",
    	})
    saml, err := client.UpdateSAMLProviderConfig(ctx, "saml.myProvider", updatedConfig)
    if err != nil {
    	log.Fatalf("error updating SAML provider: %v\n", err)
    }
    
    log.Printf("Updated SAML provider: %s", saml.ID)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L920-L930)

###  Python 
    
    
    saml = auth.update_saml_provider_config(
        'saml.myProvider',
        x509_certificates=[
            '-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----',
            '-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----',
        ])
    
    print('Updated SAML provider:', saml.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L694-L701)

###  Java 
    
    
    SamlProviderConfig.UpdateRequest request =
        new SamlProviderConfig.UpdateRequest("saml.myProvider")
          .addX509Certificate("-----BEGIN CERTIFICATE-----\nCERT2...\n-----END CERTIFICATE-----")
          .addX509Certificate("-----BEGIN CERTIFICATE-----\nCERT3...\n-----END CERTIFICATE-----");
    SamlProviderConfig saml = FirebaseAuth.getInstance().updateSamlProviderConfig(request);
    System.out.println("Updated SAML provider: " + saml.getProviderId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L741-L746)

On completion, the method returns a [`SAMLAuthProviderConfig`](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs) object for the updated configuration.

### Getting a SAML provider configuration

The primary way to identify a SAML configuration is using its provider ID. The following example shows how to get a SAML provider configuration:

###  Node.js 
    
    
    admin.auth().getProviderConfig('saml.myProvider').then((config) => {
      // Get display name and whether it is enabled.
      console.log(config.displayName, config.enabled);
    }).catch((error) => {
      // Handle error. Common error is that config is not found.
    });
    

###  Go 
    
    
    saml, err := client.SAMLProviderConfig(ctx, "saml.myProvider")
    if err != nil {
    	log.Fatalf("error retrieving SAML provider: %v\n", err)
    }
    
    log.Printf("%s %t", saml.DisplayName, saml.Enabled)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L936-L941)

###  Python 
    
    
    saml = auth.get_saml_provider_config('saml.myProvider')
    print(saml.display_name, saml.enabled)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L706-L707)

###  Java 
    
    
    SamlProviderConfig saml = FirebaseAuth.getInstance().getSamlProviderConfig("saml.myProvider");
    System.out.println(saml.getDisplayName() + ": " + saml.isEnabled());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L752-L753)

If a provider with the given ID exists, the method returns a [`SAMLAuthProviderConfig`](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.inboundSamlConfigs) object.

### Deleting a SAML provider configuration

The following example shows how to delete a SAML provider configuration:

###  Node.js 
    
    
    admin.auth().deleteProviderConfig('saml.myProvider').then(() => {
      // Successful deletion.
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    if err := client.DeleteSAMLProviderConfig(ctx, "saml.myProvider"); err != nil {
    	log.Fatalf("error deleting SAML provider: %v\n", err)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L947-L949)

###  Python 
    
    
    auth.delete_saml_provider_config('saml.myProvider')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L712-L712)

###  Java 
    
    
    FirebaseAuth.getInstance().deleteSamlProviderConfig("saml.myProvider");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L759-L759)

### Listing SAML provider configurations

The following example shows how to list existing SAML provider configurations:

###  Node.js 
    
    
    // Returns 10 SAML provider configs starting from the specified nextPageToken offset.
    admin.auth().listProviderConfigs({type: 'saml', maxResults: 10, pageToken: 'nextPageToken'}).then((results) => {
      results.providerConfigs.forEach((config) => {
        console.log(config.providerId);
      });
      // To list the next 10:
      // return admin.auth().listProviderConfigs(
      //     {type: 'saml', maxResults: 10, pageToken: results.pageToken});
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    iter := client.SAMLProviderConfigs(ctx, "nextPageToken")
    for {
    	saml, err := iter.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		log.Fatalf("error retrieving SAML providers: %v\n", err)
    	}
    
    	log.Printf("%s\n", saml.ID)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L955-L966)

###  Python 
    
    
    for saml in auth.list_saml_provider_configs('nextPageToken').iterate_all():
        print(saml.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L717-L718)

###  Java 
    
    
    ListProviderConfigsPage<SamlProviderConfig> page = FirebaseAuth.getInstance()
        .listSamlProviderConfigs("nextPageToken");
    for (SamlProviderConfig config : page.iterateAll()) {
      System.out.println(config.getProviderId());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L765-L769)

Each batch of results contains a list of provider configurations, and a next page token used to fetch the next batch. When all providers have been listed, no token is returned.

By default, 100 providers are returned with each batch. This is also the maximum number of providers per batch.

## Working with OIDC providers

### Creating an OIDC provider configuration

You'll need to supply the following parameters when creating an OIDC provider configuration. You may need to consult your identity provider's documentation for details on how to obtain some of the values.

Display name
     A user-friendly display name for the configuration. This name is also the provider label in the Google Cloud console. 
Enabled
     Whether the current provider configuration is enabled or disabled. Users cannot sign in with disabled providers. 
Provider ID
     The provider's unique identifier, beginning with `oidc.`. 
Client ID
     The ID used to confirm the audience of an OIDC provider's [ ID token](https://openid.net/specs/openid-connect-core-1_0-final.html#IDToken). 
Client Secret
     The client secret required to enable the OIDC code flow. 
Issuer
     The provider's `Issuer`. This should look something like `https://example.com`. Identity Platform uses this URL to locate the OIDC discovery document (typically found at `/.well-known/openid-configuration`), which specifies the provider's OAuth endpoints and public keys. Identity Platform validates ID tokens according to the [ OpenID Connect specification](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation). If your provider doesn't comply with the OIDC specification for discovery, it won't work with Identity Platform. 
Response Type
     The provider's response type for the OAuth authorization flow. You can set one of {`idToken`, `code`} to `true`, not both. If the code flow is enabled, you must provide a client secret. 
**Note:** The authorization code flow is currently only supported in Node.js and Java.

The following example demonstrates how to create an OIDC provider configuration that uses the implicit authorization flow:

###  Node.js 
    
    
    const newConfig = {
      displayName: 'OIDC provider name',
      enabled: true,
      clientId: 'CLIENT_ID2',
      issuer: 'https://oidc.com/CLIENT_ID2',
      providerId: 'oidc.provider2',
      responseType: {
        idToken: true,
        code: false,
      },
    };
    admin.auth().createProviderConfig(newConfig).then(() => {
      // Successful creation.
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    newConfig := (&auth.OIDCProviderConfigToCreate{}).
    	DisplayName("OIDC provider name").
    	Enabled(true).
    	ID("oidc.myProvider").
    	ClientID("CLIENT_ID2").
    	Issuer("https://oidc.com/CLIENT_ID2")
    oidc, err := client.CreateOIDCProviderConfig(ctx, newConfig)
    if err != nil {
    	log.Fatalf("error creating OIDC provider: %v\n", err)
    }
    
    log.Printf("Created new OIDC provider: %s", oidc.ID)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L972-L983)

###  Python 
    
    
    oidc = auth.create_oidc_provider_config(
        display_name='OIDC provider name',
        enabled=True,
        provider_id='oidc.myProvider',
        client_id='CLIENT_ID2',
        issuer='https://oidc.com/CLIENT_ID2')
    
    print('Created new OIDC provider:', oidc.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L723-L730)

###  Java 
    
    
    OidcProviderConfig.CreateRequest request = new OidcProviderConfig.CreateRequest()
        .setDisplayName("OIDC provider name")
        .setEnabled(true)
        .setProviderId("oidc.myProvider")
        .setClientId("CLIENT_ID2")
        .setIssuer("https://oidc.com/CLIENT_ID2");
    OidcProviderConfig oidc = FirebaseAuth.getInstance().createOidcProviderConfig(request);
    System.out.println("Created new OIDC provider: " + oidc.getProviderId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L775-L782)

On completion, the method returns an [`OIDCAuthProviderConfig`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.oauthIdpConfigs) object for the newly created configuration.

### Updating an OIDC provider configuration

The following example demonstrates how to modify an OIDC provider configuration. You can update any field, except for the provider ID.

###  Node.js 
    
    
    const updatedConfig = {
      displayName: 'OIDC provider name',
      enabled: true,
      clientId: 'CLIENT_ID',
      clientSecret: 'CLIENT_SECRET'
      issuer: 'https://oidc.com/',
      responseType: {
        code: true,
        idToken: false,
      },
    };
    admin.auth().updateProviderConfig('oidc.myProvider', updatedConfig).then(() => {
      // Successful update.
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    updatedConfig := (&auth.OIDCProviderConfigToUpdate{}).
    	DisplayName("OIDC provider name").
    	Enabled(true).
    	ClientID("CLIENT_ID").
    	Issuer("https://oidc.com")
    oidc, err := client.UpdateOIDCProviderConfig(ctx, "oidc.myProvider", updatedConfig)
    if err != nil {
    	log.Fatalf("error updating OIDC provider: %v\n", err)
    }
    
    log.Printf("Updated OIDC provider: %s", oidc.ID)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L989-L999)

###  Python 
    
    
    oidc = auth.update_oidc_provider_config(
        'oidc.myProvider',
        client_id='CLIENT_ID',
        issuer='https://oidc.com')
    
    print('Updated OIDC provider:', oidc.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L735-L740)

###  Java 
    
    
    OidcProviderConfig.UpdateRequest request =
        new OidcProviderConfig.UpdateRequest("oidc.myProvider")
            .setDisplayName("OIDC provider name")
            .setEnabled(true)
            .setClientId("CLIENT_ID")
            .setIssuer("https://oidc.com");
    OidcProviderConfig oidc = FirebaseAuth.getInstance().updateOidcProviderConfig(request);
    System.out.println("Updated OIDC provider: " + oidc.getProviderId());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L788-L795)

On completion, the method returns an [`OIDCAuthProviderConfig`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.oauthIdpConfigs) object for the updated configuration.

### Getting an OIDC provider configuration

The primary way to identify an OIDC configuration is using its provider ID. The following example shows how to get an OIDC provider configuration:

###  Node.js 
    
    
    admin.auth().getProviderConfig('oidc.myProvider').then((config) => {
      // Get display name and whether it is enabled.
      console.log(config.displayName, config.enabled);
    }).catch((error) => {
      // Handle error. Common error is that config is not found.
    });
    

###  Go 
    
    
    oidc, err := client.OIDCProviderConfig(ctx, "oidc.myProvider")
    if err != nil {
    	log.Fatalf("error retrieving OIDC provider: %v\n", err)
    }
    
    log.Printf("%s %t", oidc.DisplayName, oidc.Enabled)
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L1005-L1010)

###  Python 
    
    
    oidc = auth.get_oidc_provider_config('oidc.myProvider')
    
    print(oidc.display_name, oidc.enabled)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L745-L747)

###  Java 
    
    
    OidcProviderConfig oidc = FirebaseAuth.getInstance().getOidcProviderConfig("oidc.myProvider");
    System.out.println(oidc.getDisplayName() + ": " + oidc.isEnabled());
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L801-L802)

If a provider with the given ID exists, the method returns an [`OIDCAuthProviderConfig`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.oauthIdpConfigs) object.

### Deleting an OIDC provider configuration

The following example demonstrates how to delete an OIDC provider configuration:

###  Node.js 
    
    
    admin.auth().deleteProviderConfig('oidc.myProvider').then(() => {
      // Successful deletion.
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    if err := client.DeleteOIDCProviderConfig(ctx, "oidc.myProvider"); err != nil {
    	log.Fatalf("error deleting OIDC provider: %v\n", err)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L1016-L1018)

###  Python 
    
    
    auth.delete_oidc_provider_config('oidc.myProvider')
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L752-L752)

###  Java 
    
    
    FirebaseAuth.getInstance().deleteOidcProviderConfig("oidc.myProvider");
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L808-L808)

### Listing OIDC provider configurations

The following example shows how to list existing OIDC provider configurations:

###  Node.js 
    
    
    // Returns 10 OIDC provider configs starting from the specified nextPageToken offset.
    admin.auth().listProviderConfigs({type: 'oidc', maxResults: 10, pageToken: 'nextPageToken'}).then((results) => {
      results.providerConfigs.forEach((config) => {
        console.log(config.providerId);
      });
      // To list the next 10:
      // return admin.auth().listProviderConfigs(
      //     {type: 'oidc', maxResults: 10, pageToken: results.pageToken});
    }).catch((error) => {
      // Handle error.
    });
    

###  Go 
    
    
    iter := client.OIDCProviderConfigs(ctx, "nextPageToken")
    for {
    	oidc, err := iter.Next()
    	if err == iterator.Done {
    		break
    	}
    	if err != nil {
    		log.Fatalf("error retrieving OIDC providers: %v\n", err)
    	}
    
    	log.Printf("%s\n", oidc.ID)
    }
    
    [auth.go](https://github.com/firebase/firebase-admin-go/blob/66a72c371b4dbc592317ab7e7f99ce00d76c62ae/snippets/auth.go#L1024-L1035)

###  Python 
    
    
    for oidc in auth.list_oidc_provider_configs('nextPageToken').iterate_all():
        print(oidc.provider_id)
    
    [index.py](https://github.com/firebase/firebase-admin-python/blob/de456071dc7450a6d7715667debf6049f38fd85d/snippets/auth/index.py#L757-L758)

###  Java 
    
    
    ListProviderConfigsPage<OidcProviderConfig> page = FirebaseAuth.getInstance()
        .listOidcProviderConfigs("nextPageToken");
    for (OidcProviderConfig oidc : page.iterateAll()) {
      System.out.println(oidc.getProviderId());
    }
    
    [FirebaseAuthSnippets.java](https://github.com/firebase/firebase-admin-java/blob/2225373d97869e72b164a4081968027c130c782b/src/test/java/com/google/firebase/snippets/FirebaseAuthSnippets.java#L814-L818)

Each batch of results contains a list of provider configurations, and a next page token used to fetch the next batch. When all providers have been listed, no token is returned.

By default, 100 providers are returned with each batch. This is also the maximum number of providers per batch.

## What's next

  * [Migrate users](https://docs.cloud.google.com/identity-platform/docs/migrating-users) from an existing app.
  * Sign in users with [SAML](https://docs.cloud.google.com/identity-platform/docs/web/saml) and [OIDC](https://docs.cloud.google.com/identity-platform/docs/web/oidc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
