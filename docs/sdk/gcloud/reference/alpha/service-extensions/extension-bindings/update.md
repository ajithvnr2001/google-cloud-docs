---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-extensions/extension-bindings/update/
title: gcloud alpha service-extensions extension-bindings update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:30:13.294976+00:00
---

# gcloud alpha service-extensions extension-bindings update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/service-extensions/extension-bindings/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha service-extensions extension-bindings update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha service-extensions extension-bindings update - update extensionBindings 
SYNOPSIS
    

`gcloud alpha service-extensions extension-bindings update` (`EXTENSION_BINDING` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--[no-]fail-open`] [`--producer-extension`=`PRODUCER_EXTENSION`] [`--clear-target` `--scope-parent`=`SCOPE_PARENT` `--scope-resource-types`=[`SCOPE_RESOURCE_TYPES`,…] `--target-resources`=[`TARGET_RESOURCES`,…] | `--add-target-resources`=[`ADD_TARGET_RESOURCES`,…] `--clear-target-resources` | `--remove-target-resources`=[`REMOVE_TARGET_RESOURCES`,…]] [`--labels`=[`LABELS`,…] | `--update-labels`=[`UPDATE_LABELS`,…] `--clear-labels` | `--remove-labels`=`REMOVE_LABELS`] [`--match-conditions`=[`to`=`TO`] | `--add-match-conditions`=[`to`=`TO`] `--clear-match-conditions` | `--remove-match-conditions`=[`to`=`TO`]] [`--producer-metadata`=[`PRODUCER_METADATA`,…] | `--update-producer-metadata`=[`UPDATE_PRODUCER_METADATA`,…] `--clear-producer-metadata` | `--remove-producer-metadata`=`REMOVE_PRODUCER_METADATA`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Update an extensionBinding 
EXAMPLES
     To update the extensionBinding, run: 
    
    
    gcloud alpha service-extensions extension-bindings update

POSITIONAL ARGUMENTS
    

ExtensionBinding resource - Identifier. Name of the `ExtensionBinding` resource in the following format: `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `extension_binding` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`EXTENSION_BINDING`
     ID of the extensionBinding or fully qualified identifier for the extensionBinding. 

To set the `extension_binding` attribute: 

  * provide the argument `extension_binding` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the extensionBinding resource. 

To set the `location` attribute: 

  * provide the argument `extension_binding` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A human-readable description of the resource. 
`--etag`=`ETAG`
     Etag of the resource. If provided, it must match the server's etag. If the provided etag does not match the server's etag, the request will fail with a 409 ABORTED error. 
`--[no-]fail-open`
     Determines the behavior of the extension binding when the call to the extension fails or times out. Default value is `FALSE`. 

When set to `TRUE`, failures of the extension are silently ignored. 

Use `--fail-open` to enable and `--no-fail-open` to disable. 

`--producer-extension`=`PRODUCER_EXTENSION`
     The name of the extension that this binding should attach to target resources. 

Format: For Google-provided extensions, specify the service endpoint, for example `modelarmor.us-central1.rep.googleapis.com`. 

Specifies a list of targets to which this `ExtensionBinding` should attach. 
`--clear-target`
     Set extensionBinding.target back to default value. 
Specifies the scope of resources to which this binding should attach. 
`--scope-parent`=`SCOPE_PARENT`
     The parent resource that defines the scope, in the format `projects/{project_number}`. 

When the scope is a project, the binding applies to the resources that meet all of the following conditions: 

  * The resource belongs to the specified project. 
  * The resource is in the same location as the `ExtensionBinding`. 
  * The resource type is listed in `resource_types`. 


`--scope-resource-types`=[`SCOPE_RESOURCE_TYPES`,…]
     The types of resources to which the binding should attach. Limited to 1 resource type. `SCOPE_RESOURCE_TYPES` must be one of: 

`agent-gateway`
     Agent Gateway resources. 
`ai-application`
     AI Application resources. 
Update target_resources. 

At most one of these can be specified: 

`--target-resources`=[`TARGET_RESOURCES`,…]
     Set target_resources to new value. 
Or at least one of these can be specified: 

`--add-target-resources`=[`ADD_TARGET_RESOURCES`,…]
     Add new value to target_resources list. 
At most one of these can be specified: 

`--clear-target-resources`
     Clear target_resources value and set to empty list. 
`--remove-target-resources`=[`REMOVE_TARGET_RESOURCES`,…]
     Remove existing value from target_resources list. 
Update labels. 

At most one of these can be specified: 

`--labels`=[`LABELS`,…]
     Set labels to new value. Set of labels associated with the `ExtensionBinding` resource. 

The format must comply with [the following requirements](https://cloud.google.com/compute/docs/labeling-resources#requirements). 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --labels=string=string

`JSON Example:`
    
    
    --labels='{"string": "string"}'

`File Example:`
    
    
    --labels=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-labels`=[`UPDATE_LABELS`,…]
     Update labels value or add key value pair. Set of labels associated with the `ExtensionBinding` resource. 

The format must comply with [the following requirements](https://cloud.google.com/compute/docs/labeling-resources#requirements). 

`KEY`
     Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`VALUE`
     Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 
`Shorthand Example:`
    
    
    --update-labels=string=string

`JSON Example:`
    
    
    --update-labels='{"string": "string"}'

`File Example:`
    
    
    --update-labels=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-labels`
     Clear labels value and set to empty map. 
`--remove-labels`=`REMOVE_LABELS`
     Remove existing value from map labels. Sets `remove_labels` value. `Shorthand Example:`
    
    
    --remove-labels=string,string

`JSON Example:`
    
    
    --remove-labels=["string"]

`File Example:`
    
    
    --remove-labels=path_to_file.(yaml|json)

Update match_conditions. 

At most one of these can be specified: 

`--match-conditions`=[`to`=`TO`]
     Set match_conditions to new value. A list of match conditions to evaluate against the incoming request. The extension is invoked if the request matches at least one condition, or if no match conditions are specified. A request matches a condition only if it matches every field that is set in that condition. 

Limited to 5 conditions. 

`to`
     Describes properties of a destination of a request. If specified, the extension will only be invoked on requests to destinations that match the specified criteria. 

`destination`
     Describes properties of the destination of a request. A request matches the destination only if it matches every field that is set. Fields that are not set are always considered a match. 

For example, if only `hosts` and `paths` are set, a request matches when any host matches and any path matches. 

At least one of `destination` or `not_destination` must be specified. 

`headerSet`
     A set of HTTP headers to match against. If not specified, requests with any headers are matched. 

`headers`
     A list of HTTP headers to match against. If multiple header matches are provided, they are evaluated as an AND, meaning that all header matches must match for the request to match. Limited to 10 headers. 

`name`
     Specifies the name of the header in the request. 
`value`
     Specifies how the header match will be performed. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`hosts`
     A list of HTTP Hosts to match against. Limited to 10 hosts. If not specified, any host is allowed. If specified, a match occurs if any of the hosts matches the host value in the request. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`paths`
     A list of paths to match against. Limited to 10 paths. If not specified, any path is allowed. 

Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`resources`
     A list of non-empty strings whose value is matched against the resource to which a request is sent (e.g., an Agent in AiApplication). If not specified, any resource is allowed. If specified, a match occurs if any of the resources matches the resource value in the request. Limited to 5 resources. When matching against resources in the AgentRegistry, use the URNs of the registry resources. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`notDestination`
     Describes the negated properties of the request destination. Extension will not be invoked on requests that match the criteria specified in this field. At least one of destination or not_destination must be specified. 

`headerSet`
     A set of HTTP headers to match against. If not specified, requests with any headers are matched. 

`headers`
     A list of HTTP headers to match against. If multiple header matches are provided, they are evaluated as an AND, meaning that all header matches must match for the request to match. Limited to 10 headers. 

`name`
     Specifies the name of the header in the request. 
`value`
     Specifies how the header match will be performed. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`hosts`
     A list of HTTP Hosts to match against. Limited to 10 hosts. If not specified, any host is allowed. If specified, a match occurs if any of the hosts matches the host value in the request. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`paths`
     A list of paths to match against. Limited to 10 paths. If not specified, any path is allowed. 

Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`resources`
     A list of non-empty strings whose value is matched against the resource to which a request is sent (e.g., an Agent in AiApplication). If not specified, any resource is allowed. If specified, a match occurs if any of the resources matches the resource value in the request. Limited to 5 resources. When matching against resources in the AgentRegistry, use the URNs of the registry resources. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`Shorthand Example:`
    
    
    --match-conditions=to={destination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]},notDestination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]}} --match-conditions=to={destination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]},notDestination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]}}

