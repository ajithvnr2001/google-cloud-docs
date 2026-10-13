---
url: https://docs.cloud.google.com/security-command-center/docs/aoss-security-metadata-fields/
title: Security metadata fields \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:12.699650+00:00
---

# Security metadata fields  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/aoss-security-metadata-fields/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Security metadata fields Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page provides examples of the security metadata that you download from Cloud Storage and an explanation of the metadata fields.

This page applies to the Assured OSS premium tier only.

## Security metadata
    
    
    {
        "overview": {
            "refreshTime": "string",        // when was the data last refreshed
            "originValidated": boolean,     // is the origin of the binary validated
            "builtByAssuredOSS": boolean,   // is the binary built by Assured OSS
            "transitivelyClosed": boolean,  // are package dependencies built by Assured OSS
            "SCADataAvailable": boolean,    // is dependency information available
            "SBOMAvailable": boolean,       // is the SBOM present in SPDX-2.3 format
            "VEXAvailable": boolean,        // is the VEX Information present in CycloneDX-1.4 format
            "licenseScanned": boolean,      // is the license information present
            "fuzzTestedByGoogle": boolean   // was the package fuzz tested by Google
        },
        "buildInfo": "string",              // build details along with SPDX
        "buildInfoSignature": {
            "certInfo": {
                "cert": "string",           // certificate for verifying build info
                "certChain": "string"       // certChain for verifying build info
            },
            "digest": [
                {
                    "digest": "string",     // digest of the build info
                    "algorithm": "string"   // algorithm used for hashing
                }
            ],
            "signature": [
                {
                    "signature": "string",  // signature of the digest
                    "algorithm": "string"   // algorithm used for signing
                }
            ]
        },
        "vexInfo": "string",                // vex information along with CycloneDX
        "vexInfoSignature": {
            "certInfo": {
                "cert": "string",           // certificate for verifying vex info
                "certChain": "string"       // certChain for verifying vex info
            },
            "digest": [
                {
                    "digest": "string",     // digest of the vex info
                    "algorithm": "string"   // algorithm used for hashing
                }
            ],
            "signature": [
                {
                    "signature": "string",  // signature of the digest
                    "algorithm": "string"   // algorithm used for signing
                }
            ]
        },
        "healthInfo": "string",             // health information
        "healthInfoSignature": {
            "certInfo": {
                "cert": "string",           // certificate for verifying health info
                "certChain": "string"       // certChain for verifying health info
            },
            "digest": [
                {
                    "digest": "string",     // digest of the health info
                    "algorithm": "string"   // algorithm used for hashing
                }
            ],
            "signature": [
                {
                    "signature": "string",  // signature of the digest
                    "algorithm": "string"   // algorithm used for signing
                }
            ]
        }
    }
    

## Build information
    
    
    {
      "creationTime": "string",    // time of creation of document (RFC 3339)
      "refreshTime": "string",     // time when the data was refreshed (RFC 3339)
      "buildDetails": [
        {
          "packageFileName": "string",  // the name of the file to which the build details apply
          "slsaLevel": "string",        // SLSA level adhered by the build system
          "buildTool": "string",
          "transitiveClosureState": "string",  // ENUM indicating if all the build dependencies for the package (direct or indirect) are also present in Assured OSS's portfolio or not. It can have 2 values, CLOSED if all dependencies are present else OPEN.
          "buildProvenances": [
            {
              "provenanceVersion": "string",  // version of SLSA provenance
              "provenance": "string",         // string representation of build provenance in "provenanceVersion" format
              "provenancePublicKey": "string", // public key used for verifying the signatures of the provenance
              "envelope": {  // a string representing a DSSE envelope that can be used to verify the integrity of the provenance document. This is also generated by Cloud Build
                "payload": "string",
                "payloadType": "string",
                "signatures": [
                  {
                    "sig": "string",
                    "keyid": "string"
                  }
                ]
              }
            }
          ]
        }
      ],
      "sourceInfo": [
        {
          "sourceUrl": "string",  // the GitHub URL
          "commitHash": "string", // the commit hash attached to release
          "tag": "string",        // release tag associated with the package-version
          "host": {
            "name": "string"      // name of the system that hosts the source code in GitHub
          },
          "commitTime": "string"  // time of commit (RFC 3339)
        }
      ],
      "sbom": "string",           // SBOM string in SPDX-2.3 format
      "creator": {
        "name": "string", // the name of the organization that created this document
        "email": "string" // the email address of the organization in case of any query or complaint
      }
    }
    

## VEX information
    
    
    {
      "creationTime": "string",    // time of creation of document (RFC 3339)
      "refreshTime": "string",     // time when the data was refreshed (RFC 3339)
      "vexData": "string",  // Vulnerability Exploitability eXchange (VEX) string in CycloneDX 1.4 format
      "creator": {
        "name": "string", // the name of the organization that created this document
        "email": "string" // the email address of the organization in case of any query or complaint
      }
    }
    

## Health information
    
    
    {
      "creationTime": "string",    // time of creation of document (RFC 3339)
      "refreshTime": "string",     // time when the data was refreshed (RFC 3339)
      "testingData": [
        {
          "testType": "string",   // the type of test that was done. For example, FUZZ
          "tool": {
            "name": "string"      // the name of the tool that was used to perform the test
          },
          "testStatus": "string"  // the status of the test. It can be one of TESTED (testing was executed) or UNTESTED (package was not tested) or NOT_REQUIRED (testing was not required for the package. For example, fuzz testing is not required on a package that contains only interfaces)
        }
      ],
      "creator": {
        "name": "string", // the name of the organization that created this document
        "email": "string" // the email address of the organization in case of any query or complaint
      }
    }
    

## What's next

  * [Access security metadata and verify packages](https://docs.cloud.google.com/security-command-center/docs/aoss-access-security-metadata)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
