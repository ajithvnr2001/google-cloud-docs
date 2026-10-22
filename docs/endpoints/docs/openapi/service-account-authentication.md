---
url: https://docs.cloud.google.com/endpoints/docs/openapi/service-account-authentication/
title: Authentication between services \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:25.052874+00:00
---

# Authentication between services  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/service-account-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Authentication between services Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication "View this page for the Cloud Endpoints gRPC docs")

In addition to authenticating users, you might need to allow other services to interact with your API. While client applications can provide users with a web sign-in prompt to submit their credentials, you need another approach for secure service-to-service communication. This page shows the approach that we recommend to implement authentication between services and provides sample code.

## Overview

To identify a service that sends requests to your API, you use a [service account](https://docs.cloud.google.com/docs/authentication#service_accounts). The calling service uses the service account's private key to sign a secure [JSON Web Token (JWT)](https://jwt.io/) and sends the signed JWT in the request to your API.

To implement service-to-service authentication in your API and calling service:

  1. Create a service account and key for the calling service to use.
  2. Add support for authentication in the OpenAPI document for your Cloud Endpoints service.
  3. Add code to the calling service that:

     * Creates a JWT and signs it with the service account's private key.
     * Sends the signed JWT in a request to the API.



ESP validates that the claims in the JWT match the configuration in your OpenAPI document before forwarding the request to your API. ESP doesn't check for [Cloud Identity](https://docs.cloud.google.com/iam/docs) permissions that you have granted on the service account.

## Prerequisites

This page assumes that you have already:

  * [Created a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  * [Created an OpenAPI document for your API](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints).

  * [Deployed your OpenAPI document](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config).

  * [Deployed the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).




## Creating a service account with a key

You need a service account with a private key file that the calling service uses to sign the JWT. If you have more than one service sending requests to your API, you can create one service account to represent all the calling services. If you need to differentiate between the services—for example, they might have different permissions—you can create a service account and key for each calling service.

This section shows how to use the Google Cloud console and the `gcloud` command-line tool to create the service account and private key file and to assign the service account the [**Service Account Token Creator**](https://docs.cloud.google.com/iam/docs/roles-permissions/iam) role. For information on using an API to do this task, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To create a service account and key:

###  Google Cloud console 

  1. Create a service account:

     1. In the Google Cloud console, go to the **Create service account** page.

[Go to the Create Service Account page](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)

     2. Select the project that you want to use.

     3. In the **Service account name** field, enter a name.

     4. Optional: In the **Service account description** field, enter a description.

     5. Click **Create**.

     6. Click **Done**.

Don't close your browser window. You will use it in the next step.

  2. Create a service account key:

     1. In the Google Cloud console, click the email address for the service account that you created.
     2. Click **Keys**.
     3. Click **Add key** , then **Create new key**.
     4. Click **Create**. A JSON file that contains the service account's private key downloads to your computer.
     5. Click **Close**.



### gcloud

You can run the following commands by using the Google Cloud CLI on your local machine, or within Cloud Shell.

  1. Set the default account for `gcloud`. If you have more than one account, make sure to choose the account that is in the Google Cloud project that you want to use.
         
         gcloud auth login
         

  2. Display the project IDs for your Google Cloud projects.
         
         gcloud projects list
         

  3. Set the default project. Replace `PROJECT_ID` with the Google Cloud project ID that you want to use.
         
         gcloud config set project PROJECT_ID

  4. Create a service account. Replace `SA_NAME` and `SA_DISPLAY_NAME` with the name and display name that you want to use.
         
         gcloud iam service-accounts create SA_NAME \
           --display-name "SA_DISPLAY_NAME"

  5. Display the email address for the service account that you just created.
         
         gcloud iam service-accounts list
         

  6. Add the **Service Account Token Creator** role. Replace `SA_EMAIL_ADDRESS` with the service account's email address.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member serviceAccount:SA_EMAIL_ADDRESS \
           --role roles/iam.serviceAccountTokenCreator

  7. Create a service account key file in the current working directory. Replace `FILE_NAME` with the name that you want to use for key file. By default, the `gcloud` command creates a JSON file.
         
         gcloud iam service-accounts keys create FILE_NAME.json \
           --iam-account SA_EMAIL_ADDRESS




See the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference) for more information about the previous commands.

For information on safeguarding the private key, see [Best practices for managing credentials](https://docs.cloud.google.com/docs/authentication/production#best_practices_for_managing_credentials).

## Configuring your API to support authentication

To enable service account authentication for services _calling_ your gateway, modify the security objects in your OpenAPI document for ESP to validate the claims in the signed JWT. The modifications will vary based on the OpenAPI specification version used.

### OpenAPI 2.0

  1. Add the service account as an issuer in your OpenAPI specification: 
         
         securityDefinitions:
             DEFINITION_NAME:
               authorizationUrl: ""
               flow: "implicit"
               type: "oauth2"
               x-google-issuer: "SA_EMAIL_ADDRESS"
               x-google-jwks_uri: "https://www.googleapis.com/robot/v1/metadata/x509/SA_EMAIL_ADDRESS"
           

     * Replace `DEFINITION_NAME` with a string that identifies this security definition. You might want to replace it with the service account name or a name that identifies the calling service.
     * Replace `SA_EMAIL_ADDRESS` with the service account's email address.
     * You can define multiple security definitions in your OpenAPI specification, but each definition must have a different `x-google-issuer`. If you have created separate service accounts for each calling service, you can create a security definition for each service account, for example: 
           
           securityDefinitions:
               service-1:
                 authorizationUrl: ""
                 flow: "implicit"
                 type: "oauth2"
                 x-google-issuer: "service-1@example-project-12345.iam.gserviceaccount.com"
                 x-google-jwks_uri: "https://www.googleapis.com/robot/v1/metadata/x509/service-1@example-project-12345.iam.gserviceaccount.com"
               service-2:
                 authorizationUrl: ""
                 flow: "implicit"
                 type: "oauth2"
                 x-google-issuer: "service-2@example-project-12345.iam.gserviceaccount.com"
                 x-google-jwks_uri: "https://www.googleapis.com/robot/v1/metadata/x509/service-2@example-project-12345.iam.gserviceaccount.com"

  2. Optionally, add `x-google-audiences` to the `securityDefinitions` section. If you don't add `x-google-audiences`, ESP requires that the `"aud"` (audience) claim in the JWT is in the format `https://SERVICE_NAME`, where SERVICE_NAME is the name of your ESP service, which you have configured in the `host` field of your OpenAPI document.
  3. Add a `security` section at either the top level of the file (not indented or nested) to apply to the entire API, or at the method level to apply to a specific method. If you use `security` sections at both the API level and at the method level, the method-level settings override the API-level settings. 
         
         security:
           - DEFINITION_NAME: []

     * Replace `DEFINITION_NAME` with the name that you used in the `securityDefinitions` section.
     * If you have more than one definition in the `securityDefinitions` section, add them in the `security` section, for example: 
           
           security:
             - service-1: []
             - service-2: []

  4. Deploy your [updated OpenAPI specification](https://docs.cloud.google.com/api-gateway/docs/creating-api-config#updating-an-api-config). Before ESP forwards a request to your API, ESP verifies: 
     * The signature of the JWT by using the public key, which is located at the URI specified in the `x-google-jwks_uri`field in your OpenAPI specification.
     * That the `"iss"`(issuer) claim in the JWT matches the value specified in the `x-google-issuer`field.
     * That the `"aud"`(audience) claim in the JWT contains your ESP service name or matches one of the values that you specified in the `x-google-audiences`field.
     * That the token isn't expired by using the `"exp"`(expiration time) claim.



### OpenAPI 3.x

  1. Add the service account as an issuer in your OpenAPI specification: 
         
         components:
           securitySchemes:
             SCHEME_NAME:
               type: oauth2
               flows:
                implicit:
                  authorizationUrl: ""
                  scopes: {}
               x-google-auth:
                 issuer: SA_EMAIL_ADDRESS
                 jwksUri: https://www.googleapis.com/robot/v1/metadata/x509/SA_EMAIL_ADDRESS
                 audiences:
                   - 848149964201.apps.googleusercontent.com
                   - 841077041629.apps.googleusercontent.com
                 jwtLocations:
                   - header: Authorization
                     valuePrefix: "Bearer "
         security:
           - SCHEME_NAME: []

     * Replace `SCHEME_NAME` with a string that identifies this security scheme. You might want to replace it with the service account name or a name that identifies the calling service.
     * Replace `SA_EMAIL_ADDRESS` with the service account's email address.
     * You can define multiple security schemes in your OpenAPI specification, but each definition must have a different `issuer`. If you have created separate service accounts for each calling service, you can create a security definition for each service account, for example: 
           
           components:
             securitySchemes:
               service-1:
                 type: oauth2
                 flows:
                  implicit:
                    authorizationUrl: ""
                    scopes: {}
                 x-google-auth:
                   issuer: "service-1@example-project-12345.iam.gserviceaccount.com"
                   jwksUri: https://www.googleapis.com/robot/v1/metadata/x509/service-1@example-project-12345.iam.gserviceaccount.com
                   jwtLocations:
                     - header: Authorization
                       valuePrefix: "Bearer "
               service-2:
                 type: oauth2
                 flows:
                  implicit:
                    authorizationUrl: ""
                    scopes: {}
                 x-google-auth:
                   issuer: "service-2@example-project-12345.iam.gserviceaccount.com"
                   jwksUri: "https://www.googleapis.com/robot/v1/metadata/x509/service-2@example-project-12345.iam.gserviceaccount.com"
                   jwtLocations:
                     - header: Authorization
                       valuePrefix: "Bearer "

  2. Optionally, add `audiences` to the `securitySchemes` section. If you don't add `audiences`, ESP requires that the `"aud"` (audience) claim in the JWT is in the format `https://SERVICE_NAME`, where SERVICE_NAME is the name of your ESP service, which you have configured in the `host` field of your OpenAPI document.
  3. Add a `security` section at either the top level of the file (not indented or nested) to apply to the entire API, or at the method level to apply to a specific method. If you use `security` sections at both the API level and at the method level, the method-level settings override the API-level settings. 
         
         security:
           - SCHEME_NAME: []

     * Replace SCHEME_NAME with the name that you used in the `securitySchemes` section.
     * If you have more than one definition in the `securitySchemes` section, add them in the `security` section, for example: 
           
           security:
             - service-1: []
             - service-2: []

  4. Deploy your [updated OpenAPI specification](https://docs.cloud.google.com/api-gateway/docs/creating-api-config#updating-an-api-config). Before ESP forwards a request to your API, ESP verifies: 
     * The signature of the JWT by using the public key, which is located at the URI specified in the `jwksUri`field in your OpenAPI specification.
     * That the `"iss"`(issuer) claim in the JWT matches the value specified in the `issuer`field.
     * That the `"aud"`(audience) claim in the JWT contains your ESP service name or matches one of the values that you specified in the `audiences`field.
     * That the token isn't expired by using the `"exp"`(expiration time) claim.



## Making an authenticated request to an Endpoints API

To make an authenticated request, the calling service sends a JWT signed by the service account that you specified in the OpenAPI document. The calling service must:

  1. Create a JWT and sign it with the service account's private key.
  2. Send the signed JWT in a request to the API.



The following sample code demonstrates this process for select languages. To make an authenticated request in other languages, reference [jwt.io](https://jwt.io) for a list of supported libraries.

  1. In the calling service, add the following function and pass it the following parameters: Java
     * `saKeyfile`: The full path to the service account's private key file. 
     * `saEmail`: The service account's email address. 
     * `audience`: If you added the `x-google-audiences` field to your OpenAPI document, set `audience` to one of the values that you specified for `x-google-audiences`. Otherwise, set `audience` to `https://SERVICE_NAME`, where `SERVICE_NAME` is your Endpoints service name. 
     * `expiryLength`: The JWT expiration time, in seconds. 
Python
     * `sa_keyfile`: The full path to the service account's private key file. 
     * `sa_email`: The service account's email address. 
     * `audience`: If you added the `x-google-audiences` field to your OpenAPI document, set `audience` to one of the values that you specified for `x-google-audiences`. Otherwise, set `audience` to `https://SERVICE_NAME`, where `SERVICE_NAME` is your Endpoints service name. 
     * `expiry_length`: The JWT expiration time, in seconds. 
Go
     * `saKeyfile`: The full path to the service account's private key file. 
     * `saEmail`: The service account's email address. 
     * `audience`: If you added the `x-google-audiences` field to your OpenAPI document, set `audience` to one of the values that you specified for `x-google-audiences`. Otherwise, set `audience` to `https://SERVICE_NAME`, where `SERVICE_NAME` is your Endpoints service name. 
     * `expiryLength`: The JWT expiration time, in seconds. 

The function creates a JWT, signs it by using the private key file, and returns the signed JWT. 

Java
    
    /**
     * Generates a signed JSON Web Token using a Google API Service Account
     * utilizes com.auth0.jwt.
     */
    public static String generateJwt(final String saKeyfile, final String saEmail,
        final String audience, final int expiryLength)
        throws FileNotFoundException, IOException {
    
      Date now = new Date();
      Date expTime = new Date(System.currentTimeMillis() + TimeUnit.SECONDS.toMillis(expiryLength));
    
      // Build the JWT payload
      JWTCreator.Builder token = JWT.create()
          .withIssuedAt(now)
          // Expires after 'expiryLength' seconds
          .withExpiresAt(expTime)
          // Must match 'issuer' in the security configuration in your
          // swagger spec (e.g. service account email)
          .withIssuer(saEmail)
          // Must be either your Endpoints service name, or match the value
          // specified as the 'x-google-audience' in the OpenAPI document
          .withAudience(audience)
          // Subject and email should match the service account's email
          .withSubject(saEmail)
          .withClaim("email", saEmail);
    
      // Sign the JWT with a service account
      FileInputStream stream = new FileInputStream(saKeyfile);
      ServiceAccountCredentials cred = ServiceAccountCredentials.fromStream(stream);
      RSAPrivateKey key = (RSAPrivateKey) cred.getPrivateKey();
      Algorithm algorithm = Algorithm.RSA256(null, key);
      return token.sign(algorithm);
    }

Python
    
    def generate_jwt(
        sa_keyfile,
        sa_email="account@project-id.iam.gserviceaccount.com",
        audience="your-service-name",
        expiry_length=3600,
    ):
        """Generates a signed JSON Web Token using a Google API Service Account."""
    
        now = int(time.time())
    
        # build payload
        payload = {
            "iat": now,
            # expires after 'expiry_length' seconds.
            "exp": now + expiry_length,
            # iss must match 'issuer' in the security configuration in your
            # swagger spec (e.g. service account email). It can be any string.
            "iss": sa_email,
            # aud must be either your Endpoints service name, or match the value
            # specified as the 'x-google-audience' in the OpenAPI document.
            "aud": audience,
            # sub and email should match the service account's email address
            "sub": sa_email,
            "email": sa_email,
        }
    
        # sign with keyfile
        signer = google.auth.crypt.RSASigner.from_service_account_file(sa_keyfile)
        jwt = google.auth.jwt.encode(signer, payload)
    
        return jwt
    
    

Go
    
    // generateJWT creates a signed JSON Web Token using a Google API Service Account.
    func generateJWT(saKeyfile, saEmail, audience string, expiryLength int64) (string, error) {
    	now := time.Now().Unix()
    
    	// Build the JWT payload.
    	jwt := &jws.ClaimSet{
    		Iat: now,
    		// expires after 'expiryLength' seconds.
    		Exp: now + expiryLength,
    		// Iss must match 'issuer' in the security configuration in your
    		// swagger spec (e.g. service account email). It can be any string.
    		Iss: saEmail,
    		// Aud must be either your Endpoints service name, or match the value
    		// specified as the 'x-google-audience' in the OpenAPI document.
    		Aud: audience,
    		// Sub and Email should match the service account's email address.
    		Sub:           saEmail,
    		PrivateClaims: map[string]interface{}{"email": saEmail},
    	}
    	jwsHeader := &jws.Header{
    		Algorithm: "RS256",
    		Typ:       "JWT",
    	}
    
    	// Extract the RSA private key from the service account keyfile.
    	sa, err := os.ReadFile(saKeyfile)
    	if err != nil {
    		return "", fmt.Errorf("could not read service account file: %w", err)
    	}
    	conf, err := google.JWTConfigFromJSON(sa)
    	if err != nil {
    		return "", fmt.Errorf("could not parse service account JSON: %w", err)
    	}
    	block, _ := pem.Decode(conf.PrivateKey)
    	parsedKey, err := x509.ParsePKCS8PrivateKey(block.Bytes)
    	if err != nil {
    		return "", fmt.Errorf("private key parse error: %w", err)
    	}
    	rsaKey, ok := parsedKey.(*rsa.PrivateKey)
    	// Sign the JWT with the service account's private key.
    	if !ok {
    		return "", errors.New("private key failed rsa.PrivateKey type assertion")
    	}
    	return jws.Encode(jwsHeader, jwt, rsaKey)
    }
    

  2. In the calling service, add the following function to send the signed JWT in the `Authorization: Bearer` header in the request to the API: Java
         
         /**
          * Makes an authorized request to the endpoint.
          */
         public static String makeJwtRequest(final String signedJwt, final URL url)
             throws IOException, ProtocolException {
         
           HttpURLConnection con = (HttpURLConnection) url.openConnection();
           con.setRequestMethod("GET");
           con.setRequestProperty("Content-Type", "application/json");
           con.setRequestProperty("Authorization", "Bearer " + signedJwt);
         
           InputStreamReader reader = new InputStreamReader(con.getInputStream());
           BufferedReader buffReader = new BufferedReader(reader);
         
           String line;
           StringBuilder result = new StringBuilder();
           while ((line = buffReader.readLine()) != null) {
             result.append(line);
           }
           buffReader.close();
           return result.toString();
         }

Python
         
         def make_jwt_request(signed_jwt, url="https://your-endpoint.com"):
             """Makes an authorized request to the endpoint"""
             headers = {
                 "Authorization": "Bearer {}".format(signed_jwt.decode("utf-8")),
                 "content-type": "application/json",
             }
             response = requests.get(url, headers=headers)
             print(response.status_code, response.content)
             response.raise_for_status()
         
         

Go
         
         // makeJWTRequest sends an authorized request to your deployed endpoint.
         func makeJWTRequest(signedJWT, url string) (string, error) {
         	client := &http.Client{
         		Timeout: 10 * time.Second,
         	}
         
         	req, err := http.NewRequest("GET", url, nil)
         	if err != nil {
         		return "", fmt.Errorf("failed to create HTTP request: %w", err)
         	}
         	req.Header.Add("Authorization", "Bearer "+signedJWT)
         	req.Header.Add("content-type", "application/json")
         
         	response, err := client.Do(req)
         	if err != nil {
         		return "", fmt.Errorf("HTTP request failed: %w", err)
         	}
         	defer response.Body.Close()
         	responseData, err := io.ReadAll(response.Body)
         	if err != nil {
         		return "", fmt.Errorf("failed to parse HTTP response: %w", err)
         	}
         	return string(responseData), nil
         }
         




When you send a request by using a JWT, for security reasons, we recommend that you put the authentication token in the `Authorization: Bearer` header. For example:
    
    
    curl --request POST \
      --header "Authorization: Bearer ${TOKEN}" \
      "${ENDPOINTS_HOST}/echo"
    

where `ENDPOINTS_HOST` and `TOKEN` are environment variables containing your API hostname and authentication token, respectively.

## Receiving authenticated results in your API

ESP usually forwards all headers it receives. However, it overrides the original `Authorization` header when the backend address is specified by `x-google-backend` in OpenAPI specification or `BackendRule` in gRPC service configuration. 

ESP will send the authentication result in the `X-Endpoint-API-UserInfo` to the backend API. We recommend using this header instead of the original `Authorization` header. This header is a string that `base64url` encodes a JSON object. The JSON object format differs between ESPv2 and ESP. For ESPv2, the JSON object is exactly the original JWT payload. For ESP, the JSON object uses different field names and put original JWT payload under `claims` field. See [Handle JWTs in the backend service](https://docs.cloud.google.com/endpoints/docs/openapi/migrate-to-esp-v2#handle-jwt) for more information on the format.

## What's next

  * [Troubleshooting JWT validation](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-jwt)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
