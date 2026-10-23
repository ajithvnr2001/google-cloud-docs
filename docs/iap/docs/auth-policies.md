---
url: https://docs.cloud.google.com/iap/docs/auth-policies/
title: Use authorization policies to delegate authorization to IAP and IAM \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:22.803260+00:00
---

# Use authorization policies to delegate authorization to IAP and IAM  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/auth-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Use authorization policies to delegate authorization to IAP and IAM Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use authorization policies to designate Identity-Aware Proxy (IAP) as the custom authorization engine in an authorization policy for Application Load Balancers.

To delegate authorization to IAP and Identity and Access Management (IAM), you authorize traffic to a forwarding rule based on IAM or end-user identities for managed load balancers. This lets you enforce IAP-based access control for your backend services.

## Before you begin

  * Understand [authorization policies](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview) concepts.
  * Ensure that the backend services of the forwarding rules don't have IAP enabled. If IAP is enabled, you receive an error when submitting your configuration.
  * [Enable the Network Services API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#enabling_an_api).



## Create the authorization policy and enable IAP

To create an authorization policy, you create a policy file that defines the target and rules, and then enable IAP on the forwarding rule. You can choose to apply IAP only to specific requests by defining conditions in the `httpRules` section of your policy file. If the `httpRules` section is omitted, IAP is enforced on all requests.

###  gcloud 

  1. Run the following command to prepare a `policy.yaml` file. The policy allows clients with an IP address range of `10.0.0.0/24` to enable IAP on a forwarding rule.


    
    
    $ cat << EOF > policy.yaml
    action: CUSTOM
    description: authz policy with Cloud IAP
    name: AUTHZ_POLICY_NAME
    httpRules:
      - from:
          sources:
          - ipBlocks:
            - prefix: "10.0.0.0"
              length: 24
    customProvider:
      cloudIap: {}
    target:
      loadBalancingScheme: EXTERNAL_MANAGED
      resources:
      - https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_ID
    EOF
    

  1. Run the following command to enable IAP on a forwarding rule.


    
    
    gcloud network-security authz-policies import AUTHZ_POLICY_NAME \
    --source=policy.yaml \
    --location=LOCATION \
    --project=PROJECT_ID
    

Replace the following:

  * PROJECT_ID: The Google Cloud project ID.
  * LOCATION: The region that the resource is located in.
  * FORWARDING_RULE_ID: The ID of the forwarding rule resource.
  * AUTHZ_POLICY_NAME: The name of the authorization policy.



###  API 

  1. Run the following command to prepare a `policy.json` file. 
         
         cat << EOF > policy.json
         {
         "name": "AUTHZ_POLICY_NAME",
         "target": {
           "loadBalancingScheme": "INTERNAL_MANAGED",
           "resources": [
             "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/LOCATION/forwardingRules/FORWARDING_RULE_ID"
           ],
         },
         "action": "CUSTOM",
         "httpRules": [
           {
             "from": {
               "sources": {
                 "ipBlocks": [
                   {
                     "prefix": "10.0.0.0",
                     "length": 24
                   }
                 ]
               }
             }
           }
         ],
         "customProvider": {
           "cloudIap": {}
         }
         }
         EOF
         

  2. Run the following command to enable IAP on a forwarding rule. 
         
         curl -X PATCH \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Accept: application/json" \
         -H "Content-Type: application/json" \
         -d @policy.json \
         "https://networksecurity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/authzPolicies"
         

Replace the following:

     * PROJECT_ID: The Google Cloud project ID.
     * LOCATION: The region that the resource is located in.
     * FORWARDING_RULE_ID: The ID of the forwarding rule resource.
     * AUTHZ_POLICY_NAME: The name of the authorization policy.



### Apply permissions to resources

You can use the IAP API to apply IAM permissions to individual resources in an IAP-secured project. IAM permissions granted at a certain level apply to all of the levels underneath it. For example, a permission granted at the project level applies to all of the Google Cloud resources in the project.

Following are some example commands for configuring permissions. For more information, see [`gcloud iap web set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policies/get).

###  gcloud 

In the example commands, replace POLICY_FILE with the path to a YAML formatted file that contains a valid policy. Following is an example YAML file:
    
    
    bindings:
      members: user:example@example.com
      role: roles/iap.httpsResourceAccessor
    

#### Update the permission for who can access the forwarding rule resource
    
    
    gcloud iap web set-iam-policy POLICY_FILE [--organization=ORGANIZATION \
    --folder=FOLDER --project=PROJECT_ID \
    --resource-type=RESOURCE_TYPE --service=SERVICE]
    

#### Configure permission at the organization level
    
    
    gcloud iap web set-iam-policy POLICY_FILE --organization=ORGANIZATION
    

#### Configure permission at the folder level
    
    
    gcloud iap web set-iam-policy POLICY_FILE --folder=FOLDER
    

#### Configure permission at the project level
    
    
    gcloud iap web set-iam-policy POLICY_FILE --project=PROJECT_ID --resource-type=iap_web
    

#### Configure permission for all global forwarding rules in a project
    
    
    gcloud iap web set-iam-policy POLICY_FILE --project=PROJECT_ID --resource-type=forwarding_rule
    

#### Configure permission for all forwarding rules in a project in a region
    
    
    gcloud iap web set-iam-policy POLICY_FILE --project=PROJECT_ID \
    --resource-type=forwarding_rule --region=REGION
    

#### Configure permission for a specific global forwarding rule in a project
    
    
    gcloud iap web set-iam-policy POLICY_FILE --project=PROJECT_ID \
    --resource-type=forwarding_rule --service=SERVICE
    

#### Configure permission for a specific forwarding rule in a project in a region
    
    
    gcloud iap web set-iam-policy POLICY_FILE --project=PROJECT_ID \
    --resource-type=forwarding_rule --service=SERVICE --region=REGION
    

Replace the following:

  * POLICY_FILE: The path to a YAML file that contains a valid policy.
  * ORGANIZATION: The ID of your organization.
  * FOLDER: The folder that contains your application.
  * PROJECT_ID: The Google Cloud project ID.
  * RESOURCE_TYPE: The IAP resource type. The resource type must be `app-engine`, `iap_web`, `compute`, `organization`, or `folder`.
  * SERVICE: The forwarding rule ID or name.
  * REGION: The region that the resource is located in.



###  API 

#### Configure permission at the organization level
    
    
    organization/ORGANIZATION
    

#### Configure permission at the folder level
    
    
    folders/FOLDER
    

#### Configure permission at the project level
    
    
    projects/PROJECT_ID
    

#### Configure permission for all global forwarding rules in a project
    
    
    projects/PROJECT_ID/forwarding_rule
    

#### Configure permission for all forwarding rules in a project in a region
    
    
    projects/PROJECT_ID/iap_web/forwarding_rule-REGION
    

#### Configure permission for a specific global forwarding rule in a project
    
    
    projects/PROJECT_ID/iap_web/forwarding_rule/services/SERVICE
    

#### Configure permission for a specific forwarding rule in a project in a region
    
    
    projects/PROJECT_ID/iap_web/forwarding_rule-REGION/services/SERVICE
    

#### Set the authorization policy
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -d @policy.json \
    "https://iap.googleapis.com/v1/RESOURCE_NAME:setIamPolicy"
    

For `policy.json`, you can create the JSON file by running the following command. Update the values as needed.
    
    
    cat << EOF > policy.json
    {
      "bindings": {
         "members": "user:example@example.com",
         "role": "roles/iap.httpsResourceAccessor",
       }
    }
    EOF
    

Replace the following:

  * ORGANIZATION: The ID of your organization.
  * FOLDER: The folder that contains your application.
  * PROJECT_ID: The Google Cloud project ID.
  * REGION: The region that the resource is located in.
  * SERVICE: The forwarding rule ID or name.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
