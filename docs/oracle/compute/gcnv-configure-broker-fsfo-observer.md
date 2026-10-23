---
url: https://docs.cloud.google.com/oracle/compute/gcnv-configure-broker-fsfo-observer/
title: Configure Data Guard Broker, Fast-Start Failover, and Observer for Oracle Database on NetApp Volumes \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:53.979880+00:00
---

# Configure Data Guard Broker, Fast-Start Failover, and Observer for Oracle Database on NetApp Volumes  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-configure-broker-fsfo-observer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Configure Data Guard Broker, Fast-Start Failover, and Observer for Oracle Database on NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Oracle Data Guard Broker and Fast-Start Failover with a dedicated Observer to enable automatic role transitions for Oracle Database 26ai on Google Cloud NetApp Volumes.

Complete the following steps:

  1. Enable Data Guard broker.
  2. Confirm flashback for Fast-Start Failover (FSFO).
  3. Configure and enable FSFO.
  4. Install Instant Client on the Observer.
  5. Run Observer as a `systemd` service.
  6. Test FSFO.



## Enable Data Guard broker

On both the primary and standby databases, enable the Data Guard Broker and create the broker configuration that links the primary and standby databases under unified management.

  1. Set `dg_broker_start=TRUE` on the primary and standby database hosts.
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         sqlplus / as sysdba <<SQL
         ALTER SYSTEM SET dg_broker_start=TRUE SCOPE=BOTH;
         EXIT
         SQL'
         

  2. On the primary database, connect to `DGMGRL` with OS authentication and create the broker configuration.

**Note:** On the Observer host only, use `dgmgrl /@orcl` after the auto-login wallet exists. Don't use passwords on the `dgmgrl` command line.
         
         sudo -u oracle bash -c '
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export ORACLE_SID=orcl
         export PATH=$ORACLE_HOME/bin:$PATH
         dgmgrl /
         '
         
         DGMGRL> CREATE CONFIGURATION 'orcl_dg' AS
                 PRIMARY DATABASE IS 'orcl' CONNECT IDENTIFIER IS orcl;
         DGMGRL> ADD DATABASE 'orcls' AS CONNECT IDENTIFIER IS orcls;
         DGMGRL> ENABLE CONFIGURATION;
         DGMGRL> SHOW CONFIGURATION;
         -- Expect: Configuration Status: SUCCESS, both members SUCCESS.
         

  3. Validate the configuration and fix any `WARNING` or non-NULL `ERROR` before Step: Configure and enable FSFO.
         
         DGMGRL> VALIDATE DATABASE 'orcls';
         DGMGRL> SHOW CONFIGURATION VERBOSE;




## Confirm flashback for FSFO

Confirm that flashback database is enabled on both hosts. Flashback is required for Fast-Start Failover (FSFO) auto-reinstate, which allows the former primary to automatically rejoin the configuration as a standby after a failover.

  1. Confirm that the `flashback_on` is `YES` on both database hosts.
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         sqlplus -s / as sysdba <<<"SELECT flashback_on FROM v\$database;"
         '
         # Expected on both hosts: YES

  2. On the primary only, set flashback retention if not already set.
         
         sudo -u oracle bash -c '
         . ~/.bash_profile
         export ORACLE_SID=orcl
         sqlplus / as sysdba <<SQL
         ALTER SYSTEM SET db_flashback_retention_target=1440 SCOPE=BOTH;
         EXIT
         SQL'
         




