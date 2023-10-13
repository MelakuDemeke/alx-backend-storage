-- This SQL statement creates an index named idx_name_first_score on the 'names' table.
-- It indexes the first character of the 'name' column and the 'score' column, facilitating efficient querying based on these attributes.
CREATE INDEX idx_name_first_score
ON names (name(1), score);