`JSON Example:`
    
    
    --match-conditions='[{"to": {"destination": {"headerSet": {"headers": [{"name": "string", "value": {"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}}]}, "hosts": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "paths": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "resources": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}]}, "notDestination": {"headerSet": {"headers": [{"name": "string", "value": {"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}}]}, "hosts": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "paths": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "resources": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}]}}}]'

`File Example:`
    
    
    --match-conditions=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--add-match-conditions`=[`to`=`TO`]
     Add new value to match_conditions list. A list of match conditions to evaluate against the incoming request. The extension is invoked if the request matches at least one condition, or if no match conditions are specified. A request matches a condition only if it matches every field that is set in that condition. 

Limited to 5 conditions. 

`to`
     Describes properties of a destination of a request. If specified, the extension will only be invoked on requests to destinations that match the specified criteria. 

`destination`
     Describes properties of the destination of a request. A request matches the destination only if it matches every field that is set. Fields that are not set are always considered a match. 

For example, if only `hosts` and `paths` are set, a request matches when any host matches and any path matches. 

At least one of `destination` or `not_destination` must be specified. 

`headerSet`
     A set of HTTP headers to match against. If not specified, requests with any headers are matched. 

`headers`
     A list of HTTP headers to match against. If multiple header matches are provided, they are evaluated as an AND, meaning that all header matches must match for the request to match. Limited to 10 headers. 

`name`
     Specifies the name of the header in the request. 
`value`
     Specifies how the header match will be performed. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`hosts`
     A list of HTTP Hosts to match against. Limited to 10 hosts. If not specified, any host is allowed. If specified, a match occurs if any of the hosts matches the host value in the request. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`paths`
     A list of paths to match against. Limited to 10 paths. If not specified, any path is allowed. 

Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`resources`
     A list of non-empty strings whose value is matched against the resource to which a request is sent (e.g., an Agent in AiApplication). If not specified, any resource is allowed. If specified, a match occurs if any of the resources matches the resource value in the request. Limited to 5 resources. When matching against resources in the AgentRegistry, use the URNs of the registry resources. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`notDestination`
     Describes the negated properties of the request destination. Extension will not be invoked on requests that match the criteria specified in this field. At least one of destination or not_destination must be specified. 

`headerSet`
     A set of HTTP headers to match against. If not specified, requests with any headers are matched. 

`headers`
     A list of HTTP headers to match against. If multiple header matches are provided, they are evaluated as an AND, meaning that all header matches must match for the request to match. Limited to 10 headers. 

`name`
     Specifies the name of the header in the request. 
`value`
     Specifies how the header match will be performed. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`hosts`
     A list of HTTP Hosts to match against. Limited to 10 hosts. If not specified, any host is allowed. If specified, a match occurs if any of the hosts matches the host value in the request. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`paths`
     A list of paths to match against. Limited to 10 paths. If not specified, any path is allowed. 

Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`resources`
     A list of non-empty strings whose value is matched against the resource to which a request is sent (e.g., an Agent in AiApplication). If not specified, any resource is allowed. If specified, a match occurs if any of the resources matches the resource value in the request. Limited to 5 resources. When matching against resources in the AgentRegistry, use the URNs of the registry resources. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`Shorthand Example:`
    
    
    --add-match-conditions=to={destination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]},notDestination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]}} --add-match-conditions=to={destination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]},notDestination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]}}

`JSON Example:`
    
    
    --add-match-conditions='[{"to": {"destination": {"headerSet": {"headers": [{"name": "string", "value": {"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}}]}, "hosts": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "paths": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "resources": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}]}, "notDestination": {"headerSet": {"headers": [{"name": "string", "value": {"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}}]}, "hosts": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "paths": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "resources": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}]}}}]'

`File Example:`
    
    
    --add-match-conditions=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-match-conditions`
     Clear match_conditions value and set to empty list. 
