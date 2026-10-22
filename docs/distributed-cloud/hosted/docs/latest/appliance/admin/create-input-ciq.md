---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-input-ciq/
title: Create the config file \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:21.537828+00:00
---

# Create the config file  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-input-ciq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create the config file Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create the input configuration file used to configure the Google Distributed Cloud (GDC) air-gapped appliance.

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

## Before you begin

[Connect the laptop to the switch](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device)

## Create the input configuration file

  1. The appliance configuration process uses an input YAML file. Create this file in the same exact format as the template provided. Fields or sections that are noted as "Optional" must be omitted, not left empty.

  2. The following is an example of an input configuration file.
         
         bgp:
           dataASN: DATAPLANE_ASN
         interconnects:
           customerData:
             asn: CUSTOMER_ASN
             customerPeerSubnets:
             - ipFamily: UPLINK_IP_FAMILY_1
               ipv4:
                 ip: UPLINK_IPV4_PEER_1
                 subnet:
                   gateway: UPLINK_IPV4_GW_1
                   subnet: UPLINK_IPV4_NET_1
               # Optional: Only specify ipv6 for DualStack ipFamily
               ipv6:
                 ip: UPLINK_IPV6_PEER_1
                 subnet:
                   gateway: UPLINK_IPV6_GW_1
                   subnet: UPLINK_IPV6_NET_1
             - ipFamily: UPLINK_IP_FAMILY_2
               ipv4:
                 ip: UPLINK_IPV4_PEER_2
                 subnet:
                   gateway: UPLINK_IPV4_GW_2
                   subnet: UPLINK_IPV4_NET_2
               # Optional: Only specify ipv6 for DualStack ipFamily
               ipv6:
                 ip: UPLINK_IPV6_PEER_2
                 subnet:
                   gateway: UPLINK_IPV6_GW_2
                   subnet: UPLINK_IPV6_NET_2
         dns:
           delegatedSubdomain: DELEGATED_SUBDOMAIN
         externalCIDR:
           ipFamily: IP_FAMILY
           ipv4: EXTERNAL_NETWORK_IPV4
           ipv6: EXTERNAL_NETWORK_IPV6
         
         # Optional: External hardware security module (HSM) information
         externalHSM:
           primaryAddress:  EXTERNAL_HSM_PR_ADDR
           secondaryAddresses:
             - EXTERNAL_HSM_SE_ADDR
           caCert: EXTERNAL_HSM_CA_CERT
           clientCert: EXTERNAL_HSM_CLIENT_CERT
           clientKey: EXTERNAL_HSM_CLIENT_KEY
         
         # Optional: External IdP information
         externalIDP:
           name: EXTERNAL_IDP_NAME
           oidc:
             clientID: EXTERNAL_IDP_CLIENT_ID
             clientSecret: EXTERNAL_IDP_CLIENT_SECRET
             issuerURI: EXTERNAL_IDP_ISSUER_URI
             scopes: EXTERNAL_IDP_SCOPES
             userClaim: EXTERNAL_IDP_USER_CLAIM
             caCert: EXTERNAL_IDP_CA_DATA
           saml:
             idpEntityID: EXTERNAL_IDP_ENTITY_ID
             idpSingleSignOnURI: EXTERNAL_IDP_SSO_URI
             idpCertDataList: EXTERNAL_IDP_CERT_DATA
             userAttribute: EXTERNAL_IDP_USER_ATTRIBUTE
           initialAdmin: EXTERNAL_IDP_INITIAL_ADMIN
         




### Border Gateway Protocol (BGP) information

Border Gateway Protocol (BGP) exchanges routing information with external networks. These networks are identified using autonomous system numbers (ASN). To ensure proper connectivity between GDC air-gapped appliance and the external networks, all ASN values must be globally unique.

  1. `DATAPLANE_ASN`: the **ASN assigned to the data plane** for the GDC air-gapped appliance instance. For example `65204`.

  2. `CUSTOMER_ASN`: the **ASN assigned to the data plane** for the customer network. For example, `4200002002`.


**Note:** The MTU of the interface on the customer network router that connects to the appliance TOR switch must be set to 9216 bytes to avoid any MTU mismatches and potential BGP session flaps.**Note:** Virtual Machine (VM) IP addresses are assigned from the `instance-default-vpc-cidr` range, which is fixed at `192.168.0.0/16`. If the appliance is connected to a customer network through the TOR switch, it is crucial to ensure that the customer network's IP range does not conflict with the `192.168.0.0/16` range. Overlapping IP ranges can lead to incorrect routing of appliance traffic.

### Uplink information

