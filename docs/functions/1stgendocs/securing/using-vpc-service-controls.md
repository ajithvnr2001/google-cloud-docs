---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/using-vpc-service-controls/
title: Configure VPC Service Controls (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:41.405482+00:00
---

# Configure VPC Service Controls (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/using-vpc-service-controls/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure VPC Service Controls (1st gen)

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) is a Google Cloud feature that lets you set up a secure perimeter to guard against data exfiltration. This guide shows how to use VPC Service Controls with Cloud Run functions to add additional security to your functions.

For limitations with this integration, see the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#functions).

## Organization-level setup

To use VPC Service Controls with Cloud Run functions, you can configure a service perimeter at the organization level. By configuring appropriate organization policies, you can ensure that VPC Service Controls checks are enforced when using Cloud Run functions and that developers can only deploy services compliant with VPC Service Controls. Learn more about [inheritance](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#inheritance) and [violations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#violations) when setting an organization policy.

### Set up a VPC Service Controls perimeter

To set up a service perimeter, you need the [Organization Viewer](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles) (`roles/resourcemanager.organizationViewer`) and [Access Context Manager Editor](https://docs.cloud.google.com/access-context-manager/docs/access-control#required_roles) (`roles/accesscontextmanager.policyEditor`) roles.

Follow the [VPC Service Controls Quickstart](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter) to:

  1. Create a service perimeter.

**Note:** Cloud Run functions uses Cloud Build, Artifact Registry, Container Registry ([Deprecated](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation)), and Cloud Storage to build and manage your source code in a runnable container. If these services are restricted by the service perimeter, VPC Service Controls blocks the Cloud Run functions build, even if Cloud Run functions is not added as a restricted service to the perimeter. To use Cloud Run functions inside a service perimeter, configure an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the Cloud Build service account in your service perimeter. Cloud Build also uses Cloud Logging, which can fail to log properly if a VPC-SC perimeter restricts it. This won't cause builds to fail, but we recommend granting Cloud Build access to the service perimeter with an ingress rule to ensure proper logging.
  2. Add one or more projects to the perimeter.

**Note:** If you are using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), make sure to add the host project and service projects to the same perimeter.
  3. Restrict the Cloud Functions API.




After setting up your service perimeter, all calls to the restricted API are checked to ensure that the calls originate from within the same perimeter.

#### Optional: Enable perimeter access for development machines

Because VPC Service Controls checks are enforced for the Cloud Functions API, calls to the Cloud Functions API fail unless they originate from within the service perimeter. Thus, to manage functions with the Cloud Functions API, the Cloud Run functions UI in the Google Cloud console, or the Google Cloud CLI, choose one of the following options:

  * **Use a machine inside the VPC Service Controls perimeter.** For example, you can use a Compute Engine VM or an on-premises machine connected to your VPC network using a VPN.

  * **Grant function developers access to the perimeter.** For example, you can create access levels that enable perimeter access based on IP address or user identity. See [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) for more information.




### Set up organization policies

To manage organization policies, you need the [Organization Policy Administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin) (`roles/orgpolicy.policyAdmin`) role.

To comply with VPC Service Controls and protect against data exfiltration, set up the following organization policies that control the allowable [network settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings) for Cloud Run functions in the service perimeter.

**Note:** The organization policies go into effect for new function deployments. Existing functions continue to work and might pose an exfiltration risk until they are redeployed with the allowed settings. See Audit existing functions to ensure VPC Service Controls compliance.

#### Restrict allowed ingress settings

The `cloudfunctions.allowedIngressSettings` organization policy controls the [ingress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#ingress_settings) that developers are allowed to use for Cloud Run functions. Set this organization policy to mandate that developers use the value [`ALLOW_INTERNAL_ONLY`](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#ingresssettings):

###  Console 

  1. Go to the **Allowed ingress settings** policy page in the Google Cloud console:

[Go to organization policy](https://console.cloud.google.com/iam-admin/orgpolicies/cloudfunctions-allowedIngressSettings)

  2. Click **Manage Policy**.

  3. On the **Edit policy** page, select **Customize**.

  4. Under **Policy enforcement** , select **Replace**.

  5. Under **Policy values** , select **Custom**.

  6. Under **Policy type** , select **Allow**.

  7. Under **Custom values** , enter `ALLOW_INTERNAL_ONLY`.

  8. Click **Set Policy**.




###  gcloud 

Use the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command:
    
    
    gcloud resource-manager org-policies allow \
      cloudfunctions.allowedIngressSettings ALLOW_INTERNAL_ONLY \
      --organization ORGANIZATION_ID
    

where `ORGANIZATION_ID` is your organization ID.

After this organization policy is in place, all functions must use the value `ALLOW_INTERNAL_ONLY` for their ingress settings. This means that HTTP functions can only accept traffic originating from a VPC network within the service perimeter. Function deployments specifying a different value will fail.

#### Require VPC connector

The `cloudfunctions.requireVPCConnector` organization policy controls whether a [Serverless VPC Access connector](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc#configuring) is required for functions. Set this organization policy to enforce this constraint:

###  Console 

  1. Go to the **Require VPC Connector** policy page in the Google Cloud console:

[Go to organization policy](https://console.cloud.google.com/iam-admin/orgpolicies/cloudfunctions-requireVPCConnector)

  2. Click **Manage policy**.

  3. On the **Edit policy** page, select **Customize**.

  4. Under **Enforcement** , select **On**.

  5. Click **Set Policy**.




###  gcloud 

Use the [`gcloud resource-manager org-policies enable-enforce`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/enable-enforce) command:
    
    
    gcloud resource-manager org-policies enable-enforce \
      cloudfunctions.requireVPCConnector \
      --organization ORGANIZATION_ID
    

where `ORGANIZATION_ID` is your organization ID.

After this organization policy is in place, all functions must use a Serverless VPC Access connector. Function deployments that don't specify a connector will fail.

#### Restrict allowed VPC connector egress settings

The `cloudfunctions.allowedVpcConnectorEgressSettings` organization policy controls the [egress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#egress_settings) that developers are allowed to use for Cloud Run functions. Set this organization policy to allow only the value [`ALL_TRAFFIC`](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions#vpcconnectoregresssettings):

###  Console 

  1. Go to the **Allowed VPC Connector egress settings** policy page in the Google Cloud console:

[Go to organization policy](https://console.cloud.google.com/iam-admin/orgpolicies/cloudfunctions-allowedVpcConnectorEgressSettings)

  2. Click **Manage policy**.

  3. On the **Edit policy** page, select **Customize**.

  4. Under **Policy enforcement** , select **Replace**.

  5. Under **Policy values** , select **Custom**.

  6. Under **Policy type** , select **Allow**.

  7. Under **Custom values** , enter `ALL_TRAFFIC`.

  8. Click **Set Policy**.




###  gcloud 

Use the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command:
    
    
    gcloud resource-manager org-policies allow \
      cloudfunctions.allowedVpcConnectorEgressSettings ALL_TRAFFIC \
      --organization ORGANIZATION_ID
    

where `ORGANIZATION_ID` is your organization ID.

After this organization policy is in place, all functions must use the value `ALL_TRAFFIC` for their egress settings. This means that functions must route all egress traffic through your VPC network. Function deployments specifying a different value will fail.

Combined with the `cloudfunctions.requireVPCConnector` organization policy, this forces all egress traffic to traverse the VPC network where it is subject to its configured firewall and routing rules.

## Project-level setup

For individual projects within the service perimeter, you must perform additional configuration to use VPC Service Controls.

### Configure VPC networks

To access Google APIs and services while mitigating data exfiltration risks, requests should be sent to the [restricted virtual IP (VIP) range](https://docs.cloud.google.com/vpc/docs/private-access-options#domain-vips), `199.36.153.4/30` (`restricted.googleapis.com`).

For each VPC network in a project, follow these steps to block outbound traffic except for traffic to the restricted VIP range:

  1. [Configure firewall rules](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-firewall) to prevent data from leaving the VPC network:

**Caution:** Failure to correctly configure firewall rules could leave your functions vulnerable to data exfiltration.
     * Create a deny egress rule that blocks all outbound traffic.

**Note:** Ensure the deny all egress firewall rule has a priority after 1000. Otherwise, traffic from the Serverless VPC Access connector to your function will be blocked.
     * Create an allow egress rule that permits traffic to `199.36.153.4/30` on TCP port 443. Ensure that it has a priority _before_ the deny egress rule you just created—this allows egress only to the restricted VIP range.

  2. [Configure DNS to resolve `*.googleapis.com` to `restricted.googleapis.com`](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-dns).

  3. Configure DNS with an A record mapping `*.cloudfunctions.net` to the `199.36.153.4/30` IP range. You can do this with Cloud DNS:
         
         gcloud dns managed-zones create ZONE_NAME \
         --visibility=private \
         --networks=https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/global/networks/VPC_NAME \
         --description=none \
         --dns-name=cloudfunctions.net
         
         gcloud dns record-sets transaction start --zone=ZONE_NAME
         
         gcloud dns record-sets transaction add --name=*.cloudfunctions.net. \
         --type=A 199.36.153.4 199.36.153.5 199.36.153.6 199.36.153.7 \
         --zone=ZONE_NAME \
         --ttl=300
         
         gcloud dns record-sets transaction execute --zone=ZONE_NAME
         

**Note:** `ZONE_NAME` must be different than the name used to set up the `*.googleapis.com` rules in step 2.**Note:** In some terminals, you may need to add double quotes around the value for the `--name` flag (for example, `--name="\*.cloudfunctions.net."`) that is passed to the `gcloud record-sets transaction add` command.
  4. [Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) for your VPC Connector's Subnet.

**Note:** This is only necessary if you specified your own subnet when [creating the VPC Connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#creating_a_connector). If you instead created the connector using a Custom IP Range, a Google managed subnet was created for you with Private Google Access enabled.



At this point, requests originating from within the VPC network:

  * are not able to leave the VPC network, preventing egress outside the service perimeter.
  * can only reach Google APIs and services that check VPC Service Controls, preventing exfiltration through Google APIs.



### Grant the Cloud Build service account access to the VPC Service Controls perimeter

Cloud Run functions uses Cloud Build to build your source code into a runnable container. In order to use Cloud Run functions with VPC Service Controls, you must configure the Cloud Build service account to have access to your service perimeter:

**Note:** The default Cloud Build service account may have changed starting in May 2024. Review [Cloud Build service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates) to confirm the default service account for your project before proceeding.

#### Find the service account name

  1. Use the IAM page in the Google Cloud console to find the Cloud Build service account.

[Open IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Make sure the correct project is displayed in the project drop down.

  3. Search for `cloudbuild.gserviceaccount.com`. The email address in the form `PROJECT_NUMBER@cloudbuild.gserviceaccount.com` is the service account name.




#### Grant the service account access to the service perimeter

Once you have the service account name, follow the guide at [Limit access by user or service account](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) to create an access level for the service account. Then, follow [Adding an access level to an existing perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level) to add the access level to your service perimeter.

### Deploy functions compliant with VPC Service Controls

After VPC Service Controls is configured for Cloud Run functions, you must ensure that all functions deployed within the service perimeter comply with the specified organization policies. This means that:

  * **All functions must use a Serverless VPC Access connector.** See [Connecting to a VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc) for more information.
  * **All functions must allow only traffic from internal sources.** See [Ingress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#ingress_settings) for more information.
  * **All functions must route all outgoing traffic through the VPC network.** See [Egress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#egress_settings) for more information.



Function deployments that don't meet these criteria will fail.

#### Audit existing functions to ensure VPC Service Controls compliance

After setting up VPC Service Controls, new functions created in projects within the service perimeter are automatically checked for compliance. However, to avoid disruption of existing workloads, existing functions continue to work and might not comply with organization policies.

We recommend that you audit existing functions and update or redeploy functions as necessary. To facilitate this process, you might create a script that uses the Cloud Functions API to list your functions and highlight those that don't specify the proper network settings.

## Using VPC Service Controls with functions outside a perimeter

The preceding sections apply to the scenario where you deploy Cloud Run functions within a VPC Service Controls service perimeter.

If you need to deploy a function outside of a service perimeter but the function requires access to resources inside a perimeter, use the following configuration:

  1. Grant the Cloud Build service account access to the VPC Service Controls perimeter.
  2. Grant the function's [runtime service account](https://docs.cloud.google.com/functions/1stgendocs/concepts/iam#runtime_service_accounts) access to the perimeter. You can do this either by [creating an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) and [adding the access level to the service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level), or by [creating an ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies) on the perimeter.
  3. [Connect the function to a VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc).
  4. Route all outgoing traffic from the function through the VPC network. See [Egress settings](https://docs.cloud.google.com/functions/1stgendocs/networking/network-settings#egress_settings) for more information.



After you complete this configuration, the function will be able to reach resources protected by the perimeter.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
