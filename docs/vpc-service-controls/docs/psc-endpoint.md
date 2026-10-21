---
url: https://docs.cloud.google.com/vpc-service-controls/docs/psc-endpoint/
title: Configure Private Service Connect endpoints in service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:22.841627+00:00
---

# Configure Private Service Connect endpoints in service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/psc-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Configure Private Service Connect endpoints in service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Private Service Connect endpoints in service perimeters.

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) is a Google Cloud networking feature that lets you access managed services privately from your Virtual Private Cloud network through [endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints). VPC Service Controls lets you specify a Private Service Connect endpoint in ingress and egress rules, enabling communication between independent companies using internal IP addresses.

## Before you begin

  * Review [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

  * Understand the [roles](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#roles) and [requirements](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#begin) for creating endpoints.

  * [Create a new Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#create-endpoint) that only allows access to Google APIs supported by VPC Service Controls.

    * When you create the endpoint, ensure you use the target API bundle for VPC Service Controls (`vpc-sc`). For more information, see [Supported APIs](https://docs.cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#supported-apis).

    * After you create the endpoint, copy the **Endpoint ID**. You can also [retrieve this ID](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#endpoint-info) using the endpoint's forwarding rule name.




## Configure endpoints in ingress rules

### Console

You can configure an ingress rule to include forwarding rules when you [create](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#console) or [update](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console) a perimeter in the Google Cloud console.

  1. In the Google Cloud console navigation menu, click **Security** > **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. To create a new perimeter, click **New perimeter**.

To modify an existing perimeter, select the perimeter and click **Edit**.

  3. Select **Ingress policy**.

  4. In the **Ingress rules** pane, click **Add an ingress rule**.

  5. In the **From** section, select **Select sources** from the **Sources** list.

  6. Click **Private Service Connect endpoints**.

  7. Click **Add endpoints**.

  8. In the **Add Private Service Connect endpoints** pane, select one of the options:

     * **Search for PSC endpoints:** This option lets you search and select the required Private Service Connect endpoints from the list.

     * **Enter PSC endpoint ID manually:** This option lets you manually enter the Private Service Connect endpoints. To specify a Private Service Connect endpoint, use the following format: `//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_ID`, where `FORWARDING_RULE_ID` is the ID of the endpoint's forwarding rule.

  9. Click **Add endpoints**.

  10. Click **Done**.

  11. Click **Create** or **Save**.




For information about other ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

### gcloud

You can configure an ingress rule to include forwarding rules using a JSON file or a YAML file. The following sample uses the YAML format:
    
    
    - ingressFrom:
        identityType: ANY_IDENTITY | ANY_USER_ACCOUNT | ANY_SERVICE_ACCOUNT
        *OR*
        identities:
        - PRINCIPAL_IDENTIFIER
        sources:
        - resource: RESOURCE
        *OR*
        - accessLevel: ACCESS_LEVEL
        *OR*
        - pscEndpoint:
            forwardingRule: PSC_ENDPOINT
      ingressTo:
        operations:
        - serviceName: SERVICE_NAME
          methodSelectors:
          - method: METHOD_NAME
          *OR*
          - permission: PERMISSION
        *OR*
        roles:
        - ROLE_NAME
        resources:
        - projects/PROJECT_NUMBER
    

Replace `PSC_ENDPOINT` with the Private Service Connect endpoints from which you want to allow access to resources in the perimeter. To specify a Private Service Connect endpoint, use the following format: `//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_ID`, where `FORWARDING_RULE_ID` is the ID of the endpoint's forwarding rule.

For information about other ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

After you configure the ingress rule file with Private Service Connect endpoints, you can use the rule when you create or update a perimeter.

To configure the rule when you create a perimeter, run the following command:
    
    
    gcloud access-context-manager perimeters create NAME \
    --title=TITLE \
    --resources=RESOURCES \
    --restricted-services=RESTRICTED_SERVICES \
    --ingress-policies=INGRESS_FILENAME.yaml \
    --policy=POLICY_NAME
    

Replace `INGRESS_FILENAME` with the path of the ingress rule file.

For more information, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#gcloud).

To configure the rule when you update a perimeter, run the following command:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
    --set-ingress-policies=INGRESS_FILENAME.yaml
    

Replace the following:

  * `PERIMETER_ID`: The ID of the service perimeter that you want to update.
  * `INGRESS_FILENAME`: The path of the ingress rule file.



For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#gcloud).

## Configure endpoints in egress rules

### Console

You can configure an egress rule to include forwarding rules when you [create](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#console) or [update](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#console) a perimeter in the Google Cloud console.

  1. In the Google Cloud console navigation menu, click **Security** > **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. To create a new perimeter, click **New perimeter**.

To modify an existing perimeter, select the perimeter and click **Edit**.

  3. Select **Egress policy**.

  4. In the **Egress rules** pane, click **Add an egress rule**.

  5. In the **From** section, select **Select sources** from the **Sources** list.

  6. Click **Private Service Connect endpoints**.

  7. Click **Add endpoints**.

  8. In the **Add Private Service Connect endpoints** pane, select one of the options:

     * **Search for PSC endpoints:** This option lets you search and select the required Private Service Connect endpoints from the list.

     * **Enter PSC endpoint ID manually:** This option lets you manually enter the Private Service Connect endpoints. To specify a Private Service Connect endpoint, use the following format: `//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_ID`, where `FORWARDING_RULE_ID` is the ID of the endpoint's forwarding rule.

  9. Click **Add endpoints**.

  10. Click **Done**.

  11. Click **Create** or **Save**.




For information about other egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

### gcloud

You can configure an egress rule to include forwarding rules using a JSON file or a YAML file. The following sample uses the YAML format:
    
    
    - egressTo:
        operations:
        - serviceName: SERVICE_NAME
          methodSelectors:
          - method: METHOD_NAME
          *OR*
          - permission: PERMISSION
        *OR*
        roles:
        - ROLE_NAME
        resources:
        - projects/PROJECT_NUMBER
        *OR*
        externalResources:
        - EXTERNAL_RESOURCE_PATH
      egressFrom:
        identityType: ANY_IDENTITY | ANY_USER_ACCOUNT | ANY_SERVICE_ACCOUNT
        *OR*
        identities:
        - PRINCIPAL_IDENTIFIER
        sources:
        - resource: RESOURCE
        *OR*
        - accessLevel: ACCESS_LEVEL
        *OR*
        - pscEndpoint:
            forwardingRule: PSC_ENDPOINT
        sourceRestriction: RESTRICTION_STATUS
    

Replace `PSC_ENDPOINT` with the Private Service Connect endpoints through which you want to allow resources inside the perimeter to access external resources. To specify a Private Service Connect endpoint, use the following format: `//compute.googleapis.com/projects/PROJECT_ID/global/forwardingRules/FORWARDING_RULE_ID`, where `FORWARDING_RULE_ID` is the ID of the endpoint's forwarding rule.

For information about other egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

After you configure the egress rule file with Private Service Connect endpoints, you can use the rule when you create or update a perimeter.

To configure the rule when you create a perimeter, run the following command:
    
    
    gcloud access-context-manager perimeters create NAME \
    --title=TITLE \
    --resources=RESOURCES \
    --restricted-services=RESTRICTED_SERVICES \
    --egress-policies=EGRESS_FILENAME.yaml \
    --policy=POLICY_NAME
    

Replace `EGRESS_FILENAME` with the path of the egress rule file.

For more information, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#gcloud).

To configure the rule when you update a perimeter, run the following command:
    
    
    gcloud access-context-manager perimeters update PERIMETER_ID \
    --set-egress-policies=EGRESS_FILENAME.yaml
    

Replace the following:

  * `PERIMETER_ID`: The ID of the service perimeter that you want to update.
  * `EGRESS_FILENAME`: The path of the egress rule file.



For more information, see [Updating ingress and egress policies for a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies#gcloud).

## Troubleshoot access denials

If a Private Service Connect endpoint causes an access denial, the troubleshooting results page additionally displays the following information:

  * **PSC forwarding rule ID:** The endpoint ID of the forwarding rule that requested access.

  * **PSC forwarding rule state:** The status of the forwarding rule that requested access.

  * **Ingress and egress sections:** The violation analyzer evaluates the Private Service Connect endpoint against all ingress and egress rules and displays the results in the **Ingress** and **Egress** sections.


**Note:** You can view these details in the violation analyzer only if you have the required permissions for the project and resources where the Private Service Connect endpoint is configured.

For more information, see [Diagnose an access denial in violation analyzer](https://docs.cloud.google.com/vpc-service-controls/docs/violation-analyzer).

## Limitations

  * For the quotas and limits that apply to Private Service Connect endpoints in service perimeters, see [Quotas and limits](https://docs.cloud.google.com/vpc-service-controls/quotas).

  * You can use Private Service Connect endpoints in ingress and egress rules to access only the [supported services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

  * VPC Service Controls only supports newly created Private Service Connect endpoints in ingress and egress rules. You cannot use existing, older Private Service Connect endpoints; they must be recreated to be used with VPC Service Controls.




## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Learn more about [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
  * Learn how to [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
