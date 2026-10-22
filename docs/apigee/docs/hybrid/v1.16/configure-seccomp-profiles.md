---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles/
title: Configure Seccomp profiles for pod security \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:53.171907+00:00
---

# Configure Seccomp profiles for pod security  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configure Seccomp profiles for pod security Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configure-seccomp-profiles.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configure-seccomp-profiles.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/configure-seccomp-profiles.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configure-seccomp-profiles.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/configure-seccomp-profiles.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/configure-seccomp-profiles.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/configure-seccomp-profiles.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configure-seccomp-profiles.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/configure-seccomp-profiles.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/configure-seccomp-profiles.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/configure-seccomp-profiles.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/configure-seccomp-profiles.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/configure-seccomp-profiles.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/configure-seccomp-profiles.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/configure-seccomp-profiles.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/configure-seccomp-profiles.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/configure-seccomp-profiles.html)



This document describes how to configure Kubernetes Seccomp (Secure Computing Mode) profiles for Apigee hybrid pods to enhance security by restricting the system calls (syscalls) that containers are allowed to make.

## About Seccomp profiles in Kubernetes

Seccomp is a Linux kernel security feature that limits the system calls a process can make. When used with Kubernetes, you can apply Seccomp profiles to a pod's `securityContext` to restrict the syscalls available to its containers. This helps reduce the attack surface of the container and mitigates the risk of container breakouts or privilege escalation by enforcing the principle of least privilege.

For more information on Seccomp in Kubernetes, see [Secure Computing (Seccomp)](https://kubernetes.io/docs/tutorials/security/seccomp/) in the Kubernetes documentation.

In hybrid, Seccomp profiles are **not enabled by default**. You can choose to apply a Seccomp profile to hybrid components by adding the `seccompProfile` object to your `overrides.yaml` file.

## Configuring Seccomp profiles

You can apply Seccomp profiles globally, per environment, or per component in your `overrides.yaml` file by adding the `securityContext.seccompProfile` configuration block. hybrid supports the following Seccomp profile types:

  * **`RuntimeDefault`:** The default profile specified by the container runtime. This is the recommended option, as it provides a reasonable level of security while maintaining compatibility for most workloads.
  * **`Unconfined`:** Applies no Seccomp restrictions to the pod. This is the least secure option and should be used with caution.

**Note:** The `Localhost` profile type is not supported in this release of hybrid.

### Configuration precedence

You can set the `seccompProfile` at the following levels in `overrides.yaml`. Component-level settings take precedence over environment-level settings, and environment-level settings take precedence over global settings:

  1. **Component level:** Applies to a specific component (for example, `runtime` or `cassandra`).
  2. **Environment level:** Applies to all components within a specific environment defined in the `envs[]` array, unless overridden at the component level.
  3. **Global level:** Applies to all components in the cluster, unless overridden at the environment or component level.



### Examples

#### Global configuration

To apply the `RuntimeDefault` Seccomp profile to all components that do not have an environment- or component-level override, add the following to the top level of your `overrides.yaml`:
    
    
    securityContext:
      seccompProfile:
        type: RuntimeDefault

#### Environment configuration

To apply the `RuntimeDefault` Seccomp profile to all components in a specific environment, add the configuration under the `envs[]` element:
    
    
    envs:
      - name: "my-environment"
        securityContext:
          seccompProfile:
            type: RuntimeDefault
        ...

#### Component configuration

To apply the `RuntimeDefault` Seccomp profile to a specific component (for example, the runtime component), add the configuration under that component:
    
    
    runtime:
      securityContext:
        seccompProfile:
          type: RuntimeDefault
    ...

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
