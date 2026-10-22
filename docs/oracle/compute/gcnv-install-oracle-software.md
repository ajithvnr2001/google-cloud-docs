---
url: https://docs.cloud.google.com/oracle/compute/gcnv-install-oracle-software/
title: Install Oracle software \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:52.987499+00:00
---

# Install Oracle software  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-install-oracle-software/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Install Oracle software Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to install Oracle software.

To install Oracle software, complete the following tasks:

  1. Install Oracle Grid Infrastructure.
  2. Install Oracle Database 26ai.



## Install Oracle Grid Infrastructure

Install the Oracle Grid Infrastructure GoldImage on each database host to enable Oracle Restart and ASM. Both hosts require their own Grid home, ASM instance, and disk groups.

Oracle Data Guard replicates data over Oracle Net, not over shared storage. 

Perform the following steps on `oracdb1`, and then on `oracdb2`.

  1. Stage the Oracle GoldImages, Release Update, and OPatch binaries on `/u01/stage`.
         
         sudo chown oracle:oinstall /u01/stage && sudo chmod 775 /u01/stage

  2. Extract the Grid GoldImage in the target Grid home. The 26ai Grid GoldImage installs by extracting in the target Grid home:
         
         sudo -u grid bash -c '
         cd /u01/app/26ai/grid
         unzip -q /u01/stage/LINUX.X64_<RELEASE>_grid_home.zip
         '
         sudo chown -R grid:oinstall /u01/app/26ai/grid

If the Grid GoldImage is older than the target Release Update, patch the Grid home during setup using the `gridSetup.sh -applyRU` flow, or use a GoldImage with the Release Update bundled. Keep Grid and Database homes at the same intended patch level.

  3. Build the `gridSetup` response file `/tmp/grid.rsp` on each host. Replace the hostname and use strong passwords.
         
         HOST=$(hostname -s)
         sudo -u grid bash -c "cat > /tmp/grid.rsp <<RSP
         oracle.install.responseFileVersion=/oracle/install/rspfmt_crsinstall_response_schema_v23.0.0
         INVENTORY_LOCATION=/u01/app/oraInventory
         installOption=HA_CONFIG
         ORACLE_BASE=/u01/app/grid
         clusterUsage=GENERAL_PURPOSE
         OSDBA=asmdba
         OSOPER=asmoper
         OSASM=asmadmin
         storageOption=FLEX_ASM_STORAGE
         sysasmPassword=WelcomeOracle1!
         asmsnmpPassword=WelcomeOracle1!
         diskGroupName=DATA
         redundancy=EXTERNAL
         auSize=4
         diskString=/dev/mapper/ora_${HOST}_*p*
         diskList=/dev/mapper/ora_${HOST}_data_01p1,/dev/mapper/ora_${HOST}_data_02p1
         managementOption=NONE
         RSP"
         sudo -u grid chmod 600 /tmp/grid.rsp

  4. Run `gridSetup.sh` in silent mode to copy the binaries and stage the configuration.
         
         sudo -u grid bash -c '
         export ORACLE_HOME=/u01/app/26ai/grid
         export ORACLE_BASE=/u01/app/grid
         cd /u01/app/26ai/grid
         ./gridSetup.sh -silent -responseFile /tmp/grid.rsp -ignorePrereqFailure
         '

Expected output is `Successfully Setup Software with warning(s) and exit code 6 (warnings) or 0`.

  5. Run `orainstRoot.sh` and `root.sh` as `root`. The `root.sh` script creates the `crsctl`, `srvctl`, and `asmcmd` wrappers and brings up OHAS.
         
         sudo /u01/app/oraInventory/orainstRoot.sh
         sudo /u01/app/26ai/grid/root.sh

  6. Run `gridSetup.sh -executeConfigTools` to run the configuration assistants (NETCA, ASMCA, CVU) against the response file. This creates the ASM instance and the `+DATA` disk group.
         
         sudo -u grid bash -c '
         export ORACLE_HOME=/u01/app/26ai/grid
         export ORACLE_BASE=/u01/app/grid
         cd /u01/app/26ai/grid
         ./gridSetup.sh -silent -executeConfigTools -responseFile /tmp/grid.rsp
         '

