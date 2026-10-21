---
url: https://docs.cloud.google.com/deployment-manager/v2beta1/templates/
title: Templates \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:58.728362+00:00
---

# Templates  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/v2beta1/templates/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Templates Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This is a **deprecated** version of the Deployment Manager API. Please use the [latest API version](https://docs.cloud.google.com/deployment-manager/latest) instead.

Represents a Template resource, which defines the settings for your deployments.

For a list of methods for this resource, see the end of this page.

## Resource representations

A Template represents a complete configuration for a Deployment.
    
    
    {
      "name": string,
      "description": string,
      "modules": {
        (key): {
          "type": string,
          "healthCheckModule": {
            "host": string,
            "path": string,
            "port": integer,
            "checkIntervalSec": integer,
            "timeoutSec": integer,
            "unhealthyThreshold": integer,
            "healthyThreshold": integer,
            "description": string
          },
          "lbModule": {
            "targetModules": [
              string
            ],
            "ipProtocol": string,
            "healthChecks": [
              string
            ],
            "ipAddress": string,
            "portRange": string,
            "description": string
          },
          "replicaPoolModule": {
            "numReplicas": integer,
            "envVariables": {
              (key): {
                "value": string,
                "hidden": boolean
              }
            },
            "resourceView": string,
            "replicaPoolParams": {
              "v1beta1": {
                "machineType": string,
                "zone": string,
                "baseInstanceName": string,
                "serviceAccounts": [
                  {
                    "email": string,
                    "scopes": [
                      string
                    ]
                  }
                ],
                "description": string,
                "tags": {
                  "fingerPrint": string,
                  "items": [
                    string
                  ]
                },
                "networkInterfaces": [
                  {
                    "name": string,
                    "network": string,
                    "networkIp": string,
                    "accessConfigs": [
                      {
                        "name": string,
                        "type": string,
                        "natIp": string
                      }
                    ]
                  }
                ],
                "metadata": {
                  "fingerPrint": string,
                  "items": [
                    {
                      "key": string,
                      "value": string
                    }
                  ]
                },
                "canIpForward": boolean,
                "autoRestart": boolean,
                "initAction": string,
                "onHostMaintenance": string,
                "disksToCreate": [
                  {
                    "boot": boolean,
                    "autoDelete": boolean,
                    "attachment": {
                      "deviceName": string,
                      "index": unsigned integer
                    },
                    "initializeParams": {
                      "sourceImage": string,
                      "diskSizeGb": long
                    }
                  }
                ],
                "disksToAttach": [
                  {
                    "source": string,
                    "attachment": {
                      "deviceName": string,
                      "index": unsigned integer
                    }
                  }
                ]
              }
            },
            "healthChecks": [
              string
            ]
          },
          "autoscalingModule": {
            "minNumReplicas": integer,
            "maxNumReplicas": integer,
            "signalType": string,
            "targetUtilization": double,
            "targetModule": string,
            "description": string,
            "coolDownPeriodSec": integer
          },
          "firewallModule": {
            "description": string,
            "network": string,
            "sourceRanges": [
              string
            ],
            "sourceTags": [
              string
            ],
            "targetTags": [
              string
            ],
            "allowed": [
              {
                "IPProtocol": string,
                "ports": [
                  string
                ]
              }
            ]
          },
          "networkModule": {
            "description": string,
            "IPv4Range": string,
            "gatewayIPv4": string
          }
        }
      },
      "actions": {
        (key): {
          "commands": [
            string
          ],
          "timeoutMs": integer
        }
      }
    }

Property name | Value | Description | Notes  
---|---|---|---  
`actions` | `object` | Actions defined for use in the modules that this template defines. |   
`actions.(key)` | `nested object` | The name of this action, used when specifying Actions in Module definitions. |   
`actions.(key).commands[]` | `list` | A list of commands to run sequentially for this action. |   
`actions.(key).timeoutMs` | `integer` | The timeout in milliseconds for this action to run. |   
`description` | `string` | A description of this template. |   
`modules` | `object` | A list of modules for this template. |   
`modules.(key)` | `nested object` | Name of the module. The name must conform to the following regular expression: `[a-zA-Z0-9-_]{1,64}` |   
`modules.(key).autoscalingModule` | `nested object` | Defines an autoscaling module. |   
`modules.(key).autoscalingModule.coolDownPeriodSec` | `integer` | The number of seconds that the autoscaler should wait between two succeeding changes to the number of virtual machines. You should define an interval that is as least as long as the initialization time of a virtual machine. The default is 5 seconds. |   
`modules.(key).autoscalingModule.description` | `string` | An optional description for this autoscaling module. |   
`modules.(key).autoscalingModule.maxNumReplicas` | `integer` | The maximum number of replicas you would like to autoscale to. |   
`modules.(key).autoscalingModule.minNumReplicas` | `integer` | The minimum number of replicas you would like to autoscale to. |   
`modules.(key).autoscalingModule.signalType` | `string` | The signal that Deployment Manager should use to determine if autoscaling is needed.   
  
