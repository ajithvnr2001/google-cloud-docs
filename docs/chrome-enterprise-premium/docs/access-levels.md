---
url: https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels/
title: Creating and applying access levels to IAP-secured resources \u00a0|\u00a0 Chrome Enterprise Premium \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:43.417060+00:00
---

# Creating and applying access levels to IAP-secured resources  |  Chrome Enterprise Premium  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chrome-enterprise-premium/docs/access-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Chrome Enterprise Premium ](https://docs.cloud.google.com/chrome-enterprise-premium/docs)



Send feedback 

#  Creating and applying access levels to IAP-secured resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create access levels using [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) and apply them on [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview)-secured resources.

## Overview

An [access level](https://docs.cloud.google.com/access-context-manager/docs/overview#access-levels) is a set of attributes assigned to requests based on their origin. Using information such as device type, IP address, and user identity, you can designate what level of access to grant. For example, you might assign a "High_Trust" level to connections from within your corporate network and "Medium_Trust" trust to external devices running approved operating systems.

Device information is gathered and referenced by access levels once you set up [Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview). Endpoint Verification creates an inventory of all the corporate and personal devices accessing your corporate resources.

An access level is enforced by adding it as an [Identity and Access Management (IAM) condition](https://docs.cloud.google.com/iam/docs/conditions-overview) on your [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview)-secured resource. IAP lets you apply a fine-grained, resource-level access control model instead of using network-level firewalls. For example, you might specify that while many resources are available to "Medium_Trust," certain more sensitive resources require the "High_Trust" level.

For more information, see the [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) overview.

## Before you begin

Before you begin, you need to do the following:

  * Secure a resource with IAP.
  * Set up [Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/overview). Note that this is only needed if you want to limit access to your resources based on user device information like storage encryption status.
  * Ensure that you have one of the following roles [granted](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) on your project.

    * Access Context Manager Admin
    * Access Context Manager Editor



## Creating an access level

The following process creates an access level.

For this example, assume you want to create an access level that allows a group of internal auditors to access Google Cloud Observability for a project. All of the devices for the auditors are assigned IPs on a subnet ranging between `203.0.113.0` and `203.0.113.127`. You also want to ensure their devices are encrypted. You know there won't be any devices assigned to that subnet other than those used by the auditors.

###  Console 

  1. Got to the Access Context Manager page in the Google Cloud console.

[Go to the Access Context Manager page](https://console.cloud.google.com/security/access-level)

  2. If you are prompted, select your organization.

  3. At the top of the **Access Context Manager** page, click **New**.

  4. In the **New Access Level** pane, in the **Conditions** section, click **Add attribute** and then click **Device Policy**.

  5. Click the **Storage encryption** drop-down and select **Encrypted**. Note that this rule only works once you [set up Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/quickstart) on your employees' devices.

  6. Click **Add attribute** again and select **IP Subnetworks**.

  7. In the **IP Subnetworks** box, enter one or more IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, you would enter `203.0.113.0/25` in the **IP Subnetworks** box.

  8. Click **Save**.




###  gcloud 

  1. Create a YAML file for an access level that includes one or more IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks.

In this example, to limit access to only the auditors, enter the following into the YAML file:
         
         - ipSubnetworks:
             - 203.0.113.0/25
         - devicePolicy:
             allowedEncryptionStatuses
               - ENCRYPTED
         

For a list of access level attributes and their YAML format, see [Access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes). See this [example access level YAML file](https://docs.cloud.google.com/access-context-manager/docs/example-yaml-file) for a comprehensive YAML file of all possible attributes.

Note that the `devicePolicy` rule only works once you [set up Endpoint Verification](https://docs.cloud.google.com/endpoint-verification/docs/quickstart) on your employees' devices.

  2. Save the file. In this example, the file is named _CONDITIONS.yaml_.

  3. Create the access level.
         
         gcloud access-context-manager levels create NAME \
            --title TITLE \
            --basic-level-spec CONDITIONS.yaml \
            --policy=POLICY_NAME

Where:

     * NAME is the unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores.

     * TITLE is a human-readable title. It must be unique to the policy.

     * POLICY_NAME is the name of your organization's access policy.

You should see output similar to:
    
    Create request issued for: NAME
    Waiting for operation [accessPolicies/POLICY_NAME/accessLevels/NAME/create/1521594488380943] to complete...done.
    Created level NAME.
    




###  API 

  1. Craft a request body to create an [`AccessLevel`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels#AccessLevel) resource that includes one or more IPv4 or IPv6 ranges formatted as [CIDR](https://wikipedia.org/wiki/Classless_Inter-Domain_Routing) blocks and a device policy that requires encrypted storage.

In this example, to limit access to only the auditors, you would enter the following into the request body:
         
         {
          "name": "NAME",
          "title": "TITLE",
          "basic": {
            "conditions": [
              {
                "ipSubnetworks": [
                  "203.0.113.0/25"
                ]
              },
              {
              "devicePolicy": [
                "allowedEncryptionStatuses": [
                  "ENCRYPTED"
                ]
              ]
              }
            ]
          }
         }

Where:

     * NAME is the unique name for the access level. It must begin with a letter and include only letters, numbers, and underscores.

     * TITLE is a human-readable title. It must be unique to the policy.

  2. Create the access level by calling [`accessLevels.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.accessLevels/create).
         
         POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NAME/accessLevels

Where:

     * POLICY_NAME is the name of your organization's access policy.



**Note:** Users that own resources in the organization could learn the names of access levels even without the required permissions. For example, IAP generates a JWT with a [`google.accessLevels`](https://docs.cloud.google.com/iap/docs/signed-headers-howto#verifying_the_jwt_payload) claim that contains the access level names satisfied by the request.

## Applying an access level

An IAP-secured resource has an IAM policy that binds the IAP role to the resource.

By adding an [IAM conditional binding](https://docs.cloud.google.com/iam/docs/conditions-overview) to the IAM policy, access to your resources are further restricted based on request attributes. These request attributes include:

  * Access levels
  * URL host and path
  * Date and time

**Important:** Limiting access based on URL host and path and date and time can only be done with the gcloud CLI.

Note that request values being compared to `request.host` and `request.path` specified in an IAM conditional binding must be exact. For example, if you restrict access to paths starting with `/internal admin`, one can bypass the restriction by going to `/internal%20admin`. See [Using hostname and path conditions](https://docs.cloud.google.com/chrome-enterprise-premium/docs/hostname-and-path-conditions) for more information.

When you apply access levels to an IAP resource, make sure that the access levels are at the organization level, rather than at the project or folder level. The following steps show how to add your access level to a IAP-secured resource by updating its IAM policy.

###  Console 

  1. Go to the [IAP page](https://console.cloud.google.com/security/iap).

[Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Select the checkbox next to the resources that you want to update IAM permissions for.

  3. On the right side **Info panel** , click **Add principal**.

  4. In the **New principal** box, enter the principals that you want to assign a role to.

  5. In the **Select a role** drop-down list, select the **IAP-secured Web App User** role.

  6. To specify existing access levels, select them from the **Access levels** drop-down list. You need to select the **IAP-secured Web App User** role and have organization level permissions to view existing access levels.

When you apply multiple access levels to a resource, users are granted access to the resource when they meet the conditions specified in at least one of the access levels you select (it`s a logical OR of the access levels in the list). If you want users to meet the conditions in more than one access level (a logical AND of access levels), create an access level that contains multiple access levels.

  7. If you want to add more roles to the principals, click **Add another role**.

  8. When you're finished adding roles, click **Save**.




###  gcloud 

Currently, you can only use the gcloud CLI to set project-level conditional bindings.

To set conditional bindings, edit your project's `policy.yaml` file:

  1. Open the IAM policy for the app using the following gcloud command:
         
         gcloud projects get-iam-policy PROJECT_ID > policy.yaml

  2. Edit the `policy.yaml` file to specify the following:

     * The users and groups you want to apply the IAM condition to.
     * The `iap.httpsResourceAccessor` role to grant them access to the resources.
     * The IAM condition with your access level.

The following condition grants access to the user and group if the ACCESS_LEVEL_NAME access level requirements are met and the resource URL path starts with `/`.
    
    ...
    - members:
    - group:EXAMPLE_GROUP@GOOGLE.COM
    - user:EXAMPLE_USER@GOOGLE.COM
    role: roles/iap.httpsResourceAccessor
    condition:
        expression: "accessPolicies/ORGANIZATION_NUMBER/accessLevels/ACCESS_LEVEL_NAME" in request.auth.access_levels && request.path.startsWith("/")
        title: CONDITION_TITLE
    ...

  3. Bind the policy to the app using the `set-iam-policy` command. `none gcloud projects set-iam-policy PROJECT_ID policy.yaml`




###  API 

To edit your app's `policy.json` file, follow the process for your app type. See [Managing access to IAP-secured resources](https://docs.cloud.google.com/iap/docs/managing-access#managing_access_via_the_api) for more information about using the IAM API to manage access policies.

Before you complete the app-specific API steps, export the following variables:
    
    
     export PROJECT_NUM=PROJECT_NUMBER
     export IAP_BASE_URL=https://iap.googleapis.com/v1beta1/projects/${PROJECT_NUMBER}/iap_web
     # Replace POLICY_FILE.JSON with the name of JSON file to use for setIamPolicy
     export JSON_NEW_POLICY=POLICY_FILE.JSON
     

### App Engine

  1. Export the following App Engine variables: 
         
         # The APP_ID is usually the project ID
         export GAE_APP_ID=APP_ID
         export GAE_BASE_URL=${IAP_BASE_URL}/appengine-${GAE_APP_ID}

  2. Get the IAM policy for the App Engine app using the `getIamPolicy` method. The empty data bit at the end turns the `curl` request into POST instead of GET. 
         
         curl -i -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -d '' ${GAE_BASE_URL}/:getIamPolicy

  3. Add your IAM conditional binding to the IAM policy JSON file. The following is an example of an edited `policy.json` file that binds the `iap.httpsResourceAccessor` role to two users, granting them access to the Chrome Enterprise Premium- secured resources. An IAM condition has been added to grant them access to the resources only if the ACCESS_LEVEL_NAME access level requirement is met and the resource URL path starts with `/`. There can be only one condition per binding.  
  
**Example policy.json file**
         
         {
         "policy": {
           "bindings": [
                 {
                   "role": "roles/iap.httpsResourceAccessor",
                   "members": [
                       "group:EXAMPLE_GROUP@GOOGLE.COM",
                       "user:EXAMPLE_USER@GOOGLE.COM"
                   ],
                   "condition": {
                     "expression": ""accessPolicies/ORGANIZATION_NUMBER/accessLevels/ACCESS_LEVEL_NAME" in request.auth.access_levels && request.path.startsWith("/")",
                     "title": "CONDITION_NAME"
                   }
                 }
             ]
           }
         }

  4. Set your new `policy.json` file using the `setIamPolicy` method. 
         
         curl -i -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         ${GAE_BASE_URL}:setIamPolicy -d @${JSON_NEW_POLICY}




#### App Engine services and versions

You can also update the IAM policy of a App Engine service, all versions, or a specific version of a service. To do this for a specific version of a service:

  1. Export the following additional variables. 
         
         export GAE_SERVICE=SERVICE_NAME
         export GAE_VERSION=VERSION_NAME

  2. Update the exported GAE_BASE_URL variable. 
         
         export GAE_BASE_URL=${IAP_BASE_URL}/appengine-${GAE_APP_ID}/services/${GAE_SERVICE}/versions/${GAE_VERSION}

  3. Get and set the IAM policy for the version using the `getIamPolicy` and `setIamPolicy` commands.



### GKE and Compute Engine

  1. Export the project ID of your backend service. 
         
         export BACKEND_SERVICE_NAME=BACKEND_SERVICE_NAME

  2. Get the IAM policy for the Compute Engine app using the `getIamPolicy` method. The empty data bit at the end turns the `curl` request into POST instead of GET. 
         
         curl -i -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          ${IAP_BASE_URL}/compute/services/${BACKEND_SERVICE_NAME}:getIamPolicy \
          -d ''

  3. Add your IAM conditional binding to the IAM policy JSON file. The following is an example of an edited `policy.json` file that binds the `iap.httpsResourceAccessor` role to two users, granting them access to the Chrome Enterprise Premium- secured resources. An IAM condition has been added to grant them access to the resources only if the ACCESS_LEVEL_NAME access level requirement is met and the resource URL path starts with `/`. There can be only one condition per binding.

  
**Example policy.json file**
         
         {
           "policy": {
             "bindings": [
               {
                 "role": "roles/iap.httpsResourceAccessor",
                 "members": [
                   "group":EXAMPLE_GROUP@GOOGLE.COM,
                   "user:EXAMPLE_USER@GOOGLE.COM"
                 ],
                 "condition": {
                   "expression": ""accessPolicies/ORGANIZATION_NUMBER/accessLevels/ACCESS_LEVEL_NAME" in request.auth.access_levels && request.path.startsWith("/")",
                   "title": "CONDITION_NAME"
                 }
               }
             ]
           }
         }

  4. Set your new `policy.json` file using the `setIamPolicy` method. 
         
         curl -i -H "Content-Type:application/json" \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              ${IAP_BASE_URL}/compute/services/${BACKEND_SERVICE_NAME}:setIamPolicy \
              -d @${JSON_NEW_POLICY}




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
