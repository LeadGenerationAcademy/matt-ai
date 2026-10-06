# Step #10: Call Summary > Follow Up Flow

Course: Step #5: Funnel Tech
System: Marketing System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=bf942b1fff484338a83be3111614d580

---
Video: this lesson has a video in Skool (open the Skool link to watch).

Call summary software like Read AI or Fathom automatically records and summarizes your sales calls.

This automation tags a prospect "Closed Lost" in your CRM and your email platform straight from their Call Summary meeting notes, and automatically enrolls them into your Follow Up Flow. This same Zapier automation is what you'll keep building on in Steps 11, 12, and 13.

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/3d785a16f6834c2d847c7069147045de0f001a9b93a04436b36f0e6fed2437e4.png)

### Prerequisites

- [Step #10A: Post-Call Follow Up Flow](https://www.skool.com/leadgenerationacademy/classroom/ff36840f?md=1664da623aa544a2b921c81d2c771598) (Funnel Emails Course)
- [Step #2: CRM](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=868dc5749079446eb83660516b92dd8a) (Current Course)

### Links

- [Zapier](https://zapier.com)
- [Read AI](https://www.read.ai)
- [Fathom](https://fathom.video)
- [Close](https://www.close.com)
- [Kit](https://kit.com)

### Step-by-Step Instructions

1. **Create a "Closed Lost" tag in your email platform.** This tag is what starts your Follow Up Flow, so it needs to exist before you build anything else.
2. **Create a new automation inside your email platform, set the trigger to Tag Is Added, then select the "Closed Lost" tag.** This has to match exactly. It's the same tag Zapier applies later in this build.
3. **Add an action step to enroll the subscriber into your Follow Up Flow, then confirm the automation is set to Active.** An automation left inactive will not enroll anyone, even if it's built correctly.
4. **Log in to Zapier, then click Create, then click Zaps.** Sign up if you don't already have an account. This is where the rest of this build happens, and where Steps #11 through #13 will keep adding on.
5. **Set your Call Summary software (e.g. Read AI, Fathom) as the trigger app, set the trigger event to the one that fires when new meeting notes are ready (e.g. New Meeting Notes in Read AI), then connect your account.** This fires the automation the moment a new meeting summary is created, whether that call went well or fell apart in the first two minutes.
6. **Click Continue, then click Test trigger and select a recent meeting note record.** Zapier will load up to 3 recent records that haven't appeared previously. Click Find new records if you need a fresher one, then select one and click Continue with selected record.
7. **Click the + button to add an action step.** Set Close as the action app, set the action event to Find Lead, then connect your account. This searches your CRM for the lead that matches the person on the call.
8. **Insert the participant's Email into the Email field.** Click into the Email field, click the + button or press "/" to open Insert Data, go to Previous Steps, and select the prospect's email field from Step 1. Leave Company Name, Company Name Matching, Company URL, Phone, and Lead ID blank. Email is the only search field you need here.
9. **Check the "Create Close Lead if it doesn't exist yet?" box.** If the person on the call isn't in your CRM yet, Close creates the lead for them instead of the rest of the Zap having nothing to update.
10. **Insert the participant's Name into the Contact Name field and the participant's Email into the Contact Direct Email field.** Use the prospect's name and email fields from Step 1. Leave the rest of the fields in the Create section blank.
11. **Click the + button to add an action step.** Set Close as the action app, set the action event to Find Opportunities, then connect your account if you haven't already. This finds the opportunity attached to the lead from the previous step, which is what gets its status changed later in this build.
12. **Insert the Lead Id from Step 2 into the Lead field.** Click into the Lead field, click the + button or press "/" to open Insert Data, go to Previous Steps, and select Contacts [0] > Lead Id from Step 2 (Find Lead in Close). Leave Contact ID and Opportunity ID blank.
13. **Check the "Create Close Opportunity if it doesn't exist yet?" box, then set the Status dropdown to "Call Completed".** If the lead doesn't have an opportunity yet, Close creates one with a "Call Completed" status so the Update Opportunity steps below always have something to update.
14. **Add a Paths step.** You're only building Path A right now, but this is what lets [Step #13: No Call Summary > No Show Flow](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=d40812de91b64fd88b32f743dd94febb) split off the no-summary calls without you having to rebuild anything you already made.
15. **Inside Path A, set the condition so it only continues when the Summary field exists.** Set the rule type to Custom rules. Click Choose field and select the summary field from Step 1 under Previous Steps. Click Choose condition and select Exists.
16. **Click the + button to add an action step.** Set Close as the action app, set the action event to Update Opportunity, then connect your account if you haven't already. This updates the opportunity status, which is the status your database automation from Step #4 watches for.
17. **Insert the ID from Step 3 into the Opportunity ID field.** Click into the Opportunity ID field, click the + button or press "/" to open Insert Data, go to Previous Steps, and select ID from Step 3 (Find Opportunities in Close).
18. **Set the Status dropdown to "Closed Lost".** Leave Assigned to User, Contact ID, Confidence, and every other field blank.
19. **Click the + button to add an action step.** Set your email platform (e.g. Kit) as the action app, set the action event to Add Tag to Subscriber, then connect your account. This is the specific action that enrolls the subscriber into the email platform automation you built in step 2.
20. **Set the Tag field to "Closed Lost".** This has to match the exact tag your email platform automation is watching for.
21. **Insert the participant's Email, First Name, and Last Name into the Email, First Name, and Last Name fields, not the call owner's.** Click into each field, then click the + button or press "/" and insert the prospect's email, first name, and last name fields from Step 1. Do not type these in manually. Typed text won't pull real data. Leave every other field blank.
22. **Test every step you just built in this path.** Confirm Find Lead finds the right lead, Find Opportunities finds the right opportunity, the opportunity status actually updates, and the tag applies correctly, all from the same test record.
23. **Check your CRM and your email platform to confirm the opportunity status and tag both updated correctly from the test.** Two systems are getting updated here, and it's easy to confirm one and assume the other worked.
24. **Confirm the Follow Up Flow sequence actually started sending.** This proves the tag correctly triggered the automation you built inside your email platform, proving the whole chain works end to end.
25. **If the prospect closes, update their opportunity status to "Closed Won" in your CRM, then open their subscriber profile in your email platform and remove them from every sequence they're in.** This automation only knows how to mark someone Closed Lost. It has no way of knowing when a prospect actually buys, whether that happens right on the call or weeks later. The subscriber profile shows every sequence they're in, so you can remove them from all of them in one place.
26. **Continue to [Step #11: Call Summary > Slack Notification](https://www.skool.com/leadgenerationacademy/classroom/0a453095?md=4d84eae5e11647a690c32ffead493a6c) to keep building this automation.** Don't publish yet. You'll publish the whole Zap once at the end of Step #13.

### Completion Audit

- Did you create a "Closed Lost" tag in your email platform?
- Did you create a new automation inside your email platform, set the trigger to Tag Is Added, and select the "Closed Lost" tag?
- Did you add an action step to enroll the subscriber into your Follow Up Flow and confirm the automation is set to Active?
- Did you log in to Zapier, then click Create, then click Zaps?
- Did you set your Call Summary software as the trigger app, set the trigger event to new meeting notes, and connect your account?
- Did you click Continue, then click Test trigger and select a recent meeting note record?
- Did you add an action step, set Close as the action app, set the action event to Find Lead, and connect your account?
- Did you insert the participant's Email into the Email field?
- Did you check the "Create Close Lead if it doesn't exist yet?" box?
- Did you insert the participant's Name into Contact Name and the participant's Email into Contact Direct Email?
- Did you add an action step, set Close as the action app, set the action event to Find Opportunities, and connect your account?
- Did you insert the Lead Id from Step 2 into the Lead field?
- Did you check the "Create Close Opportunity if it doesn't exist yet?" box and set the Status to "Call Completed"?
- Did you add a Paths step?
- Did you set Path A's condition to only continue when the Summary field exists?
- Did you add an action step, set Close as the action app, set the action event to Update Opportunity, and connect your account?
- Did you insert the ID from Step 3 into the Opportunity ID field?
- Did you set the Status to "Closed Lost"?
- Did you add an action step, set your email platform as the action app, set the action event to Add Tag to Subscriber, and connect your account?
- Did you set the Tag field to "Closed Lost"?
- Did you insert the participant's Email, First Name, and Last Name, not the call owner's?
- Did you test every step in this path?
- Did you confirm your CRM and your email platform both updated correctly from the test?
- Did you confirm the Follow Up Flow sequence actually started sending?
- Did you update the opportunity status to "Closed Won" and remove anyone who closes from every sequence they're in?
- Did you continue to Step #11: Call Summary > Slack Notification?
