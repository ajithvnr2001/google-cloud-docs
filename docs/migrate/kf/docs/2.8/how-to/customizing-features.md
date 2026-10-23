---
url: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/customizing-features/
title: Customizing Kf Features \u00a0|\u00a0 Kf 2.8 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:46.094787+00:00
---

# Customizing Kf Features  |  Kf 2.8  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/customizing-features/

Version 2.8

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.8 ](https://docs.cloud.google.com/migrate/kf/docs/2.8)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.8/getting-started)



Send feedback 

#  Customizing Kf Features Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** Please proceed with caution, and test before using any customizations in production.

## Build Retention

You can control how many Kf Builds are kept before being garbage collected.

**Note:** This example sets the retention to 1 Build. Change the value as needed.
    
    
    kubectl patch \
    kfsystem kfsystem \
    --type='json' \
    -p="[{'op': 'replace', 'path': '/spec/kf/config/buildRetentionCount', 'value': 1}]"
    

## Enable or Disable the Istio Sidecar

If you do not require the Istio sidecar for the Build pods, then they can be disabled by setting the value to `true`. Enable by setting the value to `false`.
    
    
    kubectl patch \
    kfsystem kfsystem \
    --type='json' \
    -p="[{'op': 'replace', 'path': '/spec/kf/config/buildDisableIstioSidecar', 'value': true}]"
    

## Build Pod Resource Limits

The default pod resource size can be increased from the default to accommodate very large builds. The units for the value are in `Mi` or `Gi`.

**Note:** This is only applicable for built-in Tasks (which is normal for a `kf push` build). For V2 buildpack builds, this will be set on two steps and one for V3 buildpacks or Dockerfiles. This means that for a V2 build the required Pod size will be double the limit. For example, if the memory limit is 1Gi, then the pod will require 2Gi.
    
    
    kubectl patch \
    kfsystem kfsystem \
    --type='json' \
    -p="[{'op': 'replace', 'path': '/spec/kf/config/buildPodResources', 'value': {'limits': {'memory': '234Mi'}}}]"
    

Read [Kubernetes container resource docs](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for more information about container resource management.

## Self Signed Certificates for Service Brokers

If you want to use self signed certificates for TLS (`https` instead of `http`) for the service broker URL, the Kf controller requires the CA certificate. To configure Kf for this scenario, create an immutable Kubernetes secret in the `kf` namespace and update the `kfsystem.spec.kf.config.secrets.controllerCACerts.name` object to point to it.

  1. Create a secret to store the self-signed certificate.

**Note:** Customize the secret name if desired, or leave the default name of `cacerts`. Replace `/path/to/cert/certs.pem` with the path to the self-signed certificate.
         
         kubectl create secret generic cacerts -nkf --from-file /path/to/cert/certs.pem
         

  2. Make the secret immutable.
         
         kubectl patch -nkf secret cacerts \
           --type='json' \
           -p="[{'op':'add','path':'/immutable','value':true}]"
         

  3. Update kfsystem to point to the secret.

**Note:** This will cause the controller pod to be re-deployed with the certs mounted as a volume.
         
         kubectl patch \
           kfsystem kfsystem \
           --type='json' \
           -p="[{'op':'add','path':'/spec/kf/config/secrets','value':{'controllerCACerts':{'name':'cacerts'}}}]"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
