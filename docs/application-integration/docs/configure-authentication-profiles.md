---
url: https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles/
title: Manage authentication profiles \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:17.916760+00:00
---

# Manage authentication profiles  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage authentication profiles

The tasks in your Application Integration may require connection to an external application, service, or data source. An authentication profile lets you configure and store the authentication details for the connection in Application Integration. You can configure the task to use the stored authentication profile. Creating an authentication profile is a one-time activity, and you can reuse the same profile in multiple integrations. 

## Required roles

To get the permissions that you need to manage authentication profiles, ask your administrator to grant you the following IAM roles on an integration: 

  * [Application Integration Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`)
  * Create authentication profiles: [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) 
  * Edit authentication profiles: [Application Integration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationEditor) (`roles/integrations.integrationEditor`) 
  * Delete authentication profiles: [Application Integration Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/integrations#integrations.integrationAdmin) (`roles/integrations.integrationAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create OAuth 2.0 client ID

A client ID is used to identify a single application to Google's OAuth servers. If your application runs on multiple platforms, then each will need its own client ID. To use OAuth 2.0 in your application, you need an OAuth 2.0 client ID, which your application uses when requesting an OAuth 2.0 access token. 

To create an OAuth 2.0 client ID, do the following steps: 

  1. In the Google Cloud console, go to **APIs & Services > Credentials**. 

[Go to Credentials](https://console.cloud.google.com/apis/credentials)

  2. Click **\+ Create Credentials** and select **OAuth client ID** from the list of available options. 

The **Create OAuth client ID** page appears. 

  3. **Application type:** Select **Web Application** from the drop-down list.
  4. **Name:** Enter a name for your OAuth 2.0 client to identify the client in the Cloud console.
  5. Under **Authorized redirect URIs** , click **+Add URI** and enter the following: 
         
         https://console.cloud.google.com/integrations/callback/locations/AUTH_PROFILE_REGION

  6. Click **Create**. 

An OAuth 2.0 client ID is created successfully.




## Create a new authentication profile

To create a new authentication profile, select one of the following options: 

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Auth Profiles**. 

The **Authentication Profiles** page appears. 

  3. Click **Create** and enter the following details: 
     * In the **Profile name** field, enter the name of the authentication profile to be displayed in the integration editor.
     * From the **Region** list, select a region for the authentication profile.

The region you select here must be the same as the `AUTH_PROFILE_REGION` used in the **Authorized redirect URIs** when you created the OAuth 2.0 client ID.

     * In the **Description** field, enter a description for the authentication profile.
     * Click **Continue**. 
     * From the **Authentication type** list, select the authentication type and enter the required details. Based on your selection, the dialog displays additional fields required for the authentication credentials. You can select any of the following authentication types: 
       * Auth token
       * Google OIDC ID Token
       * JSON Web Token (JWT)
       * OAuth 2.0 authorization code
       * OAuth 2.0 client credentials
       * OAuth 2.0 resource owner password credentials
       * SSL/TLS client certification only
       * Service account
     * Optionally, you can add SSL/TLS client certificates that are used by the server to validate a client's identity. You can enter the following field: 
       1. **SSL certificate**
       2. **Private key**
       3. **Private key passphrase**
  4. Click **Create**.



### Terraform

Use the `[google_integrations_client](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/integrations_client)` resource. You can use terraform to create the following authentication profiles: 

  * Auth token
  * SSL/TLS client certification only
  * JSON Web Token (JWT)
  * OAuth 2.0 authorization code
  * OAuth 2.0 client credentials
  * OIDC ID token
  * Service account



**Auth token**

The following example creates a Auth token authentication type in the `us-central1` region:
    
    
    resource "google_integrations_client" "client" {
      location = "us-central1"
    }
    
    resource "google_integrations_auth_config" "auth_config_auth_token" {
      location     = "us-central1"
      display_name = "tf-auth-token"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "AUTH_TOKEN"
        auth_token {
          type  = "Basic"
          token = "some-random-token"
        }
      }
      depends_on = [google_integrations_client.client]
    }

**SSL/TLS client certification**

The following example creates a SSL/TLS client certification authentication type in the `us-central1` region:
    
    
    resource "google_integrations_auth_config" "auth_config_certificate" {
      location     = "us-central1"
      display_name = "tf-certificate"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "CLIENT_CERTIFICATE_ONLY"
      }
      client_certificate {
        ssl_certificate       = <<EOT
    -----BEGIN CERTIFICATE-----
    MIICTTCCAbagAwIBAgIJAPT0tSKNxan/MA0GCSqGSIb3DQEBCwUAMCoxFzAVBgNV
    BAoTDkdvb2dsZSBURVNUSU5HMQ8wDQYDVQQDEwZ0ZXN0Q0EwHhcNMTUwMTAxMDAw
    MDAwWhcNMjUwMTAxMDAwMDAwWjAuMRcwFQYDVQQKEw5Hb29nbGUgVEVTVElORzET
    MBEGA1UEAwwKam9lQGJhbmFuYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYEA
    vDYFgMgxi5W488d9J7UpCInl0NXmZQpJDEHE4hvkaRlH7pnC71H0DLt0/3zATRP1
    JzY2+eqBmbGl4/sgZKYv8UrLnNyQNUTsNx1iZAfPUflf5FwgVsai8BM0pUciq1NB
    xD429VFcrGZNucvFLh72RuRFIKH8WUpiK/iZNFkWhZ0CAwEAAaN3MHUwDgYDVR0P
    AQH/BAQDAgWgMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAMBgNVHRMB
    Af8EAjAAMBkGA1UdDgQSBBCVgnFBCWgL/iwCqnGrhTPQMBsGA1UdIwQUMBKAEKey
    Um2o4k2WiEVA0ldQvNYwDQYJKoZIhvcNAQELBQADgYEAYK986R4E3L1v+Q6esBtW
    JrUwA9UmJRSQr0N5w3o9XzarU37/bkjOP0Fw0k/A6Vv1n3vlciYfBFaBIam1qRHr
    5dMsYf4CZS6w50r7hyzqyrwDoyNxkLnd2PdcHT/sym1QmflsjEs7pejtnohO6N2H
    wQW6M0H7Zt8claGRla4fKkg=
    -----END CERTIFICATE-----
    EOT
        encrypted_private_key = <<EOT
    -----BEGIN PRIVATE KEY-----
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCA/Oj2HXqs5fTk
    j/8DrlOQtLG3K9RMsYHvnwICLxkGqVcTfut58hDFLbQM8C3C0ENAKitNJplCJmYG
    8VpgZzgq8VxaGnlP/sXUFLMGksd5sATn0sY3SkPndTKk/dqqA4MIh/dYfh19ynEN
    hB9Ll/h54Yic2je2Qaxe/uMMu8RODTz3oCn7FcoYpPvfygfU0ntn4IcqH/hts5DG
    s+3otJk4entRZglQDxR+sWOsbLtJIQZDP8rH3jDVdl5l3wspgtMTY8b5T5+pLm0p
    /OzCmxT0dq/O6BhpxI1xf/zcdRZeWk5DTJxTi5AgPquTlAG/B6A3HkqBJ14hT/Rk
    iv7Ma3DLAgMBAAECggEABATkf9VfpiAT9zYdouk50bBpckvymQTyQLD8SlBaX+KY
    kgv/pHSXK4Pm4iensrQerFLgfqPA3U+FiqjW5Mv7c1VRK6HJbuVkpdzoXLI9IQsL
    vsBY7//9Ajk5P7NokjdB6JPdU/2dHROuQVa59cxPtzpHo0htnPlDOKXfFZZuoZ17
    Nr8WQHrHy8P8ABM1tLOzvU9Nlh7TcjQvev+HxkLek4qzYyJ/Ac7XOjg/XKUm1tZk
    O3BHr8YLabwyjO7l1t+2b14rUTL/8pfUZnAkEi3FAlPxm3ilftmX65zliC9G4ghk
    dr5PByT3DqnuIIglua9bISv1H34ogecd+9a6EU7RxQKBgQC2RPKLounXZo8vYiU4
    sFTEvjbs+u9Ypk4OrNLnb8KdacLBUaJGnf++xbBoKpwFCBJfy//fvuQfusYF9Gyn
    GxL43tw94C/H5upQYnDsmnQak6TbOu3mA24OGK7Rcq6NEHgeCY4HomutnSiPTZJq
    8jlpqgqh1itETe5avgkMNq3zBwKBgQC1KlztGzvbB+rUDc6Kfvk5pUbCSFKMMMa2
    NWNXeD6i2iA56zEYSbTjKQ3u9pjUV8LNqAdUFxmbdPxZjheNK2dEm68SVRXPKOeB
    EmQT+t/EyW9LqBEA2oZt3h2hXtK8ppJjQm4XUCDs1NphP87eNzx5FLzJWjG8VqDq
    jOvApNqPHQKBgDQqlZSbgvvwUYjJOUf5R7mri0LWKwyfRHX0xsQQe43cCC6WM7Cs
    Zdbu86dMkqzp+4BJfalHFDl0llp782D8Ybiy6CwZbvNyxptNIW7GYfZ9TVCllBMh
    5izIqbgub4DWNtq591l+Bf2BnmstU3uiagYw8awSBP4eo9p6y1IgkDafAoGBAJbi
    lIiqEP0IqA06/pWc0Qew3rD7OT0ndqjU6Es2i7xovURf3QDkinJThBZNbdYUzdsp
    IgloP9yY33/a90SNLLIYlARJtyNVZxK59X4qiOpF9prlfFvgpOumfbkj15JljTB8
    aGKkSvfVA5jRYwLysDwMCHwO0bOR1u3itos5AgsFAoGAKEGms1kuQ5/HyFgSmg9G
    wBUzu+5Y08/A37rvyXsR6GjmlZJvULEopJNUNCOOpITNQikXK63sIFry7/59eGv5
    UwKadZbfwbVF5ipu59UxfVE3lipf/mYePDqMkHVWv/8p+OnnJt9uKnyW8VSOu5uk
    82QF30zbIWDTUjrcugVAs+E=
    -----END PRIVATE KEY-----
    EOT
      }
      depends_on = [google_integrations_client.client]
    }