`--remove-match-conditions`=[`to`=`TO`]
     Remove existing value from match_conditions list. A list of match conditions to evaluate against the incoming request. The extension is invoked if the request matches at least one condition, or if no match conditions are specified. A request matches a condition only if it matches every field that is set in that condition. 

Limited to 5 conditions. 

`to`
     Describes properties of a destination of a request. If specified, the extension will only be invoked on requests to destinations that match the specified criteria. 

`destination`
     Describes properties of the destination of a request. A request matches the destination only if it matches every field that is set. Fields that are not set are always considered a match. 

For example, if only `hosts` and `paths` are set, a request matches when any host matches and any path matches. 

At least one of `destination` or `not_destination` must be specified. 

`headerSet`
     A set of HTTP headers to match against. If not specified, requests with any headers are matched. 

`headers`
     A list of HTTP headers to match against. If multiple header matches are provided, they are evaluated as an AND, meaning that all header matches must match for the request to match. Limited to 10 headers. 

`name`
     Specifies the name of the header in the request. 
`value`
     Specifies how the header match will be performed. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`hosts`
     A list of HTTP Hosts to match against. Limited to 10 hosts. If not specified, any host is allowed. If specified, a match occurs if any of the hosts matches the host value in the request. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`paths`
     A list of paths to match against. Limited to 10 paths. If not specified, any path is allowed. 

Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`resources`
     A list of non-empty strings whose value is matched against the resource to which a request is sent (e.g., an Agent in AiApplication). If not specified, any resource is allowed. If specified, a match occurs if any of the resources matches the resource value in the request. Limited to 5 resources. When matching against resources in the AgentRegistry, use the URNs of the registry resources. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`notDestination`
     Describes the negated properties of the request destination. Extension will not be invoked on requests that match the criteria specified in this field. At least one of destination or not_destination must be specified. 

