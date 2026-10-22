---
url: https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting/
title: Troubleshooting Looker (Google Cloud core) networking issues \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:40.039940+00:00
---

# Troubleshooting Looker (Google Cloud core) networking issues  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Troubleshooting Looker (Google Cloud core) networking issues Stay organized with collections  Save and categorize content based on your preferences. 

You can diagnose and resolve common inbound and outbound connectivity issues for your Looker (Google Cloud core) instance across public, private, and hybrid networking configurations. Troubleshooting your custom domains, Private Service Connect, private services access, and controlled egress helps you restore user access to your instance and maintain connections to identity providers, external services, and database backends.

## Custom domain verification fails with code 9 error

When you configure a custom domain for a Looker (Google Cloud core) instance that uses public connections, domain verification might fail with a `code: 9` error.

### Symptoms

When you click **VERIFY DOMAIN** on the **CUSTOM DOMAIN** tab of your Looker (Google Cloud core) instance, verification fails and displays an error message similar to the following:
    
    
    DNS record is not created or not the same as public IP address (code: 9)
    

The custom domain status also remains **Unverified** or displays as **Unavailable**.

### Cause

Although the error message indicates that the DNS A record is missing or incorrect, this error typically occurs for one of the following reasons:

  * **Restrictive CAA records** : Your domain's DNS configuration includes Certification Authority Authorization (CAA) records that don't authorize Google's Certificate Authorities (CAs) to issue SSL/TLS certificates. Because Looker (Google Cloud core) uses Google-managed certificates for public instances, certificate provisioning fails.
  * **Third-party CDN or proxy** : Looker (Google Cloud core) instances with public connections exclusively use Load Balancer (LB) authorization for Google-managed certificates. LB authorization requires that your custom domain's DNS A record resolves directly to the Looker (Google Cloud core) ingress public IP address. If you route traffic through a third-party Content Delivery Network (CDN), web application firewall (WAF), or reverse proxy (such as Akamai or Cloudflare), automated LB authorization fails.



### Resolution

Depending on the cause of the failure, use the following methods to resolve the issue:

#### Authorize Google Certificate Authorities in CAA records

If your domain uses CAA records, then verify and update your DNS records to permit Google's certificate providers:

  1. Check your domain's existing CAA records using a DNS lookup tool such as `dig`:
         
         dig CAA DOMAIN_NAME +short
         

Replace `DOMAIN_NAME` with your custom domain name (for example, `example.com` or `looker.example.com`).

  2. Add CAA records to authorize both `pki.goog` and `letsencrypt.org`:
         
         DOMAIN_NAME. IN CAA 0 issue "pki.goog"
         DOMAIN_NAME. IN CAA 0 issue "letsencrypt.org"
         

Allowing both CAs ensures reliable automated provisioning and renewal.

  3. After updating your CAA records, wait for DNS propagation, and then click **VERIFY DOMAIN** again in the Google Cloud console.




#### Use Private Service Connect for third-party CDNs and proxies

Third-party CDNs and reverse proxies cannot be placed directly in front of a public Looker (Google Cloud core) instance because automated Load Balancer authorization requires direct DNS resolution to the instance's public IP address.

To route incoming traffic through a third-party CDN or WAF, deploy Looker (Google Cloud core) using a [Private Service Connect architecture](https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public) instead of public connections:

  1. Deploy a Looker (Google Cloud core) instance with Private Service Connect enabled.
  2. Configure an external Application Load Balancer with a Private Service Connect backend in your VPC network.
  3. Provision and attach your own self-managed or Google-managed SSL certificate to the external Application Load Balancer. This architecture gives you control over TLS termination and lets you route traffic through your CDN or WAF.



## OpenID Connect authentication failure with controlled egress

When you set up OpenID Connect authentication on a Looker (Google Cloud core) instance that's configured with Private Service Connect and controlled egress enabled, authentication might fail.

### Symptoms

If authentication has failed, you might experience either of the following symptoms:

  * The Looker `/openidconnect` endpoint hangs for approximately 60 seconds in the browser before displaying an error or timing out with a `504 Upstream Request Timeout` or `504 Gateway Timeout` error.
  * Your identity provider displays an error message indicating that the redirect URI doesn't match, such as:
        
        AADSTS50011: The redirect URI specified in the request does not match the
        redirect URIs configured for the application
        

This error message is misleading because the redirect URI that you configured in your identity provider might be correct. The actual failure occurs when Looker (Google Cloud core) cannot contact the token endpoint of the identity provider during the backend exchange.




### Cause

The automated provisioning workflow for controlled egress occasionally fails to create the necessary Secure Web Proxy network route (`looker-swp-route`) in the Looker (Google Cloud core) tenant project.

When this route is missing, backend requests from Looker (Google Cloud core) to the identity provider's token endpoint time out because the instance cannot route outbound traffic to the public internet through the Secure Web Proxy.

### Resolution

To resolve this issue, follow these steps to reset the controlled egress configuration to force the system to recreate the missing network route:

  1. In the Google Cloud console, go to the **Looker** page:

