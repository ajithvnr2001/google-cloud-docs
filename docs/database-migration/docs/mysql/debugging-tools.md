---
url: https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools/
title: Debugging and other tools \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:15.908148+00:00
---

# Debugging and other tools  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/debugging-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Debugging and other tools Stay organized with collections  Save and categorize content based on your preferences. 

This page includes scripts that help with debugging and using MySQL.

## Find write activities
    
    
    #!/bin/bash
    
    # Tail the binlog and look for insert / update / delete
    # The goal is to help the user understand which writes are happening
    
    
    MYSQL=$(which mysql)
    MYSQLBINLOG=$(which mysqlbinlog)
    DATE=$(which date)
    
    if [[ -z "${MYSQL}" ]]
    then
      echo "ERROR: Could not find mysql shell"
      exit 1
    fi
    if [[ -z "${MYSQLBINLOG}" ]]
    then
      echo "ERROR: Could not find mysqlbinlog utility"
      exit 1
    fi
    
    if [[ -z "$1" ]]
    then
      echo "Usage: $0 [mysql connection parameters]"
      exit 1
    fi
    
    last_log=$("${MYSQL}" "$@" -N -B -e "SHOW BINARY LOGS;" | tail -n 1 | cut -f1)
    time=$("${DATE}" '+%Y-%m-%d %H:%M:%S')
    
    echo "Continuously reading from ${last_log} starting from ${time}"
    
    "${MYSQLBINLOG}" --base64-output=DECODE-ROWS --verbose --start-datetime="${time}" --read-from-remote-server "$@" "${last_log}" --stop-never | grep "INSERT\|UPDATE\|DELETE"
    

## Find `ALTER TABLE` commands
    
    
    #!/bin/bash
    
    # Search for DDL Commands in the last 24 hours. Should help the user understand
    # which DDL commands they are performing.
    
    MYSQL=$(which mysql)
    MYSQLBINLOG=$(which mysqlbinlog)
    DATE=$(which date)
    
    if [[ -z "${MYSQL}" ]]
    then
      echo "ERROR: Could not find mysql shell"
      exit 1
    fi
    
    if [[ -z "${MYSQLBINLOG}" ]]
    then
      echo "ERROR: Could not find mysqlbinlog utility"
      exit 1
    fi
    
    if [[ -z "$1" ]]
    then
      echo "Usage: $0 [mysql connection parameters]"
      exit 1
    fi
    
    log_files=$("${MYSQL}" "$@" -N -B -e "SHOW BINARY LOGS;" | cut -f1)
    
    yesterday=$("${DATE}" --date="-1 day" '+%Y-%m-%d %H:%M:%S')
    
    echo "Searching for DDL commands, starting at ${yesterday}"
    for file in ${log_files}
    do
      echo "Log file: ${file}"
      "${MYSQLBINLOG}" --start-datetime "${yesterday}" --read-from-remote-server "$@" "${file}" | grep -B 2 "ALTER TABLE\|CREATE TABLE\|TRUNCATE TABLE\|RENAME TABLE\|DROP TABLE"
    done
    

## Lock all tables
    
    
    #!/bin/bash
    
    # This script locks all non-system tables on a MySQL database.
    # Helps for the case where we cannot acquire read lock with flush.
    
    MYSQL="$(which mysql)"
    
    if [[ -z "${MYSQL}" ]]
    then
      echo "ERROR: Could not find mysql shell"
      exit 1
    fi
    
    if [[ -z "$1" ]]
    then
      echo "Usage: $0 [mysql connection parameters]"
      exit 1
    fi
    
    LOCK_TABLES_STMT="select concat('LOCK TABLES ', group_concat(concat('\`',table_schema,'\`.\`',table_name,'\` READ')),';') as stmt from information_schema.tables where table_schema not in ('mysql', 'sys', 'performance_schema', 'information_schema');"
    QUERY="$("${MYSQL}" "$@" -N -B -e "${LOCK_TABLES_STMT}")"
    
    (
     echo "${QUERY}"
     read -n 1 -r -s -p $'Tables locked, press any key to stop the session and UNLOCK TABLES\n'
     echo "UNLOCK TABLES;"
    ) | "${MYSQL}" "$@"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
