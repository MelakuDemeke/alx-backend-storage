-- This SQL statement creates an index named idx_name_first on the 'names' table, which indexes the first character of the 'name' column.
CREATE INDEX idx_name_first
ON names (name(1));
