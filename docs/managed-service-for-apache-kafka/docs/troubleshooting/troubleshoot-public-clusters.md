---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-public-clusters/
title: Troubleshoot public cluster connectivity \u00a0|\u00a0 Managed Service for Apache Kafka \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:50.095923+00:00
---

# Troubleshoot public cluster connectivity  |  Managed Service for Apache Kafka  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/troubleshooting/troubleshoot-public-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)



Send feedback 

#  Troubleshoot public cluster connectivity Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to resolve issues when connecting to a public Google Cloud Managed Service for Apache Kafka cluster.

## Client connection failures

This section lists issues that your client applications might encounter when connecting to a public cluster.

### Verify public cluster configuration

If client applications can't connect to the public endpoints of the cluster, first confirm that the feature is enabled and configured.

To confirm that the public cluster feature is enabled, do the following:

  1. In the Google Cloud console, go to the **Clusters** page and click the cluster name. On the **Configurations** tab, confirm that public access is enabled.

  2. Alternatively, retrieve the cluster details using `gcloud` or the REST API, and verify that the response contains a `publicClusterConfig` section. For more information, see [Allowed source IP ranges](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-allowed-source-ip-ranges).

  3. Verify that the bootstrap address is publicly resolvable:

     1. Retrieve the bootstrap address of your cluster. For more information, see [Bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).

     2. Run the `dig` command on the hostname part of the bootstrap address (the bootstrap address minus the port number, such as `:9092`):
            
            dig BOOTSTRAP_ADDRESS_HOST +short
            

Replace `BOOTSTRAP_ADDRESS_HOST` with the hostname part of your bootstrap address (for example, `bootstrap.example-cluster.us-central1.managedkafka.example-project.cloud.goog`).

If the public cluster feature is enabled and DNS has resolved successfully, the command returns the external IP addresses associated with the bootstrap endpoint. Example output:
    
    203.0.113.1
    

If the command doesn't return an IP address, verify your connection, confirm the project configuration, or wait a few minutes for DNS propagation to complete.




### Access is blocked by allowed source IP ranges

If you receive `Connection timed out` errors or similar errors when attempting to connect to a public cluster, the client application's external IP address might not be allowed by the cluster's configured allowed source IP ranges.

To resolve this issue, do the following:

  1. Determine the public IP address of the client application. Contact your network administrator if you need help determining the public IP address.

To determine your client machine's outbound public IP address, run `curl -4 ifconfig.me` in your client machine's shell environment.

  2. Verify that this IP address is in the range set in `allowedSourceIpRanges` for the cluster.

     * In the Google Cloud console, check the **Allowed source IP ranges** table on the cluster details page under the **Configurations** tab.

     * Alternatively, retrieve the configured ranges using `gcloud managed-kafka clusters describe`:
           
           gcloud managed-kafka clusters describe CLUSTER_ID \
               --location=LOCATION \
               --format="value(gcpConfig.accessConfig.publicClusterConfig.allowedSourceIpRanges)"
           

Replace the following:

       * `CLUSTER_ID`: The ID of the cluster.
       * `LOCATION`: The location of the cluster.
  3. If the IP address isn't allowed, update the allowed IP ranges on the cluster.

     * In the Google Cloud console, click **Edit** on the cluster details page, update the allowed source IP ranges, and click **Save**.

     * Alternatively, run the following command to add the IP address, and include any existing allowed ranges:
           
           gcloud managed-kafka clusters update CLUSTER_ID \
               --location=LOCATION \
               --allowed-source-ip-ranges=EXISTING_RANGES,CLIENT_IP_RANGE
           

Replace `EXISTING_RANGES,CLIENT_IP_RANGE` with the comma-separated list of allowed CIDR blocks. For more information about allowed source IP range requirements, see [Public clusters](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/create-cluster#public-connectivity).




### Traffic is restricted by client-side or on-premises firewalls

Connectivity issues can occur when client-side or on-premises firewalls block outbound traffic to the public endpoints of the cluster. To resolve this issue, do the following:

  1. Verify outbound firewall rules in the client environment. Make sure that egress is allowed for TCP ports `9092` (SASL) and `9192` (mTLS) to all external IPv4 addresses of the cluster.

  2. Confirm that the external client can resolve the bootstrap address FQDN using DNS debugging tools such as `dig`. You can also run `nslookup` (or equivalent) to diagnose the lookup if `dig` isn't available:

     1. Retrieve the bootstrap address of your cluster. For more information, see [Bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address).

     2. Run `dig` or `nslookup` on the hostname part of the bootstrap address (the bootstrap address minus the port number, such as `:9092`):
            
            dig BOOTSTRAP_ADDRESS_HOST +short
            

Replace `BOOTSTRAP_ADDRESS_HOST` with the hostname part of your bootstrap address.

If resolution is successful, the `dig` command returns the external IP addresses of the cluster. If it doesn't resolve, check for DNS block rules in your firewall or local DNS server.
            
            nslookup BOOTSTRAP_ADDRESS_HOST
            

  3. Verify TCP reachability to the ports using `nc` or `telnet` on the bootstrap address:
         
         nc -zv BOOTSTRAP_ADDRESS_HOST PORT
         

Replace the following:

     * `BOOTSTRAP_ADDRESS_HOST`: The hostname part of the bootstrap address.
     * `PORT`: The port number (typically `9092` for SASL or `9192` for mTLS).
**Note:** Testing reachability using the bootstrap address confirms connectivity to the load balancer, but doesn't verify access to individual broker IP addresses. If `nc` to the bootstrap address succeeds but producing or consuming messages fails, test TCP reachability against each external IP address returned by `publicClusterDetails.externalIpAddresses`:
    
    nc -zv EXTERNAL_IP_ADDRESS PORT
    

Replace `EXTERNAL_IP_ADDRESS` with an external IP address of the cluster. For more information about how to retrieve external IP addresses, see [Public cluster details](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-public-cluster-details).

  4. If the cluster is scaled up or public access is turned off and on, check whether the external IP addresses list has changed.




### Clients experience TLS handshake failures

If you receive errors similar to `TLS handshake failed` when attempting to connect to a public cluster, this issue can occur when the Kafka consumer or producer is configured to use a discovery DNS record instead of the bootstrap address.

To resolve this issue, make sure that the client is configured to connect to the cluster's bootstrap address instead of a discovery DNS record. To retrieve the bootstrap address of your cluster, see [Bootstrap address](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-bootstrap-address). Discovery records (which are listed in the [Public cluster details](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/view-cluster#view-public-cluster-details)) are reserved only for configuring egress firewalls.

_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
