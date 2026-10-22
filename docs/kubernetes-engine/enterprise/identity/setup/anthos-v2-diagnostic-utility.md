---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/anthos-v2-diagnostic-utility/
title: Troubleshoot third-party authentication with a diagnostic utility \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:55.220053+00:00
---

# Troubleshoot third-party authentication with a diagnostic utility  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/anthos-v2-diagnostic-utility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Troubleshoot third-party authentication with a diagnostic utility Stay organized with collections  Save and categorize content based on your preferences. 

You can use a diagnostic utility to troubleshoot [FQDN-based authentication](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/authenticate-fqdn-access) issues in fleet member clusters. If you're experiencing difficulties authenticating to a cluster using a specific OIDC provider, you can enable the tool and use it to quickly identify configuration issues by simulating sign-in flows with your OIDC provider. This document applies only to [supported cluster types](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity#supported_cluster_types).

The diagnostic utility is only available on individual clusters running version 1.32 or higher and only supports OIDC.

## Enable the diagnostic utility

The diagnostic utility is disabled by default and must be enabled before you can use it to troubleshoot. To enable it, use these instructions:

  1. Open the ClientConfig custom resource for editing:
         
         kubectl edit clientconfig default \
             --kubeconfig CLUSTER_KUBECONFIG -n kube-public
         

The manifest should look similar to the following:
         
         apiVersion: authentication.gke.io/v2alpha1
         kind: ClientConfig
         metadata:
           name: default
           namespace: kube-public
         spec:
           authentication:
           - name: oidc
             oidc:
               clientID: example-client-id
               clientSecret: example-client-secret
               cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
               extraParams: prompt=consent, access_type=offline
               issuerURI: https://example.com
               kubectlRedirectURI: http://localhost:PORT/callback
               scopes: openid,email,offline_access
               userClaim: email
         

  2. As shown in the following example, add an `identityServiceOptions` section to the ClientConfig manifest to specify the diagnostic utility configuration:
         
         apiVersion: authentication.gke.io/v2alpha1
           kind: ClientConfig
           metadata:
             name: default
             namespace: kube-public
           spec:
             **identityServiceOptions :**
               **diagnosticInterface :**
                 **enabled : true**
                 **expirationTime : TIMESTAMP**
             authentication:
             - name: oidc
               oidc:
                 clientID: example-client-id
                 clientSecret: example-client-secret
                 cloudConsoleRedirectURI: https://console.cloud.google.com/kubernetes/oidc
                 extraParams: prompt=consent, access_type=offline
                 issuerURI: https://example.com
                 kubectlRedirectURI: http://localhost:PORT/callback
                 scopes: openid,email,offline_access
                 userClaim: email
         

Replace `TIMESTAMP` with an expiration time in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. For example, `2025-05-01T17:05:00Z`. The expiration time determines when the diagnostic utility feature automatically turns off. Since the diagnostic utility is available to anyone with cluster access, setting the expiration time appropriately helps ensure that the utility doesn't remain enabled longer than necessary. When setting the expiration time, it's recommended to set it to 12 hours in the future, although any time in the future is valid.

  3. Save your changes and exit the text editor to apply the manifest to the cluster.




## Use the diagnostic utility to simulate a sign-in

Once the diagnostic utility is enabled, you can simulate a sign-in event and get the corresponding diagnostic information that you can use to troubleshoot issues with a specific provider.

  1. Open the diagnostic page in a browser by navigating to the following URL:
         
         APISERVER-URL/diagnose
         

Replace `APISERVER_URL` with the fully qualified domain name (FQDN) for your cluster. For example, `https://apiserver.example.com`.

If you encounter a forbidden error, like the following:
         
         forbidden: user \"system:anonymous\" cannot get path \"/diagnose\"
         

Append the port number value of **`:11001`** to the `APISERVER_URL`. For example, `https://apiserver.example.com:11001/diagnose`.

The diagnostic page displays a list of OIDC providers configured for your cluster.

  2. Select the provider that you want to troubleshoot.

  3. Sign in as usual.

At the end of the sign in process, the utility displays a page with diagnostic information that can help you troubleshoot.




## Use the diagnostics page to troubleshoot sign-in problems

The diagnostics page provides an authentication summary, which is divided into three sections:

  * **Status** : contains either `Success` or `Failed`, depending on whether the authentication has succeeded or not.

  * **Identity Provider** : contains details, such as `Name`, `Client ID`, and `UserClaim`, about the provider that was used to sign in.

  * **ID Token** : contains information about ID token fetched by the cluster using the given provider. The ID token is a JSON object containing a set of key-value pairs. Keys might include `iss`, `aud`, `sub`, and `email`.




### Troubleshoot authentication success

If the content of the **Status** section indicates that the authentication has succeeded and you're still experiencing issues, missing role-based-access-controls (RBACs) might be the cause. For additional troubleshooting information, see [RBACs for groups not working for OIDC providers](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting#rbacs_for_groups_not_working_for_oidc_providers) for further troubleshooting.

### Troubleshoot authentication failure

If the content of the **Status** section indicates that the authentication has failed, start by looking for inconsistencies between the **Identity Provider** and **ID Token** sections.

Here are a few authentication requirements that you should check:

  * If the `UserClaim` field in **Identity Provider** is empty, then the **ID Token** section must contain a field named `sub`. A missing `sub` field is an indication that there's a problem with the ID token.

  * The `UserClaim` field value in **Identity Provider** must be a key in the **ID Token** section. For example, if the `UserClaim` field is set to `email`, then there must be a field named `email` in **ID Token**.

  * The `GroupsClaim` field value in **Identity Provider** must be a key in **ID Token**. For example, if the `GroupsClaim` field is set to `groupsList` (for a provider that supports groups), then there must be a field named `groupsList` in **ID Token**.

  * The `Client ID` field value in **Identity Provider** must be contained within the value of the `aud` field in **ID Token** section.




If any of the preceding conditions aren't met, see one of the following guides for more details on how to properly configure your clusters for authentication:

  * If you set up authentication for individual clusters, see the [instructions to configure individual clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/per-cluster#configure_clusters).

  * If you set up authentication at a fleet level, see the [instructions to configure a fleet of clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#configure_clusters).




### Use logs for further troubleshooting

The [identity service Pod logs](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/ais-pod-troubleshooting) contain additional debugging information. To use these logs:

  1. [Enable the debug log](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting#enable_the_debug_log).
  2. [Check the container log](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting#check_the_container_log).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
