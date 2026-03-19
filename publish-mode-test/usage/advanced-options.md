# Advanced Options

Configuration options for power users.

## Custom workflows

Workflows can be configured per site. Navigate to **Settings → Workflows** and define states and transitions.

## Scheduled ingestion

Set the ingestion source to **Enabled** and configure a CRON expression under **Settings → Ingestion Sources → Schedule**.

## Taxonomy tags

All content ingested from GitHub inherits the taxonomy tags configured on the ingestion source. Tags can be updated on the source and re-ingestion will apply them to existing content.

## Troubleshooting

If content does not appear after ingestion, check:
- The ingestion source is enabled
- The branch and root directory are correctly set
- The completion action is set to **Publish** for immediate live content
