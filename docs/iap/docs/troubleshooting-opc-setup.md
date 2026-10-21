---
url: https://docs.cloud.google.com/iap/docs/troubleshooting-opc-setup/
title: Troubleshooting your on-premises connector setup \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:51.182089+00:00
---

# Troubleshooting your on-premises connector setup  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/troubleshooting-opc-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)



Send feedback 

#  Troubleshooting your on-premises connector setup Stay organized with collections  Save and categorize content based on your preferences. 

This page provides step-by-step instructions to help you troubleshoot your IAP On-premises Connector configuration. For additional troubleshooting information, see [Cloud Service Mesh debugging](https://docs.cloud.google.com/service-mesh/docs/troubleshooting).

## Troubleshooting error 500 issues

Following are various issues and possible solutions to help you resolve a 500 error that you receive when attempting to access your application.

**The on-premises application is not connected to the Google Cloud network**

Your on-premises application might not be connected to the Google Cloud network. Verify connectivity by pinging the on-premises application from one of the on-premises connector Compute Engine instances. If the on-premises connector endpoint is unreachable, debug the network connectivity and settings before continuing. 

**Envoy is not properly installed in the VMs**

Complete the following steps to verify that Envoy is properly installed:

  1. Log on to one of the Compute Engine VMs from the on-premises connector. The on-premises connector VM name starts with `opc-on-prem-app-deployment-ig-${app}`.
  2. In the Cloud console, verify that the `opc-on-prem-app-deployment-gclb-urlmap` load balancing backend service health checks are green.
  3. If the backend service does not show up as healthy, SSH into one of the instances: 
         
         gcloud compute ssh INSTANCE_NAME --zone=ZONE_NAME

  4. Verify that Envoy is up and running, by issuing the following command: 
         
         ps aux | grep envoy
         

There should be more than one process running, other than the `grep envoy`. 

An example output:
         
         envoy      943  0.0  0.0   5488  3076 ?        Ss   06:25   0:00 /bin/bash /usr/local/bin/run-proxy.sh
         envoy      944  0.1  1.5 178928 57352 ?        Sl   06:25   1:23 /usr/local/bin/envoy --config-path /usr/local/etc/
         envoy/envoy-proxy-bootstrap.json --allow-unknown-static-fields --disable-hot-restart --log-level info --drain-time-
         s 60
         

  5. Verify that the Envoy log directory is created at `/var/log/envoy/`.

  6. Ensure the gce-mesh bucket is reachable by the VMs, by issuing the following command: 
         
         gcloud storage cp gs://gce-mesh/service-proxy-agent/releases/service-proxy-agent-0.2.tgz .




If any of the validations in this step failed, Envoy is not properly installed. Review the startup logs at `/var/log/daemon.log` for more information.

If you've observed that Envoy isn't running from the earlier steps, one of the reasons could be VPC Service Controls. The start-up script in the VMs downloads the Envoy image from the `gce-mesh` bucket. If the VPC Service Controls rules don't allow the connection, the on-premises connector deployment will not work.

To ensure Envoy installs correctly, allow access to the `gce-mesh` storage bucket in VPC Service Controls in the host project. Also, ensure the VPC has a routing rule to allow traffic to the public internet. This allows Envoy to be deployed. For more information, see [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).

**Your on-premises application is not connected to Envoy**

If you can ping the on-premises application from the VM but cannot use the on-premises connector, it's possible that Envoy cannot connect to the application.

To verify that Envoy can connect to your on-premises application, try making a call to Envoy from the machine where Envoy is running. Using SSH,connect to the VM `opc-on-prem-app-deployment-ig-${app}` and run the following command. You can find the Envoy port number in **Instance Groups > Details > Port Name Mapping**. 
    
    
    curl -x -v localhost:${envoy_port}

If the endpoint is not reachable, check the following:

  * `/var/log/envoy/envoy.err.log` for any error logs. If there are no error logs, check if Cloud Service Mesh is enabled and is able to configure Envoy, by running the following command: 
        
        sudo curl 0.0.0.0:15000/config_dump 

  * Verify that `TRAFFICDIRECTOR_INTERCEPTION_LISTENER` is set. If `TRAFFICDIRECTOR_INTERCEPTION_LISTENER` is not set, Cloud Service Mesh could not configure Envoy.
  * Check for any error messages in each listener.



**The Envoy and Cloud Service Mesh account permissions aren't set**

If you see the `GRPC 403` error in the `envoy.err.log` or if you do not see `TRAFFICDIRECTOR_INTERCEPTION_LISTENER` in the Envoy configuration, you might not have the correct account permissions set.

Verify that the VM service account has `TD` access permissions for `xDS v3`:

  * Verify the permissions: [Prepare to set up Cloud Service Mesh with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-for-envoy-setup#grant-permissions)
  * Verify the account: [Enable the service account](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-for-envoy-setup#enable-service-account)



## Troubleshooting `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` errors

If the browser shows the error `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` without redirecting to the login page, verify the status of the certificates on the Google Cloud load balancer details page.

Note that provisioning a Google-managed certificate might take up to 60 minutes.

## Troubleshooting Envoy installation issue

If the on-premises connector is deployed successfully and the certificate has been provisioned, but the connection is still failing, this might indicate that Envoy might not be installed correctly on the VMs.

To verify if that Envoy is installed, SSH to one of the VMs and run the following command:

  * ps aux | grep envoy 

There should be more than one process running, other than the `grep envoy`.
  * netstat -tlpn 

The Envoy admin port 127.0.0.1:15000 should be listening.



If any of the previous actions fail, take the following actions to mitigate the issue:

  1. Make sure [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) is enabled on the subnet the connector is being deployed.
  2. Make sure [VM Manager (OS Config API)](https://console.cloud.google.com/marketplace/product/google/osconfig.googleapis.com) is enabled.



## Troubleshooting Deployment Failure on IamMemberBinding Resources

If the on-premises connector is being deployed or updated and encounters a `PERMISSION_DENIED` error related to `IamMemberBinding` resources, it may be because the `Google APIs Service Agent` Service Account has not been granted the `OWNER` role as required when [enabling IAP for on-premises apps](https://docs.cloud.google.com/iap/docs/enabling-on-prem-howto).

Example Deployment Errors:
    
    
    bind-iam-policy: {"ResourceType":"gcp-types/cloudresourcemanager-v1:virtual.projects.iamMemberBinding","ResourceErrorCode":"403","ResourceErrorMessage":{"code":403,"message":"Policy update access denied.","status":"PERMISSION_DENIED","statusMessage":"Forbidden","requestPath":"https://cloudresourcemanager.googleapis.com/v1/projects/<project-ID>:setIamPolicy","httpMethod":"POST"}}
    
    
    
    bind-storage-admin-account-iam-policy: {"ResourceType":"gcp-types/cloudresourcemanager-v1:virtual.projects.iamMemberBinding","ResourceErrorCode":"403","ResourceErrorMessage":{"code":403,"message":"Policy update access denied.","status":"PERMISSION_DENIED","statusMessage":"Forbidden","requestPath":"https://cloudresourcemanager.googleapis.com/v1/projects/<project-ID>:setIamPolicy","httpMethod":"POST"}}
    

If you are seeing these errors with the deployment, verify the `Google APIs Service Agent` Service Account is granted the `OWNER` role and retry.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
