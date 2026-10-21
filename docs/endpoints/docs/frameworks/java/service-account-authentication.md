---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/service-account-authentication/
title: Authenticating with a service account \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:19.485210+00:00
---

# Authenticating with a service account  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/service-account-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Authenticating with a service account Stay organized with collections  Save and categorize content based on your preferences. 

## Prerequisites

This page assumes that you have already:

  * [Created a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  * [Added API management](https://docs.cloud.google.com/endpoints/docs/frameworks/java/adding-api-management).




## Configuring authentication

To authenticate with a service account:

  1. Add the following to your [`@Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/annotations#api_api-scoped_annotations) or method annotation:

     * Add an `authenticators` parameter to your annotation, set to the value `{EspAuthenticator.class}`.
     * Add an `issuers` parameter containing an `@ApiIssuer`.
     * Add an `issuerAudiences` parameter containing an `@ApiIssuerAudience` set to the service account issuer and your audience.

For example:
    
    @Api(
        name = "echo",
        version = "v1",
        authenticators = {EspAuthenticator.class},
        issuers = {
            @ApiIssuer(
                name = "serviceAccount",
                issuer = "YOUR_SERVICE_ACCOUNT_EMAIL",
                jwksUri = "https://www.googleapis.com/robot/v1/metadata/x509/YOUR_SERVICE_ACCOUNT_EMAIL")
        },
        issuerAudiences = {
            @ApiIssuerAudience(name = "serviceAccount", audiences = "YOUR_AUDIENCE")
        })
    

     * Replace `echo` with the name of your API.
     * Replace `v1` with your API version.
     * Replace `YOUR_SERVICE_ACCOUNT_EMAIL` with your service account email.
     * Replace `YOUR_AUDIENCE` with the value in the `aud` field sent by the calling service.
  2. In your API implementation code, import `Users`:
         
         import com.google.api.server.spi.auth.common.User;
         

  3. In each API method where you want to check for proper authentication, check for a valid `User` and throw an exception if there isn't one, as shown in this sample method definition:
         
         @ApiMethod(httpMethod = ApiMethod.HttpMethod.GET)
         public Email getUserEmail(User user) throws UnauthorizedException {
           if (user == null) {
             throw new UnauthorizedException("Invalid credentials");
           }
         
           Email response = new Email();
           response.setEmail(user.getEmail());
           return response;
         }
         

  4. [Deploy the API](https://docs.cloud.google.com/endpoints/docs/frameworks/java/test-deploy). You need to redeploy the API whenever you add new clients.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
