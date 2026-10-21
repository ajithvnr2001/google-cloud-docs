---
url: https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions/
title: IAM Conditions for forwarding rules \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:45:17.677298+00:00
---

# IAM Conditions for forwarding rules  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  IAM Conditions for forwarding rules Stay organized with collections  Save and categorize content based on your preferences. 

[Identity and Access Management (IAM) Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) let you define IAM policies with conditional grants. You specify conditions in the [role bindings](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Binding) of a resource's IAM policy. If a condition exists, the role is granted only when the condition expression evaluates to `true`. Each condition expression is a set of logic statements, letting you specify one or many attributes. For more information, see the [Attribute reference for IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference).

When used with Cloud Load Balancing, IAM Conditions let you conditionally grant predefined roles — such as Load Balancer Admin or Network Admin — or custom roles.

IAM Conditions supports a condition expression to check the [load balancing scheme of a forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). For example, you can conditionally grant an IAM principal the ability to create internal load balancers, but not external ones. If that IAM principal attempts to create a forwarding rule for an external load balancer, Google Cloud denies the action and returns an error like the following:
    
    
    ERROR: (gcloud.compute.forwarding-rules.create) Could not fetch resource:
    
     - Required 'compute.forwardingRules.create' permission for
     'projects/PROJECT_ID/regions/REGION/forwardingRules/FORWARDING_RULE_NAME'
    

### Using IAM Conditions on Google Cloud load balancers

The load balancing scheme of a forwarding rule determines which type or types of load balancer can use the forwarding rule. In other words, the load balancing scheme corresponds to the load balancer type, as shown in the following table.

**Note:** Forwarding rules are also used for [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) and [Classic VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) to provide forwarding information in the control plane. This page only discusses forwarding rules in the context of Cloud Load Balancing and [Traffic Director](https://docs.cloud.google.com/service-mesh/docs). However, IAM Conditions affect protocol forwarding and Classic VPN gateways as well.Load balancing scheme | Description  
---|---  
EXTERNAL |  Classic Application Load Balancer  
Classic proxy Network Load Balancer  
External passthrough Network Load Balancer   
EXTERNAL_MANAGED |  Global external Application Load Balancer  
Global external proxy Network Load Balancer  
Regional external Application Load Balancer  
regional external proxy Network Load Balancer   
INTERNAL | Internal passthrough Network Load Balancer  
INTERNAL_MANAGED | Regional internal Application Load Balancer  
Regional internal proxy Network Load Balancer  
Cross-region internal Application Load Balancer  
Cross-region internal proxy Network Load Balancer  
INTERNAL_SELF_MANAGED | Cloud Service Mesh  
  
You specify the `loadBalancingScheme` field when you create the load balancer. By checking the `loadBalancingScheme` field in an IAM condition, you can grant principals the ability to create certain types of load balancers.

### Specifying IAM Conditions

You can set conditional role bindings using the same `setIamPolicy` method that you use to configure any other role bindings. To set a role binding with a condition on a project, you can use the REST API, the `gcloud` command-line tool, or the IAM page in the Google Cloud console.

For more information, see [Managing conditional policies](https://docs.cloud.google.com/iam/docs/managing-conditional-policies).

## Example condition expressions for load balancing

The following condition expression, which can be used in an IAM policy, permits an API request only if one of the following is true:

  * The request doesn't involve creating a forwarding rule.
  * The request is to create a forwarding rule that has one of the internal load balancing schemes.
        
        !compute.isForwardingRuleCreationOperation() || (
          compute.isForwardingRuleCreationOperation() &&
          compute.matchLoadBalancingSchemes(['INTERNAL', 'INTERNAL_MANAGED'])
        )
        




The load balancing scheme `EXTERNAL` is omitted. If a principal tries to create a forwarding rule with the `EXTERNAL` load balancing scheme, a permissions error message appears.

### Example policy

This example IAM policy for a project grants the IAM principal `jane@example.com` the Load Balancer Admin predefined role, excluding the ability to create external load balancers (because the load balancing scheme `EXTERNAL` is omitted). `jane@example.com` can create internal load balancers, and can manage, modify, and delete any load balancer.
    
    
    {
      "bindings": [
        {
          "role": "roles/compute.loadBalancerAdmin",
          "members": ["user:jane@example.com"],
          "condition": {
              "title": "only_internal_lb_schemes",
              "description": "Internal LB creation only permitted",
              "expression": "
                 !compute.isForwardingRuleCreationOperation() || (
                    compute.isForwardingRuleCreationOperation() &&
                    compute.matchLoadBalancingSchemes(['INTERNAL', 'INTERNAL_MANAGED'])
                 )
              "
          }
        }
      ]
    }
    

### Granting GKE service account permissions for specific types of forwarding rules

You can also use IAM Conditions to limit access to the GKE service account to create only specific types of forwarding rules.

This JSON example demonstrates a complete IAM policy to grant the GKE service account (`service-PROJECT_ID@container-engine-robot.iam.gserviceaccount.com`) the Kubernetes Engine Service Agent role. This role allows the service account to create, modify, and delete load balancer components, except for external forwarding rules.

Using this conditional grant, the GKE service account can only create _new_ internal forwarding rules, but can manage all existing forwarding rules.
    
    
    {
      "bindings": [
        {
          "role": "roles/container.serviceAgent",
          "members": ["serviceAccount:service-<var>PROJECT_ID</var>@container-engine-robot.iam.gserviceaccount.com"],
          "condition": {
              "title": "only_internal_lb_schemes",
              "description": "Internal LB Creation Only Permitted",
              "expression": "(
                     compute.isForwardingRuleCreationOperation()
                          &&
                      compute.matchLoadBalancingSchemes(['INTERNAL', 'INTERNAL_MANAGED'])
                  )
                      ||
                  !compute.isForwardingRuleCreationOperation()
              "
          }
        }
      ]
    }
    

Absent other grants, attempting to create a new GKE Service of type LoadBalancer, without the [annotation for an internal passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing), results in an error message like the following:
    
    
    Error creating load balancer (will retry): failed to ensure load balancer for
    service default/SERVICE-NAME: failed to create forwarding rule for load balancer
    (a01d427111c7011ea96e142010a80006(default/SERVICE-NAME)): googleapi: Error 403:
    Required 'compute.forwardingRules.create' permission for
    'projects/PROJECT_ID/regions/[region]/forwardingRules/FORWARDING_RULE_NAME',
    forbidden
    

Also, without other grants, attempting to create a new Ingress object causes a similar error message because the Cloud Load Balancing Ingress controller needs to create an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https).

GKE error messages are available using the `kubectl describe` and `kubectl get events -w` commands.

## What's next

  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * [Grant IAM roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
