---
url: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-jwt/
title: Troubleshooting JWT validation \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:27.313027+00:00
---

# Troubleshooting JWT validation  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-jwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Troubleshooting JWT validation Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/troubleshoot-jwt "View this page for the Cloud Endpoints gRPC docs")

When a client application includes a JSON Web Token (JWT) in a request to an API, the [Extensible Service Proxy (ESP)](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy) validates the JWT before sending the request to the API backend. This page provides troubleshooting information if the JWT validation fails and ESP returns an error in the response to the client. See [RFC 7519](https://tools.ietf.org/html/rfc7519) for more information about JWTs.

**Error:`401: Jwt issuer is not configured`**

This may happen when deploying ESPv2 in Cloud Run, the flag `--allow-unauthenticated` is not used in `gcloud run deploy` command. If the flag is not used, the JWT token is intercepted and verified by Cloud Run access control IAM server and not by ESPv2. IAM may use a different issuer than ESPv2. 

**Error:`BAD_FORMAT`**

Check the following:

  * Make sure the JWT contains valid JSON.
  * Check that the JWT header has the `"alg"` field and is set to one of the following: `"RS256"`, `"HS256"`, `"RS384"`, `"HS384"`, `"RS512"`, or `"HS512"`
  * Check the data type of the following fields (if they are present) in the JWT payload:
    * The `"iat"` (issued at), `"exp"` (expiration time), and `"nbf"`(not before) claims are numbers greater than 0 and not strings.
    * The `"sub"` (subject), `"iss"` (issuer), and `"jti"` (JWT ID) fields are strings.
    * The `"aud"` (audience) claim is either a string or an array of strings.
  * Ensure that the following claims are present in the JWT payload: `"sub"` (subject), `"iss"` (issuer), and `"aud"` (audience).



The following is an example of a decoded JWT token that is valid:
    
    
    {
      "alg": "RS256",
      "typ": "JWT",
      "kid": "42ba1e234ac91ffca687a5b5b3d0ca2d7ce0fc0a"
    }
    
    Payload:
    {
      "iss": "myservice@myproject.iam.gserviceaccount.com",
      "iat": 1493833746,
      "aud": "myservice.appspot.com",
      "exp": 1493837346,
      "sub": "myservice@myproject.iam.gserviceaccount.com"
    }
    

**Error:`TIME_CONSTRAINT_FAILURE`**

Use [jwt.io](https://jwt.io/) to decode the JWT and make sure that:

  * The `"exp"` (expiration time) claim exists.
  * The `"exp"` (expiration time) claim value is a date and time in the future. The current date and time must be before the expiration date and time listed in the `"exp"` claim.
  * The `"nbf"` (not before) claim (If present) is a date and time in the past. The current date and time must be after or equal to the date and time listed in the `"nbf"` claim.

**Error:`UNKNOWN`**

Use [jwt.io](https://jwt.io/) to decode the JWT and ensure that:

  * If the `"iss"` (issuer) claim is an email address, then the `"sub"` (subject) and `"iss"` claims should be the same. This is to ensure that for e-mail issuers, the JWT is self issued.



**Error:`KEY_RETRIEVAL_ERROR`**

  * Check that the public key URI specified in the [`x-google-jwks_uri`](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-jwks_uri) field in your OpenAPI document is correct and valid.



**Error:`Issuer not allowed`**

  * Check that the `"iss"` (issuer) claim in your JWT token matches the [`x-google-issuer`](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-issuer) field in the `securityDefinitions` section of the security object in your OpenAPI document.

  * In your OpenAPI document, check that the security object is enabled for the API method invoked.




See the [sample openapi.yaml](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/endpoints/getting-started/openapi.yaml) file for an example of how to describe security at the method level by using `securityDefinition` and `security` objects.

**Error:`Audience not allowed`**

Compare the `"aud"` (audience) claim in a JWT token to see if it matches the Endpoints service name, which corresponds to the `host` field in the OpenAPI document.

If the `"aud"` claim and the Endpoints service name are different:

  * Check that the `"aud"` claim in the JWT matches one of the `x-google-audiences` values specified in your OpenAPI document.

  * Make sure that the `x-google-audiences` and `x-google-issuer` are in the same `securityDefinitions` object in your OpenAPI document.




If the `"aud"` claim and the Endpoints service name are the same, the ESP validates the audience and ignores the [`x-google-audiences`](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions#x-google-audiences) values in your OpenAPI document. For example, if your service name is `"myservice.endpoints.example-project-12345.cloud.goog"`, then a JWT with `"aud"` set to `"myservice.endpoints.example-project-12345.cloud.goog"` or `"https://myservice.endpoints.example-project-12345.cloud.goog"` is a valid audience.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
