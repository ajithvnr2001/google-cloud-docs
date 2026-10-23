---
url: https://docs.cloud.google.com/looker/docs/looker-core-psc-migration/
title: Migrating Private Service Connect connections to the new service attachment URI \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:34.899051+00:00
---

# Migrating Private Service Connect connections to the new service attachment URI  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-psc-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Migrating Private Service Connect connections to the new service attachment URI Stay organized with collections  Save and categorize content based on your preferences. 

Recently Looker (Google Cloud core) released a new type of service attachment URI that facilitates [global access](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#using_global_access) and [Google-managed certificates with custom domains](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-google-managed-certs).

This page provides a step-by-step guide for migrating your existing Private Service Connect endpoints or backends to the new service attachment URI for Looker (Google Cloud core).

If your Looker (Google Cloud core) instance was created before the enhanced service attachments were introduced, your instance will likely need to undergo this migration to use global access and Google-managed certificates. [Check the Looker (Google Cloud core) backend](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration#identifying_your_service_attachment_uri) to determine if you need to migrate the instance.

## Before you begin

This guide assumes that you have an existing Looker (Google Cloud core) instance with a private IP configuration that uses Private Service Connect.

To identify which type of service attachment your instance is using, you must have the [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`) Identity and Access Management (IAM) role.

See the Private Service Connect documentation for [endpoints](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#begin) or [backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls#roles) to determine which IAM role or roles you need to create or view Private Service Connect endpoints or configure Cloud DNS for endpoints.

## Identifying your service attachment URI

First, you need to identify which type of service attachment your instance is using.

  1. In the Google Google Cloud console, go to the **Instances** page for Looker (Google Cloud core).
  2. Click the name of your instance to open its **Details** page.
  3. In the **Instance details** section, look for the **Looker Service Attachment URI**.

     * If the URI contains **`...looker-psc-gateway-HASHSTRING`** and is in the format `projects/TENANT_PROJECT/regions/REGION/serviceAttachments/looker-psc-gateway-HASHSTRING`, you're already using the new enhanced service attachment and no further action is needed.
     * If the URI contains **`...looker-psc-HASHSTRING`** and is in the format `projects/TENANT_PROJECT/regions/REGION/serviceAttachments/looker-psc-HASHSTRING`, you are using the legacy backend and should migrate.



## Migration steps

To migrate your PSC endpoints, you will create a new Private Service Connect endpoint that points to the new service attachment URI and then update your network configuration to use the new endpoint.

### Get the new service attachment URI

If the Looker (Google Cloud core) instance isn't using the Gateway backend, the new service attachment URI isn't displayed in the Google Cloud console. However, you can construct it by replacing `looker-psc` with `looker-psc-gateway` in your existing URI.

Your old URI may look like the following example:

`projects/t4dd1c6219b22b382p-tp/regions/us-central1/serviceAttachments/looker-psc-2a94bb22-9b8a-4b62-9262-2337a47d15ed`

In that case, your new URI would look like this:

`projects/t4dd1c6219b22b382p-tp/regions/us-central1/serviceAttachments/looker-psc-gateway-2a94bb22-9b8a-4b62-9262-2337a47d15ed`

### Private Service Connect endpoint

To migrate an existing Private Service Connect endpoint, follow these steps:

  1. **Create a new Private Service Connect endpoint:** Identify your existing northbound connections by reviewing the **Allowed VPCs** field in the Google Cloud console. For each allowed Virtual Private Cloud (VPC), create a [new Private Service Connect endpoint](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#northbound_access_to_your_instance) that targets the service attachment URI created in the previous section.

  2. **Create a[private Cloud DNS zone](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-google-managed-certs#dns_configuration_steps) for the `*.private.looker.app` domain.**

  3. **Test the new endpoint:** After you create the endpoint, verify connectivity to your Looker (Google Cloud core) instance. Run a `curl` command from a VM located in the same VPC network, targeting your specific `*.private.looker.app` domain (for example, `my-instance.private.looker.app`).

     1. From a VM in your VPC network, run the following `curl` command:
            
            curl -v https://your_looker_custom_domain.private.looker.app \
                --resolve your_looker_custom_domain.private.looker.app:443:psc_endpoint_ip_address
            

Replace the following:

        * `<your_looker_custom_domain.private.looker.app>`: the actual custom domain for your Looker instance.
        * `<psc_endpoint_ip_address>`: the internal IP address of the PSC endpoint in your VPC.
     2. If the `curl` command returns a `200` status code, the new endpoint is working correctly.




### Private Service Connect backend

The recommended configuration for Looker (Google Cloud core) uses an Internal Application Load Balancer with a Private Service Connect network endpoint group (NEG) backend. This architecture supports custom domains and provides TLS termination for private connections.

To migrate an existing Private Service Connect NEG to one created with an enhanced service attachment, you must first [create a new Private Service Connect NEG](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends) that targets the enhanced service attachment. Once the NEG is created, update your load balancer configuration as follows:

  1. In the Google Cloud console, go to the **Load balancing** page.
  2. Click the name of your load balancer and click **Edit**.
  3. Navigate to **Backend configuration** and select the backend service that's associated with your Looker (Google Cloud core) instance.
  4. Click **Edit backend service**.
  5. In the **Backends** section, select the new enhanced Private Service Connect NEG from the drop-down menu to replace the existing Private Service Connect NEG.
  6. Click **Done**
  7. Click **Update**.



### Test the new endpoint

The Internal Application Load Balancer update that you made targeted the backend service for the enhanced service attachment. Consequently, the frontend configuration—including the IP address, Cloud DNS, and certificates—remains unchanged. Users can now validate the setup by accessing the Looker (Google Cloud core) instance using a browser.

## What's next

After migrating your instance's Private Service Connect endpoints, you can take advantage of the following new features:

  * [**Global access**](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview#using_global_access): Create PSC endpoints in any region, regardless of where your Looker (Google Cloud core) instance is located.
  * [**Google-managed certificates**](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-google-managed-certs): Use the `*.private.looker.app` domain for your custom domain, and let Google manage the SSL certificate.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
