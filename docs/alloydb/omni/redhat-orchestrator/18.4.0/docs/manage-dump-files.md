---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/manage-dump-files/
title: Generate AlloyDB Omni diagnosis dump files \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:55:33.051504+00:00
---

# Generate AlloyDB Omni diagnosis dump files  |  AlloyDB Omni using the RPM orchestrator: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/manage-dump-files/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/overview)



Send feedback 

#  Generate AlloyDB Omni diagnosis dump files Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/manage-dump-files)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/manage-dump-files)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/manage-dump-files)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/manage-dump-files)

Generate AlloyDB Omni debug dump with system state and diagnostic logs to troubleshoot unexpected issues in your deployments. The debug logs provide critical diagnostic information about AlloyDB Omni's state, helping you or the Cloud Customer Care team analyze problems related to the failures or issues with running various services of the AlloyDB Omni stack. Collect these files using either an Ansible role or a standalone tool. 

Control orchestrator level diagnostic logs for alloydbctl and Ansible to adjust verbosity for troubleshooting or to silence output for automated scripts. These logs are essential for diagnosing issues during cluster bootstrap, management, or general operation.

## Collect and dump debug information

You can collect and dump debug information using either an Ansible role or the debug dump tool.

### Collect debug information using Ansible

The `google.alloydbomni_orchestrator.dump_debug` Ansible role automates the collection process across all AlloyDB Omni nodes defined in your deployment specification. It collects and consolidates the following information:

  * Systemd status: current state of all AlloyDB Omni services.
  * Journal logs: system logs, allowing for time-based filtering.