**JSON Web Token (JWT)**

The following example creates a JSON Web Token (JWT) authentication type in the `us-central1` region:
    
    
    resource "google_integrations_auth_config" "auth_config_jwt" {
      location     = "us-central1"
      display_name = "tf-jwt"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "JWT"
        jwt {
          jwt_header  = "{\"alg\": \"HS256\", \"typ\": \"JWT\"}"
          jwt_payload = "{\"sub\": \"1234567890\", \"name\": \"John Doe\", \"iat\": 1516239022}"
          secret      = "secret"
        }
      }
      depends_on = [google_integrations_client.client]
    }

**OAuth 2.0 authorization code**

The following example creates a SSL/TLS client certification authentication type in the `us-central1` region:
    
    
    resource "google_integrations_auth_config" "auth_config_oauth2_authorization_code" {
      location     = "us-central1"
      display_name = "tf-oauth2-authorization-code"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "OAUTH2_AUTHORIZATION_CODE"
        oauth2_authorization_code {
          client_id      = "Kf7utRvgr95oGO5YMmhFOLo8"
          client_secret  = "D-XXFDDMLrg2deDgczzHTBwC3p16wRK1rdKuuoFdWqO0wliJ"
          scope          = "photo offline_access"
          auth_endpoint  = "https://authorization-server.com/authorize"
          token_endpoint = "https://authorization-server.com/token"
        }
      }
      depends_on = [google_integrations_client.client]
    }

