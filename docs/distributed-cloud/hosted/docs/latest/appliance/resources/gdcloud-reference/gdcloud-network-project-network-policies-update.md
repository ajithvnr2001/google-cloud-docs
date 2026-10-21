---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-network-project-network-policies-update/
title: gdcloud network project-network-policies update \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:40.656979+00:00
---

# gdcloud network project-network-policies update  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-network-project-network-policies-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud network project-network-policies update Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud network project-network-policies update - Update project network policies.

## SYNOPSIS
    
    
    gdcloud network project-network-policies update POLICY_NAME [flags]
    

### EXAMPLES
    
    
    To update the source project of an existing ingress PNP from project1 to project2, run:
    
        gdcloud network project-network-policies update example-policy \
          --policyType Ingress \
          --source-projects project2
    
        To update the source project of an existing ingress rule from project1 to all projects, run:
    
        gdcloud network project-network-policies update example-policy \
          --policyType Ingress \
          --source-projects ""
    
        To change the policy of a rule from ingress to egress, run:
    
        gdcloud network project-network-policy update example-policy \
          --policyType Egress \
          --destination-projects project2 \
          --layer4-configs "tcp:80, tcp:81"
    

### OPTIONAL FLAGS
    
    
          --destination-cidrs string         CIDR block to allow traffic to. Can only be specified if policy-type is Egress. (default "unetDef@123")
          --destination-projects string      Name of the destination project in the organization to allow traffic to. If not specified or empty, traffic to all project workloads will be allowed. Can only be specified if policy-type is Egress. (default "unetDef@123")
          --layer4-configs strings           List of comma-separated protocol and port combinations (protocol:port) to which the policy applies. Set to "protocol" if you want to allow all ports for a specific protocol. Set to "all" to make the policy applicable to all ports and protocols. Cannot be specified if 'target-managed-services' is not empty.'
          --policyType string                Direction of the traffic for which you want to specify the policy. Supported values are "Ingress" and "Egress". Defaults to "Ingress" if not specified. (default "unetDef@123")
          --source-cidrs string              CIDR block to allow traffic from. Can only be specified if policy-type is Ingress. (default "unetDef@123")
          --source-projects string           Name of the source project in the organization to allow traffic from. If not specified or empty, traffic from all project workloads will be allowed. Can only be specified if policy-type is Ingress. (default "unetDef@123")
          --target-managed-services string   Name of the managed service to apply this policy on. Omit this field if you want to target all user workloads within the project. Defaults to all user workloads if not specified. (default "unetDef@123")
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
