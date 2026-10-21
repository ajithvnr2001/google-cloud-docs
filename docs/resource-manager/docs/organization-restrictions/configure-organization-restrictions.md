---
url: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/configure-organization-restrictions/
title: Configure organization restrictions \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:30.096308+00:00
---

# Configure organization restrictions  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/configure-organization-restrictions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Configure organization restrictions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the prerequisites for egress proxy configuration, how to get the organization ID, add the organization restrictions header, and configure the proxy with the list of target URLs.

Google Cloud administrators, who administer Google Cloud, and egress proxy administrators who configure the egress proxy must work together to configure organization restrictions. For information about partner solutions that are validated with organization restrictions, see [Validated partner solutions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/validated-solutions).

## Before you begin

If you're an egress proxy administrator, before you configure the egress proxy to add the organization restrictions header, you must complete the following prerequisites:

  * If the Google Cloud administrator and egress proxy administrator roles are different in your organization, ensure that the Google Cloud administrator engages with the egress proxy administrator to configure the egress proxy.

  * Configure your organization firewall rules or configure the managed devices to ensure that the outbound traffic from all users in your organization pass through the egress proxy.

  * Ensure that the egress proxy in your organization has the following features:

    * **Insert headers**. Inserts a custom HTTP header to outbound requests traversing through the egress proxy.
    * **TLS inspection**. If the traffic to the egress proxy is encrypted, the egress proxy must decrypt the packets, insert the header, and re-encrypt the packet before sending it to the target.
    * **Filter and insert headers**. Optional. Support one or more of the following filters and then add the header only for requests that match the filter condition:

      * **Target URLs**. A list of target URLs that the egress proxy can match.
      * **Device IDs**. A list of device IDs that the egress proxy can match. The device IDs must be propagated to the egress proxy.
      * **User IDs**. A list of user IDs that the egress proxy can match. The user IDs must be propagated to the egress proxy.



## Get the organization ID

As a Google Cloud administrator, you must get the Google Cloud organization ID so that it can be added to the organization restrictions header.

To find your organization resource ID, run the following command:
    
    
       gcloud organizations list
    

This command lists all the organization resources to which you belong to, and their corresponding organization resource IDs.

After getting the organization ID, you can either add the organization restrictions header or engage with the egress proxy administrator to add the header.

## Add the organization restrictions header

As an egress proxy administrator, to add the organization restrictions header to outbound requests, do the following:

  * Create the header.
  * Encode the header.
  * Configure the egress proxy.



### Create the header

Create the JSON representation for the header in the following format: `X-Goog-Allowed-Resources: HEADER_VALUE`

`HEADER_VALUE` contains a comma-separated list of authorized Google Cloud organization IDs. The value must then be encoded in [web safe base64 encoding](https://en.wikipedia.org/wiki/Base64#URL_applications).

`HEADER_VALUE` has the following JSON structure:
    
    
      {
      "resources": [string,..],
      "options": string
      }
    

  * `resources`. A list of strings. Each string in this list must refer to a Google Cloud organization ID. Organization IDs in this list are considered authorized organizations during evaluation.
  * `options`. A string that contains one of the following values: 
    * `"strict"`. Enforces the organization restrictions header for all request types to the [supported Google Cloud services](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/supported-services).
    * `"cloudStorageReadAllowed"`. Allows read requests to Cloud Storage but enforces organization restrictions header for all other request types to the [supported Google Cloud services](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/supported-services). This option allows access for the following Cloud Storage read operations: 
      * `storage.objects.get`
      * `storage.objects.list`
      * `storage.objects.getIamPolicy`
      * `storage.buckets.get`
      * `storage.buckets.list`
      * `storage.buckets.getIamPolicy`



To demonstrate this option, consider an example where Alex is the administrator of Example Organization and Lee is an employee of this organization. Consider a website such as altostrat.com that stores static content in public Cloud Storage buckets and is outside Example Organization. If Alex uses the `strict` option to restrict Lee's access only to Example Organization, Lee is denied access to static content in altostrat.com, which exists in public Cloud Storage buckets owned by altostrat.com. This behaviour impacts Lee's ability to browse the website effectively and the same behavior is experienced for any website that uses public Cloud Storage to store static content. To enable Lee to view the static content in altostrat.com and restrict all other Google Cloud access only to Example Organization, Alex uses the `cloudStorageReadAllowed` option.

Here's an example of a valid organization restrictions header:
    
    
      {
      "resources": ["organizations/1234", "organizations/3456"],
      "options": "strict"
      }
    

### Encode the header

Encode the organization IDs in web safe base64 format. The encoding must follow the [RFC 4648 Section 5 specifications](https://datatracker.ietf.org/doc/html/rfc4648#section-5).

For example, if the JSON representation for the header value is stored in the `authorized_orgs.json` file, to encode the file, run the following [basenc](https://man7.org/linux/man-pages/man1/basenc.1.html) command:
    
    
         $ cat authorized_orgs.json | basenc --base64url -w0
    ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiLCAib3JnYW5pemF0aW9ucy8xMDExMTIxMzE0Il0sCiAib3B0aW9ucyI6ICJzdHJpY3QiCn0K
    

Here's an example header after encoding the organization ID:
    
    
    // Encoded representation
    X-Goog-Allowed-Resources: ewogInJlc291cmNlcyI6IFsib3JnYW5pemF0aW9ucy8xMjM0NTY3ODkiLCAib3JnYW5pemF0aW9ucy8xMDExMTIxMzE0Il0sCiAib3B0aW9ucyI6ICJzdHJpY3QiCn0K
    
    // Plain-text representation (As HTTP disallows some characters, encode the organization ID)
    // Plain-text representation is included here only for readability
    X-Goog-Allowed-Resources: {"resources": ["organizations/1234", "organizations/3456"], "options": "strict"}
    
    

### Configure the egress proxy

To insert the header to requests originating from the managed devices, configure the egress proxy.

Ensure that if a Google Cloud user in your organization explicitly supplies an HTTP header, the egress proxy overrides the user-supplied values with the values provided by Google Cloud administrator.

To avoid adding this header to targets outside of Google Cloud, configure the egress proxy to add the organization restrictions header to requests only with the following targets:

  * `*.google.com`
  * `*.googleapis.com`
  * `*.gcr.io`
  * `*.pkg.dev`
  * `*.cloudfunctions.net`
  * `*.run.app`
  * `*.tunnel.cloudproxy.app`
  * `*.datafusion.googleusercontent.com`



For information about error messages that occur due to organization restrictions violations, see [error messages](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/error-messages).

## What's next

  * Learn about [using organization restrictions](https://docs.cloud.google.com/resource-manager/docs/organization-restrictions/examples-org-restrictions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
