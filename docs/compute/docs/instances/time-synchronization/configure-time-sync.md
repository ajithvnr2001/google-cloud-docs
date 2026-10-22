---
url: https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-time-sync/
title: Configure accurate time for Compute Engine VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:13.149594+00:00
---

# Configure accurate time for Compute Engine VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/time-synchronization/configure-time-sync/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure accurate time for Compute Engine VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

Many software systems that depend on careful sequencing of events rely on a stable, consistent system clock, using system logs with timestamps to ensure time synchronization and debug issues as they occur. To help keep system clocks in sync, Compute Engine virtual machine (VM) instances are preconfigured to use _network time protocol (NTP)_ , a bundled solution of time synchronization hardware and software. If ensuring accurate time synchronization and monitoring the accuracy of your time synchronization are important for your goals, you can configure _accurate time_ instead of NTP, to sync your VM's clock with the host clock by using `chrony` and `ptp_kvm`. This configuration is designed to achieve accuracy within 1 ms for supported setups.

## Supported machine types

The following machine types support accurate time:

  * [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series)
  * [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series)
  * [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types)
  * [C4D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_machine_types)



## Supported operating systems

The following operating systems (OSes) support accurate time:

OS | Versions | Images  
---|---|---  
CentOS Stream | 9 | centos-stream-9  
Container-Optimized OS  | COS 105 LTS, COS 109 LTS, COS 113 LTS, COS 117 LTS | cos-105-lts, cos-109-lts, cos-113-lts, cos-117-lts   
Debian  | 11 (Bullseye), 12 (Bookworm) | debian-11, debian-12   
Fedora Cloud | 39 | fedora-cloud-39  
RHEL  | 8, 9  | rhel-8-4-sap-ha, rhel-8-6-sap-ha, rhel-8-8-sap-ha, rhel-8-10-sap-ha, rhel-9, rhel-9-0-sap-ha, rhel-9-2-sap-ha, rhel-9-4-sap-ha  
Rocky Linux  | 8, 9  | rocky-linux-8, rocky-linux-8-optimized-gcp, rocky-linux-9-optimized-gcp, rocky-linux-9-optimized-gcp  
SLES  | 15  | sles-15, sles-15-sp2-byos, sles-15-sp2-sap, sles-15-sp3-byos, sles-15-sp3-sap, sles-15-sp4-byos, sles-15-sp4-sap, sles-15-sp5-byos, sles-15-sp5-sap  
Ubuntu  | 22.04 LTS (Jammy Jellyfish), 24.04 LTS (Noble Numbat) | ubuntu-2204-lts, ubuntu-2404-lts-amd64   
Ubuntu Pro  | 2004  | ubuntu-pro-2004-lts, ubuntu-pro-2004-lts-amd64  
  
## Supported zones

Accurate time synchronization is supported in all standard public Google Cloud [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) for supported machine types and OSes.

## Configure accurate time synchronization

To configure accurate time synchronization for your project's VMs, complete the following tasks for each VM:

  * Configure `chrony` to use `ptp-kvm` as its time source.
  * Configure Google Cloud Ops Agent for data collection and analysis.



After you've completed both tasks, accurate time synchronization is set up for the VMs in your project.

