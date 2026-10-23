---
url: https://docs.cloud.google.com/mcp/control-mcp-use-vpc-sc-perimeter/
title: Control MCP use in a VPC Service Controls perimeter \u00a0|\u00a0 Google Cloud MCP servers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:38.393009+00:00
---

# Control MCP use in a VPC Service Controls perimeter  |  Google Cloud MCP servers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mcp/control-mcp-use-vpc-sc-perimeter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)
  * [ Google Cloud MCP servers ](https://docs.cloud.google.com/mcp)
  * [ Guides ](https://docs.cloud.google.com/mcp/overview)



Send feedback 

#  Control MCP use in a VPC Service Controls perimeter Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) lets you protect Model Context Protocol (MCP) integrations by establishing context-aware security boundaries around your resources. You can combine [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview) [custom access levels](https://docs.cloud.google.com/access-context-manager/docs/custom-access-levels) with perimeter ingress and egress policies to govern access based on agent identities, network origins, and whether tool calls are read-only. You can't use VPC Service Controls to control access to [non-Google Cloud MCP servers](https://docs.cloud.google.com/mcp/supported-products#google-mcp-servers).

## Before you begin

  1. [Set up a VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter).
  2. Ensure that you have the [correct permissions](https://docs.cloud.google.com/access-context-manager/docs/access-control) to use Access Context Manager.



## Access level attributes

Use the following [`api` attributes](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec#api) in your access levels and egress policies to control MCP use:

  * `mcp.is_mcp`: indicates whether the API call is being made by an MCP service.
  * `mcp.tool.is_read_only`: indicates whether the MCP tool call is read-only.
  * `request.auth.oauth.client_id`: the client ID of the agent principal making the MCP tool call.



## Create a custom access level

[Create a custom access level](https://docs.cloud.google.com/access-context-manager/docs/create-custom-access-level) that uses the `api` attributes to control MCP use within your perimeter. For example, the following access level is only applicable to the principal with the OAuth client ID `12345678-example.apps.googleusercontent.com`:
    
    
    request.auth.oauth.client_id==12345678-example.apps.googleusercontent.com
    

For details about building Common Expression Language (CEL) expressions for custom access levels, refer to the [custom access level specification](https://docs.cloud.google.com/access-context-manager/docs/custom-access-level-spec).

Access levels only allow requests from _outside_ a perimeter for the resources of a protected service _inside_ a perimeter. To allow access from a protected resource inside a perimeter to resources outside the perimeter, create an egress policy. For more information, see [Limitations of using access levels with VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels#limitations_of_using_access_levels_with)

## Configure context-aware ingress rules

[Context-aware ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access) allow access to resources in the perimeter based on client attributes such as network origin (IP address or VPC network), identity type (service account or user), identity, MCP tool call or call type, and device data defined either within the policy or within an access level.

[Configure your ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) to use the custom access level that you created.

For example, the following ingress policy allows ingress to read-only MCP tools in the project number `123456` within a corporate network with the IP range `198.51.100.0/24`:
    
    
    - ingressFrom:
      identityType: ANY_IDENTITY
      sources:
      - accessLevel: accessPolicies/222/accessLevels/corpNetwork_to_readOnlyMcpTool
      ingressTo:
      operations:
      - serviceName: bigquery.googleapis.com
        methodSelectors:
        - method: "*"
      resources:
      - projects/123456
    
    

Where `accessPolicies/222/accessLevels/corpNetwork_to_readOnlyMcpTool` is the name of an access level with the following conditions:
    
    
    inIpRange(origin.ip, '198.51.100.0/24') && 'api.mcp.tool.is_read_only'== true
    

For more information about how to configure ingress rules, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

## Create an egress policy

_Egress_ refers to any access that involves an API client or resources within the service perimeter and resources outside a service perimeter. You might want to use an egress policy to only allow access to Google Cloud APIs outside the perimeter to a specific principal.

For example, the following egress policy allows the principal `//agents.global.org-123456789012.system.id.goog/resources/discoveryengine/projects/9876543210/locations/global/collections/default_collection/engines/my-agent` to access Cloud Storage outside the perimeter. For more information about identities in egress rules, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).
    
    
    egressPolicies:
    - egressTo:
        operations:
        - serviceName: storage.googleapis.com
          methodSelectors:
          - method: '*'
        resources:
        - projects/123
     egressFrom:
        identities:
        - principal://agents.global.org-123456789012.system.id.goog/resources/discoveryengine/projects/9876543210/locations/global/collections/default_collection/engines/my-agent
    

For more information about how to configure egress rules, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

## Examples

The following are useful examples of access levels and ingress policies that control MCP use within a perimeter.

### Deny ingress to MCP requests

The following access level evaluates to true for any API request that isn't sent with MCP:
    
    
    api.mcp.is_mcp == false
    

The following ingress policy allows access to the perimeter for non-MCP API calls:
    
    
    - ingressFrom:
       identityType: ANY_IDENTITY
       sources:
       - accessLevel: ACCESS_POLICY
      ingressTo:
       operations:
       - serviceName: SERVICE_NAME
         methodSelectors:
         - method: "*"
       resources:
       - projects/PROJECT_NUMBER
    

Replace the following:

  * `ACCESS_POLICY`: The name of the access level that you created. To list access levels, follow the instructions in [List access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels#list_access_levels).
  * `SERVICE_NAME`: The name of the protected service—for example, `bigquery.googleapis.com`.
  * `PROJECT_NUMBER`: The Google Cloud project number. To find the project number, see [Find the project name, number, and ID](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).



## What's next

  * [Configure MCP in an AI application](https://docs.cloud.google.com/mcp/configure-mcp-ai-application)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
