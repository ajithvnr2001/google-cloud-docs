---
url: https://docs.cloud.google.com/iap/docs/samples/iap-validate-jwt/
title: Securing your app with signed headers \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:35.395949+00:00
---

# Securing your app with signed headers  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/samples/iap-validate-jwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Samples ](https://docs.cloud.google.com/iap/docs/samples)



#  Securing your app with signed headers Stay organized with collections  Save and categorize content based on your preferences. 

Help secure your app using signed Identity-Aware Proxy (IAP) headers.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Securing your app with signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto)



## Code sample

### C#

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to IAP, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityawareproxy). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
