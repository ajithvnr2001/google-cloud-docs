---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/deploy-wsfc-create-ag/
title: Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:12.893205+00:00
---

# Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/configure-availability-groups-shared/deploy-wsfc-create-ag/




Stay organized with collections  Save and categorize content based on your preferences. 

## Create an availability group

You can now create a sample database `bookshelf`, include it in a new availability group named `bookshelf-ag` and configure high availability.

### Create a database

Create a new database using the following steps. For the purpose of this tutorial, the database doesn't need to contain any data.

  1. Return to the Remote Desktop session on `node-1`.
  2. Open the **SQL Server Management Studio**.
  3. In the **Connect to server** dialog, verify the server name is set to `node-1` and select **Connect**.
  4. In the menu, select **File > New > Query with current connection**.
  5. Paste the following SQL script into the editor.
         
         -- Create a sample database
         CREATE DATABASE bookshelf ON PRIMARY (
           NAME = 'bookshelf',
           FILENAME='d:\Data\bookshelf.mdf',
           SIZE = 256MB,
           MAXSIZE = UNLIMITED,
           FILEGROWTH = 256MB)
         LOG ON (
           NAME = 'bookshelf_log',
           FILENAME='d:\Logs\bookshelf.ldf',
           SIZE = 256MB,
           MAXSIZE = UNLIMITED,
           FILEGROWTH = 256MB)
         GO
         
         USE [bookshelf]
         SET ANSI_NULLS ON
         SET QUOTED_IDENTIFIER ON
         GO
         
         -- Create sample table
         CREATE TABLE [dbo].[Books] (
           [Id] [bigint] IDENTITY(1,1) NOT NULL,
           [Title] [nvarchar](max) NOT NULL,
           [Author] [nvarchar](max) NULL,
           [PublishedDate] [datetime] NULL,
           [ImageUrl] [nvarchar](max) NULL,
           [Description] [nvarchar](max) NULL,
           [CreatedById] [nvarchar](max) NULL,
           CONSTRAINT [PK_dbo.Books] PRIMARY KEY CLUSTERED ([Id] ASC) WITH (
             PAD_INDEX = OFF,
             STATISTICS_NORECOMPUTE = OFF,
             IGNORE_DUP_KEY = OFF,
             ALLOW_ROW_LOCKS = ON,
             ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
         ) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
         GO
         
         -- Create a backup
         EXEC dbo.sp_changedbowner @loginame = 'sa', @map = false;
           ALTER DATABASE [bookshelf] SET RECOVERY FULL;
           GO
           BACKUP DATABASE bookshelf to disk = '\\witness\Backup\bookshelf.bak' WITH INIT
         GO
         

The script creates a new database with a single table and performs an initial backup to `witness`.

  6. Select **Execute** to run the SQL script.




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
