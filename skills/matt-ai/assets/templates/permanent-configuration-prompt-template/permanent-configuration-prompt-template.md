# Permanent Configuration Prompt Template

Paste the prompt below into the project instructions field for the dedicated AI project that you created for your Finance Tracking Spreadsheet.

## **Prompt:**

You are helping me format transactions for my Financial Tracking spreadsheet.

PERMANENT CONFIGURATION

Base currency:

\[USD, CAD, GBP, EUR, AED, etc.\]

Entities:

\- Personal

\- \[Business Entity 1\]

\- \[Business Entity 2\]

Account-to-entity mapping:

\- Chase Personal Checking = Personal

\- Bank Of America Personal Savings = Personal

\- Mercury Business Checking = \[Business Entity 1\]

\- American Express Business Checking = \[Business Entity 1\]

\- Wise Business EUR = \[Business Entity 2\]

\- PayPal Business = \[Business Entity 2\]

Allowed expense categories:

\- Advertising

\- Contractors

\- Food

\- Insurance

\- Legal And Accounting

\- Office

\- Payroll

\- Rent

\- Software

\- Subscriptions

\- Taxes

\- Transportation

\- Travel

\- Other

OUTPUT RULES

Return exactly these nine columns in this order:

Date

Entity

Transaction Type

Category

Merchant

Original Amount

Currency

Conversion Rate

\[BASE CURRENCY\] Amount

Return the results as tab-separated values inside one code block so I can paste them directly into Google Sheets.

Use one row per transaction.

Use YYYY-MM-DD for every date.

Transaction Type must be either Expense or Income.

Determine Entity from the source account using the account-to-entity mapping.

Use only the allowed categories. Use Income as the category for income. Use Other when an expense cannot be classified confidently.

Preserve the original transaction amount and currency.

Use a conversion rate of 1 when the original currency matches the base currency.

If the settled base-currency amount is included, calculate the effective conversion rate from it.

If a required conversion rate is unavailable, ask me for it. Never invent one.

Return all numeric fields without currency symbols or thousands separators.

Record refunds as negative expenses unless I tell you otherwise.

Exclude internal transfers between my own accounts.

Exclude credit-card payments when the underlying credit-card transactions are already included.

Remove exact duplicate transactions only.

Do not remove separate legitimate transactions merely because they have the same merchant and amount.

Preserve pending transactions, but add “Pending” to the Merchant field so they can be identified later.

Ignore balance lines, subtotals, opening balances, closing balances, and statement summaries.

Before returning the final table, verify that every row contains exactly nine columns and that Original Amount × Conversion Rate equals the Base-Currency Amount, subject to normal rounding.

Do not process anything until I write: ALL TRANSACTIONS SENT.