Expected output is `Successfully Configured Software`.

  7. Create the `+RECO` and `+FRA` disk groups using `asmca`. The single-shot install only creates `+DATA`. `Create the other two through`asmca`.
         
         HOST=$(hostname -s)
         sudo -u grid bash -c "
         export ORACLE_HOME=/u01/app/26ai/grid
         export ORACLE_SID=+ASM
         \$ORACLE_HOME/bin/asmca -silent -createDiskGroup \
           -diskGroupName RECO \
           -disk /dev/mapper/ora_${HOST}_arch_01p1 \
           -redundancy EXTERNAL -au_size 4
         \$ORACLE_HOME/bin/asmca -silent -createDiskGroup \
           -diskGroupName FRA \
           -disk /dev/mapper/ora_${HOST}_fra_01p1 \
           -redundancy EXTERNAL -au_size 4
         "

  8. Verify the ASM disk groups and Oracle Restart resource status.
         
         sudo -u grid ORACLE_HOME=/u01/app/26ai/grid ORACLE_SID=+ASM \
           /u01/app/26ai/grid/bin/sqlplus -s / as sysasm <<'SQL'
         SELECT name, total_mb, free_mb, state FROM v$asm_diskgroup ORDER BY name;
         SQL
         sudo /u01/app/26ai/grid/bin/crsctl stat res -t
         # Expected ONLINE: `ora.DATA.dg`, `ora.RECO.dg`, `ora.FRA.dg`, `ora.LISTENER.lsnr`, `ora.asm`, `ora.cssd`, `ora.evmd`.

  9. Repeat steps 1 to 8 on `oracdb2`.

Use the same ASM disk group names. Oracle Data Guard replicates over Oracle Net, not storage.




## Install Oracle Database 26ai

Install the Oracle Database 26ai software home on each database host using a silent, software-only installation with the latest Release Update applied. 

Perform all steps on `oracdb1`, and then on `oracdb2`.

  1. Extract the Database home, the latest OPatch, and the RU patch into their respective directories. Refer to the Oracle documentation for RU directory layout and the `-applyRU` path.
         
         sudo su - oracle
         cd /u01/app/oracle/product/26ai/db_1
         unzip -q /u01/stage/LINUX.X64_<RELEASE>_db_home.zip
         rm -rf OPatch
         unzip -q /u01/stage/p6880880_<base>_Linux-x86-64.zip                    # latest OPatch
         unzip -q /u01/stage/p<RU_PATCH>_<base>_Linux-x86-64.zip -d /u01/stage   # latest 26ai RU

  2. Write the install response file and run the silent software-only installation with the RU applied. 
         
         sudo -u oracle tee /u01/stage/dbinstall.rsp >/dev/null <<'EOF'
         oracle.install.option=INSTALL_DB_SWONLY
         UNIX_GROUP_NAME=oinstall
         INVENTORY_LOCATION=/u01/app/oraInventory
         ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         ORACLE_BASE=/u01/app/oracle
         oracle.install.db.InstallEdition=EE
         oracle.install.db.OSDBA_GROUP=dba
         oracle.install.db.OSOPER_GROUP=oper
         oracle.install.db.OSBACKUPDBA_GROUP=backupdba
         oracle.install.db.OSDGDBA_GROUP=dgdba
         oracle.install.db.OSKMDBA_GROUP=kmdba
         oracle.install.db.OSRACDBA_GROUP=racdba
         oracle.install.db.rootconfig.executeRootScript=false
         EOF

  3. Run Oracle Database Installer.

**Note:** On OL 8 and 9, omit `-applyOneOffs` from the `runInstaller` line.
         
         sudo -u oracle bash -c '
         export CV_ASSUME_DISTID=OEL10    # OEL9 / OEL8.10 if cluvfy requires it
         cd /u01/app/oracle/product/26ai/db_1
         ./runInstaller -applyRU /u01/stage/<RU_PATCH> -applyOneOffs /u01/stage/39292021 \
           -silent -ignorePrereqFailure -responseFile /u01/stage/dbinstall.rsp
         '

  4. As `root` user, run the post-install root script.
         
         sudo /u01/app/oracle/product/26ai/db_1/root.sh

  5. Set the Oracle environment on each database host. Use `ORACLE_SID=orcl` on `oracdb1` and `ORACLE_SID=orcls` on `oracdb2`.
         
         sudo -u oracle tee -a /home/oracle/.bash_profile >/dev/null <<'EOF'
         export ORACLE_HOME=/u01/app/oracle/product/26ai/db_1
         export ORACLE_SID=orcl                         # use 'orcls' on oracdb2
         export GRID_HOME=/u01/app/26ai/grid
         export PATH=$ORACLE_HOME/bin:$GRID_HOME/bin:$PATH
         export TNS_ADMIN=$ORACLE_HOME/network/admin
         EOF




## What's next

  * [Create the primary database](https://docs.cloud.google.com/oracle/compute/gcnv-create-primary-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