## Configure and enable FSFO

  1. Set the redo transport mode to `SYNC` on both databases and raise the protection mode to `MaxAvailability`.
         
         -- Transport mode and protection mode
         DGMGRL> EDIT DATABASE 'orcl'  SET PROPERTY LogXptMode='SYNC';
         DGMGRL> EDIT DATABASE 'orcls' SET PROPERTY LogXptMode='SYNC';
         DGMGRL> EDIT CONFIGURATION SET PROTECTION MODE AS MaxAvailability;

  2. Set the FSFO targets so each database names the other as its failover target, then configure the threshold and auto-reinstate behavior.
         
         -- FSFO targets (each side names the other)
         DGMGRL> EDIT DATABASE 'orcl'  SET PROPERTY FastStartFailoverTarget = 'orcls';
         DGMGRL> EDIT DATABASE 'orcls' SET PROPERTY FastStartFailoverTarget = 'orcl';
         -- 30 s = default; lower for faster RTO but more sensitive to network blips
         DGMGRL> EDIT CONFIGURATION SET PROPERTY FastStartFailoverThreshold = 30;
         DGMGRL> EDIT CONFIGURATION SET PROPERTY FastStartFailoverAutoReinstate = TRUE;

  3. Enable FSFO and confirm the configuration.
         
         DGMGRL> ENABLE FAST_START FAILOVER;
         DGMGRL> SHOW FAST_START FAILOVER;
         -- Expected: Threshold 30 seconds, Target orcls, Observer not yet registered.




## Install Instant Client on the Observer

  1. On the Observer host `oradg-obs`, install Oracle Instant Client packages.
         
         # Use -el8 / -el9 if the Observer is on an older OL/RHEL release
         sudo dnf install -y oracle-instantclient-release-el10
         sudo dnf install -y oracle-instantclient-basic \
                             oracle-instantclient-sqlplus \
                             oracle-instantclient-tools

  2. Create a dedicated `oracle` OS user that will own the wallet and the systemd unit.
         
         sudo useradd -u 54321 -m oracle
         sudo passwd -l oracle

  3. On Observer, configure the Oracle Net environment.
         
         sudo mkdir -p /etc/oracle/network/admin
         sudo chown -R oracle:oracle /etc/oracle
         sudo -u oracle tee /home/oracle/.bash_profile >/dev/null <<'EOF'
         export ORACLE_HOME=/usr/lib/oracle/26/client64
         export LD_LIBRARY_PATH=$ORACLE_HOME/lib
         export PATH=$ORACLE_HOME/bin:$PATH
         export TNS_ADMIN=/etc/oracle/network/admin
         EOF

  4. Configure TNS Names for Observer.
         
         # tnsnames.ora must reach both DB hosts on TCP/1521 (see Step 8.2 for full DB-host file)
         sudo tee /etc/oracle/network/admin/tnsnames.ora >/dev/null <<'EOF'
         orcl =
           (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = oracdb1)(PORT = 1521))
                           (CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = orcl)))
         orcls =
           (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = oracdb2)(PORT = 1521))
                           (CONNECT_DATA = (SERVER = DEDICATED)(SERVICE_NAME = orcls)))
         EOF
         sudo chown oracle:oracle /etc/oracle/network/admin/tnsnames.ora




## Run Observer as a `systemd` service

Create an auto-login wallet with credentials for both database members, then configure and start the Observer as a `systemd` service so it survives reboots and automatically reconnects to the configuration.