**OAuth 2.0 client credentials**

The following example creates a OAuth 2.0 client credentials authentication type in the `us-central1` region:
    
    
    resource "google_integrations_auth_config" "auth_config_oauth2_client_credentials" {
      location     = "us-central1"
      display_name = "tf-oauth2-client-credentials"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "OAUTH2_CLIENT_CREDENTIALS"
        oauth2_client_credentials {
          client_id      = "demo-backend-client"
          client_secret  = "MJlO3binatD9jk1"
          scope          = "read"
          token_endpoint = "https://login-demo.curity.io/oauth/v2/oauth-token"
          request_type   = "ENCODED_HEADER"
          token_params {
            entries {
              key {
                literal_value {
                  string_value = "string-key"
                }
              }
              value {
                literal_value {
                  string_value = "string-value"
                }
              }
            }
          }
        }
      }
      depends_on = [google_integrations_client.client]
    }

**Google OIDC ID token**

The following example creates a Google OIDC ID token authentication type in the `us-central1` region:
    
    
    resource "random_id" "default" {
      byte_length = 8
    }
    
    resource "google_service_account" "service_account" {
      account_id   = "sa-${random_id.default.hex}"
      display_name = "Service Account"
    }
    
    resource "google_integrations_auth_config" "auth_config_oidc_token" {
      location     = "us-central1"
      display_name = "tf-oidc-token"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "OIDC_TOKEN"
        oidc_token {
          service_account_email = google_service_account.service_account.email
          audience = "https://us-central1-project.cloudfunctions.net/functionA 1234987819200.apps.googleusercontent.com"
        }
      }
    depends_on = [google_service_account.service_account, google_integrations_client.client]
    }
    

