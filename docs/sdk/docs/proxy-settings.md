---
url: https://docs.cloud.google.com/sdk/docs/proxy-settings/
title: Configuring the gcloud CLI for use behind a proxy/firewall \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:54.145236+00:00
---

# Configuring the gcloud CLI for use behind a proxy/firewall  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/docs/proxy-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Configuring the gcloud CLI for use behind a proxy/firewall Stay organized with collections  Save and categorize content based on your preferences. 

If you are behind a corporate proxy or firewall, the Google Cloud CLI might not be able to access the internet with its default settings.

## Installing the gcloud CLI

The interactive gcloud CLI installers download components from the internet as part of the installation process, which might not work correctly if you're behind a proxy or firewall.

For a simpler installation process when proxy configuration is necessary, use one of the self-contained [versioned archives](https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives) to install the gcloud CLI. All previous versions of the gcloud CLI are also available to download from the [downloads archive](https://console.cloud.google.com/storage/browser/cloud-sdk-release).

## Proxy configuration

**Note:** The gcloud CLI respects the `http_proxy`, `https_proxy`, and `no_proxy` environment variables set in your proxy configuration; these control the proxy server used for plain HTTP connections, the proxy server used for HTTPS connections (typically more relevant for most gcloud CLI commands), and the domains not to proxy, respectively. Configure your `gcloud` proxy settings only if you would like to use a different proxy. If `gcloud` proxy settings are set, they override existing proxy configuration; this includes ignoring `no_proxy`.**Tip:** If you see warnings or errors related to the `https_proxy` environment variable, it may be because you have specified e.g. `https_proxy=https://...` instead of `https_proxy=http://...`. The latter is needed since the gcloud CLI only supports HTTP proxies. Earlier versions of the gcloud CLI silently ignored this difference and would always attempt to contact the proxy via HTTP even if the proxy URL specified HTTPS.

After you have the gcloud CLI installed, proxy settings can be configured using gcloud CLI properties by running `gcloud config`. For more information on what gcloud CLI properties are and how to use them, refer to the [properties](https://docs.cloud.google.com/sdk/docs/properties) page.

To start, set the type of proxy you are using and the address and port on which to reach it:
    
    
    gcloud config set proxy/type [PROXY_TYPE]
    
    gcloud config set proxy/address [PROXY_IP_ADDRESS]
    
    gcloud config set proxy/port [PROXY_PORT]
    

  * The gcloud CLI supports the following values for `PROXY_TYPE`: `http`, `http_no_tunnel`, `socks4`, `socks5`
  * `PROXY_IP_ADDRESS` is the hostname or IP address of where the proxy can be reached.
  * `PROXY_PORT` is the port the proxy is running on (e.g. `8080`).



For an authenticated proxy, you will need to set your proxy username and password using [properties](https://docs.cloud.google.com/sdk/docs/properties) as follows:
    
    
    gcloud config set proxy/username [USERNAME]
    
    gcloud config set proxy/password [PASSWORD]
    

Alternatively, to avoid having the proxy credentials recorded in any logs (such as shell history or gcloud CLI logs) or in the gcloud CLI configuration file, you can set the properties using environment variables, as shown in the following sample:
    
    
    export CLOUDSDK_PROXY_USERNAME [USERNAME]
    
    export CLOUDSDK_PROXY_PASSWORD [PASSWORD]
    

The gcloud CLI won't store these values. This way, the credentials can be stored in an encrypted file locally, or they can be stored in a secure network location and retrieved when necessary.

If you are behind a proxy and you receive SSL handshake errors, it's likely that your proxy is a man-in-the-middle proxy which uses a custom CA. You need to set the following property to point to your custom CA file:
    
    
    gcloud config set core/custom_ca_certs_file [PATH_TO_CUSTOM_CA]
    

For a full description of related properties, run [`gcloud topic configurations`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) or [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) and look for **proxy** under the Available properties section.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
