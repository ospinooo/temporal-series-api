

# Influx docs


## Columns

- Time. (ALL tables)
- Field key. (not indexed, just values)
- Tag key. (are indexed) -> Typically enums.

## Measurement

- Container of tags, fields and time column
- Similar to SQL-table
- Can belong to different retention policies
  - How much time the data is available
  - How many copies there is

## Series

- Share a measurement, tag set, and field key
- Data that belongs to a measurement with a specific tag set and ONE field key.

Example
- 1 measurement
- 2 tags
- 3 fields
- TOTAL SERIES = 1 x (2x2) x 3

## Point

- Has measurement, tag set, field set, and a timestamp
- A Series is composed by some points.