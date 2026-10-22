---
url: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-access-control/
title: Manage access policies \u00a0|\u00a0 Network Intelligence Center - Connectivity Tests \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:28.730709+00:00
---

# Manage access policies  |  Network Intelligence Center - Connectivity Tests  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/managing-access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Connectivity Tests ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)



Send feedback 

#  Manage access policies Stay organized with collections  Save and categorize content based on your preferences. 

You can set or get the Identity and Access Management (IAM), or access control, policy for one or more Connectivity Tests. In addition, you can view the permissions that a user or service account has for a specific Connectivity Test.

This document shows access control examples that use the Network Management API. To follow these steps in the Google Cloud console or by using `gcloud` commands, see the [IAM how-to guides](https://docs.cloud.google.com/iam/docs/how-to).

For information about policy bindings and etags listed in the following commands, see the [API reference for IAM policies](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

For information about the IAM roles and permissions needed to run Connectivity Tests, see [Roles and permissions](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/access-control).

## Set an access control policy

This procedure sets the access control policy on the specified Connectivity Tests resource.

###  API 

Use the [`networkmanagement.connectivitytests.setIamPolicy`](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/setIamPolicy) method to set the access control policy for a `USER`, `ROLE`, and `TEST_ID`.

The following example sets a policy that binds the role of `networkmanagement.admin` to `username@yourcompany.com` for `mytest-1`.
    
    
     POST https: //networkmanagement.googleapis.com/v1/{resource=projects/*/locations/global/connectivityTests/TEST_ID}:setIamPolicy
       {
         "version": "VERSION",
         "etag": "ETAG",
         "bindings": [{
           "role": "ROLE",
           "members": [
             "PRINCIPAL"
           ]
         }]
       }
    

Replace the following values:

  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running
  * `VERSION`: specifies the format of the policy; valid values are `0`, `1`, and `3`—any operation that affects conditional role bindings must specify version `3`
  * `ETAG`: used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other (an example etag is `BwWbrqiZFRs=`)
  * `ROLE`: a role that is assigned to principals (for example, `roles/networkmanagement.admin`)
  * `PRINCIPAL`: specifies the identities requesting access for a Google Cloud resource (for example, `user:username@yourcompany.com`); for a list of principal, or member, types, see the [API reference for IAM policies](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy)



## Get an access control policy

This procedure gets the access control policy for the specified Connectivity Tests resource.

###  API 

Use the [`networkmanagement.connectivitytests.getIamPolicy`](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/getIamPolicy) method to set the access control policy for a `PRINCIPAL`, `ROLE`, and `TEST_ID`.

The following example gets a policy that binds the role of `networkmanagement.admin` to `username@yourcompany.com` for `mytest-1`.
    
    
      GET https: //networkmanagement.googleapis.com/v1/{resource=projects/*/locations/global/connectivityTests/TEST_ID}:getIamPolicy
        {
          "version": "VERSION",
          "etag": "ETAG",
          "bindings": [{
            "role": "ROLE",
            "members": [
              "PRINCIPAL"
            ]
          }]
        }
    

Replace the following values:

  * `TEST_ID`: the ID of the Connectivity Tests object (test) that you are running
  * `VERSION`: specifies the format of the policy; valid values are `0`, `1`, and `3`—any operation that affects conditional role bindings must specify version `3`
  * `ETAG`: used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other (an example etag is `BwWbrqiZFRs=`)
  * `ROLE`: a role that is assigned to principals (for example, `roles/networkmanagement.admin`)
  * `PRINCIPAL`: specifies the identities requesting access for a Google Cloud resource (for example, `user:username@yourcompany.com`); for a list of principal types, see the [API reference for IAM policies](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy)



## Test IAM permissions

This procedure returns permissions that a user or service account has for a Connectivity Tests resource.

###  API 

Use the [`networkmanagement.connectivitytests.testIamPermissions`](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/testIamPermissions) method to return the permissions assigned to a `TEST_ID`.

The following example verifies that `username@yourcompany.com` has the `networkmanagement.connectivitytests.get` permission for `mytest-1`.
    
    
      POST https://networkmanagement.googleapis.com/v1/{resource=projects/*/locations/global/connectivityTests/TEST_ID}:testIamPermissions
        {
          "permissions": [
            "networkmanagement.connectivitytests.get"
          ]
        }
    

Replace `TEST_ID` with the ID of the Connectivity Tests object (test) that you are running.

## What's next

  * [Learn about Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview)
  * [Troubleshoot Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/support/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
