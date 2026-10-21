---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-test-event-threat-detection/
title: Test Event Threat Detection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:04.752144+00:00
---

# Test Event Threat Detection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-test-event-threat-detection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Test Event Threat Detection Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Verify that Event Threat Detection is working by intentionally triggering the detectors, viewing the findings in Security Command Center or Cloud Logging, and then cleaning up the test resources.

Event Threat Detection is a built-in service that monitors your organization's Cloud Logging and Google Workspace logging streams and detects threats in near-real time. To learn more, read [Event Threat Detection overview](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).

## Before you begin

To test Event Threat Detection, verify the following prerequisites:

  * **Service enablement:** to view Event Threat Detection findings, the service must be enabled in Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings.
  * **IAM permissions:** depending on which detector you want to test, you must have one of the following roles: 
    * **IAM Anomalous Grant:** an Identity and Access Management (IAM) role with the `resourcemanager.projects.setIamPolicy` permission, like the Project IAM Admin role.
    * **Malware: Bad Domain:** an IAM role with the `compute.instances.create` and `dns.policies.create` permissions, like the Project Editor role.
    * **SSH Brute Force:** an IAM role with the `compute.instances.create` permission, like the Compute Instance Admin (v1) role or Project Editor role.



## Trigger test findings

To verify that Event Threat Detection generates findings, select one of the following detectors to trigger:

  * **IAM Anomalous Grant detector:** trigger this detector by granting a sensitive role to an external test user account.
  * **Malware: Bad Domain detector:** trigger this detector by executing a query to a test bad domain from a VM instance.
  * **SSH Brute Force detector:** trigger this detector by configuring a VM instance to stream system authentication logs. Then, simulate multiple failed SSH sign-in attempts, followed by a successful sign in.



### Trigger the IAM Anomalous Grant detector

To trigger the IAM Anomalous Grant detector, create an external test user and grant the Project Owner role:

  1. Create a test user with a personal `@gmail.com` email address. Make sure that this `@gmail.com` account doesn't already have any IAM permissions in the project where you are performing the test.

**Note:** This finding is only triggered for Security Command Center users with a `@gmail.com` email address.
  2. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Click **Grant access**.

  4. In the **New principals** field, enter the test user's `@gmail.com` address.

  5. In the **Select a role** drop-down list, select **Project > Owner**.

  6. Click **Save**.




### Trigger the Malware: Bad Domain detector

To trigger the Malware: Bad Domain detector, create a VM instance with DNS query logging enabled and then query a test domain:

  1. Create a VM instance on a VPC network. For instructions, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). Ensure that the project containing the VM instance is in scope for Event Threat Detection. That is, Event Threat Detection service is enabled for the project or its parent organization.
  2. To enable logging, configure a DNS server policy for the VPC network:

     1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns)

     2. Select the **DNS server policies** tab.

     3. Click **Create policy**.

     4. In the **Name** field, enter a name for the policy.

     5. Under **Logs** , select **On** to enable logging of DNS queries.

     6. Under **Networks** , select the VPC network that your VM instance uses.

     7. Click **Create**.

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. In the list of virtual machine instances, click **SSH** in the row of the VM instance you created. A terminal window opens on your VM instance.

  5. Run the following command:
         
         curl etd-malware-trigger.goog
         

**Note:** Cloud DNS logs this DNS request and triggers the finding because `etd-malware-trigger.goog` is a known test bad domain.



### Trigger the SSH Brute Force detector

To trigger the SSH Brute Force detector, configure authentication logging and simulate failed SSH sign-in attempts:

  1. Create a Linux VM instance (such as Debian) on a VPC network. For instructions, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). Ensure that the project containing the VM instance is in scope for Event Threat Detection.
  2. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. In the list of virtual machine instances, click **SSH** in the row of the VM instance you created. A terminal window opens on your VM instance.

  4. Enable SSH password authentication on the VM instance:

     1. Open the SSH daemon configuration file in a text editor:
            
            sudo vim /etc/ssh/sshd_config
            

     2. Set `PasswordAuthentication` to `yes`:
            
            PasswordAuthentication yes
            

     3. Restart the SSH service:
            
            sudo systemctl restart ssh
            

  5. Create a test user account with a password:
         
         sudo adduser TEST_USER
         

Follow the prompts to specify a password for the test user.

  6. To stream authentication logs to Cloud Logging, install the Ops Agent on the VM instance. For instructions, see [Install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index).

  7. From an external host or terminal with network access to the VM instance, attempt to sign in to the VM instance by using SSH with incorrect credentials 8 consecutive times:
         
         ssh TEST_USER@INSTANCE_IP_ADDRESS
         

When prompted for a password, enter an incorrect password. Repeat this 8 times.

  8. Sign in with the correct password:
         
         ssh TEST_USER@INSTANCE_IP_ADDRESS
         

