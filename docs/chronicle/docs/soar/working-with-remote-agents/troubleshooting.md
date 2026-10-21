---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting/
title: Troubleshoot common issues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:44.274087+00:00
---

# Troubleshoot common issues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot common issues

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document provides a collection of tips and procedures to help you diagnose and resolve common issues encountered during the deployment and operation of the Google Security Operations Remote Agent.

## Key mismatch issue

This issue occurs when the private keys in Google Security Operations and the Remote Agent don't match. To solve this, make sure the key in the agent resources matches the key in the Siemplify `agent_db`.

## Remote connector failure

If a remote connector fails, follow these steps:

  1. Verify that an integrations instance is successfully installed on the agent.
  2. Check the agent logs at the error level to find any failures in the connection process.
  3. Test the same connector configuration locally and see if there are errors.



## Installation failure: Unsupported host OS or EOL incompatibilities

If fresh installations or automatic upgrades fail due to glibc tracking errors and system call blocks, follow these steps:

  1. Verify that the host environment is not running a legacy operating system, which may lack modern system call hooks.
  2. Re-host the agent environment on an enterprise Linux distribution with the latest official version.
  3. Ensure the host is a supported platform: Debian 12 (Official base), RHEL 8.7: 

Check `/etc/os-release`: Run the following command and look for `NAME=` and `VERSION_ID=`:
         
         cat /etc/os-release

     * For Debian 12: Look for `NAME="Debian GNU/Linux"` and `VERSION_ID="12"`.
     * For RHEL 8.7: Look for `NAME="Red Hat Enterprise Linux"` and `VERSION_ID="8.7"`.



## Container setup pulls previous operational layer instead of the "latest" build

If re-running container setup commands inadvertently pulls a previous operational layer instead of the newly released software build, run the following commands to explicitly pull the latest image:

  * For Docker:

`docker pull us-docker.pkg.dev/siem-ar-public/images/agent:latest `
  * For Podman:

`podman pull us-docker.pkg.dev/siem-ar-public/images/agent:latest`



To ensure that the deployment runs on the most up-to-date software release, always pull the latest image before you execute the agent run command.

## Docker agent deployment failure

If the Docker deployment fails, follow these steps:

  1. Remove the Docker container: 
     1. Run the following command to list the running containers:

`docker ps `
     2. Run the following command to remove the failed containers:

`docker rm -f container_id_or_name`
  2. Remove images: 
     1. Run the following command to list the images:

`docker images `
     2. Run the following command to remove the image:

`docker rmi image_id_or_name`
  3. Remove volumes: 
     1. Run the following command to list the volumes:

`docker volume ls`
     2. Run the following command to remove the volumes:

`docker volume rm volume_name`
  4. Redeploy the agent. For more information, see [Create an agent using Docker](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-agent-with-docker).



## Agent stuck in 'Waiting for agent' status

If the agent was successfully deployed but the status remains "waiting for agent", follow these steps to troubleshoot the issue:

  1. **Check host connectivity** : Test the Agent host machine's internet connectivity (for example, `curl www.google.com` or `ping 8.8.8.8`). If this fails, the issue is with the host's internet connection.
  2. **Check container connectivity** : If the host test passes, enter the container shell using `docker exec -it container_ID bash` and recheck connectivity. If the container lacks connectivity, restart the Docker service on the host machine (service docker restart).

     1. Run the following command:

`docker exec -it  bash`

     2. Check the connectivity again as you did previously. 
     3. If there is no connectivity, run the following command to restart the Docker service from the host machine (not the container): 

`service docker restart`

     4. Run the following command to start container again:

`docker start`

  3. Review container logs for errors

If the previous step did not help, and the agent status is still 'waiting for agent' after refreshing the **Remote agent** page in Google SecOps, log back in the container and pull the logs.

     1. Find the logs in the `/var/log/SiemplifyAgent/` directory.
     2. Look for any errors in the log files to identify the root cause.



## DNS networking issues

If the container experiences DNS resolution failures or network connectivity issues, add `--network host` to the `docker run` command. Using host network mode allows the container to share the host machine's network stack and DNS configuration directly.

**Note:** Host network mode only works with one agent per host machine. 

## Docker image fails to load (IP4 forwarding is disabled)

If you see an error in the CLI when you try to load a Google SecOps Docker image (system) or agent, IP4 forwarding might be disabled. Follow these steps to enable it and restart your agent:

  1. Add the following line to the `/etc/sysctl.conf` file:

`net.ipv4.ip_forward=1` Note that you will need to use a file editor (like nano for example use: `yum install nano -y`  

  2. Run the following command to restart network service:

`systemctl restart network`
  3. Run the following command to restart the Docker service:

`sudo systemctl restart docker`
  4. Run the following command to check if the container is running:

`docker ps`
  5. If the container is not running, run the following command to list all containers (including stopped ones):

`docker ps -a`
  6. If the container is listed but stopped, run the following command to start it:

`docker start container_id_or_name`
  7. If the agent or system is still not running after restarting Docker and the container: 
     1. Run the following command to stop the container:

`docker stop container_id_or_name`
     2. Run the following command to delete the container:

`docker rm container_id_or_name`
     3. Run the following command to delete the image:

`docker rmi image_name`
     4. Load the image again.



## Error after shutdown or reboot of Agent

Run the following command to force start of Installer agent:   
`systemctl start supervisord`

Run the following command to force start of the Docker agent:  
`docker start `

## Remote Agent tasks fail on hardened environments

When you deploy a Remote Agent on a hardened Linux host like RHEL 8, agent tasks (including saving or upgrading an integration, or running connectors and actions) might fail or time out in the UI while the agent status remains **Live**. This issue occurs when host OS security enforcement—such as SELinux in `Enforcing` mode, AppArmor, or endpoint security software—blocks OS commands executed by the agent inside the container.

To resolve this issue, the Remote Agent must be exempted from the host security enforcement policies that block its OS commands. Follow these steps to diagnose and resolve the issue:

  1. Verify whether SELinux is in `Enforcing` mode on the host machine:
         
         getenforce
         sestatus
         

To check `/var/log/audit/audit.log` for recent blocked commands or denied operations without returning the entire log file, run the following command:
         
         sudo grep -i "denied" /var/log/audit/audit.log | tail -n 50
         

You can also inspect your endpoint security logs on the host for blocked operations related to the agent container processes.

  2. Exempt the Remote Agent from the blocking security policy on the host:

     * For containerized deployments (Docker or Podman), exempt the entire Remote Agent container when starting it for the first time by adding `--security-opt label=disable` (for SELinux) or `--security-opt apparmor=unconfined` (for AppArmor) to your `docker run` or `podman run` command.
     * Configure custom SELinux policy rules, AppArmor profiles, or host endpoint security exemptions for the Remote Agent directories (`/opt/SiemplifyAgent`, `/home/siemplify_agent/agent_source`, and `/var/log/SiemplifyAgent`) and executables (`/usr/local/bin/python3.11`, `/usr/local/bin/pip3`, and `/usr/bin/supervisord`) so OS commands aren't blocked.
  3. Alternatively, if you can't configure a targeted SELinux exemption, set SELinux to `Permissive` mode persistently across reboots by setting `SELINUX=permissive` in `/etc/selinux/config` on the host.

If modifying `/etc/selinux/config` isn't possible or you need to apply the change immediately without rebooting, run the following command to switch SELinux to `Permissive` mode temporarily:
         
         sudo setenforce 0
         




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
