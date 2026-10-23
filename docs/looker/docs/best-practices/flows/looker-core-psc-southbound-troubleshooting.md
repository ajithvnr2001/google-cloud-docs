---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-psc-southbound-troubleshooting/
title: Troubleshooting southbound connections \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:58.541309+00:00
---

# Troubleshooting southbound connections  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-psc-southbound-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Troubleshooting southbound connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to troubleshoot southbound (outbound) connection issues for Looker (Google Cloud core) instances that use a private IP configuration with Private Service Connect.

If you're encountering a failure with your southbound Private Service Connect connection, use the following decision tree to begin troubleshooting.

For more information, see [the Looker (Google Cloud core) outbound access to external services using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) documentation.

## Troubleshooting connection errors

Even if the Private Service Connect connection status is `Accepted`, you may still encounter connection errors when Looker (Google Cloud core) attempts to reach your service.

### Hostname resolution issues

If you receive an "Unknown host" error in the Looker (Google Cloud core) UI when testing a database connection, or when Looker (Google Cloud core) attempts to connect to your service, this may indicate that DNS resolution failed for the hostname that you configured for the southbound Private Service Connect connection.

In this case, take the following troubleshooting steps:

  * Verify that the hostname configured in Looker (Google Cloud core) for the service is correct and that it matches the hostname for which a DNS record should exist.
  * Verify that your load balancer and backend service are healthy.
  * Test connectivity from a VM within your producer VPC to ensure that the backend service is reachable through the load balancer's forwarding rule. You can create a temporary VM in the same VPC and region as your load balancer and use a tool like `curl` or `telnet` to test connectivity to service's IP address and port.



If hostname resolution issues persist, contact Cloud Customer Care for assistance.

### Connection timeouts

If connections from Looker (Google Cloud core) to your service are timing out, this may be due to firewall rules in your producer VPC that are blocking traffic from the Private Service Connect NAT subnet, or it may be due to other network issues.

  * Review your firewall rules to ensure that ingress traffic is allowed from the Private Service Connect NAT subnet to your load balancer's backends.
  * Use [Virtual Private Cloud Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) and load balancer logging (such as [internal Application Load Balancer logging](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring) or [internal passthrough Network Load Balancer logging](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring)) to help diagnose connection issues. Virtual Private Cloud Flow Logs can help you determine if traffic from the NAT subnet is reaching your load balancer, and load balancer logs can provide details about whether traffic is being successfully forwarded to healthy backends.



### Verifying southbound Private Service Connect configuration

To verify that the connection between the Looker (Google Cloud core) instance and your network is established correctly, follow these steps:

#### Check Looker (Google Cloud core) instance Private Service Connect endpoint status

To verify the status of the southbound service attachment connection from within the Looker (Google Cloud core) instance's configuration:

  1. In the Google Cloud console, go to the **Looker** page.
  2. Click the name of the instance for which you want to check the connection.
  3. In the **Networking** section, under **Service attachment** , find the endpoint that you are troubleshooting.
  4. Check that the **Status** is `Accepted`.



##### **Pending** status

If the status is `Pending`, it may be due to one of the following reasons:

  * The service attachment's connection preference is not set to 'Automatically accept all connections' and the connection has not been manually approved.
  * The Looker (Google Cloud core) instance's project is not in the service attachment's allowlist.



To resolve a `Pending` status, check your Service Attachment configuration and ensure that the connection preference is set to `Automatically accept all connections`, or that the Looker (Google Cloud core) project has been explicitly allowed.

##### **Closed** status

If the status is `Closed`, the target service attachment might not exist, or mandatory networking prerequisites might be missing. Specifically, any of the following missing prerequisites can trigger a `Closed` connection status:

  * The Looker (Google Cloud core) tenant project ID (for example, `vbb...-tp`) isn't included in the service attachment's consumer allowlist.
  * The backend service lacks a mandatory TCP health check.
  * Cloud NAT isn't configured for the proxy-only subnet, which is required when you're using an Internet NEG.