Uplink configurations are peering connections used to externally connect GDC air-gapped appliance instances to other services such as customer networks and other GDC air-gapped appliance instances. These uplink configurations and wiring from a GDC air-gapped appliance instance are important to ensure proper connectivity with the external network.

  1. For each **uplink needed for customer peering** to the GDC air-gapped appliance instance, fill out an uplink item section in the **customer Peer Subnets** field. If the number you provided does not match the expected number of uplinks (2), the remaining uplinks are allocated from the external data plane subnet.
  2. For the uplinks, specify the following: 
     1. `UPLINK_IP_FAMILY_1`, `UPLINK_IP_FAMILY_2`: Specify the **IP family subnet**. Must be either `IPv4` or `DualStack`. 
        1. If you select `IPv4`, 
           1. `UPLINK_IPV4_PEER_1 IP`, `UPLINK_IPV4_PEER_2 IP`: describes the **IP address** assigned on the routed port. If left blank, it will be taken from the **peer subnet block**.
           2. `UPLINK_IPV4_NET_1`, `UPLINK_IPV4_NET_2`: Enter the **peer subnet block** configured on the customer network for the provided switch and port link. This is a `/31` subnet. For example, `172.16.255.148/31`.
           3. `UPLINK_IPV4_GW_1`, `UPLINK_IPV4_GW_2`: Enter the **IP address** representing the customer facing IP address in the `/31` peer subnet. For example, `172.16.255.148`.
        2. If you select `DualStack`, 
           1. `UPLINK_IPV4_PEER_1 IP`, `UPLINK_IPV4_PEER_2 IP`: describes the **IPv4 address** assigned on the routed port. If left blank, it will be taken from the **peer subnet block**.
           2. `UPLINK_IPV4_NET_1`, `UPLINK_IPV4_NET_2`: For IPv4, enter the **peer subnet block** configured on the customer network for the provided switch and port link. This is a `/31` subnet. For example, `172.16.255.148/31`.
           3. `UPLINK_IPV4_GW_1`, `UPLINK_IPV4_GW_2`: For IPv4, enter the **IPv4 address** representing the customer facing IP address in the `/31` peer subnet. For example, `172.16.255.148`.
           4. `UPLINK_IPV6_PEER_1 IP`, `UPLINK_IPV6_PEER_2 IP`: describes the **IPv6 address** assigned on the routed port. If left blank, it will be taken from the **peer subnet block**.
           5. `UPLINK_IPV6_NET_1`, `UPLINK_IPV6_NET_2`: For IPv6, enter the **peer subnet block** configured on the customer network for the provided switch and port link. This is a `/127` subnet. For example, `FC00::/127`.
           6. `UPLINK_IPV6_GW_1`, `UPLINK_IPV6_GW_2`: For IPv6, enter the **IPv6 address** representing the customer facing IP address in the `/127` peer subnet. For example, `FC00::`.



### Domain Name System (DNS) information

  1. `DELEGATED_SUBDOMAIN`: Enter the **DNS delegated subdomain name** for the GDC air-gapped appliance instance from the parent DNS server. This fully qualified domain name is used as a suffix for GDC air-gapped appliance services such as cluster management. The expected format is `LOCATION`.`SUFFIX`.

Replace the following:

     * `LOCATION`: the zone identifier of the GDC air-gapped appliance deployment, such as `us-central1-a`
     * `SUFFIX`: any valid DNS suffix, such as `zone1.google.gdch.test` or `us-central1-a.gdch.customer`



### Data plane network (external CIDR)

  1. For the data plane IP family network, specify if the subnet is IPv4, or DualStack. In the **externalCIDR** section, replace `IP_FAMILY` with either `IPv4` or `DualStack`. 
     1. If you select IPv4, 
        1. Enter the IPv4 network address with minimum size of `23` for the **external dataplane network**. Use this network for external accessible services such as the Management API server and storage interfaces. The network address must be a continuous IP block that is preallocated in your network. For example, replace `EXTERNAL_NETWORK_IPV4` with `10.100.101.0/23`.
     2. If you select DualStack, 
        1. Enter the IPv4 network address with minimum size of `23` for the **external dataplane network**. Use this network for external accessible services such as the Management API server and storage interfaces. The network address must be a continuous IP block that is preallocated in your network. For example, replace `EXTERNAL_NETWORK_IPV4` with `10.100.101.0/23`.
        2. Enter the IPv6 network address with the minimum size of `64`. This IP block is divided into two, the first half is used as the **external dataplane network** and the second half is used as the **internal dataplane network**. For example, replace `EXTERNAL_NETWORK_IPV6` with `FC00::/64`.



### Optional: External hardware security module (HSM) information

HSM devices host encryption keys and perform cryptographic operations using KMIP (Key Management Interoperability Protocol). You can use HSM with NetApp ONTAP Select (OTS) for storage. If you would like to use an external NTP server, fill out the **externalHSM** section.

