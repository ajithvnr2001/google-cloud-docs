---
url: https://docs.cloud.google.com/iap/docs/authentication-howto/
title: Programmatic authentication \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:47.962336+00:00
---

# Programmatic authentication  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/authentication-howto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Programmatic authentication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to authenticate to an IAP-secured resource from a user account or a service account. 

Programmatic access refers to calling IAP-secured applications from non-browser clients, such as command-line tools, service-to-service calls, and mobile applications. Depending on your use case, you might want to authenticate to IAP using user credentials or service credentials.

  * A **user account** belongs to an individual user. You authenticate a user account when your application requires access to IAP-secured resources on a user's behalf. For more information, see [User accounts](https://docs.cloud.google.com/docs/authentication#user-accounts).

**Caution:** Only Google Identities are supported for user account programmatic access in IAP. Identity Platform and Workforce Identity Federation identities are not supported for programmatic access.


  * A **service account** represents an application instead of an individual user. You authenticate a service account when you want to allow an application to access your IAP-secured resources. For more information, see [Service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview).



IAP supports the following types of credentials for programmatic access:

* **OAuth 2.0 ID token** \- A Google-issued token for a human user or service account with the audience claim set to the resource ID of the IAP application. * **Service account signed JWT** \- A self-signed or Google-issued JWT token for a service account. 

Include these credentials to IAP in the `Authorization` or `Proxy-Authorization` HTTP header of the request.

## Before you begin

