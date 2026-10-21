---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-instance-not-reporting-status/
title: Instance is not reporting status for environment group \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:22.770227+00:00
---

# Instance is not reporting status for environment group  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/deployment/apigee-instance-not-reporting-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Instance is not reporting status for environment group Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/support-d) documentation._

**Note:** This document is applicable for Apigee hybrid users only. 

## Symptoms

Deployments of API proxies fail with `Instance INSTANCE_NAME is not reporting status for environment group ENV_GROUP_NAME` error in the Apigee hybrid UI. 

## Error Messages

`The Instance INSTANCE_NAME is not reporting status for environment group ENV_GROUP_NAME` error is displayed in the **API proxies** menu under the **Overview** tab when hovering over the red exclamation mark appearing in the **Status** column of **Deployments** section: 

![instance-not-reporting-status](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/instance-not-reporting-status.png)

## Possible Causes

Cause | Description  
---|---  
The selector `app: apigee-ingressgateway` is missing | When using the Apigee ingress, the `overrides.yaml` file needs to have the selector `app: apigee-ingressgateway` under `virtualhosts` section  
  
### Cause: The selector `app: apigee-ingressgateway` is missing

When using the Apigee ingress gateway, the `overrides.yaml` file includes a section for `virtualhosts` configuration in which the selector `app: apigee-ingressgateway` needs to be configured. 

#### Diagnosis

First, confirm that you are using the Apigee ingress gateway which is available with Hybrid version 1.8 and later (the following configuration does not work for customer-managed Istio ASM). In your `overrides.yaml` file which includes the environment group mentioned in the error, find the `virtualhosts` section and check if the following selectors are missing: 
    
    
      selector:
        app: apigee-ingressgateway
        ingress_name: INGRESS_NAME

#### Resolution

Edit the `overrides.yaml` file so that the `virtualhosts[].selector` section looks similar to the following example: 
    
    
        virtualhosts:
        - name: my-environment-group
          sslCertPath: my-cert.crt
          sslKeyPath: my-cert.key
          **selector:**
            **app: apigee-ingressgateway**
            **ingress_name: INGRESS_NAME**
      

After editing the `overrides.yaml` file apply the new configuration using [Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/helm-reference):

Dry run:
    
    
    helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
    --namespace APIGEE_NAMESPACE \
    --atomic \
    --set envgroup=ENV_GROUP \
    -f OVERRIDES_FILE \
    --dry-run=server

Make sure to include all of the settings shown, including `--atomic` so that the action rolls back on failure.

Your installation may or may not have been set up using an ENV_GROUP_RELEASE_NAME that differs from ENV_GROUP. For information on the settings, see [Install Apigee hybrid using Helm](https://docs.cloud.google.com/apigee/docs/hybrid/latest/install-helm-charts).

Install the chart:
    
    
    helm upgrade ENV_GROUP_RELEASE_NAME apigee-virtualhost/ \
    --namespace APIGEE_NAMESPACE \
    --atomic \
    --set envgroup=ENV_GROUP \
    -f OVERRIDES_FILE
    

## References

  * [ Mapping virtual hosts to Apigee ingress gateway deployments](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/managing-ingress#targetvh)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