Before you start, [configure the HSM network](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-hsm-network-connection) first.

  1. `EXTERNAL_HSM_PR_ADDR`: The address of the primary KMIP service. Follow the format of (IP|DNS):Port. If port is omitted, then the default port 5696 will be used.

     * For **IP** , enter the **IP network address** of the KMIP service. For example, `8.8.8.8:5696`.
     * For **DNS name** , enter the fully qualified **domain name** of the KMIP service. For example, `te.us-central1-a:5696`.
  2. `EXTERNAL_HSM_SE_ADDR`: The addresses of the secondary KMIP services. Follow the format of (IP|DNS):Port. If port is omitted, then the default port 5696 will be used. You can specify up to 3 secondary addresses, separated by commas.

  3. `EXTERNAL_HSM_CA_CERT`: Enter the **CACert**. The CA cert is the signed certificate for the KMIP service.

  4. `EXTERNAL_HSM_CLIENT_CERT`: Enter the **client certificate** for connecting to the external HSM.

  5. `EXTERNAL_HSM_CLIENT_KEY`: Enter the **client key** associated with the client certificate for connecting to the external HSM.




### Optional: Connect an identity provider

You can connect to your own existing identity provider (IdP) for identity and access management or alternatively set up a built-in Keycloak IdP. If you would like to use your own identity provider, fill out the **externalIDP** section.

  1. Choose the type of identity provider that you are connecting to: **OIDC** (OpenID Connect) or **SAML** (Security Assertion Markup Language).
  2. If you choose an OIDC provider, specify the following parameters: 
     1. `EXTERNAL_IDP_NAME`: Enter the **name of the IdP**. The name that you provide here is the alias of the identity in the system.
     2. `EXTERNAL_IDP_ISSUER_URI`: Enter the **issuer URI**. The issuer URI must point to the level inside `.well-known/openid-configuration`. Client applications send authorization requests to this URL. The Kubernetes API server uses this URL to discover public keys for verifying tokens.
     3. `EXTERNAL_IDP_CA_DATA`: Enter a base64-encoded PEM-encoded certificate for the **certificate authority data** for the IdP. For more information, see <https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail>. 
        1. To create the string, encode the certificate, including headers, into `base64`.
        2. Include the resulting string as a single line. Example: `LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tC...k1JSUN2RENDQWFT==`
     4. `EXTERNAL_IDP_CLIENT_ID`: Enter the **client ID** for the client application that makes authentication requests to the IdP.
     5. `EXTERNAL_IDP_CLIENT_SECRET`: Enter the **client secret** , which is a shared secret between your IdP and GDC air-gapped appliance.
     6. `EXTERNAL_IDP_USER_CLAIM`: Enter the **user claim** field to identify each user. This is the name of the claim in the OIDC ID Token that holds the username. If this claim is missing from the ID Token, users cannot authenticate. The default claim for many providers is `sub`. You can choose other claims, such as `email` or `name`, depending on the identity provider. Claims other than `email` are prefixed with the issuer URL to prevent naming clashes.
     7. `EXTERNAL_IDP_SCOPES`: If your identity provider requires additional scopes, enter a comma-separated list of **scopes** to send to the IDP. For example, Microsoft Azure and Okta require the `offline_access` scope.
  3. If you choose a SAML provider, specify the following parameters: 
     1. `EXTERNAL_IDP_NAME`: Enter the **name of the IdP**. The name that you provide here is the alias of the identity in the system.
     2. `EXTERNAL_IDP_ENTITY_ID`: Enter the **entity ID** for the SAML provider, specified in a URI format, such as: `https://www.idp.com/saml`.
     3. `EXTERNAL_IDP_SSO_URI`: Enter the **SSO URI** , which is the URI to the SAML provider's SSO endpoint, such as `https://www.idp.com/saml/sso`.
     4. `EXTERNAL_IDP_CERT_DATA`: Enter a list of the **IDP certificates** used to verify the SAML response. These certificates must be standard Base64 encoded and PEM formatted. A maximum of two certificates are supported to facilitate IDP certificate rotation.
     5. `EXTERNAL_IDP_USER_ATTRIBUTE`: Enter the **user attribute** , which is the name of the attribute in the SAML response that holds the username. If this attribute is missing from the SAML response, authentication fails.
  4. `EXTERNAL_IDP_INITIAL_ADMIN`: For both SAML and OIDC providers, enter the account for the **initial admin**. The initial administrator is the first account that is granted access to the system after the installation is complete. The value that you enter must match the claim type, such as an email address if the user claim for an OIDC provider is set to `email`.

Record the name of the initial administrator, as you need this information to login to the system for the first time after the installation is complete.




## What's next

[Configure the device and install software](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
