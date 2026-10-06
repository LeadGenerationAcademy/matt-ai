# Step #4: Database

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=b666ef5eaa094592983a38cb36ec2b64

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Connect your CRM to your customer database, so every deal that comes through your CRM automatically gets stored in your Database (e.g Airtable, Google Sheet, or app).

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/ffa937a2b72a48aa9d071c972adc97197abd936dd7bb4367a8648402033a3fee-md.png)

### Links

- [Zapier](https://zapier.com)
- [Close](https://www.close.com)
- [Airtable](https://airtable.com)
- [Google Sheets](https://sheets.google.com)

### Step-by-Step Instructions

1. **Create a column called "Opportunity ID" in your database.** This is the lookup field that matches the opportunity ID in your CRM to the right record in your database, for the most accuracy and no duplicates.
2. **Create a fake lead manually in your CRM and place it in any opportunity status.** This is an instant trigger, meaning the Zap fires as soon as a new event happens. Without a fresh lead sitting in an opportunity status, you may not see any lead come through when you test the trigger.
3. **Log in to [Zapier](https://zapier.com), then click Create, then click Zaps.** This is where you'll be building the automation.
4. **Set your CRM (e.g. Close) as the trigger app, set the trigger event to New Opportunity in Status, then connect your account.** This updates your database every time an opportunity moves to a new stage. The connection lets Zapier read opportunity data from your CRM.
5. **Leave every field on the Configure tab blank except Trigger on Opportunity Creation, and set that field to Yes.** None of the status fields need a value for this automation to work. Setting this to Yes makes the automation fire when a new opportunity is created, as well as when one moves to a new status.
6. **Click Continue, then click Test trigger.** You should find the fake lead you created in step 2. You need a real, tested opportunity on file before you can map any of its fields in the action step.
7. **Click the + button to add an action step. Set whichever app hosts your database (e.g. Airtable or Google Sheets) as the action app, set the action event to Create or Update Record, then connect your account.** If an existing record matches the opportunity ID, that record gets updated. If no match is found, a new record is created instead.
8. **Choose where in your database you want the records stored.** Pick whichever base or sheet you actually keep your customer data in.
9. **Set the primary lookup field to "Opportunity ID" and leave the secondary lookup field empty.** This is the column you created in step 1. You don't need the secondary lookup field.
10. **Insert the opportunity ID from your CRM into the Opportunity ID field.** Click the + button, or press "/", and search "opportunity" to find it. In Close, this is the field labeled ID that starts with "oppo_". This keeps every record matched to the right opportunity in your CRM.
11. **Insert the rest of your CRM data into the matching fields.** Click the + button, or press "/", then select the data from your CRM for each field you want stored. What you log will differ from business to business, so map whatever your business actually tracks. Do not type these in manually. Typed text won't pull real data.
12. **Click Continue, then click Test step.** This sends a real test record using the mapped data from your fake lead.
13. **Go back to your database and confirm every field is filled out correctly.** Make sure nothing is missing or mismatched before you publish.
14. **If it works, publish the automation. If not, ask ChatGPT or Claude to diagnose the problem.** Only publish once you've confirmed the record actually appears in your database with the correct data.

### Completion Audit

- Did you create a column called "Opportunity ID" in your database?
- Did you create a fake lead manually in your CRM and place it in any opportunity status?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set your CRM as the trigger app, set the trigger event to New Opportunity in Status, and connect your account?
- Did you leave every field on the Configure tab blank except Trigger on Opportunity Creation, and set that field to Yes?
- Did you click Continue, then click Test trigger?
- Did you add an action step, set your database app as the action app, set the action event to Create or Update Record, and connect your account?
- Did you choose where in your database you want the records stored?
- Did you set the primary lookup field to "Opportunity ID" and leave the secondary lookup field empty?
- Did you insert the opportunity ID from your CRM into the Opportunity ID field?
- Did you insert the rest of your CRM data into the matching fields?
- Did you click Continue, then click Test step?
- Did you go back to your database and confirm every field is filled out correctly?
- Did you publish the automation, or diagnose the problem if it didn't work?
