---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig-Oauth2JwtBearer/
title: Connectors V1 API - Class Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:19.491248+00:00
---

# Connectors V1 API - Class Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig-Oauth2JwtBearer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Connectors V1 API - Class Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Connectors V1 API class Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer.

Parameters to support JSON Web Token (JWT) Profile for Oauth 2.0 Authorization Grant based authentication. See <https://tools.ietf.org/html/rfc7523> for more details.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #client_key
    
    
    def client_key() -> ::Google::Cloud::Connectors::V1::Secret

**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Secret version reference containing a PKCS#8 PEM-encoded private key associated with the Client Certificate. This private key will be used to sign JWTs used for the jwt-bearer authorization grant. Specified in the form as: `projects/*/secrets/*/versions/*`. 



### #client_key=
    
    
    def client_key=(value) -> ::Google::Cloud::Connectors::V1::Secret

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Secret version reference containing a PKCS#8 PEM-encoded private key associated with the Client Certificate. This private key will be used to sign JWTs used for the jwt-bearer authorization grant. Specified in the form as: `projects/*/secrets/*/versions/*`. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::Secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-Secret)) — Secret version reference containing a PKCS#8 PEM-encoded private key associated with the Client Certificate. This private key will be used to sign JWTs used for the jwt-bearer authorization grant. Specified in the form as: `projects/*/secrets/*/versions/*`. 



### #jwt_claims
    
    
    def jwt_claims() -> ::Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer::JwtClaims

**Returns**

  * ([::Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer::JwtClaims](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig-Oauth2JwtBearer-JwtClaims)) — JwtClaims providers fields to generate the token. 



### #jwt_claims=
    
    
    def jwt_claims=(value) -> ::Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer::JwtClaims

**Parameter**

  * **value** ([::Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer::JwtClaims](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig-Oauth2JwtBearer-JwtClaims)) — JwtClaims providers fields to generate the token. 



**Returns**

  * ([::Google::Cloud::Connectors::V1::AuthConfig::Oauth2JwtBearer::JwtClaims](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-connectors-v1/latest/Google-Cloud-Connectors-V1-AuthConfig-Oauth2JwtBearer-JwtClaims)) — JwtClaims providers fields to generate the token. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
