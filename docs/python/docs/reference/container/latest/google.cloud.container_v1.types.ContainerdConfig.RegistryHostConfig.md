---
url: https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1.types.ContainerdConfig.RegistryHostConfig
title: Class RegistryHostConfig (2.67.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:27.057654+00:00
---

# Class RegistryHostConfig (2.67.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1.types.ContainerdConfig.RegistryHostConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RegistryHostConfig (2.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.67.0 (latest)  2.66.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.1  2.55.1  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.4  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.2  2.10.8  2.9.0  2.8.1  2.7.1  2.6.1  2.5.0  2.4.1  2.3.1  2.2.0  2.1.0  2.0.1  1.0.3  0.5.0  0.4.0  0.3.0 
    
    
    RegistryHostConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

RegistryHostConfig configures the top-level structure for a single containerd registry server's configuration, which represents one hosts.toml file on the node. It will override the same fqdns in PrivateRegistryAccessConfig.

## Attributes  
  
---  
**Name** | **Description**  
`server` |  `str`   
Defines the host name of the registry server, which will be used to create configuration file as /etc/containerd/hosts.d//hosts.toml. It supports fully qualified domain names (FQDN) and IP addresses: Specifying port is supported, while scheme and path are NOT supported. Wildcards are NOT supported. Examples: \- `my.customdomain.com` \- `10.0.1.2:5000`  
`hosts` |  `MutableSequence[[google.cloud.container_v1.types.ContainerdConfig.RegistryHostConfig.HostConfig](https://docs.cloud.google.com/python/docs/reference/container/latest/google.cloud.container_v1.types.ContainerdConfig.RegistryHostConfig.HostConfig)]`   
HostConfig configures a list of host-specific configurations for the server. Each server can have at most 10 host configurations.   
  
## Classes 

### CertificateConfig
    
    
    CertificateConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

CertificateConfig configures certificate for the registry.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### CertificateConfigPair
    
    
    CertificateConfigPair(mapping=None, *, ignore_unknown_fields=False, **kwargs)

CertificateConfigPair configures pairs of certificates, which is used for client certificate and key pairs under a registry.

### HostCapability
    
    
    HostCapability(value)

HostCapability configures capabilities for the registry host.

### HostConfig
    
    
    HostConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

HostConfig configures the registry host under a given Server.

### RegistryHeader
    
    
    RegistryHeader(mapping=None, *, ignore_unknown_fields=False, **kwargs)

RegistryHeader configures headers for the registry.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
