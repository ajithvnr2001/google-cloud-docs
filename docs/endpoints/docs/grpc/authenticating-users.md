---
url: https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users/
title: Authenticating users \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:57.324407+00:00
---

# Authenticating users  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/authenticating-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Authenticating users Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

Authentication lets the Extensible Service Proxy (ESP) identify the users calling your service's methods and then, based on this, decide whether to let them use that method (authorization). This page describes how authentication works with Cloud Endpoints for gRPC services, including how to configure ESP in a gRPC service to support authenticated requests, and how to call authenticated methods from a gRPC client.

ESP supports multiple authentication methods, including [Firebase](https://firebase.google.com/docs/auth/), [Auth0](http://auth0.com), and [Google ID tokens](https://docs.cloud.google.com/endpoints/docs/grpc/glossary#google_id_token), all of which can be set up as part of your gRPC API Configuration. In each case the client needs to provide an identifying JSON web token (JWT) in their requests. The ESP validates the token on behalf of your API, so you don't need to add any special authentication code yourself.

While both authentication and API key requirements let you restrict who can call your service's methods, they don't provide the same level of security, and provide different information to the called service. You can find out more about the differences between API keys and authentication, and when it's appropriate to use each scheme, in [When and why to use API keys](https://docs.cloud.google.com/endpoints/docs/when-why-api-key).

For a complete working example using authentication, see [Authenticating using a service account](https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication), which adds authentication to the Bookstore service from our [Tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials).

## Configuring authentication for ESP

You configure authentication for a Endpoints for gRPC service in its [gRPC service configuration](https://docs.cloud.google.com/endpoints/docs/grpc/grpc-service-config) YAML file, by using the [`authentication`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#google.api.Authentication) section. You specify the authentication method and details of the authentication source as `providers`, where:

  * The `id` value is used to identify the auth provider when used in `rules`: this typically uses the name of the authentication method, but it doesn't have to.

  * The `issuer` value is the issuer of the required tokens, and hence specifies the authentication method.

  * The `jwks_uri` value is the URI of the provider's public key, used to validate tokens. Some authentication methods don't require you to specify this, such as Google ID tokens where the ESP obtains the information automatically.

  * The `jwt_locations` is used to define the locations to extract the JWT.


**Note:** * If you specify the `jwt_locations`, Endpoints then ignores all default locations. * The customized `jwt_locations` are only supported by ESPv2 so far.

You can define multiple security providers in the same file, but each one must have a different `issuer`. See [`AuthProvider`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#authprovider) for more information.

You specify the API methods that you want to use these authentication requirements using `rules`, as described in [`AuthenticationRule`](https://docs.cloud.google.com/endpoints/docs/grpc-service-config/reference/rpc/google.api#authenticationrule).

The following examples show how to set up ESP in a gRPC service for some supported authentication methods:

### firebase

To support Firebase authentication:
    
    
    authentication:
      providers:
      - id: firebase
        jwks_uri: https://www.googleapis.com/service_accounts/v1/metadata/x509/securetoken@system.gserviceaccount.com
        # Replace FIREBASE-PROJECT-ID with your Firebase project ID
        issuer: https://securetoken.google.com/FIREBASE-PROJECT-ID
        audiences: "FIREBASE-PROJECT-ID"
        # Optional.
        jwt_locations:
        # expect header "jwt-header-foo": "jwt-prefix-foo<TOKEN>"
        - header: "jwt-header-foo"
          value_prefix: "jwt-prefix-foo"
        - query: "jwt_query_bar"
      rules:
      - selector: "*"
        requirements:
          - provider_id: firebase
    

### auth0

To support Auth0 authentication:
    
    
    authentication:
      providers:
      - id: auth0_jwk
        # Replace YOUR-ACCOUNT-NAME with your service account's email address.
        issuer: https://YOUR-ACCOUNT-NAME.auth0.com/
        jwks_uri: "https://YOUR-ACCOUNT-NAME.auth0.com/.well-known/jwks.json"
        # Optional. Replace YOUR-CLIENT-ID with your client ID
        audiences: "YOUR-CLIENT-ID"
      rules:
      - selector: "*"
        requirements:
          - provider_id: auth0_jwk
    

### Google ID Token

To support authentication using a Google ID token:
    
    
    authentication:
      providers:
      - id: google_id_token
        # This "issuer" field has to match the field "iss" in the JWT token.
         # Sometime it is "accounts.google.com".
        issuer: https://accounts.google.com
        # Optional. Replace YOUR-CLIENT-ID with your client ID
        audiences: "YOUR-CLIENT-ID"
      rules:
      - selector: "*"
        requirements:
          - provider_id: google_id_token
    

### custom

To support custom authentication:
    
    
    authentication:
      providers:
      - id: custom_auth_id
        # The value below should be unique
        issuer: issuer of the token
        jwks_uri: url to the public key
        # Optional. Replace YOUR-CLIENT-ID with your client ID
        audiences: "YOUR-CLIENT-ID"
     rules:
     - selector: "*"
       requirements:
         - provider_id: custom_auth_id
    

For Firebase authentication, the `audiences` field is required and must be your Firebase project ID. For all other authentication methods, it is optional. If not specified, ESP accepts all JWTs with the back-end service name in the form of `https://SERVICE_NAME` in the `aud` claim. To permit additional client IDs to access the back-end service, you can specify the allowed client IDs in the `audiences` field by using comma-separated values. ESP then accepts the JWTs with the whitelisted client IDs in the `aud` claim.

## Calling an authenticated method from gRPC

If a method requires authentication, gRPC clients need to pass the authentication token as [metadata](http://www.grpc.io/docs/guides/concepts.html#metadata) with their method call, where the key is `authorization` and the value is `Bearer <JWT_TOKEN>`. See an example of how to do this when calling the Bookstore example in Python, Node.js, or Java:

### Python
    
    
    def run(
        host, port, api_key, auth_token, timeout, use_tls, servername_override, ca_path

### Java
    
    
    private static final class Interceptor implements ClientInterceptor {
      private final String apiKey;
      private final String authToken;
    
      private static Logger LOGGER = Logger.getLogger("InfoLogging");
    
      private static Metadata.Key<String> API_KEY_HEADER =
          Metadata.Key.of("x-api-key", Metadata.ASCII_STRING_MARSHALLER);
      private static Metadata.Key<String> AUTHORIZATION_HEADER =
          Metadata.Key.of("authorization", Metadata.ASCII_STRING_MARSHALLER);
    
      public Interceptor(String apiKey, String authToken) {
        this.apiKey = apiKey;
        this.authToken = authToken;
      }
    
      @Override
      public <ReqT, RespT> ClientCall<ReqT, RespT> interceptCall(
          MethodDescriptor<ReqT,RespT> method, CallOptions callOptions, Channel next) {
        LOGGER.info("Intercepted " + method.getFullMethodName());
        ClientCall<ReqT, RespT> call = next.newCall(method, callOptions);
    
        call = new ForwardingClientCall.SimpleForwardingClientCall<ReqT, RespT>(call) {
          @Override
          public void start(Listener<RespT> responseListener, Metadata headers) {
            if (apiKey != null && !apiKey.isEmpty()) {
              LOGGER.info("Attaching API Key: " + apiKey);
              headers.put(API_KEY_HEADER, apiKey);
            }
            if (authToken != null && !authToken.isEmpty()) {
              System.out.println("Attaching auth token");
              headers.put(AUTHORIZATION_HEADER, "Bearer " + authToken);
            }
            super.start(responseListener, headers);
          }
        };
        return call;
      }
    }

### Node.js
    
    
    const makeGrpcRequest = (JWT_AUTH_TOKEN, API_KEY, HOST, GREETEE) => {
      // Uncomment these lines to set their values
      // const JWT_AUTH_TOKEN = 'YOUR_JWT_AUTH_TOKEN';
      // const API_KEY = 'YOUR_API_KEY';
      // const HOST = 'localhost:50051'; // The IP address of your endpoints host
      // const GREETEE = 'world';
    
      // Import required libraries
      const grpc = require('@grpc/grpc-js');
      const protoLoader = require('@grpc/proto-loader');
      const path = require('path');
    
      // Load protobuf spec for an example API
      const PROTO_PATH = path.join(__dirname, '/protos/helloworld.proto');
    
      const packageDefinition = protoLoader.loadSync(PROTO_PATH, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true,
      });
    
      const protoObj = grpc.loadPackageDefinition(packageDefinition).helloworld;
    
      // Create a client for the protobuf spec
      const client = new protoObj.Greeter(HOST, grpc.credentials.createInsecure());
    
      // Build gRPC request
      const metadata = new grpc.Metadata();
      if (API_KEY) {
        metadata.add('x-api-key', API_KEY);
      } else if (JWT_AUTH_TOKEN) {
        metadata.add('authorization', `Bearer ${JWT_AUTH_TOKEN}`);
      }
    
      // Execute gRPC request
      client.sayHello({name: GREETEE}, metadata, (err, response) => {
        if (err) {
          console.error(err);
        }
    
        if (response) {
          console.log(response.message);
        }
      });
    };

How the client gets a valid JWT to send depends on the authentication method.

  * You can see a complete example of using a Google service account to generate a token in [Authentication between services](https://docs.cloud.google.com/endpoints/docs/grpc/service-account-authentication).

  * You can see a further example of using a client secret file to generate a Google ID token in [this sample client for Cloud Endpoints on App Engine API](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/getting-started/clients/google-id-token-client.py).




## Receiving authentication results in your API

ESP usually forwards all headers it receives. However, it overrides the original `Authorization` header when the backend address is specified by `x-google-backend` in OpenAPI specification or `BackendRule` in gRPC service configuration. 

ESP will send the authentication result in the `X-Endpoint-API-UserInfo` to the backend API. We recommend using this header instead of the original `Authorization` header. This header is a string that `base64url` encodes a JSON object. The JSON object format differs between ESPv2 and ESP. For ESPv2, the JSON object is exactly the original JWT payload. For ESP, the JSON object uses different field names and put original JWT payload under `claims` field. See [Handle JWTs in the backend service](https://docs.cloud.google.com/endpoints/docs/openapi/migrate-to-esp-v2#handle-jwt) for more information on the format.

## What's next

  * [Troubleshooting JWT validation](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-jwt)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
