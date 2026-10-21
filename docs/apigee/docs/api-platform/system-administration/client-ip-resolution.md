---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution/
title: Client IP resolution \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:57.585619+00:00
---

# Client IP resolution  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/client-ip-resolution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Client IP resolution Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Accurately identifying the client IP address on API requests is important for some functionality within Apigee, including [Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview) and [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security) features such as abuse detection and security actions.

The client IP identification process is challenging in modern network architectures that employ proxies and load balancers, as these intermediaries can obscure the true originating IP address.

To overcome this challenge, Apigee supports an environment-level setting specifying how to resolve the client IP address from a specified header. This can be any header, such as `X-Forwarded-For` or `True-Client-Ip`. The setting identifies the index in the header that matches the IP address for your network topology and security requirements. Using this setting provides visibility, consistency, and control over how client IP addresses are determined for all requests in the environment and results in consistent client IP address identification across Advanced API Security, flow variables, and analytics variables in the environment.

If the environment-level client IP resolution is not configured, or if the configured header does not exist or does not contain an IP address at the specified index, the client IP address variables are populated using the default client IP address resolution behavior.

## Default client IP address resolution

If client IP resolution is not configured at the environment level, the default value of the `ax_resolved_client_ip` dimension is calculated as described in [Analytics dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions).

If client IP resolution _is_ configured for an environment, the flow and Analytics variables are set from the client IP resolution configuration. See Set the client IP resolution for an environment.

## When to set the client IP resolution for an environment

Although it's not required to set client IP resolution, you might want to if the default client IP address resolution does not meet your needs and you want to override it to provide a specified client IP address resolution for Analytics, Advanced API Security, or performing any other function that requires consistent and reliable information on client IP addresses.

## Understand the client IP resolution configuration syntax

The client IP resolution setting has this format:
    
    
    "clientIpResolutionConfig": {
      "headerIndexAlgorithm": {
         "ipHeaderName" : "X-Forwarded-For",
         "ipHeaderIndex": 2
      }
    }

The following example uses the `True-Client-Ip` header:
    
    
    "clientIpResolutionConfig": {
      "headerIndexAlgorithm": {
         "ipHeaderName" : "True-Client-Ip",
         "ipHeaderIndex": 0
      }
    }

where 

  * `ipHeaderName` is the header to use for the client IP. For example, `X-Forwarded-For` or `True-Client-Ip`.
  * `ipHeaderIndex` is the index value within the `ipHeaderName`.  
  
A positive number selects an address starting from the left (the first address added to the header), where the first position on the left is `0` and increases by one for each subsequent address (e.g. `0, 1, 2`). For example, if the list is `192.0.2.1, 192.0.2.2, 192.0.2.3`, an index of `1` resolves to `192.0.2.2`.  
  
A negative number selects an address starting from the right (the last address added to the header) where the first position on the right is `-1` and decrements by one for each subsequent address (e.g. `-3, -2, -1`). For example, if the list is `192.0.2.1, 192.0.2.2, 192.0.2.3, 192.0.2.4`, an index of `-1` resolves to `192.0.2.4` and the index `-2` resolves to `192.0.2.3`.



See the [organizations.environment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments#Environment) for additional information about this setting. 

## View client IP resolution configurations

You can view the current client IP resolution configuration for an environment using either the Apigee UI or Management APIs.

### View the client IP resolution configuration using the UI

To view the client IP resolution configuration:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the environment, and see **Client IP configuration** in the **About** tab.

![Client IP resolution in the Apigee UI](https://docs.cloud.google.com/static/apigee/docs/api-platform/system-administration/images/client-ip-resolution-view-ui.png)



### View the client IP resolution configuration using the API

To use the Apigee Management APIs to view the client IP resolution configuration, send a request to the [organizations.environments.get API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/get).

## Set client IP resolution for an environment

After setting the client IP resolution configuration for an environment, the [`client.resolved.ip`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#client) flow variable populates using the specified algorithm. So does the [`Resolved Client IP` Analytics dimension](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions).

Once you've set the client IP resolution configuration for an environment, the changes might impact existing Advanced API Security configurations for security action rules. Review and, if necessary, regenerate existing rules to use the new variables and settings.

Keep these implications in mind when selecting the index for Client IP resolution:

  * Apigee to Apigee calls are not handled as a special case. Take care to note and skip the number of IPs accordingly.
  * Since the X-Forwarded-For header can be spoofed, it's better to use the right index based on the number of expected hops between the client and the Apigee load balancer. A malicious user can send a pre-filled X-Forwarded-For header. While the first IP in the XFF is closest to the actual client IP, the last IP in the XFF is most trustworthy, given the load balancer knows the TCP client which is connected to it.



To set client IP resolution on an environment, use one of the Apigee API Management APIs to set the client IP resolution for the environment in the `client_ip_resolution_config`. Use [organizations.environments.create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create) for new environments. Use [updateEnvironment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/updateEnvironment) or [modifyEnvironment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/modifyEnvironment) for existing environments.

## Test the client IP address resolution

After saving a new client IP configuration, you can test it by following these instructions:

  1. Wait at least 5 minutes after saving a new configuration setting.
  2. Start a [debug session](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace). Enable the setting to **Show all FlowInfos**.
  3. Check the **FlowInfo** just before **Proxy Request Flow Started**. You should see the configured client IP address captured in that section.



Look for these variables in the FlowInfo:

  * `client_ip_resolution.resolved.ip`: The resolved client IP address.
  * `client_ip_resolution.used.fallback`: Boolean. This value is `false` unless Apigee fell back to the default client IP resolution due to an inability to use a configured client IP resolution. For example, if the configured resolution specifies an index which doesn't exist in the header.
  * `client_ip_resolution.algorithm`: The algorithm used to determine the client IP address. If configured, this is `"HeaderIndexAlgorithm{IpHeaderName:header_name, IpHeaderIndex: $header_index}"`. Otherwise, this shows `default`.



## Limitations

These limitations apply to environment-level client IP resolution:

  * Updates to client IP resolution configurations can take up to 5 minutes to be effective.
  * Avoid frequent (for example, every 5 minutes) changes to the client IP resolution configuration, as this could cause performance degradation.
  * Setting the client IP resolution configuration for an environment in Apigee hybrid is available with hybrid versions 1.14.0 and later.
  * The configuration can be viewed via the Apigee Console or API but can be set only via the API.
  * Even in the absence of malicious users, the X-Forwarded-For list relies on each proxy to add the right information to the list. That complete list is outside Apigee's oversight and control, so setting the client IP resolution configuration does not guarantee identification of the correct request IP address.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
