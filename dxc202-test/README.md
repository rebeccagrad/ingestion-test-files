# DXC-202 Test Playbook

This playbook is used to verify the fix for DXC-202: Playbook body should update correctly when README.md changes, regardless of publish state.

## About This Test

Created fresh to ensure no prior revision history. The Playbook will be ingested in draft state with chapters from the topic files below.

## What We Are Testing

When this README body is modified and an incremental ingestion runs, the Playbook body should update without throwing a ValidationException.