To resolve a `Closed` status, verify that the target service attachment exists and that all prerequisites — including the tenant project allowlist, TCP health check, and Cloud NAT configuration — are correctly configured.

Because `Closed` is a terminal state, the connection doesn't automatically retry even after backend configurations are fixed. Once you have resolved the underlying configuration issues, you must re-run the `gcloud looker instances update` command with the `--psc-service-attachment` flag to force Looker (Google Cloud core) to re-trigger the connection attempt.

##### Resetting service attachments

If the domain or attachment URI is incorrect, run the `gcloud looker instances update` command again with the correct values. This command overwrites all existing attachments, so all selected attachments must be included. See [**Edit Looker (Google Cloud core) instance settings**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#editing_settings) for more information.

#### Verify producer's service attachment configuration

You should also check the configuration of the service attachment in your producer project to ensure that it's set up correctly to receive connections from Looker (Google Cloud core).

In the Google Cloud console, go to **Network Services > Private Service Connect**, and click the **Published Services** tab. Click the service attachment that is used for the connection to view its details.

Verify that the following requirements are met:

  * The service attachment is configured with a valid target forwarding rule and a dedicated Private Service Connect NAT subnet.
  * The **Connection preference** is set to `Accept automatically`. If connection preference is `Accept for selected networks` or `Accept for selected projects`, ensure that the connection from Looker (Google Cloud core)'s project has been approved.
  * The target service is pointing to the correct forwarding rule.
  * The NAT subnet is correctly configured and has sufficient IP space.
  * The service attachment URI provided to the Looker (Google Cloud core) instance is correct.



You can update service attachment configuration using the Google Cloud console or by running the `gcloud compute service-attachments update` command.

#### Verify firewall rules

Traffic from Looker (Google Cloud core) enters your VPC through the Private Service Connect NAT subnet. You must have firewall rules that allow this traffic to reach the load balancer's backends.

To verify your firewall rules:

  1. Identify the IP range of the Private Service Connect NAT subnet that is configured on your service attachment.
  2. In the Google Cloud console, go to the **Firewall** page in your producer VPC.
  3. Verify that there is an ingress firewall rule that allows TCP traffic from the Private Service Connect NAT subnet to your load balancer's backends on the port used by your service. The rule should meet the following criteria: 
     * **Source filter** : Source IP ranges include the Private Service Connect NAT subnet range.
     * **Targets** : The rule applies to the internal load balancer backends (for example, through network tags).
     * **Protocols and ports** : The rule allows TCP traffic on the port of the target service.



If no such rule exists, or if a higher-priority rule denies this traffic, create an ingress firewall rule to allow traffic from the Private Service Connect NAT subnet.

#### Verify load balancer and Network Endpoint Group configuration

Your service is exposed to Looker (Google Cloud core) through an internal load balancer and a Network Endpoint Group (NEG) that points to your service. Verify that these components are healthy and correctly configured.

To check the NEG configuration:

  1. In the Google Cloud console, go to **Network Services > Load balancing**.
  2. Click your load balancer, and then click the backend service to view its details.
  3. In the backend service details, click the name of the Network Endpoint Group.
  4. Verify the **Network endpoint group type** : 
     * For on-premises or multi-cloud services reachable through Cloud VPN or Cloud Interconnect, the type should be **Hybrid connectivity NEG** (`NON_GCP_PRIVATE_IP_PORT`).
     * For public internet services, such as Git providers, the type should be an **Internet NEG** (`INTERNET_FQDN_PORT`).
  5. In the **Network endpoints** section, check that the IP address and port (for hybrid NEGs) or FQDN and port (for internet NEGs) correctly match your target service.



If the NEG is misconfigured, you may need to update it or create a new one.

#### Verify DNS resolution and routing

If you can't connect from Looker (Google Cloud core), but other troubleshooting steps show no issues, test connectivity from within the producer VPC to isolate the problem:

  1. Create a temporary Compute Engine VM in the same producer VPC and subnet as your internal load balancer.
  2. From that VM, use tools like `telnet` or `nc` to test connectivity to the load balancer's forwarding rule IP address on your service's port — for example: `telnet LOAD_BALANCER_IP TARGET_PORT`.



If you can connect successfully from the VM, the issue is likely in the path from Looker (Google Cloud core) to your VPC. Re-check your service attachment and Looker (Google Cloud core) instance configuration.

If you can't connect from the VM, the issue is likely in your producer VPC. Check the load balancer's forwarding rule, backend service status, and firewall rules within your VPC.

### Investigating specific service connection issues

Certain target services have unique requirements or dependencies when connected through Private Service Connect.

#### Snowflake: Secondary storage endpoints

The Snowflake JDBC driver often downloads result sets or metadata from an intermediate cloud storage location (such as Amazon S3 or Azure Blob Storage), rather than from the primary database host. If Looker (Google Cloud core) is unable to reach these secondary endpoints, connections or queries may fail, especially for large result sets.

To troubleshoot this issue:

  1. Check your Looker (Google Cloud core) logs for timeout errors that reference external storage domains, such as `s3.amazonaws.com` or `blob.core.windows.net`.
  2. Identify the exact FQDN of the storage endpoint required by your Snowflake instance. You can find this information in your Snowflake logs or by contacting Snowflake support.
  3. Each external FQDN must be configured as a separate southbound connection. Create a new Private Service Connect configuration (Internet NEG, load balancer, and service attachment) for the storage endpoint's FQDN.
  4. Add the new service attachment to your Looker (Google Cloud core) instance's configuration.



#### Public Git providers: Egress to the internet

Looker (Google Cloud core) instances with a private IP configuration do not have a default route to the public internet. To connect to public Git providers like GitHub or GitLab, you must explicitly configure an egress path.

To troubleshoot this issue:

  1. Verify if you're trying to connect to a public Git provider from a private IP instance. Connection failures often manifest as generic timeouts or SSL handshake errors.
  2. Create a southbound Private Service Connect connection using an **Internet NEG**.
  3. Ensure the Internet NEG is configured for the correct port (for example, port 22 for SSH or port 443 for HTTPS).
  4. If you have a DNS override policy in your VPC that creates a routing loop with an FQDN-based Internet NEG, consider using an IP-based Internet NEG (`INTERNET_IP_PORT`) instead.



#### Action Hub and Marketplace

The default, Google-hosted Looker (Google Cloud core) Marketplace and Action Hub are public internet services and are not accessible from private IP instances by default.

  * **Action Hub** : To use Action Hub with a private IP instance, you must deploy a self-hosted, private Action Hub server and connect to it using a southbound Private Service Connect connection.
  * **Marketplace** : To connect to the Looker Marketplace, you can enable connection to the Marketplace in your instance's outbound connections configuration. When enabled, Looker (Google Cloud core) uses a [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) to connect directly to the Marketplace and `github.com`. For more information, see [Connect to the Looker Marketplace](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#connect-to-marketplace). If you don't enable this connection, you must manually download the extensions or blocks from their Git repositories and install them as local projects.



#### Check logs

[Virtual Private Cloud Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) and load balancer logging (such as [internal Application Load Balancer logging](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring) or [internal passthrough Network Load Balancer logging](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring)) can provide more insight into connectivity issues.

Enable Virtual Private Cloud Flow Logs on the subnets used by the load balancer and enable logging on the backend service of your internal load balancer, then try to connect from Looker (Google Cloud core) to reproduce the error.

In Cloud Logging, query the Virtual Private Cloud Flow Logs, filtering for traffic from the Private Service Connect NAT subnet IP range to the load balancer's IP address. If traffic is reaching the load balancer, query the load balancing logs for information about the connection status to the backend.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
