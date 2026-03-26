# DXC Publish Mode Test Playbook

This playbook is a clean test fixture for verifying GitHub ingestion behavior when the completion action is set to **Publish**.

## What this tests

- Playbook created from README.md (this file)
- Topics ingested from `.md` files in subdirectories
- Chapter hierarchy built from folder structure
- All content published immediately (no draft state)

## Expected result

After ingestion with the completion action set to Publish (DXC-209 QA run):
- This Playbook should be live in the CMS
- All five Topics should be live (not draft)
- Chapter structure should reflect the folder tree below