When prompted, enter the correct password for TEST_USER.

  9. Verify that the authentication logs appear in Cloud Logging under the log ID `authlog`.




## View findings

After triggering findings by testing a detector, verify that the findings are generated by viewing them in Security Command Center or Cloud Logging:

### View findings in Security Command Center

To view the Event Threat Detection finding in Security Command Center, do the following:

  1. In the Google Cloud console, go to the Security Command Center **Findings** page.

[Go to Findings](https://console.cloud.google.com/security/command-center/findings)

  2. In the **Category** section of the **Quick filters** panel, select the finding category:

     * For **IAM Anomalous Grant** , select **Persistence: IAM anomalous grant** (click **View more** if necessary).
     * For **Malware: Bad Domain** , select **Malware: Bad Domain** (click **View more** if necessary).
     * For **SSH Brute Force** , select **Brute Force: SSH** (click **View more** if necessary).
  3. To sort the list in the **Findings query results** panel, click the **Event time** column header so that the most recent finding displays first.

  4. In the **Findings query results** panel, display the details of the finding by clicking the category name (**Persistence: IAM Anomalous Grant** , **Malware: Bad Domain** , or **Brute Force: SSH**) in the **Category** column. The details panel for the finding opens and displays the **Summary** tab.

  5. Verify the details of the finding:

     * For **IAM anomalous grant** , check that the value on the **Principal email** row contains your test `gmail.com` email address.
     * For **Malware: Bad Domain** , select the **Source properties** tab and check that the **Domains** row contains `etd-malware-trigger.goog`.
     * For **SSH Brute Force** , check that the **User name** matches your test username and that the **Caller IP** matches the IP address from which you performed the sign-in attempts.



### View findings in Cloud Logging

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

If you enabled logging findings to Cloud Logging, you can view the findings there.

**Prerequisite:** Before you can view Event Threat Detection findings in Logging, [configure log export](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging). 

To view findings in Cloud Logging, follow these steps:

  1. In the Google Cloud console, go to **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the Google Cloud project where you are storing your Event Threat Detection logs.

  3. Use the **Query** pane to query findings using one of the following methods:

     * In the **All resources** list, do the following: 
       1. Select **Threat Detector** to display a list of all detectors.
       2. Under **DETECTOR_NAME** , select **iam_anomalous_grant** , **bad_domain** , or **ssh_brute_force**.
       3. Click **Apply**.
     * In the query editor, enter the following query and click **Run query** :
           
           resource.type="threat_detector"
           

  4. To view the log, click a table row and click **Expand nested fields**.




## Clean up test resources

To avoid leaving security anomalies or incurring unwanted charges, clean up the test resources for the detector that you tested:

### Clean up IAM Anomalous Grant resources

To revoke permissions granted for the IAM Anomalous Grant test:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. In the row for the test user's gmail.com address, click edit **Edit principal**.

  3. In the pane that appears, click delete **Delete role** next to the **Owner** role.

  4. Click **Save**.




### Clean up Malware: Bad Domain resources

To clean up resources created for the Malware: Bad Domain test, follow these steps:

  1. Delete the VM instance you created. For instructions, see [Delete a VM instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).
  2. Disassociate or delete the DNS server policy that you created. For instructions, see [Delete a DNS policy](https://docs.cloud.google.com/dns/docs/policies).



### Clean up SSH Brute Force resources

To clean up resources created for the SSH Brute Force test, follow these steps:

  1. Delete the VM instance that you created. For instructions, see [Delete a VM instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).
  2. Alternatively, if you want to keep the VM instance, revert `PasswordAuthentication` to `no` in `/etc/ssh/sshd_config`, restart the SSH service (`sudo systemctl restart ssh`), and delete the test user account (`sudo deluser TEST_USER`).



## Troubleshoot

If a finding doesn't appear in Security Command Center or Cloud Logging after testing:

  * Verify that Event Threat Detection is enabled in your Security Command Center [Services](https://docs.cloud.google.com/security-command-center/docs/how-to-configure-security-command-center#enable-service) settings.
  * If testing the Malware: Bad Domain or SSH Brute Force detectors, verify that the project containing the VM instance is in scope for Event Threat Detection.
  * For viewing findings in Cloud Logging, ensure you have [configured log export](https://docs.cloud.google.com/security-command-center/docs/export-cloud-logging).
  * For more troubleshooting steps, see [Troubleshooting Security Command Center](https://docs.cloud.google.com/security-command-center/docs/troubleshooting).



## What's next

  * Learn more about [using Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/how-to-use-event-threat-detection).
  * Read a high-level overview of [Event Threat Detection concepts](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview).
  * Learn how to [investigate and develop response plans](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats) for threats.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
