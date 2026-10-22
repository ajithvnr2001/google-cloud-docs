---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/cis-compliance/
title: Configuring and Checking CIS Compliance \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:18.561466+00:00
---

# Configuring and Checking CIS Compliance  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/cis-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Configuring and Checking CIS Compliance Stay organized with collections  Save and categorize content based on your preferences. 

This document explains what the CIS Benchmark is, how the benchmark relates to Container-Optimized OS (COS), how to audit the status of compliance in the instance and how to troubleshoot in case of failure.

## Overview

The Center for Internet Security (CIS) releases benchmarks for best practice security recommendations for various platforms. The Container-Optimized OS CIS Benchmark is a set of recommendations for configuring instances that use Container-Optimized OS to support a strong security posture. Both COS x86 and ARM images are CIS compliant.

## Accessing the Benchmark

The Container-Optimized OS CIS Benchmark is available on the CIS website:

  * Go to the [CIS Benchmarks downloads page](https://downloads.cisecurity.org).
  * Search for **CIS Google Container-Optimized OS Benchmark**.
  * Click **Download PDF**.



## Security recommendation levels

CIS defines the following recommendation levels for Container-Optimized OS.

### Level 1

Recommendations at this level are meant to be applicable to the majority of environments. This level includes recommendations such as the following:

  * Address space layout randomization is enabled
  * `/tmp` cannot be used for running executable binaries
  * Packet redirect sending is disabled



### Level 2

Recommendations at this level extend the Level 1 recommendations, resulting in a more stringent security environment. The Level 2 recommendations are not necessarily applicable to all cases as they may require application changes. You should evaluate the recommendations at Level 2 for your environment before you apply them. This level includes recommendations such as the following:

  * Firewall rules exist for all open ports
  * ICMP redirects and router advertisements are not accepted
  * Default user shell timeout is 900 seconds or less



## How Container-Optimized OS complies with the CIS Benchmarks

Starting with [Milestone 97](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m97), Container-Optimized OS images comply with to CIS Level 1 by default and provide an option to comply with CIS Level 2. We also provide a scanner that you can use to audit your instance against the CIS recommendation levels.

The CIS configuration defining the recommendations is present at `/usr/share/google/security/cis-compliance/cis_config.textproto`. The CIS scanner uses the configuration to check the compliance status of the instance. The results of each run of the CIS level compliance scanner are written to `/var/lib/google/cis_scanner_scan_result.textproto`. This file is overwritten on each run of the CIS scanner. If any of the CIS Level 1 or Level 2 scans fail, the `cis_scanner_scan_result.textproto` file will contain a list of all failing checks.

## Check instance compliance status

Container-Optimized OS images provide the following systemd services for compliance checking and configuration:

  * **cis-level1.service** : Enabled by default and starts on boot. When the service starts, it checks if the instance complies with CIS Level 1.
  * **cis-level2.service** : Disabled by default. This service lets you configure the instance to comply with CIS Level 2, and checks the compliance status against both Level 1 and Level 2.



The following sections explain how to check the compliance status of the instance and how to automate the audit process.

## Check CIS Level 1 compliance status

To see if your instance is CIS Level 1 compliant, check the status of the `cis-level1.service`:
    
    
    systemctl status cis-level1
    

The output is similar to the following:
    
    
    Reading scan config from /usr/share/google/security/cis-compliance/cis_config.textproto
    Running scan of 62 benchmarks
    Scan status: SUCCEEDED
    Found 0 non-compliant benchmarks
    Writing scan results to /var/lib/google/cis_scanner_scan_result.textproto
    

If there are any non-compliant checks found, refer to CIS compliance Level 1/Level 2 check fails.

The `cis-level1.service` checks for CIS Level 1 compliance only once, when the instance boots. To configure periodic compliance checking, refer to Periodic checking of CIS compliance status.

## Configure CIS Level 2 compliance and check status

You can use the `cis-level2` service to configure the instance to comply with CIS Level 2 and to check compliance status against both Level 1 and Level 2. The systemd service supports all of the CIS Level 2 recommendations **except** for the following:

  * 4.1.1.2 Ensure Logging is running (ID: logging-service-running)

This recommendation is opted-out by default but can be re-enabled by deleting the ID from the opted-out list which can be found in the `/etc/cis-scanner/env_vars` file. This check only exists in milestones 109 and later. In earlier milestones, enabling Logging yourself makes you compliant with this recommendation. If you undo the opt-out, running the `cis-level2` service runs a script that starts fluent-bit logging. Keep `logging-service-running` opted out if you don't want to use our default logging or you want to use your own logging.




For the following recommendations, `cis-level2` service configures the instance but does not verify the compliance status:

  * 105 and lower:

    * 3.3.1.1 Ensure IPv6 default deny firewall policy
    * 3.3.1.2 Ensure IPv6 loopback traffic is configured
    * 3.3.1.3 Ensure IPv6 outbound and established connections are configured
    * 3.3.1.4 Ensure IPv6 firewall rules exist for all open ports
    * 3.3.2.1 Ensure default deny firewall policy
    * 3.3.2.2 Ensure loopback traffic is configured
    * 3.3.2.3 Ensure outbound and established connections are configured
  * 109 and later:

    * 3.3.1.4 Ensure IPv6 firewall rules exist for all open ports



The `cis-level2` service is disabled by default. To start the service, run the following command:
    
    
    systemctl start cis-level2.service
    

To see if your instance is successfully configured and complies with CIS Level 2 recommendations, check the status of `cis-level2.service`:
    
    
    systemctl status cis-level2
    

The output is similar to the following:
    
    
    Reading scan config from /usr/share/google/security/cis-compliance/cis_config.textproto
    Running scan of 112 benchmarks
    Scan status: SUCCEEDED
    Found 0 non-compliant benchmarks
    Writing scan results to /var/lib/google/cis_scanner_scan_result.textproto
    

If the instance configuration fails or there are any non-compliant checks found, refer to Troubleshooting.

The `cis-level2` service configures the instance and checks for the CIS Level 2 compliance only once. To configure periodic compliance checking, refer to Periodic checking of CIS compliance status.

## Periodic checking of CIS compliance status

Container-Optimized OS images include the following services to periodically check CIS compliance:

  * **cis-compliance-scanner.service** : checks the compliance status based on environment variables defined at `/etc/cis-scanner/env_vars`. By default, this service checks for CIS Level 1 compliance and is disabled.
  * **cis-compliance-scanner.timer** : runs `cis-compliance-scanner.service` periodically. The default period is once a day.



### Configure the scanner service

The `cis-compliance-scanner.service` is responsible for checking the status of CIS compliance based on the environment variables defined at `/etc/cis-scanner/env_vars`. By default, this service checks for CIS Level 1 compliance.

To check CIS Level 2 compliance, set the **LEVEL** environment variable in `/etc/cis-scanner/env_vars` to **2**. The `/etc/cis-scanner/env_vars` file is similar to the following:
    
    
    # cis-compliance-scanner.service environment variables
    # The config file defines which checks to perform by cis_scanner
    CONFIG="/usr/share/google/security/cis-compliance/cis_config.textproto"
    # Where to store the result of the scan
    RESULT="/var/lib/google/cis_scanner_scan_result.textproto"
    # Upto which level to scan. It can be 1 or 2
    LEVEL="2"
    # Extra options that can be passed to cis_scanner
    # For valid options, see output of `cis_scanner -h`
    EXTRA_OPTIONS=""
    

### Configure the timer

To set up periodic compliance scanning, start the `cis-compliance-scanner.timer` unit:
    
    
    systemctl start cis-compliance-scanner.timer
    

By default, `cis-compliance-scanner.timer` starts `cis-compliance-scanner.service` once a day. To change the scanning period, override the **OnUnitActiveSec** field of the `cis-compliance-scanner.timer` unit:
    
    
    sudo mkdir /etc/systemd/system/cis-compliance-scanner.timer.d
    sudo tee /etc/systemd/system/cis-compliance-scanner.timer.d/override.conf <<EOF
    [Unit]
    Description=Run CIS Scanner once an hour
    [Timer]
    OnUnitActiveSec=1h
    EOF
    

This example sets the scanner period to once every hour.

To apply the changes, reload systemd units:
    
    
    systemctl daemon-reload
    

## Opting out of specific CIS compliance checks

CIS Level 1 and Level 2 recommendations are made to be applicable to most environments. However ,some recommendations might not be applicable to your specific environment. To opt out of specific recommendations, use the **EXTRA_OPTIONS** environment variable in `/etc/cis-scanner/env_vars`.

The following example `env_vars` file opts out of the `etc-passwd-permissions` recommendation:
    
    
    # cis-compliance-scanner.service environment variables
    # The config file defines which checks to perform by cis_scanner
    CONFIG="/usr/share/google/security/cis-compliance/cis_config.textproto"
    # Where to store the result of the scan
    RESULT="/var/lib/google/cis_scanner_scan_result.textproto"
    # Upto which level to scan. It can be 1 or 2
    LEVEL="1"
    # Extra options that can be passed to cis_scanner
    # For valid options:`cis_scanner -h`
    **EXTRA_OPTIONS="--benchmark-opt-out-ids=etc-passwd-permissions"**
    

## Automate enabling and checking of CIS compliance status

You can automate the compliance checking process for your instances using cloud-init or OS Policy. The following examples show some use cases with each tool:

  * Example 1: check CIS Level 1 compliance once a day.
  * Example 2: check CIS Level 1 compliance once an hour.
  * Example 3: check CIS Level 2 compliance once a day.
  * Example 4: opt-out of specific CIS compliance check.



### Using cloud-init

Before you try the following examples, ensure that you're familiar with configuring a COS instance with cloud-init by following the instructions at [Using cloud-init with the Cloud config format](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init_with_the_cloud_config_format).

### Example 1

The following example configuration starts periodic CIS Level 1 scanning with the default period of once a day.
    
    
    #cloud-config
    
    runcmd:
    # Check the compliance status of the instance once a day.
    - systemctl start cis-compliance-scanner.timer

### Example 2

The following example configures periodic CIS Level 1 scanning once every hour.
    
    
    #cloud-config
    
    # Override cis-compliance-scanner.timer with 1 hour frequency.
    write_files:
    
    - path: /etc/systemd/system/cis-compliance-scanner.timer.d/override.conf
      permissions: 0600
      owner: root
      content: |
        [Unit]
        Description=Run CIS Scanner once an hour
    
        [Timer]
        OnUnitActiveSec=1h
    
    runcmd:
    # Reload systemd units.
    - systemctl daemon-reload
    # Check the compliance status of the instance once an hour.
    - systemctl start cis-compliance-scanner.timer

### Example 3

The following example configures periodic CIS Level 2 scanning with the default period of once a day.
    
    
    #cloud-config
    
    runcmd:
    # Configure the instance for CIS level 2.
    - systemctl start cis-level2.service
    # Change the scan level to CIS Level 2.
    - sed -i 's/^LEVEL=.*$/LEVEL="2"/' /etc/cis-scanner/env_vars
    # Check the compliance status of the instance once a day.
    - systemctl start cis-compliance-scanner.timer

### Example 4

The following example configures the scanner to run once a day and opts out of a specific CIS recommendation.
    
    
    #cloud-config
    
    runcmd:
    # Opt-out of the etc-passwd-permissions check.
    - sed -i 's/^EXTRA.*$/EXTRA_OPTIONS="--benchmark-opt-out-ids=etc-passwd-permissions"/' /etc/cis-scanner/env_vars
    # Check the compliance of the instance once a day.
    - systemctl start cis-compliance-scanner.timer

### Using OS Policy

You can use an OS Policy to configure CIS Benchmark scanning. Before you begin, ensure that you're familiar with OS Policy, including the following:

  * [Writing OS Policy](https://docs.cloud.google.com/compute/docs/os-configuration-management/working-with-os-policies)
  * [OS Policy assignment](https://docs.cloud.google.com/compute/docs/os-configuration-management/create-os-policy-assignment)
  * [Viewing OS Policy assignment reports](https://docs.cloud.google.com/compute/docs/os-configuration-management/view-compliance)



In addition, you must add the `instanceFilter` and `rollout` options in the following examples for the deployment.

### Example 1

The following example configuration starts periodic CIS Level 1 scanning with the default period of once a day.
    
    
    # An OS policy to check CIS level 1 compliance once a day.
    id: ensure-cis-level1-compliance-once-a-day-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: ensure-cis-level1-compliance-once-a-day
          exec:
            validate:
              interpreter: SHELL
              # If cis-compliance-scanner.service is active, return an exit code
              # 100 to indicate that the instance is in compliant state.
              # Otherwise, return an exit code of 101 to run `enforce` step.
              script: |-
                is_active=$(systemctl is-active cis-compliance-scanner.timer)
                result=$(systemctl show -p Result --value cis-compliance-scanner.service)
    
                if [ "$is_active" == "active" ] && [ "$result" == "success" ]; then
                  exit 100;
                else
                  exit 101;
                fi
            enforce:
              interpreter: SHELL
              # COS 97 images are by-default CIS Level 1 compliant and there is no
              # additional configuration needed. However, if certain changes
              # cause non-compliance because of the workload on the instance, this
              # section can be used to automate to make fixes. For example, the
              # workload might generate a file that does not comply with the
              # recommended file permissions.
              # Return an exit code of 100 to indicate that the desired changes
              # successfully applied.
              script: |-
                # optional <your code>
                # Check the compliance of the instance once a day.
                systemctl start cis-compliance-scanner.timer && exit 100
    

### Example 2

The following example configures periodic CIS Level 1 scanning once every hour.
    
    
    # An OS policy to check CIS level 1 compliance once an hour.
    id: ensure-cis-level1-compliance-once-an-hour-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: ensure-cis-level1-compliance-once-an-hour
          exec:
            validate:
              interpreter: SHELL
              # If cis-compliance-scanner.service is active, return an exit code
              # 100 to indicate that the instance is in compliant state.
              # Otherwise, return an exit code of 101 to run `enforce` step.
              script: |-
                is_active=$(systemctl is-active cis-compliance-scanner.timer)
                result=$(systemctl show -p Result --value cis-compliance-scanner.service)
    
                if [ "$is_active" == "active" ] && [ "$result" == "success" ]; then
                  exit 100;
                else
                  exit 101;
                fi
            enforce:
              interpreter: SHELL
              # Return an exit code of 100 to indicate that the desired changes
              # were successfully applied.
              script: |-
                # Overwrite "OnUnitActiveSec" field of the
                # cis-compliance-scanner.timer to trigger
                # cis-compliance-scanner.service once an hour
                # instead of once a day.
                mkdir /etc/systemd/system/cis-compliance-scanner.timer.d
                tee /etc/systemd/system/cis-compliance-scanner.timer.d/override.conf <<EOF
                [Unit]
                Description=Run CIS Scanner once an hour
    
                [Timer]
                OnUnitActiveSec=1h
                EOF
                # Reload systemd units.
                systemctl daemon-reload
                # Check the compliance of the instance once an hour.
                systemctl start cis-compliance-scanner.timer && exit 100
    

### Example 3

The following example configures periodic CIS Level 2 scanning with the default period of once a day.
    
    
    # An OS policy to check CIS level 2 compliance once a day.
    id: ensure-cis-level2-compliance-once-a-day-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: ensure-cis-level2-compliance-once-a-day
          exec:
            validate:
              interpreter: SHELL
              # If cis-compliance-scanner.service is active, return an exit code
              # 100 to indicate that the instance is in compliant state.
              # Otherwise, return an exit code of 101 to run `enforce` step.
              script: |-
                is_active=$(systemctl is-active cis-compliance-scanner.timer)
                result=$(systemctl show -p Result --value cis-compliance-scanner.service)
    
                if [ "$is_active" == "active" ] && [ "$result" == "success" ]; then
                  exit 100;
                else
                  exit 101;
                fi
            enforce:
              interpreter: SHELL
              # Return an exit code of 100 to indicate that the desired changes
              # were successfully applied.
              script: |-
                # Configure the instance for CIS level 2.
                systemctl start cis-level2.service
                # Change the scan level to 2.
                sed -i 's/^LEVEL=.*$/LEVEL="2"/' /etc/cis-scanner/env_vars
                # Check the compliance of the instance once a day.
                systemctl start cis-compliance-scanner.timer && exit 100

### Example 4

The following example configures the scanner to run once a day and opts out of a specific CIS recommendation.
    
    
    # An OS policy to opt-out of CIS check and check compliance status once a day.
    id: exclude-cis-check-and-check-compliance-once-a-day-policy
    mode: ENFORCEMENT
    resourceGroups:
      - resources:
          id: exclude-cis-check-and-check-compliance-once-a-day
          exec:
            validate:
              interpreter: SHELL
              # If cis-compliance-scanner.service is active, return an exit code
              # 100 to indicate that the instance is in compliant state.
              # Otherwise, return an exit code of 101 to run `enforce` step.
              script: |-
                is_active=$(systemctl is-active cis-compliance-scanner.timer)
                result=$(systemctl show -p Result --value cis-compliance-scanner.service)
    
                if [ "$is_active" == "active" ] && [ "$result" == "success" ]; then
                  exit 100;
                else
                  exit 101;
                fi
            enforce:
              interpreter: SHELL
              # Return an exit code of 100 to indicate that the desired changes
              # were successfully applied.
              script: |-
                # Opt-out of the etc-passwd-permissions check.
                sed -i 's/^EXTRA.*$/EXTRA_OPTIONS="--benchmark-opt-out-ids=etc-passwd-permissions"/' /etc/cis-scanner/env_vars &&
                # Check the compliance of the instance once a day.
                systemctl start cis-compliance-scanner.timer
                # Ensure cis-compliance-scanner completes before exiting
                PID=$(systemctl show --property MainPID --value cis-compliance-scanner.service) &&
                timeout 5m bash -c -- 'while [ -e /proc/'$PID' ]; do echo "CIS Scanner with PID:'$PID' is still running"; sleep 1; done' &&
                exit 100
    

## Troubleshooting

This section describes how to resolve issues related to CIS benchmark scanning.

### Configuring an instance to comply with CIS Level 2 recommendations fails

The `cis-level2` service first configures the instance to comply with CIS Level 2 recommendations and then checks for compliance with both CIS Level 1 and Level 2. In case configuring the instance fails, the `cis-level2` service exits with the following error message:
    
    
    Job for cis-level2.service failed because the control process exited with error code.
    See "systemctl status cis-level2.service" and "journalctl -xeu cis-level2.service" for details.
    

The journal logs will mention the recommendations which failed to apply on the instance and resulting into failure of `cis-level2` systemd service.

### CIS compliance Level 1 or Level 2 check fails

The scanning results for each run of CIS level compliance are written at `/var/lib/google/cis_scanner_scan_result.textproto`. If any of the CIS Level 1 or Level 2 scans fail, the textproto file will contain the list of all failing checks, such as in the following example:
    
    
    cat /var/lib/google/cis_scanner_scan_result.textproto
    
    # Output
    start_time: {
      seconds: 1648241700
      nanos: 763152171
    }
    end_time: {
      seconds: 1648241700
      nanos: 812992527
    }
    scanner_version: "1.1.4.3"
    benchmark_version: "1.0.0"
    status: {
      status: SUCCEEDED
    }
    non_compliant_benchmarks: {
      id: "etc-passwd-permissions"
      compliance_occurrence: {
        non_compliant_files: {
          path: "/etc/passwd"
          reason: "File permission is 0664, expected the following bits to be set: 0444 and the following bits to be clear: 0133"
        }
      }
    }
    compliant_benchmarks:  {
      id:  "etc-passwd-permissions"
      compliance_occurrence:  {}
    }
    

To mitigate the failed checks, use the CIS Benchmark and follow the steps in the `Remediation` section for the failing check to make the instance compliant. To find which recommendation corresponds to a failing check in the CIS Benchmark, look up the `non_compliant_benchmark's` ID in the CIS scanner config file located at `/usr/share/google/security/cis-compliance/cis_config.textproto`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
