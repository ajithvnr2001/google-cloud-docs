---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/rotate-logs/
title: Use log rotation for Ops Agent self logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:13.215396+00:00
---

# Use log rotation for Ops Agent self logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/rotate-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Use log rotation for Ops Agent self logs Stay organized with collections  Save and categorize content based on your preferences. 

The Ops Agent writes to a log file called `logging-module.log`. When the agent runs unattended for long periods or when a problem occurs, this "self log" file can consume all available disk space. This document describes how to use log rotation to prevent this problem.

Ops Agent version 2.31.0 introduces a configurable log-rotation feature built into the agent. If you are running Ops Agent version 2.31.0 or newer, then you can use the built-in log-rotation feature; see Configure log rotation in the Ops Agent.

You can also manage log rotation manually. You might need a manual process if you are using a version of the Ops Agent without built-in log rotation, or if you prefer to rotate your logs manually. See Set up self-log file rotation on Linux VMs for one possible approach.

## Configure log rotation in the Ops Agent

This section describes how to modify the default log-rotation configuration used by Ops Agent to rotate its logs automatically. Using this feature requires Ops Agent version 2.31.0 or newer.

### Default configuration

The Ops Agent uses the `default_self_log_file_rotation` entry to configure log rotation. This configuration entry takes three options; the following snippet shows the options and their default values:
    
    
      default_self_log_file_rotation:
        enabled: true
        max_file_size_megabytes: 400
        backup_count: 1
    

The `default_self_log_file_rotation` configuration takes three options:

  * `enabled`: Whether log rotation is enabled; default is `true`.
  * `max_file_size_megabytes`: The maximum size the log file can reach before it is backed up by log rotation. Measured in megabytes (10242 bytes). Default is 400, minimum valid value is 1.
  * `backup_count`: The number of old log files to retain. Default is 1, minimum valid value is 1.



### User configuration of log rotation

To modify the default log-rotation configuration, you override that configuration by redefining the configuration in the Ops Agent user-configuration file:

  * On Linux: `/etc/google-cloud-ops-agent/config.yaml`
  * On Windows: `C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml`

**Note:** If you make any changes to the configuration file, then you must [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart) to apply the updated configurations.

To configure log rotation in the Ops Agent, add a `global` section to the user configuration file and include the configuration element `default_self_log_file_rotation` in the `global` section. You might already have logging or metrics pipelines in the this configuration file; add the `global` section after your pipelines. The result, specifying all options and default values, looks like the following:
    
    
    logging:  ...
    metrics:  ...
    global:
      default_self_log_file_rotation:
        enabled: true
        max_file_size_megabytes: 400
        backup_count: 1
    

### Example configurations

To disable log rotation by the Ops Agent, specify the `enabled` option with the value `false`:
    
    
    logging:  ...
    metrics:  ...
    global:
      default_self_log_file_rotation:
        enabled: false
    

To rotate the log when the log file reaches 20 MB and keep 5 backups (6 files total):
    
    
    logging:  ...
    metrics:  ...
    global:
      default_self_log_file_rotation:
        max_file_size_megabytes: 20
        backup_count: 5
    

To rotate the log when the log file reaches 2,000 MB (2 GB) and keep 1 backup (2 files total):
    
    
    logging:  ...
    metrics:  ...
    global:
      default_self_log_file_rotation:
        max_file_size_megabytes: 2000
    

To rotate the log when the log file reaches 400 MB and keep 2 backups (3 files total):
    
    
    logging:  ...
    metrics:  ...
    global:
      default_self_log_file_rotation:
        backup_count: 2
    

If you make frequent changes as you refine your log-rotation configuration, remember to [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart) to apply your changes.

## Set up self-log file rotation on Linux VMs

To limit the size of the logging sub-agent log at `/var/log/google-cloud-ops-agent/subagents/logging-module.log`, install and configure the `logrotate` utility.

  1. Install the `logrotate` utility by running the following command:

**On Debian and Ubuntu**
         
         sudo apt install logrotate
         

**On CentOS, RHEL and Fedora**
         
         sudo yum install logrotate
         

  2. Create a `logrotate` config file at `/etc/logrotate.d/google-cloud-ops-agent.conf`.
         
         sudo tee /etc/logrotate.d/google-cloud-ops-agent.conf > /dev/null << EOF
         # logrotate config to rotate Google Cloud Ops Agent self log file.
         # See https://manpages.debian.org/jessie/logrotate/logrotate.8.en.html for
         # the full options.
         /var/log/google-cloud-ops-agent/subagents/logging-module.log
         {
             # Log files are rotated every day.
             daily
             # Log files are rotated this many times before being removed. This
             # effectively limits the disk space used by the Ops Agent self log files.
             rotate 30
             # Log files are rotated when they grow bigger than maxsize even before the
             # additionally specified time interval
             maxsize 256M
             # Skip rotation if the log file is missing.
             missingok
             # Do not rotate the log if it is empty.
             notifempty
             # Old versions of log files are compressed with gzip by default.
             compress
             # Postpone compression of the previous log file to the next rotation
             # cycle.
             delaycompress
         }
         EOF
         

  3. Set up [`crontab`](https://linux.die.net/man/5/crontab) or [`systemd timer`](https://wiki.archlinux.org/title/Systemd/Timers) to trigger the `logrotate` utility periodically.




After the log rotation takes effect, you see rotated files in the `/var/log/google-cloud-ops-agent/subagents/` directory. The results look similar to the following output:
    
    
    /var/log/google-cloud-ops-agent/subagents$ ls -lh
    total 24K
    -rw-r--r-- 1 root root  717 Sep  3 19:54 logging-module.log
    -rw-r--r-- 1 root root 6.8K Sep  3 19:51 logging-module.log.1
    -rw-r--r-- 1 root root  874 Sep  3 19:50 logging-module.log.2.gz
    -rw-r--r-- 1 root root  873 Sep  3 19:50 logging-module.log.3.gz
    -rw-r--r-- 1 root root 3.2K Sep  3 19:34 logging-module.log.4.gz
    

To test log rotation, do the following:

  1. Temporarily reduce the file size at which rotation is triggered by setting the `maxsize` value to `1k` in the `/etc/logrotate.d/google-cloud-ops-agent.conf` file.

  2. Trigger the agent self log file to be larger than 1K by restarting the agent a few times:
         
         sudo service google-cloud-ops-agent restart
         

  3. Wait for the `crontab` or `systemd timer` to take effect to trigger the `logrotate` utility, or trigger the `logrotate` utility manually by running this command:
         
         sudo logrotate /etc/logrotate.d/google-cloud-ops-agent.conf
         

  4. Verify that you see rotated log files in the `/var/log/google-cloud-ops-agent/subagents/` directory.

  5. Reset the log-rotation configuration by restoring the original `maxsize` value.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
