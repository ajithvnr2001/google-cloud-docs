---
url: https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls/
title: Using VPC Service Controls (VPC SC) \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:21.665268+00:00
---

# Using VPC Service Controls (VPC SC)  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Using VPC Service Controls (VPC SC) Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) is a Google Cloud feature that lets you set up a secure perimeter to guard against data exfiltration. Both the default `run.app` URL and custom domains are subject to VPC Service Controls. This guide shows how to use VPC Service Controls with Cloud Run to add additional security to your services.

## Limitations and advisories

  * For Artifact Registry or Container Registry:

    * The registry where you store your container must be in the same VPC Service Controls service perimeter as the project you're deploying to.
    * The code being built must be in the same perimeter as the registry that the container is being pushed to.
  * The [continuous deployment](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build) feature is not available for projects inside a VPC Service Controls perimeter.

  * When Cloud Run services are invoked, VPC Service Controls policy enforcement does not use the client's IAM authentication information. Such requests have the following limitations:

    * VPC Service Controls ingress policy rules that use IAM principals are not supported. Only the `ANY_IDENTITY` identity type is supported.
    * Access levels for VPC Service Controls perimeters that use IAM principals are not supported.



## Set up your organization to support VPC Service Controls

To use VPC Service Controls with Cloud Run, you can configure a service perimeter at the organization level. By configuring appropriate organization policies, you can make sure that VPC Service Controls checks are enforced when using Cloud Run and that developers can only deploy services compliant with VPC Service Controls. Learn more about [inheritance](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#inheritance) and [violations](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#violations) when setting an organization policy.

If you are deploying Cloud Run functions with `gcloud functions`, you or your administrator must grant the Cloud Build service account access on the VPC Service Controls perimeter. Refer to [Build process overview](https://docs.cloud.google.com/functions/docs/building#grant-build-access) for more information.

### Set up a VPC Service Controls perimeter

The following steps show how to [set up a VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter).

  1. Make sure that you have the [required roles for administering VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/access-control).

  2. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to the VPC Service Controls page](https://console.cloud.google.com/security/service-perimeter)

  3. If you are prompted, select your **Organization**.

  4. Click **Manage Access Policies**. Select an access policy or [create one](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#create-access-policy). The access policy must include all projects that you want to add to the perimeter.

  5. Click **New Perimeter**. Type a name for the perimeter.

  6. Select the projects that you want to secure within the perimeter.

     1. Click **Projects**.

     2. In the **Add Projects** window, select the projects you want to add.

If you are using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), make sure to add the host project and service projects.

     3. Click the **Add Projects** button.

  7. Select Cloud Run as the service that you want to secure within the perimeter.

     1. Click **Restricted Services**.

     2. Click **Add Services**.

     3. Search for "Cloud Run." Then select **Cloud Run Admin API**. (Select **Cloud Functions V2 API** if you used `gcloud functions`.)

     4. Click **Add Cloud Run Admin API** (or **Cloud Functions V2 API** if you used `gcloud functions`).

  8. Enable access for developers.

Turning on VPC Service Controls for Cloud Run prevents all access from outside the perimeter, including viewing and deploying services from machines not in the perimeter, such as company laptops. In order for developers and application operators to view and deploy resources within the perimeter, you must configure the perimeter [ingress policy](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules):

     1. Click **Ingress Policy**.

     2. Specify the **Source** , **Identity** , **Project** , and **Services**.

     3. Click **Add Rule**.

If your organization uses Access Context Manager, you can also enable access for developers by setting access levels.

  9. Click **Create Perimeter**.




Once you have completed these steps, all calls to the Cloud Run Admin API are checked to make sure that they originate from within the same perimeter.

### Set up organization policies

To manage organization policies, you need the [Organization Policy Administrator](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#add-org-policy-admin) (`roles/orgpolicy.policyAdmin`) role.

To comply with VPC Service Controls and protect against data exfiltration, set up the following organization policies that control the allowable [ingress](https://docs.cloud.google.com/run/docs/securing/ingress) and [egress](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#egress) settings for Cloud Run in the service perimeter.

**Note:** The organization policies are enforced during administrative actions such as deploying a revision, migrating traffic and changing service settings. Existing services continue to serve traffic and might pose an exfiltration risk until they are re-deployed with the allowed settings. Refer to Audit existing services to ensure VPC Service Controls compliance.

#### Restrict allowed ingress settings

The `run.allowedIngress` organization policy controls the [ingress settings](https://docs.cloud.google.com/run/docs/securing/ingress) that developers are allowed to use for Cloud Run. Set this organization policy to mandate that developers use the value [`internal`](https://docs.cloud.google.com/run/docs/securing/ingress#settings) if you want to allow only internal requests, or [`internal-and-cloud-load-balancing`](https://docs.cloud.google.com/run/docs/securing/ingress#settings) if you want to allow requests through an external Application Load Balancer, with the access controls managed by Cloud Load Balancing.

For more information on these settings, refer to [Restricting ingress for Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress)

###  Console 

  1. Go to the **Allowed ingress settings (Cloud Run)** policy page in the Google Cloud console:

[Go to organization policy](https://console.cloud.google.com/iam-admin/orgpolicies/run-allowedIngress)

  2. Click **Edit**.

  3. On the **Edit** page, select **Customize**.

  4. Under **Policy enforcement** , select **Replace**.

  5. Under **Policy values** , select **Custom**.

  6. Under **Policy type** , select **Allow**.

  7. Under **Custom values** , enter `internal`. If you'd like to also allow Cloud Load Balancing traffic, click **New policy value** and enter `internal-and-cloud-load-balancing`.

  8. Click **Save**.




###  gcloud 

Use the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command:
    
    
    gcloud resource-manager org-policies allow \
      run.allowedIngress internal \
      --organization ORGANIZATION_ID
    

where `ORGANIZATION_ID` is your organization ID. If you'd like to also allow Cloud Load Balancing traffic, replace `run.allowedIngress internal` with `run.allowedIngress internal-and-cloud-load-balancing`.

After this organization policy is in place, all services must use allowed values for their ingress settings. This means that Cloud Run services can only accept traffic originating from a VPC network within the service perimeter. Attempts to set ingress to a different value will be blocked by the [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

#### Restrict allowed VPC egress settings

The `run.allowedVPCEgress` organization policy controls the [egress settings](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#egress) that developers are allowed to use for Cloud Run. Set this organization policy to allow only the value [`all-traffic`](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#egress):

###  Console 

  1. Go to the **Allowed VPC egress settings (Cloud Run)** policy page in the Google Cloud console:

[Go to organization policy](https://console.cloud.google.com/iam-admin/orgpolicies/run-allowedVPCEgress)

  2. Click **Edit**.

  3. On the **Edit** page, select **Customize**.

  4. Under **Policy enforcement** , select **Replace**.

  5. Under **Policy values** , select **Custom**.

  6. Under **Policy type** , select **Allow**.

  7. Under **Custom values** , enter `all-traffic`.

  8. Click **Save**.




###  gcloud 

Use the [`gcloud resource-manager org-policies allow`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow) command:
    
    
    gcloud resource-manager org-policies allow \
      run.allowedVPCEgress all-traffic \
      --organization ORGANIZATION_ID
    

where `ORGANIZATION_ID` is your organization ID.

##### Behavior after organization policy is set

After the organization policy is in place, all new revisions must use Direct VPC egress or a Serverless VPC Access connector and must use the value `all-traffic` for their egress settings. This combination routes all egress traffic from these revisions through a VPC network, subjecting this traffic to the VPC network's firewall rules and other settings. New revision deployments specifying a different value are blocked by the [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

##### Org policy and traffic migrations

For services existing before the organization policy was set, you can continue to migrate traffic to non-compliant revisions until all revisions serving traffic have become compliant.

This behavior lets you test and gradually roll out new revisions that comply with the policy. After all revisions serving traffic are compliant with the policy, any attempt to move traffic to non-compliant revisions will be blocked by the org policy.

## Set up your project to support VPC Service Controls

For individual projects within the service perimeter, you must perform additional configuration to use VPC Service Controls.

### Configure VPC networks

This section shows how to configure your VPC network so that requests sent to the regular `googleapis.com` domains are automatically routed to the restricted [restricted virtual IP (VIP) range](https://docs.cloud.google.com/vpc/docs/private-access-options#domain-vips), `199.36.153.4/30` (`restricted.googleapis.com`) where your Cloud Run service is serving. No code changes are needed.

For each VPC network in a project, follow these steps to block outbound traffic except for traffic to the restricted VIP range:

  1. Enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) on the subnets hosting your VPC network resources.

  2. [Configure firewall rules](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configure-firewall) to prevent data from leaving the VPC network:

**Caution:** Failure to correctly configure firewall rules could leave your services vulnerable to data exfiltration.
     * Create a deny egress rule that blocks all outbound traffic.

**Note:** Make sure that the deny all egress firewall rule has a priority after 1000\. Otherwise, traffic from Direct VPC egress or the Serverless VPC Access connector to your service is blocked.
     * Create an allow egress rule that permits traffic to `199.36.153.4/30` on TCP port 443. Make sure that it has a priority _before_ the deny egress rule you just created—this allows egress only to the restricted VIP range.

  3. Create a Cloud DNS [response policy](https://docs.cloud.google.com/dns/docs/key-terms#response-policy).
         
         gcloud dns response-policies create RESPONSE_POLICY \
         --networks=NETWORK \
         --description=DESCRIPTION
         

Replace the following:

     * `RESPONSE_POLICY`: a name for your response policy.
     * `NETWORK`: the name of the network to associate with this policy. To specify multiple networks, separate the names of each network by commas, for example: `network1,network2`.
     * `DESCRIPTION`: a description of the response policy, such as `Cloud Run VPC Service Controls response policy`
  4. Add a rule to the response policy to resolve `*.googleapis.com` to `restricted.googleapis.com`. The IP address range for `restricted.googleapis.com` is `199.36.153.4/30`.
         
         gcloud dns response-policies rules create RESPONSE_POLICY_RULE \
         --response-policy=RESPONSE_POLICY \
         --dns-name="*.googleapis.com." \
         --local-data=name="restricted.googleapis.com.",type="A",ttl=300,rrdatas="199.36.153.4|199.36.153.5|199.36.153.6|199.36.153.7"
         

Replace the following:

     * `RESPONSE_POLICY_RULE`: a name for your response policy rule.
     * `RESPONSE_POLICY`: the name of the response policy that you created in the previous step, in quotes.
  5. Add a rule to the response policy to resolve `*.run.app` (or `*.cloudfunctions.net` if you created your function using `gcloud functions deploy`) to the `restricted.googleapis.com`. The IP address range for `restricted.googleapis.com` is `199.36.153.4/30`.
         
         gcloud dns response-policies rules create RESPONSE_POLICY_RULE \
         --response-policy=RESPONSE_POLICY \
         --dns-name="*.run.app." \
         --local-data=name="restricted.googleapis.com.",type="A",ttl=300,rrdatas="199.36.153.4|199.36.153.5|199.36.153.6|199.36.153.7"
         

Replace the following:

     * `RESPONSE_POLICY_RULE`: a name for your response policy rule.
     * `RESPONSE_POLICY`: the name of the response policy that you specified in the previous step, in quotes.



At this point, requests originating from within the VPC network:

  * Are not able to leave the VPC network, preventing egress outside the service perimeter.
  * Can only reach Google APIs and services that check VPC Service Controls, preventing exfiltration through Google APIs.



### Deploy VPC Service Controls-compliant Cloud Run services and jobs

After VPC Service Controls is configured for Cloud Run, make sure that all Cloud Run services and jobs deployed within the service perimeter enable VPC Service Controls. This requires the following:

  * **Cloud Run services and jobs must use Direct VPC egress or a Serverless VPC Access connector.** See [Connecting to a VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) for more information.
  * **Cloud Run services and jobs must route all outgoing traffic through the VPC network.** See [Egress settings](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#egress) for more information.
  * **Cloud Run services must allow traffic from internal sources only.** See [Ingress settings](https://docs.cloud.google.com/run/docs/securing/ingress) for more information. Setting ingress to "all" disables VPC Service Controls enforcement.



#### Audit existing services for VPC Service Controls compliance

After setting up VPC Service Controls, new services created in projects within the service perimeter are automatically checked for compliance. However, to avoid disruption of existing workloads, existing services continue to work and might not comply with organization policies.

Google recommends that you periodically audit your services to make sure your ingress and egress settings conform with the requirements, and update or redeploy services as necessary. For example, you could create a script that uses the Cloud Run Admin API to list your services and highlight those that do not specify the proper network settings.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
