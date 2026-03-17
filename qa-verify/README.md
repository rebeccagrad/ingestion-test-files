# DXC-202 Test Playbook

This playbook tests the fix for DXC-202: Playbook body should update correctly when README.md changes, even when the Playbook is in draft/non-published state.

## About This Test

Fresh content to establish a clean baseline. The Playbook will be ingested in draft state with two chapters from the topic files below.

## What We Are Testing

When this README body is modified and an incremental ingestion runs, the Playbook body should update without throwing a ValidationException — regardless of whether the Playbook is in draft or published state.