[Go to Looker](https://console.cloud.google.com/looker)

  2. Click the name of the instance that you want to update.

  3. Click **Edit**.

  4. Expand the **Connections** section and go to the **Configure outbound connections** section.

  5. Record all existing fully qualified domain names (FQDNs) listed in the **Global FQDN** section (such as your identity provider's endpoints).

  6. Delete all FQDNs that are listed in the **Global FQDN** section.

  7. Clear the **Enable Looker to connect to external services** checkbox to disable controlled egress.

  8. Click **Save**.

  9. Wait for the instance update to finish and for the configuration changes to clear.

  10. Click **Edit** again.

  11. Expand the **Connections** section and select the **Enable Looker to connect to external services** checkbox.

  12. In the **Global FQDN** section, re-add the required FQDNs for your identity provider and any other external services.

  13. Click **Save**.




Resetting controlled egress triggers the automated provisioning process to recreate the missing `looker-swp-route` network route. After the route is created, outbound backend requests to the identity provider can be completed.

## 504 Upstream Request Timeout error

When you make API calls, run long-running queries, or authenticate with an external service on a Looker (Google Cloud core) instance, the request might fail with an HTTP `504` timeout error.

### Symptoms

You might receive a `504 Upstream Request Timeout` or `504 Gateway Timeout` error in either of the following scenarios:

  * **Inbound API calls or queries** : API calls to Looker endpoints, such as `/result_format`, or long-running queries in the Looker UI fail with a `504` error after approximately 30 seconds on an instance that's fronted by a load balancer.
  * **Outbound authentication or external service connections** : You receive a `504` error in your browser after returning from an identity provider's sign-in page or when connecting to an external service on an instance with controlled egress enabled.



### Cause

A `504` timeout error typically occurs for one of the following reasons:

  * **Load balancer backend service timeout for inbound requests** : When your Looker (Google Cloud core) instance is accessed through a Cloud Load Balancing load balancer, the load balancer's backend service has a default [backend service timeout](https://docs.cloud.google.com/load-balancing/docs/backend-service#timeout-setting) of 30 seconds. If the combined database query execution time and Looker payload rendering time exceed this timeout limit, the load balancer closes the connection and returns an HTTP `504` error.
  * **Blocked outbound domain with controlled egress** : The Looker (Google Cloud core) instance can't reach an external domain through controlled egress. Unlike missing route errors, a `504` error during outbound requests typically means that the network path exists, but a required domain is missing from the **Global FQDN** allowlist and is being blocked, or the request is timing out at the gateway.



### Resolution

Depending on the cause of the error, complete the steps in the following sections to resolve the issue.

#### Resolve load balancer timeouts on API calls or queries

To resolve `504` errors that are caused by the load balancer backend service timeout, use one or both of the following methods:

  * **Increase the load balancer backend service timeout** :

    1. In the Google Cloud console, go to the **Load balancing** page:

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/loadBalancers/list)

    2. Click **Backends** , and then click the name of the backend service that's associated with your Looker (Google Cloud core) instance.

    3. Click **Edit**.

    4. In the **Timeout** field, increase the timeout value, such as from 30 seconds to 300 seconds, to accommodate your longest-running queries and API requests.

    5. Click **Save**.

  * **Use an asynchronous API workflow** : If you're calling the Looker API to fetch query data and can't modify the load balancer timeout, use asynchronous endpoints instead of synchronous requests. Call [`create_query_task`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/create_query_task) to start the query asynchronously, and then poll [`query_task_results`](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Query/query_task_results) to retrieve the results after the query finishes.




#### Resolve controlled egress timeouts

To resolve `504` errors that occur when Looker (Google Cloud core) fails to connect to an external service or identity provider with controlled egress enabled, follow these steps:

  1. **Verify required FQDNs** : In the Google Cloud console, verify that all domains that are required by your external service or identity provider are added to the **Global FQDN** list. OIDC authentication flows often require multiple endpoints (such as authorization, token, and user information endpoints) that might use different domains.
  2. **Capture a network trace** : If the error persists, capture a browser network trace (HAR file) while reproducing the issue. Search the trace for `504` status codes or failed HTTP requests to identify any domains that were contacted during the flow but aren't included in your **Global FQDN** list.
  3. **Reset configuration** : If the required FQDNs are present but requests continue to time out, follow the steps in the Resolution for OpenID Connect authentication failures to reset the controlled egress configuration.



## HttpClient:ConnectTimeoutError execution expired

When testing an OpenID Connect connection or other external network connections in the Looker Admin panel, the connection test might fail with a timeout error.

### Symptoms

When you run a connection test in the Looker Admin panel (such as on the **OpenID Connect Authentication** page), Looker returns the following error:
    
    
    HttpClient:ConnectTimeoutError execution expired
    

### Cause

This error indicates that the Looker (Google Cloud core) instance lacks the necessary network path that it needs to communicate with the external service or identity provider. This issue typically occurs when either of the following conditions is met:

  * **Missing route propagation** : Cloud Router is using default settings and isn't propagating VPC network routes (such as custom advertised routes) to the Looker (Google Cloud core) instance.
  * **Missing internet NEG** : An [internet network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) isn't configured in your VPC network to route traffic to the external service.



### Resolution

To resolve this issue, follow these steps:

  1. **Configure Cloud Router route propagation** : Verify that Cloud Router is configured to propagate the necessary VPC network routes to your Looker (Google Cloud core) instance by setting up custom advertised routes.
  2. **Configure an internet NEG** : Set up an internet NEG in your VPC network to allow the Looker (Google Cloud core) instance to route egress traffic to the external identity provider or service.
  3. **Verify private services access** : For instances that use private services access, ensure that your VPC network is properly peered with Google services. For more information, see [Access external services using private services access](https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config).



## Southbound Private Service Connect connection issues

For Looker (Google Cloud core) instances that use Private Service Connect for outbound connections to database backends or published services, you might encounter connection errors even when the endpoint status is `Accepted`.

Common issues include the following:

  * **Hostname resolution errors** : If Looker (Google Cloud core) displays an `Unknown host` error when testing a connection, verify that the configured hostname matches the DNS record in your private network and that the backend load balancer is healthy.
  * **Connection timeouts** : If connections time out, check your VPC firewall rules to verify that ingress traffic is allowed from the Private Service Connect NAT subnet to your load balancer's backends.
  * **Pending or Closed status** : If the service attachment status is `Pending` or `Closed`, check that the consumer project is in the service attachment's allowlist and that mandatory TCP health checks are configured.
  * **Update failures with internal error 13** : When you update outbound service attachments by using Terraform or the API, the update might fail with an `Internal error 13` if your inbound configuration is in an error state. For more information, see Internal error 13 when updating outbound service attachments.



For detailed diagnostic workflows and a decision tree, see [Troubleshooting southbound Private Service Connect connections](https://docs.cloud.google.com/looker/docs/best-practices/flows/looker-core-psc-southbound-troubleshooting).

### Internal error 13 when updating outbound service attachments

When you use Terraform or the Looker (Google Cloud core) API to add, update, or remove Private Service Connect outbound (egress) service attachments on an existing Looker (Google Cloud core) instance, the update might fail with an internal error.

#### Symptoms

You might observe the following symptoms:

  * Terraform or the API update fails with an error similar to the following:
        
        Error: Error waiting for Updating Instance: Error code 13, message: an internal error has occurred
        

  * The Looker (Google Cloud core) instance fails to establish connections to the target services, even if the service attachment in the producer VPC network displays an `Accepted` connection status.




#### Cause

This error occurs when the instance's Private Service Connect inbound configuration (`allowed_vpcs`) enters an error state in the backend.

When you use Terraform or an API client to update outbound service attachments (`psc_service_attachments`), the request payload typically includes the entire `psc_config` block, which contains the `allowed_vpcs` parameter. The Looker (Google Cloud core) API attempts to validate the inbound configuration during the update. Because `allowed_vpcs` is in an error state, the validation fails, causing the entire instance update to fail with error code 13 and preventing outbound service attachment changes from being applied.

#### Resolution

To bypass the inbound configuration validation error and apply your outbound service attachment updates, complete the following workaround:

  1. In your Terraform configuration or API payload, temporarily comment out or remove the `allowed_vpcs` parameter from the `psc_config` block.
  2. Apply the Terraform configuration or resubmit the API request to update your outbound service attachments (`psc_service_attachments`).

Because the request payload omits `allowed_vpcs`, the API skips validation for the inbound configuration and applies the outbound service attachment changes.

  3. After the outbound service attachments are deployed and connections are established, restore the `allowed_vpcs` parameter in your Terraform configuration or API payload.

  4. Re-apply the Terraform configuration.




## Private services access route and connectivity issues

For Looker (Google Cloud core) instances that use private services access, outbound communication to external services requires proper route propagation and network infrastructure:

  * **Route propagation** : Verify that Cloud Router is configured to propagate VPC network routes to the Looker (Google Cloud core) instance, such as custom advertised routes.
  * **Internet network endpoint groups** : If your instance needs to reach external endpoints over private services access, ensure that an [internet network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) is configured in your VPC network.



If these routes or endpoint groups are missing, connection tests to external endpoints fail with an `HttpClient:ConnectTimeoutError execution expired` error.

For more information, see [Access external services using private services access](https://docs.cloud.google.com/looker/docs/looker-core-private-ip-config).

## Diagnostic tools and logs

Use the following tools and logs to help diagnose networking issues:

  * **Cloud Logging** : View instance-level logs in Cloud Logging to identify connection failures and system events. For more information, see [View instance logs](https://docs.cloud.google.com/looker/docs/looker-core-logging).
  * **Looker System Activity** : If you can sign in as an administrator, review the **User Activity** dashboard in System Activity. This dashboard displays recent login failures, the authentication method that was used, and error messages. For more information, see [User Activity dashboard](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#user_activity_dashboard).
  * **VPC Flow Logs** : Check [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) to determine whether network traffic from Looker (Google Cloud core) reaches your destination subnet or is blocked by firewall rules.
  * **Cloud Customer Care** : If you completed the troubleshooting steps and the issue persists, contact [Cloud Customer Care](https://docs.cloud.google.com/looker/docs/looker-core-support) for assistance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
