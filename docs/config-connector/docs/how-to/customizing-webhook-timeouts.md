---
url: https://docs.cloud.google.com/config-connector/docs/how-to/customizing-webhook-timeouts/
title: Configure webhook timeout \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:16.660741+00:00
---

# Configure webhook timeout  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/how-to/customizing-webhook-timeouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure webhook timeout

This page describes how to configure the webhook timeout for Config Connector. You can configure these webhooks in Config Connector version 1.110 and later.

## Configure timeout for validating webhooks

You can configure the following validating webhooks:

  * `deny-immutable-field-updates.cnrm.cloud.google.com`
  * `deny-unknown-fields.cnrm.cloud.google.com`
  * `iam-validation.cnrm.cloud.google.com`
  * `resource-validation.cnrm.cloud.google.com`
  * `abandon-on-uninstall.cnrm.cloud.google.com`



For example, you can configure the timeout of validating webhooks `deny-immutable-field-updates.cnrm.cloud.google.com` and `deny-unknown-fields.cnrm.cloud.google.com` by creating and applying the following example YAML file. These webhooks are part of the configuration of the `validating-webhook.cnrm.cloud.google.com` [validating webhook configuration](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#webhook-configuration).

  1. Create a file named `configure-validating-webhook-timeout.yaml` and copy the following YAML into it:
         
         apiVersion: customize.core.cnrm.cloud.google.com/v1beta1
         kind: ValidatingWebhookConfigurationCustomization
         metadata:
           name: validating-webhook
         spec:
           webhooks:
           - name: deny-immutable-field-updates
             timeoutSeconds: 12
           - name: deny-unknown-fields
             timeoutSeconds: 15
         

**Note:** when specifying the name of webhook configuration and the names of webhooks in the YAML file, don't include the `.cnrm.cloud.google.com` suffix.
  2. Use [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) to apply the webhook timeout customization to your cluster:
         
         kubectl apply -f configure-validating-webhook-timeout.yaml

  3. Verify the successful configuration by running the following command:
         
         kubectl get validatingwebhookconfigurationcustomizations validating-webhook -o jsonpath='{.status.healthy}{"\n"}'

It should display `status.healthy` field set to `true`.

  4. Verify that the new custom timeout has been applied to the target webhooks:
         
         kubectl get validatingwebhookconfigurations validating-webhook.cnrm.cloud.google.com -o jsonpath='{.webhooks[?(@.name=="deny-immutable-field-updates.cnrm.cloud.google.com")].timeoutSeconds}{"\n"}'
         
         kubectl get validatingwebhookconfigurations validating-webhook.cnrm.cloud.google.com -o jsonpath='{.webhooks[?(@.name=="deny-unknown-fields.cnrm.cloud.google.com")].timeoutSeconds}{"\n"}'

Applying the customization could take a few minutes.




## Configure timeout for mutating webhooks

You can configure the following mutating webhooks:

  * `container-annotation-handler.cnrm.cloud.google.com`
  * `generic-defaulter.cnrm.cloud.google.com`
  * `iam-defaulter.cnrm.cloud.google.com`
  * `management-conflict-annotation-defaulter.cnrm.cloud.google.com`



For example, you can configure the timeout of mutating webhook `container-annotation-handler.cnrm.cloud.google.com` by creating and applying the following example YAML file. The webhook is part of the configuration of the `mutating-webhook.cnrm.cloud.google.com` [mutating webhook configuration](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/#webhook-configuration).

  1. Create a file named `configure-mutating-webhook-timeout.yaml` and copy the following YAML into it:
         
         apiVersion: customize.core.cnrm.cloud.google.com/v1beta1
         kind: MutatingWebhookConfigurationCustomization
         metadata:
           name: mutating-webhook
         spec:
           webhooks:
           - name: container-annotation-handler
             timeoutSeconds: 20
         

**Note:** when specifying the name of webhook configuration and the names of webhooks in the YAML file, don't include the `.cnrm.cloud.google.com` suffix.
  2. Use [`kubectl apply`](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#apply) to apply the webhook timeout customization to your cluster:
         
         kubectl apply -f configure-mutating-webhook-timeout.yaml

  3. Verify the successful configuration by running the following command:
         
         kubectl get mutatingwebhookconfigurationcustomizations mutating-webhook -o jsonpath='{.status.healthy}{"\n"}'

It should display `status.healthy` field set to `true`.

  4. Verify that the new custom timeout has been applied to the target webhooks:
         
         kubectl get mutatingwebhookconfigurations mutating-webhook.cnrm.cloud.google.com -o jsonpath='{.webhooks[?(@.name=="container-annotation-handler.cnrm.cloud.google.com")].timeoutSeconds}{"\n"}'

Applying the customization could take a few minutes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