Acceptable values are: 

  * "`AVG_CPU`": Uses the average CPU of your target replica pool module to determine when to scale.

|   
`modules.(key).autoscalingModule.targetModule` | `string` | The target replica pool module to scale. |   
`modules.(key).autoscalingModule.targetUtilization` | `double` | The target utilization, between `(0, 1]`. The autoscaler works to maintain the value of your desired signal (currently, only average CPU) at approximately this target level. For example, If the average CPU of your replicas is significantly below your target utilization, the autoscaler will scale down, until it reaches the target utilization or the minimum number of replicas. If the average CPU is above this number, the autoscaler will scale up until it reaches the target utilization or the maximum number of resources. |   
`modules.(key).firewallModule` | `nested object` | Creates a firewall module, equivalent to a Google Compute Engine [Firewall resource](https://docs.cloud.google.com/compute/docs/reference/latest/firewalls). |   
`modules.(key).firewallModule.allowed[]` | `quilist` | Defines the allowed ports and protocols for this firewall. |   
`modules.(key).firewallModule.allowed[].IPProtocol` | `string` | The allowed IP protocol for this Firewall module. Can either be `tcp`,`udp`, or `icmp` or an IP protocol number. |   
`modules.(key).firewallModule.allowed[].ports[]` | `list` | List of allowed ports or port ranges (Example inputs include:````` ["22"],` `````[?33?, "12345-12349"]`. |   
`modules.(key).firewallModule.description` | `string` | The description of the firewall. |   
`modules.(key).firewallModule.network` | `string` | ````The Network module to which this firewall should apply. If not specified, or if specified as `default`````, this firewall will be applied to the `default `network. |   
`modules.(key).firewallModule.sourceRanges[]` | `list` | The IP address blocks that this rule applies to, expressed in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) format. One or both of `sourceRanges` and sourceTags may be set. An inbound connection is allowed if either the range or the tag of the source matches the `sourceRanges` or `sourceTags`. |   
`modules.(key).firewallModule.sourceTags[]` | `list` | A list of instance tags which this rule applies to. One or both of `sourceRanges` and sourceTags may be set. An inbound connection is allowed if either the range or the tag of the source matches the `sourceRanges` or `sourceTags`. |   
`modules.(key).firewallModule.targetTags[]` | `list` |  A list of instance tags indicating sets of instances located on network which may make network connections as specified in `allowed[]`. If no `targetTags` are specified, the firewall rule applies to all instances on the specified network. |   
`modules.(key).healthCheckModule` | `nested object` | Defines a health check module to use for load balancing. |   
`modules.(key).healthCheckModule.checkIntervalSec` | `integer` | Sets the interval in seconds to perform a health check. The default is 5 seconds. |   
`modules.(key).healthCheckModule.description` | `string` | A description of this health check module. |   
`modules.(key).healthCheckModule.healthyThreshold` | `integer` | Specifies the number of successful retries before an unhealthy virtual machine instance is marked as healthy. The default is 2. |   
`modules.(key).healthCheckModule.host` | `string` | The value of the host header used in this health check request. For example, if you are serving webpages from an instance using the domain www.mydomain.com, you may want to set the hostname as www.mydomain.com so that the health check for that host is performed.   
  
By default, this is empty and Google Compute Engine automatically sets the host header in health requests to the same external IP address as the forwarding rule associated with this target pool. For example, if a load balancing module has an external IP address of `1.2.3.4` and is directing traffic to a target module pool named `tp1` that has a health check object with a default host setting, the host header would be set to `1.2.3.4`. |   
`modules.(key).healthCheckModule.path` | `string` | The request path for this health check. For example, `/healthcheck`. The default value is `/` |   
`modules.(key).healthCheckModule.port` | `integer` | The TCP port number for this health check request. The default value is `80`. |   
`modules.(key).healthCheckModule.timeoutSec` | `integer` | If Google Compute Engine doesn't receive an `HTTP 200` response from the instance by the `timeoutSec`, the health check request is considered a failure. The default is `5` seconds. |   
`modules.(key).healthCheckModule.unhealthyThreshold` | `integer` | Specifies the number of successful retries before an healthy virtual machine instance is marked as unhealthy. The default is 2. |   
`modules.(key).lbModule` | `nested object` | Specifies a load balancing module. |   
`modules.(key).lbModule.description` | `string` | A description of this load balancing module. |   
`modules.(key).lbModule.healthChecks[]` | `list` | A list of health checks to use for this load balancing module. |   
`modules.(key).lbModule.ipAddress` | `string` | An external static IP that this forwarding rule serves on behalf of. This can be a reserved static IP, or if left blank or unspecified, the default is to assign an ephemeral IP address. Multiple forwarding rules can use the same IP address as long as their port range and protocol do not overlap. For example, `--ip="1.2.3.106"`. |   
`modules.(key).lbModule.ipProtocol` | `string` | The protocol that this load balancing module is handling.   
  
Acceptable values are: 

  * "`TCP`": Specifies the [Transmission Control Protocol](http://www.ietf.org/rfc/rfc793.txt).
  * "`UDP`": Specifies the [User Datagram Protocol](http://www.ietf.org/rfc/rfc768.txt).

|   
`modules.(key).lbModule.portRange` | `string` | The list of ports for which this load balancer is responsible. Packets of the specified protocol sent to these ports will be forwarded on to the appropriate target pool. If this field is left empty, then the load balancer sends traffic for all ports for the specified protocol. Can be a single port, or a range of ports. |   
`modules.(key).lbModule.targetModules[]` | `list` | Specifies the target module that handles traffic from this load balancer. A traffic module contains one or more virtual machine instances that will receive traffic sent to this load balancer.  |   
`modules.(key).networkModule` | `nested object` | Defines a Network module. |   
`modules.(key).networkModule.IPv4Range` | `string` | The range of internal addresses that are legal on this network. This range is a CIDR specification, for example: ```````````````192.168.0.0/16.` |   
`modules.(key).networkModule.description` | `string` | The description of the network. |   
`modules.(key).networkModule.gatewayIPv4` | `string` | An optional address that is used for default routing to other networks. This must be within the range specified by IPv4Range, and is typically the first usable address in that range. If not specified, the default value is the first usable address in IPv4Range. |   
`modules.(key).replicaPoolModule` | `nested object` | Specifies a replica pool module, which creates a Compute Engine virtual machine instance. |   
`modules.(key).replicaPoolModule.envVariables` | `object` | A list of environment variables. |   
`modules.(key).replicaPoolModule.envVariables.(key)` | `nested object` | Name of the environment variable. The name must conform to the following regular expression: `[a-zA-Z_]+[a-zA-Z0-9_]+`. |   
`modules.(key).replicaPoolModule.envVariables.(key).hidden` | `boolean` | Whether this variable is hidden or visible. |   
`modules.(key).replicaPoolModule.envVariables.(key).value` | `string` | Value of the environment variable. |   
`modules.(key).replicaPoolModule.healthChecks[]` | `list` | A list of health checks to use for this replica pool module. |   
`modules.(key).replicaPoolModule.numReplicas` | `integer` | Number of replicas in this module. |   
`modules.(key).replicaPoolModule.replicaPoolParams` | `nested object` | Information for a ReplicaPoolModule. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1` | `nested object` | ReplicaPoolParams specifications for use with ReplicaPools v1beta1. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.autoRestart` | `boolean` | Whether these replicas should be restarted if they experience a failure. The default value is `true`. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.baseInstanceName` | `string` | The base name for instances within this ReplicaPool. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.canIpForward` | `boolean` | Enables IP Forwarding. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.description` | `string` | An optional textual description of the resource. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToAttach[]` | `list` | A list of existing Persistent Disk resources to attach to each replica in the pool. Each disk will be attached in read-only mode to every replica. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToAttach[].attachment` | `nested object` | Optional. How the disk will be attached to the Replica. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToAttach[].attachment.deviceName` | `string` | The device name of this disk. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToAttach[].attachment.index` | `unsigned integer` | A zero-based index to assign to this disk, where 0 is reserved for the boot disk. If not specified, this is assigned by the server. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToAttach[].source` | `string` | The fully-qualified URL of the Persistent Disk resource. It must be in the same zone as the Pool. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[]` | `list` | A list of Disk resources to create and attach to each Replica in the Pool. Currently, you can only define one disk and it must be a root persistent disk. Note that Replica Pool will create a root persistent disk for each replica. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].attachment` | `nested object` | How the disk will be attached to the Replica. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].attachment.deviceName` | `string` | The device name of this disk. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].attachment.index` | `unsigned integer` | A zero-based index to assign to this disk, where 0 is reserved for the boot disk. If not specified, this is assigned by the server. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].autoDelete` | `boolean` | If `true`, then this disk will be deleted when the instance is deleted. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].boot` | `boolean` | If `true`, indicates that this is the root persistent disk. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].initializeParams` | `nested object` | Create the new disk using these parameters. The name of the disk will be `<instance_name>-<five_random_characters>`. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].initializeParams.diskSizeGb` | `long` | The size of the created disk in gigabytes. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.disksToCreate[].initializeParams.sourceImage` | `string` | The name or fully-qualified URL of a source image to use to create this disk. If you provide a name of the source image, the ReplicaPool module will look for an image with that name in your project. If you are specifying an image provided by Compute Engine, you will need to provide the full URL with the correct project, such as:
    
    
    https://www.googleapis.com/compute/v1/projects/debian-cloud/global/images/debian-wheezy-7-vYYYYMMDD

|   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.initAction` | `string` | Name of the Action to be run during initialization of a ReplicaPoolModule. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.machineType` | `string` | The machine type for this instance. Either a complete URL, or the resource name (e.g. `n1-standard-1`). |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.metadata` | `nested object` | The metadata key/value pairs assigned to this instance. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.metadata.fingerPrint` | `string` | The fingerprint of the metadata. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.metadata.items[]` | `list` | A list of metadata items. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.metadata.items[].key` | `string` | A metadata key. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.metadata.items[].value` | `string` | A metadata value. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[]` | `list` | A list of network interfaces for the instance. Currently only one interface is supported by Google Compute Engine. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].accessConfigs[]` | `list` | An array of configurations for this interface. This specifies how this interface is configured to interact with other network services |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].accessConfigs[].name` | `string` | Name of this access configuration. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].accessConfigs[].natIp` | `string` | An external IP address associated with this instance. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].accessConfigs[].type` | `string` | Type of this access configuration file. (Currently only `ONE_TO_ONE_NAT` is legal.) |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].name` | `string` | Name of the interface. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].network` | `string` | The name of the NetworkModule to which this interface applies. If not specified, or specified as 'default', this will use the 'default' network. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.networkInterfaces[].networkIp` | `string` | An optional IPV4 internal network address to assign to the instance for this network interface. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.onHostMaintenance` | `string` | Sets the maintenance behavior for the instances in this replica pool.   
  
Acceptable values are: 

  * "`MIGRATE`": Migrates the instances away from maintenance events without restarting the instances.
  * "`TERMINATE`": Terminate and restart the instances away from maintenance events.

|   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.serviceAccounts[]` | `list` | A list of Service Accounts to enable for this instance. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.serviceAccounts[].email` | `string` | Service account email address. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.serviceAccounts[].scopes[]` | `list` | List of OAuth2 scopes to obtain for the service account. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.tags` | `nested object` | A list of tags to apply to the Google Compute Engine instance to identify resources. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.tags.fingerPrint` | `string` | The fingerprint of the tag. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.tags.items[]` | `list` | Items contained in this tag. |   
`modules.(key).replicaPoolModule.replicaPoolParams.v1beta1.zone` | `string` | The zone for this ReplicaPool. |   
`modules.(key).replicaPoolModule.resourceView` | `string` | _[Output Only]_ The name of the resource view associated with a _  
_replica pool module. This field is generated by the service. |   
`modules.(key).type` | `string` | The type of this module>.   
  
Acceptable values are: 

  * "`AUTOSCALING`": Creates an autoscaling module
  * "`FIREWALL`": Creates a firewall module.
  * "`HEALTH_CHECK`": Creates a health check module.
  * "`LOAD_BALANCING`": Creates a load balancing module.
  * "`NETWORK`": Creates a networking module.
  * "`REPLICA_POOL`": Creates a replica pool module.

|   
`name` | `string` | Name of this template. The name must conform to the expression: `[a-zA-Z0-9-_]{1,64}` |   
  
## Methods

delete
    Deletes a template. This removes the template from your project. Removing the template does not affect any deployments that were created from this template.
get
    Gets detailed information about a template.
insert
    Inserts a template. Inserting a template does not create any resources. You still need to create a deployment with the template before physical resources are created.
list
    Lists all templates within a project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
