WITH Contacts AS (
    SELECT
    AccountId, Email, CONCAT_WS(' ', FirstName, LastName) AS Name
    FROM Contact.csv
),
Accounts AS (
    SELECT
    a.Id, a.Name AS AccountName,
    (SELECT Name FROM Account.csv WHERE Id = a.ParentId) AS ParentAccountName
    FROM Account.csv a
)
SELECT
c.*, a.AccountName, a.ParentAccountName
FROM Accounts a
JOIN Contacts c ON c.AccountId = a.Id
WHERE ParentAccountName IS NOT NULL
LIMIT 20;