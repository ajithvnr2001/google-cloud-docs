---
url: https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc/
title: Configure VPC Service Controls \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:56.473481+00:00
---

# Configure VPC Service Controls  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 3 Guides ](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

**Managed Airflow (Gen 3)** | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc "View this page for Managed Airflow \(Gen 2\)") | [Managed Airflow (Legacy Gen 1)](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc "View this page for Managed Airflow \(Legacy Gen 1\)")

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) enable organizations to define a perimeter around Google Cloud resources to mitigate data exfiltration risks.

Managed Airflow environments can be deployed within a service perimeter. By configuring your environment with VPC Service Controls, you can keep sensitive data private while taking advantage of the fully-managed workflow orchestration capabilities of Managed Airflow.

VPC Service Controls support for Managed Airflow means that:

  * Managed Airflow can now be selected as a secured service inside a VPC Service Controls perimeter.
  * All underlying resources used by Managed Airflow are configured to support VPC Service Controls architecture and follow its rules.



Deploying Managed Airflow environments with VPC Service Controls gives you:

  * Reduced risk of data exfiltration.
  * Protection against data exposure due to misconfigured access controls.
  * Reduced risk of malicious users copying data to unauthorized Google Cloud resources, or external attackers accessing Google Cloud resources from the internet.



## About VPC Service Controls in Managed Airflow

  * All VPC Service Controls network constraints also apply to your Managed Airflow environments. See the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for details.


  * If a Managed Airflow environment is protected by a perimeter, access to public PyPI repositories is restricted. See the Install PyPI packages in VPC Service Controls for more information.

  * If your environment uses [Private IP networking](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type), **all internal traffic is routed to your VPC network** , except the traffic to Google APIs, services, and domains that [are available to Private IP environments](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#about-networking-type) through Private Google Access.

  * Depending on how you configure your VPC network, a Private IP environment **can gain access to the internet through you VPC network**.

  * Managed Airflow doesn't support using [third-party identities](https://docs.cloud.google.com/composer/docs/composer-3/access-environments-with-workforce-identity-federation) in ingress and egress rules to allow [Apache Airflow UI](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface) operations. However, you can use the `ANY_IDENTITY` identity type in ingress and egress rules to allow access to all identities, including third-party identities. For more information about the `ANY_IDENTITY` identity type, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

  * In VPC Service Controls mode, access to web server is protected by the perimeter and access from outside of the perimeter is blocked. To allow access from outside the service perimeter, configure [access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) or [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) as required. In addition, you can [restrict access to web server to specific IP ranges](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#network-access-controls).




## About connectivity to Google APIs and services in VPC Service Controls

Managed Airflow (Gen 3) routes traffic to Google services through `restricted.googleapis.com`, which enables access to Google APIs, services, and domains supported by this range.

**Caution:** If your environment is [attached to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network), all internal traffic that isn't routed to `restricted.googleapis.com` **is routed to the VPC network**. Depending on how you configure your VPC network, your environment **can gain access to the internet through you VPC network**.

For more information and the list of services and domains available through `restricted.googleapis.com`, see [Network configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid#config-choose-domain) in the Virtual Private Cloud documentation.

Managed Airflow (Gen 3) environments **block calls** to Google APIs, services, and domains that aren't in the list of required APIs and services. If you want to call an API from a DAG:

  1. Make sure that the service [supports VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).
  2. Add the service to restricted services.
  3. Add the service to VPC accessible services.



For example, if you use a VertexAI Operator, add `aiplatform.googleapis.com` both to restricted services and to VPC accessible services.

For more information about adding services to a perimeter, see [Manage service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters) in the VPC Service Controls documentation.

In Managed Airflow (Gen 3), services that don't [support VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products) and aren't available through `restricted.googleapis.com` **can't be accessed** from environments protected with VPC Service Controls. This restriction was added in Managed Airflow (Gen 3) to enhance environment's security. While Managed Airflow (Gen 2) allows configuring access to such unsupported services, we strongly recommend to avoid doing so in any environment protected by VPC Service Controls.

## Perimeters for environments with Shared VPC and CMEK

If your environment is protected by a service perimeter and uses [Shared VPC](https://docs.cloud.google.com/composer/docs/composer-3/configure-shared-vpc), [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/composer/docs/composer-3/configure-cmek-encryption), or both, then make sure that the following projects are located in the **same service perimeter** :

  * Service project: The project that contains the Managed Airflow environment.
  * Host project: The project that contains the Shared VPC network.
  * Project that hosts the Cloud Key Management Service keys.

**Important:** Perimeter misalignment between these projects can block critical database management operations and cause environment creation or update failures.

## Create environments in a perimeter

The following steps are required to deploy Managed Airflow inside a perimeter:

  1. Enable **Access Context Manager API** and **Cloud Composer API** for your project. See [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for reference.

  2. Create a perimeter by following the [perimeter configuration instructions](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#create-perimeter) in the VPC Service Controls documentation. Make sure that the list of services protected by the perimeter includes all services used by Managed Airflow, in addition to other services that you want to restrict:

     * Cloud Composer API (composer.googleapis.com)
     * Artifact Registry API (artifactregistry.googleapis.com)
     * Compute Engine API (compute.googleapis.com)
     * Kubernetes Engine API (container.googleapis.com)
     * Container File System API (containerfilesystem.googleapis.com)
     * Cloud DNS API (dns.googleapis.com)
     * Backup for GKE API (gkebackup.googleapis.com)
     * Service Account Credentials API (iamcredentials.googleapis.com)
     * Cloud Logging API (logging.googleapis.com)
     * Cloud Monitoring API (monitoring.googleapis.com)
     * Cloud Pub/Sub API (pubsub.googleapis.com)
     * Cloud SQL Admin API (sqladmin.googleapis.com)
     * Cloud Storage API (storage.googleapis.com)

     * For all other services used by your DAGs:

       1. Add the service to restricted services.
       2. Add the service to VPC accessible services.
  3. If your service perimeter restricts API access using [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services), make sure that the list of allowed services includes all services used by Managed Airflow.

  4. Create a new Managed Airflow environment:

     1. Use Google Cloud CLI to create your environment.
     2. Enable Private IP with the `--enable-private-environment` argument.
     3. Specify access parameters for the web server with `--web-server-allow-all`, `--web-server-allow-ip`, or `--web-server-deny-all` arguments. For more information about using these arguments, see [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments#web-server-access). To improve protection, only allow access to the web server from specific IP ranges. 
     4. Disallow the installation of packages from public internet repositories with the `--enable-private-builds-only` argument.

Example:
            
            gcloud composer environments create example-environment \
              --location us-central1 \
              --enable-private-environment \
              --web-server-allow-all \
              --enable-private-builds-only
            

  5. By default, access to Airflow UI and API is only allowed from within the security perimeter. If you want to make it available outside of the security perimeter, then configure [access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) or [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

  6. By default, your environment can't access resources outside the perimeter, even if a corresponding API is added to the list of VPC accessible services. To allow access to resources outside the perimeter, configure a [perimeter bridge](https://docs.cloud.google.com/vpc-service-controls/docs/create-perimeter-bridges), [egress and ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules), or move the resources to the same perimeter.

For example, suppose you have a Cloud KMS key in perimeter A and a Managed Airflow environment in perimeter B. Even if you allow the Cloud Key Management Service API in perimeter B using VPC accessible services, your environment still can't access the key. You must also configure communication across the perimeter boundary.




## Add an existing environment to the perimeter

You can add the project containing your environment to a perimeter if your environments use Private IP and the installation of PyPI packages from public repositories is disabled.

To update an existing Managed Airflow (Gen 3) environment to this configuration:

  1. Make sure that you already created or configured the perimeter as described in the previous section.
  2. Use Google Cloud CLI to update your environment.
  3. Enable Private IP with the `--enable-private-environment` argument.
  4. Disallow the installation of packages from public internet repositories with the `--enable-private-builds-only` argument.
  5. If required, [configure access to the Airflow web server](https://docs.cloud.google.com/composer/docs/composer-3/access-airflow-web-interface#network-access-controls). To improve protection, only allow access to the web server from specific IP ranges. 



Example:
    
    
    gcloud composer environments update example-environment \
      --location us-central1 \
      --enable-private-environment \
      --enable-private-builds-only
    

## Install PyPI packages in VPC Service Controls

In the default VPC Service Controls configuration, Managed Airflow only supports installing PyPI packages from private repositories that are reachable from the internal IP address space of the VPC network.

All Managed Airflow environments within a VPC Service Controls perimeter don't have access to public PyPI repositories by default.

### Install from a private repository

The recommended configuration is to set up a private PyPI repository:

  1. Populate it with vetted packages used by your organization, then configure Managed Airflow to [install Python dependencies from a private repository](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-private-repo).




### Install from a public repository

**Caution:** When using this setup, make sure that you understand the **risks of using external repositories**. Be sure that you trust the content and integrity of any external repositories, because these connections can potentially be used as an exfiltration vector.

To install PyPI packages from an external repository:

  1. Create an [Artifact Registry remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).
  2. Grant this repository [access to upstream sources](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo#vpc).
  3. Configure Airflow to [install packages from an Artifact Registry repository](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-ar-repo).



## VPC Service Controls logs

When troubleshooting environment creation issues, you can analyze audit logs generated by VPC Service Controls.

In addition to other log messages, you can check logs for information about `cloud-airflow-prod@system.gserviceaccount.com` and `service-PROJECT_ID@cloudcomposer-accounts.iam.gserviceaccount.com` service accounts that configure components of your environments.

Managed Airflow service uses the `cloud-airflow-prod@system.gserviceaccount.com` service account to manage [tenant project components](https://docs.cloud.google.com/composer/docs/composer-3/environment-architecture#about-customer-tenant) of your environments.

The `service-PROJECT_ID@cloudcomposer-accounts.iam.gserviceaccount.com` service account, also known as Composer Service Agent Service Account manages environment components in [service and host projects](https://docs.cloud.google.com/composer/docs/composer-3/configure-shared-vpc#shared-vpc-guidelines).

## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-3/create-environments)
  * [Install PyPI packages](https://docs.cloud.google.com/composer/docs/composer-3/install-python-dependencies#install-private-repo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