For a sample script that creates a VM and completes both tasks to configure accurate time synchronization, see the [VM creation script](https://github.com/GoogleCloudPlatform/solutions-gke-init-daemonsets-tutorial/blob/master/time-sync-example/gce/time-sync-vm-creation.sh) in GitHub.

### Configure `chrony` to use `ptp-kvm`

To configure `chrony` to use `ptp-kvm` as its time source, run the following script inside each of your Google Cloud project's VMs:
    
    
    #!/bin/bash
    
    # Install chrony as needed
    if ! command -v chronyc &>/dev/null; then
        # Detect the package manager and install chrony
        if command -v apt &>/dev/null; then
            # Debian, Ubuntu, and derivatives
            echo "Detected apt. Installing chrony..."
            apt-get update
            apt-get install -y chrony
        elif command -v dnf &>/dev/null; then
            # Fedora, RHEL 8+, CentOS 8+
            echo "Detected dnf. Installing chrony..."
            dnf install -y chrony
        elif command -v yum &>/dev/null; then
            # RHEL 7, CentOS 7
            echo "Detected yum. Installing chrony..."
            yum install -y chrony
        elif command -v zypper &>/dev/null; then
            # openSUSE, SLES
            echo "Detected zypper. Installing chrony..."
            zypper install -y chrony
        else
            echo "Please install chrony manually."
            exit 1
        fi
    fi
    
    # Different distros place chrony config in
    # different locations, detect this.
    if [ -f "/etc/chrony/chrony.conf" ]; then
        CHRONY_CONF="/etc/chrony/chrony.conf"
    else
        CHRONY_CONF="/etc/chrony.conf"
    fi
    
    # Load PTP-KVM clock for high-accuracy clock synchronization
    # PTP-KVM allows the VM to read a cross time-stamp of a platform
    # provided clock and the VM CPU Clock (CycleCounter), providing
    # resiliency from network and virtualization variability when
    # synchronizing the realtime/wall clock
    /sbin/modprobe ptp_kvm
    echo "ptp_kvm" >/etc/modules-load.d/ptp_kvm.conf
    
    # NTP servers might indicate the wrong time due to chrony
    # greatly reducing the polling frequency, resulting in
    # overall negative impact to the clock synchronization
    # achieved, especially after live migration events.
    #
    # We disable NTP servers to prevent these issues.
    #
    # Customers interested in monitoring the clock accuracy compared to NTP sources
    # should run a second instance of chrony in a no-change mode to do so.
    
    # Disable NTP servers:
    sed -i '/^server /d' $CHRONY_CONF
    sed -i '/^pool /d' $CHRONY_CONF
    sed -i '/^include /d' $CHRONY_CONF
    
    #Disable DHCP based NTP config:
    sed -i 's/^NETCONFIG_NTP_POLICY="auto"/NETCONFIG_NTP_POLICY=""/' /etc/sysconfig/network/config
    truncate -s 0 /var/run/netconfig/chrony.servers
    echo PEERNTP=no | sudo tee -a /etc/sysconfig/network
    service NetworkManager restart
    systemctl disable systemd-timesyncd.service
    timedatectl set-ntp false
    
    # Configure PTP-KVM based HW refclock, with leap second smearing
    # Google's clocks are doing leap second smearing, and therefore chrony shouldn't attempt to adjust
    # the time received from PTP-KVM to adjust for leap seconds.
    sed "s/^leapsectz/#leapsectz/" -i $CHRONY_CONF
    echo "refclock PHC /dev/ptp_kvm poll -1" >>$CHRONY_CONF
    # For extra debugging logging, uncomment the following line
    #echo "log measurements statistics tracking" >> $CHRONY_CONF
    # Enable chrony's clock accuracy tracking log,
    # for monitoring and auditing.
    echo "log tracking" >>$CHRONY_CONF
    
    # Restart chrony (Ubuntu named it differently)
    systemctl restart chronyd
    systemctl restart chrony
    

### Configure Google Cloud Ops Agent on your VM

To configure Google Cloud Ops Agent for data collection and analysis, run the following script inside each of your Google Cloud project's VMs:
    
    
    #!/bin/bash
    
    # From https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#install-latest-version
    curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
    bash add-google-cloud-ops-agent-repo.sh --also-install
    
    OPS_AGENT_CONF="
    logging:
        receivers:
            chrony_tracking_receiver:
                type: files
                include_paths:
                    - /var/log/chrony/tracking.log
        processors:
            chrony_tracking_processor:
                type: parse_regex
                regex: \"^.*PHC0.*  (?<max_error>[-\d\.eE]+)$\"
        service:
            pipelines:
                chrony_tracking_pipeline:
                    receivers: [chrony_tracking_receiver]
                    processors: [chrony_tracking_processor]
    "
    
    OPS_AGENT_CONF_PATH="/etc/google-cloud-ops-agent/config.yaml"
    echo "$OPS_AGENT_CONF" >"$OPS_AGENT_CONF_PATH"
    systemctl restart google-cloud-ops-agent
    

## Configure time synchronization monitoring

To configure time synchronization monitoring for your Google Cloud project's VMs, run the logging and dashboard setup script for your Google Cloud project. This script helps you to complete the following tasks for your Google Cloud project:

  * It sets appropriate permissions on the service account associated with your VM's Google Cloud project.
  * It creates a log-based metric that `chrony` uses to ensure accuracy between the clocks on the VM and its host server.
  * It creates a dashboard measuring the VM clock's traceability to UTC by combining the following metrics: 
    * The VM host clock's accuracy to UTC, which is available as a Google Cloud metric, [`instance/clock_accuracy/ptp_kvm/nanosecond_accuracy`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c).
    * The `chrony` metrics measuring the VM clock's accuracy to its host's clock.



To accomplish the preceding tasks, run the following script:
    
    
    #!/bin/bash
    
    if [ -z "$1" ]; then
        echo "Usage: time-sync-logging-dashboard.sh <project_id>" >&2
        exit 1
    fi
    
    PROJECT_ID="$1"
    PROJECT_NUMBER=$(gcloud projects describe "$PROJECT_ID" --format="value(projectNumber)")
    SERVICE_ACCOUNT_EMAIL=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com
    
    gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
        --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
        --role="roles/compute.instanceAdmin"
    
    gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
        --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
        --role="roles/monitoring.metricWriter"
    
    gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
        --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
        --role="roles/logging.logWriter"
    
    cp clock-error-metric.json /tmp/clock-error-metric.json
    sed -i "s/PROJECT_ID/${PROJECT_ID}/" /tmp/clock-error-metric.json
    
    gcloud logging metrics create --project "${PROJECT_ID}" phc-clock-max-error-gce --config-from-file=/tmp/clock-error-metric.json
    gcloud monitoring dashboards create --project "${PROJECT_ID}" --config-from-file=metric-dashboard.json
    

After the script completes running, use the dashboard it created to view clock accuracy data for your project's VMs.

## What's next

  * For complete sample code for setting up accurate time, including Google Kubernetes Engine samples, visit the [example repository](https://github.com/GoogleCloudPlatform/solutions-gke-init-daemonsets-tutorial/blob/master/time-sync-example/).
  * For information about configuring time synchronization for Google Kubernetes Engine nodes, see the documentation for [Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#time-sync).
  * Review the available options for [configuring your VM's time synchronization](https://docs.cloud.google.com/compute/docs/instances/time-synchronization).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
