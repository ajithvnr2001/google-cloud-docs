---
url: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/test-org-restrictions/
title: Test an organization restrictions header before configuring an egress proxy \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:06.670031+00:00
---

# Test an organization restrictions header before configuring an egress proxy  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/test-org-restrictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Test an organization restrictions header before configuring an egress proxy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Google Cloud administrators can test organization restrictions without having to configure an egress proxy.

To create and test the organization restrictions header, do the following:

  1. To get the Google Cloud organization ID of the organization, use the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list):
         
         gcloud organizations list
         

The following is the example output:
         
         DISPLAY_NAME: Organization A
             ID: 123456789
             DIRECTORY_CUSTOMER_ID: a1b2c3d4
         

  2. After you get the organization ID, compose the JSON representation for the header value in the following format:
         
         {
          "resources": ["organizations/123456789"],
           "options": "strict"
          }
         

  3. Encode the value for the request header by following the [RFC 4648 Section 5 specifications](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

For example, if the JSON representation for the header value is stored in the `authorized_orgs.json` file, the following is the encoding through [basenc](https://man7.org/linux/man-pages/man1/basenc.1.html):
         
         $ OR_HEADER=`cat authorized_orgs.json | basenc --base64url -w0`
          $ echo $OR_HEADER
         ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiXQogIm9wdGlvbnMiOiAic3RyaWN0Igp9Cgo=
         

  4. To test whether header configuration allows access to a resource within an authorized Google Cloud organization, create a curl request to a resource within an authorized Google Cloud organization. Here is an example curl request:
         
         # Get auth token
         $ TOKEN=$(gcloud auth print-access-token)
         
         # Make a request that includes the organization restriction header; this call makes a request to the logging API for a project within the same organization listed in the header
         $ curl -H "X-Goog-Allowed-Resources: ${OR_HEADER}" -X POST -d '{"projectIds":
         ["my-project-123"]}' -H 'Content-Type: application/json' -H "Authorization: Bearer ${TOKEN}" "https://logging.googleapis.com/v2/entries:list"
         # A successful request returns log entries in this project
         

  5. To test whether header configuration denies access to a resource that is outside the authorized Google Cloud organization, create a curl request to a resource outside an authorized Google Cloud organization. Here is an example curl request:
         
         # Get auth token
         $ TOKEN=$(gcloud auth print-access-token)
         
         # Make a request that includes the organization restriction header; this call makes a request to the logging API for a project not within the same organization listed in the header
         $ curl -H "X-Goog-Allowed-Resources: ${OR_HEADER}" -X POST -d '{"projectIds": ["other-project-123"]}' -H 'Content-Type: application/json' -H "Authorization: Bearer ${TOKEN}" "https://logging.googleapis.com/v2/entries:list" 
         {
           "error": {
          "code": 403,
             "message": "Access denied by organization restriction. Contact your administrator for additional information.",
             "status": "PERMISSION_DENIED",
             "details": [
               {
                 "@type": "type.googleapis.com/google.rpc.ErrorInfo",
                 "reason": "ORG_RESTRICTION_VIOLATION",
                 "domain": "googleapis.com",
                 "metadata": {
                   "service": "logging.googleapis.com",
                   "consumer": "other-project-123"
                 }
               }
             ]
           }
         }
         
         

An access denied error message indicates that the request to the resource is denied.




## What's next

  * Learn about [using organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/examples-org-restrictions).
  * Learn about the [services supported by organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/supported-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
