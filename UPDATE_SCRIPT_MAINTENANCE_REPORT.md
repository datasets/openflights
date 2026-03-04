# Update Script Maintenance Report

Date: 2026-03-04

- Added a reproducible file-sync updater at `scripts/sync_data.py` to pull snapshot `.dat` files directly from upstream OpenFlights (`jpatokal/openflights`).
- Added dependency file `scripts/requirements.txt`.
- Added first GitHub Actions automation at `.github/workflows/actions.yml` with:
  - daily schedule,
  - manual dispatch,
  - `contents: write` permissions,
  - commit-if-changed behavior for `data/*.dat`.
- This replaces the old database-coupled airport update path (`data/update_airports.py`) for repository freshness use-cases.
