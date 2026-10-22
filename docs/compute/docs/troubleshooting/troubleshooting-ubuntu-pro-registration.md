---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ubuntu-pro-registration/
title: Troubleshooting Ubuntu Pro Registration \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:45.890940+00:00
---

# Troubleshooting Ubuntu Pro Registration  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ubuntu-pro-registration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting Ubuntu Pro Registration Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

Occasionally, Compute Engine fails to register PAYG Ubuntu Pro licenses automatically. This document describes how to resolve issues you might encounter with registering Compute Engine virtual machine (VM) instances running pay-as-you-go (PAYG) Ubuntu Pro licenses.

## Check registration status

To check if your license is registered, connect to the VM and run the following command
    
    
    sudo ua status
    

If the registration succeeded, you see output similar to the following and no further action is required:
    
    
    SERVICE          ENTITLED  STATUS    DESCRIPTION
    cc-eal           yes       disabled  Common Criteria EAL2 Provisioning Packages
    cis              yes       disabled  Security compliance and audit tools
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    fips             yes       disabled  NIST-certified core packages
    fips-updates     yes       disabled  NIST-certified core packages with priority security updates
    livepatch        yes       enabled   Canonical Livepatch service
    

If the registration failed and Ubuntu Pro isn't registered, you see a message similar to the following:
    
    
    This machine is not attached to an Ubuntu Pro subscription.
    

## Manually register license

If Compute Engine failed to automatically register you Ubuntu pro license, you can manually register the license by running the following command:
    
    
    sudo pro auto-attach
    

The output is similar to the following:

  * **Registration success** :
        
        This machine is already attached to PROJECT_ID
        To use a different subscription first run: sudo pro detach.
        

  * **Registration failure** :
        
        Internal Server Error
        




## Troubleshoot license registration

If you were unable to manually register a Ubuntu Pro license, resolve the issue by doing the following:

  1. Verify that the VM can reach the metadata server by running the following command to check the number of disks attached to the VM:
         
         curl "http://metadata.google.internal/computeMetadata/v1/instance/disks/" -H "Metadata-Flavor: Google"
         

The output is similar to the following, which shows the number of disks attached to the VM:
         
         0/
         1/
         2/
         

If the output doesn't show the number of disks attached to the VM, see [Troubleshooting metadata server access issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-metadata-server).

  2. Verify the Google guest agent is running by running the following command:
         
         systemctl status google-guest-agent.service
         

The output is similar to the following:
         
         ● google-guest-agent.service - Google Compute Engine Guest Agent
         Loaded: loaded (/lib/systemd/system/google-guest-agent.service; enabled;
         vendor preset: enabled)
         Active: active (running) since Thu 2023-04-20 16:35:11 PDT; 2h 12min ago
         Main PID: 4582 (google_guest_ag)
         Tasks: 10 (limit: 9525)
         

If the guest agent is not installed or failed, [install or reinstall the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment).

  3. Verify that a Service account is attached to the VM, by running the following command from your local workstation:
         
         gcloud compute instances describe VM_NAME \
            --zone ZONE --format="table(serviceAccounts.email)"
         

Replace the following:

     * `VM_NAME`: the name of the VM
     * `ZONE`: the zone where the VM is located

The output is similar to the following:
    
    EMAIL: ['XXXXXXXX-compute@developer.gserviceaccount.com']
    

Note the email of the service account.

  4. Check if the service account is enabled by running the following query:
         
         gcloud logging read --freshness=90d "SERVICE_ACCOUNT_EMAIL protoPayload.methodName=google.iam.admin.v1.DisableServiceAccount"
         

Replace `SERVICE_ACCOUNT_EMAIL` with the email address associated with the VM's service account.

The output is similar to the following:
         
         insertId: 1ne5thkf13sxec
         logName: projects/testproject/logs/cloudaudit.googleapis.com%2Factivity
         protoPayload:
          '@type': type.googleapis.com/google.cloud.audit.AuditLog
         authenticationInfo:
         principalEmail: principalemail@google.com
         principalSubject: user:pricipalemail@google.com
         authorizationInfo:
          granted: true
         permission: iam.serviceAccounts.disable
         resource: projects/-/serviceAccounts/XXXXXXXXXXXXXX
         resourceAttributes:
           name: projects/-/serviceAccounts/XXXXXXXXXXXXXXXX
         methodName: google.iam.admin.v1.DisableServiceAccount
         request:
         '@type': type.googleapis.com/google.iam.admin.v1.DisableServiceAccountRequest
         name: projects/testproject/serviceAccounts/-compute@developer.gserviceaccount.com
         requestMetadata:
          destinationAttributes: {}
          requestAttributes:
            auth: {}
            time: '2024-01-25T21:37:55.748811275Z'
         resourceName: projects/-/serviceAccounts/XXXXXXXXXX
         response:
          '@type': type.googleapis.com/google.protobuf.Empty
          serviceName: iam.googleapis.com
          status: {}
         receiveTimestamp: '2024-01-25T21:37:56.409675900Z'
         resource:
         labels:
          email_id: -compute@developer.gserviceaccount.com
          project_id: testproject
          unique_id: 'XXXXXXXXXXXXXXXX'
         type: service_account
         severity: NOTICE
         timestamp: '2024-01-25T21:37:55.721215307Z'
         

If the service account isn't enabled, [re-enable it](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#enabling).




After you have re-enabled the service account, try to register the license by following the instructions in the manually register license section of this document.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
