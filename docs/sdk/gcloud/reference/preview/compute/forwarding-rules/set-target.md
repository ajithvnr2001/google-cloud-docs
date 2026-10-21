---
url: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/forwarding-rules/set-target/
title: gcloud preview compute forwarding-rules set-target \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:01.480812+00:00
---

# gcloud preview compute forwarding-rules set-target  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/preview/compute/forwarding-rules/set-target/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud preview compute forwarding-rules set-target Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud preview compute forwarding-rules set-target - modify a forwarding rule to direct network traffic to a new target 
SYNOPSIS
    

`gcloud preview compute forwarding-rules set-target` `NAME` (`--backend-service`=`BACKEND_SERVICE` | `--target-grpc-proxy`=`TARGET_GRPC_PROXY` | `--target-http-proxy`=`TARGET_HTTP_PROXY` | `--target-https-proxy`=`TARGET_HTTPS_PROXY` | `--target-instance`=`TARGET_INSTANCE` | `--target-pool`=`TARGET_POOL` | `--target-ssl-proxy`=`TARGET_SSL_PROXY` | `--target-tcp-proxy`=`TARGET_TCP_PROXY` | `--target-vpn-gateway`=`TARGET_VPN_GATEWAY`) [`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`; default="EXTERNAL"] [`--network`=`NETWORK`] [`--subnet`=`SUBNET`] [`--subnet-region`=`SUBNET_REGION`] [`--target-instance-zone`=`TARGET_INSTANCE_ZONE`] [`--target-pool-region`=`TARGET_POOL_REGION`] [`--target-vpn-gateway-region`=`TARGET_VPN_GATEWAY_REGION`] [`--backend-service-region`=`BACKEND_SERVICE_REGION` | `--global-backend-service`] [`--global` | `--region`=`REGION`] [`--global-target-http-proxy` | `--target-http-proxy-region`=`TARGET_HTTP_PROXY_REGION`] [`--global-target-https-proxy` | `--target-https-proxy-region`=`TARGET_HTTPS_PROXY_REGION`] [`--global-target-tcp-proxy` | `--target-tcp-proxy-region`=`TARGET_TCP_PROXY_REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(PREVIEW)` `gcloud preview compute forwarding-rules set-target` is used to set a new target for a forwarding rule. A forwarding rule directs traffic that matches a destination IP address (and possibly a TCP or UDP port) to a forwarding target (load balancer, VPN gateway or VM instance). 

Forwarding rules can be either global or regional, specified with the ``\--global`` or ``\--region=REGION`` flags. For more information about the scope of a forwarding rule, refer to <https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts>. 

Forwarding rules can be external, internal, internal managed, or internal self-managed, specified with the ``\--load-balancing-scheme=[EXTERNAL|EXTERNAL_MANAGED|INTERNAL|INTERNAL_MANAGED|INTERNAL_SELF_MANAGED]`` flag. External forwarding rules are accessible from the internet, while internal forwarding rules are only accessible from within their VPC networks. You can specify a reserved static external or internal IP address with the ``\--address=ADDRESS`` flag for the forwarding rule. Otherwise, if the flag is unspecified, an ephemeral IP address is automatically assigned (global IP addresses for global forwarding rules and regional IP addresses for regional forwarding rules); an internal forwarding rule is automatically assigned an ephemeral internal IP address from the subnet specified with the ``\--subnet`` flag. You must provide an IP address for an internal self-managed forwarding rule. 

Different types of load balancers work at different layers of the OSI networking model (http://en.wikipedia.org/wiki/Network_layer). Layer 3/4 targets include target pools, target SSL proxies, target TCP proxies, and backend services. Layer 7 targets include target HTTP proxies and target HTTPS proxies. For more information, refer to <https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts>. 
    
    
    When creating a forwarding rule, exactly one of  `_--target-instance_`,
    `_--target-pool_`, `_--target-http-proxy_`, `_--target-https-proxy_`,
    `_--target-grpc-proxy_`, `_--target-ssl-proxy_`,
    `_--target-tcp-proxy_` or `_--target-vpn-gateway_`
    must be specified.

POSITIONAL ARGUMENTS
    

`NAME`
     Name of the forwarding rule to operate on. 
REQUIRED FLAGS
    

Exactly one of these must be specified: 

`--backend-service`=`BACKEND_SERVICE`
     Target backend service that receives the traffic. 
`--target-grpc-proxy`=`TARGET_GRPC_PROXY`
     Target gRPC proxy that receives the traffic. 
`--target-http-proxy`=`TARGET_HTTP_PROXY`
     Target HTTP proxy that receives the traffic. For the acceptable ports, see [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). 
`--target-https-proxy`=`TARGET_HTTPS_PROXY`
     Target HTTPS proxy that receives the traffic. For the acceptable ports, see [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). 
`--target-instance`=`TARGET_INSTANCE`
     Name of the target instance that receives the traffic. The target instance must be in a zone in the forwarding rule's region. Global forwarding rules cannot direct traffic to target instances. If not specified and the ``compute/zone`` property isn't set, you might be prompted to select a zone (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/zone`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/zone ZONE

A list of zones can be fetched by running: 
    
    
    [gcloud compute zones list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/zones/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/zone

Alternatively, the zone can be stored in the environment variable ``CLOUDSDK_COMPUTE_ZONE``. 

`--target-pool`=`TARGET_POOL`
     Target pool that receives the traffic. The target pool must be in the same region as the forwarding rule. Global forwarding rules cannot direct traffic to target pools. 
`--target-ssl-proxy`=`TARGET_SSL_PROXY`
     Target SSL proxy that receives the traffic. For the acceptable ports, see [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). 
`--target-tcp-proxy`=`TARGET_TCP_PROXY`
     Target TCP proxy that receives the traffic. For the acceptable ports, see [Port specifications](https://cloud.google.com/load-balancing/docs/forwarding-rule-concepts#port_specifications). 
`--target-vpn-gateway`=`TARGET_VPN_GATEWAY`
     Target VPN gateway (Cloud VPN Classic gateway) that receives forwarded traffic. Acceptable values for --ports flag are: 500, 4500. 
OPTIONAL FLAGS
    

`--load-balancing-scheme`=`LOAD_BALANCING_SCHEME`; default="EXTERNAL"
     (DEPRECATED) This defines the forwarding rule's load balancing scheme. 

The --load-balancing-scheme option is deprecated and will be removed in an upcoming release. If you're currently using this argument, you should remove it from your workflows. `LOAD_BALANCING_SCHEME` must be one of: 

`EXTERNAL`
     Classic Application Load Balancers, global external proxy Network Load Balancers, external passthrough Network Load Balancers or protocol forwarding, used with one of --target-http-proxy, --target-https-proxy, --target-tcp-proxy, \--target-ssl-proxy, --target-pool, --target-vpn-gateway, --target-instance. 
`EXTERNAL_MANAGED`
     Global and regional external Application Load Balancers, and regional external proxy Network Load Balancers, used with --target-http-proxy, \--target-https-proxy, --target-tcp-proxy. 
`INTERNAL`
     Internal passthrough Network Load Balancers or protocol forwarding, used with \--backend-service. 
`INTERNAL_MANAGED`
     Internal Application Load Balancers and internal proxy Network Load Balancers, used with --target-http-proxy, --target-https-proxy, --target-tcp-proxy. 
`INTERNAL_SELF_MANAGED`
     Traffic Director, used with --target-http-proxy, --target-https-proxy, \--target-grpc-proxy, --target-tcp-proxy. 
`--network`=`NETWORK`
     (DEPRECATED) Only for --load-balancing-scheme=INTERNAL or \--load-balancing-scheme=INTERNAL_SELF_MANAGED or \--load-balancing-scheme=EXTERNAL_MANAGED (regional) or \--load-balancing-scheme=INTERNAL_MANAGED) Network that this forwarding rule applies to. If this field is not specified, the default network is used. In the absence of the default network, this field must be specified. 

The --network option is deprecated and will be removed in an upcoming release. If you're currently using this argument, you should remove it from your workflows. 

`--subnet`=`SUBNET`
     (DEPRECATED) Only for --load-balancing-scheme=INTERNAL and \--load-balancing-scheme=INTERNAL_MANAGED) Subnetwork that this forwarding rule applies to. If the network is auto mode, this flag is optional. If the network is custom mode, this flag is required. 

The --subnet option is deprecated and will be removed in an upcoming release. If you're currently using this argument, you should remove it from your workflows. 

`--subnet-region`=`SUBNET_REGION`
     (DEPRECATED) Region of the subnetwork to operate on. If not specified, the region is set to the region of the forwarding rule. Overrides the default compute/region property value for this command invocation. 

The --subnet-region option is deprecated and will be removed in an upcoming release. If you're currently using this argument, you should remove it from your workflows. 

`--target-instance-zone`=`TARGET_INSTANCE_ZONE`
     Zone of the target instance to operate on. Overrides the default `compute/zone` property value for this command invocation. 
`--target-pool-region`=`TARGET_POOL_REGION`
     Region of the target pool to operate on. If not specified, the region is set to the region of the forwarding rule. Overrides the default `compute/region` property value for this command invocation. 
`--target-vpn-gateway-region`=`TARGET_VPN_GATEWAY_REGION`
     Region of the VPN gateway to operate on. If not specified, the region is set to the region of the forwarding rule. Overrides the default `compute/region` property value for this command invocation. 
At most one of these can be specified: 

`--backend-service-region`=`BACKEND_SERVICE_REGION`
     Region of the backend service to operate on. If not specified, the region is set to the region of the forwarding rule. Overrides the default `compute/region` property value for this command invocation. 
`--global-backend-service`
     If set, the backend service is global. 
At most one of these can be specified: 

`--global`
     If set, the forwarding rule is global. 
`--region`=`REGION`
     Region of the forwarding rule to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

At most one of these can be specified: 

`--global-target-http-proxy`
     If set, the http proxy is global. 
`--target-http-proxy-region`=`TARGET_HTTP_PROXY_REGION`
     Region of the http proxy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

At most one of these can be specified: 

`--global-target-https-proxy`
     If set, the https proxy is global. 
`--target-https-proxy-region`=`TARGET_HTTPS_PROXY_REGION`
     Region of the https proxy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

At most one of these can be specified: 

`--global-target-tcp-proxy`
     If set, the tcp proxy is global. 
`--target-tcp-proxy-region`=`TARGET_TCP_PROXY_REGION`
     Region of the tcp proxy to operate on. If not specified, you might be prompted to select a region (interactive mode only). 

To avoid prompting when this flag is omitted, you can set the ``compute/region`` property: 
    
    
    [gcloud config set](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) compute/region REGION

A list of regions can be fetched by running: 
    
    
    [gcloud compute regions list](https://docs.cloud.google.com/sdk/gcloud/reference/compute/regions/list)

To unset the property, run: 
    
    
    [gcloud config unset](https://docs.cloud.google.com/sdk/gcloud/reference/config/unset) compute/region

Alternatively, the region can be stored in the environment variable ``CLOUDSDK_COMPUTE_REGION``. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in DEVELOPER PREVIEW and may change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud compute forwarding-rules set-target](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/set-target)
    
    
    [gcloud alpha compute forwarding-rules set-target](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/forwarding-rules/set-target)
    
    
    [gcloud beta compute forwarding-rules set-target](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/forwarding-rules/set-target)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
