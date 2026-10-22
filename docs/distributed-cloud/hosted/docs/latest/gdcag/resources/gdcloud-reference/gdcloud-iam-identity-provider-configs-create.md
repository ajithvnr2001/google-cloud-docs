---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-identity-provider-configs-create/
title: gdcloud iam identity-provider-configs create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:58:23.143887+00:00
---

# gdcloud iam identity-provider-configs create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-iam-identity-provider-configs-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud iam identity-provider-configs create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud iam identity-provider-configs create - Create an identity provider configuration.

## SYNOPSIS
    
    
    gdcloud iam identity-provider-configs create IDENTITY_PROVIDER_ID [flags]
    

## DESCRIPTION

Create an identity provider configuration for OIDC or SAML, with individual settings or a YAML file.

### EXAMPLES
    
    
    To create an identity provider with OIDC, run:
    
        gdcloud iam identity-provider-configs create example-identity-provider-id --input-type=oidc \
            --oidc-issuer-uri "https://issuer.example.com" \
            --oidc-client-id "client-123" \
            --oidc-ca-data "cert-data-example" \
            --oidc-groups-claim "groups" \
            --oidc-groups-prefix "group-1" \
            --oidc-user-claim "userId" \
            --oidc-scopes "openid"
    
    To create an identity provider with SAML, run:
    
        gdcloud iam identity-provider-configs create example-identity-provider-id --input-type=saml\
            --saml-group-attribute "default group value" \
            --saml-group-prefix "customer1prod" \
            --saml-idp-entity-id "https://sample.com" \
            --saml-idp-sso-uri "https://sso.sample.com" \
            --saml-user-prefix "customer1prod"
    
    To create an identity provider from a YAML configuration file, run:
    
        gdcloud iam identity-provider-configs create example-identity-provider-id --input-type=file --file=YAML_FILE
    

### REQUIRED FLAGS
    
    
          --input-type string   IDP input type (allowed: oidc, saml, file).
    

### OPTIONAL FLAGS
    
    
          --file string                       Path to file or directory containing YAML configuration for the IDP config.
          --oidc-attribute-mapping string     OIDC attribute mapping (in json format).
          --oidc-ca-data string               OIDC Certificate Authority (CA) data.
          --oidc-client-id string             OIDC client ID.
          --oidc-client-secret string         OIDC client secret.
          --oidc-console-uri string           OIDC cloud console URI.
          --oidc-group-prefix string          OIDC groups prefix.
          --oidc-groups-claim string          OIDC group claim.
          --oidc-issuer-uri string            OIDC issuer URI.
          --oidc-kubectl-uri string           OIDC kubectl redirect URI.
          --oidc-scopes string                OIDC scopes.
          --oidc-user-claim string            OIDC user Claim.
          --oidc-user-prefix string           OIDC user prefix.
          --saml-attribute-mapping string     SAML attribute mapping (in json format).
          --saml-encrypted-assertion string   SAML encrypted assertion (in json format).
          --saml-group-attribute string       SAML group attribute.
          --saml-group-prefix string          SAML group prefix.
          --saml-idp-cert-data stringArray    SAML IDP certificate data list.
          --saml-idp-entity-id string         SAML identity ID.
          --saml-idp-sso-uri string           SAML IDP single sign on URI.
          --saml-signed-requests string       SAML signed requests (in json format).
          --saml-user-attribute string        SAML user attribute.
          --saml-user-prefix string           SAML user prefix.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
