WITH RECURSIVE tree AS (
    SELECT Name, Id, ARRAY[]::varchar[] AS Ancestors
    FROM Account.csv WHERE ParentId IS NULL

    UNION ALL

    SELECT a.Name, a.Id, tree.Ancestors || [a.ParentId]
    FROM Account.csv a, tree
    WHERE a.ParentId = tree.Id
)
SELECT * FROM tree;