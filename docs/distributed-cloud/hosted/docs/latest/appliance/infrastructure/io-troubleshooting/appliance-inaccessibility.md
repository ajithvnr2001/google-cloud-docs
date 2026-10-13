---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/appliance-inaccessibility/
title: Troubleshoot appliance access issues \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:00.173478+00:00
---

# Troubleshoot appliance access issues  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/appliance-inaccessibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Troubleshoot appliance access issues Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines how to troubleshoot appliance inaccessibility issues post-bootstrapping. You might encounter the following issues:

  * Error messages such as `Unable to connect to the server: dial tcp 198.18.0.64:443: i/o timeout` when attempting to query using kubectl.
  * `Webpage not available` error when trying to access the UI.
  * Deployed applications on the appliance are not working, or you cannot deploy any new applications.



## Troubleshooting UI inaccessible issue

![Flowchart to debug UI inaccessible issue](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/infrastructure/images/appl-flow.png)

  1. Follow the [UI inaccessible](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/ui/runbooks/ui-r0001) runbook to troubleshoot the issue.
  2. Check if the cluster is reachable by following the Cluster reachability section.
  3. If the cluster is responsive, verify if the management API is accessible by following the Management API accessible section.
  4. If the cluster is not reachable and returns errors like `Connection timed out` or `i/o timeout error`, refer to the troubleshooting guide for further troubleshooting steps.



## Basic troubleshooting steps

![LED locations on the device](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/infrastructure/images/led_appl.png)

  1. Verify the power supply of the chassis by checking if the indicator lights (green) on either of the two power supplies are illuminated, as indicated by the arrows in the image.

LED light status | Description  
---|---  
Solid Green | System On and normal operation  
Flashing Green | Standby power present (power supply off)  
Solid Amber | Power supply failed (overvoltage/undervoltage, overtemperature, overcurrent, short-circuit), fan failed, or input overvoltage protection  
Flashing Amber | Power supply error  
Off | No power present or standby power failed (overvoltage/ undervoltage, overtemperature, overcurrent, short-circuit, fan lock)  
  2. If the indicator lights are off, first ensure the power cord is receiving power. If the power cord is functioning properly, the power supplies are likely faulty and need to be replaced. For replacement instructions, refer to the [Power Supply Replacement Guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/appl/runbooks/appl-r0011).

  3. If the power supplies are functioning but the device is still not working, check for any loose or damaged connections.

  4. Verify the LEDs of the switch and servers are illuminated as indicated by the arrows in the image.

  5. If the Link LED of the switch is solid green, verify it is operational by following Verify switch operational section.

  6. If the switch health and configuration is correct, log in to iLO using the steps mentioned in [Steps to log in to iLO](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/appl/guides/appl-g0001). to check the health of the device.

     1. If any of the fans are critical, contact HPE support team to get a replacement of the critical fan and follow the [Fan Replacement Guide](https://support.hpe.com/hpesc/public/docDisplay?docId=psg000031aen_us&page=GUID-84AFBBBB-F451-4EF3-8A6E-890CAC2A799E.html) to replace it.
     2. If any blades are powered off, turn them on by navigating to the Blades section, selecting the blade, and pressing the power button.
     3. If any of the blades are in a critical state, navigate to the Blades section, select the critical blade, go to the Power section, and initiate a Force System Reset.
     4. If the chassis health is critical, you can also try resetting the chassis by going to the **Power and Thermal** tab. Select the **Management Power** section, click **Reset EL8000CM Button**. This process resets the chassis manager firmware and might take a few minutes, during which the chassis is unavailable.
     5. If the issue persists, go to the **Information** tab, select **Logs** , choose **Health Logs** from the drop-down menu, and download them as a CSV file. Raise a ticket with Google and attach the logs to request hardware replacement.

![Heath logs](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/infrastructure/images/health_logs.png)

  7. If the Power LEDs on the blades are illuminated, perform a ping test to the following blade IP addresses from a machine connected to the appliance:
         
         ping 198.18.0.7  //BM01
             ping 198.18.0.8  //BM02
             ping 198.18.0.9  //BM03
         

If the ping test is successful, it indicates that the nodes are operational.

  8. If all the nodes fail the ping test, escalate to Google Support.

  9. If the issue persists after following all the steps outlined in this section, escalate the issue to Google Support for further assistance.




### Loose or damaged connections

  1. Verify that all connections are secure and properly seated. For guidance on checking and securing cable connections within the appliance, refer to [check cables](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/check-cables).

  2. Inspect the cables for any visible damage. If any cables are damaged, replace them.




### Verify switch operational

  1. [Sign in to the switch's serial console](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/appl/guides/appl-g0002). If the login is successful, run the following command to check the health of the switch. This command displays the uptime and resource consumption of the switch.
         
         show version
         

  2. If the serial console is responsive, validate the BGP configuration on the switch by referring to [Validate BGP Summary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/pnet/runbooks/pnet-r3000).

  3. If the Link LED is off or the serial console is unresponsive, the switch might be faulty. Escalate the issue to Google Support for a replacement.




## Verify cluster reachability

  1. Log in to the gdcloud session with IO credentials:
         
         gdcloud auth login
         

  2. If you are unable to log in, locate the emergency credential backed up during the [appliance setup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#back_up_emergency_credentials) to be used with the command -: root-admin-kubeconfig.

  3. Check if the cluster is reachable:
         
         kubectl --kubeconfig root-admin-kubeconfig get servers -A
         




## Verify Management API accessibility

  1. Log in to the gdcloud session with IO credentials:
         
         gdcloud auth login
         

If the login fails, log in with management plane credentials.

  2. The AIS database can sometimes malfunction or be misconfigured causing login failure. Refer to [IAM-R0009 - AIS Database](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/iam/runbooks/iam-r0009).

  3. If you are unable to resolve issues with login, locate the emergency credential backed up during the [appliance setup](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup#back_up_emergency_credentials) to be used with the command -: root-admin-kubeconfig.

  4. Fetch the management plane kubeconfig:
         
         kubectl --kubeconfig root-admin-kubeconfig -n management-kube-system get secret kube-admin-remote-kubeconfig -ojsonpath='{.data.value}' | base64 -d > kube-admin-remote-kubeconfig
         

  5. Get the health status of the cluster:
         
         kubectl --kubeconfig kube-admin-remote-kubeconfig get --raw='/readyz?verbose'
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
