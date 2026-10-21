---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-network-project-network-policies-create/
title: gdcloud network project-network-policies create \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:39.978906+00:00
---

# gdcloud network project-network-policies create  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-network-project-network-policies-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud network project-network-policies create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud network project-network-policies create - Create project network policies.

## SYNOPSIS
    
    
    gdcloud network project-network-policies create POLICY_NAME [flags]
    

### EXAMPLES
    
    
    To create a new ingress project network policy that targets all user workloads allowing only UDP traffic on Port 53 and 54, run:
    
        gdcloud network project-network-policies create example-policy \
          --policyType Ingress \
          --layer4-configs 'udp:53, udp:54'
    
        To create a new egress project network policy that sends UDP traffic to only project 'example-proj-2' on port 53, run:
    
        gdcloud network project-network-policies create example-policy \
          --policyType Egress \
          --destination-projects example-proj-2 \
          --layer4-configs 'udp:53'
    

### OPTIONAL FLAGS
    
    
          --destination-cidrs string         CIDR block to allow traffic to. Can only be specified if policy-type is Egress.
          --destination-projects string      Name of the destination project in the organization to allow traffic to. If not specified or empty, traffic to all project workloads will be allowed. Can only be specified if policy-type is Egress.
          --layer4-configs strings           List of comma-separated protocol and port combinations (protocol:port) to which the policy applies. Set to "protocol" if you want to allow all ports for a specific protocol. Set to "all" to make the policy applicable to all ports and protocols. Cannot be specified if 'target-managed-services' is not empty.'
          --policy-type string               Direction of the traffic for which you want to specify the policy. Supported values are "Ingress" and "Egress". Defaults to "Ingress" if not specified.
          --source-cidrs string              CIDR block to allow traffic from. Can only be specified if policy-type is Ingress.
          --source-projects string           Name of the source project in the organization to allow traffic from. If not specified or empty, traffic from all project workloads will be allowed. Can only be specified if policy-type is Ingress.
          --target-managed-services string   Name of the managed service to apply this policy on. Omit this field if you want to target all user workloads within the project. Defaults to all user workloads if not specified.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
