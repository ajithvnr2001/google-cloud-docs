---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/troubleshoot-jwt/
title: Troubleshooting JWT validation \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:10.866419+00:00
---

# Troubleshooting JWT validation  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/troubleshoot-jwt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Troubleshooting JWT validation Stay organized with collections  Save and categorize content based on your preferences. 

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

  * Check that the public key URI specified in the second parameter of the [`endpoints.Issuer`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi) object is correct and valid.



**Error:`Issuer not allowed`**

  * Check that the `"iss"` (issuer) claim in your JWT token matches the first parameter of the [`endpoints.Issuer`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi) object.



**Error:`Audience not allowed`**

If the `"aud"` (audience) claim in a JWT token matches the Endpoints service name, then Cloud Endpoints Frameworks validates the audience and ignores the values set in the [`audiences`](https://docs.cloud.google.com/endpoints/docs/frameworks/python/decorators-reference#defining_the_api_endpointsapi) argument in the `@endpoints.api` decorator. For example, if your service name is `"myservice.appspot.com"`, then a JWT with `"aud"` set to `"myservice.appspot.com"` or `"https://myservice.appspot.com"` is a valid audience.

If the `"aud"` claim is not the same as the Endpoints service name:

  * Check that the `"aud"` claim in the JWT matches one of the values in the `audiences` argument in the `@endpoints.api` decorator.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
