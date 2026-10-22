---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/nessus-scans/
title: Perform Nessus scans \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:40.248241+00:00
---

# Perform Nessus scans  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/nessus-scans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Perform Nessus scans Stay organized with collections  Save and categorize content based on your preferences. 

Nessus is a security scanner used to detecting security vulnerabilities in hardware and software.

This document presents the steps to:

  * install Nessus

  * perform Nessus scans

  * export Nessus scan results




## 1\. Background

Tenable Nessus is a licensed 3rd party tool. Please see the following resources to learn more about Nessus:

  * <https://docs.tenable.com/Nessus.htm>

  * <https://docs.tenable.com/nessus/Content/GetStarted.htm>




## 2\. Before you begin

  * Workstation

    * The bootstrapper (te-bf), or equivalent operator accessible workstation, is required to host Nessus.
**Note:** This workstation will be referred to as the "Nessus workstation" through the rest of this doc.
  * Access required

    * Follow [IAM-R0005](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/iam/runbooks/iam-r0005):

      * Obtain a cluster admin role for each target cluster.
    * Follow [IAM-R0004](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/gdch-io/service-manual/iam/runbooks/iam-r0004):

      * Generate the KUBECONFIG for each target cluster.
  * Tools required

    * kubectl
    * ssh-keygen
  * Software

    * A Nessus installer compatible with your workstation OS is required. Obtain the installer from <https://www.tenable.com/downloads/nessus> and transfer it to the Nessus workstation before continuing.
  * Licensing

    * A single Tenable Nessus license (Pro, Export or Manager) activation code is required. If you don't have a license activation code, reach out to your team POC for third party licensing / software bill of materials.



## 3\. Install Nessus

This section covers steps to install Nessus on the Nessus workstation.

If Nessus is already installed and activated then this section should be skipped.

If Nessus is no longer available (for example it was installed on a machine which no longer exists) then the license used to activate the prior instance of Nessus must be reset before continuing.

**Important:** These steps assume that the Nessus workstation is Ubuntu Linux. If the Nessus workstation is not Ubuntu, refer to the official Nessus documentation for guidance: <https://docs.tenable.com/nessus/Content/InstallNessus.htm>.

  1. Export the path to the Nessus installer:
         
         NESSUS_INSTALLER=
         

  2. Install Nessus with dpkg:
         
         dpkg -i ${NESSUS_INSTALLER:?}
         

  3. Restart Nessus and confirm that it's running:
         
         sudo systemctl restart nessusd
         sudo systemctl status nessusd
         

  4. Get challenge code to register nessus offline:
         
         /opt/nessus/sbin/nessuscli fetch --challenge
         

  5. On an internet connected machine, visit the Nessus offline activation page <https://plugins.nessus.org/v2/offline.php>.

  6. Copy the Nessus offline activation code and Nessus license activation code into the Nessus offline activation page and press "Submit"

  7. The Nessus offline activation page should now show a Nessus plugin URL and product license. Both of these values are needed for next steps.

  8. Save the Nessus plugin URL to a safe location for future reference as it will be needed later in this guide.

  9. Save the license from the Nessus offline activation page to the Nessus workstation in a file named `/opt/nessus/etc/nessus/nessus.license`.

  10. Apply the license to Nessus:
         
         /opt/nessus/sbin/nessuscli fetch --register-offline /opt/nessus/etc/nessus/nessus.license
         

  11. Create an admin user:

Follow the prompts from `nessuscli adduser` to create an `admin` user. These credentials will later be used to perform scans and download results, so save them in a safe place.
         
         /opt/nessus/sbin/nessuscli adduser
         

  12. While Nessus is running, it's user interface is accessible on port 8834. Using your browser of choice, navigate to `https://<nessus-workstation-ip>:8834` and login as the `admin` user.




## 4\. Update Nessus plugins

The latest Nessus plugins must be downloaded and applied to Nessus before running scans to ensure the scan results are relevant and up to date. The Nessus plugins must be obtained from Tenable directly by using the Nessus plugin URL obtained from the Nessus offline activation page.

  1. Obtain the plugin bundle.

Option 1: Navigate to the Nessus plugin URL using your browser of choice and the bundle will be automatically downloaded.

Option 2: Download the bundle using wget `wget "${PLUGIN_URL:?}" -O plugin-updates.tar.gz`

  2. Transfer the plugin bundle to the Nessus workstation and export the location of the file:
         
         NESSUS_PLUGIN_BUNDLE=
         

  3. Apply the plugin updates to Nessus:
         
         /opt/nessus/sbin/nessuscli update ${NESSUS_PLUGIN_BUNDLE:?}
         

  4. Plugin updates take ~30 minutes to finish compiling. The next steps to create scans can be followed while this happens, but hold off on running the scans until plugins have finishing compiling.




## 5\. Configure Nessus scans

Scans need to be created for each unique combination of target class and credential. This section will walk through how to create the needed scan through the Nessus UI.

Before continuing, confirm access to the Nessus UI at `https://<nessus-workstation-ip>:8834` and login as the `admin` user.

### 5.1. Collect network CIDRs

Nessus scans are created to scan the external and internal network CIDRs for the environment.

  1. Collect the external and internal network CIDRs for the target appliance network (ideally this network is not overlapping with another neighboring environment).

**Tip:** Both network CIDRs should be specified in the bootstrapper subnet claim `/root/gdch/cell/cellcfg/bd-cell-cidr-subnet-claim.yaml`. If you don't have access to the bootstrapper, check the org infrastructure cluster `subnetclaim` custom resources.
  2. The IP ranges will likely include the bootstrapper IP or other IPs which should not be scanned. Enter the following commands for each IP which should not be scanned (eg bootstrapper IP):
         
         IGNORE_IP=
         IGNORE_IP_REASON=
         
         echo "# ${IGNORE_IP_REASON:?}" >> /opt/nessus/etc/nessus/nessusd.rules
         echo "reject ${IGNORE_IP:?}" >>  /opt/nessus/etc/nessus/nessusd.rules
         