**Service account**

The following example creates a service account authentication type in the `us-central1` region:
    
    
    resource "random_id" "default" {
      byte_length = 8
    }
      
    resource "google_service_account" "service_account" {
      account_id   = "sa-${random_id.default.hex}"
      display_name = "Service Account"
    }
    resource "google_integrations_auth_config" "auth_config_service_account" {
      location     = "us-central1"
      display_name = "tf-service-account"
      description  = "Test auth config created via terraform"
      decrypted_credential {
        credential_type = "SERVICE_ACCOUNT"
        service_account_credentials {
        service_account = google_service_account.service_account.email
        scope = "https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/adexchange.buyer https://www.googleapis.com/auth/admob.readonly"
        }
      }
    depends_on = [google_service_account.service_account, google_integrations_client.client]
    }
    

After you save, the new authentication profile is available as an option in the **Authorization profile to use** drop-down of any task requiring authentication. 

_Optional_. If you have not created an authentication profile prior to configuring an integration task, you can access the profile creation dialog by selecting **\+ Add new authentication profile** from the **Authorization profile to use** drop-down in the task configuration pane. Follow the preceding steps to create a new authentication profile.

**Note:** When you associate a newly created or an updated authentication profile with a task in a draft integration, you must [publish the integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) for the changes to take effect during testing or execution. If you test the integration without publishing, the integration will continue to use the previously published authentication profile associated with the task.

## Edit authentication profiles

To edit an authentication profile, follow these steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Auth Profiles**. 

The **Authentication Profiles** page appears. 

  3. Select a **Region** for the authentication profile using the drop-down menu in the **Authentication Profiles** page.
  4. Click  more_vert  (Actions menu) and click **Edit**. 

The **Authentication Profiles** dialog appears. 

  5. Edit the details and click **Save**. 



When you edit an authentication profile, consider the following:

  * If you edit an authentication profile that is used by a task in a draft integration, [publish the integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) for the changes to take effect. When you test a draft integration, it will still use the authentication profile from the last published version.
  * If a task in an integration with a retry mechanism uses an authentication profile, [publish the integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) after updating the profile to ensure the task uses the updated profile.



## Delete authentication profiles

To delete an authentication profile, follow these steps:

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Auth Profiles**. 

The **Authentication Profiles** page appears. 

  3. Select a **Region** for the authentication profile using the drop-down menu in the **Authentication Profiles** page.
  4. Click **Delete**.



## Authentication types

The authentication type required to complete an integration task depends on the authentication configured in the authorization server. The authorization server can be a standalone server or an API that issues credentials to the calling client. Application Integration supports the following authentication types: 

  * Auth token
  * Google OIDC ID Token
  * JSON Web Token (JWT)
  * OAuth 2.0 authorization code
  * OAuth 2.0 client credentials
  * OAuth 2.0 resource owner password credentials
  * SSL/TLS client certification only
  * Service account



The following sections describe the configuration properties of the authentication types.

### Auth token

The **Auth token** authentication type uses a token (credentials) for authentication. The credentials are sent to the server in the HTTP `Authorization` request header in the `Authorization: TYPE CREDENTIALS` format. To configure this authentication type, set the following properties: 

  * **Type** : Authentication type such as `Basic`, `Bearer`, or `MAC`.
  * **Token** : Credentials for the authentication type.



If the authentication server requires an SSL/TLS certificate, upload the certificate and the private key. 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### Google OIDC ID Token

