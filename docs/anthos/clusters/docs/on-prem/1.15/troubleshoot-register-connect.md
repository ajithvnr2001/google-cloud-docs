---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-register-connect/
title: Troubleshooting registration and connection \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:12.396615+00:00
---

# Troubleshooting registration and connection  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-register-connect/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Troubleshooting registration and connection Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/troubleshoot-register-connect)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/troubleshoot-register-connect)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document gives troubleshooting guidance for issues you might encounter during registration and connection.

## Invalid configuration

If Google Cloud console cannot read the OIDC configuration from your cluster, the **LOGIN** button is disabled.

## Login URL not found

The following issue occurs when the Google Cloud console is not able to reach the identity provider.

An attempt to log in gets redirected to a page with a "URL not found" error.

To resolve this issue:

  1. If the identity provider is not reachable over the public internet, then you need to enable the OIDC HTTP proxy to log in via Google Cloud console. In the `authentication.oidc` section of your cluster configuration file, set `deployCloudConsoleProxy`to `true`. If you have already created a cluster and want to turn on the proxy, you can edit the ClientConfig custom resource directly and set `useHTTPProxy` to `true`:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG edit clientconfig default -n kube-public
         

  2. If the HTTP proxy is enabled and you are still seeing this error, there might have been an issue with the proxy starting up. To get the logs of the proxy:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG logs deployment/clientconfig-operator -n kube-system

Note that even if your identity provider has a well-known CA, for the HTTP proxy to start, you must provide a value for `authentication.oidc.caPath` in your cluster configuration file.

  3. If the authorization server prompts for consent, and you have not included the `extraparam` `prompt=consent`, then you might see this error. Edit the ClientConfig object, and add `prompt=consent` to `extraparams`:
         
         kubectl --kubeconfig USER_CLUSTER_KUBECONFIG edit clientconfig default -n kube-public
         

Then try logging in again.

  4. If you have not done so already, try authenticating using the [Authentication Plugin for Anthos](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/oidc). If you are seeing an authorization error logging in with the plugin as well, then follow the [troubleshooting steps](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/troubleshoot-identity-authorization) to resolve the issue with the plugin. Then try logging in via the Google Cloud console again.

  5. In some cases, if settings are changed on storage service, you might need to log out explicitly. In the Google Cloud console, go to the cluster details page, and click **Log out**. Then try logging in again.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
