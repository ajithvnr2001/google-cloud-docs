---
url: https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters/
title: Create a service perimeter \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:31.659550+00:00
---

# Create a service perimeter  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Create a service perimeter Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a service perimeter.

## Before you begin

  * Read about [configuring service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  * Read about [management of VPC networks in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management).

  * Read about [granting access to VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

  * If you want to configure external access to your protected services when you create your perimeter, [create one or more access levels](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) before you create the perimeter.




## Create a service perimeter

**Note:** Service perimeters cannot contain projects from different organizations.

This section describes how to create a service perimeter, add projects or [VPC networks](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-perimeters-management) to the perimeter, and protect services.

When you create a service perimeter, you can optionally [allow access to protected services from _outside_ the perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels), and [specify what services are accessible](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) to other services and users _inside_ the perimeter. If preferred, you can configure these settings after you create a perimeter.

After you create a service perimeter or update an existing service perimeter, it can take up to 30 minutes for the changes to propagate and take effect. During this time, the perimeter might block requests with the following error message: `Error 403: Request is prohibited by organization's policy.`

### Console

  1. In the Google Cloud console navigation menu, click **Security** , and then click **VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. If you are prompted, select your organization, folder, or project.

  3. Select an existing access policy or [create a new access policy](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#create-access-policy). Make sure that the access policy scope includes all projects and VPC networks that you want to add to the perimeter.

  4. On the **VPC Service Controls** page, select a perimeter enforcement mode. By default, **Enforced mode** is selected. If you want to create a dry run perimeter, click **Dry run mode**.

_Enforced perimeters_ actively prevent access to protected services. _Dry run perimeters_ log violations of the perimeter as though services were protected, but do not prevent access to those services. For more information about the enforced and dry run modes, read about [service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  5. Click **New perimeter**.

  6. On the **Create a service perimeter** page, in the **Title** field, enter a name for the perimeter.

A perimeter name can have a maximum length of 50 characters, must start with a letter, and can contain only ASCII Latin letters (a-z, A-Z), numbers (0-9), or underscores (`_`). The perimeter name is case sensitive and must be unique within an access policy.

  7. Optional: In the **Description** field, enter a description for the perimeter.

  8. For **Perimeter type** , select **Regular**.

  9. For **Enforcement mode** , select a perimeter enforcement mode. The available options are **Dry run** and **Enforced**.

  10. Click **Continue**.

  11. To add projects or VPC networks that you want to secure within the perimeter, do the following:

     1. To add projects to the perimeter, click **Add projects**.

        1. In the **Add projects** pane, select the projects that you want to protect.

        2. Click **Add selected projects**. The added projects appear in the **Projects** section.

     2. To add VPC networks to the perimeter, click **Add networks**.

        1. From the list of projects, click the project that contains the VPC networks.

        2. In the **Add VPC networks** pane, select the VPC networks that you want to protect.

        3. Click **Add selected networks**. The added networks appear in the **VPC networks** section.

     3. Click **Continue**.

  12. To select the services that you want to secure within the perimeter, do the following:

     1. In the **Restricted services** pane, click **Add services**.

     2. In the **Add services** pane, select the services that you want to protect.

**Note:** We recommend that you restrict all services when you create a perimeter to mitigate the risk of data exfiltration from Google Cloud services.
     3. Click **Add selected services**.

     4. Click **Continue**.

  13. Optional: If you want to define what services are accessible _from network endpoints inside_ a perimeter, in the **VPC accessible services** pane, select one of the available options:

     * **All services** : This option allows all the Google Cloud services.

     * **No services** : This option doesn't allow any of the Google Cloud services.

     * **All restricted services** : This option allows only the Google Cloud services that you have protected in this perimeter.

     * **Selected services** : This option allows only the Google Cloud services that you have selected.

       1. Click **Add services**.

       2. In the **Add services** pane, select the services that you want to allow.

       3. Click **Add selected services**.

       4. To additionally include all the restricted services that the perimeter protects to the selected services, click the **Include all restricted services** toggle to the on position.

       5. Click **Continue**.

You can also [add accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#accessible-services) after a perimeter has been created.

For more information, see [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

  14. Optional: To allow access to protected resources from outside the perimeter by using access levels, do the following:

     1. In the **Access levels** pane, click **Add access levels**.

You can also [add access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) after a perimeter has been created.

     2. Select the checkboxes corresponding to the access levels that you want to apply to the perimeter.

     3. Click **Add selected access levels**.

     4. Click **Continue**.

  15. To allow access to resources within a perimeter from API clients outside the perimeter, do the following:

     1. In the **Ingress rules** pane, click **Add an ingress rule**.

     2. In the **Title** field, enter a title for the ingress rule.

     3. In the **From** section, specify the sources from outside the perimeter that require access. You can specify projects, access levels, and VPC networks as sources.

     4. In the **To** section, specify the resources within the perimeter that the sources can access.

     5. Click **Continue**.

For the list of ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

**Note:** Access levels and ingress rules work together to control incoming traffic to a perimeter. A request is allowed if it satisfies the conditions of either the access level or the ingress rule.
  16. To allow access that involves an API client or resources within the perimeter to resources outside a perimeter, do the following:

     1. In the **Egress rules** pane, click **Add an egress rule**.

     2. In the **Title** field, enter a title for the egress rule.

     3. In the **From** section, specify the sources from within the perimeter that require access.

     4. In the **To** section, specify the resources outside the perimeter that the sources can access.

For the list of egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

  17. Click **Create**.




### gcloud

To create a new perimeter in [enforced mode](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#enforced-mode), use the [`gcloud access-context-manager perimeters create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/create) command.
    
    
    gcloud access-context-manager perimeters create NAME \
      --title=TITLE \
      --resources=RESOURCES \
      --restricted-services=RESTRICTED-SERVICES \
      --ingress-policies=INGRESS-FILENAME.yaml \
      --egress-policies=EGRESS-FILENAME.yaml \
      [--access-levels=LEVELS] \
      [--enable-vpc-accessible-services] \
      [--vpc-allowed-services=ACCESSIBLE-SERVICES] \
      --policy=POLICY_NAME

To create a new perimeter in [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#dry-run-mode), use the [`gcloud access-context-manager perimeters dry-run create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/create) command.
    
    
    gcloud access-context-manager perimeters dry-run create NAME \
      --perimeter-title=TITLE \
      --perimeter-type=TYPE \
      --perimeter-resources=RESOURCES \
      --perimeter-restricted-services=RESTRICTED-SERVICES \
      --perimeter-ingress-policies=INGRESS-FILENAME.yaml \
      --perimeter-egress-policies=EGRESS-FILENAME.yaml \
      [--perimeter-access-levels=LEVELS] \
      [--perimeter-enable-vpc-accessible-services] \
      [--perimeter-vpc-allowed-services=ACCESSIBLE-SERVICES] \
      --policy=POLICY_NAME

Replace the following:

  * NAME is the name of the perimeter.

A perimeter name can have a maximum length of 50 characters, must start with a letter, and can contain only ASCII Latin letters (a-z, A-Z), numbers (0-9), or underscores (`_`). The perimeter name is case sensitive and must be unique within an access policy.

  * TITLE is the human-readable title of the perimeter.

  * TYPE is the type of the perimeter. For example, a "regular" perimeter or a "bridge" perimeter.

  * RESOURCES is a comma-separated list of one or more project numbers or VPC network names. For example: `projects/12345` or `//compute.googleapis.com/projects/my-project/global/networks/vpc1`. Only projects and VPC networks are allowed. Project format: `projects/project_number`. VPC format: `//compute.googleapis.com/projects/project-id/global/networks/network_name`. If you specify projects, only project numbers are supported. You cannot use the project name or ID.

  * RESTRICTED-SERVICES is a comma-separated list of one or more services. For example: `storage.googleapis.com` or `storage.googleapis.com,bigquery.googleapis.com`.

**Note:** We recommend you restrict all services when you create a perimeter to mitigate the risk of data exfiltration from Google Cloud services.
  * INGRESS-FILENAME is a JSON or YAML file that contains the values of source, identity, project, and service attributes. For the list of ingress rule attributes, see [Ingress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference).

  * EGRESS-FILENAME is a JSON or YAML file that contains the values of identity, project, and service attributes. For the list of egress rule attributes, see [Egress rules reference](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#egress-rules-reference).

  * POLICY_NAME is the numeric name of your organization's access policy. For example, `330193482019`. You only need to include the policy name if you haven't [set a default access policy](https://docs.cloud.google.com/access-context-manager/docs/manage-access-policy#set-default).




Additional options:

  * `--access-levels` or `--perimeter-access-levels` is required only if you want to add access levels when you create the perimeter. LEVELS is a comma-separated list of one or more access levels that you want to apply to the service perimeter.

You can also [add access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) after you create the perimeter.

  * `--enable-vpc-accessible-services` and `--vpc-allowed-services`, or `--perimeter-enable-vpc-accessible-services` and `--perimeter-vpc-allowed-services` are required only if you want to add VPC accessible services when you create the perimeter. ACCESSIBLE-SERVICES is a comma-separated list of one or more services that you want to _allow_ networks _inside_ your perimeter to access. Access to any services that are _not included_ in this list are prevented.

You can only make a service accessible if you also protect it when configuring the perimeter.

To quickly include all the services protected by a perimeter, specify `RESTRICTED-SERVICES` in the list for ACCESSIBLE-SERVICES. For example, `--perimeter-vpc-allowed-services=RESTRICTED-SERVICES`.

You can also [define VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#accessible-services) after you create the perimeter.




For example, the following command creates a new dry run mode perimeter named `ProdPerimeter` that includes projects `example-project` and `example-project2`, and restricts the Cloud Storage and BigQuery APIs.
    
    
    gcloud access-context-manager perimeters \
      dry-run create ProdPerimeter --perimeter-title="Production Perimeter" \
      --perimeter-type="regular" \
      --perimeter-resources=projects/12345,projects/67890 \
      --perimeter-restricted-services=storage.googleapis.com,bigquery.googleapis.com \
      --perimeter-ingress-policies=ingress.yaml \
      --perimeter-egress-policies=egress.yaml \
      --policy=330193482019

###  API 

To create a service perimeter, call [`accessPolicies.servicePerimeters.create`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters/create).
    
    
     POST https://accesscontextmanager.googleapis.com/v1/accessPolicies/POLICY_NAME/servicePerimeters

Where:

  * POLICY_NAME is the numeric name of your organization's access policy. For example, `330193482019`.



### Request body

The request body must include a [`ServicePerimeter`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters#ServicePerimeter) resource that defines the service perimeter.

For the `ServicePerimeter` resource, specify `PERIMETER_TYPE_REGULAR` for `perimeterType`.

**Note:** We recommend that you restrict all services when you create a perimeter.

#### Dry Run Mode

The proposed perimeter must be included as the `spec` and `useExplicitDryRunSpec` set to true.

### Response body

If successful, the response body for the call contains an [`Operation`](https://docs.cloud.google.com/access-context-manager/docs/reference/rest/Shared.Types/Operation) resource that provides details about the `POST` operation.

## What's next

  * Learn how to [configure Private Service Connect endpoints in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/psc-endpoint).
  * Learn how to test the impact of a service perimeter using the [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).
  * Learn how to [manage existing](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) service perimeters.
  * Learn how to [troubleshoot common VPC Service Controls issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).
  * Complete this [codelab](https://codelabs.developers.google.com/codelabs/vpc-sc-beginnerlab-1) to learn how to protect projects and their services using VPC Service Controls.
  * Learn how to [set up and view the violation dashboard](https://docs.cloud.google.com/vpc-service-controls/docs/violation-dashboard).
  * Complete the [Deploy an agent and Agent Gateway with VPC Service Controls codelab](https://codelabs.developers.google.com/agw-vpcsc-codelab) to learn how to secure agents and Agent Gateway within a service perimeter.
  * Watch a video to [learn about deploying and creating service perimeters](https://youtu.be/rK-45qUpGJE).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
