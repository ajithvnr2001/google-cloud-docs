---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/connect-ha-vpn-aws-peer-gateway/
title: Connect HA VPN to AWS peer gateways \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:49.095312+00:00
---

# Connect HA VPN to AWS peer gateways  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/connect-ha-vpn-aws-peer-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Connect HA VPN to AWS peer gateways Stay organized with collections  Save and categorize content based on your preferences. 

When configuring an HA VPN external VPN gateway to Amazon Web Services (AWS), you can use either a transit gateway or a virtual private gateway. Only the transit gateway supports equal-cost multipath (ECMP) routing. When enabled, ECMP equally distributes traffic across active tunnels. The supported topology requires two AWS Site-to-Site VPN connections, `A` and `B`, each with two external IP addresses. This topology yields four external IP addresses in AWS: `A1`, `A2`, `B1`, and `B2`.

**Known issue:** When configuring VPN tunnels to AWS, use the IKEv2 encryption protocol and select fewer transform sets on the AWS side; otherwise, the Cloud VPN tunnel can fail to rekey. For example, select a combination of single Phase 1 and Phase 2 encryption algorithms, integrity algorithms, and DH group numbers. This rekeying issue is caused by a large SA payload size for the default set of AWS transform sets. This large payload size results in IP fragmentation of IKE packets on the AWS side, which Cloud VPN does not support.

## Create HA VPN to AWS peer gateways

  1. Configure the four AWS IP addresses as a single external HA VPN gateway with `FOUR_IPS_REDUNDANCY`, where:
     * AWS IP `0`=`A1`
     * AWS IP `1`=`A2`
     * AWS IP `2`=`B1`
     * AWS IP `3`=`B2`
  2. Create four tunnels on the HA VPN gateway to meet the 99.99% SLA by using the following configuration:
     * HA VPN `interface 0` to AWS `interface 0`
     * HA VPN `interface 0` to AWS `interface 1`
     * HA VPN `interface 1` to AWS `interface 2`
     * HA VPN `interface 1` to AWS `interface 3`



Set up HA VPN with AWS:

  1. In Google Cloud, create an HA VPN gateway and a Cloud Router in the region that you want. This action creates two external IP addresses, one for each gateway interface. Record the external IP addresses for use in the next step.
  2. In AWS, create two customer gateways by using the following: 
     * The **Dynamic** routing option
     * The Google ASN of the Cloud Router
     * The external IP addresses of the Google Cloud HA VPN gateway `interfaces 0` and `1`
  3. Complete the steps that correspond to the AWS VPN option that you are using: 
     * **Transit Gateway**
       1. Create a [transit gateway VPN attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html#create-vpn-attachment) for the first customer gateway (`interface 0`), and use the **Dynamic** routing option.
       2. Repeat the previous step for the second customer gateway (`interface 1`).
     * **Virtual Private Gateway**
       1. [Create a Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-vpn-connection) for the first customer gateway (`interface 0`) by using the following: 
          * A **Target Gateway Type** of **Virtual Private Gateway**
          * The **Dynamic** routing option
       2. Repeat the previous step for the second customer gateway (`interface 1`).
  4. Download the AWS configuration files for both connections that you created. The files contain information that you need during the next steps in this procedure, including pre-shared authentication keys, outside tunnel IP addresses, and inside tunnel IP addresses.
  5. In Google Cloud, do the following: 
     1. Create a new peer VPN gateway with four interfaces by using the AWS external IP addresses from the files that you downloaded in the previous step.
     2. Create four VPN tunnels on the HA VPN gateway that you created in step 1. For each tunnel, configure the HA VPN gateway interface with the appropriate peer VPN gateway interface and pre-shared keys by using the information in the AWS configuration files that you downloaded.
     3. Configure BGP sessions on the Cloud Router by using the BGP IP addresses from the downloaded AWS configuration files.



## Configure the external HA VPN gateway

  1. Configure the four AWS IP addresses as a single external HA VPN gateway with `FOUR_IPS_REDUNDANCY`, where: 
     * AWS IP `0`=`A1`
     * AWS IP `1`=`A2`
     * AWS IP `2`=`B1`
     * AWS IP `3`=`B2`
  2. Create four tunnels on the HA VPN gateway to meet the 99.99% SLA by using the following configuration: 
     * HA VPN `interface 0` to AWS `interface 0`
     * HA VPN `interface 0` to AWS `interface 1`
     * HA VPN `interface 1` to AWS `interface 2`
     * HA VPN `interface 1` to AWS `interface 3`



## Set up HA VPN with AWS

  1. In Google Cloud, create an HA VPN gateway and a Cloud Router in the region that you want. This action creates two external IP addresses, one for each gateway interface. Record the external IP addresses for use in the next step.
  2. In AWS, create two customer gateways by using the following: 
     1. The **Dynamic** routing option
     2. The Google ASN of the Cloud Router
     3. The external IP addresses of the Google Cloud HA VPN gateway `interfaces 0` and `1`
  3. Complete the steps that correspond to the AWS VPN option that you are using:

     1. **Transit Gateway**
        1. Create a [transit gateway VPN attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html#create-vpn-attachment) for the first customer gateway (`interface 0`), and use the **Dynamic** routing option.
        2. Repeat the previous step for the second customer gateway (`interface 1`).
     2. **Virtual Private Gateway**
        1. [Create a Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-vpn-connection) for the first customer gateway (`interface 0`) by using the following: 
           * A **Target Gateway Type** of **Virtual Private Gateway**
           * The **Dynamic** routing option
        2. Repeat the previous step for the second customer gateway (`interface 1`).
  4. Download the AWS configuration files for both connections that you created. The files contain information that you need during the next steps in this procedure, including pre-shared authentication keys, outside tunnel IP addresses, and inside tunnel IP addresses.

  5. In Google Cloud, do the following:

     1. Create a new peer VPN gateway with four interfaces by using the AWS external IP addresses from the files that you downloaded in the previous step.
     2. Create four VPN tunnels on the HA VPN gateway that you created in step 1. For each tunnel, configure the HA VPN gateway interface with the appropriate peer VPN gateway interface and pre-shared keys by using the information in the AWS configuration files that you downloaded.
     3. Configure BGP sessions on the Cloud Router by using the BGP IP addresses from the downloaded AWS configuration files.



## What's next

  * To control which IP addresses are allowed for peer VPN gateways, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