The **Google OIDC ID Token** authentication type uses JSON Web Tokens (JWT) for authentication. The Google OpenID Connect (OIDC) provider, _accounts.google.com_ , signs and issues these JWTs for authentication using a service account. To configure this authentication type, set the following properties: 

  * **Service account** : Service account (principal) in your Google Cloud project with permission to access your API. **Note:** Assign the **Service Account Token Creator** IAM role to the `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com` service account. For more information about assigning IAM roles, see [IAM roles and permissions](https://docs.cloud.google.com/application-integration/docs/integrations-access-permissions). 
  * **Audience** : The audience for the OIDC token (this identifies the recipients that the JWT is intended for). For example, _Trigger URL_ is the audience for the **Cloud Function** task. 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### JSON Web Token (JWT)

The **JWT** authentication type uses JSON Web Token (JWT) for authentication. For more information about JWT, see [RFC7519](https://tools.ietf.org/html/rfc7519). To configure this authentication type, set the following properties: 

  * **JWT header** : Algorithm used to generate the signature. 

**Note** : You can only specify the HS256 algorithm.

  * **JWT payload** : A set of claims. You can use registered, public, or custom claims.
  * **Secret** : Shared key between the client and the authentication server.



If the authentication server requires an SSL certificate, upload the certificate and the private key using the file picker. Enter the private key passphrase . 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### OAuth 2.0 authorization code

The **OAuth 2.0 authorization code** authentication type uses an `OAuth 2.0` authorization token for authentication. To configure this authentication type, set the following properties: 

  * **Authentication endpoint** : Endpoint to the application's authentication endpoint. You will be redirected to this URL to review the access permissions for the application. The token will only be generated after access is granted. 
  * **Token endpoint** : Endpoint that grants or refreshes the access token.
  * **Client ID** : A unique string provided by the authentication server to the registered client. The **Client ID** is not a secret, and it is exposed to the resource owner. Use this field along with a client secret.
  * **Secret** : Shared secret key between the client (integration) and the authentication server.
  * **Scope(s)** : Scope of the access token. Scopes let you specify access permissions for users. You can specify multiple scopes separated by a single space (" "). For more information, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).



If the authentication server requires an SSL certificate, upload the certificate and the private key using the file picker. Enter the private key passphrase in the available field, if required. 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### OAuth 2.0 client credentials

The **OAuth 2.0 client credentials** authentication type uses an `OAuth 2.0` authorization token for authentication. This authentication first requests an access token using the client credentials and then uses the token to access the protected resources. To configure this authentication type, set the following properties: 

  * **Token endpoint** : Endpoint that grants or refreshes the access token.
  * **Client ID** : A unique string provided by the authentication server to the registered client. The **Client ID** is not a secret, and it is exposed to the resource owner. Use this field along with a client secret.
  * **Secret** : Shared secret key between the client (integration) and the authentication server.
  * **Scope(s)** : Scope of the access token. Scopes let you specify access permissions for users. You can specify multiple scopes separated by a single space (" "). For more information, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).
  * **Request types** : Mechanisms to send the request parameters to the authentication server for fetching the access token. You can specify any of the following request types: 

    * **Encoder header** : Encodes the `CLIENT ID` and `CLIENT SECRET` in `Base64` format and sends the encoded string in the HTTP authorization header. The remaining request parameters are sent in the HTTP request body. 
    * **Query parameters** : Sends the request parameters in a query string.
    * **Request body** : Sends the request parameters by using the `application/x-www-form-urlencoded` content type and `UTF-8` charset in the `entity-body` of the HTTP request. 
    * **Unspecified**
  * **Token parameters** : Request parameters required to get the token. Specify the values in key-value format where `Key` is the parameter name and `Value` is the corresponding parameter value.



If the authentication server requires an SSL certificate, upload the certificate and the private key using the file picker. Enter the private key passphrase in the available field, if required. 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### OAuth 2.0 resource owner password credentials