**Note:** If you configured your application to use the Google-managed OAuth 2.0 client (the default when IAP is enabled without a custom OAuth 2.0 client), you cannot use programmatic access. You don't own or have access to the credentials of the Google-managed client, which prevents the OAuth token exchange required for programmatic authentication. However, service accounts can still achieve programmatic access by using self-signed JSON Web Tokens (JWTs).

  1. Ensure you have an application that you want to access programmatically using a developer account, service account, or mobile app credentials.

  2. To create one or more OAuth 2.0 clients, see [Programmatic access](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients#programmatic_access).




## Authenticate a user account

You can enable user access to your application from a desktop or mobile app to allow a program to interact with an IAP-secured resource.

### Authenticate from a mobile app

  1. [Create](https://docs.cloud.google.com/iap/docs/oauth-client-creation) or use an existing OAuth 2.0 client ID for your mobile app. To use an existing OAuth 2.0 client ID, follow the steps in [How to share OAuth Clients](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients). Add the OAuth client ID to the allowlist for [programmatic access](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients#programmatic_access) to the application.
  2. Get an ID token for the OAuth 2.0 client ID of the IAP-secured resource. 
     * **Android** : Use the [Google Sign-In API](https://developers.google.com/identity/sign-in/android/) to request an [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect) (OIDC) token. Set the [`requestIdToken` client ID](https://developers.google.com/android/reference/com/google/android/gms/auth/api/signin/GoogleSignInOptions.Builder.html#requestIdToken\(java.lang.String\)) to the client ID for the resource you're connecting to.
     * **iOS** : Use [Google Sign-In](https://developers.google.com/identity/sign-in/ios/backend-auth) to get an ID token.
  3. Include the ID token in an `Authorization: Bearer` header to make the authenticated request to the IAP-secured resource.



### Authenticate from a desktop app

This section describes how to authenticate a user account from a desktop command line.

  1. To allow developers to access your application from the command line, [create a desktop OAuth 2.0 client ID](https://docs.cloud.google.com/iap/docs/oauth-client-creation) or [share an existing desktop OAuth client ID](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients).
  2. Add the OAuth ID to the allowlist for [programmatic access](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients#programmatic_access) for the application.



#### Sign in to the application

Each developer must sign in to access an IAP-secured app. You can package the process into a script, such as by using [gcloud CLI](https://docs.cloud.google.com/sdk/docs). The following example uses curl to sign in and generate a token that can be used to access the application:

  1. Sign in to your account that has access to the Google Cloud resource.
  2. Start a local server that can echo the incoming requests.
         
         # Example using Netcat (http://netcat.sourceforge.net/)
           nc -k -l 4444
         

  3. Go to the following URI, where `DESKTOP_CLIENT_ID` is the **Desktop app** client ID:
         
         https://accounts.google.com/o/oauth2/v2/auth?client_id=DESKTOP_CLIENT_ID&response_type=code&scope=openid%20email&access_type=offline&redirect_uri=http://localhost:4444&cred_ref=true
         

  4. In the local server output, look for the request parameters:
         
         GET /?code=CODE&scope=email%20openid%20https://www.googleapis.com/auth/userinfo.email&hd=google.com&prompt=consent HTTP/1.1
         

  5. Copy the **CODE** value to replace CODE in the following command, along with the **Desktop app** client ID and secret:
         
         curl --verbose \
             --data client_id=DESKTOP_CLIENT_ID \
             --data client_secret=DESKTOP_CLIENT_SECRET \
             --data code=CODE \
             --data redirect_uri=http://localhost:4444 \
             --data grant_type=authorization_code \
             https://oauth2.googleapis.com/token
         

This command returns a JSON object with an `id_token` field that you can use to access the application.




#### Access the application

To access the app, use the `id_token`:
    
    
    curl --verbose --header 'Authorization: Bearer ID_TOKEN' URL
    

#### Refresh token

You can use the refresh token generated during the sign-in flow to get new ID tokens. This is useful when the original ID token expires. Each ID token is valid for about one hour, during which time you can make multiple requests to a specific app.

The following example uses curl to use the refresh token to get a new ID token. In this example, `REFRESH_TOKEN` is the token from the sign-in flow. `DESKTOP_CLIENT_ID` and `DESKTOP_CLIENT_SECRET` are the same as used in the sign-in flow:
    
    
    curl --verbose \
      --data client_id=DESKTOP_CLIENT_ID \
      --data client_secret=DESKTOP_CLIENT_SECRET \
      --data refresh_token=REFRESH_TOKEN \
      --data grant_type=refresh_token \
      https://oauth2.googleapis.com/token
    

This command returns a JSON object with a new `id_token` field that you can use to access the app.

**Note:** The refresh token workflow is not supported for access level policies. You must regenerate a new ID token using the full authentication flow. 

## Authenticate a service account

You can use a [service account JWT](https://developers.google.com/identity/protocols/oauth2/service-account#jwt-auth) or an [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect) (OIDC) token to authenticate a service account with an IAP-secured resource. The following table outlines some of the differences between the different authentication tokens and their features. Authentication features | Service account JWT | OpenID Connect token  
---|---|---  
Context-aware access support |  |   
OAuth 2.0 Client ID requirement |  |   
Token scope | URL of IAP-secured resource | OAuth 2.0 client ID  
**Note:** Service accounts don't support [device policy attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#device-policy) with context-aware access. 

### Authenticate with a service account JWT

IAP supports service account JWT authentication for Google identities, Identity Platform, and Workforce Identity Federation configured applications. 

Authenticating a service account using a JWT involves the following steps:

  1. Grant the calling service account the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) role (`roles/iam.serviceAccountTokenCreator`).

**Warning:** To follow the principle of least privilege, we recommend that you grant the `roles/iam.serviceAccountTokenCreator` role on a specific target service account resource and not at the project level. Granting `roles/iam.serviceAccountTokenCreator` at the project level allows the principal (the calling service account) to create tokens for any service account within that project.

The role gives principals permission to create [short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#id), like JWTs.

  2. Create a JWT for the IAP-secured resource.

  3. Sign the JWT using the service account private key.




#### Create the JWT

The created JWT should have a payload similar to the following example:
    
    
    {
      "iss": SERVICE_ACCOUNT_EMAIL_ADDRESS,
      "sub": SERVICE_ACCOUNT_EMAIL_ADDRESS,
      "aud": TARGET_URL,
      "iat": IAT,
      "exp": EXP,
    }
    

  * For the `iss` and `sub` fields, specify the service account's email address. The email address is in the `client_email` field of the service account JSON file or is provided as input. Typical format: `service-account@PROJECT_ID.iam.gserviceaccount.com`

  * For the `aud` field, specify the exact URL or the URL with a path wildcard (`/*`) of the IAP-secured resource—for example, `https://example.com/` or `https://example.com/*`. A JWT with the exact URL in the `aud` field can only access that specific URL. A JWT with the path wildcard (`/*`) in the `aud` field can access all of the URLs that are prefixed with the `aud` string without the trailing `*`.

  * For the `iat` field, specify the current Unix epoch time, and for the `exp` field, specify a time within 3600 seconds later. This defines when the JWT expires.




#### Sign the JWT

You can use one of the following methods to sign the JWT:

  * Use the IAM credentials API to sign a JWT without requiring direct access to a private key.
  * Use a local credentials key file to sign the JWT locally.



##### Sign the JWT using IAM Service Account Credentials API

Use the IAM Service Account Credentials API to [sign a service account JWT](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/signJwt). The method fetches the private key associated with your service account and uses it to sign the JWT payload. This allows the signing of a JWT without direct access to a private key.

To authenticate to IAP, set up application default credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#local-dev).

### gcloud

  1. Run the following command to prepare a request with the JWT payload:


    
    
    cat > claim.json << EOM
    {
      "iss": "SERVICE_ACCOUNT_EMAIL_ADDRESS",
      "sub": "SERVICE_ACCOUNT_EMAIL_ADDRESS",
      "aud": "TARGET_URL",
      "iat": $(date +%s),
      "exp": $((`date +%s` + 3600))
    }
    EOM
    

  1. Use the following Google Cloud CLI command to sign the payload in `claim.json`:


    
    
    gcloud iam service-accounts sign-jwt --iam-account="SERVICE_ACCOUNT_EMAIL_ADDRESS" claim.json output.jwt
    

After a successful request, `output.jwt` contains a signed JWT that you can use to access your IAP-secured resource.

### Python
    
    
    import datetime
    import json
    
    import google.auth
    from google.cloud import [iam_credentials](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.html)_v1
    
    def generate_jwt_payload(service_account_email: str, resource_url: str) -> str:
        """Generates JWT payload for service account.
    
        Creates a properly formatted JWT payload with standard claims (iss, sub,
        aud, iat, exp) needed for IAP authentication.
    
        Args:
            service_account_email (str): Specifies the service account that the
            JWT is created for.
            resource_url (str): Specifies the scope of the JWT, the URL that the
            JWT will be allowed to access.
    
        Returns:
            str: JSON string containing the JWT payload with properly formatted
            claims.
        """
        # Create current time and expiration time (1 hour later) in UTC
        iat = datetime.datetime.now(tz=datetime.timezone.utc)
        exp = iat + datetime.timedelta(seconds=3600)
    
        # Convert datetime objects to numeric timestamps (seconds since epoch)
        # as required by JWT standard (RFC 7519)
        payload = {
            "iss": service_account_email,
            "sub": service_account_email,
            "aud": resource_url,
            "iat": int(iat.timestamp()),
            "exp": int(exp.timestamp()),
        }
    
        return json.dumps(payload)
    
    def sign_jwt(target_sa: str, resource_url: str) -> str:
        """Signs JWT payload using ADC and IAM credentials API.
    
        Uses Google Cloud's IAM Credentials API to sign a JWT. This requires the
        caller to have iap.webServiceVersions.accessViaIap permission on the
        target service account.
    
        Args:
            target_sa (str): Service Account JWT is being created for.
                iap.webServiceVersions.accessViaIap permission is required.
            resource_url (str): Audience of the JWT and scope of the JWT token.
                This is the URL of the IAP-secured application.
    
        Returns:
            str: A signed JWT that can be used to access IAP-secured applications.
                Use in Authorization header as: 'Bearer <signed_jwt>'
        """
        # Get default credentials from environment or application credentials
        source_credentials, project_id = google.auth.default()
    
        # Initialize IAM credentials client with source credentials
        iam_client = iam_credentials_v1.[IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html)(credentials=source_credentials)
    
        # Generate the service account resource name.
        # Project should always be "-".
        # Replacing the wildcard character with a project ID is invalid.
        name = iam_client.[service_account_path](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_service_account_path)("-", target_sa)
    
        # Create and sign the JWT payload
        payload = generate_jwt_payload(target_sa, resource_url)
    
        # Sign the JWT using the IAM credentials API
        response = iam_client.[sign_jwt](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.html#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_sign_jwt)(name=name, payload=payload)
    
        return response.signed_jwt
    

### curl

  1. Run the following command to prepare a request with the JWT payload:
         
         cat << EOF > request.json
         {
           "payload": JWT_PAYLOAD
         }
         EOF
         

  2. Sign the JWT using the IAM

Service Account Credentials API:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json; charset=utf-8" \
           -d @request.json \
           "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/SERVICE_ACCOUNT_EMAIL_ADDRESS:signJwt"
         

After a successful request, a signed JWT is returned in the response.

  3. Use the JWT to access your IAP-secured resource.


**Note:** Signing the JWT using the IAM credentials API requires a network call.

##### Sign the JWT from a local credential key file

JWTs are signed using the private key of the service account.

If you have a [service account key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys), the JWT can be signed locally.

When signing the JWT locally, include a JWT header with the payload. For the `kid` field in the header, use the service account's private key ID, which is in the `private_key_id` field of the service account credential JSON file. The private key from the file is used to sign the JWT.

#### Access the application

To access the application, include the signed JWT in the Authorization header:
    
    
    curl --verbose --header 'Authorization: Bearer SIGNED_JWT' URL
    

### Authenticate with a service account OIDC token

To authenticate with a service account OIDC token, do the following:

  1. Create a new OIDC client ID or use an existing one.

     * **To create a new OAuth 2.0 client ID, do the following** :

       1. Make sure that you have [registered](https://docs.cloud.google.com/iap/docs/custom-oauth-configuration#configure-branding) your application to use Google Auth, if you haven't already.

       2. Go to the Google Auth Platform page.

[Go to Google Auth Platform](https://console.cloud.google.com/auth/overview)

You will be prompted to create a project if you don't have one selected.

       3. Click **Create Client**.

       4. Select the appropriate application type and enter any additional information required.

       5. Fill out the required information for the selected client type. To create the client, click **Create**.

**Note:** The application's client secret is shown only once, after you create the client. Store this information in a secure place such as Secret Manager because it won't be visible or accessible again.
     * **To use an existing OAuth 2.0 client ID** : Follow the steps in [How to share OAuth Clients](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients).

  2. Add the OAuth ID to the allowlist for [programmatic access](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients#programmatic_access) for the application.

  3. Ensure that the default service account is added to the [access list](https://docs.cloud.google.com/iap/docs/managing-access) for the IAP-secured project.




When making requests to the IAP-secured resource, you must include the token in the `Authorization` header: `Authorization: 'Bearer OIDC_TOKEN'`

**Note:** The generated ID token must have an `email` claim for IAP to accept it.

The following code samples demonstrate how to obtain an OIDC token.

#### Obtain an OIDC token for the default service account

To get an OIDC token for the default service account for Compute Engine, App Engine, or Cloud Run, reference the following code sample to generate a token to access an IAP-secured resource:

### C#

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#local-dev).
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class IAPClient
    {
        /// <summary>
        /// Makes a request to a IAP secured application by first obtaining
        /// an OIDC token.
        /// </summary>
        /// <param name="iapClientId">The client ID observed on 
        /// https://console.cloud.google.com/apis/credentials. </param>
        /// <param name="uri">HTTP URI to fetch.</param>
        /// <param name="cancellationToken">The token to propagate operation cancel notifications.</param>
        /// <returns>The HTTP response message.</returns>
        public async Task<HttpResponseMessage> InvokeRequestAsync(
            string iapClientId, string uri, CancellationToken cancellationToken = default)
        {
            // Get the OidcToken.
            // You only need to do this once in your application
            // as long as you can keep a reference to the returned OidcToken.
            [OidcToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcToken.html) oidcToken = await GetOidcTokenAsync(iapClientId, cancellationToken);
    
            // Before making an HTTP request, always obtain the string token from the OIDC token,
            // the OIDC token will refresh the string token if it expires.
            string token = await oidcToken.[GetAccessTokenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcToken.html#Google_Apis_Auth_OAuth2_OidcToken_GetAccessTokenAsync_System_Threading_CancellationToken_)(cancellationToken);
    
            // Include the OIDC token in an Authorization: Bearer header to 
            // IAP-secured resource
            // Note: Normally you would use an HttpClientFactory to build the httpClient.
            // For simplicity we are building the HttpClient directly.
            using HttpClient httpClient = new HttpClient();
            httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", token);
            return await httpClient.GetAsync(uri, cancellationToken);
        }
    
        /// <summary>
        /// Obtains an OIDC token for authentication an IAP request.
        /// </summary>
        /// <param name="iapClientId">The client ID observed on 
        /// https://console.cloud.google.com/apis/credentials. </param>
        /// <param name="cancellationToken">The token to propagate operation cancel notifications.</param>
        /// <returns>The HTTP response message.</returns>
        public async Task<OidcToken> GetOidcTokenAsync(string iapClientId, CancellationToken cancellationToken)
        {
            // Obtain the application default credentials.
            [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html) credential = await [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefaultAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefaultAsync)(cancellationToken);
    
            // Request an OIDC token for the Cloud IAP-secured client ID.
           return await credential.[GetOidcTokenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetOidcTokenAsync_Google_Apis_Auth_OAuth2_OidcTokenOptions_System_Threading_CancellationToken_)([OidcTokenOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcTokenOptions.html).[FromTargetAudience](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.OidcTokenOptions.html#Google_Apis_Auth_OAuth2_OidcTokenOptions_FromTargetAudience_System_String_)(iapClientId), cancellationToken);
        }
    }
    

### Go

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"net/http"
    
    	"google.golang.org/api/idtoken"
    )
    
    // makeIAPRequest makes a request to an application protected by Identity-Aware
    // Proxy with the given audience.
    func makeIAPRequest(w io.Writer, request *http.Request, audience string) error {
    	// request, err := http.NewRequest("GET", "http://example.com", nil)
    	// audience := "IAP_CLIENT_ID.apps.googleusercontent.com"
    	ctx := context.Background()
    
    	// client is a http.Client that automatically adds an "Authorization" header
    	// to any requests made.
    	client, err := idtoken.NewClient(ctx, audience)
    	if err != nil {
    		return fmt.Errorf("idtoken.NewClient: %w", err)
    	}
    
    	response, err := client.Do(request)
    	if err != nil {
    		return fmt.Errorf("client.Do: %w", err)
    	}
    	defer response.Body.Close()
    	if _, err := io.Copy(w, response.Body); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	return nil
    }
    

### Java

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html);
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.[HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.auth.oauth2.[IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html);
    import com.google.auth.oauth2.[IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html);
    import com.google.common.base.Preconditions;
    import java.io.IOException;
    import java.util.Collections;
    
    public class BuildIapRequest {
      private static final String IAM_SCOPE = "https://www.googleapis.com/auth/iam";
    
      private static final [HttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html) httpTransport = new [NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html)();
    
      private BuildIapRequest() {}
    
      private static [IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html) getIdTokenProvider() throws IOException {
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials =
            [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)().createScoped(Collections.singleton(IAM_SCOPE));
    
        Preconditions.checkNotNull(credentials, "Expected to load credentials");
        Preconditions.checkState(
            credentials instanceof [IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html),
            String.format(
                "Expected credentials that can provide id tokens, got %s instead",
                credentials.getClass().getName()));
    
        return ([IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html)) credentials;
      }
    
      /**
       * Clone request and add an IAP Bearer Authorization header with ID Token.
       *
       * @param request Request to add authorization header
       * @param iapClientId OAuth 2.0 client ID for IAP protected resource
       * @return Clone of request with Bearer style authorization header with ID Token.
       * @throws IOException exception creating ID Token
       */
      public static [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) buildIapRequest([HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) request, String iapClientId)
          throws IOException {
    
        [IdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenProvider.html) idTokenProvider = getIdTokenProvider();
        [IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html) credentials =
            [IdTokenCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.html).newBuilder()
                .[setIdTokenProvider](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setIdTokenProvider_com_google_auth_oauth2_IdTokenProvider_)(idTokenProvider)
                .[setTargetAudience](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.IdTokenCredentials.Builder.html#com_google_auth_oauth2_IdTokenCredentials_Builder_setTargetAudience__org_jspecify_annotations_Nullable_java_lang_String_)(iapClientId)
                .build();
    
        [HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html) httpRequestInitializer = new [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)(credentials);
    
        return httpTransport
            .[createRequestFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpTransport.html#com_google_api_client_http_HttpTransport_createRequestFactory__)(httpRequestInitializer)
            .buildRequest(request.[getRequestMethod](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getRequestMethod__)(), request.[getUrl](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getUrl__)(), request.[getContent](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getContent__)());
      }
    }

### Node.js

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const url = 'https://some.iap.url';
    // const targetAudience = 'IAP_CLIENT_ID.apps.googleusercontent.com';
    
    const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    const auth = new [GoogleAuth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
    
    async function request() {
      console.info(`request IAP ${url} with target audience ${targetAudience}`);
      const client = await [auth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html).[getIdTokenClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)(targetAudience);
      const res = await client.fetch(url);
      console.info(res.data);
    }
    
    request().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace Google\Cloud\Samples\Iap;
    
    # Imports Auth libraries and Guzzle HTTP libraries.
    use Google\Auth\ApplicationDefaultCredentials;
    use GuzzleHttp\Client;
    use GuzzleHttp\HandlerStack;
    
    /**
     * Make a request to an application protected by Identity-Aware Proxy.
     *
     * @param string $url The Identity-Aware Proxy-protected URL to fetch.
     * @param string $clientId The client ID used by Identity-Aware Proxy.
     */
    function make_iap_request($url, $clientId)
    {
        // create middleware, using the client ID as the target audience for IAP
        $middleware = ApplicationDefaultCredentials::getIdTokenMiddleware($clientId);
        $stack = HandlerStack::create();
        $stack->push($middleware);
    
        // create the HTTP client
        $client = new Client([
            'handler' => $stack,
            'auth' => 'google_auth'
        ]);
    
        // make the request
        $response = $client->get($url);
        print('Printing out response body:');
        print($response->getBody());
    }

### Python

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.auth.transport.requests import Request
    from google.oauth2 import id_token
    import requests
    
    
    def make_iap_request(url, client_id, method="GET", **kwargs):
        """Makes a request to an application protected by Identity-Aware Proxy.
    
        Args:
          url: The Identity-Aware Proxy-protected URL to fetch.
          client_id: The client ID used by Identity-Aware Proxy.
          method: The request method to use
                  ('GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE')
          **kwargs: Any of the parameters defined for the request function:
                    https://github.com/requests/requests/blob/master/requests/api.py
                    If no timeout is provided, it is set to 90 by default.
    
        Returns:
          The page body, or raises an exception if the page couldn't be retrieved.
        """
        # Set the default timeout, if missing
        if "timeout" not in kwargs:
            kwargs["timeout"] = 90
    
        # Obtain an OpenID Connect (OIDC) token from metadata server or using service
        # account.
        open_id_connect_token = id_token.fetch_id_token(Request(), client_id)
    
        # Fetch the Identity-Aware Proxy-protected URL, including an
        # Authorization header containing "Bearer " followed by a
        # Google-issued OpenID Connect token for the service account.
        resp = requests.request(
            method,
            url,
            headers={"Authorization": "Bearer {}".format(open_id_connect_token)},
            **kwargs
        )
        if resp.status_code == 403:
            raise Exception(
                "Service account does not have permission to "
                "access the IAP-protected application."
            )
        elif resp.status_code != 200:
            raise Exception(
                "Bad response from application: {!r} / {!r} / {!r}".format(
                    resp.status_code, resp.headers, resp.text
                )
            )
        else:
            return resp.text
    
    

### Ruby

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # url = "The Identity-Aware Proxy-protected URL to fetch"
    # client_id = "The client ID used by Identity-Aware Proxy"
    require "googleauth"
    require "faraday"
    
    # The client ID as the target audience for IAP
    id_token_creds = Google::Auth::[Credentials](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Credentials.html).[default](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Credentials.html) target_audience: client_id
    
    headers = {}
    id_token_creds.[client](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-Credentials.html).apply! headers
    
    resp = Faraday.get url, nil, headers
    
    if resp.status == 200
      puts "X-Goog-Iap-Jwt-Assertion:"
      puts resp.body
    else
      puts "Error requesting IAP"
      puts resp.status
      puts resp.headers
    end

#### Obtain an OIDC token from a local service account key file

To generate an OIDC token using a service account key file, create and sign a JWT assertion using the key file and then exchange that assertion for an ID token. The following Bash script demonstrates this process:

### Bash
    
    
    #!/usr/bin/env bash
    #
    # Example script that generates an OIDC token using a service account key file and uses it to access an IAP-secured resource.
    
    set -euo pipefail
    
    get_token() {
      # Get the bearer token in exchange for the service account credentials
      local service_account_key_file_path="${1}"
      local iap_client_id="${2}"
    
      # Define the scope and token endpoint
      local iam_scope="https://www.googleapis.com/auth/iam"
      local oauth_token_uri="https://www.googleapis.com/oauth2/v4/token"
    
      # Extract data from service account key file
      local private_key_id="$(cat "${service_account_key_file_path}" | jq -r '.private_key_id')"
      local client_email="$(cat "${service_account_key_file_path}" | jq -r '.client_email')"
      local private_key="$(cat "${service_account_key_file_path}" | jq -r '.private_key')"
    
      # Set token timestamps (current time and expiration 10 minutes later)
      local issued_at="$(date +%s)"
      local expires_at="$((issued_at + 600))"
    
      # Create JWT header and payload
      local header="{'alg':'RS256','typ':'JWT','kid':'${private_key_id}'}"
      local header_base64="$(echo "${header}" | base64 | tr -d '\n')"
      local payload="{'iss':'${client_email}','aud':'${oauth_token_uri}','exp':${expires_at},'iat':${issued_at},'sub':'${client_email}','target_audience':'${iap_client_id}'}"
      local payload_base64="$(echo "${payload}" | base64 | tr -d '\n')"
    
      # Create JWT signature using the private key
      local signature_base64="$(printf %s "${header_base64}.${payload_base64}" | openssl dgst -binary -sha256 -sign <(printf '%s\n' "${private_key}")  | base64 | tr -d '\n')"
      local assertion="${header_base64}.${payload_base64}.${signature_base64}"
    
      # Exchange the signed JWT assertion for an ID token
      local token_payload="$(curl -s \
        --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer" \
        --data-urlencode "assertion=${assertion}" \
        https://www.googleapis.com/oauth2/v4/token)"
    
      # Extract just the ID token from the response
      local bearer_id_token="$(echo "${token_payload}" | jq -r '.id_token')"
      echo "${bearer_id_token}"
    }
    
    main() {
      # Check if required arguments are provided
      if [[ $# -lt 3 ]]; then
        echo "Usage: $0 <service_account_key_file.json> <iap_client_id> <url>"
        exit 1
      fi
    
      # Assign parameters to variables
      SERVICE_ACCOUNT_KEY="$1"
      IAP_CLIENT_ID="$2"
      URL="$3"
    
      # Generate the ID token
      echo "Generating token..."
      ID_TOKEN=$(get_token "${SERVICE_ACCOUNT_KEY}" "${IAP_CLIENT_ID}")
    
      # Access the IAP-secured resource with the token
      echo "Accessing: ${URL}"
      curl --header "Authorization: Bearer ${ID_TOKEN}" "${URL}"
    }
    
    # Run the main function with all provided arguments
    main "$@"
    

This script performs the following steps:

  1. Extracts the service account key information from your JSON key file
  2. Creates a JWT with the necessary fields, including the IAP client ID as the target audience
  3. Signs the JWT using the service account's private key
  4. Exchanges this JWT for an OIDC token through Google's OAuth service
  5. Uses the resulting token to make an authenticated request to your IAP-secured resource



To use this script:

  1. Save it to a file, for example: `get_iap_token.sh`
  2. Make it executable: `chmod +x get_iap_token.sh`
  3. Run it with three parameters:


    
    
      ./get_iap_token.sh service-account-key.json \
        OAUTH_CLIENT_ID \
        URL
    

Where:

  * `service-account-key.json` is your downloaded service account key file
  * OAUTH_CLIENT_ID is the OAuth client ID for your IAP-secured resource
  * URL is the URL you want to access



#### Obtain an OIDC token by using service account impersonation

In all other cases, use the IAM credentials API to [generate an OIDC token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#id) by impersonating a target service account right before accessing an IAP-secured resource. This process involves the following steps:

  1. Provide the calling service account (the service account associated with the code that is obtaining the ID token) with the Service Account OpenID Connect Identity Token Creator role (`roles/iam.serviceAccountOpenIdTokenCreator`).

This gives the calling service account the ability to impersonate the target service account.

  2. Use the credentials provided by the calling service account to call the [generateIdToken](https://docs.cloud.google.com/iam/docs/reference/credentials/rest/v1/projects.serviceAccounts/generateIdToken) method on the target service account.

Set the `audience` field to your client ID.




For step-by-step instructions, see [Create an ID token](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#id). 

## Authenticate from Proxy-Authorization Header

If your application uses the `Authorization` request header, you can include the ID token in a `Proxy-Authorization: Bearer` header instead. If a valid ID token is found in a `Proxy-Authorization` header, IAP authorizes the request with it. After authorizing the request, IAP passes the `Authorization` header to your application without processing the content.

If no valid ID token is found in the `Proxy-Authorization` header, IAP continues to process the `Authorization` header and strips the `Proxy-Authorization` header before passing the request to your application.

#### Access the application

To access the application by using the `Proxy-Authorization` header, run the following command:
    
    
    curl --verbose --header 'Proxy-Authorization: Bearer SIGNED_JWT' URL
    

## What's next

  * Learn more about [Authorization: Bearer Tokens](https://developers.google.com/gmail/markup/actions/verifying-bearer-tokens). 
  * Try [Sign-In for Android](https://developers.google.com/identity/sign-in/android/start) or [Sign-In for iOS](https://developers.google.com/identity/sign-in/ios/start). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
