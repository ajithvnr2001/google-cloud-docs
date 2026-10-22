---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-forwarding-rules-create/
title: gdcloud compute forwarding-rules create \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:32.128127+00:00
---

# gdcloud compute forwarding-rules create  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-compute-forwarding-rules-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud compute forwarding-rules create Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud compute forwarding-rules create - Create forwarding rules for a load balancer.

## SYNOPSIS
    
    
    gdcloud compute forwarding-rules create FORWARDING_RULE_NAME [flags]
    

### EXAMPLES
    
    
    To create the global forwarding rule "fr-elb" for a load balancer, run:
    
        gdcloud compute forwarding-rules create fr-elb \
          --backend-service=network-lb-backend-service \
          --cidr=my-cidr \
          --ip-protocol-port=tcp:8080,udp:443 \
          --global
    
        To create the zonal forwarding rule "fr-ilb" for a load balancer, run:
    
        gdcloud compute forwarding-rules create fr-elb \
          --backend-service=network-lb-backend-service \
          --cidr=my-cidr \
          --ip-protocol-port=tcp:8080,udp:443 \
          --load-balancing-scheme=INTERNAL
    

### REQUIRED FLAGS
    
    
          --ip-protocol-port strings   IP protocol that the rule serves. Note that the protocol must be either TCP or UDP. The L4 port for which packets are forwarded to the backend are configured with this forwarding rule. Protocol defaults to TCP if not specified.
    

### OPTIONAL FLAGS
    
    
          --backend-service string         Target backend service that receives the traffic. It has to reference a backend service in the same namespace as this forwarding rule.
          --cidr string                    CIDR to use for this forwarding rule. It has to be an object in the same namespace as this forwarding rule. If not specified, an IPv4/32 CIDR will be auto-reserved from the IP address pool.
          --global                         If set, the global forwarding rule is created.
          --load-balancing-scheme string   Load balancing scheme of the forwarding rule. Available values are INTERNAL or EXTERNAL. (default "EXTERNAL")
          --zone string                    Zone to use for this invocation. To preset the zone flag for all commands that require it, run: "gdcloud config set core/zone ZONE". The zone flag is available only in multi-zone environments.
    

### GDCLOUD WIDE FLAGS

These flags are available to all commands: `--configuration`, `--format`, `--help`, `--project`, `--quiet`.

For more information, see the [gdcloud CLI reference overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
