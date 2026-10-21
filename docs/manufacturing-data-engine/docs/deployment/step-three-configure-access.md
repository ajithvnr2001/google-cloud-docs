---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access/
title: Step 3: Configure access \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:40.778591+00:00
---

# Step 3: Configure access  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Step 3: Configure access

This section provides guidance on different ways to grant access to your MDE deployment, depending on your needs.

### SSH tunneling over IAP

To connect to the private IPs of the MDE services, you can use an SSH tunnel to a proxy VM. This approach lets you use local tools like Postman for interacting with the MDE APIs.

The standard MDE deployment creates a proxy VM called `mde-proxy`. This machine can proxy incoming requests to the MDE API gateway or MDE web interface. This VM only has a private IP, but IAP lets you to create a secure SSH tunnel to this machine using [Identity-Aware Proxy (IAP) for TCP forwarding](https://docs.cloud.google.com/iap/docs/tcp-forwarding-overview). The rest of this section explains how to configure IAP for tunneling traffic to the `mde-proxy`, and how to create a tunnel to it from your workstation:

  1. In the Google Cloud console, go to the [IAP](https://console.cloud.google.com/security/iap) and click **Enable API**. This operation may take several minutes to complete.

  2. In the Google Cloud console, go to the [IAP](https://console.cloud.google.com/security/iap) and click **SSH AND TCP RESOURCES**.

  3. Grant permission to users who are authorized to use IAP to connect to `mde-proxy` over IAP:

Before users can use IAP to connect to `mde-proxy`, grant them the `roles/iap.tunnelResourceAccessor` [role](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#grant-permission) with the following instructions:

     1. Select **mde-proxy** from the list.

**Note:** You can expect to see a warning message next to the mde-proxy resource. This is expected and doesn't pose a problem. IAP does have access to the mde-proxy through a firewall rule that uses network tags.
     2. Click **Add Principal** in the right side panel.

     3. Type the email of the principal you want to grant access.

     4. Select the `IAP-secured Tunnel User` role.

  4. Create a tunnel to the MDE API using the following command:

**Note:** SSH tunneling in Cloud Shell requires an additional `-4` flag with the `gcloud compute ssh` command to force it using IPv4.
         
         export MDE_PROXY_ZONE=$(gcloud compute instances list --filter="mde-proxy"  \
         --format="value(zone)")
         
         gcloud compute ssh mde-proxy \
         --zone "$MDE_PROXY_ZONE" --tunnel-through-iap  \
         -- -N -L 8080:api.mde.cloud.google.com:80
         

After running the command, the MDE APIs are accessible under `http://localhost:8080`.

  5. Create a tunnel to the MDE web interface.

If you created a tunnel to the MDE API in Step 3, you can open a new terminal to execute the commands later. The SSH tunnels to the MDE API and MDE web interface can run in parallel.
         
         export MDE_PROXY_ZONE=$(gcloud compute instances list --filter="mde-proxy" \
         --format="value(zone)")
         
         gcloud compute ssh mde-proxy \
         --zone "$MDE_PROXY_ZONE" --tunnel-through-iap  \
         -- -N -L 8081:ui.mde.cloud.google.com:80
         

After running the command, the MDE web interface is accessible under `http://localhost:8081`.




### Configure Identity-Aware Proxy

Identity-Aware Proxy (IAP) lets you securely connect to the internal IPs of the MDE API and web interface, as well as to restrict external access the MDE web interface to only authorized users if you deployed it with the External Load Balancer option.

**Note:** If your client has access to the Virtual Private Cloud (VPC) in which MDE is deployed (for example, over Cloud Interconnect), you can skip this section.

To use IAP, you must first enable the IAP service API (if you haven't done it already) and configure the OAuth screen:

  1. In the Google Cloud console, go to the [IAP](https://console.cloud.google.com/security/iap) and click **Enable API**. This operation may take several minutes to complete.

  2. Configure the OAuth consent screen for IAP:

     1. In the Google Cloud console, go to the [Google Auth Platform](https://console.cloud.google.com/auth/overview) page and select the MDE deployment project if prompted.
     2. On the Overview page, click **Get started**.
     3. Enter the **Application name** you want to display, for example `MDE`.
     4. Add your email as **User support email** and click **Next**.
     5. For audience, select **External** and click **Next**.
     6. Add your email as **Contact information** and click **Next**.
     7. Read and agree to the Google API Services User Data Policy, click **Continue**.
     8. Click **Create**.



### Configure access to the web interface External HTTP Load Balancer

In this section, you will configure access to the MDE web interface External HTTP Load Balancer using IAP.

**Note:** If you didn't deploy MDE with the web interface option enabled, you can skip this section.

If you enabled the External HTTP Load balancer for the MDE web interface, you must use IAP to restrict access to the application to only authorized users.

#### Before you begin

Make sure you complete the following prerequisites:

  * You deployed MDE with the MDE web interface.
  * You deployed the MDE web interface with an External HTTP Load Balancer.
  * You completed the [general IAP configuration](https://docs.cloud.google.com/manufacturing-data-engine/docs/deployment/step-three-configure-access#configure-Identity-Aware%20Proxy) steps.



#### Steps

  1. In the Google Cloud console, go to the [IAP](https://console.cloud.google.com/security/iap) page.

  2. Locate the resource corresponding to the external UI service (look for `mde-ui-ext-service`).

**Note:** You can expect to see an error message next to the `mde/mde-ui-int-service` resource. This is expected behavior, and isn't a problem. IAP does have access to the `mde/mde-ui-ext-service`.
  3. In the **IAP** column for that resource, toggle the switch to **Enabled**.

  4. In the confirmation dialog, read and accept the configuration requirements, then click **Turn On**.

  5. Once activated, select the checkbox next to the resource name (`mde-ui-ext-service`).

  6. In the right side panel, click **Add Principal**.

  7. Type the email address of the user or group you want to grant access to.

  8. In the **Role** drop-down, select **Cloud IAP > IAP-secured Web App User**.

  9. Click **Save**.




#### Cross-Organization Access (Optional)

By default, IAP uses Google-managed OAuth clients, which strictly restrict access to users within the same Google Cloud Organization as the project. If your deployment requires access from external users (partners using a different domain), you must use a **Custom OAuth client** configured with an **External** user type.

For more details, see the official Google Cloud documentation on [Using custom OAuth clients with IAP](https://cloud.google.com/iap/docs/custom-oauth-configuration) and [Enabling IAP for GKE](https://cloud.google.com/iap/docs/enabling-kubernetes-howto).

You can configure this using one of the following methods:

#### Method A: Direct Console Configuration (No GKE Secrets)

If your GKE `BackendConfig` does not manage IAP settings (meaning it does not have an `iap` block, allowing GKE Ingress to inherit existing settings), you can configure the custom client directly in the console:

  1. Go to the [IAP page](https://console.cloud.google.com/security/iap).
  2. For the `mde-ui-ext-service` resource, click **More options** (three dots) in the **Actions** column and select **Settings**.
  3. Select **Custom OAuth**.
  4. Click **Auto Generate Credentials** (or provide existing credentials if you created them manually in APIs & Services).
  5. Click **Save**.



#### Method B: GKE-Managed Configuration (Using Kubernetes Secrets)

If you prefer to manage IAP configuration using Kubernetes manifests (GitOps), you must store the credentials in a secret and reference it in your `BackendConfig`:

  1. Configure the **OAuth consent screen** as **External** and create **OAuth client credentials** manually under **APIs & Services > Credentials** (Web application type).
  2. Create a Kubernetes Secret in the cluster: `sh kubectl create secret generic iap-oauth-secret \ --namespace=mde \ --from-literal=client_id=YOUR_CLIENT_ID \ --from-literal=client_secret=YOUR_CLIENT_SECRET`
  3. Update the `BackendConfig` for your service to reference the secret: `yaml spec: iap: enabled: true oauthclientCredentials: secretName: iap-oauth-secret`



### Configure DNS for MDE web interface

If you enabled the External HTTP Load balancer for the MDE web interface, you must set the A record of the domain name you assigned to the variable `MDE_UI_DOMAIN_NAME` in `input.tfvars` to the IP address of the external HTTP load balancer that was deployed to finish provisioning the Google-managed SSL certificate.

You can look up the IP address of the external HTTP balancer with the following command:
    
    
    gcloud compute addresses list --filter="name~'.*mde-ui.*'" --format="value(address)" --global
    

Consult your DNS host for details on how to create an A record.

**Note:** While in most cases DNS changes propagate in less than an hour, it may take up to 24 hours. Your application won't be accessible under the domain name until DNS propagation completes and the subsequent provisioning of an SSL certificate succeeds.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
