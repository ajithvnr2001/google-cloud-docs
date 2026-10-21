---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/policy-based-routes/create/
title: gcloud beta network-connectivity policy-based-routes create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:42:21.650093+00:00
---

# gcloud beta network-connectivity policy-based-routes create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-connectivity/policy-based-routes/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta network-connectivity policy-based-routes create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta network-connectivity policy-based-routes create - create a new policy-based route 
SYNOPSIS
    

`gcloud beta network-connectivity policy-based-routes create` `POLICY_BASED_ROUTE` `--network`=`NETWORK` [`--async`] [`--description`=`DESCRIPTION`] [`--destination-range`=`DESTINATION_RANGE`] [`--ip-protocol`=`IP_PROTOCOL`] [`--labels`=[`KEY`=`VALUE`,…]] [`--priority`=`PRIORITY`] [`--protocol-version`=`PROTOCOL_VERSION`; default="IPV4"] [`--source-range`=`SOURCE_RANGE`] [`--interconnect-attachment-region`=`INTERCONNECT_ATTACHMENT_REGION` | `--tags`=[`TAGS`,…]] [`--next-hop-ilb-ip`=`NEXT_HOP_ILB_IP` | `--next-hop-other-routes`=`NEXT_HOP_OTHER_ROUTES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new policy-based route with the given name. 
EXAMPLES
     To create a policy-based route with the name ``my-pbr`` to route all traffic in ``default`` network to an internal load balancer with IP 10.0.0.1, run: 
    
    
    gcloud beta network-connectivity policy-based-routes create my-pbr --network="projects/my-project/global/networks/default" --next-hop-ilb-ip=10.0.0.1

POSITIONAL ARGUMENTS
    

Policy based route resource - Name of the policy-based route to be created. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `policy_based_route` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`POLICY_BASED_ROUTE`
     ID of the policy based route or fully qualified identifier for the policy based route. 

To set the `policy_based_route` attribute: 

  * provide the argument `policy_based_route` on the command line. 


REQUIRED FLAGS
    

`--network`=`NETWORK`
     Fully-qualified URL of the network that this route applies to. E.g. `projects/my-project/global/networks/my-network`
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     Optional description of this resource. Provide this field when you create the resource. 
`--destination-range`=`DESTINATION_RANGE`
     Destination IP range of outgoing packets that this policy-based route applies to. 
`--ip-protocol`=`IP_PROTOCOL`
     IP protocol that this policy-based route applies to. Valid values are `TCP`, `UDP`, and `ALL`. Default is `ALL`. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--priority`=`PRIORITY`
     Priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000. The priority value must be from 1 to 65535, inclusive. Note the priority of policy-based route is always higher than other types of route (e.g. static routes/advanced routes) 
`--protocol-version`=`PROTOCOL_VERSION`; default="IPV4"
     Internet protocol versions that this policy-based route applies to. Valid values are `IPV4`, and `IPV6`. Default is `IPV4'. `PROTOCOL_VERSION` must be one of: *ipv4*, *ipv6*, *protocol-version-unspecified*. `
`--source-range`=`SOURCE_RANGE`
     Source IP range of outgoing packets that this policy-based route applies to. 
At most one of these can be specified: 

`--interconnect-attachment-region`=`INTERCONNECT_ATTACHMENT_REGION`
     Cloud region to install this policy-based route on interconnect attachment. Use all` to install it on all interconnect attachments. Note if both `\--tags` and `\--interconnect-attachment-region` are not set, then the policy-based route will be installed in all network endpoints, including VMs, VPNs, and Interconnect attachements, in the network. `
`--tags`=[`TAGS`,…]
     List of VM instance tags that this route applies to. VM instances that have ANY of tags specified here installs this route. Note if both --tags` and `\--interconnect-attachment-region` are not set, then the policy-based route will be installed in all endpoints, including VMs, VPNs, and Interconnect attachements, in the network. `
At most one of these can be specified: 

`--next-hop-ilb-ip`=`NEXT_HOP_ILB_IP`
     IP of a global access enabled L4 ILB that should be the next hop to handle packets. 
`--next-hop-other-routes`=`NEXT_HOP_OTHER_ROUTES`
     Next hop should be other routes that handle packets. This effectively excludes matching packets being applied on other policy-based routes with a lower priority. `NEXT_HOP_OTHER_ROUTES` must be one of: `default-routing`, `other-routes-unspecified`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `networkconnectivity/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud network-connectivity policy-based-routes create](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes/create)
    
    
    [gcloud alpha network-connectivity policy-based-routes create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-connectivity/policy-based-routes/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
