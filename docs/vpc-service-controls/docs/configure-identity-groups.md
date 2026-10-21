---
url: https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups/
title: Configure identity groups and third-party identities in ingress and egress rules \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:48.661487+00:00
---

# Configure identity groups and third-party identities in ingress and egress rules  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/configure-identity-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Configure identity groups and third-party identities in ingress and egress rules Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use identity groups in ingress and egress rules to allow access to resources protected by service perimeters.

VPC Service Controls uses [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) to allow access to and from the resources and clients protected by service perimeters. To further refine access, you can specify identity groups in your ingress and egress rules.

An identity group is a convenient way to apply access controls to a collection of users and lets you manage identities that have similar access policies.

To configure identity groups in the ingress or egress rules, you can use the following supported identity groups in the `identities` attribute:

  * [Google group](https://docs.cloud.google.com/iam/docs/overview#google_group)
  * Third-party identities such as [workforce pool users](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) and [workload identities](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) ([Preview](https://cloud.google.com/products#product-launch-stages)) principals (such as Kubernetes service accounts, namespaces, or clusters).



For information about principal identifier formats of supported identity groups, see [Supported identities for ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

For information about how to apply ingress and egress rule policies, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

## Before you begin

  * Make sure that you read the [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).



## Configure identity groups in ingress rules

### Console

When you [update an ingress policy of a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console) or [set an ingress policy during perimeter creation](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console_1) using the Google Cloud console, you can configure the ingress rule to use identity groups.

  1. When you create a perimeter or edit a perimeter in the Google Cloud console, select **Ingress policy**.

  2. In the **From** section of your ingress policy, select **Select identities & groups** from the **Identities** list.

  3. Click **Add identities**.

  4. In the **Add identities** pane, specify a Google group, third-party identity, or [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) principal that you want to access resources in the perimeter. To specify an identity group, use the format specified in [Supported identities](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

  5. Click **Add identities**.

  6. Click **Save**.




For information about the other ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

### gcloud

You can configure an ingress rule to use identity groups using a JSON file or a YAML file. The following sample uses the YAML format:
    
    
    - ingressFrom:
        identities:
        - PRINCIPAL_IDENTIFIER
        sources:
        - resource: RESOURCE
          *OR*
        - accessLevel: ACCESS_LEVEL
      ingressTo:
        operations:
        - serviceName: SERVICE_NAME
          methodSelectors:
          - method: METHOD_NAME
        resources:
        - projects/PROJECT_NUMBER
    

Replace the following:

  * `PRINCIPAL_IDENTIFIER`: specify a Google group, third-party identity, or [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) principal that you want to access resources in the perimeter. To specify an identity group, use the format specified in [Supported identities](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).



For information about the other ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

After you update an existing ingress rule to configure identity groups, you need to update the rule policies of the service perimeter:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID --set-ingress-policies=RULE_POLICY.yaml
    

Replace the following:

  * `PERIMETER_ID`: the ID of the service perimeter that you want to update.
  * `RULE_POLICY`: the path of the modified ingress rule file.



For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating).

## Configure identity groups in egress rules

### Console

When you [update an egress policy of a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console) or [set an egress policy during perimeter creation](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console_1) using the Google Cloud console, you can configure the egress rule to use identity groups.

  1. When you create a perimeter or edit a perimeter in the Google Cloud console, select **Egress policy**.

  2. In the **From** section of your egress policy, select **Select identities & groups** from the **Identities** list.

  3. Click **Add identities**.

  4. In the **Add identities** pane, specify a Google group, third-party identity, or [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) principal that can access the specified resources outside the perimeter. To specify an identity group, use the format specified in [Supported identities](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).

  5. Click **Add identities**.

  6. Click **Save**.




For information about the other egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

### gcloud

You can configure an egress rule to use identity groups using a JSON file or a YAML file. The following sample uses the YAML format:
    
    
    - egressTo:
        operations:
        - serviceName: SERVICE_NAME
          methodSelectors:
          - method: METHOD_NAME
        resources:
        - projects/PROJECT_NUMBER
      egressFrom:
        identities:
        - PRINCIPAL_IDENTIFIER
    

Replace the following:

  * `PRINCIPAL_IDENTIFIER`: specify a Google group, third-party identity, or [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) principal that can access the specified resources outside the perimeter. To specify an identity group, use the format specified in [Supported identities](https://docs.cloud.google.com/vpc-service-controls/docs/supported-identities).



For information about the other egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

After you update an existing egress rule to configure identity groups, you need to update the rule policies of the service perimeter:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID --set-egress-policies=RULE_POLICY.yaml
    

Replace the following:

  * `PERIMETER_ID`: the ID of the service perimeter that you want to update.
  * `RULE_POLICY`: the path of the modified egress rule file.



For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#updating).

## Limitations

  * Before using identity groups, understand the [unsupported features](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#unsupported-features) in ingress and egress rules.
  * When you use identity groups in an egress rule, you can't set the `resources` field in the `egressTo` attribute to `"*"`.
  * You can't use a workload identity in ingress and egress rules to allow [Apache Airflow web interface](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) operations in Managed Airflow. However, you can use the `ANY_IDENTITY` identity type in ingress and egress rules to allow access to all identities, including workload identities. For more information about the `ANY_IDENTITY` identity type, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).
  * For information about ingress and egress rule limits, see [Quotas and limits](https://docs.cloud.google.com/vpc-service-controls/quotas).



## What's next

  * [Example of using identity groups and third-party identities in ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/identity-groups-examples)
  * Watch a video to [learn about using identity groups in ingress and egress rules](https://youtu.be/5rysBo2tL88).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