#### Generate dump of debug information

  1. [Create an Ansible playbook](https://docs.ansible.com/projects/ansible/latest/network/getting_started/first_playbook.html) (for example, `dump_debug.yml`) on your control node. Add the following to the playbook:
         
         - name: Collect AlloyDB Omni Debug Dump
           hosts: all
           become: true
           gather_facts: true
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: PATH_TO_PRIVATE_SSH_KEY
             # Optional: Customize dump behavior
             dump_debug_binary_path: "BINARY_PATH"
             dump_debug_collection_type: "COLLECTION_TYPE"
             dump_debug_local_dest: ""ANSIBLE_DESTINATION""
             dump_debug_tag: ""TAG_NAME""
             dump_debug_journal_spec: "JOURNAL_SPEC"
           roles:
             - role: google.alloydbomni_orchestrator.dump_debug
         

Replace the following:

     * `ANSIBLE_USER`: The user Ansible logs in as.
     * `PATH_TO_PRIVATE_SSH_KEY`: The path to the SSH private key file.
     * `BINARY_PATH`: Optional. Path to binaries on remote nodes. Defaults to `/usr/local/bin`.
     * `COLLECTION_TYPE`: Optional. The collection type (`status`, `logs`, `config`, or `all`). Defaults to `all`.
     * `ANSIBLE_DESTINATION`: Optional. Destination on the Ansible control node. Defaults to `/tmp/debug_dump`.
     * `TAG_NAME`: Optional. Custom identifier. Suffixes (for example, `_1`) are added if the tag exists. Defaults to system timestamp.
     * `JOURNAL_SPEC`: Optional. Supports `journalctl` flags (for example, `"--since '1 hour ago'"`). Defaults to `-n 1000`.
  2. Run the playbook using the `ansible-playbook` command, specifying your `deployment_spec.yaml` as the inventory.
         
         # standard execution
         ansible-playbook dump_debug.yml -i PATH_TO_DEPLOYMENT_SPEC

Alternatively, run the playbook with a custom tag and a journal specification of your choice.
         
         ansible-playbook dump_debug.yml -i PATH_TO_DEPLOYMENT_SPEC \
         -e 'dump_debug_tag=TAG_NAME' \
         -e 'dump_debug_journal_spec: "JOURNAL_SPEC"'

Replace the following:

     * `PATH_TO_DEPLOYMENT_SPEC`: The path to your deployment specification YAML file.
     * `TAG_NAME`: Optional. Custom identifier. Suffixes (for example, `_1`) are added if the tag exists. Defaults to system timestamp.
     * `JOURNAL_SPEC`: Optional. Supports `journalctl` flags (for example, `"--since '1 hour ago'"`). Defaults to `-n 1000`.



### Collect debug information using debug dump tool

You can use the `alloydbomni_dump` tool to generate a dump file. This tool is included with the AlloyDB Omni orchestrator package.

#### Generate a dump file

**Note:** The `yq` command-line YAML processor should already be installed on the control machine. If not, run `sudo dnf install -y yq`.

Run the following script on your AlloyDB Omni cluster nodes that you want to debug.
    
    
    sudo /usr/local/bin/alloydbomni_dump \
       -k SSH_KEY \
       -u USER \
       -d PATH_TO_DEPLOYMENT_SPEC \
       -o OUTPUT_DIRECTORY \
       [options]

Replace the following:

  * `SSH_KEY`: The path to the SSH private key of the user.
  * `USER`: The username for SSH access to the cluster nodes.
  * `PATH_TO_DEPLOYMENT_SPEC`: The path to your deployment specification YAML file.
  * `OUTPUT_DIRECTORY`: The local directory to save the generated dump file.



#### Supported commands

  * `-k`: Required path to the SSH private key.
  * `-u`: Required service account username.
  * `-d`: Required path to the deployment specification YAML file.
  * `-o`: Required output directory for the final tar file.
  * `-t`: Optional custom tag identifier.
  * `-c`: Optional collection type (`status`, `logs`, `config`, `all`).
  * `-s`: Optional journal size and time specification (for example, `-s "--since \"30 minutes ago\""`).



#### Execution example
    
    
    alloydbomni_dump -k /home/user/ssh-key \
      -u sa_12345 -d /tmp/deployment_spec.yaml \
      -o /tmp/debug_dump -s "--since \"2 hours ago\""

## Obtain orchestrator diagnostic logs

You can obtain the diagnostic logs generated by both `alloydbctl` and Ansible orchestrators. This lets you increase verbosity for troubleshooting or silence output for automated scripts. Logging is essential for diagnosing issues during bootstrap, management, or general operation of your clusters.

### Obtain `alloydbctl` debug logs

The `alloydbctl` tool supports command-line arguments to control the log level and the output destination. The log level determines the severity of messages to be logged, while the log destination specifies where these logs are written.
    
    
    alloydbctl [command] ... [{-l|--log_level} <LEVEL>] [{-f|--log_file} <FILE>]

#### Log levels (`-l` / `--log_level`)

You can use the following log levels. Log levels are case-insensitive (for example, `DEBUG` and `debug` are treated the same).

  * **NOTSET (Default):** no logging.
  * **DEBUG:** logs detailed information, typically of interest only when diagnosing problems. Logs RPC requests and responses.
  * **INFO:** confirms that things are working as expected.
  * **WARNING:** an indication that something unexpected happened (for example, 'disk space low'), but the software is still working.
  * **ERROR:** due to a more serious problem, the software isn't able to perform some function.
  * **CRITICAL:** a serious error, indicating that the program itself might be unable to continue running.



#### Log destination (`-f` / `--log_file`)

You can select the following log destinations:

  * **File path:** if provided (for example, `-f /tmp/alloydbctl.log`), logs are written to the specified file.
  * **Standard output:** if not provided, logs are printed to the console (stdout).



#### Example

The following example uses `alloydbctl` to apply deployment and resource specifications while enabling DEBUG level logging. The logs, including detailed information and RPC requests/responses, are written to the file `/tmp/alloydbctl_debug.log` instead of the standard output.
    
    
    alloydbctl apply -d deployment_spec.yaml -r resource_spec.yaml -l DEBUG -f /tmp/alloydbctl_debug.log

### Obtain Ansible debug logs

The Ansible Orchestrator generates logs from Ansible tasks and Ansible modules. You can pass standard Ansible command line arguments to change the logging behavior for both tasks and modules. For more detailed information, see the [`ansible-playbook` documentation](https://docs.ansible.com/projects/ansible/latest/cli/ansible-playbook.html).

#### Log level for Ansible modules

By default, logs are sent to the console where the playbook is running.

To set the `log_level` configuration setting, run the following:
    
    
    ansible-playbook -i inventory.yaml bootstrap.yaml \
      -e resource_spec=resource_spec.yaml \
      -e log_level=DEBUG
    

You can also use the following standard Ansible verbosity flags to control output verbosity:

  * **`-v`:** basic verbosity (INFO level logs).
  * **`-vv` or higher:** increased verbosity (DEBUG level logs).



For example:
    
    
    ansible-playbook -i inventory.yaml bootstrap.yaml \
      -e resource_spec=resource_spec.yaml \
      -vv
    

#### Log path for Ansible modules

By default, logs aren't captured and the log level must be configured to capture logs in the log file.

To save the Ansible output to a log file, run the following to set the `log_path` configuration:
    
    
    ansible-playbook -i inventory.yaml bootstrap.yaml \
      -e resource_spec=resource_spec.yaml \
      -e log_file=/tmp/ansible-module.log
    

## Reset failed systemd instances

If the debug dump shows stale, failed service instances, clear them by running the following command on the affected cluster node:
    
    
    sudo systemctl reset-failed

To reset a specific systemd service, specify the service instance name:
    
    
    sudo systemctl reset-failed INSTANCE_NAME

Replace `INSTANCE_NAME` with the name of the systemd service instance-for example, `alloydbomni18@abc.service`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
