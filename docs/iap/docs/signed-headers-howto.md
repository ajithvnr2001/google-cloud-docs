---
url: https://docs.cloud.google.com/iap/docs/signed-headers-howto/
title: Securing your app with signed headers \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:22.004852+00:00
---

# Securing your app with signed headers  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/signed-headers-howto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Securing your app with signed headers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to secure your app with signed IAP headers. When configured, Identity-Aware Proxy (IAP) uses JSON Web Tokens (JWT) to make sure that a request to your app is authorized. This protects your app from the following risks:

  * IAP is accidentally disabled
  * Misconfigured firewalls
  * Unauthorized access from within the project



To help secure your app, you must use signed headers for all app types.

Alternatively, if you have an App Engine standard environment app, you can use the [Users API](https://docs.cloud.google.com/iap/docs/identity-howto#get_identity_gae). 

Compute Engine and GKE health checks don't include JWT headers and IAP doesn't process health checks. If your health check returns access errors, make sure that you have the health check configured correctly in the Google Cloud console and that your JWT header validation allows the health check path. For more information, see [Create a health check exception](https://docs.cloud.google.com/iap/docs/signed-headers-howto#health-check-exception).

## Before you begin

To secure your app with signed headers, you'll need the following:

  * An application that you want users to connect to.
  * A [third-party JWT library for your language](https://jwt.io/) that supports the `ES256` algorithm.



## Securing your app with IAP headers

To secure your app with the IAP JWT, verify the header, payload, and signature of the JWT. The JWT is in the HTTP request header `x-goog-iap-jwt-assertion`. If an attacker bypasses IAP, the attacker can forge the IAP unsigned identity headers, `x-goog-authenticated-user-{email,id}`. The IAP JWT provides a more secure alternative.

Signed headers provide secondary security in case someone bypasses IAP. When IAP is enabled, IAP strips the `x-goog-*` headers provided by the client when the request goes through the IAP serving infrastructure.

### Verifying the JWT header

Verify that the JWT's header conforms to the following constraints:

JWT Header Claims  
---  
`alg` | Algorithm | `ES256`  
`kid` | Key ID |  Must correspond to one of the public keys listed in the IAP key file, available in two different formats: `https://www.gstatic.com/iap/verify/public_key` and `https://www.gstatic.com/iap/verify/public_key-jwk`  
  
Ensure that the JWT was signed by the private key that corresponds to the token's `kid` claim. First, retrieve the public key from one of two places:

  * `https://www.gstatic.com/iap/verify/public_key`. This URL contains a JSON dictionary that maps the `kid` claims to the public key values.
  * `https://www.gstatic.com/iap/verify/public_key-jwk`. This URL contains the IAP public keys in [JWK](https://tools.ietf.org/html/rfc7517) format.



After you have the public key, use a JWT library to verify the signature.

IAP periodically rotates its public keys. To make sure that you can always verify the JWTs, see Automate public key caching.

### Verifying the JWT payload

Verify the JWT's payload conforms to the following constraints:

JWT Payload Claims  
---  
`exp` | Expiration time |  Must be in the future. The time is measured in seconds since the UNIX epoch. Allow 30 seconds for skew. _The maximum lifetime of a token is 10 minutes + 2 * skew._  
`iat` | Issued-at time |  Must be in the past. The time is measured in seconds since the UNIX epoch. Allow 30 seconds for skew.   
`aud` | Audience |  Must be a string with the following values: 

  * App Engine: `/projects/PROJECT_NUMBER/apps/PROJECT_ID`
  * Compute Engine and GKE: `/projects/PROJECT_NUMBER/global/backendServices/SERVICE_ID`
  * Cloud Run: `/projects/PROJECT_NUMBER/locations/REGION/services/SERVICE_NAME`

  
`iss` | Issuer |  Must be `https://cloud.google.com/iap`.   
`hd` | Account domain |  If an account belongs to a hosted domain, the `hd` claim is provided to differentiate the domain the account is associated with.   
`google` | Google claim |  If one or more [access levels](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) apply to the request, their names are stored within the `google` claim's JSON object, under the `access_levels` key, as an array of strings. When you specify a device policy and the Org has access to the device data, the `DeviceId` is also stored in the JSON object. Note that a request going to another Org might not have permission to view the device data.  
You can get the values for the `aud` string mentioned above by accessing the Google Cloud console, or you can use the Google Cloud CLI. 

To get `aud` string values from the Google Cloud console, go to the [Identity-Aware Proxy settings](https://console.cloud.google.com/security/iap/) for your project, click **More** next to the Load Balancer resource, and then select **Signed Header JWT Audience**. The **Signed Header JWT** dialog that appears shows the `aud` claim for the selected resource. 

To use the [gcloud CLI](https://docs.cloud.google.com/sdk/downloads) to get the `aud` string values, you need to know the project ID. You can find the project ID on the [Google Cloud console](https://console.cloud.google.com/) **Project info** card, then run the specified commands for each value.

**Project number**

To get your project number using the gcloud CLI, run the following command:

`gcloud projects describe PROJECT_ID`

The command returns output like the following:
    
    
    createTime: '2016-10-13T16:44:28.170Z'
    lifecycleState: ACTIVE
    name: project_name
    parent:
      id: '433637338589'
      type: organization
    projectId: PROJECT_ID
    **projectNumber : 'PROJECT_NUMBER'**

**Service ID**

To get your service ID using the gcloud CLI, run the following command:

`gcloud compute backend-services describe SERVICE_NAME --project=PROJECT_ID --global`

The command returns output like the following:
    
    
    affinityCookieTtlSec: 0
    backends:
    - balancingMode: UTILIZATION
      capacityScaler: 1.0
      group: https://www.googleapis.com/compute/v1/projects/project_name/regions/us-central1/instanceGroups/my-group
    connectionDraining:
      drainingTimeoutSec: 0
    creationTimestamp: '2017-04-03T14:01:35.687-07:00'
    description: ''
    enableCDN: false
    fingerprint: zaOnO4k56Cw=
    healthChecks:
    - https://www.googleapis.com/compute/v1/projects/project_name/global/httpsHealthChecks/my-hc
    **id : 'SERVICE_ID'**
    kind: compute#backendService
    loadBalancingScheme: EXTERNAL
    name: my-service
    port: 8443
    portName: https
    protocol: HTTPS
    selfLink: https://www.googleapis.com/compute/v1/projects/project_name/global/backendServices/my-service
    sessionAffinity: NONE
    timeoutSec: 3610

### Retrieving the user identity

If all of the preceding verifications are successful, retrieve the user identity. The ID token's payload contains the following user information:

ID Token Payload User Identity  
---  
`sub` | Subject |  The unique, stable identifier for the user. Use this value instead of the `x-goog-authenticated-user-id` header.   
`email` | User email | User email address. 

  * Use this value instead of the `x-goog-authenticated-user-email` header. 
  * Unlike that header and the `sub` claim, this value doesn't have a namespace prefix. 

  
  
Following is sample code to secure an app with signed IAP headers:

### C#
    
    
    using [Google.Apis.Auth](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.html);
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class IAPTokenVerification
    {
        /// <summary>
        /// Verifies a signed jwt token and returns its payload.
        /// </summary>
        /// <param name="signedJwt">The token to verify.</param>
        /// <param name="expectedAudience">The audience that the token should be meant for.
        /// Validation will fail if that's not the case.</param>
        /// <param name="cancellationToken">The cancellation token to propagate cancellation requests.</param>
        /// <returns>A task that when completed will have as its result the payload of the verified token.</returns>
        /// <exception cref="InvalidJwtException">If verification failed. The message of the exception will contain
        /// information as to why the token failed.</exception>
        public async Task<JsonWebSignature.Payload> VerifyTokenAsync(
            string signedJwt, string expectedAudience, CancellationToken cancellationToken = default)
        {
            [SignedTokenVerificationOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.SignedTokenVerificationOptions.html) options = new [SignedTokenVerificationOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.SignedTokenVerificationOptions.html)
            {
                // Use clock tolerance to account for possible clock differences
                // between the issuer and the verifier.
                IssuedAtClockTolerance = TimeSpan.FromMinutes(1),
                ExpiryClockTolerance = TimeSpan.FromMinutes(1),
                TrustedAudiences = { expectedAudience },
                TrustedIssuers = { "https://cloud.google.com/iap" },
                CertificatesUrl = [GoogleAuthConsts](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleAuthConsts.html).[IapKeySetUrl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleAuthConsts.html#Google_Apis_Auth_OAuth2_GoogleAuthConsts_IapKeySetUrl),
            };
    
            return await [JsonWebSignature](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.JsonWebSignature.html).[VerifySignedTokenAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.JsonWebSignature.html#Google_Apis_Auth_JsonWebSignature_VerifySignedTokenAsync_System_String_Google_Apis_Auth_SignedTokenVerificationOptions_System_Threading_CancellationToken_)(signedJwt, options, cancellationToken: cancellationToken);
        }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"google.golang.org/api/idtoken"
    )
    
    // validateJWTFromAppEngine validates a JWT found in the
    // "x-goog-iap-jwt-assertion" header.
    func validateJWTFromAppEngine(w io.Writer, iapJWT, projectNumber, projectID string) error {
    	// iapJWT := "YmFzZQ==.ZW5jb2RlZA==.and0" // req.Header.Get("X-Goog-IAP-JWT-Assertion")
    	// projectNumber := "123456789"
    	// projectID := "your-project-id"
    	ctx := context.Background()
    	aud := fmt.Sprintf("/projects/%s/apps/%s", projectNumber, projectID)
    
    	payload, err := idtoken.Validate(ctx, iapJWT, aud)
    	if err != nil {
    		return fmt.Errorf("idtoken.Validate: %w", err)
    	}
    
    	// payload contains the JWT claims for further inspection or validation
    	fmt.Fprintf(w, "payload: %v", payload)
    
    	return nil
    }
    
    // validateJWTFromComputeEngine validates a JWT found in the
    // "x-goog-iap-jwt-assertion" header.
    func validateJWTFromComputeEngine(w io.Writer, iapJWT, projectNumber, backendServiceID string) error {
    	// iapJWT := "YmFzZQ==.ZW5jb2RlZA==.and0" // req.Header.Get("X-Goog-IAP-JWT-Assertion")
    	// projectNumber := "123456789"
    	// backendServiceID := "backend-service-id"
    	ctx := context.Background()
    	aud := fmt.Sprintf("/projects/%s/global/backendServices/%s", projectNumber, backendServiceID)
    
    	payload, err := idtoken.Validate(ctx, iapJWT, aud)
    	if err != nil {
    		return fmt.Errorf("idtoken.Validate: %w", err)
    	}
    
    	// payload contains the JWT claims for further inspection or validation
    	fmt.Fprintf(w, "payload: %v", payload)
    
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html);
    import com.google.api.client.json.webtoken.[JsonWebToken](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.html);
    import com.google.auth.oauth2.[TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html);
    
    /** Verify IAP authorization JWT token in incoming request. */
    public class VerifyIapRequestHeader {
    
      private static final String IAP_ISSUER_URL = "https://cloud.google.com/iap";
    
      // Verify jwt tokens addressed to IAP protected resources on App Engine.
      // The project *number* for your Google Cloud project via 'gcloud projects describe $PROJECT_ID'
      // The project *number* can also be retrieved from the Project Info card in Cloud Console.
      // projectId is The project *ID* for your Google Cloud Project.
      boolean verifyJwtForAppEngine([HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) request, long projectNumber, String projectId)
          throws Exception {
        // Check for iap jwt header in incoming request
        String jwt = request.[getHeaders](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getHeaders__)().[getFirstHeaderStringValue](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpHeaders.html#com_google_api_client_http_HttpHeaders_getFirstHeaderStringValue_java_lang_String_)("x-goog-iap-jwt-assertion");
        if (jwt == null) {
          return false;
        }
        return verifyJwt(
            jwt,
            String.format("/projects/%s/apps/%s", Long.toUnsignedString(projectNumber), projectId));
      }
    
      boolean verifyJwtForComputeEngine([HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html) request, long projectNumber, long backendServiceId)
          throws Exception {
        // Check for iap jwt header in incoming request
        String jwtToken = request.[getHeaders](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequest.html#com_google_api_client_http_HttpRequest_getHeaders__)().[getFirstHeaderStringValue](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpHeaders.html#com_google_api_client_http_HttpHeaders_getFirstHeaderStringValue_java_lang_String_)("x-goog-iap-jwt-assertion");
        if (jwtToken == null) {
          return false;
        }
        return verifyJwt(
            jwtToken,
            String.format(
                "/projects/%s/global/backendServices/%s",
                Long.toUnsignedString(projectNumber), Long.toUnsignedString(backendServiceId)));
      }
    
      private boolean verifyJwt(String jwtToken, String expectedAudience) {
        [TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html) tokenVerifier =
            [TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html).newBuilder().setAudience(expectedAudience).setIssuer(IAP_ISSUER_URL).build();
        try {
          [JsonWebToken](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.html) jsonWebToken = tokenVerifier.[verify](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html#com_google_auth_oauth2_TokenVerifier_verify_java_lang_String_)(jwtToken);
    
          // Verify that the token contain subject and email claims
          [JsonWebToken](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.html).[Payload](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.Payload.html) payload = jsonWebToken.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.html#com_google_api_client_json_webtoken_JsonWebToken_getPayload__)();
          return payload.[getSubject](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.webtoken.JsonWebToken.Payload.html#com_google_api_client_json_webtoken_JsonWebToken_Payload_getSubject__)() != null && payload.get("email") != null;
        } catch ([TokenVerifier](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.html).[VerificationException](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.TokenVerifier.VerificationException.html) e) {
          System.out.println(e.getMessage());
          return false;
        }
      }
    }

### Node.js
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const iapJwt = 'SOME_ID_TOKEN'; // JWT from the "x-goog-iap-jwt-assertion" header
    
    let expectedAudience = null;
    if (projectNumber && projectId) {
      // Expected Audience for App Engine.
      expectedAudience = `/projects/${projectNumber}/apps/${projectId}`;
    } else if (projectNumber && backendServiceId) {
      // Expected Audience for Compute Engine
      expectedAudience = `/projects/${projectNumber}/global/backendServices/${backendServiceId}`;
    }
    
    const oAuth2Client = new OAuth2Client();
    
    async function verify() {
      // Verify the id_token, and access the claims.
      const response = await oAuth2Client.getIapPublicKeys();
      const ticket = await oAuth2Client.verifySignedJwtWithCertsAsync(
        iapJwt,
        response.pubkeys,
        expectedAudience,
        ['https://cloud.google.com/iap'],
      );
      // Print out the info contained in the IAP ID token
      console.log(ticket);
    }
    
    verify().catch(console.error);
    

### PHP
    
    
    namespace Google\Cloud\Samples\Iap;
    
    # Imports Google auth libraries for IAP validation
    use Google\Auth\AccessToken;
    
    /**
     * Validate a JWT passed to your App Engine app by Identity-Aware Proxy.
     *
     * @param string $iapJwt The contents of the X-Goog-IAP-JWT-Assertion header.
     * @param string $cloudProjectNumber The project *number* for your Google
     *     Cloud project. This is returned by 'gcloud projects describe $PROJECT_ID',
     *     or in the Project Info card in Cloud Console.
     * @param string $cloudProjectId Your Google Cloud Project ID.
     */
    function validate_jwt_from_app_engine(
        string $iapJwt,
        string $cloudProjectNumber,
        string $cloudProjectId
    ): void {
        $expectedAudience = sprintf(
            '/projects/%s/apps/%s',
            $cloudProjectNumber,
            $cloudProjectId
        );
        validate_jwt($iapJwt, $expectedAudience);
    }
    
    /**
     * Validate a JWT passed to your Compute / Container Engine app by Identity-Aware Proxy.
     *
     * @param string $iapJwt The contents of the X-Goog-IAP-JWT-Assertion header.
     * @param string $cloudProjectNumber The project *number* for your Google
     *     Cloud project. This is returned by 'gcloud projects describe $PROJECT_ID',
     *     or in the Project Info card in Cloud Console.
     * @param string $backendServiceId The ID of the backend service used to access the
     *     application. See https://cloud.google.com/iap/docs/signed-headers-howto
     *     for details on how to get this value.
     */
    function validate_jwt_from_compute_engine(
        string $iapJwt,
        string $cloudProjectNumber,
        string $backendServiceId
    ): void {
        $expectedAudience = sprintf(
            '/projects/%s/global/backendServices/%s',
            $cloudProjectNumber,
            $backendServiceId
        );
        validate_jwt($iapJwt, $expectedAudience);
    }
    
    /**
     * Validate a JWT passed to your app by Identity-Aware Proxy.
     *
     * @param string $iapJwt The contents of the X-Goog-IAP-JWT-Assertion header.
     * @param string $expectedAudience The expected audience of the JWT with the following formats:
     *     App Engine:     /projects/{PROJECT_NUMBER}/apps/{PROJECT_ID}
     *     Compute Engine: /projects/{PROJECT_NUMBER}/global/backendServices/{BACKEND_SERVICE_ID}
     */
    function validate_jwt(string $iapJwt, string $expectedAudience): void
    {
        // Validate the signature using the IAP cert URL.
        $token = new AccessToken();
        $jwt = $token->verify($iapJwt, [
            'certsLocation' => AccessToken::IAP_CERT_URL
        ]);
    
        if (!$jwt) {
            print('Failed to validate JWT: Invalid JWT');
            return;
        }
    
        // Validate token by checking issuer and audience fields.
        assert($jwt['iss'] == 'https://cloud.google.com/iap');
        assert($jwt['aud'] == $expectedAudience);
    
        print('Printing user identity information from ID token payload:');
        printf('sub: %s', $jwt['sub']);
        printf('email: %s', $jwt['email']);
    }

### Python
    
    
    from google.auth.transport import requests
    from google.oauth2 import id_token
    
    
    def validate_iap_jwt(iap_jwt, expected_audience):
        """Validate an IAP JWT.
    
        Args:
          iap_jwt: The contents of the X-Goog-IAP-JWT-Assertion header.
          expected_audience: The Signed Header JWT audience. See
              https://cloud.google.com/iap/docs/signed-headers-howto
              for details on how to get this value.
    
        Returns:
          (user_id, user_email, error_str).
        """
    
        try:
            decoded_jwt = id_token.verify_token(
                iap_jwt,
                requests.Request(),
                audience=expected_audience,
                certs_url="https://www.gstatic.com/iap/verify/public_key",
            )
            return (decoded_jwt["sub"], decoded_jwt["email"], "")
        except Exception as e:
            return (None, None, f"**ERROR: JWT validation error {e}**")
    
    

### Ruby
    
    
    # iap_jwt = "The contents of the X-Goog-Iap-Jwt-Assertion header"
    # project_number = "The project *number* for your Google Cloud project"
    # project_id = "Your Google Cloud project ID"
    # backend_service_id = "Your Compute Engine backend service ID"
    require "googleauth"
    
    audience = nil
    if project_number && project_id
      # Expected audience for App Engine
      audience = "/projects/#{project_number}/apps/#{project_id}"
    elsif project_number && backend_service_id
      # Expected audience for Compute Engine
      audience = "/projects/#{project_number}/global/backendServices/#{backend_service_id}"
    end
    
    # The client ID as the target audience for IAP
    payload = Google::Auth::[IDTokens](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html).[verify_iap](https://docs.cloud.google.com/ruby/docs/reference/googleauth/latest/Google-Auth-IDTokens.html) iap_jwt, aud: audience
    
    puts payload
    
    if audience.nil?
      puts "Audience not verified! Supply a project_number and project_id to verify"
    end

### Testing your validation code

If you visit your app using the [`secure_token_test` query parameters](https://docs.cloud.google.com/iap/docs/query-parameters-and-headers-howto#testing-jwt-verification), IAP will include an invalid JWT. Use this to make sure your JWT-validation logic is handling all of the various failure cases and to see how your app behaves when it receives an invalid JWT.

### Creating a health check exception

As mentioned previously, Compute Engine and GKE health checks don't use JWT headers and IAP doesn't handle health checks. You'll need to configure your [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks) and app to allow the health check access.

#### Configuring the health check

If you haven't already set a path for your health check, use the Google Cloud console to set a non-sensitive path for the health check. Make sure this path isn't shared by any other resource.

  1. Go to the Google Cloud console [Health checks](https://console.cloud.google.com/compute/healthChecks) page.   
[Go to the Health checks page](https://console.cloud.google.com/compute/healthChecks)
  2. Click the health check you're using for your app, then click **Edit**.
  3. Under **Request path** add a non-sensitive path name. This specifies the URL path that Google Cloud uses when sending health check requests. If omitted, the health check request is sent to `/`.
  4. Click **Save**.



#### Configuring the JWT validation

In your code that calls the JWT validation routine, add a condition to serve an 200 HTTP status for your health check request path. For example:
    
    
    if HttpRequest.path_info = '/HEALTH_CHECK_REQUEST_PATH'
      return HttpResponse(status=200)
    else
      VALIDATION_FUNCTION

### Automate public key caching

IAP rotates its public keys periodically. To ensure you can always verify the IAP JWT, we recommend that you cache the keys to avoid fetching them from the public URL for each request and that you automate the process of updating the cached key. This approach is particularly useful for applications that run in an environment with network restrictions, like a VPC Service Controls perimeter.

A VPC Service Controls perimeter can prevent direct access to the public URL for the keys. By caching the keys in a Cloud Storage bucket, your applications can fetch them from a location within your VPC-SC perimeter.

The following Terraform configuration deploys a function to Cloud Run that fetches the latest IAP public keys from `https://www.gstatic.com/iap/verify/public_key-jwk` and stores them in a Cloud Storage bucket. A Cloud Scheduler job triggers this function every 12 hours to keep the keys up to date.

This setup includes the following: 

  * Necessary Google Cloud APIs enabled to use Cloud Run and store and cache keys
  * A Cloud Storage bucket to store the fetched IAP public keys
  * A Cloud Storage bucket to stage Cloud Run functions source code
  * Service accounts for Cloud Run functions and Cloud Scheduler with appropriate IAM permissions
  * A Python function to fetch and store keys
  * A Cloud Scheduler job to trigger the function every 12 hours



#### Directory structure
    
    
    ├── function_source/
    │   ├── main.py
    │   └── requirements.txt
    ├── main.tf
    ├── outputs.tf
    ├── variables.tf
    └── terraform.tfvars
    

#### `function_source/main.py`
    
    
    import functions_framework
    import requests
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import os
    
    # Environment variables to be set in the function configuration
    BUCKET_NAME = os.environ.get("BUCKET_NAME")
    OBJECT_NAME = os.environ.get("OBJECT_NAME", "iap_public_keys.jwk")
    IAP_KEYS_URL = "https://www.gstatic.com/iap/verify/public_key-jwk"
    
    @functions_framework.http
    def update_iap_keys(request):
        """Fetches IAP public keys from the public URL and stores them in a Cloud Storage bucket."""
        if not BUCKET_NAME:
            print("Error: BUCKET_NAME environment variable not set.")
            return "BUCKET_NAME environment variable not set.", 500
    
        try:
            # Fetch the keys
            response = requests.get(IAP_KEYS_URL)
            response.raise_for_status()  # Raise an exception for bad status codes
            keys_content = response.text
            print(f"Successfully fetched keys from {IAP_KEYS_URL}")
    
            # Store in Cloud Storage
            storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
            bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(BUCKET_NAME)
            blob = bucket.blob(OBJECT_NAME)
    
            blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(keys_content, content_type='application/json')
    
            print(f"Successfully wrote IAP keys to gs://{BUCKET_NAME}/{OBJECT_NAME}")
            return f"Successfully updated {OBJECT_NAME} in bucket {BUCKET_NAME}", 200
    
        except requests.[exceptions](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.exceptions.html).RequestException as e:
            print(f"Error fetching keys from {IAP_KEYS_URL}: {e}")
            return f"Error fetching keys: {e}", 500
        except Exception as e:
            print(f"Error interacting with Cloud Storage: {e}")
            return f"Error interacting with Cloud Storage: {e}", 500

Replace the following:

  * `BUCKET_NAME`: the name of your Cloud Storage bucket 
  * `OBJECT_NAME`: the name of the object to store your keys to 



#### `function_source/requirements.txt`
    
    
    functions-framework==3.*
    requests
    google-cloud-storage
    

#### `variables.tf`
    
    
    variable "project_id" {
      description = "The Google Cloud project ID."
      type        = string
      default     = PROJECT_ID
    }
    
    variable "region" {
      description = "The Google Cloud region."
      type        = string
      default     = "REGION"
    }
    
    variable "iap_keys_bucket_name" {
      description = "The name of the Cloud Storage bucket to store IAP keys."
      type        = string
      default     = BUCKET_NAME"
    }
    
    variable "function_source_bucket_name" {
      description = "The name of the Cloud Storage bucket to store the function source code."
      type        = string
      default     = "BUCKET_NAME_FUNCTION"
    }

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID 
  * `REGION`: the region to deploy resources in—for example, `us-central1`
  * `BUCKET_NAME`: the name for the Cloud Storage bucket that stores IAP keys 
  * `BUCKET_NAME_FUNCTION`: the name for the Cloud Storage bucket that stores Cloud Run functions source code 



#### `main.tf`
    
    
    terraform {
      required_providers {
        google = {
          source  = "hashicorp/google"
          version = ">= 4.50.0"
        }
        google-beta = {
          source  = "hashicorp/google-beta"
          version = ">= 4.50.0"
        }
      }
    }
    
    provider "google" {
      project = var.project_id
      region  = var.region
    }
    
    provider "google-beta" {
      project = var.project_id
      region  = var.region
    }
    
    # Enable necessary APIs
    resource "google_project_service" "services" {
      for_each = toset([
        "storage.googleapis.com",
        "cloudfunctions.googleapis.com",
        "run.googleapis.com", # Cloud Functions v2 uses Cloud Run
        "cloudscheduler.googleapis.com",
        "iamcredentials.googleapis.com",
        "cloudbuild.googleapis.com" # Needed for Cloud Functions deployment
      ])
      service            = each.key
      disable_on_destroy = false
    }
    
    # Cloud Storage Bucket to store the IAP public keys
    resource "google_storage_bucket" "iap_keys_bucket" {
      name                        = var.iap_keys_bucket_name
      location                    = var.region
      uniform_bucket_level_access = true
      versioning {
        enabled = true
      }
      lifecycle {
        prevent_destroy = false # Set to true in production to prevent accidental deletion
      }
    }
    
    # Cloud Storage Bucket to store the Cloud Function source code
    resource "google_storage_bucket" "function_source_bucket" {
      name                        = var.function_source_bucket_name
      location                    = var.region
      uniform_bucket_level_access = true
    }
    
    # Archive the function source code
    data "archive_file" "function_source_zip" {
      type        = "zip"
      source_dir  = "${path.module}/function_source"
      output_path = "${path.module}/function_source.zip"
    }
    
    # Upload the zipped source code to the source bucket
    resource "google_storage_bucket_object" "function_source_object" {
      name   = "function_source.zip"
      bucket = google_storage_bucket.function_source_bucket.name
      source = data.archive_file.function_source_zip.output_path
    }
    
    # Service Account for the Cloud Function
    resource "google_service_account" "iap_key_updater_sa" {
      account_id   = "iap-key-updater"
      display_name = "IAP Key Updater Function SA"
    }
    
    # Grant the function's SA permission to write to the IAP keys bucket
    resource "google_storage_bucket_iam_member" "keys_bucket_writer" {
      bucket = google_storage_bucket.iap_keys_bucket.name
      role   = "roles/storage.objectAdmin"
      member = "serviceAccount:${google_service_account.iap_key_updater_sa.email}"
    }
    
    # Cloud Function (v2)
    resource "google_cloudfunctions2_function" "update_iap_keys_func" {
      provider = google-beta # CFv2 often has newer features in google-beta
      name     = "update-iap-keys-function"
      location = var.region
    
      build_config {
        runtime     = "python312"
        entry_point = "update_iap_keys"
        source {
          storage_source {
            bucket = google_storage_bucket.function_source_bucket.name
            object = google_storage_bucket_object.function_source_object.name
          }
        }
      }
    
      service_config {
        max_instance_count = 1
        available_memory   = "256M"
        timeout_seconds    = 60
        ingress_settings   = "ALLOW_ALL"
        service_account_email = google_service_account.iap_key_updater_sa.email
        environment_variables = {
          BUCKET_NAME = google_storage_bucket.iap_keys_bucket.name
          OBJECT_NAME = "iap_public_keys.jwk"
        }
      }
    
      depends_on = [
        google_project_service.services,
        google_storage_bucket_iam_member.keys_bucket_writer
      ]
    }
    
    # Service Account for the Cloud Scheduler job
    resource "google_service_account" "iap_key_scheduler_sa" {
      account_id   = "iap-key-scheduler"
      display_name = "IAP Key Update Scheduler SA"
    }
    
    # Grant the Scheduler SA permission to invoke the Cloud Function
    resource "google_cloudfunctions2_function_iam_member" "invoker" {
      provider       = google-beta
      project        = google_cloudfunctions2_function.update_iap_keys_func.project
      location       = google_cloudfunctions2_function.update_iap_keys_func.location
      cloud_function = google_cloudfunctions2_function.update_iap_keys_func.name
      role           = "roles/cloudfunctions.invoker"
      member         = "serviceAccount:${google_service_account.iap_key_scheduler_sa.email}"
    }
    
    # Cloud Scheduler Job
    resource "google_cloud_scheduler_job" "iap_key_update_schedule" {
      name        = "iap-key-update-schedule"
      description = "Fetches IAP public keys and stores them in Cloud Storage every 12 hours"
      schedule    = "0 */12 * * *" # Every 12 hours
      time_zone   = "Etc/UTC"
      region      = var.region
    
      http_target {
        uri = google_cloudfunctions2_function.update_iap_keys_func.service_config[0].uri
        http_method = "POST"
    
        oidc_token {
          service_account_email = google_service_account.iap_key_scheduler_sa.email
        }
      }
    
      depends_on = [
        google_cloudfunctions2_function_iam_member.invoker,
        google_project_service.services
      ]
    }

#### `outputs.tf`
    
    
    output "iap_keys_bucket_url" {
      description = "The Cloud Storage bucket URL where IAP public keys are stored."
      value       = "gs://${google_storage_bucket.iap_keys_bucket.name}"
    }
    
    output "cloud_function_url" {
      description = "The URL of the Cloud Function endpoint that triggers key updates."
      value       = google_cloudfunctions2_function.update_iap_keys_func.service_config[0].uri
    }

#### `terraform.tfvars`

Create a `terraform.tfvars` file to specify your project ID and customize bucket names if needed:
    
    
    project_id = "your-gcp-project-id"
    # Optional: Customize bucket names
    # iap_keys_bucket_name = "custom-iap-keys-bucket"
    # function_source_bucket_name = "custom-func-src-bucket"

#### Deploy with Terraform

  1. Save the files in the directory structure described previously.
  2. Navigate to the directory in your terminal and initialize Terraform: 
         
         terraform init

  3. Plan the changes: 
         
         terraform plan

  4. Apply the changes: 
         
         terraform apply




This deploys the infrastructure. The Cloud Scheduler job triggers the function every 12 hours, fetching the IAP keys and storing them in `gs://BUCKET_NAME/iap_public_keys.jwk` by default. Your applications can now fetch the keys from this bucket.

#### Clean up resources

To remove the resources created by Terraform, run the following commands:
    
    
    gsutil rm -a gs://BUCKET_NAME/**
    
    terraform destroy -auto-approve

Replace `BUCKET_NAME` with the Cloud Storage bucket for your keys.

**Note:** The `gsutil` command is necessary because Terraform doesn't destroy Cloud Storage buckets that contain objects when versioning is enabled.

## JWTs for external identities

If you're using IAP with external identities, IAP will still issue a signed JWT on every authenticated request, just as it does with Google identities. However, there are a few differences.

### Provider information

When using external identities, the JWT payload will contain a claim named `gcip`. This claim contains user information, such as their email, photo URL, and any additional provider-specific attributes.

The following is an example of a JWT for a user who logged in with Facebook:
    
    
    "gcip": '{
      "auth_time": 1553219869,
      "email": "facebook_user@gmail.com",
      "email_verified": false,
      "firebase": {
        "identities": {
          "email": [
            "facebook_user@gmail.com"
          ],
          "facebook.com": [
            "1234567890"
          ]
        },
        "sign_in_provider": "facebook.com",
      },
      "name": "Facebook User",
      "picture: "https://graph.facebook.com/1234567890/picture",
      "sub": "gZG0yELPypZElTmAT9I55prjHg63"
    }',
    

### The `email` and `sub` fields

If a user was authenticated by Identity Platform, the `email` and `sub` fields of the JWT will be prefixed with the Identity Platform token issuer and the tenant ID used (if any). For example:
    
    
    "email": "securetoken.google.com/PROJECT-ID/TENANT-ID:demo_user@gmail.com",
    "sub": "securetoken.google.com/PROJECT-ID/TENANT-ID:gZG0yELPypZElTmAT9I55prjHg63"

### Controlling access with `sign_in_attributes`

IAM doesn't support external identities, but you can use claims embedded in the `sign_in_attributes` field to control access. For example, consider a user signed in using a SAML provider:
    
    
    {
      "aud": "/projects/project_number/apps/my_project_id",
      "gcip": '{
        "auth_time": 1553219869,
        "email": "demo_user@gmail.com",
        "email_verified": true,
        "firebase": {
          "identities": {
            "email": [
              "demo_user@gmail.com"
            ],
            "saml.myProvider": [
              "demo_user@gmail.com"
            ]
          },
          "sign_in_attributes": {
            "firstname": "John",
            "group": "test group",
            "role": "admin",
            "lastname": "Doe"
          },
          "sign_in_provider": "saml.myProvider",
          "tenant": "my_tenant_id"
        },
        "sub": "gZG0yELPypZElTmAT9I55prjHg63"
      }',
      "email": "securetoken.google.com/my_project_id/my_tenant_id:demo_user@gmail.com",
      "exp": 1553220470,
      "iat": 1553219870,
      "iss": "https://cloud.google.com/iap",
      "sub": "securetoken.google.com/my_project_id/my_tenant_id:gZG0yELPypZElTmAT9I55prjHg63"
    }
    

You could add logic to your application similar to the code below to restrict access to users with a valid role:
    
    
    const gcipClaims = JSON.parse(decodedIapJwtClaims.gcip);
    if (gcipClaims &&
        gcipClaims.firebase &&
        gcipClaims.firebase.sign_in_attributes &&
        gcipClaims.firebase.sign_in_attribute.role === 'admin') {
      // Allow access to admin restricted resource.
    } else {
      // Block access.
    }
    

You can access additional user attributes from Identity Platform SAML and OIDC providers using the `gcipClaims.gcip.firebase.sign_in_attributes` nested claim.

### IdP claims size limitations

After a user signs in with Identity Platform, the additional user attributes will be propagated to the stateless Identity Platform ID token payload, which will be securely passed to IAP. IAP will then issue its own stateless opaque cookie, which also contains the same claims. IAP will generate the signed JWT header based on the cookie content.

As a result, if a session is initiated with many claims, it might exceed the maximum allowed cookie size, which is typically about 4KB in most browsers. This will cause the sign-in operation to fail.

Make sure that only the necessary claims are propagated in the IdP SAML or OIDC attributes. Another option is to use [blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions) to filter out the claims that aren't required for the authorization check.
    
    
    const gcipCloudFunctions = require('gcip-cloud-functions');
    
    const authFunctions = new gcipCloudFunctions.Auth().functions();
    
    // This function runs before any sign-in operation.
    exports.beforeSignIn = authFunctions.beforeSignInHandler((user, context) => {
      if (context.credential &&
          context.credential.providerId === 'saml.my-provider') {
        // Get the original claims.
        const claims = context.credential.claims;
        // Define this function to filter out the unnecessary claims.
        claims.groups = keepNeededClaims(claims.groups);
        // Return only the needed claims. The claims will be propagated to the token
        // payload.
        return {
          sessionClaims: claims,
        };
      }
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