`headerSet`
     A set of HTTP headers to match against. If not specified, requests with any headers are matched. 

`headers`
     A list of HTTP headers to match against. If multiple header matches are provided, they are evaluated as an AND, meaning that all header matches must match for the request to match. Limited to 10 headers. 

`name`
     Specifies the name of the header in the request. 
`value`
     Specifies how the header match will be performed. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`hosts`
     A list of HTTP Hosts to match against. Limited to 10 hosts. If not specified, any host is allowed. If specified, a match occurs if any of the hosts matches the host value in the request. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`paths`
     A list of paths to match against. Limited to 10 paths. If not specified, any path is allowed. 

Note that this path match includes the query parameters. For gRPC services, this should be a fully-qualified name of the form /package.service/method. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`resources`
     A list of non-empty strings whose value is matched against the resource to which a request is sent (e.g., an Agent in AiApplication). If not specified, any resource is allowed. If specified, a match occurs if any of the resources matches the resource value in the request. Limited to 5 resources. When matching against resources in the AgentRegistry, use the URNs of the registry resources. 

`contains`
     The input string must contain the substring specified here. An empty substring is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc.def`. 


`exact`
     The input string must match exactly the string specified here. 

Examples: 

  * `abc` only matches the value `abc`. 


`ignoreCase`
     If true, the `exact`, `prefix`, `suffix`, or `contains` match is case insensitive. For example, the matcher `data` matches both `Data` and `data` when set to true. 
`prefix`
     The input string must have the prefix specified here. An empty prefix is not allowed. 

Examples: 

  * `abc` matches the value `abc.xyz`. 


`suffix`
     The input string must have the suffix specified here. An empty suffix is not allowed. 

Examples: 

  * `abc` matches the value `xyz.abc`. 


`Shorthand Example:`
    
    
    --remove-match-conditions=to={destination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]},notDestination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]}} --remove-match-conditions=to={destination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]},notDestination={headerSet={headers=[{name=string,value={contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}}]},hosts=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],paths=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}],resources=[{contains=string,exact=string,ignoreCase=boolean,prefix=string,suffix=string}]}}

`JSON Example:`
    
    
    --remove-match-conditions='[{"to": {"destination": {"headerSet": {"headers": [{"name": "string", "value": {"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}}]}, "hosts": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "paths": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "resources": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}]}, "notDestination": {"headerSet": {"headers": [{"name": "string", "value": {"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}}]}, "hosts": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "paths": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}], "resources": [{"contains": "string", "exact": "string", "ignoreCase": boolean, "prefix": "string", "suffix": "string"}]}}}]'

`File Example:`
    
    
    --remove-match-conditions=path_to_file.(yaml|json)

Update producer_metadata. 

At most one of these can be specified: 

`--producer-metadata`=[`PRODUCER_METADATA`,…]
     Set producer_metadata to new value. Additional metadata that should be passed to the attached extension with each request. 

This field is subject to the following limitations: 

  * The total size of the metadata must be less than 1 KiB. 
  * The total number of keys must be less than 16. 
  * The length of each key must be less than 64 characters. 
  * The length of each value must be less than 1024 characters. 



`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --producer-metadata=string=string

`JSON Example:`
    
    
    --producer-metadata='{"string": "string"}'

`File Example:`
    
    
    --producer-metadata=path_to_file.(yaml|json)

Or at least one of these can be specified: 

`--update-producer-metadata`=[`UPDATE_PRODUCER_METADATA`,…]
     Update producer_metadata value or add key value pair. Additional metadata that should be passed to the attached extension with each request. 

This field is subject to the following limitations: 

  * The total size of the metadata must be less than 1 KiB. 
  * The total number of keys must be less than 16. 
  * The length of each key must be less than 64 characters. 
  * The length of each value must be less than 1024 characters. 



`KEY`
     Sets `KEY` value. 
`VALUE`
     Sets `VALUE` value. 
`Shorthand Example:`
    
    
    --update-producer-metadata=string=string

`JSON Example:`
    
    
    --update-producer-metadata='{"string": "string"}'

`File Example:`
    
    
    --update-producer-metadata=path_to_file.(yaml|json)

At most one of these can be specified: 

`--clear-producer-metadata`
     Clear producer_metadata value and set to empty map. 
`--remove-producer-metadata`=`REMOVE_PRODUCER_METADATA`
     Remove existing value from map producer_metadata. Sets `remove_producer_metadata` value. `Shorthand Example:`
    
    
    --remove-producer-metadata=string,string

`JSON Example:`
    
    
    --remove-producer-metadata=["string"]

`File Example:`
    
    
    --remove-producer-metadata=path_to_file.(yaml|json)

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkservices/v1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/networking>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta service-extensions extension-bindings update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/service-extensions/extension-bindings/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
