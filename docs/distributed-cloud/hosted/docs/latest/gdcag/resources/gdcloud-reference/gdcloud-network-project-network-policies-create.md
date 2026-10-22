---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-network-project-network-policies-create/
title: gdcloud network project-network-policies create \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:13:20.662357+00:00
---

# gdcloud network project-network-policies create  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-network-project-network-policies-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  gdcloud network project-network-policies create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud network project-network-policies create - Create project network policies.

## SYNOPSIS
    
    
    gdcloud network project-network-policies create POLICY_NAME [flags]
    

### EXAMPLES
    
    
    To create an ingress project network policy that targets all user workloads allowing only UDP traffic on Port 53 and TCP traffic on Port 80, run:
        gdcloud network project-network-policies create example-policy \
          --policy-type=Ingress \
          --layer4-configs=udp:53,tcp:80
    
    To create an egress project network policy in project 'project-1' that allows only UDP traffic on port 53 to project 'project-2', run:
        gdcloud network project-network-policies create example-policy \
          --project=project-1 \
          --policy-type=Egress \
          --destination-projects=project-2 \
          --layer4-configs=udp:53
    

### OPTIONAL FLAGS
    
    
          --destination-cidrs string         Destination IPv4 CIDR range to allow traffic to. Can only be specified if 'policy-type' is 'Egress'.
          --destination-projects string      Name of the destination project in the organization to allow traffic to. If not specified, traffic to all project workloads is allowed. Can only be specified if 'policy-type' is 'Egress'.
          --layer4-configs strings           A list of protocol and port combinations to which the policy applies.
                                             This flag can be specified multiple times. For example:
                                                 --layer4-configs=udp:53 --layer4-configs=tcp:8080
                                             A comma-separated list is also supported. For example:
                                                 --layer4-configs=udp:53,tcp:8080
                                             To allow all ports for a protocol, specify only the protocol. For example:
                                                 --layer4-configs=tcp
                                             To allow all protocols and ports, use '--layer4-configs=all'.
                                             This flag cannot be used with '--target-managed-services'.
          --policy-type string               The direction of traffic for the project network policy. Supported values are "Ingress" and "Egress". Defaults to "Ingress" if not specified.
          --source-cidrs string              Source IPv4 CIDR range to allow traffic from. Can only be specified if 'policy-type' is 'Ingress'.
          --source-projects string           Name of the source project in the organization to allow traffic from. If not specified, traffic from all project workloads is allowed. Can only be specified if 'policy-type' is 'Ingress'.
          --target-managed-services string   Name of the managed service to apply this policy on. If omitted, this policy applies to all user workloads within the project.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