Store credentials for a dedicated Data Guard administrative account (for example, `SYSDG`) in the wallet rather than `SYS`. Credentials must never appear on a `dgmgrl` command line, where they are visible to `ps` and `journalctl`, always connect using `/@<tns_alias>` on the Observer.

  1. Create the encrypted wallet and populate credentials for both database members.
         
         sudo -iu oracle bash <<'BASH'
         mkdir -p $TNS_ADMIN/wallet
         mkstore -wrl $TNS_ADMIN/wallet -create     # prompts for a wallet password can be stored in your secret manager
         mkstore -wrl $TNS_ADMIN/wallet -createCredential orcl  sys ChangeMe!1
         mkstore -wrl $TNS_ADMIN/wallet -createCredential orcls sys ChangeMe!1
         BASH

  2. Configure `sqlnet.ora` for wallet authentication.
         
         sudo tee /etc/oracle/network/admin/sqlnet.ora >/dev/null <<'EOF'
         WALLET_LOCATION = (SOURCE = (METHOD = FILE) (METHOD_DATA = (DIRECTORY = /etc/oracle/network/admin/wallet)))
         SQLNET.WALLET_OVERRIDE = TRUE
         EOF
         sudo chown oracle:oracle /etc/oracle/network/admin/sqlnet.ora

  3. Verify wallet and test connectivity.
         
         sudo -iu oracle ls -l /etc/oracle/network/admin/wallet
         # Expected: cwallet.sso and ewallet.p12
         
         sudo -iu oracle bash <<'BASH'
         sqlplus -L "/@orcl as sysdba" <<'SQL'
         SELECT database_role FROM v$database;
         EXIT
         SQL
         BASH
         
         sudo -iu oracle bash <<'BASH'
         sqlplus -L "/@orcls as sysdba" <<'SQL'
         SELECT database_role FROM v$database;
         EXIT
         SQL
         BASH
         
         sudo -iu oracle dgmgrl /@orcl  'SHOW CONFIGURATION;'
         sudo -iu oracle dgmgrl /@orcls 'SHOW CONFIGURATION;'
         

  4. Generate the auto-login wallet (`cwallet.sso`) so the Observer `systemd` service can start without a password prompt. If `cwallet.sso` is missing after running `mkstore`, use `orapki` from the Instant Client tools package or a database home to create it, then re-add the stored credentials.
         
         sudo -iu oracle orapki wallet create \
           -wallet /etc/oracle/network/admin/wallet \
           -auto_login
         sudo -iu oracle ls -l /etc/oracle/network/admin/wallet
         # Expected: cwallet.sso and ewallet.p12

  5. Create the `systemd` unit, enable the service, and verify that the Observer is connected.
         
         sudo tee /etc/systemd/system/dgmgrl-observer.service >/dev/null <<'EOF'
         [Unit]
         Description=Oracle Data Guard Fast-Start Failover Observer
         After=network-online.target
         Wants=network-online.target
         [Service]
         Type=simple
         User=oracle
         Group=oracle
         Environment=ORACLE_HOME=/usr/lib/oracle/26/client64
         Environment=LD_LIBRARY_PATH=/usr/lib/oracle/26/client64/lib
         Environment=TNS_ADMIN=/etc/oracle/network/admin
         Environment=PATH=/usr/lib/oracle/26/client64/bin:/usr/bin:/bin
         ExecStart=/usr/lib/oracle/26/client64/bin/dgmgrl -silent /@orcl "START OBSERVER FILE IS '/var/lib/oracle/dgmgrl-observer.dat'"
         Restart=always
         RestartSec=5
         [Install]
         WantedBy=multi-user.target
         EOF

  6. Create Observer data directory and log file.
         
         sudo install -d -o oracle -g oracle -m 0755 /var/lib/oracle
         sudo install -o oracle -g oracle -m 0640 /dev/null /var/log/dgmgrl-observer.log

  7. Configure Observer Log Rotation.
         
         sudo tee /etc/logrotate.d/dgmgrl-observer >/dev/null <<'EOF'
         /var/log/dgmgrl-observer.log {
             weekly
             rotate 8
             compress delaycompress missingok notifempty
             create 0640 oracle oracle
             copytruncate
         }
         EOF

  8. Enable and start Observer service.
         
         sudo systemctl daemon-reload && sudo systemctl enable --now dgmgrl-observer.service
         sudo systemctl status dgmgrl-observer.service

  9. Verify from the primary that the Observer reads `CONNECTED`. A `DISCONNECTED` Observer silently suspends FSFO.
         
         DGMGRL> SHOW FAST_START FAILOVER;
         DGMGRL> SHOW CONFIGURATION;       -- Configuration Status: SUCCESS, FSFO: ENABLED




## Test FSFO

Validate the Oracle Data Guard configuration with `VALIDATE DATABASE`, then perform a planned switchover and, in a test window, an unplanned VM-reset failover to confirm FSFO is working end to end.

  1. Test a planned switchover and restore the original topology:
         
         DGMGRL> VALIDATE DATABASE 'orcls';
         DGMGRL> SWITCHOVER TO 'orcls';
         DGMGRL> SHOW CONFIGURATION;
         DGMGRL> SWITCHOVER TO 'orcl';        -- restore topology

  2. Test an unplanned failover using a VM reset in a controlled test window:

     1. Use a VM **Reset** (crash-style test) in a test window. A normal **Stop** may not trigger FSFO.
     2. Tail `/var/log/dgmgrl-observer.log` on `oradg-obs`.
     3. Restore topology when done.



Oracle Data Guard Broker, FSFO, and Observer configuration is now configured for this deployment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
