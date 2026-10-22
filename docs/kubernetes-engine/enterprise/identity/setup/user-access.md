---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access/
title: Set up an authentication method for user access \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:42.539579+00:00
---

# Set up an authentication method for user access  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Set up an authentication method for user access Stay organized with collections  Save and categorize content based on your preferences. 

This document is for **cluster administrators** who have already configured their fleet member clusters for third-party identity providers. It provides instructions on how to set up and manage user access to these configured clusters for your organization's developers and other users.

There are two types of authentication methods you can use to set up user access to your clusters:

  * Set up with FQDN access (Recommended): With this approach, users can directly authenticate to the cluster using the fully qualified domain name (FQDN) of the cluster's Kubernetes API server. For more information, see Set up FQDN access.
  * Set up with file-based access: With this approach, you generate a login configuration file and distribute it to cluster users. Users can then sign in to configured clusters with `gcloud` authentication commands using this file. For more information, see Set up file-based access.



## Set up FQDN access (Recommended)

**Note:** If you experience any issues with this setup and your cluster is running version 1.31 or higher, consider using the [diagnostic utility](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/anthos-v2-diagnostic-utility) to assist with troubleshooting.

This section tells you how to set up user login access by providing the user with the URL (FQDN) for a server to use for authentication. The authentication flow lets the user sign in with their IdP and provides the user with a token that is added to their kubeconfig file for accessing the cluster. This authentication approach is supported only for on-premises clusters (Google Distributed Cloud) on VMware and bare metal, from version 1.29 onwards. Other cluster types are not supported. If you need to set up authentication for on-premises clusters using an older supported software version, or for other cluster types, follow the instructions to set up file-based access.

Before sharing the FQDN to users, ensure that you or your platform administrator have followed the appropriate [setup](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/idp-overview#beforeyoubegin), including DNS setup for the FQDN and providing the FQDN as part of registering to your identity provider if required.

### Share FQDN with users

Instead of a configuration file, _cluster administrators_ can share the FQDN of the cluster's Kubernetes API server, such as `https://apiserver.example.com`, with users. Users can use this FQDN to sign in to the cluster.

### Configure Identity Service options

With this set up option, you can configure the token lifetime duration. The `identityServiceOptions` in the ClientConfig CR has a `sessionDuration` parameter that lets you configure the token lifetime (in minutes). The `sessionDuration` parameter has a lower limit of 15 minutes and a maximum limit of 1440 minutes (24 hours).

Here's an example of what it looks like in the ClientConfig CR:
    
    
    spec:
        identityServiceOptions:
          sessionDuration: INT
    

where INT is the session duration in minutes.

## Set up file-based access

As an alternative to FQDN access, cluster administrators can generate a login configuration file and distribute it to cluster users. You may want to use this option if you are setting up authentication to a cluster with a version or type that does not support FQDN access. This file lets users access clusters from the command line with the chosen provider. This authentication approach is supported for OIDC and LDAP providers only.

### Generate the login config

### Console

([Fleet-level setup](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet) only)

Copy the displayed `gcloud` command and run it to generate the file.

### gcloud

If you configured the cluster using `gcloud` CLI or if you need to generate the file again, run the following command to generate the file:
    
    
    gcloud anthos create-login-config --kubeconfig=KUBECONFIG

where `KUBECONFIG` is the path to the kubeconfig file for the cluster. If there are multiple contexts in the kubeconfig, the current context is used. You may need to reset the current context to the correct cluster before running the command.

You can see complete reference details for this command, including additional optional parameters, in the [Google Cloud CLI reference guide](https://docs.cloud.google.com/sdk/gcloud/reference/anthos/create-login-config).

The default name for the login config file is `kubectl-anthos-config.yaml`, which is the name the Google Cloud CLI expects when using the file to sign in. If you want to change this to a non-default name, see the relevant section in [Distribute the login config](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/fleet-cluster#distribute_the_login_config).

For troubleshooting information related to user access, see [Troubleshoot user access issues](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/setup/user-access-troubleshooting).

## Distribute the login config

The following are some ways to distribute the config file:

  * Host the file at an accessible URL. Users can specify this location with the `--login-config` flag when running `gcloud anthos auth login`, allowing the Google Cloud CLI to get the file.

Consider hosting the file on a secure host. See the [`--login-config-cert`](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing#plugin_to_authenticate) flag of the gcloud CLI for more information about using PEM certificates for secure HTTPS access.

  * Manually provide the file to each user, with information on where to save it on their local machine—the Google Cloud CLI expects to find the file in an OS-specific default location. If the file has a non-default name or location, your users must use the `--login-config` flag to specify the config file location when running commands against the cluster. Instructions for users to save the file are in [Choose an access method to log in to clusters](https://docs.cloud.google.com/kubernetes-engine/enterprise/identity/accessing).

  * Use your internal tools to push the authentication configuration file onto each user's machine. The Google Cloud CLI expects to find the file in the following locations, depending on the user OS:

### Linux
        
        $HOME/.config/google/anthos/kubectl-anthos-config.yaml

### macOS
        
        $HOME/Library/Preferences/google/anthos/kubectl-anthos-config.yaml

### Windows
        
        %APPDATA%\google\anthos\kubectl-anthos-config.yaml




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
