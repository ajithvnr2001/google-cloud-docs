---
url: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/examples-org-restrictions/
title: Examples of organization restrictions \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:52.445978+00:00
---

# Examples of organization restrictions  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/examples-org-restrictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Examples of organization restrictions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes several common examples of how to use organization restrictions.

## Restrict access only to your organization

In this example, the Google Cloud administrator and egress proxy administrator of Organization A engage together to restrict employees to only access resources in their Google Cloud organization.

To restrict access only to your organization, do the following:

  1. As a Google Cloud administrator, to get the Google Cloud organization ID of Organization A, use the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list):
         
         gcloud organizations list
         
         

The following is the example output:
         
         DISPLAY_NAME: Organization A
             ID: 123456789
             DIRECTORY_CUSTOMER_ID: a1b2c3d4
         

  2. As an egress proxy administrator, after you get the organization ID from the Google Cloud administrator, compose the JSON representation for the header value in the following format:
         
         {
          "resources": ["organizations/123456789"],
           "options": "strict"
          }
         

  3. As an egress proxy administrator, encode the value for the request header by following the [RFC 4648 Section 5 specifications](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

For example, if the JSON representation for the header value is stored in the `authorized_orgs.json` file, to encode the file, run the following [basenc](https://man7.org/linux/man-pages/man1/basenc.1.html) command: 
         
         $ cat authorized_orgs.json | basenc --base64url -w0
          ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiXSwKICJvcHRpb25zIjogInN0cmljdCIKfQo
         

  4. As an egress proxy administrator, configure the egress proxy such that the following request header is inserted in all of the requests originating from the managed devices in Organization A:
         
         X-Goog-Allowed-Resources: ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiXSwKICJvcHRpb25zIjogInN0cmljdCIKfQo
         




## Restrict access to your organization and allow read requests to Cloud Storage resources

In this example, the Google Cloud administrator and egress proxy administrator of Organization A engage together to restrict employees to only access resources in their Google Cloud organization, except for read requests to Cloud Storage resources. Administrators might want to omit read requests to Cloud Storage resources from organization restrictions enforcement to ensure that their employees can access external websites that use Cloud Storage to host static content. The administrator uses the `cloudStorageReadAllowed` option to allow read requests to Cloud Storage resources.

To restrict access only to your organization and allow read requests to Cloud Storage resources, do the following:

  1. As a Google Cloud administrator, to get the Google Cloud organization ID of Organization A, use the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list):
         
         gcloud organizations list
         

The following is the example output:
         
         DISPLAY_NAME: Organization A
             ID: 123456789
             DIRECTORY_CUSTOMER_ID: a1b2c3d4
         

  2. As an egress proxy administrator, after you get the organization ID from the Google Cloud administrator, compose the JSON representation for the header value in the following format:
         
         {
          "resources": ["organizations/123456789"],
           "options": "cloudStorageReadAllowed"
          }
         

  3. As an egress proxy administrator, encode the value for the request header by following the [RFC 4648 Section 5 specifications](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

For example, if the JSON representation for the header value is stored in the `authorized_orgs.json` file, to encode the file, run the following [basenc](https://man7.org/linux/man-pages/man1/basenc.1.html) command:
         
         $ cat authorized_orgs.json | basenc --base64url -w0
         ewogICJyZXNvdXJjZXMiOiBbIm9yZ2FuaXphdGlvbnMvMTIzNDU2Nzg5Il0sCiAgIm9wdGlvbnMiOiAiY2xvdWRTdG9yYWdlUmVhZEFsbG93ZCIKfQo=l
         

  4. As an egress proxy administrator, configure the egress proxy such that the following request header is inserted in all of the requests originating from the managed devices in Organization A:
         
         X-Goog-Allowed-Resources: ewogICJyZXNvdXJjZXMiOiBbIm9yZ2FuaXphdGlvbnMvMTIzNDU2Nzg5Il0sCiAgIm9wdGlvbnMiOiAiY2xvdWRTdG9yYWdlUmVhZEFsbG93ZCIKfQo=l
         

The employees of Organization A now have access to their Google Cloud organization and read access to Cloud Storage resources.




## Allow employees access to a vendor Google Cloud organization

In this example, the Google Cloud administrator and egress proxy administrator of Organization B engage together to allow employees to access a vendor Google Cloud organization in addition to their existing Google Cloud organization.

To restrict employee access only to your organization and the vendor organization, do the following:

  1. As a Google Cloud administrator, engage with the vendor to get the Google Cloud organization ID of the vendor organization.

  2. As an egress proxy administrator, to include the vendor organization ID in addition to the existing organization ID, you must update the JSON representation for the header value. After you get the vendor organization ID from the Google Cloud administrator, update the header value in the following format:
         
         {
          "resources": ["organizations/1234", "organizations/3456"],
           "options": "strict"
          }
         

  3. As an egress proxy administrator, encode the value for the request header by following the [RFC 4648 Section 5 specifications](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

For example, if the JSON representation for the header value is stored in the `authorized_orgs.json` file, to encode the file, run the following [basenc](https://man7.org/linux/man-pages/man1/basenc.1.html) command:
         
         $ cat authorized_orgs.json | basenc --base64url -w0
          ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiLCAib3JnYW5pemF0aW9ucy8xMDExMTIxMzE0Il0sCiAib3B0aW9ucyI6ICJzdHJpY3QiCn0K
         

  4. As an egress proxy administrator, configure the egress proxy such that the following request header is inserted in all of the requests originating from the managed devices in Organization B:
         
         X-Goog-Allowed-Resources: ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiLCAib3JnYW5pemF0aW9ucy8xMDExMTIxMzE0Il0sCiAib3B0aW9ucyI6ICJzdHJpY3QiCn0K
         

The employees of Organization B now have access to both the vendor and their Google Cloud organizations.




## Restrict access only for uploads

In this example, the Google Cloud administrator and egress proxy administrator of Organization C engage together to restrict upload access of employees only to resources in the Google Cloud organization.

To restrict upload access only to your organization, do the following:

  1. As a Google Cloud administrator, to get the Google Cloud organization ID of Organization C, use the [`gcloud organizations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/organizations/list):
         
         gcloud organizations list
         

The following is the example output:
         
         DISPLAY_NAME: Organization C
             ID: 123456789
             DIRECTORY_CUSTOMER_ID: a1b2c3d4
         

  2. As an egress proxy administrator, after you get the organization ID from the Google Cloud administrator, compose the JSON representation for the header value in the following format:
         
         {
          "resources": ["organizations/123456789"],
           "options": "strict"
          }
         

  3. As an egress proxy administrator, encode the value for the request header by following the [RFC 4648 Section 5 specifications](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

For example, if the JSON representation for the header value is stored in the `authorized_orgs.json` file, to encode the file, run the following [basenc](https://man7.org/linux/man-pages/man1/basenc.1.html) command:
         
         $ cat authorized_orgs.json | basenc --base64url -w0
         ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiXSwKICJvcHRpb25zIjogInN0cmljdCIKfQo
         

  4. As an egress proxy administrator, configure the egress proxy such that the following request header is inserted only for requests with PUT, POST, and PATCH methods originating from the managed devices in Organization C:
         
         X-Goog-Allowed-Resources: ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiXSwKICJvcHRpb25zIjogInN0cmljdCIKfQo
         




## What's next

  * Learn about the [services supported by organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/supported-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