### 5.2. Host discovery scans

Network discovery scans are unauthenticated and are meant to sweep a network for targets and insecure network exposures.

This scan will be configured to scan the external and internal network CIDRs identified in the previous section.

In the Nessus UI:

  1. Create a host discovery scan called `host-discovery`
  2. Specify Hosts: both external and internal CIDRs
  3. Save and launch



### 5.3. Node OS scans

Node scans are authenticated and meant to inspect critical operating systems for known vulnerabilities, insecure configuration, and compliance.

Work through this section for the org infrastructure cluster:

  1. Export the cluster kubeconfig:
         
         KUBECONFIG=
         

  2. List all the cluster nodes:
         
         kubectl --kubeconfig=${KUBECONFIG:?} get nodes -o wide
         

  3. Note the column which shows the data IP for each node. Double check that the data IP is accessible from the Nessus workstation with ping before continuing.
         
         ping <node_data_ip>
         

  4. In the Nessus UI, start creating an "Advanced scan" with the name `nodeos-compliance-<cluster_name>`

  5. In the advanced scan, fill the hosts field with a comma separated list of all node data IPs from step 1

  6. Follow Appendix: Add cluster node SSH Credentials to add scan credentials.

  7. Navigate to the compliance tab and choose the latest available revision of "DISA STIG Ubuntu 20.04 v1". Save the compliance config as is without making any changes to the default values.

**Important:** If Nessus is more than a few months old then it needs to be updated to ensure the latest compliance is used. Alternatively, obtain the latest revision of the DISA STIG ubuntu compliance from <https://www.tenable.com/audits/DISA_STIG_Ubuntu_20.04_LTS_v1r10> (follow any redirects to the latest version). Once obtained, add it to the scan by selecting the compliance option like "Upload custom unix" and select the latest compliance file.
  8. Save the scan configuration and launch the scan.




### 5.4. Take a break

The scans should take 30+ minutes to finish. Now is a good time to take a break or do something else until they are completed.

## 6\. Export scan results

This section walks through the process to export scan results.

For each completed scan, download the results:

  1. Select the completed scan to review its results.

  2. Click the "Report" button in the upper right.

  3. Choose Report Format CSV and select all columns.

  4. Click "Generate Report". After a short delay the report should be downloaded.

  5. (Optional) If an HTML report is also required, instead choose Report Format HTML and whichever Report Template seems reasonable. The recommended report template is "Detailed Vulnerabilities By Plugin with Compliance/Remediation".




## 7\. Next steps

The resulting CSV / HTML reports must be processed according to your environment security processes. When in doubt, reach out to a SecOps or Compliance POC for further instruction.

## 8\. Appendix

### 8.1. Add cluster node SSH Credentials

This section walks through the process to obtain a set of ssh credentials for Nessus to scan the nodes of a target cluster.

  1. Export the cluster kubeconfig:
         
         KUBECONFIG=
         

  2. List the cluster SSH keys
         
         kubectl --kubeconfig=${KUBECONFIG} get -A secret | grep ssh-key
         

  3. Identify the namespace of the "ssh-key" secret corresponding to the target cluster and export the namespace:
         
         CLUSTER_NS=
         

  4. Create a Nessus ssh directory:
         
         NESSUS_FOLDER=nessus
         mkdir -p ${NESSUS_FOLDER}/.ssh
         

  5. Export the ssh key pair to the Nessus ssh directory:
         
         kubectl --kubeconfig=${KUBECONFIG:?} get -n ${CLUSTER_NS:?} secret/ssh-key -o jsonpath='{ .data.id_rsa }' | base64 -d > ${NESSUS_FOLDER}/.ssh/nessus-${CLUSTER_NS}-id_rsa
         
         kubectl --kubeconfig=${KUBECONFIG:?} get -n ${CLUSTER_NS:?} secret/ssh-key -o jsonpath='{ .data.id_rsa-cert\.pub }' | base64 -d > ${NESSUS_FOLDER}/.ssh/nessus-${CLUSTER_NS}-id_rsa-cert.pub
         

  6. Fix the permissions of the key pair:
         
         # fix permissions
         chmod 600 ${NESSUS_FOLDER}/.ssh/nessus-${CLUSTER_NS}-id_rsa
         chmod 600 ${NESSUS_FOLDER}/.ssh/nessus-${CLUSTER_NS}-id_rsa-cert.pub
         

  7. Convert the private key to pem format with an empty passphrase:
         
         ssh-keygen -p -m PEM -f ${NESSUS_FOLDER}/.ssh/nessus-${CLUSTER_NS}-id_rsa
         

Successful output should look something like the following:
         
         Key has comment 'root@te-bd-bootstrapper'
         Enter new passphrase (empty for no passphrase):
         Enter same passphrase again:
         Your identification has been saved with the new passphrase.
         

  8. Transfer `nessus-<cluster>-id_rsa` and `nessus-<cluster>-id_rsa-cert.pub` to the workstation used to access the Nessus UI.

  9. In the Nessus UI, go to the scan settings Credentials tab.

  10. Create a new SSH credential and choose "certificate" for authentication method.

  11. Provide the following settings to the certificate ssh authentication method:

     * Username: "root"

     * User Certificate: Add file `nessus-<cluster>-id_rsa-cert.pub`

     * Private key: Add file `nessus-<cluster>-id_rsa`

  12. Save the SSH settings.

  13. Return to where this section was referenced.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
