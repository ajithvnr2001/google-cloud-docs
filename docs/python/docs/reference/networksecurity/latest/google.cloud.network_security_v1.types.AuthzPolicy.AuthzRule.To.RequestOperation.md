---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation
title: Class RequestOperation (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:02.122963+00:00
---

# Class RequestOperation (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RequestOperation (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 
    
    
    RequestOperation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes properties of one or more targets of a request.

## Attributes  
  
---  
**Name** | **Description**  
`header_set` |  `[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.HeaderSet](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.HeaderSet)`   
Optional. A list of headers to match against in http header.   
`hosts` |  `MutableSequence[[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch)]`   
Optional. A list of HTTP Hosts to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 hosts per Authorization Policy.   
`paths` |  `MutableSequence[[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch)]`   
Optional. A list of paths to match against. The match can be one of exact, prefix, suffix, or contains (substring match). Matches are always case sensitive unless the ignoreCase is set. Limited to 10 paths per Authorization Policy. Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method.   
`methods` |  `MutableSequence[str]`   
Optional. A list of HTTP methods to match against. Each entry must be a valid HTTP method name (GET, PUT, POST, HEAD, PATCH, DELETE, OPTIONS). It only allows exact match and is always case sensitive. Limited to 10 methods per Authorization Policy.   
`mcp` |  `[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.MCP](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.To.RequestOperation.MCP)`   
Optional. Defines the MCP protocol attributes to match on. If the MCP payload in the request body cannot be successfully parsed, the request will be denied. This field can be set only for AuthzPolicies targeting AgentGateway resources.   
`snis` |  `MutableSequence[[google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1.types.AuthzPolicy.AuthzRule.StringMatch)]`   
Optional. A list of SNIs to match against. The match can be one of exact, prefix, suffix, or contains (substring match). If there is no SNI (i.e. plaintext HTTP traffic), the request will be denied. Matches are always case sensitive unless the ignoreCase is set. Limited to 10 SNIs per Authorization Policy.   
  
## Classes 

### BaseProtocolMethodsOption
    
    
    BaseProtocolMethodsOption(value)

Describes the option to match against the base MCP protocol methods.

### HeaderSet
    
    
    HeaderSet(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes a set of HTTP headers to match against.

### MCP
    
    
    MCP(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes a set of MCP protocol attributes to match against for a given MCP request.

### MCPMethod
    
    
    MCPMethod(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes a set of MCP methods to match against.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
