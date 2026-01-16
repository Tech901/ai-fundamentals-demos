# Memphis Data Hub: Bike Facilities

This data set is from the [Memphis Data Hub](https://data.memphistn.gov):
- [Bike Facilities Existing and Programmed](https://data.memphistn.gov/datasets/eec74e9a53d24fcc953ed368c3538440_0/explore?location=35.050363%2C-89.735548%2C10.91).

## Files

This folder contains the same dataset exported in multiple formats:

- `Bike_Facilities_Existing_and_Programmed_9013950368666529764.csv`
  - Tabular CSV export (recommended for Azure ML Studio / Designer).
- `Bike_Facilities_Existing_and_Programmed_-8059126702258668379.xlsx`
  - Excel export (same fields as the CSV).
- `Bike_Facilities_Existing_and_Programmed_2171051057583135019.geojson`
  - GeoJSON `FeatureCollection` with `LineString` geometries + per-feature properties.
- `Bike_Facilities_Existing_and_Programmed_-1380518132303616096.txt`
  - Esri JSON / ArcGIS "Feature Collection" export (attributes + geometry paths).

## Columns

### CSV / XLSX columns

- `FID` (integer): feature id
- `objectid_1`, `objectid` (integer): source system ids
- `facility_n` (string): facility/road/segment name
- `begin`, `end` (string): segment start/end street names
- `facility_c` (string): facility category (example values: `Bike Lane`, `Buffered Bike Lane`, `Paved Shoulder`, `Marked Shared Roadway`)
- `status` (string): whether the facility is `Existing` or planned/programmed
- `route_id` (string): route identifier (often blank)
- `bpp_2005` (string): legacy plan field (often blank)
- `local_plan` (string): local plan/program reference (example values: `2016CIP`, `2015CIP`)
- `jurisdicti` (string): jurisdiction (example: `Memphis`)
- `st` (string): state (example: `TN`)
- `note` (string): notes (often blank)
- `miles` (number): segment length in miles
- `priority` (string): priority field (often blank)
- `yr_constr` (number): year constructed (0/blank when unknown)
- `i269`, `blvd`, `divided` (string): additional flags (often blank)
- `fund_sourc` (string): funding source (example: `Local`)
- `shape_leng`, `shape_le_1`, `Shape__Length` (number): GIS length fields from the export

### GeoJSON fields

- Geometry: `LineString` coordinates (CRS is listed as `EPSG:4326`).
- Properties: largely match the CSV/XLSX fields; note that `begin`/`end` appear as `begin_`/`end_` in the GeoJSON export.