The **OAuth 2.0 resource owner password credentials** authentication type uses an `OAuth 2.0` authorization token for authentication. This authentication first requests an access token using the resource owner credentials (Username and Password) and then uses the token to access the protected resources. To configure this authentication type, set the following properties based on the instance type that you connect to: 

  * **Token endpoint** : Endpoint that grants or refreshes the access token.
  * **Client ID** : A unique string provided by the authentication server to the registered client. The **Client ID** is not a secret, and it is exposed to the resource owner. Use this field along with a client secret.
  * **Secret** : Shared secret key between the client (integration) and the authentication server.
  * **Scope(s)** : Scope of the access token. Scopes let you specify access permissions for users. You can specify multiple scopes separated by a single space (" "). For more information, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).
  * **Username** : Username of the resource owner.
  * **Password** : User password.
  * **Request types** : Mechanisms to send the request parameters to the authentication server for fetching the access token. You can specify any of the following request types: 

    * **Encoder header** : Encodes the `CLIENT ID` and `CLIENT SECRET` in `Base64` format and sends the encoded string in the HTTP authorization header. Sends the remaining request parameters in the HTTP request body. 
    * **Query parameters** : Sends the request parameters in a query string.
    * **Request body** : Sends the request parameters by using the `application/x-www-form-urlencoded` content type and `UTF-8` charset in the `entity-body` of the HTTP request. 
  * **Token parameters** : Request parameters required to get the token. Specify the values in key-value format where `Key` is the parameter name and `Value` is the corresponding parameter value.



If the authentication server requires an SSL certificate, upload the certificate and the private key using the file picker. Enter the private key passphrase in the available field, if required. 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### SSL/TLS client certificate only

The **SSL/TLS client certificate only** authentication type uses only the SSL/TLS certificate for authentication. Upload the required certificate and the private key. To configure this authentication type, upload the following files: 

  * **SSL certificate** : Certificate encoded in PEM format.
  * **Private key** : Certificate's private key file encoded in PEM format. 

If the private key requires a `passphrase`, enter the **Private key passphrase**.


To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

### Service account

The **Service account** authentication type uses the credentials of a Google Cloud project's service account for authentication. To configure this authentication type, set the following properties: 

  * **Service account** : Service account (principal) in your Google Cloud project with permission to access your API. **Note:** Assign the **Service Account Token Creator** IAM role to the `service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com` service account. For more information about assigning IAM roles, see [IAM roles and permissions](https://docs.cloud.google.com/application-integration/docs/integrations-access-permissions). 
  * **Scope(s)** : Scope of the access permissions granted to users. You can specify multiple scopes separated by a single space (" "). For more information, see [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes).



To learn about best practices for creating and managing service accounts, read the [Best practices for working with service accounts documentation](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

If the authentication server requires an SSL certificate, upload the certificate and the private key using the file picker. Enter the private key passphrase in the available field, if required. 

To find out which tasks support this authentication type, see Compatibility of authentication types with tasks. 

## Compatibility of authentication types with tasks

The following table lists the authentication types and the corresponding compatible tasks. You can use this information to decide which authentication type to use for a task.

Authentication type  | Compatible tasks and triggers   
---|---  
Auth token | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)

  
Google OIDC ID Token | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)
  * [Cloud Function](https://docs.cloud.google.com/application-integration/docs/run-cloud-function-task)

  
JSON Web Token (JWT) | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)

  
OAuth 2.0 authorization code | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)
  * [Run Apps Script](https://docs.cloud.google.com/application-integration/docs/run-apps-script-task)
  * [Cloud Run functions task](https://docs.cloud.google.com/application-integration/docs/configure-cloud-function-task)

  
OAuth 2.0 client credentials | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)

  
OAuth 2.0 resource owner password credentials | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)
  * [Salesforce Trigger](https://docs.cloud.google.com/application-integration/docs/configuring-salesforce-cdc-trigger)

  
SSL/TLS client certificate only | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)

  
Service account | 

  * [Call REST Endpoint](https://docs.cloud.google.com/application-integration/docs/call-rest-endpoint-task)
  * [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task)
  * [Call Integration task](https://docs.cloud.google.com/application-integration/docs/configure-call-integration-task)
  * [Cloud Run functions task](https://docs.cloud.google.com/application-integration/docs/configure-cloud-function-task)

  
  
## Authentication rules

If your integration has both OAuth 2.0 profile and a user-managed service account configured, then by default the OAuth 2.0 profile is used for authentication. If neither OAuth 2.0 profile nor user-managed service account is configured, then the default service account (`service-PROJECT_NUMBER@gcp-sa-integrations.iam.gserviceaccount.com`) is used. If the task does not use the default service account, the execution fails.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
